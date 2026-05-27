"""
index_skeleton.py — Generate a skeleton index JSON from a converted MD file.

Usage:
    py .claude/scripts/index_skeleton.py <path_to_converted.md> [--version <ver>]

Output:
    Creates {filename}_index.json next to the input file.
    Structural fields (id, title, start_line, end_line, depth) are auto-filled.
    Semantic fields (topic_types, flags, mapped_feature) are left as defaults
    for AI to fill during the ingest phase.

Strategy for WMS-style PDFs (no markdown headings):
    Pass 1 — Detect page markers: lines matching "Operation, E-commerce, ... N"
             give us page boundaries and page numbers.
    Pass 2 — For each page range, find the first substantive line
             (not empty, not table, not bullet) as the section title candidate.
    Pass 3 — Merge consecutive pages that appear to be the same section
             (no title candidate found in a page = continuation of previous).
"""

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

TZ_VN = timezone(timedelta(hours=7))

# Pattern for WMS PDF page markers (last line before new page)
PAGE_MARKER_RE = re.compile(
    r"Operation,\s*E-commerce.*?(?:POS|POS….)\s*\.?\s*(\d+)\s*$",
    re.IGNORECASE,
)

# Markdown heading (for properly formatted MD files)
MD_HEADING_RE = re.compile(r"^(#{1,4})\s+(.+)")

# Lines to skip when looking for section titles
SKIP_PATTERNS = [
    re.compile(r"^\s*$"),               # empty
    re.compile(r"^\s*\|"),              # table row
    re.compile(r"^\s*[-•–]"),           # bullet / dash
    re.compile(r"^\s*\d+[\.\)]"),       # numbered list
    re.compile(r"^---"),               # separator
    re.compile(r"Operation,.*E-commerce", re.IGNORECASE),  # page marker
    re.compile(r"^\s*[0-9]+\s*$"),      # standalone page number line
]


def is_skip_line(line: str) -> bool:
    return any(p.match(line) for p in SKIP_PATTERNS)


def is_section_title_candidate(line: str) -> bool:
    """A line is a title candidate if it's short, standalone, and not skipped."""
    stripped = line.strip()
    if not stripped or is_skip_line(stripped):
        return False
    if len(stripped) > 120:
        return False
    return True


def extract_sections_from_md_headings(lines: list[str]) -> list[dict]:
    """For properly formatted MD files with # headings."""
    headings = []
    for i, line in enumerate(lines):
        m = MD_HEADING_RE.match(line)
        if m:
            headings.append({"line": i, "depth": len(m.group(1)), "title": m.group(2).strip()})

    sections = []
    parent_stack: list[dict] = []

    for idx, h in enumerate(headings):
        start = h["line"]
        end = headings[idx + 1]["line"] - 1 if idx + 1 < len(headings) else len(lines) - 1

        # Find parent
        while parent_stack and parent_stack[-1]["depth"] >= h["depth"]:
            parent_stack.pop()
        parent_id = parent_stack[-1]["id"] if parent_stack else None

        section = _make_section(f"S-{len(sections):02d}", h["title"], start, end, h["depth"], parent_id)
        sections.append(section)
        parent_stack.append(section)

    return sections


def extract_sections_from_page_markers(lines: list[str]) -> list[dict]:
    """For WMS PDF-converted files: use page markers to find page boundaries,
    then pick the first title candidate per page as the section heading."""

    # Find page marker positions and their page numbers
    pages: list[dict] = []
    for i, line in enumerate(lines):
        m = PAGE_MARKER_RE.search(line)
        if m:
            pages.append({"marker_line": i, "page_num": int(m.group(1))})

    if not pages:
        # No page markers — fall back to naive split every ~50 lines
        return _fallback_split(lines)

    # Build page ranges: content between consecutive markers
    page_ranges: list[dict] = []
    for idx, page in enumerate(pages):
        start = pages[idx - 1]["marker_line"] + 1 if idx > 0 else 0
        end = page["marker_line"]
        page_ranges.append({
            "page_num": page["page_num"],
            "start": start,
            "end": end,
            "lines": lines[start:end],
        })

    # After last marker → trailing content
    if pages:
        trailing_start = pages[-1]["marker_line"] + 1
        if trailing_start < len(lines):
            page_ranges.append({
                "page_num": pages[-1]["page_num"] + 1,
                "start": trailing_start,
                "end": len(lines) - 1,
                "lines": lines[trailing_start:],
            })

    # For each page range, find first title candidate
    raw_sections: list[dict] = []
    for pr in page_ranges:
        title = None
        title_offset = 0
        for offset, line in enumerate(pr["lines"]):
            if is_section_title_candidate(line):
                title = line.strip()
                title_offset = offset
                break
        if title:
            raw_sections.append({
                "title": title,
                "start": pr["start"] + title_offset,
                "end": pr["end"],
                "page_num": pr["page_num"],
            })

    # Merge sections that are continuations (next page has no title candidate
    # in first 3 lines = same section continues)
    merged: list[dict] = []
    for rs in raw_sections:
        if merged and rs["page_num"] == merged[-1]["_last_page"] + 1:
            # Check if this page's title looks like a new section or a continuation
            # Heuristic: if this title is the SAME as parent section, merge
            merged[-1]["end"] = rs["end"]
            merged[-1]["_last_page"] = rs["page_num"]
        else:
            rs["_last_page"] = rs["page_num"]
            merged.append(rs)

    # Convert to section dicts
    sections = []
    for idx, s in enumerate(merged):
        section = _make_section(
            f"S-{idx:02d}",
            s["title"],
            s["start"],
            s["end"],
            1,  # depth — AI will adjust
            None,
        )
        section["_page_num"] = s["page_num"]
        sections.append(section)

    return sections


def _fallback_split(lines: list[str]) -> list[dict]:
    """Last resort: split every 50 lines."""
    sections = []
    chunk = 50
    for i in range(0, len(lines), chunk):
        title = f"Section at line {i}"
        sections.append(_make_section(
            f"S-{len(sections):02d}", title, i, min(i + chunk - 1, len(lines) - 1), 1, None
        ))
    return sections


def _make_section(sid, title, start, end, depth, parent_id) -> dict:
    return {
        "id": sid,
        "title": title,
        "start_line": start,
        "end_line": end,
        "depth": depth,
        "parent_id": parent_id,
        "topic_types": [],
        "flags": {
            "has_enum": False,
            "has_state_transition": False,
            "has_formula": False,
            "has_error_messages": False,
            "has_validation_rule": False,
        },
        "mapped_feature": None,
        "coverage_status": "unmapped",
        "last_verified_version": None,
        "change_history": [],
    }


def has_md_headings(lines: list[str]) -> bool:
    return any(MD_HEADING_RE.match(l) for l in lines[:100])


def build_index(md_path: Path, version: str) -> dict:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    if has_md_headings(lines):
        sections = extract_sections_from_md_headings(lines)
        strategy = "markdown_headings"
    else:
        sections = extract_sections_from_page_markers(lines)
        strategy = "page_markers"

    now = datetime.now(TZ_VN).strftime("%Y-%m-%dT%H:%M:%S+07:00")
    return {
        "source_file": md_path.name,
        "source_version": version,
        "last_full_index_version": version,
        "indexed_at": now,
        "total_lines": len(lines),
        "extraction_strategy": strategy,
        "note": (
            "Auto-generated skeleton. AI must fill: topic_types, flags, "
            "mapped_feature, coverage_status, last_verified_version, "
            "and verify/correct start_line/end_line where needed."
        ),
        "sections": sections,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: py index_skeleton.py <converted.md> [--version <ver>]")
        print("Example: py index_skeleton.py raw_sources/.../07062_converted.md --version ver2.17")
        sys.exit(1)

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        print(f"Error: file not found: {md_path}")
        sys.exit(1)

    version = "unknown"
    if "--version" in sys.argv:
        idx = sys.argv.index("--version")
        if idx + 1 < len(sys.argv):
            version = sys.argv[idx + 1]

    index = build_index(md_path, version)
    out_path = md_path.with_name(md_path.stem + "_index.json")

    out_path.write_text(
        json.dumps(index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    section_count = len(index["sections"])
    print(f"OK  {out_path.name}")
    print(f"    Strategy : {index['extraction_strategy']}")
    print(f"    Sections : {section_count}")
    print(f"    Lines    : {index['total_lines']}")
    print(f"    Version  : {version}")
    print()
    print("Next: open the JSON and fill topic_types, flags, mapped_feature for each section.")


if __name__ == "__main__":
    main()
