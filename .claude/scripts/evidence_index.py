"""Build evidence index from Feature Spec + API Spec.

Parses:
- Requirement table (`| ID | Requirement | ... | Source |`)
- AC bullet form (`- **Scenario N: ...` or `- **AC-NN: ...`) inside `## Tiêu Chí Nghiệm Thu`
- AC table form (`| AC-NN | ... | Source |`) if used
- Business Rules table (`| Tên trường | ... | Ràng buộc |` — synthetic ID `BR-{feature}-{idx}`)
- API List table (`| API ID | Method | Endpoint | ... | Source |`)
- Question table (`| Q-NN | ... |`)

Source column supports canonical multi-range:
  `07062#L234-L239, 07062#L500-L502`

See `.claude/skills/hasaki-wiki/references/shared.md#source-reference-format-ssot`.
"""

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


WIKI_TZ = ZoneInfo("Asia/Ho_Chi_Minh")

# Canonical source ref: `doc#L{start}-L{end}`. Tolerate no-L for backwards compat.
SOURCE_REF_RE = re.compile(r"([A-Za-z0-9_.]+)#L?(\d+)(?:-L?(\d+))?")
MULTI_RANGE_SPLIT_RE = re.compile(r",\s*")

# AC bullet patterns (template uses Scenario; some specs use AC-NN directly).
AC_BULLET_RE = re.compile(
    r"^\s*-\s*\*\*\s*(?:(AC-\d+)|Scenario\s+(\d+))\s*[:.\-—]",
    re.IGNORECASE,
)

# Section heading markers.
SECTION_REQUIREMENT_RE = re.compile(r"^##\s*Phân rã Requirement", re.IGNORECASE)
SECTION_BUSINESS_RULES_RE = re.compile(r"^##\s*.*Quy Tắc Nghiệp Vụ", re.IGNORECASE)
SECTION_ACCEPTANCE_RE = re.compile(r"^##\s*.*Tiêu Chí Nghiệm Thu", re.IGNORECASE)
SECTION_API_LIST_RE = re.compile(r"^##\s*API\s*/?\s*Interface\s*List", re.IGNORECASE)
SECTION_QUESTION_RE = re.compile(r"^##\s*.*Câu hỏi", re.IGNORECASE)


def now_iso() -> str:
    return datetime.now(WIKI_TZ).isoformat(timespec="seconds")


def read_frontmatter(md_text: str) -> dict:
    if not md_text.startswith("---"):
        return {}
    end = md_text.find("\n---", 3)
    if end == -1:
        return {}
    block = md_text[3:end].splitlines()
    data = {}
    for line in block:
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip().strip('"')
    return data


def parse_source_refs(cell: str) -> list[dict]:
    """Parse a Source cell into list of {doc, start, end} entries. Multi-range supported."""
    refs = []
    for part in MULTI_RANGE_SPLIT_RE.split(cell):
        part = part.strip()
        if not part:
            continue
        for match in SOURCE_REF_RE.finditer(part):
            start_line = int(match.group(2))
            end_line = int(match.group(3)) if match.group(3) else start_line
            refs.append({
                "source_doc": match.group(1),
                "source_line_start": start_line,
                "source_line_end": end_line,
            })
    return refs


def parse_table_rows(lines: list[str], start_idx: int) -> tuple[list[list[str]], int]:
    """Parse a markdown table starting at start_idx. Returns (rows, next_idx)."""
    rows: list[list[str]] = []
    i = start_idx
    while i < len(lines):
        line = lines[i].rstrip("\n")
        if not line.startswith("|"):
            break
        # Separator row (---|---|---)
        if set(line.replace("|", "").replace(":", "").replace("-", "").strip()) == set():
            i += 1
            continue
        cells = [cell.strip() for cell in line.strip().split("|")[1:-1]]
        rows.append(cells)
        i += 1
    return rows, i


def find_header_row(lines: list[str], start_idx: int, max_scan: int = 6) -> int | None:
    """Look ahead from start_idx for a markdown table header row. Returns line idx or None."""
    for j in range(start_idx, min(start_idx + max_scan, len(lines))):
        if lines[j].lstrip().startswith("|"):
            return j
    return None


def build_record(
    feature: str,
    feature_file: str,
    claim_type: str,
    coverage_class: str,
    claim_local_id: str,
    text: str,
    sources: list[dict],
    frontmatter: dict,
    extra: dict | None = None,
) -> list[dict]:
    """Build one record per source ref (multi-range explodes into multiple records)."""
    out = []
    base = {
        "claim_id": f"{feature}:{claim_local_id}",
        "claim_type": claim_type,
        "coverage_class": coverage_class,
        "feature": feature,
        "feature_file": feature_file,
        "requirement_id": claim_local_id if claim_type == "requirement" else "",
        "ac_id": claim_local_id if claim_type == "acceptance_criteria" else "",
        "api_id": claim_local_id if claim_type == "api" else "",
        "business_rule_id": claim_local_id if claim_type == "business_rule" else "",
        "question_id": claim_local_id if claim_type == "question" else "",
        "claim_text": text.strip()[:280],
        "source_version": frontmatter.get("source_version", ""),
        "partial_read": frontmatter.get("partial_read", "false").lower() == "true",
        "verification_status": frontmatter.get("verification_status", "Unknown"),
        "last_verified_at": frontmatter.get("last_verified_at", ""),
    }
    if extra:
        base.update(extra)

    if not sources:
        rec = base.copy()
        rec.update({"source_doc": "", "source_line_start": None, "source_line_end": None})
        out.append(rec)
    else:
        for src in sources:
            rec = base.copy()
            rec.update(src)
            out.append(rec)
    return out


def scan_requirement_table(
    lines: list[str],
    start: int,
    feature: str,
    feature_file: str,
    frontmatter: dict,
) -> tuple[list[dict], int]:
    header = find_header_row(lines, start)
    if header is None:
        return [], start
    rows, end_idx = parse_table_rows(lines, header + 2)
    records = []
    for row in rows:
        if len(row) < 6:
            continue
        rid, req_text, _kind, _prio, _testable, source = row[:6]
        if not rid or rid.startswith(":"):
            continue
        sources = parse_source_refs(source)
        records.extend(build_record(
            feature, feature_file,
            claim_type="requirement",
            coverage_class="requirement",
            claim_local_id=rid,
            text=req_text,
            sources=sources,
            frontmatter=frontmatter,
        ))
    return records, end_idx


def scan_business_rules_table(
    lines: list[str],
    start: int,
    feature: str,
    feature_file: str,
    frontmatter: dict,
) -> tuple[list[dict], int]:
    """Business Rules table has no ID column. Synthesize BR-{idx} per row."""
    header = find_header_row(lines, start)
    if header is None:
        return [], start
    rows, end_idx = parse_table_rows(lines, header + 2)
    records = []
    for idx, row in enumerate(rows, start=1):
        if len(row) < 4:
            continue
        field_name, fmt, required, constraint = row[:4]
        if not field_name or field_name.startswith(":"):
            continue
        br_id = f"BR-{idx:03d}"
        rule_text = f"{field_name} | {fmt} | {required} | {constraint}"
        # Business Rules table template has no Source column.
        # Source must be carried via constraint text if explicit.
        sources_from_constraint = parse_source_refs(constraint)
        records.extend(build_record(
            feature, feature_file,
            claim_type="business_rule",
            coverage_class="business_rule",
            claim_local_id=br_id,
            text=rule_text,
            sources=sources_from_constraint,
            frontmatter=frontmatter,
            extra={"field_name": field_name.strip()},
        ))
    return records, end_idx


def scan_acceptance_section(
    lines: list[str],
    start: int,
    feature: str,
    feature_file: str,
    frontmatter: dict,
) -> tuple[list[dict], int]:
    """Scan AC section — supports both bullet (template) and table forms."""
    records = []
    i = start
    while i < len(lines):
        line = lines[i]
        # Stop at next ## heading.
        if line.startswith("## ") and i > start:
            break
        # Table form: header row inside AC section.
        if line.lstrip().startswith("|") and i + 1 < len(lines) and "AC" in line.upper():
            rows, next_idx = parse_table_rows(lines, i + 2)
            for row in rows:
                if len(row) < 2:
                    continue
                ac_id = row[0]
                if not ac_id.startswith("AC-"):
                    continue
                text_cell = row[1] if len(row) > 1 else ""
                source_cell = row[-1] if len(row) >= 3 else ""
                sources = parse_source_refs(source_cell)
                records.extend(build_record(
                    feature, feature_file,
                    claim_type="acceptance_criteria",
                    coverage_class="ac",
                    claim_local_id=ac_id,
                    text=text_cell,
                    sources=sources,
                    frontmatter=frontmatter,
                ))
            i = next_idx
            continue
        # Bullet form.
        match = AC_BULLET_RE.match(line)
        if match:
            ac_label = match.group(1) or f"Scenario-{int(match.group(2)):02d}"
            # Collect following Given/When/Then lines until blank line or next bullet.
            block_lines = [line.rstrip()]
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if AC_BULLET_RE.match(nxt) or nxt.startswith("## "):
                    break
                if not nxt.strip() and (j + 1 >= len(lines) or AC_BULLET_RE.match(lines[j + 1] or "") or lines[j + 1].startswith("## ")):
                    break
                block_lines.append(nxt.rstrip())
                j += 1
            block_text = "\n".join(block_lines)
            # Source ref may appear inline (e.g. "...source: 07062#L234").
            sources = parse_source_refs(block_text)
            records.extend(build_record(
                feature, feature_file,
                claim_type="acceptance_criteria",
                coverage_class="ac",
                claim_local_id=ac_label,
                text=block_text,
                sources=sources,
                frontmatter=frontmatter,
            ))
            i = j
            continue
        i += 1
    return records, i


def scan_question_table(
    lines: list[str],
    start: int,
    feature: str,
    feature_file: str,
    frontmatter: dict,
) -> tuple[list[dict], int]:
    header = find_header_row(lines, start)
    if header is None:
        return [], start
    rows, end_idx = parse_table_rows(lines, header + 2)
    records = []
    for row in rows:
        if len(row) < 5:
            continue
        qid = row[0]
        if not qid.startswith("Q-"):
            continue
        question_text = row[2] if len(row) > 2 else ""
        status_cell = row[4] if len(row) > 4 else ""
        source_cell = row[6] if len(row) > 6 else ""
        sources = parse_source_refs(source_cell)
        records.extend(build_record(
            feature, feature_file,
            claim_type="question",
            coverage_class="question",
            claim_local_id=qid,
            text=question_text,
            sources=sources,
            frontmatter=frontmatter,
            extra={"question_status": status_cell.strip()},
        ))
    return records, end_idx


def scan_api_list_table(
    lines: list[str],
    start: int,
    feature: str,
    feature_file: str,
    frontmatter: dict,
) -> tuple[list[dict], int]:
    """API List table: `| API ID | Method | Endpoint | Mục đích | R/AC | Source | Status |`."""
    header = find_header_row(lines, start)
    if header is None:
        return [], start
    rows, end_idx = parse_table_rows(lines, header + 2)
    records = []
    for row in rows:
        if len(row) < 6:
            continue
        api_id = row[0]
        if not api_id.startswith("API-"):
            continue
        method = row[1] if len(row) > 1 else ""
        endpoint = row[2] if len(row) > 2 else ""
        purpose = row[3] if len(row) > 3 else ""
        rac = row[4] if len(row) > 4 else ""
        source = row[5] if len(row) > 5 else ""
        sources = parse_source_refs(source)
        records.extend(build_record(
            feature, feature_file,
            claim_type="api",
            coverage_class="api",
            claim_local_id=api_id,
            text=f"{method} {endpoint} — {purpose}",
            sources=sources,
            frontmatter=frontmatter,
            extra={
                "method": method.strip(),
                "endpoint": endpoint.strip(),
                "linked_r_ac": rac.strip(),
            },
        ))
    return records, end_idx


def scan_feature_spec(feature_path: Path, vault_root: Path) -> list[dict]:
    text = feature_path.read_text(encoding="utf-8")
    frontmatter = read_frontmatter(text)
    feature_name = frontmatter.get("feature", feature_path.stem)
    feature_file = str(feature_path.relative_to(vault_root)).replace("\\", "/")
    lines = text.splitlines()
    records: list[dict] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if SECTION_REQUIREMENT_RE.match(line):
            recs, i = scan_requirement_table(lines, i + 1, feature_name, feature_file, frontmatter)
            records.extend(recs)
            continue
        if SECTION_BUSINESS_RULES_RE.match(line):
            recs, i = scan_business_rules_table(lines, i + 1, feature_name, feature_file, frontmatter)
            records.extend(recs)
            continue
        if SECTION_ACCEPTANCE_RE.match(line):
            recs, i = scan_acceptance_section(lines, i + 1, feature_name, feature_file, frontmatter)
            records.extend(recs)
            continue
        if SECTION_QUESTION_RE.match(line):
            recs, i = scan_question_table(lines, i + 1, feature_name, feature_file, frontmatter)
            records.extend(recs)
            continue
        i += 1
    return records


def scan_api_spec(api_path: Path, vault_root: Path) -> list[dict]:
    text = api_path.read_text(encoding="utf-8")
    frontmatter = read_frontmatter(text)
    feature_name = frontmatter.get("feature", api_path.stem)
    feature_file = str(api_path.relative_to(vault_root)).replace("\\", "/")
    lines = text.splitlines()
    records: list[dict] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if SECTION_API_LIST_RE.match(line):
            recs, i = scan_api_list_table(lines, i + 1, feature_name, feature_file, frontmatter)
            records.extend(recs)
            continue
        if SECTION_QUESTION_RE.match(line):
            recs, i = scan_question_table(lines, i + 1, feature_name, feature_file, frontmatter)
            records.extend(recs)
            continue
        i += 1
    return records


def build_evidence_index(vault_root: Path, project: str) -> dict:
    features_dir = vault_root / "wiki" / project / "features"
    api_specs_dir = vault_root / "wiki" / project / "api_specs"

    payload = {
        "project_id": project,
        "generated_at": now_iso(),
        "schema_version": "2.0",
        "records": [],
    }

    if features_dir.exists():
        for feature_path in sorted(features_dir.glob("*.md")):
            payload["records"].extend(scan_feature_spec(feature_path, vault_root))

    if api_specs_dir.exists():
        for api_path in sorted(api_specs_dir.glob("*.md")):
            payload["records"].extend(scan_api_spec(api_path, vault_root))

    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Build evidence index from Feature Spec + API Spec")
    parser.add_argument("--project", default="project_hasaki")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    payload = build_evidence_index(root, args.project)
    out_path = root / "wiki" / args.project / "evidence_index.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    counts: dict[str, int] = {}
    for rec in payload["records"]:
        counts[rec["coverage_class"]] = counts.get(rec["coverage_class"], 0) + 1

    print(json.dumps({
        "output": str(out_path.relative_to(root)).replace("\\", "/"),
        "records": len(payload["records"]),
        "by_class": counts,
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
