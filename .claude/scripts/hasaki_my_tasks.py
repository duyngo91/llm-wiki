"""
CLI: Scan and sync my Hasaki Workplace tasks.

HSK-xxxxx = parent task (requirement/feature)
TBB2-xxxxx = test request linked to an HSK parent via parent_id

Usage:
  python hasaki_my_tasks.py                         # Scan + diff, dry-run
  python hasaki_my_tasks.py --download              # Download all new/updated HSK tasks
  python hasaki_my_tasks.py --download HSK-40187ZYO # Download one HSK task
  python hasaki_my_tasks.py --check-updates         # Quick summary only
  python hasaki_my_tasks.py --json                  # Machine-readable JSON
  python hasaki_my_tasks.py --status all            # Include done tasks
  python hasaki_my_tasks.py --limit 200             # Max tasks to fetch

Exit codes: 0=ok, 1=error, 2=token expired
"""

import sys
import io
import re
import json
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path

if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent))
from hasaki_client import HasakiClient, load_token, TOKEN_PATH

TZ_VN = timezone(timedelta(hours=7))
RAW_DIR_DEFAULT = Path(__file__).resolve().parents[2] / "raw_sources" / "project_hasaki" / "tasks"
WIKI_DIR = Path(__file__).resolve().parents[2] / "wiki"

STATUS_CODE_MAP = {"open": "_00_01", "done": "_02", "all": None}
STATUS_LABEL = {0: "Todo", 1: "Processing", 2: "Done"}
PRIORITY_LABEL = {0: "Normal", 1: "High", 2: "Urgent"}


# ── Helpers ───────────────────────────────────────────────────────────────────

def now_vn() -> str:
    return datetime.now(TZ_VN).strftime("%Y-%m-%d %H:%M:%S")


def is_hsk(task: dict) -> bool:
    return task.get("code", "").startswith("HSK-")


def read_raw_frontmatter(path: Path) -> dict:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    result = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            result[k.strip()] = v.strip().strip('"').strip("'")
    return result


def find_wiki_impact(hsk_code: str) -> list[str]:
    if not WIKI_DIR.exists():
        return []
    pattern = re.compile(re.escape(hsk_code), re.IGNORECASE)
    results = []
    for md_file in WIKI_DIR.rglob("*.md"):
        try:
            if pattern.search(md_file.read_text(encoding="utf-8", errors="replace")):
                results.append(str(md_file.relative_to(WIKI_DIR.parent)))
        except Exception:
            pass
    return results


# ── Grouping ──────────────────────────────────────────────────────────────────

def group_tasks(client: HasakiClient, tasks: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    Separate HSK (parent) and TBB2 (test request) tasks.
    For each TBB2: fetch full detail to get parent_id, then attach to its HSK parent.
    If the HSK parent is not in my-tasks list, fetch it separately.

    Returns:
        hsk_groups  — list of HSK task dicts, each with '_tbb2_requests' key
        orphan_tbb2 — TBB2 tasks whose HSK parent could not be resolved
    """
    hsk_by_id = {}
    tbb2_list = []

    for t in tasks:
        if is_hsk(t):
            hsk_by_id[t["id"]] = dict(t, _tbb2_requests=[])
        else:
            tbb2_list.append(t)

    if not tbb2_list:
        return list(hsk_by_id.values()), []

    orphan_tbb2 = []
    missing_parent_ids = set()

    print(f"   Đang resolve {len(tbb2_list)} TBB2 test requests...", flush=True)

    for tbb2 in tbb2_list:
        # Fetch full detail to get parent_id
        try:
            full = client.get_task(tbb2["id"])
        except Exception as e:
            print(f"   ⚠ Không fetch được TBB2 {tbb2.get('code')}: {e}", flush=True)
            orphan_tbb2.append(tbb2)
            continue

        parent_id = full.get("parent_id") or full.get("parent", {}).get("id") if isinstance(full.get("parent"), dict) else None

        if not parent_id:
            orphan_tbb2.append(full)
            continue

        if parent_id in hsk_by_id:
            hsk_by_id[parent_id]["_tbb2_requests"].append(full)
        else:
            # HSK parent not in my-tasks → need to fetch it
            missing_parent_ids.add(parent_id)
            # Temporarily store TBB2 keyed by parent_id for later attachment
            hsk_by_id.setdefault(f"__pending_{parent_id}", {
                "id": parent_id,
                "_tbb2_requests": [],
                "_fetch_parent": True,
            })["_tbb2_requests"].append(full)

    # Fetch missing HSK parents
    pending_keys = [k for k in hsk_by_id if str(k).startswith("__pending_")]
    for key in pending_keys:
        placeholder = hsk_by_id.pop(key)
        parent_id = placeholder["id"]
        try:
            print(f"   Đang fetch HSK parent (id={parent_id})...", flush=True)
            hsk_full = client.get_task(parent_id)
            hsk_full["_tbb2_requests"] = placeholder["_tbb2_requests"]
            hsk_by_id[parent_id] = hsk_full
        except Exception as e:
            print(f"   ⚠ Không fetch được HSK parent id={parent_id}: {e}", flush=True)
            for t in placeholder["_tbb2_requests"]:
                orphan_tbb2.append(t)

    return list(hsk_by_id.values()), orphan_tbb2


# ── Diff ──────────────────────────────────────────────────────────────────────

def diff_hsk_groups(hsk_groups: list[dict], raw_dir: Path) -> tuple[list, list, list]:
    """Compare HSK groups against existing raw files.
    Returns (new_groups, updated_groups, current_groups).
    """
    new_groups, updated_groups, current_groups = [], [], []

    for g in hsk_groups:
        code = g.get("code", "")
        raw_path = raw_dir / f"{code}.md"
        api_updated = g.get("updated_at", "")

        if not raw_path.exists():
            new_groups.append(g)
        else:
            fm = read_raw_frontmatter(raw_path)
            stored = fm.get("updated_at", "")
            if stored and api_updated and stored == api_updated:
                current_groups.append(g)
            else:
                g = dict(g)
                g["_old_updated_at"] = stored
                g["_wiki_impact"] = find_wiki_impact(code)
                updated_groups.append(g)

    return new_groups, updated_groups, current_groups


# ── Format & Download ─────────────────────────────────────────────────────────

def format_hsk_raw(hsk_task: dict) -> str:
    lines = []
    ts = now_vn()
    tbb2_list = hsk_task.get("_tbb2_requests", [])

    status_num = hsk_task.get("status", 0)
    assigner = hsk_task.get("created_by_user") or {}
    assignees = hsk_task.get("assign_to_user") or []
    milestone = (hsk_task.get("milestone") or {}).get("name", "")
    project_name = (hsk_task.get("project") or {}).get("name", "")

    # YAML frontmatter
    lines += [
        "---",
        "tags: [hasaki-task, raw-source]",
        f'task_id: {hsk_task.get("id")}',
        f'task_code: "{hsk_task.get("code")}"',
        f'task_name: "{hsk_task.get("name", "").replace(chr(34), chr(39))}"',
        f'project_id: {hsk_task.get("prid")}',
        f'project_name: "{project_name}"',
        f'milestone: "{milestone}"',
        f'status: {STATUS_LABEL.get(status_num, status_num)}',
        f'priority: {PRIORITY_LABEL.get(hsk_task.get("piority", 0), "Normal")}',
        f'percent_done: {hsk_task.get("percent", 0)}',
        f'planned_hours: {hsk_task.get("planned_hours", 0)}',
        f'deadline: "{hsk_task.get("date_end") or ""}"',
        f'task_created_at: "{hsk_task.get("created_at") or ""}"',
        f'updated_at: "{hsk_task.get("updated_at") or ""}"',
        f'downloaded_at: "{ts}"',
        f'assignees: "{", ".join(p.get("staff_email", "") for p in assignees)}"',
        f'created_by: "{assigner.get("staff_email", "")}"',
        f'tbb2_count: {len(tbb2_list)}',
        f'tbb2_codes: "{", ".join(t.get("code","") for t in tbb2_list)}"',
        "---",
        "",
    ]

    # Header
    lines.append(f"# {hsk_task.get('code')} — {hsk_task.get('name', '')}")
    lines.append("")
    lines.append(
        f"> **Status:** {STATUS_LABEL.get(status_num, status_num)} | "
        f"**Priority:** {PRIORITY_LABEL.get(hsk_task.get('piority', 0), 'Normal')} | "
        f"**% Done:** {hsk_task.get('percent', 0)}% | "
        f"**Deadline:** {hsk_task.get('date_end') or '—'}"
    )
    lines.append(
        f"> **Project:** {project_name} | **Milestone:** {milestone}"
    )
    lines.append(f"> **Updated:** {hsk_task.get('updated_at')}")
    lines.append(
        f"> **Người giao:** {assigner.get('staff_name', '')} <{assigner.get('staff_email', '')}>"
    )
    for p in assignees:
        lines.append(
            f"> **Assignee:** {p.get('staff_name', '')} <{p.get('staff_email', '')}> — {p.get('staff_title', '')}"
        )
    lines.append("")

    # Task content
    note = (hsk_task.get("note") or "").strip()
    lines.append("## Nội dung task (read-only)")
    lines.append("")
    lines.append(note if note else "_(Không có nội dung mô tả)_")
    lines.append("")

    # Attachments
    note_files = hsk_task.get("note_files") or []
    if note_files:
        lines.append("## Hình ảnh đính kèm")
        lines.append("")
        for f in note_files:
            lines.append(f"- https://hr-media.hasaki.vn/production/hr/{f}")
        lines.append("")

    # TBB2 test requests
    if tbb2_list:
        lines.append("## Test Requests (TBB2)")
        lines.append("")
        lines.append("| Code | Tên | Status | Updated |")
        lines.append("|------|-----|--------|---------|")
        for t in tbb2_list:
            st = STATUS_LABEL.get(t.get("status", 0), "?")
            lines.append(
                f"| {t.get('code','')} | {t.get('name','')[:80]} | {st} | {t.get('updated_at','')} |"
            )
        lines.append("")
    else:
        lines.append("## Test Requests (TBB2)")
        lines.append("")
        lines.append("_(Không có TBB2 test request nào liên kết)_")
        lines.append("")

    return "\n".join(lines)


def download_hsk_group(client: HasakiClient, group: dict, raw_dir: Path) -> Path:
    """Fetch full HSK task detail and save raw file. TBB2 list already attached."""
    task_id = group.get("id")
    code = group.get("code", f"task_{task_id}")

    # Fetch fresh full detail (list view may be incomplete)
    full_task = client.get_task(task_id)
    full_task["_tbb2_requests"] = group.get("_tbb2_requests", [])

    raw_dir.mkdir(parents=True, exist_ok=True)
    dest = raw_dir / f"{code}.md"
    dest.write_text(format_hsk_raw(full_task), encoding="utf-8")
    return dest


# ── Output formatters ─────────────────────────────────────────────────────────

def _tbb2_label(t: dict) -> str:
    name = t.get("name", "")
    # Strip "request test: " prefix if present
    name = re.sub(r"^request test:\s*", "", name, flags=re.IGNORECASE)
    return f"{t.get('code','')} — {name[:65]}"


def print_summary(new_g, updated_g, current_g, orphan_tbb2, raw_dir: Path):
    total_hsk = len(new_g) + len(updated_g) + len(current_g)
    total_tbb2 = sum(len(g.get("_tbb2_requests", [])) for g in new_g + updated_g + current_g)
    print(f"\n📋 SCAN RESULT — {now_vn()}")
    print("══════════════════════════════════════════════════")
    print(f"Tổng: {total_hsk} nhóm HSK | {total_tbb2} TBB2 test requests | Raw dir: {raw_dir}")
    print()

    if new_g:
        print(f"🆕 NEW ({len(new_g)} HSK chưa có raw file):")
        for g in new_g:
            tbb2 = g.get("_tbb2_requests", [])
            print(f"   {g.get('code')} — {g.get('name','')[:65]}")
            for t in tbb2:
                print(f"      └─ {_tbb2_label(t)}")
        print()

    if updated_g:
        print(f"🔄 UPDATED ({len(updated_g)} HSK có thay đổi):")
        for g in updated_g:
            tbb2 = g.get("_tbb2_requests", [])
            old = g.get("_old_updated_at", "?")
            new = g.get("updated_at", "?")
            print(f"   {g.get('code')} — {g.get('name','')[:60]}")
            print(f"      updated: {old} → {new}")
            for t in tbb2:
                print(f"      └─ {_tbb2_label(t)}")
            impact = g.get("_wiki_impact", [])
            if impact:
                print(f"      Wiki impact ({len(impact)} file):")
                for f in impact:
                    print(f"         • {f}")
        print()

    if current_g:
        codes = [g.get("code", "") for g in current_g]
        print(f"✅ CURRENT ({len(current_g)} HSK không đổi): {', '.join(codes)}")
        print()

    if orphan_tbb2:
        print(f"⚠️  ORPHAN TBB2 ({len(orphan_tbb2)} — không resolve được HSK parent):")
        for t in orphan_tbb2:
            print(f"   {t.get('code')} — {t.get('name','')[:65]}")
        print()

    if new_g or updated_g:
        print("👉 Chạy với --download để lưu new/updated tasks vào raw_sources/")
    else:
        print("✅ Tất cả tasks đã đồng bộ.")


def print_download_result(downloaded: list[tuple]):
    print(f"\n✅ DOWNLOAD COMPLETE — {now_vn()}")
    print("══════════════════════════════════════════════════")
    for code, path in downloaded:
        print(f"  {code} → {path}")
    print(f"\nTổng: {len(downloaded)} file(s) đã lưu.")
    print("\n⚠️  Nhắc nhở HITL Gate 1/2:")
    print("   Raw file đã cập nhật. Để update Feature Spec/Test Suite,")
    print("   chạy /wiki-requirement-analyzer sau khi PO/QA Lead duyệt.")


def json_output(new_g, updated_g, current_g, orphan_tbb2):
    def serialize(g):
        return {
            "code": g.get("code"),
            "name": g.get("name"),
            "updated_at": g.get("updated_at"),
            "old_updated_at": g.get("_old_updated_at"),
            "wiki_impact": g.get("_wiki_impact", []),
            "tbb2_requests": [
                {"code": t.get("code"), "name": t.get("name")}
                for t in g.get("_tbb2_requests", [])
            ],
        }

    print(json.dumps({
        "scanned_at": now_vn(),
        "summary": {
            "new": len(new_g), "updated": len(updated_g),
            "current": len(current_g), "orphan_tbb2": len(orphan_tbb2),
            "total_hsk": len(new_g) + len(updated_g) + len(current_g),
        },
        "new": [serialize(g) for g in new_g],
        "updated": [serialize(g) for g in updated_g],
        "current": [serialize(g) for g in current_g],
        "orphan_tbb2": [{"code": t.get("code"), "name": t.get("name")} for t in orphan_tbb2],
    }, ensure_ascii=False, indent=2))


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Scan and sync my Hasaki tasks (HSK-centric)")
    parser.add_argument("--download", nargs="?", const="all", metavar="HSK_CODE",
                        help="Download new/updated HSK tasks (or a specific HSK code)")
    parser.add_argument("--check-updates", action="store_true",
                        help="Quick summary only (no grouping detail)")
    parser.add_argument("--status", choices=["open", "done", "all"], default="open")
    parser.add_argument("--output", default=str(RAW_DIR_DEFAULT))
    parser.add_argument("--limit", type=int, default=200)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--token")
    args = parser.parse_args()

    token = args.token or load_token()
    if not token:
        print(f"ERROR: Không tìm thấy token. Paste vào: {TOKEN_PATH}")
        sys.exit(2)

    client = HasakiClient(token)
    if not client.validate_token():
        print("TOKEN HẾT HẠN hoặc không hợp lệ.")
        print("  1. Đăng nhập work.hasaki.vn")
        print("  2. F12 → Application → Cookies → wshr-token")
        print(f"  3. Paste vào: {TOKEN_PATH}")
        sys.exit(2)

    raw_dir = Path(args.output)
    status_param = STATUS_CODE_MAP.get(args.status)

    # Phase 1: Scan
    if not args.json:
        print(f"🔍 Fetch tasks (status={args.status}, limit={args.limit})...", flush=True)
    tasks = client.get_my_tasks(status=status_param, limit=args.limit)
    if not args.json:
        hsk_count = sum(1 for t in tasks if is_hsk(t))
        tbb2_count = len(tasks) - hsk_count
        print(f"   {len(tasks)} tasks: {hsk_count} HSK + {tbb2_count} TBB2", flush=True)

    # --check-updates: skip grouping, just count
    if args.check_updates:
        hsk_tasks = [t for t in tasks if is_hsk(t)]
        new_c = sum(1 for t in hsk_tasks if not (raw_dir / f"{t.get('code','')}.md").exists())
        upd_c = sum(1 for t in hsk_tasks
                    if (raw_dir / f"{t.get('code','')}.md").exists()
                    and read_raw_frontmatter(raw_dir / f"{t.get('code','')}.md").get("updated_at") != t.get("updated_at"))
        cur_c = len(hsk_tasks) - new_c - upd_c
        tbb2_c = len(tasks) - len(hsk_tasks)
        if args.json:
            print(json.dumps({"new": new_c, "updated": upd_c, "current": cur_c,
                               "tbb2_total": tbb2_c, "total_hsk": len(hsk_tasks)}))
        else:
            print(f"New: {new_c} | Updated: {upd_c} | Current: {cur_c} | HSK total: {len(hsk_tasks)} | TBB2: {tbb2_c}")
        return

    # Phase 2: Group TBB2 under HSK parents
    hsk_groups, orphan_tbb2 = group_tasks(client, tasks)

    # Phase 3: Diff
    new_g, updated_g, current_g = diff_hsk_groups(hsk_groups, raw_dir)

    if args.json and not args.download:
        json_output(new_g, updated_g, current_g, orphan_tbb2)
        return

    # Phase 4: Download
    if args.download:
        if args.download == "all":
            to_download = new_g + [
                {k: v for k, v in g.items() if not k.startswith("_old") and k != "_wiki_impact"}
                for g in updated_g
            ]
        else:
            code_target = args.download.upper()
            all_g = new_g + updated_g + current_g
            match = next((g for g in all_g if g.get("code", "").upper() == code_target), None)
            if not match:
                print(f"ERROR: HSK task '{args.download}' không tìm thấy.")
                sys.exit(1)
            to_download = [match]

        if not to_download:
            print("✅ Không có task nào cần download.")
            return

        print(f"\n⬇️  Downloading {len(to_download)} HSK task(s)...", flush=True)
        downloaded = []
        for g in to_download:
            code = g.get("code", "?")
            try:
                path = download_hsk_group(client, g, raw_dir)
                downloaded.append((code, path))
                tbb2_n = len(g.get("_tbb2_requests", []))
                print(f"   ✓ {code} ({tbb2_n} TBB2) → {path}")
            except Exception as e:
                print(f"   ✗ {code}: {e}")

        if args.json:
            print(json.dumps({"downloaded": [{"code": c, "path": str(p)} for c, p in downloaded]},
                             ensure_ascii=False, indent=2))
        else:
            print_download_result(downloaded)
    else:
        if args.json:
            json_output(new_g, updated_g, current_g, orphan_tbb2)
        else:
            print_summary(new_g, updated_g, current_g, orphan_tbb2, raw_dir)


if __name__ == "__main__":
    main()
