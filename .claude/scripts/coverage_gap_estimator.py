"""Estimate requirement-coverage gap per section.

For each section in `<raw>_index.json`:
1. Read raw lines in `[start_line+1, end_line+1]` (1-based display).
2. Count signals that look like requirement statements:
   - Modal keywords (phải, không được, bắt buộc, cấm, yêu cầu, buộc, chỉ được, must, shall)
   - Action verbs (hiển thị, validate, cập nhật, gửi, block, cho phép, từ chối, tính toán, kiểm tra, lưu, xóa)
   - Conditional clauses (Khi /Nếu /Chỉ khi /Trừ khi /When /If )
   - Constraint-bearing table rows (rows with `|` and a digit-bearing or modal cell)
3. Compute `expected_claims` = unique-counted across signals.
4. Compare with `actual_claims` = count of evidence_index records mapped to this section.
5. Flag `UNDERREPORTED_COVERAGE` if gap_ratio = actual / expected < threshold.

Output: `wiki/[project]/refiner/coverage_gap_report.json`.

See `.claude/skills/hasaki-spec-verifier/SKILL.md` (Tầng L_structural).
"""

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


WIKI_TZ = ZoneInfo("Asia/Ho_Chi_Minh")

# Signal patterns (Vietnamese + English). Word-boundary using lookaround for Unicode.
MODAL_RE = re.compile(
    r"(?<![\w])(phải|không được|bắt buộc|cấm|yêu cầu|chỉ được|buộc phải|must|shall|should not)(?![\w])",
    re.IGNORECASE,
)
ACTION_VERB_RE = re.compile(
    r"(?<![\w])(hiển thị|validate|cập nhật|gửi|block|cho phép|từ chối|tính toán|kiểm tra|lưu|xóa|xoá|tạo|sinh|trả về|chuyển trạng thái)(?![\w])",
    re.IGNORECASE,
)
CONDITIONAL_RE = re.compile(
    r"(?:^|\s)(khi|nếu|chỉ khi|trừ khi|when|if)\s",
    re.IGNORECASE,
)
TABLE_ROW_CONSTRAINT_RE = re.compile(r"^\s*\|")
DIGIT_OR_PATTERN_RE = re.compile(r"(\d|\bregex\b|\bpattern\b)", re.IGNORECASE)

DEFAULT_THRESHOLD = 0.5


def now_iso() -> str:
    return datetime.now(WIKI_TZ).isoformat(timespec="seconds")


def find_raw_files(raw_root: Path) -> list[Path]:
    if not raw_root.exists():
        return []
    return sorted(raw_root.glob("*_converted.md"))


def load_index(raw_path: Path) -> dict | None:
    idx_path = raw_path.with_name(raw_path.stem + "_index.json")
    if not idx_path.exists():
        return None
    try:
        return json.loads(idx_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def estimate_claims_in_range(lines: list[str], start_zero: int, end_zero: int) -> dict:
    """Count signals in raw[start_zero:end_zero+1]. Returns counts + estimate."""
    end_inclusive = min(end_zero, len(lines) - 1)
    chunk = lines[start_zero:end_inclusive + 1]
    text = "\n".join(chunk)

    modal_count = len(MODAL_RE.findall(text))
    action_count = len(ACTION_VERB_RE.findall(text))
    conditional_count = len(CONDITIONAL_RE.findall(text))

    table_constraint_rows = 0
    for line in chunk:
        if TABLE_ROW_CONSTRAINT_RE.match(line) and DIGIT_OR_PATTERN_RE.search(line):
            # Header/separator rows excluded.
            if set(line.replace("|", "").replace(":", "").replace("-", "").strip()) == set():
                continue
            table_constraint_rows += 1

    # De-dupe: a single statement often hits multiple signals.
    # Use max of (modal+action de-duped, sentence count of conditional+constraint).
    # Heuristic: assume each conditional clause + each constraint row ≈ 1 distinct claim;
    # modal/action signals overlap so collapse to max(modal, action).
    distinct_modal_action = max(modal_count, action_count)
    expected = distinct_modal_action + conditional_count + table_constraint_rows

    return {
        "expected_claims": expected,
        "signals": {
            "modal_keywords": modal_count,
            "action_verbs": action_count,
            "conditional_clauses": conditional_count,
            "table_constraint_rows": table_constraint_rows,
        },
    }


def load_evidence_index(vault_root: Path, project: str) -> dict:
    p = vault_root / "wiki" / project / "evidence_index.json"
    if not p.exists():
        return {"records": []}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"records": []}


def map_evidence_to_section(records: list[dict], doc_short: str, start_one: int, end_one: int) -> int:
    """Count evidence records whose source_doc matches and line range overlaps section."""
    count = 0
    for rec in records:
        if rec.get("source_doc", "") != doc_short:
            continue
        rec_start = rec.get("source_line_start")
        rec_end = rec.get("source_line_end")
        if rec_start is None or rec_end is None:
            continue
        # Overlap test
        if rec_end < start_one or rec_start > end_one:
            continue
        count += 1
    return count


def short_name(raw_path: Path) -> str:
    """`07062_Receiving_PO_Docs_ver2.17.md` -> `07062`."""
    stem = raw_path.stem
    if stem.endswith("_converted"):
        stem = stem[: -len("_converted")]
    return stem.split("_", 1)[0]


def build_report(vault_root: Path, project: str, threshold: float) -> dict:
    raw_root = vault_root / "raw_sources" / project / "requirements"
    raw_files = find_raw_files(raw_root)
    evidence = load_evidence_index(vault_root, project)
    records = evidence.get("records", [])

    findings: list[dict] = []

    for raw_path in raw_files:
        index = load_index(raw_path)
        if not index:
            continue
        text = raw_path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        doc_short = short_name(raw_path)

        for section in index.get("sections", []):
            start_zero = section.get("start_line")
            end_zero = section.get("end_line")
            if start_zero is None or end_zero is None:
                continue

            est = estimate_claims_in_range(lines, start_zero, end_zero)
            expected = est["expected_claims"]

            # One-based for evidence comparison (Source column uses 1-based).
            start_one = start_zero + 1
            end_one = end_zero + 1
            actual = map_evidence_to_section(records, doc_short, start_one, end_one)

            gap_ratio = (actual / expected) if expected > 0 else 1.0
            coverage_status = section.get("coverage_status", "unmapped")

            verdict = "OK"
            if coverage_status == "unmapped":
                verdict = "UNMAPPED"
            elif expected > 0 and gap_ratio < threshold:
                if coverage_status == "full":
                    verdict = "UNDERREPORTED_COVERAGE"
                elif coverage_status in ("partial", "stub"):
                    verdict = "EXPECTED_GAP"
            elif expected == 0 and actual == 0 and coverage_status not in ("unmapped",):
                verdict = "NO_SIGNALS"

            findings.append({
                "doc": doc_short,
                "raw_file": raw_path.name,
                "section_id": section.get("id"),
                "section_title": section.get("title"),
                "lines": f"L{start_one}-L{end_one}",
                "coverage_status": coverage_status,
                "expected_claims": expected,
                "actual_claims": actual,
                "gap_ratio": round(gap_ratio, 3),
                "signals": est["signals"],
                "verdict": verdict,
                "mapped_feature": section.get("mapped_feature"),
            })

    summary: dict[str, int] = {}
    for f in findings:
        summary[f["verdict"]] = summary.get(f["verdict"], 0) + 1

    return {
        "project_id": project,
        "generated_at": now_iso(),
        "schema_version": "1.0",
        "threshold": threshold,
        "summary": summary,
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Estimate requirement coverage gap per section")
    parser.add_argument("--project", default="project_hasaki")
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD,
                        help="gap_ratio < threshold triggers UNDERREPORTED_COVERAGE (default 0.5)")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    report = build_report(root, args.project, args.threshold)

    if args.out:
        out_path = Path(args.out)
    else:
        out_path = root / "wiki" / args.project / "refiner" / "coverage_gap_report.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "output": str(out_path.relative_to(root)).replace("\\", "/"),
        "findings": len(report["findings"]),
        "summary": report["summary"],
    }, ensure_ascii=False))

    # Non-zero if any critical underreport.
    critical = {"UNDERREPORTED_COVERAGE", "UNMAPPED"}
    has_critical = any(v in critical for v in report["summary"])
    return 2 if has_critical else 0


if __name__ == "__main__":
    raise SystemExit(main())
