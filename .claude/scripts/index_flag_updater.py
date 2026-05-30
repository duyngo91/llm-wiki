r"""Auto-detect critical content flags from Feature Specs and update raw_sources index.json.

Spec verifier L_inference filters scope theo flags trên index sections (`has_enum`,
`has_error_messages`, `has_business_rule`, `has_validation_rule`, `has_formula`,
`has_state_transition`). Sau khi refine stub → full spec, sections vẫn có
`flags = {...: false}` mặc dù spec content rõ ràng có các phần này.

Script này quét từng Feature Spec, detect các flags tương ứng, và update flags
cho các sections mà spec map tới (`mapped_feature`).

Heuristics (tất cả case-insensitive):

| Flag | Detect khi |
|:-----|:-----------|
| `has_enum` | Spec có claim text với pattern "Values:" / "Value:" tiếp theo bullet list, HOẶC table column "Giá trị" với ≥ 2 values, HOẶC `enum` keyword trong BR table |
| `has_error_messages` | Section `## 🚨 Đặc Tả Thông Điệp Báo Lỗi` có ≥ 1 row với ERR-/MSG- ID |
| `has_business_rule` | Section `## ⚙️ Quy Tắc Nghiệp Vụ` có ≥ 1 row (skip header + separator) |
| `has_validation_rule` | Bảng Requirement có ≥ 1 claim với Loại = `Validation` (có thể combo `Validation + Other`) |
| `has_formula` | Spec content match regex `=\s*[\[\(]` hoặc `công thức` (formula keyword Vietnamese) |
| `has_state_transition` | Spec content match `→` hoặc `status .* →` hoặc keyword "state transition" / "chuyển status" |

Dry-run mặc định; `--apply` để write index.json.

Usage:
    py .claude/scripts/index_flag_updater.py --project project_hasaki
    py .claude/scripts/index_flag_updater.py --project project_hasaki --apply
    py .claude/scripts/index_flag_updater.py --project project_hasaki --specs stub_x,stub_y --apply
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


FLAG_NAMES = (
    "has_enum",
    "has_error_messages",
    "has_business_rule",
    "has_validation_rule",
    "has_formula",
    "has_state_transition",
)


def detect_flags(spec_text: str) -> dict[str, bool]:
    """Run heuristics on spec markdown, return flag dict."""
    flags = {k: False for k in FLAG_NAMES}

    # Section extraction helpers
    def section_body(heading_pattern: str) -> str:
        match = re.search(heading_pattern + r"(.*?)(?=^##\s|\Z)", spec_text, re.MULTILINE | re.DOTALL)
        return match.group(1) if match else ""

    # has_error_messages: ## 🚨 section has row(s) with ERR-/MSG- ID
    err_section = section_body(r"^##\s*🚨\s*Đặc Tả Thông Điệp")
    if re.search(r"\|\s*(?:ERR|MSG)-\w+", err_section):
        flags["has_error_messages"] = True

    # has_business_rule: ## ⚙️ section has data rows (skip header + separator + TBD placeholder)
    br_section = section_body(r"^##\s*⚙️\s*Quy Tắc Nghiệp Vụ")
    br_rows = re.findall(r"^\|[^|\n]+\|", br_section, re.MULTILINE)
    # Filter out header + separator rows
    real_rows = [
        r for r in br_rows
        if not re.match(r"^\|\s*(:?-+:?\s*\|)+\s*$", r) and not re.search(r"\bTBD\b", r)
        and not re.search(r"Tên trường|Định dạng", r)  # header
    ]
    if len(real_rows) >= 1:
        flags["has_business_rule"] = True

    # has_validation_rule: requirement table has Loại = Validation
    req_section = section_body(r"^##\s*Phân rã Requirement")
    if re.search(r"\|\s*\w*Validation\w*", req_section, re.IGNORECASE):
        flags["has_validation_rule"] = True
    # Also check BR section
    if not flags["has_validation_rule"] and re.search(r"validation", br_section, re.IGNORECASE):
        flags["has_validation_rule"] = True

    # has_enum: BR table has values list (e.g., "{X, Y}" or "values:" or "∈ {")
    if re.search(r"∈\s*\{|values?:\s*\{|\benum\b|\{[A-Za-zÀ-ỹ]+,\s*[A-Za-zÀ-ỹ]+", spec_text, re.IGNORECASE):
        flags["has_enum"] = True
    # Or enum mention in claim text + at least one Listing/Filter section with multiple values
    if not flags["has_enum"]:
        if re.search(r"Filter|Listing", spec_text) and re.search(r"\benum\b|values:", spec_text, re.IGNORECASE):
            flags["has_enum"] = True

    # has_formula: explicit "=" assignment OR "công thức" keyword
    if re.search(r"công thức", spec_text, re.IGNORECASE):
        flags["has_formula"] = True
    elif re.search(r"=\s*[\[\(]", spec_text):
        flags["has_formula"] = True
    elif re.search(r"\bformula\b", spec_text, re.IGNORECASE):
        flags["has_formula"] = True

    # has_state_transition: → arrow OR "chuyển status" or "state transition"
    if re.search(r"→", spec_text):
        # Filter: must look like state X → Y, not arbitrary arrow
        if re.search(r"`[^`]+`\s*→\s*`[^`]+`", spec_text) or re.search(r"status\s+\S+\s*→", spec_text, re.IGNORECASE):
            flags["has_state_transition"] = True
        elif re.search(r"chuyển status|chuyển trạng thái|state transition", spec_text, re.IGNORECASE):
            flags["has_state_transition"] = True

    # Fallback for state_transition
    if not flags["has_state_transition"] and re.search(r"chuyển status|chuyển trạng thái|state transition", spec_text, re.IGNORECASE):
        flags["has_state_transition"] = True

    return flags


def parse_frontmatter_field(text: str, key: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    if end == -1:
        return ""
    for line in text[3:end].splitlines():
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Auto-detect spec flags + update raw index.json")
    parser.add_argument("--project", default="project_hasaki")
    parser.add_argument("--specs", default=None, help="Comma-separated spec names (default: all)")
    parser.add_argument("--apply", action="store_true", help="Write changes to index.json (default: dry-run)")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    features_dir = root / "wiki" / args.project / "features"
    raw_root = root / "raw_sources" / args.project
    if not features_dir.exists() or not raw_root.exists():
        print(f"ERR: paths not found", file=sys.stderr)
        return 1

    # Load specs
    if args.specs:
        spec_names = [s.strip() for s in args.specs.split(",") if s.strip()]
    else:
        spec_names = [p.stem for p in sorted(features_dir.glob("*.md"))]

    # Compute flags per spec
    spec_flags: dict[str, dict[str, bool]] = {}
    for name in spec_names:
        p = features_dir / f"{name}.md"
        if not p.exists():
            print(f"WARN: skip {name} (not found)", file=sys.stderr)
            continue
        spec_flags[name] = detect_flags(p.read_text(encoding="utf-8"))

    # Iterate index.json files, update sections
    diffs: list[dict] = []
    apply_count = 0
    for idx_path in raw_root.rglob("*_index.json"):
        data = json.loads(idx_path.read_text(encoding="utf-8"))
        changed = False
        for section in data.get("sections", []):
            mapped = section.get("mapped_feature", "").replace(".md", "")
            if mapped not in spec_flags:
                continue
            new_flags = spec_flags[mapped]
            old_flags = section.get("flags", {})
            # Build diff
            section_diff = {}
            for flag in FLAG_NAMES:
                old = old_flags.get(flag, False)
                new = new_flags[flag]
                if old != new:
                    section_diff[flag] = {"old": old, "new": new}
            if section_diff:
                diffs.append(
                    {
                        "doc": idx_path.name,
                        "section_id": section["id"],
                        "spec": mapped,
                        "diff": section_diff,
                    }
                )
                if args.apply:
                    section["flags"] = {**old_flags, **new_flags}
                    changed = True
                    apply_count += 1
        if args.apply and changed:
            idx_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    # Output
    if not diffs:
        print(f"✅ No flag changes needed across {len(spec_flags)} specs.")
        return 0

    mode = "APPLIED" if args.apply else "DRY-RUN"
    print(f"# Index Flag Updater — {mode}")
    print(f"\nSpecs scanned: {len(spec_flags)}")
    print(f"Sections with flag changes: {len(diffs)}")
    if args.apply:
        print(f"Sections updated: {apply_count}\n")
    else:
        print(f"\n(re-run with `--apply` to write changes)\n")

    by_spec: dict[str, list[dict]] = {}
    for d in diffs:
        by_spec.setdefault(d["spec"], []).append(d)

    for spec in sorted(by_spec):
        print(f"## {spec}\n")
        for d in by_spec[spec]:
            print(f"- **{d['doc']}** / {d['section_id']}:")
            for flag, change in d["diff"].items():
                print(f"  - `{flag}`: {change['old']} → **{change['new']}**")
            print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
