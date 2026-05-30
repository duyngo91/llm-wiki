"""Dashboard: count specs by frontmatter status per feature group.

Reads `wiki/<project>/features/*.md`, parses frontmatter, classifies:
- partial_read=true: stub (chưa refine)
- partial_read=false + verification_status=Pending: refined, chưa spec-verify
- verification_status=Verified: spec-verify PASS
- verification_status=Stale: spec-verify FAIL hoặc source_version lệch

Output: markdown table grouped by feature_group tag (qa/feature-group/<name>).

Usage:
    py .claude/scripts/spec_status_dashboard.py --project project_hasaki
    py .claude/scripts/spec_status_dashboard.py --project project_hasaki --json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" not in line or line.lstrip().startswith("-"):
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def extract_feature_group(tags_line: str) -> str:
    """Parse `tags: [qa/requirement, qa/feature-group/receiving_po]` → 'receiving_po'."""
    if not tags_line:
        return "(unknown)"
    for token in tags_line.replace("[", "").replace("]", "").split(","):
        token = token.strip()
        if token.startswith("qa/feature-group/"):
            return token.split("/", 2)[-1]
    return "(unknown)"


def classify(fm: dict[str, str]) -> str:
    pr = fm.get("partial_read", "").lower()
    vs = fm.get("verification_status", "")
    if pr == "true":
        return "stub"
    if vs == "Verified":
        return "verified"
    if vs == "Stale":
        return "stale"
    if pr == "false" and vs == "Pending":
        return "refined_pending"
    return "other"


def main() -> int:
    parser = argparse.ArgumentParser(description="Dashboard specs by frontmatter status")
    parser.add_argument("--project", default="project_hasaki")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of table")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    features_dir = root / "wiki" / args.project / "features"
    if not features_dir.exists():
        print(f"ERR: features dir not found: {features_dir}", file=sys.stderr)
        return 1

    rows: list[dict[str, str]] = []
    for spec_path in sorted(features_dir.glob("*.md")):
        text = spec_path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        rows.append({
            "spec": spec_path.stem,
            "group": extract_feature_group(fm.get("tags", "")),
            "status": classify(fm),
            "source_version": fm.get("source_version", ""),
            "last_verified_at": fm.get("last_verified_at", ""),
        })

    if args.json:
        print(json.dumps({"project": args.project, "specs": rows}, ensure_ascii=False, indent=2))
        return 0

    # Summary by status
    by_status: dict[str, int] = {}
    for r in rows:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1

    print(f"# Spec Status Dashboard — {args.project}")
    print(f"\nTotal specs: {len(rows)}\n")
    print("## Summary by status\n")
    print("| Status | Count |")
    print("|:-------|:------|")
    status_order = ["stub", "refined_pending", "verified", "stale", "other"]
    for s in status_order:
        if s in by_status:
            print(f"| {s} | {by_status[s]} |")
    print()

    # By group + status
    by_group: dict[str, dict[str, list[str]]] = {}
    for r in rows:
        by_group.setdefault(r["group"], {}).setdefault(r["status"], []).append(r["spec"])

    print("## By feature group\n")
    print("| Group | stub | refined_pending | verified | stale | total |")
    print("|:------|:----:|:---------------:|:--------:|:-----:|:-----:|")
    for group in sorted(by_group):
        counts = by_group[group]
        stub_n = len(counts.get("stub", []))
        pending_n = len(counts.get("refined_pending", []))
        verified_n = len(counts.get("verified", []))
        stale_n = len(counts.get("stale", []))
        total = stub_n + pending_n + verified_n + stale_n + len(counts.get("other", []))
        print(f"| {group} | {stub_n} | {pending_n} | {verified_n} | {stale_n} | {total} |")
    print()

    # Detail per group
    print("## Detail per group\n")
    for group in sorted(by_group):
        print(f"### {group}\n")
        for status in status_order:
            specs = by_group[group].get(status, [])
            if specs:
                icon = {"stub": "📝", "refined_pending": "🔄", "verified": "✅", "stale": "⚠️", "other": "❓"}.get(status, "•")
                print(f"**{icon} {status}** ({len(specs)}):")
                for s in sorted(specs):
                    print(f"- {s}")
                print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
