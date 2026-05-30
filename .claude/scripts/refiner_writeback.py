"""Apply spec-verifier write-back: spec frontmatter + raw_sources index.json sections.

After `hasaki-spec-verifier` produces verdict per spec, this script automates the
required write-back so refiner sessions don't have to Edit each file by hand.

Write-back fields (from .claude/skills/hasaki-spec-verifier/SKILL.md):

| File | Field | When | Value |
|:-----|:------|:-----|:------|
| Feature spec frontmatter | `last_verified_at` | Always | Now UTC+07 (or --timestamp) |
| Feature spec frontmatter | `verification_status` | PASS / CONDITIONAL | `Verified` |
| Feature spec frontmatter | `verification_status` | FAIL / source lệch | `Stale` |
| Feature spec frontmatter | `approval_note` | If --approval-note set | Provided text |
| Raw index section | `range_status` | PASS (no PHANTOM) | `verified` |
| Raw index section | `range_status` | FAIL / pending | unchanged (`needs_review`) |
| Raw index section | `last_verified_version` | PASS / CONDITIONAL | spec `source_version` |

Usage:
    py .claude/scripts/refiner_writeback.py --project project_hasaki \
        --specs stub_x,stub_y --verdict PASS
    py .claude/scripts/refiner_writeback.py --project project_hasaki \
        --specs stub_z --verdict CONDITIONAL --approval-note "FIX-001 pending"

Idempotent — re-running with same args has no effect.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

WIKI_TZ = ZoneInfo("Asia/Ho_Chi_Minh")

VERDICT_TO_STATUS = {
    "PASS": "Verified",
    "CONDITIONAL": "Verified",
    "FAIL": "Stale",
}


def now_ts() -> str:
    return datetime.now(WIKI_TZ).strftime("%Y-%m-%d %H:%M:%S")


def parse_frontmatter_bounds(text: str) -> tuple[int, int] | None:
    """Return (start, end) char indices of frontmatter content (between --- markers)."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return 4, end  # skip opening "---\n"


def update_frontmatter_field(text: str, key: str, value: str) -> str:
    """Update or insert a frontmatter field. value is a single-line string; wrap in quotes
    if it contains characters that look special to YAML."""
    bounds = parse_frontmatter_bounds(text)
    if not bounds:
        raise ValueError("No frontmatter found")
    start, end = bounds
    fm_block = text[start:end]

    # Quote value if contains : or starts with special chars
    if re.search(r"[:\#\[\]\{\}\&\*]", value) or value != value.strip():
        formatted_value = f'"{value}"'
    else:
        formatted_value = value

    pattern = re.compile(rf"^{re.escape(key)}:.*$", re.MULTILINE)
    new_line = f"{key}: {formatted_value}"

    if pattern.search(fm_block):
        new_fm = pattern.sub(new_line, fm_block, count=1)
    else:
        # Append before closing newline
        new_fm = fm_block.rstrip("\n") + "\n" + new_line + "\n"

    return text[:start] + new_fm + text[end:]


def writeback_spec(
    spec_path: Path, status: str, timestamp: str, approval_note: str | None
) -> tuple[str, str]:
    """Update spec frontmatter. Return (source_version, prev_status)."""
    text = spec_path.read_text(encoding="utf-8")

    # Extract source_version + prev verification_status for return
    bounds = parse_frontmatter_bounds(text)
    if not bounds:
        raise ValueError(f"No frontmatter in {spec_path}")
    fm_block = text[bounds[0]:bounds[1]]
    sv_match = re.search(r"^source_version:\s*(.+)$", fm_block, re.MULTILINE)
    source_version = sv_match.group(1).strip().strip('"').strip("'") if sv_match else ""
    prev_match = re.search(r"^verification_status:\s*(.+)$", fm_block, re.MULTILINE)
    prev_status = prev_match.group(1).strip() if prev_match else ""

    text = update_frontmatter_field(text, "last_verified_at", timestamp)
    text = update_frontmatter_field(text, "verification_status", status)
    # Set last_verified_source_version when verdict is Verified (PASS/CONDITIONAL).
    # When Stale, leave previous value (last successful verify version).
    if status == "Verified" and source_version:
        text = update_frontmatter_field(text, "last_verified_source_version", source_version)
    if approval_note:
        text = update_frontmatter_field(text, "approval_note", approval_note)

    spec_path.write_text(text, encoding="utf-8")
    return source_version, prev_status


def writeback_index_sections(
    project_root: Path, spec_name: str, source_version: str, mark_verified: bool
) -> dict[str, int]:
    """Update raw_sources/*/_index.json sections mapped to this spec.

    Returns counts: {'sections_updated': N, 'docs_touched': M}.
    """
    raw_root = project_root / "raw_sources"
    counts = {"sections_updated": 0, "docs_touched": 0}
    if not raw_root.exists():
        return counts

    spec_md = f"{spec_name}.md"
    for idx_path in raw_root.rglob("*_index.json"):
        data = json.loads(idx_path.read_text(encoding="utf-8"))
        changed = False
        for s in data.get("sections", []):
            if s.get("mapped_feature") == spec_md:
                if mark_verified:
                    s["range_status"] = "verified"
                s["last_verified_version"] = source_version
                changed = True
                counts["sections_updated"] += 1
        if changed:
            counts["docs_touched"] += 1
            idx_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply spec-verifier write-back")
    parser.add_argument("--project", default="project_hasaki")
    parser.add_argument("--specs", required=True, help="Comma-separated spec names (no .md)")
    parser.add_argument("--verdict", required=True, choices=["PASS", "CONDITIONAL", "FAIL"])
    parser.add_argument(
        "--timestamp",
        default=None,
        help="Override timestamp (default: now UTC+07). Format: YYYY-MM-DD HH:MM:SS",
    )
    parser.add_argument(
        "--approval-note",
        default=None,
        help="Optional approval_note text for spec frontmatter",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print planned changes, no write")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    features_dir = root / "wiki" / args.project / "features"
    if not features_dir.exists():
        print(f"ERR: features dir not found: {features_dir}", file=sys.stderr)
        return 1

    status = VERDICT_TO_STATUS[args.verdict]
    timestamp = args.timestamp or now_ts()
    mark_index_verified = args.verdict in ("PASS", "CONDITIONAL")
    spec_names = [s.strip() for s in args.specs.split(",") if s.strip()]

    if args.dry_run:
        print(f"DRY-RUN: verdict={args.verdict} → status={status}, timestamp={timestamp}")
        print(f"DRY-RUN: index sections mark_verified={mark_index_verified}")
        for name in spec_names:
            print(f"  - {name}: frontmatter update + index sections write-back")
        return 0

    summary: list[dict] = []
    for name in spec_names:
        spec_path = features_dir / f"{name}.md"
        if not spec_path.exists():
            print(f"WARN: spec not found: {spec_path}", file=sys.stderr)
            summary.append({"spec": name, "status": "SKIPPED", "reason": "spec not found"})
            continue
        source_version, prev_status = writeback_spec(spec_path, status, timestamp, args.approval_note)
        idx_counts = writeback_index_sections(root, name, source_version, mark_index_verified)
        summary.append(
            {
                "spec": name,
                "prev_status": prev_status,
                "new_status": status,
                "source_version": source_version,
                "sections_updated": idx_counts["sections_updated"],
                "docs_touched": idx_counts["docs_touched"],
            }
        )

    print(json.dumps({"verdict": args.verdict, "timestamp": timestamp, "specs": summary}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
