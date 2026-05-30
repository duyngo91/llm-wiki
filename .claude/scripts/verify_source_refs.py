"""Verify Source column references in Feature Spec + API Spec against raw files.

Catches PHANTOM_EVIDENCE, OUT_OF_RANGE, STALE, INVALID_FORMAT before refiner L3 runs.

Output: `wiki/[project]/refiner/source_refs_report.json` with per-claim verdict + preview.

See `.claude/skills/hasaki-wiki/references/shared.md#source-reference-format-ssot`.
"""

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


WIKI_TZ = ZoneInfo("Asia/Ho_Chi_Minh")

# Canonical: `doc#L{start}-L{end}`. Tolerated: no-L prefix. Anything else -> INVALID_FORMAT.
CANONICAL_RE = re.compile(r"^([A-Za-z0-9_.]+)#L(\d+)(?:-L(\d+))?$")
TOLERATED_RE = re.compile(r"^([A-Za-z0-9_.]+)#(\d+)(?:-(\d+))?$")
MULTI_RANGE_SPLIT_RE = re.compile(r",\s*")

# Heading-ish lines we DON'T want a #L pointing to (PHANTOM_EVIDENCE).
# `#` markdown headings always flag. Numbered lines (`1 ...`, `2.3 ...`) get the
# heading check, but if the line clearly contains body content (':' for key:value,
# multiple sentence words, '-' for bullets) we treat it as PDF table row content
# rather than a TOC heading. Hard cap at 80 chars catches very long PDF rows; the
# content-marker check rescues shorter PDF rows that mash step+title+description.
MD_HEADING_RE = re.compile(r"^\s*#{1,6}\s")
NUMBERED_HEADING_RE = re.compile(r"^\s*[\d\.]+\s+[A-ZĐĂÂÊÔƠƯ]")
NUMBERED_HEADING_MAX_LEN = 80
# Markers that indicate body/table content rather than a heading.
CONTENT_MARKERS_RE = re.compile(r":\s\S|\s-\s|/ ")


def _looks_like_heading(line: str) -> bool:
    if MD_HEADING_RE.match(line):
        return True
    if NUMBERED_HEADING_RE.match(line):
        stripped = line.strip()
        # Long → almost certainly PDF table row content.
        if len(stripped) >= NUMBERED_HEADING_MAX_LEN:
            return False
        # Short but contains content markers → still PDF table row content.
        if CONTENT_MARKERS_RE.search(stripped):
            return False
        return True
    return False


def now_iso() -> str:
    return datetime.now(WIKI_TZ).isoformat(timespec="seconds")


def read_frontmatter(md_text: str) -> dict:
    if not md_text.startswith("---"):
        return {}
    end = md_text.find("\n---", 3)
    if end == -1:
        return {}
    data = {}
    for line in md_text[3:end].splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip().strip('"')
    return data


def find_raw_file(raw_root: Path, doc_short: str) -> Path | None:
    """Resolve `07062` -> raw_sources/.../07062_*.md (prefer _converted)."""
    if not raw_root.exists():
        return None
    candidates = list(raw_root.rglob(f"{doc_short}*.md"))
    if not candidates:
        return None
    # Prefer _converted.md
    for c in candidates:
        if "_converted" in c.name.lower():
            return c
    return candidates[0]


def load_raw_index(raw_path: Path) -> dict | None:
    """Load matching `*_index.json` for the raw file, if present."""
    idx_path = raw_path.with_name(raw_path.stem + "_index.json")
    if not idx_path.exists():
        return None
    try:
        return json.loads(idx_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def classify_ref(cell: str, raw_root: Path, spec_source_version: str) -> list[dict]:
    """Parse one Source cell, classify each ref entry, return verdict list."""
    results = []
    parts = [p.strip() for p in MULTI_RANGE_SPLIT_RE.split(cell) if p.strip()]
    if not parts:
        return [{"raw_cell": cell, "verdict": "INVALID_FORMAT", "reason": "empty cell"}]

    for part in parts:
        result = {"raw_cell": part}
        canonical = CANONICAL_RE.match(part)
        tolerated = TOLERATED_RE.match(part) if not canonical else None

        if not canonical and not tolerated:
            result["verdict"] = "INVALID_FORMAT"
            result["reason"] = "does not match `doc#L{start}-L{end}` or `doc#{start}-{end}`"
            results.append(result)
            continue

        match = canonical or tolerated
        doc_short = match.group(1)
        start_line = int(match.group(2))
        end_line = int(match.group(3)) if match.group(3) else start_line
        result.update({
            "source_doc": doc_short,
            "source_line_start": start_line,
            "source_line_end": end_line,
            "canonical": bool(canonical),
        })

        raw_path = find_raw_file(raw_root, doc_short)
        if raw_path is None:
            result["verdict"] = "RAW_NOT_FOUND"
            result["reason"] = f"no raw file matches `{doc_short}*`"
            results.append(result)
            continue

        raw_lines = raw_path.read_text(encoding="utf-8", errors="replace").splitlines()
        total = len(raw_lines)
        if start_line < 1 or end_line > total:
            result["verdict"] = "OUT_OF_RANGE"
            result["reason"] = f"range L{start_line}-L{end_line} outside file (total {total} lines)"
            results.append(result)
            continue

        # Check STALE via index version mismatch.
        idx = load_raw_index(raw_path)
        if idx and spec_source_version and idx.get("source_version") and idx["source_version"] != spec_source_version:
            result["verdict"] = "STALE"
            result["reason"] = (
                f"spec.source_version={spec_source_version!r} but index.source_version="
                f"{idx['source_version']!r}"
            )
            # Still attach preview for context.
            preview_lines = raw_lines[start_line - 1:min(end_line, total)]
            result["preview"] = preview_lines[:3]
            results.append(result)
            continue

        # Preview + phantom check.
        first_line = raw_lines[start_line - 1] if start_line - 1 < total else ""
        preview = raw_lines[start_line - 1:min(end_line, total)]
        result["preview"] = preview[:3]
        result["preview_tail"] = preview[-3:] if len(preview) > 3 else []
        if not first_line.strip():
            result["verdict"] = "PHANTOM_EVIDENCE"
            result["reason"] = f"L{start_line} is empty"
        elif _looks_like_heading(first_line):
            result["verdict"] = "PHANTOM_EVIDENCE"
            result["reason"] = f"L{start_line} looks like a heading (`{first_line.strip()[:60]}`)"
        else:
            result["verdict"] = "OK_CANONICAL" if canonical else "OK_TOLERATED"

        results.append(result)
    return results


# --- Spec scanning -------------------------------------------------

SECTION_REQUIREMENT_RE = re.compile(r"^##\s*Phân rã Requirement", re.IGNORECASE)
SECTION_API_LIST_RE = re.compile(r"^##\s*API\s*/?\s*Interface\s*List", re.IGNORECASE)


_ESCAPED_PIPE_PLACEHOLDER = "\x00PIPE\x00"


def _split_table_row(line: str) -> list[str]:
    """Split a markdown table row on `|`, honoring `\\|` escape inside cells."""
    protected = line.replace("\\|", _ESCAPED_PIPE_PLACEHOLDER)
    parts = protected.strip().split("|")[1:-1]
    return [cell.strip().replace(_ESCAPED_PIPE_PLACEHOLDER, "|") for cell in parts]


def parse_table_rows(lines: list[str], start_idx: int) -> tuple[list[tuple[int, list[str]]], int]:
    """Return rows with (line_no_in_file, cells)."""
    rows = []
    i = start_idx
    while i < len(lines):
        line = lines[i].rstrip("\n")
        if not line.startswith("|"):
            break
        if set(line.replace("|", "").replace(":", "").replace("-", "").strip()) == set():
            i += 1
            continue
        rows.append((i + 1, _split_table_row(line)))  # 1-based line in spec
        i += 1
    return rows, i


def find_header_row(lines: list[str], start_idx: int, max_scan: int = 6) -> int | None:
    for j in range(start_idx, min(start_idx + max_scan, len(lines))):
        if lines[j].lstrip().startswith("|"):
            return j
    return None


def scan_spec(spec_path: Path, raw_root: Path, vault_root: Path) -> list[dict]:
    text = spec_path.read_text(encoding="utf-8")
    frontmatter = read_frontmatter(text)
    spec_source_version = frontmatter.get("source_version", "")
    spec_rel = str(spec_path.relative_to(vault_root)).replace("\\", "/")
    lines = text.splitlines()

    findings: list[dict] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        section_kind = None
        source_col_index = None
        id_col_index = 0

        if SECTION_REQUIREMENT_RE.match(line):
            section_kind = "requirement"
            source_col_index = 5  # Source is column 6 (0-indexed 5)
        elif SECTION_API_LIST_RE.match(line):
            section_kind = "api"
            source_col_index = 5  # API List: API ID|Method|Endpoint|Mục đích|R/AC|Source|Status

        if section_kind is None:
            i += 1
            continue

        header = find_header_row(lines, i + 1)
        if header is None:
            i += 1
            continue
        rows, next_idx = parse_table_rows(lines, header + 2)
        for spec_line_no, row in rows:
            if len(row) <= source_col_index:
                continue
            claim_id = row[id_col_index] if len(row) > id_col_index else ""
            if not claim_id or claim_id.startswith(":"):
                continue
            source_cell = row[source_col_index]
            if not source_cell:
                findings.append({
                    "spec_file": spec_rel,
                    "spec_line": spec_line_no,
                    "claim_id": claim_id,
                    "section": section_kind,
                    "raw_cell": "",
                    "verdict": "MISSING_SOURCE",
                    "reason": "empty Source cell",
                })
                continue
            for entry in classify_ref(source_cell, raw_root, spec_source_version):
                findings.append({
                    "spec_file": spec_rel,
                    "spec_line": spec_line_no,
                    "claim_id": claim_id,
                    "section": section_kind,
                    **entry,
                })
        i = next_idx

    return findings


def build_report(vault_root: Path, project: str) -> dict:
    raw_root = vault_root / "raw_sources" / project / "requirements"
    features_dir = vault_root / "wiki" / project / "features"
    api_dir = vault_root / "wiki" / project / "api_specs"

    findings: list[dict] = []
    if features_dir.exists():
        for spec_path in sorted(features_dir.glob("*.md")):
            findings.extend(scan_spec(spec_path, raw_root, vault_root))
    if api_dir.exists():
        for spec_path in sorted(api_dir.glob("*.md")):
            findings.extend(scan_spec(spec_path, raw_root, vault_root))

    summary: dict[str, int] = {}
    for f in findings:
        summary[f["verdict"]] = summary.get(f["verdict"], 0) + 1

    return {
        "project_id": project,
        "generated_at": now_iso(),
        "schema_version": "1.0",
        "summary": summary,
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Source column refs against raw files")
    parser.add_argument("--project", default="project_hasaki")
    parser.add_argument("--out", default=None, help="Output JSON path (default: wiki/<project>/refiner/source_refs_report.json)")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    report = build_report(root, args.project)

    if args.out:
        out_path = Path(args.out)
    else:
        out_path = root / "wiki" / args.project / "refiner" / "source_refs_report.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "output": str(out_path.relative_to(root)).replace("\\", "/"),
        "findings": len(report["findings"]),
        "summary": report["summary"],
    }, ensure_ascii=False))

    # Non-zero exit if any critical verdict present (so CI/refiner can branch).
    critical = {"PHANTOM_EVIDENCE", "OUT_OF_RANGE", "INVALID_FORMAT", "RAW_NOT_FOUND", "STALE"}
    has_critical = any(v in critical for v in report["summary"])
    return 2 if has_critical else 0


if __name__ == "__main__":
    raise SystemExit(main())
