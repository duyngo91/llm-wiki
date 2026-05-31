"""Bootstrap Feature Specs từ raw `*_index.json` sections.

Đọc tất cả `raw_sources/project_hasaki/requirements/*_index.json`, sinh 1 file
`wiki/project_hasaki/features/feature_<doc>.md` cho mỗi raw doc với:

- Frontmatter: `partial_read: true`, `verification_status: Pending`
- R-table 1 row / section (R001..RNNN với title từ index `title` + source ref)
- Placeholder sections (Tổng quan, Câu hỏi chưa rõ, Blocked Coverage, Changelog)

Mục đích: nhanh chóng có spec scaffold để refiner đọc raw từng section và refine
thành full spec qua process Gate 1B.

KHÔNG tự overwrite file đã tồn tại — chỉ tạo mới.

Usage:
    py .claude/scripts/generate_stub_features_from_index.py

Hardcoded project_hasaki path. Để extend multi-project, refactor REQ_DIR/WIKI_DIR thành
CLI args.
"""

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WIKI_DIR = ROOT / "wiki" / "project_hasaki" / "features"
REQ_DIR = ROOT / "raw_sources" / "project_hasaki" / "requirements"


def now_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def now_dt() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def slugify(name: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "_" for ch in name).strip("_")


def build_stub(index_path: Path) -> tuple[str, str]:
    payload = json.loads(index_path.read_text(encoding="utf-8"))
    source_name = payload.get("source_file", index_path.name.replace("_index.json", ".md"))
    source_version = payload.get("source_version", "unknown")
    stem = index_path.stem.replace("_index", "")
    feature_slug = f"feature_{slugify(stem)}"

    rows = []
    for i, sec in enumerate(payload.get("sections", []), start=1):
        rid = f"R{i:03d}"
        title = sec.get("title", "").strip()
        source_ref = sec.get("source_ref", f"{source_name}#L{sec.get('start_line',0)+1}")
        rows.append(f"| {rid} | {title} | Functional | High | ✅ | {source_ref} |")

    req_rows = "\n".join(rows) if rows else "| R001 | Stub pending | Functional | High | ✅ | n/a |"
    dt = now_dt()
    d = now_date()
    content = f"""---
aliases: [{feature_slug}]
tags: [qa/requirement, qa/feature-group/reset_bootstrap]
status: Draft
created: {d}
updated: {d}
feature: {feature_slug}
project: project_hasaki
source_version: {source_version}
source_doc: {source_name}
source_range: full-index
partial_read: true
partial_read_note: "Auto-generated stub from index after reset"
last_verified_at: "{dt}"
verification_status: Pending
approved_by:
approved_at:
approval_note:
---

# REQ: {feature_slug}

## Tổng quan
- **Mã tính năng:** {feature_slug}
- **Feature:** {feature_slug}
- **Mô tả ngắn:** Auto-generated stub from requirement index.
- **Source chính:** {source_name} ({source_version})
- **Đối tượng sử dụng (Actors):** TBD
- **Feature Group:** [[wiki/project_hasaki/feature_groups/reset_bootstrap|reset_bootstrap]]
- **Test Suite tương ứng:** [[test_{feature_slug}]]
- **API Spec liên quan:** N/A

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | {source_name} | {source_version} | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Không có API/interface explicit | N/A |

## Phân rã Requirement
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
{req_rows}

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)
### Điều kiện tiên quyết (Pre-conditions)
- TBD
### Luồng chuẩn (Happy Path)
1. TBD
### Luồng rẽ nhánh (Alternative Paths)
- TBD
### Luồng ngoại lệ (Exception Paths)
- TBD

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------|:---------|:----------|:-------------------------------|
| TBD | TBD | TBD | TBD |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
- TBD

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)
- **Scenario 1**
  - **Given:** TBD
  - **When:** TBD
  - **Then:** TBD

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R001 | Chưa review semantic của toàn bộ sections, cần phân tích theo batch. | PO/BA/Dev | Open | | | |

## 📝 Thay đổi so với version cũ
| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Initial reset bootstrap stub from index. | n/a | {source_version} | All | Draft |

## 🔎 Impact Analysis & Regression Proposal
| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | {feature_slug} | test_{feature_slug} | Add | TBD | Gate 1 pending |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001 | | ❌ Blocked | Stub only, waiting detailed review |

## 📓 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| {dt} | v1.0 | Auto-generated stub from index after reset | {source_name} |
"""
    return feature_slug, content


def main() -> int:
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    created = []
    for index_path in sorted(REQ_DIR.glob("*_index.json")):
        feature_slug, content = build_stub(index_path)
        out = WIKI_DIR / f"{feature_slug}.md"
        out.write_text(content, encoding="utf-8")
        created.append(out)
    print(json.dumps({"created": [str(p.relative_to(ROOT)).replace("\\", "/") for p in created]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
