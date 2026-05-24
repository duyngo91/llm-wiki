import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from hasaki_client import HasakiClient, load_token, TOKEN_PATH


WIKI_TZ = ZoneInfo("Asia/Ho_Chi_Minh")


class MyOpenTaskSync:
    def __init__(self, vault_root: Path):
        self.vault_root = vault_root
        self.raw_tasks_dir = vault_root / "raw_sources" / "project_hasaki" / "tasks"
        self.raw_assets_dir = vault_root / "raw_sources" / "project_hasaki" / "assets"
        self.task_specs_dir = vault_root / "wiki" / "project_hasaki" / "task_specs"
        self.features_dir = vault_root / "wiki" / "project_hasaki" / "features"
        self.feature_groups_dir = vault_root / "wiki" / "project_hasaki" / "feature_groups"
        self.traceability_path = vault_root / "wiki" / "project_hasaki" / "traceability.json"
        self.registry_path = vault_root / "wiki" / "project_hasaki" / "project_registry.json"
        self.kanban_path = vault_root / "KANBAN.md"
        self.log_path = vault_root / "log.md"

    def now_text(self) -> str:
        return datetime.now(WIKI_TZ).strftime("%Y-%m-%d %H:%M:%S")

    def now_iso(self) -> str:
        return datetime.now(WIKI_TZ).isoformat(timespec="seconds")

    def log_event(self, action_type: str, message: str, dry_run: bool):
        if dry_run:
            return
        if not self.log_path.exists():
            return
        entry = f"- [{self.now_text()}] [{action_type}] | {message}\n"
        lines = self.log_path.read_text(encoding="utf-8").splitlines(keepends=True)
        fm_end = -1
        fm_count = 0
        for idx, line in enumerate(lines):
            if line.strip() == "---":
                fm_count += 1
                if fm_count == 2:
                    fm_end = idx
                    break
        if fm_end != -1:
            lines.insert(fm_end + 1, "\n" + entry)
        else:
            lines.insert(0, entry)
        self.log_path.write_text("".join(lines), encoding="utf-8")

    def extract_related_codes(self, text: str):
        hsk = set(re.findall(r"\bHSK-[A-Z0-9]+\b", text or "", flags=re.IGNORECASE))
        tbb2 = set(re.findall(r"\bTBB2-[A-Z0-9]+\b", text or "", flags=re.IGNORECASE))
        return sorted(code.upper() for code in hsk), sorted(code.upper() for code in tbb2)

    def infer_task_kind(self, code: str) -> str:
        upper = (code or "").upper()
        if upper.startswith("HSK-"):
            return "hsk"
        if upper.startswith("TBB2-"):
            return "tbb2"
        return "unknown"

    def discover_feature_links(self, text: str):
        text_low = (text or "").lower()
        candidates = []
        for feature_file in sorted(self.features_dir.glob("*.md")):
            stem = feature_file.stem
            tokens = stem.replace("hasaki_", "").split("_")
            score = sum(1 for t in tokens if t and t in text_low)
            if score > 0:
                candidates.append((score, stem))
        candidates.sort(reverse=True)
        selected = [name for _, name in candidates[:3]]
        links = [f"wiki/project_hasaki/features/{name}.md" for name in selected]
        group_links = []
        for group_file in sorted(self.feature_groups_dir.glob("*.md")):
            group_name = group_file.stem
            if any(group_name.split("_")[0] in name for name in selected):
                group_links.append(f"wiki/project_hasaki/feature_groups/{group_name}.md")
        if not group_links and ("receiving" in text_low or "po" in text_low):
            default_group = self.feature_groups_dir / "receiving_po.md"
            if default_group.exists():
                group_links.append("wiki/project_hasaki/feature_groups/receiving_po.md")
        return links, sorted(set(group_links))

    def build_raw_frontmatter(self, task_code: str, task_kind: str, hsk_codes, tbb2_codes, feature_links, group_links):
        tags = ["hasaki-task", "raw-source", task_kind]
        for g in group_links:
            slug = Path(g).stem.replace("_", "-")
            tags.append(f"feature-group/{slug}")
        for f in feature_links:
            tags.append(f"feature/{Path(f).stem}")
        tags_joined = ", ".join(tags)
        return "\n".join([
            "---",
            f"tags: [{tags_joined}]",
            f"task-code: {task_code}",
            "project: project_hasaki",
            f"task-kind: {task_kind}",
            f"parent-hsk: {hsk_codes[0] if hsk_codes else ''}",
            f"related-hsk: {hsk_codes}",
            f"related-tbb2: {tbb2_codes}",
            f"related-feature-group: {group_links}",
            f"related-features: {feature_links}",
            "qa-status: Questions Open",
            "---",
            "",
        ])

    def append_raw_snapshot(self, task: dict, subtasks: list, comments: list, resolved_hsk_codes, dry_run: bool):
        code = (task.get("code") or "UNKNOWN").upper()
        task_kind = self.infer_task_kind(code)
        note = task.get("note") or ""
        task_text = "\n".join([
            task.get("name") or "",
            note,
            "\n".join((st.get("name") or "") for st in subtasks),
        ])
        hsk_codes, tbb2_codes = self.extract_related_codes(task_text)
        if resolved_hsk_codes:
            hsk_codes = sorted(set(hsk_codes + [c.upper() for c in resolved_hsk_codes]))
        if task_kind == "hsk" and code not in hsk_codes:
            hsk_codes = sorted(set(hsk_codes + [code]))
        if task_kind == "tbb2" and code not in tbb2_codes:
            tbb2_codes = sorted(set(tbb2_codes + [code]))

        feature_links, group_links = self.discover_feature_links(task_text)

        out = self.raw_tasks_dir / f"{code}.md"
        snap_json = {
            "synced_at": self.now_iso(),
            "task": task,
            "subtasks": subtasks,
            "comments_count": len(comments),
            "resolved_hsk_codes": hsk_codes,
            "resolved_tbb2_codes": tbb2_codes,
            "related_feature_group": group_links,
            "related_features": feature_links,
        }
        snapshot_block = "\n".join([
            f"## Snapshot {self.now_text()}",
            "",
            "```json",
            json.dumps(snap_json, ensure_ascii=False, indent=2),
            "```",
            "",
            "## Questions",
            "",
            "| Q-ID | Linked Ref | Question | Ask To | Status | Answer | Source | Answered At |",
            "|------|------------|----------|--------|--------|--------|--------|-------------|",
            "| Q-001 | TBD | Clarify missing business behavior from this task before generating blocked testcases | BA/PO | Open | | | |",
            "",
            "## Changelog",
            "",
            f"| {self.now_text()} | snapshot-appended | Auto sync my open tasks | Hasaki API |",
            "",
        ])

        if dry_run:
            return {
                "path": str(out.relative_to(self.vault_root)).replace("\\", "/"),
                "exists": out.exists(),
                "task_kind": task_kind,
                "feature_links": feature_links,
                "group_links": group_links,
                "hsk_codes": hsk_codes,
                "tbb2_codes": tbb2_codes,
            }

        self.raw_tasks_dir.mkdir(parents=True, exist_ok=True)
        if not out.exists():
            out.write_text(self.build_raw_frontmatter(code, task_kind, hsk_codes, tbb2_codes, feature_links, group_links), encoding="utf-8")
        with out.open("a", encoding="utf-8") as f:
            f.write(snapshot_block)
        return {
            "path": str(out.relative_to(self.vault_root)).replace("\\", "/"),
            "exists": True,
            "task_kind": task_kind,
            "feature_links": feature_links,
            "group_links": group_links,
            "hsk_codes": hsk_codes,
            "tbb2_codes": tbb2_codes,
        }

    def upsert_task_spec(self, tbb2_code: str, hsk_code: str, task_name: str, assignees: list, milestone: str, feature_links: list, group_links: list, dry_run: bool):
        path = self.task_specs_dir / f"task_{tbb2_code.lower().replace('-', '_')}.md"
        linked_features = "\n".join([f"- [[{item[:-3]}|{Path(item).stem}]]" for item in feature_links]) or "- TBD"
        linked_groups = "\n".join([f"- [[{item[:-3]}|{Path(item).stem}]]" for item in group_links]) or "- TBD"
        assignee_text = ", ".join([a.get("staff_name", "") for a in assignees if isinstance(a, dict)]) or "Unknown"
        content = "\n".join([
            "---",
            "tags: [qa/task-spec, project_hasaki]",
            "status: Draft",
            "project: project_hasaki",
            f"tbb2_code: {tbb2_code}",
            f"hsk_code: {hsk_code or ''}",
            "---",
            "",
            f"# Task Spec {tbb2_code}",
            "",
            "## Metadata",
            "",
            f"- TBB2: `{tbb2_code}`",
            f"- HSK: `{hsk_code or 'TBD'}`",
            f"- Name: {task_name}",
            f"- Assignee: {assignee_text}",
            f"- Milestone: {milestone or 'N/A'}",
            f"- Updated At: {self.now_text()}",
            "",
            "## Linked Raw Tasks",
            "",
            f"- [[raw_sources/project_hasaki/tasks/{tbb2_code}|{tbb2_code}]]",
            f"- [[raw_sources/project_hasaki/tasks/{hsk_code}|{hsk_code}]]" if hsk_code else "- HSK unresolved",
            "",
            "## Linked Feature Group",
            "",
            linked_groups,
            "",
            "## Linked Feature Specs",
            "",
            linked_features,
            "",
            "## Clarification Questions",
            "",
            "| Q-ID | Linked Ref | Question | Ask To | Status | Answer | Source | Answered At |",
            "|------|------------|----------|--------|--------|--------|--------|-------------|",
            "| Q-001 | TBD | Confirm business behavior not explicit in HSK/task note | BA/PO | Open | | | |",
            "",
            "## Impact Summary",
            "",
            "- Existing Flow Impact: TBD (update after requirement analysis)",
            "- Regression Proposal: TBD",
            "",
            "## Testcase Delta Summary",
            "",
            "- Clear parts: to be generated from explicit requirement/AC only",
            "- Unclear parts: move to Blocked Coverage (no testcase until answered)",
            "",
            "## Changelog",
            "",
            f"| {self.now_text()} | v0.1 | Auto upsert from sync my open tasks | Hasaki API |",
            "",
        ])

        if dry_run:
            return str(path.relative_to(self.vault_root)).replace("\\", "/")

        self.task_specs_dir.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return str(path.relative_to(self.vault_root)).replace("\\", "/")

    def update_traceability(self, records: list, dry_run: bool):
        payload = {}
        if self.traceability_path.exists():
            payload = json.loads(self.traceability_path.read_text(encoding="utf-8"))
        payload.setdefault("project_id", "project_hasaki")
        payload["generated_at"] = self.now_iso()
        payload.setdefault("test_cases", [])
        payload.setdefault("blocked_coverage", [])
        payload.setdefault("task_spec_links", [])

        existing = {
            (item.get("tbb2"), item.get("hsk"), item.get("task_spec"))
            for item in payload.get("task_spec_links", [])
        }
        for record in records:
            key = (record.get("tbb2"), record.get("hsk"), record.get("task_spec"))
            if key in existing:
                continue
            payload["task_spec_links"].append(record)
            existing.add(key)

        if dry_run:
            return payload

        self.traceability_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return payload

    def update_registry(self, records: list, dry_run: bool):
        payload = {}
        if self.registry_path.exists():
            payload = json.loads(self.registry_path.read_text(encoding="utf-8"))
        payload.setdefault("project_id", "project_hasaki")
        payload.setdefault("project_name", "Hasaki")
        payload.setdefault("status", "active")
        payload.setdefault("timezone", "Asia/Saigon")
        payload.setdefault("knowledge_scope", {})
        payload.setdefault("raw_sources", [])
        payload.setdefault("task_spec_registry", [])

        existing = {item.get("tbb2") for item in payload.get("task_spec_registry", [])}
        for record in records:
            tbb2 = record.get("tbb2")
            if tbb2 in existing:
                continue
            payload["task_spec_registry"].append(record)
            existing.add(tbb2)

        if dry_run:
            return payload

        self.registry_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return payload

    def upsert_kanban_card(self, tbb2_code: str, hsk_code: str, task_spec_path: str, suite_hint: str, dry_run: bool):
        line = (
            f"- [ ] [[raw_sources/project_hasaki/tasks/{tbb2_code}|{tbb2_code}]] -> "
            f"[[raw_sources/project_hasaki/tasks/{hsk_code}|{hsk_code}]] -> "
            f"[[{task_spec_path[:-3]}|Task Spec]] -> "
            f"[[wiki/project_hasaki/test_suites/{suite_hint}|{suite_hint}]] [High]"
        )
        if dry_run:
            return line
        if not self.kanban_path.exists():
            return line
        text = self.kanban_path.read_text(encoding="utf-8")
        if tbb2_code in text:
            return line
        marker = "## TODO"
        if marker in text:
            text = text.replace(marker, marker + "\n\n" + line, 1)
        else:
            text += "\n\n## TODO\n\n" + line + "\n"
        self.kanban_path.write_text(text, encoding="utf-8")
        return line

    def resolve_hsk_for_task(self, client: HasakiClient, task: dict):
        code = (task.get("code") or "").upper()
        if code.startswith("HSK-"):
            return code, None
        note = task.get("note") or ""
        hsk_codes, _ = self.extract_related_codes(note)
        if hsk_codes:
            return hsk_codes[0], None
        parent_id = task.get("parent_id")
        if parent_id:
            try:
                parent = client.get_task(int(parent_id))
                parent_code = (parent.get("code") or "").upper()
                if parent_code.startswith("HSK-"):
                    return parent_code, parent
            except Exception:
                pass
        return "", None

    def run(self, limit: int, with_images: bool, dry_run: bool):
        token = load_token()
        if not token:
            raise RuntimeError(f"Token not found. Please update: {TOKEN_PATH}")
        client = HasakiClient(token)
        if not client.validate_token():
            raise RuntimeError("Token expired/invalid. Please refresh token.txt")

        tasks = client.get_my_tasks(status="_00_01", limit=limit)
        details = []
        for task in tasks:
            details.append(client.get_task(task["id"]))

        if with_images:
            self.raw_assets_dir.mkdir(parents=True, exist_ok=True)

        summary_records = []
        raw_results = []
        task_spec_paths = []
        kanban_lines = []

        for task in details:
            code = (task.get("code") or "").upper()
            hsk_code, parent_hsk_task = self.resolve_hsk_for_task(client, task)
            subtasks = []
            comments = client.get_task_comments(task["id"])
            project_id = task.get("prid")
            milestone_id = (task.get("milestone") or {}).get("id")
            if project_id and milestone_id:
                try:
                    subtasks = client.get_subtasks(task["id"], project_id, milestone_id)
                except Exception:
                    subtasks = []

            if with_images and not dry_run and task.get("note_files"):
                client.download_task_images(task.get("note_files") or [], str(self.raw_assets_dir))

            if parent_hsk_task:
                self.append_raw_snapshot(parent_hsk_task, [], [], [hsk_code], dry_run)

            raw_info = self.append_raw_snapshot(task, subtasks, comments, [hsk_code] if hsk_code else [], dry_run)
            raw_results.append(raw_info)

            kind = raw_info["task_kind"]
            if kind == "tbb2":
                tbb2_code = code
                task_spec_path = self.upsert_task_spec(
                    tbb2_code=tbb2_code,
                    hsk_code=hsk_code,
                    task_name=task.get("name") or "",
                    assignees=task.get("assign_to_user") or [],
                    milestone=(task.get("milestone") or {}).get("name") or "",
                    feature_links=raw_info["feature_links"],
                    group_links=raw_info["group_links"],
                    dry_run=dry_run,
                )
                task_spec_paths.append(task_spec_path)
                suite_hint = "test_hasaki_receiving_po_app"
                if raw_info["feature_links"]:
                    suite_hint = "test_" + Path(raw_info["feature_links"][0]).stem
                kanban_lines.append(self.upsert_kanban_card(tbb2_code, hsk_code or "HSK-TBD", task_spec_path, suite_hint, dry_run))
                summary_records.append({
                    "tbb2": tbb2_code,
                    "hsk": hsk_code or "",
                    "task_spec": task_spec_path,
                    "feature_group": raw_info["group_links"],
                    "feature": raw_info["feature_links"],
                    "requirement_ac": [],
                    "testcase": [],
                    "source": [f"raw_sources/project_hasaki/tasks/{tbb2_code}.md"],
                    "question_status": "Open",
                })

        self.update_traceability(summary_records, dry_run)
        self.update_registry(summary_records, dry_run)

        self.log_event("task-sync", f"Sync my open tasks: fetched {len(details)} open task(s)", dry_run)
        self.log_event("task-spec-update", f"Upserted {len(task_spec_paths)} task spec file(s)", dry_run)
        self.log_event("impact-analysis", "Marked partial testcase generation rule for clear requirements only", dry_run)
        self.log_event("regression-proposal", "Recorded regression review pending for updated tasks", dry_run)

        return {
            "mode": "dry-run" if dry_run else "apply",
            "fetched": len(details),
            "raw_files": raw_results,
            "task_specs": task_spec_paths,
            "kanban_cards": kanban_lines,
            "traceability_links": len(summary_records),
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync my open Hasaki tasks into raw/task-spec/traceability")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--images", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    runner = MyOpenTaskSync(root)
    result = runner.run(limit=args.limit, with_images=args.images, dry_run=args.dry_run)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
