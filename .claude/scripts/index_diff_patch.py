"""
index_diff_patch.py — Diff two versions of a converted MD file and generate
a structured patch that tells the AI exactly what changed so it can update
the index JSON incrementally (Workflow 2.1b).

Usage:
    py .claude/scripts/index_diff_patch.py <old.md> <new.md> [--index <index.json>]

Output (stdout):
    JSON with:
      - hunks: list of change blocks (insert / delete / replace) with line ranges
      - line_shifts: cumulative line offset at each hunk — apply to sections below
      - summary: human-readable change summary

If --index is provided, also prints which index section IDs are likely affected.

Example:
    py .claude/scripts/index_diff_patch.py \\
        raw_sources/.../07062_ver2.16.md \\
        raw_sources/.../07062_ver2.17.md \\
        --index raw_sources/.../07062_ver2.16_index.json
"""

import difflib
import json
import sys
from pathlib import Path


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def compute_hunks(old_lines: list[str], new_lines: list[str]) -> list[dict]:
    """Use SequenceMatcher to find change blocks between old and new files."""
    matcher = difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False)
    hunks = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue

        old_count = i2 - i1
        new_count = j2 - j1
        line_delta = new_count - old_count  # positive = net insert, negative = net delete

        hunk = {
            "type": tag,               # "insert" | "delete" | "replace"
            "old_start": i1,           # line range in OLD file (0-indexed)
            "old_end": i2 - 1,
            "new_start": j1,           # line range in NEW file (0-indexed)
            "new_end": j2 - 1,
            "old_count": old_count,
            "new_count": new_count,
            "line_delta": line_delta,
            "preview_old": old_lines[i1:min(i1 + 3, i2)],
            "preview_new": new_lines[j1:min(j1 + 3, j2)],
        }
        hunks.append(hunk)

    return hunks


def compute_line_shifts(hunks: list[dict]) -> list[dict]:
    """For each hunk, compute the cumulative shift to apply to sections BELOW it.

    A section whose start_line > hunk.old_end should have its start_line and
    end_line adjusted by the running cumulative delta.
    """
    shifts = []
    cumulative = 0
    for h in hunks:
        cumulative += h["line_delta"]
        shifts.append({
            "after_old_line": h["old_end"],
            "cumulative_delta": cumulative,
            "caused_by": f"{h['type']} at old:{h['old_start']}-{h['old_end']}",
        })
    return shifts


def find_affected_sections(
    hunks: list[dict], index_path: Path
) -> dict[str, list[str]]:
    """Given hunks in old-file coordinates, find which section IDs overlap."""
    index = json.loads(index_path.read_text(encoding="utf-8"))
    sections = index.get("sections", [])

    affected: dict[str, list[str]] = {}  # section_id -> list of hunk types

    for h in hunks:
        for sec in sections:
            s_start = sec.get("start_line", 0)
            s_end = sec.get("end_line", 0)
            # Overlap check
            if h["old_start"] <= s_end and h["old_end"] >= s_start:
                sid = sec["id"]
                if sid not in affected:
                    affected[sid] = []
                affected[sid].append(h["type"])

    return affected


def summarise(hunks: list[dict]) -> str:
    inserts = sum(1 for h in hunks if h["type"] == "insert")
    deletes = sum(1 for h in hunks if h["type"] == "delete")
    replaces = sum(1 for h in hunks if h["type"] == "replace")
    net = sum(h["line_delta"] for h in hunks)
    return (
        f"{len(hunks)} hunks total — "
        f"{inserts} insert, {deletes} delete, {replaces} replace. "
        f"Net line delta: {net:+d}."
    )


def main():
    if len(sys.argv) < 3:
        print("Usage: py index_diff_patch.py <old.md> <new.md> [--index <index.json>]")
        sys.exit(1)

    old_path = Path(sys.argv[1])
    new_path = Path(sys.argv[2])

    index_path: Path | None = None
    if "--index" in sys.argv:
        idx = sys.argv.index("--index")
        if idx + 1 < len(sys.argv):
            index_path = Path(sys.argv[idx + 1])

    if not old_path.exists():
        print(f"Error: old file not found: {old_path}")
        sys.exit(1)
    if not new_path.exists():
        print(f"Error: new file not found: {new_path}")
        sys.exit(1)

    old_lines = read_lines(old_path)
    new_lines = read_lines(new_path)

    hunks = compute_hunks(old_lines, new_lines)
    shifts = compute_line_shifts(hunks)

    result: dict = {
        "old_file": old_path.name,
        "new_file": new_path.name,
        "old_total_lines": len(old_lines),
        "new_total_lines": len(new_lines),
        "summary": summarise(hunks),
        "hunks": hunks,
        "line_shifts": shifts,
    }

    if index_path and index_path.exists():
        affected = find_affected_sections(hunks, index_path)
        result["affected_sections"] = affected
        result["affected_count"] = len(affected)
    else:
        result["affected_sections"] = {}
        result["affected_count"] = 0
        if index_path:
            result["note"] = f"Index file not found: {index_path}"

    print(json.dumps(result, ensure_ascii=False, indent=2))

    # Also print a human-readable summary to stderr
    print(f"\n=== Diff Summary ===", file=sys.stderr)
    print(f"  {result['summary']}", file=sys.stderr)
    if result["affected_count"]:
        print(f"  Affected sections ({result['affected_count']}):", file=sys.stderr)
        for sid, types in result["affected_sections"].items():
            print(f"    {sid}: {', '.join(set(types))}", file=sys.stderr)
    print(f"\nHow to apply:", file=sys.stderr)
    print(f"  1. For each hunk: update affected sections' coverage_status → 'partial'", file=sys.stderr)
    print(f"  2. For sections BELOW each hunk: apply cumulative_delta from line_shifts", file=sys.stderr)
    print(f"  3. Add new version to change_history[] of affected sections", file=sys.stderr)
    print(f"  4. Update source_version and indexed_at in index JSON", file=sys.stderr)


if __name__ == "__main__":
    main()
