"""Pretty-print non-OK findings from `source_refs_report.json` for fast phantom diagnosis.

When `check_ingest.py` exits 2, refiner sessions need to inspect the report to fix
PHANTOM_EVIDENCE, INVALID_FORMAT, OUT_OF_RANGE, etc. This script groups by spec,
shows preview snippets, and suggests common fixes (shift +1 for PDF table row,
escape `|` for INVALID_FORMAT, etc.).

Usage:
    py .claude/scripts/refiner_findings_diag.py --project project_hasaki
    py .claude/scripts/refiner_findings_diag.py --project project_hasaki --json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


SUGGESTIONS = {
    "PHANTOM_EVIDENCE": (
        "Check preview — if first line is blank/footer/heading, shift source range "
        "start +1 to next content line. If line is a PDF table row mash (numbered "
        "step + title + description on one line), shift +1 to continuation line."
    ),
    "INVALID_FORMAT": (
        "Source cell doesn't match `doc#L{start}-L{end}`. Common cause: claim_text "
        "contains `|` or `\\|` which breaks markdown table parser. Replace pipe with "
        "comma or slash in claim_text."
    ),
    "OUT_OF_RANGE": (
        "Line range exceeds raw file length. Check raw file line count; correct "
        "the range upper bound."
    ),
    "RAW_NOT_FOUND": (
        "No raw file matches the doc short name. Verify raw file exists at "
        "`raw_sources/<project>/requirements/<doc>*.md`."
    ),
    "STALE": (
        "Raw `source_version` in index differs from spec `source_version`. Re-verify "
        "claim against latest raw and update spec `source_version` or re-ingest."
    ),
    "MISSING_SOURCE": (
        "Source column is empty. Add a `doc#L{start}-L{end}` reference for the claim "
        "or remove the claim if it cannot be sourced."
    ),
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Diagnose source_refs_report findings")
    parser.add_argument("--project", default="project_hasaki")
    parser.add_argument("--json", action="store_true")
    parser.add_argument(
        "--include-ok", action="store_true", help="Include OK_CANONICAL findings (debug)"
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    report_path = root / "wiki" / args.project / "refiner" / "source_refs_report.json"
    if not report_path.exists():
        print(f"ERR: report not found: {report_path}", file=sys.stderr)
        print("Run `py .claude/scripts/check_ingest.py --project <p>` first.", file=sys.stderr)
        return 1

    data = json.loads(report_path.read_text(encoding="utf-8"))
    findings = data.get("findings", [])
    if not args.include_ok:
        findings = [f for f in findings if f.get("verdict") != "OK_CANONICAL"]

    if args.json:
        print(json.dumps({"summary": data.get("summary", {}), "findings": findings}, ensure_ascii=False, indent=2))
        return 0

    # Group by spec
    by_spec: dict[str, list[dict]] = {}
    for f in findings:
        spec = f.get("spec_file", "(unknown)").split("/")[-1]
        by_spec.setdefault(spec, []).append(f)

    print(f"# Findings Diagnostic — {args.project}")
    print(f"\n**Report generated:** {data.get('generated_at', 'unknown')}")
    print(f"\n**Summary:**")
    for verdict, count in data.get("summary", {}).items():
        if verdict != "OK_CANONICAL" or args.include_ok:
            print(f"- `{verdict}`: {count}")

    if not by_spec:
        print("\n✅ No critical findings — pipeline is clean.")
        return 0

    print(f"\n**Specs with issues:** {len(by_spec)}\n")

    for spec, fs in sorted(by_spec.items()):
        print(f"## {spec}\n")
        # Sort by spec_line then claim_id
        for f in sorted(fs, key=lambda x: (x.get("spec_line", 0), x.get("claim_id", ""))):
            verdict = f.get("verdict", "?")
            preview = f.get("preview", [])
            preview_str = " / ".join(preview[:2]) if preview else "(no preview)"
            print(f"- **{f.get('claim_id', '?')}** at spec L{f.get('spec_line', '?')}  ")
            print(f"  - Source cell: `{f.get('raw_cell', '?')}`")
            print(f"  - Verdict: **`{verdict}`** — {f.get('reason', '')}")
            if preview:
                snippet = preview[0][:80] + ("..." if len(preview[0]) > 80 else "")
                print(f"  - Preview L{f.get('source_line_start', '?')}: `{snippet}`")
            suggestion = SUGGESTIONS.get(verdict)
            if suggestion:
                print(f"  - 💡 Fix: {suggestion}")
            print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
