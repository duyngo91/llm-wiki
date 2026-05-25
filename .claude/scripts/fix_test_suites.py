"""
Fix script for hasaki test suites:
1. Add missing Phạm vi column to TC table header (regex-based, handles extra spaces)
2. Remove open-question R-refs from TC AC/Req Cover (matches wiki_sync_core detection)
3. Clear cells[2] when all refs blocked (marks TC 🚫 Blocked, removes R-refs from cover)
4. Add/update ## 🚧 Blocked Coverage section with actual blocked TCs
5. Add ## 🔁 Regression Impact section if missing
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

VAULT = Path(__file__).parent.parent.parent


def is_real_tc_row(line):
    """Match actual TC rows (>= 9 pipes), not Blocked Coverage table rows (3 pipes)."""
    if not re.match(r"^\|\s*\*?\*?TC-", line):
        return False
    return line.count("|") >= 9


def extract_section(text, heading_text):
    pattern = re.compile(
        rf"^## .*{re.escape(heading_text)}.*?\n(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group(1) if match else ""


def collect_open_question_refs(feature_stem):
    """Return set of R-IDs that have Open questions in the feature spec.
    Uses same detection logic as wiki_sync_core.py: [ ], Open, or ❓ in section lines.
    """
    for fp in (VAULT / "wiki").glob(f"**/{feature_stem}.md"):
        content = fp.read_text(encoding="utf-8")
        section = extract_section(content, "Câu hỏi chưa rõ")
        refs = set()
        for line in section.splitlines():
            is_open = (
                "[ ]" in line
                or re.search(r"\|\s*Open\s*\|", line)
                or "❓" in line
            )
            if not is_open:
                continue
            refs.update(re.findall(r"\bR\d+\b|\bAC-\d+\b", line))
        return refs
    return set()


def get_tc_header_line(content):
    """Return the TC table header line (starts with '| Test ID')."""
    for line in content.splitlines():
        if line.startswith("| Test ID"):
            return line
    return ""


def add_phavi_column(content):
    """Add Phạm vi column to TC table header. Uses regex to handle extra spaces.
    Only modifies header and separator rows; skips data rows that already have
    the correct column count.
    """
    lines = content.splitlines()
    result = []
    in_tc_table = False
    header_processed = False
    sep_processed = False
    header_cols = 0

    for line in lines:
        stripped = line.strip()

        # Detect TC table header (contains Test ID, does not yet have Phạm vi)
        if stripped.startswith("|") and "Test ID" in stripped and not header_processed:
            if "Phạm vi" in stripped:
                # Already has Phạm vi — count cols and pass through
                header_cols = stripped.count("|") - 1
                result.append(line)
                in_tc_table = True
                header_processed = True
                continue

            # Use regex to insert Phạm vi after the AC/Req Cover cell
            new_line = re.sub(
                r"(\|[^|]*AC/Req Cover[^|]*\|)", r"\1 Phạm vi |", stripped
            )
            if new_line == stripped:
                # Fallback: insert after Tiêu đề cell
                new_line = re.sub(
                    r"(\|[^|]*Tiêu đề[^|]*\|)", r"\1 Phạm vi |", stripped
                )
            header_cols = new_line.count("|") - 1
            result.append(new_line)
            in_tc_table = True
            header_processed = True
            continue

        # Fix separator row — add one cell only if needed
        if (
            in_tc_table
            and not sep_processed
            and stripped.startswith("|")
            and re.match(r"[\|\s\-:]+$", stripped)
        ):
            sep_cols = stripped.count("|") - 1
            if sep_cols < header_cols:
                result.append(stripped.rstrip("|").rstrip() + " :--- |")
            else:
                result.append(line)
            sep_processed = True
            continue

        # Data rows — only insert Phạm vi if column is missing
        if in_tc_table and is_real_tc_row(stripped):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if len(cells) < header_cols:
                combined = " ".join(cells).lower()
                if "api" in combined:
                    scope = "API+Functional"
                elif any(k in combined for k in ("app", "scan", "mobile")):
                    scope = "UI+Functional"
                else:
                    scope = "Functional"
                cells.insert(3, scope)
                result.append("| " + " | ".join(cells) + " |")
                continue
            result.append(line)
            continue

        if in_tc_table and stripped and not stripped.startswith("|"):
            in_tc_table = False
            header_processed = False

        result.append(line)

    return "\n".join(result)


def fix_test_suite(suite_path, feature_stem, open_refs):
    content = suite_path.read_text(encoding="utf-8")
    original = content
    changes = []

    # 1. Add Phạm vi column to header if missing — check header line specifically
    header_line = get_tc_header_line(content)
    if header_line and "Phạm vi" not in header_line:
        content = add_phavi_column(content)
        new_header_line = get_tc_header_line(content)
        if new_header_line and "Phạm vi" in new_header_line:
            changes.append("Added Phạm vi column")
        else:
            changes.append("WARNING: Phạm vi column could not be inserted")

    # 2. Find TCs covering open-question R-IDs and build blocked list
    blocked_tcs = []
    tc_lines_to_update = {}

    lines = content.splitlines()
    for i, line in enumerate(lines):
        if not is_real_tc_row(line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        tc_id = cells[0].strip("*").strip()
        req_cover = cells[2] if len(cells) > 2 else ""
        covered_refs = set(re.findall(r"\bR\d+\b|\bAC-\d+\b", req_cover))
        blocked = covered_refs & open_refs

        if blocked:
            remaining = covered_refs - open_refs
            if remaining:
                # Remove only the blocked refs; keep remaining refs
                new_cover = req_cover
                for ref in sorted(blocked):
                    new_cover = re.sub(r"\s*/\s*" + ref + r"\b", "", new_cover)
                    new_cover = re.sub(r"\b" + ref + r"\s*/\s*", "", new_cover)
                    new_cover = re.sub(r"\b" + ref + r"\b", "", new_cover)
                new_cover = re.sub(r"\s+", " ", new_cover).strip().strip("/").strip()
                cells[2] = new_cover
                tc_lines_to_update[i] = "| " + " | ".join(cells) + " |"
                blocked_tcs.append((tc_id, sorted(blocked), "R-ref removed, TC kept"))
            else:
                # TC only covered open refs → mark as Blocked; clear cells[2]
                cells[2] = "🚫"
                cells[-1] = "🚫 Blocked"
                tc_lines_to_update[i] = "| " + " | ".join(cells) + " |"
                blocked_tcs.append(
                    (tc_id, sorted(blocked), "Only open refs — status set to Blocked")
                )
            changes.append(f"Processed {tc_id} covering open refs {sorted(blocked)}")

    # Apply TC line updates
    if tc_lines_to_update:
        lines = content.splitlines()
        for i, new_line in tc_lines_to_update.items():
            if i < len(lines):
                lines[i] = new_line
        content = "\n".join(lines)

    # 3. Build Blocked Coverage section content
    blocked_section = "## 🚧 Blocked Coverage\n\n"
    if blocked_tcs:
        blocked_section += "Các Requirement/AC chưa được sinh TC đầy đủ do còn câu hỏi Open trong Feature Spec:\n\n"
        blocked_section += "| TC ID | Blocked R-IDs | Ghi chú |\n"
        blocked_section += "|:------|:-------------|:--------|\n"
        for tc_id, refs, note in blocked_tcs:
            blocked_section += f"| {tc_id} | {', '.join(refs)} | {note} |\n"
    else:
        blocked_section += "*Không có coverage bị blocked.*\n"

    regression_section = "## 🔁 Regression Impact\n\n*Chưa có thay đổi requirement. Cập nhật khi có Task Change.*\n"

    # 4. Replace existing Blocked Coverage section OR insert new one
    if "## 🚧 Blocked Coverage" in content:
        content = re.sub(
            r"## 🚧 Blocked Coverage\n\n.*?(?=\n## |\Z)",
            blocked_section.rstrip("\n"),
            content,
            flags=re.DOTALL,
        )
        changes.append("Updated Blocked Coverage section")
    else:
        for anchor in ["## 🚫 Test Cases Lỗi Thời", "## 📅 Changelog"]:
            if anchor in content:
                content = content.replace(anchor, f"\n{blocked_section}\n{anchor}")
                changes.append("Added Blocked Coverage section")
                break
        else:
            content += f"\n\n{blocked_section}"
            changes.append("Added Blocked Coverage section (appended)")

    # 5. Add Regression Impact if missing
    if "## 🔁 Regression Impact" not in content:
        for anchor in ["## 🚧 Blocked Coverage", "## 🚫 Test Cases Lỗi Thời", "## 📅 Changelog"]:
            if anchor in content:
                content = content.replace(anchor, f"\n{regression_section}\n\n{anchor}")
                changes.append("Added Regression Impact section")
                break
        else:
            content += f"\n\n{regression_section}"
            changes.append("Added Regression Impact section (appended)")

    if content != original:
        suite_path.write_text(content, encoding="utf-8")
        print(f"✅ Fixed {suite_path.name}: {'; '.join(changes)}")
    else:
        print(f"⏭️  No changes needed for {suite_path.name}")


def main():
    suites_dir = VAULT / "wiki" / "project_hasaki" / "test_suites"
    feature_map = {
        "test_hasaki_qc_evaluation": "hasaki_qc_evaluation",
        "test_hasaki_qc_setup": "hasaki_qc_setup",
        "test_hasaki_receiving_inbound_shipment": "hasaki_receiving_inbound_shipment",
        "test_hasaki_receiving_packing_list": "hasaki_receiving_packing_list",
        "test_hasaki_receiving_po_app": "hasaki_receiving_po_app",
        "test_hasaki_receiving_vas": "hasaki_receiving_vas",
    }

    for suite_stem, feature_stem in feature_map.items():
        suite_path = suites_dir / f"{suite_stem}.md"
        if not suite_path.exists():
            print(f"⚠️  Not found: {suite_path}")
            continue
        open_refs = collect_open_question_refs(feature_stem)
        print(f"\n--- {suite_stem} ---")
        print(f"    Open question R-IDs: {sorted(open_refs) or 'none'}")
        fix_test_suite(suite_path, feature_stem, open_refs)

    print("\n✅ Done fixing all hasaki test suites.")


if __name__ == "__main__":
    main()
