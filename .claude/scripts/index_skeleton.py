"""Generate a trace-friendly index JSON from a converted requirement MD file.

The Hasaki requirement PDFs usually become Markdown without real heading
markers. This script therefore uses multiple signals, in order:

1. Real Markdown headings, if they exist.
2. Table-of-contents entries with dotted leaders and page numbers.
3. Body heading candidates such as Update/Case/feature headings.
4. Page-marker fallback.

The goal is not to infer business meaning. The goal is to create smaller,
reviewable source ranges so the ingest/refiner steps can mark coverage,
evidence, and questions precisely.
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from datetime import datetime, timezone, timedelta
from pathlib import Path


TZ_VN = timezone(timedelta(hours=7))

PAGE_MARKER_RE = re.compile(
    r"Operation,\s*E-commerce.*?POS.*?\s+(\d+)\s*$",
    re.IGNORECASE,
)
SPLIT_POS_MARKER_RE = re.compile(r"POS.*?\s+(\d+)\s*$", re.IGNORECASE)
MD_HEADING_RE = re.compile(r"^(#{1,4})\s+(.+)")
TOC_ENTRY_RE = re.compile(r"^(?P<title>.+?)\s*\.{5,}\s*(?P<page>\d+)\s*$")
DATE_HEADING_RE = re.compile(
    r"^\s*(?:\d{2}[-/]\d{2}[-/]\d{4}|update\s+\d{2}[-/]\d{2}[-/]\d{2,4})",
    re.IGNORECASE,
)

SKIP_PATTERNS = [
    re.compile(r"^\s*$"),
    re.compile(r"^\s*\|"),
    re.compile(r"^\s*[•●]\s*"),
    re.compile(r"^\s*[-*]+$"),
    re.compile(r"^\s*\d+[\.)]\s+"),
    re.compile(r"^---"),
    re.compile(r"Operation,.*E-commerce", re.IGNORECASE),
    re.compile(r"^\s*[0-9]+\s*$"),
]

def strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def normalize_title(text: str) -> str:
    text = strip_accents(text)
    text = re.sub(r"\.{3,}\s*\d+\s*$", "", text)
    text = re.sub(r"[|•●]", " ", text)
    text = re.sub(r"\s+", " ", text.strip())
    return text.lower()


def is_skip_line(line: str) -> bool:
    return any(pattern.match(line) for pattern in SKIP_PATTERNS)


def is_section_title_candidate(line: str) -> bool:
    stripped = line.strip()
    if not stripped or is_skip_line(stripped):
        return False
    if len(stripped) > 140:
        return False
    # Dense table-ish rows are usually not headings.
    if stripped.count("  ") >= 5 and len(stripped.split()) > 10:
        return False
    return True


def title_matches(candidate: str, expected: str) -> bool:
    cand = normalize_title(candidate)
    exp = normalize_title(expected)
    if not cand or not exp:
        return False
    if cand == exp:
        return True
    return len(exp) >= 8 and (exp in cand or cand in exp)


def parse_toc_entries(lines: list[str]) -> list[dict]:
    entries: list[dict] = []
    seen: set[tuple[str, int]] = set()
    for line_no, line in enumerate(lines):
        match = TOC_ENTRY_RE.match(line.strip())
        if not match:
            continue
        title = match.group("title").strip()
        page_num = int(match.group("page"))
        if len(title) < 3 or "|" in title:
            continue
        key = (normalize_title(title), page_num)
        if key in seen:
            continue
        seen.add(key)
        entries.append({"title": title, "page_num": page_num, "toc_line": line_no})
    return entries


def page_marker_at(lines: list[str], line_no: int) -> dict | None:
    line = lines[line_no]
    if not re.search(r"Operation,\s*E-commerce", line, flags=re.IGNORECASE):
        return None

    same_line = PAGE_MARKER_RE.search(line)
    if same_line:
        return {
            "marker_line": line_no,
            "page_num": int(same_line.group(1)),
            "marker_source": "same_line_footer",
        }

    for offset in range(1, 3):
        next_line_no = line_no + offset
        if next_line_no >= len(lines):
            break
        split_pos = SPLIT_POS_MARKER_RE.search(lines[next_line_no].strip())
        if split_pos:
            return {
                "marker_line": next_line_no,
                "page_num": int(split_pos.group(1)),
                "marker_source": "split_footer",
            }

    for offset in range(1, 5):
        next_line_no = line_no + offset
        if next_line_no >= len(lines):
            break
        next_line = lines[next_line_no].strip()
        standalone = re.match(r"^(\d+)$", next_line)
        if standalone:
            return {
                "marker_line": next_line_no,
                "page_num": int(standalone.group(1)),
                "marker_source": "next_page_number",
            }
        if next_line.startswith("|"):
            numbers = re.findall(r"\b\d+\b", next_line)
            if len(numbers) == 1:
                return {
                    "marker_line": next_line_no,
                    "page_num": int(numbers[0]),
                    "marker_source": "table_page_number",
                }
    return None


def repair_page_markers(markers: list[dict]) -> list[dict]:
    repaired: list[dict] = []
    seen_marker_lines: set[int] = set()
    for marker in markers:
        marker_line = marker["marker_line"]
        if marker_line in seen_marker_lines:
            continue
        seen_marker_lines.add(marker_line)

        marker = marker.copy()
        if repaired:
            previous = repaired[-1]["page_num"]
            expected = previous + 1
            raw_page = marker["page_num"]
            low_confidence = marker.get("marker_source") in {
                "next_page_number",
                "table_page_number",
            }
            if low_confidence and raw_page != expected:
                marker["raw_page_num"] = raw_page
                marker["page_num"] = expected
                marker["marker_source"] = f"{marker['marker_source']}_inferred"
        repaired.append(marker)
    return repaired


def extract_page_ranges(lines: list[str]) -> list[dict]:
    markers = []
    for line_no, line in enumerate(lines):
        marker = page_marker_at(lines, line_no)
        if marker:
            markers.append(marker)
    markers = repair_page_markers(markers)

    if not markers:
        return []

    ranges = []
    for idx, marker in enumerate(markers):
        start = markers[idx - 1]["marker_line"] + 1 if idx > 0 else 0
        end = marker["marker_line"]
        ranges.append({"page_num": marker["page_num"], "start": start, "end": end})

    trailing_start = markers[-1]["marker_line"] + 1
    if trailing_start < len(lines):
        ranges.append(
            {
                "page_num": markers[-1]["page_num"] + 1,
                "start": trailing_start,
                "end": len(lines) - 1,
            }
        )
    return ranges


def page_num_for_line(line_no: int, page_ranges: list[dict]) -> int | None:
    for page_range in page_ranges:
        if page_range["start"] <= line_no <= page_range["end"]:
            return page_range["page_num"]
    return None


def find_title_line_for_toc(entry: dict, page_ranges: list[dict], lines: list[str]) -> int | None:
    by_page = {page_range["page_num"]: page_range for page_range in page_ranges}
    # PDF page markers are occasionally off by one, so search nearby pages too.
    for page_num in (entry["page_num"], entry["page_num"] + 1, entry["page_num"] - 1):
        page_range = by_page.get(page_num)
        if not page_range:
            continue
        for line_no in range(page_range["start"], min(page_range["end"] + 1, len(lines))):
            if title_matches(lines[line_no], entry["title"]):
                return line_no

    page_range = by_page.get(entry["page_num"])
    if page_range:
        return page_range["start"]
    return None


def looks_like_body_heading(line: str) -> bool:
    stripped = line.strip()
    if not is_section_title_candidate(stripped):
        return False
    if TOC_ENTRY_RE.match(stripped):
        return False
    normalized = normalize_title(stripped)
    if DATE_HEADING_RE.match(normalized):
        return True
    if re.match(r"^Case\s+\d+", stripped, flags=re.IGNORECASE):
        return True
    if stripped.startswith("Update "):
        return True
    if stripped.startswith("Web:"):
        return True
    return False


def section_depth(title: str) -> int:
    normalized = normalize_title(title)
    if normalized in {"tong quan", "content", "yeu cau chuc nang"}:
        return 1
    if normalized.startswith(("update", "case ", "web:")):
        return 2
    return 1


def extract_sections_from_toc(lines: list[str], page_ranges: list[dict]) -> list[dict]:
    toc_entries = parse_toc_entries(lines)
    if len(toc_entries) < 5:
        return []

    starts: list[dict] = []
    for entry in toc_entries:
        start_line = find_title_line_for_toc(entry, page_ranges, lines)
        if start_line is None or start_line <= entry["toc_line"]:
            continue
        starts.append(
            {
                "title": entry["title"],
                "start": start_line,
                "page_num": entry["page_num"],
                "source": "toc",
            }
        )

    toc_start_lines = {item["start"] for item in starts}
    first_content_line = min(toc_start_lines) if toc_start_lines else 0
    for line_no, line in enumerate(lines):
        if line_no < first_content_line:
            continue
        if line_no in toc_start_lines:
            continue
        if looks_like_body_heading(line):
            if any(abs(line_no - item["start"]) <= 2 for item in starts):
                continue
            starts.append(
                {
                    "title": line.strip(),
                    "start": line_no,
                    "page_num": page_num_for_line(line_no, page_ranges),
                    "source": "body_heading",
                }
            )

    starts.sort(key=lambda item: item["start"])

    deduped: list[dict] = []
    for item in starts:
        if deduped:
            same_title = normalize_title(item["title"]) == normalize_title(deduped[-1]["title"])
            nearby = item["start"] - deduped[-1]["start"] <= 3
            if same_title and nearby:
                continue
        deduped.append(item)

    return starts_to_sections(deduped, len(lines))


def extract_sections_from_md_headings(lines: list[str]) -> list[dict]:
    headings = []
    for line_no, line in enumerate(lines):
        match = MD_HEADING_RE.match(line)
        if match:
            headings.append(
                {
                    "title": match.group(2).strip(),
                    "start": line_no,
                    "depth": len(match.group(1)),
                    "page_num": None,
                    "source": "markdown_heading",
                }
            )
    return starts_to_sections(headings, len(lines))


def extract_sections_from_page_markers(lines: list[str]) -> list[dict]:
    page_ranges = extract_page_ranges(lines)
    if not page_ranges:
        return fallback_split(lines)

    toc_sections = extract_sections_from_toc(lines, page_ranges)
    if toc_sections:
        return toc_sections

    starts = []
    for page_range in page_ranges:
        for line_no in range(page_range["start"], min(page_range["end"] + 1, len(lines))):
            if looks_like_body_heading(lines[line_no]):
                starts.append(
                    {
                        "title": lines[line_no].strip(),
                        "start": line_no,
                        "page_num": page_range["page_num"],
                        "source": "page_heading",
                    }
                )
                break
    if not starts:
        return fallback_split(lines)
    return starts_to_sections(starts, len(lines))


def starts_to_sections(starts: list[dict], line_count: int) -> list[dict]:
    sections = []
    parent_stack: list[dict] = []
    for idx, item in enumerate(starts):
        end = starts[idx + 1]["start"] - 1 if idx + 1 < len(starts) else line_count - 1
        depth = item.get("depth") or section_depth(item["title"])
        while parent_stack and parent_stack[-1]["depth"] >= depth:
            parent_stack.pop()
        parent_id = parent_stack[-1]["id"] if parent_stack else None
        section = make_section(f"S-{idx:02d}", item["title"], item["start"], end, depth, parent_id)
        section["_page_num"] = item.get("page_num")
        section["_source"] = item.get("source", "unknown")
        section["source_page"] = item.get("page_num")
        section["source_type"] = item.get("source", "unknown")
        section["range_status"] = "needs_review"
        sections.append(section)
        parent_stack.append(section)
    return sections


def fallback_split(lines: list[str]) -> list[dict]:
    sections = []
    chunk_size = 50
    for start in range(0, len(lines), chunk_size):
        end = min(start + chunk_size - 1, len(lines) - 1)
        sections.append(make_section(f"S-{len(sections):02d}", f"Section at line {start}", start, end, 1, None))
    return sections


def make_section(sid: str, title: str, start: int, end: int, depth: int, parent_id: str | None) -> dict:
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
    return any(MD_HEADING_RE.match(line) for line in lines[:150])


def build_index(md_path: Path, version: str) -> dict:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    if has_md_headings(lines):
        sections = extract_sections_from_md_headings(lines)
        strategy = "markdown_headings"
    else:
        sections = extract_sections_from_page_markers(lines)
        strategy = "toc_page_markers" if parse_toc_entries(lines) else "page_markers"

    for section in sections:
        section["source_ref"] = (
            f"{md_path.name}#L{section['start_line'] + 1}-L{section['end_line'] + 1}"
        )

    now = datetime.now(TZ_VN).strftime("%Y-%m-%dT%H:%M:%S+07:00")
    return {
        "source_file": md_path.name,
        "source_version": version,
        "last_full_index_version": version,
        "indexed_at": now,
        "total_lines": len(lines),
        "line_numbering": "zero_based_internal; source_ref is one_based_display",
        "extraction_strategy": strategy,
        "note": (
            "Auto-generated skeleton. AI must fill topic_types, flags, mapped_feature, "
            "coverage_status, last_verified_version, and verify/correct line ranges."
        ),
        "sections": sections,
    }


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: py index_skeleton.py <converted.md> [--version <ver>]")
        return 1

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        print(f"Error: file not found: {md_path}")
        return 1

    version = "unknown"
    if "--version" in sys.argv:
        idx = sys.argv.index("--version")
        if idx + 1 < len(sys.argv):
            version = sys.argv[idx + 1]

    index = build_index(md_path, version)
    out_path = md_path.with_name(md_path.stem + "_index.json")
    out_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK  {out_path.name}")
    print(f"    Strategy : {index['extraction_strategy']}")
    print(f"    Sections : {len(index['sections'])}")
    print(f"    Lines    : {index['total_lines']}")
    print(f"    Version  : {version}")
    print()
    print("Next: fill topic_types, flags, mapped_feature, coverage_status, and last_verified_version.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
