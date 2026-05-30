---
aliases: [stub_qc_overview]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_qc_overview
project: project_hasaki
source_version: 1.5
source_doc: 07105_Quality_Control_Docs_ver1.5.md
source_range: 07105#L102-L124
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 18:45:00"
verification_status: Pending
approved_by:
approved_at:
approval_note:
---

# REQ: stub_qc_overview

## Tổng quan
- **Mã tính năng:** stub_qc_overview
- **Feature:** Quality Control — Tổng quan, Thuật ngữ, Workflow, Wireframe
- **Mô tả ngắn:** Phần Tổng quan của tài liệu Quality Control v1.5 — bao gồm 4 section: `Thuật ngữ & viết tắt` (bảng rỗng — chưa định nghĩa), `Quy trình (Workflow)` (link Drive Hasaki), `Giao diện (Wireframe)` (link Figma), `Yêu cầu chức năng` (heading dẫn vào nội dung detail). Stub này gom các metadata header của doc — không chứa R/AC business explicit.
- **Source chính:** 07105_Quality_Control_Docs_ver1.5.md (v1.5)
- **Đối tượng sử dụng (Actors):** N/A — đây là phần header/metadata của doc, không phải feature có actor cụ thể.
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** [[test_stub_qc_overview]]
- **API Spec liên quan:** N/A — section này không mô tả API.
- **Mối quan hệ:** Đây là section header gateway cho toàn bộ feature group [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]. Wireframe link cover tất cả features.

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07105_Quality_Control_Docs_ver1.5.md | 1.5 | ✅ Hiện hành |
| 2 | Workflow Link | https://drive.hasaki.vn/d/d45615dafe0b441785ff/ | — | Reference (Q-001) |
| 3 | Wireframe Figma | https://www.figma.com/design/CLtzJtUv6sA4rxyaBPnbz5/34.-Quality-Control?node-id=366-229 | — | Reference (Q-002) |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Section overview không mô tả API | N/A |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Tài liệu Quality Control v1.5 có section `Thuật ngữ & viết tắt` để định nghĩa các terms dùng trong doc. Bảng terms gồm 4 cột: `# Code`, `Name`, `Desciption` (raw có typo `Desciption` → `Description` — Q-003). **Hiện tại bảng có 5 dòng nhưng tất cả đều rỗng** — chưa có thuật ngữ nào được định nghĩa trong v1.5 | Documentation | Low | ⚠️ | 07105#L102-L110 |
| R002 | Tài liệu có section `Quy trình (Workflow)` link sang Drive Hasaki: `https://drive.hasaki.vn/d/d45615dafe0b441785ff/` | Documentation | Low | ⚠️ | 07105#L112-L113 |
| R003 | Tài liệu có section `Giao diện (Wireframe)` link sang Figma: `https://www.figma.com/design/CLtzJtUv6sA4rxyaBPnbz5/34.-Quality-Control?node-id=366-229&t=dvLSI74zHLKyyM0v-1` (file `34. Quality Control`, node `366-229`) | Documentation | Low | ⚠️ | 07105#L115-L118 |
| R004 | Tài liệu có heading `Yêu cầu chức năng` (Functional requirements) tại L124 dẫn vào toàn bộ phần nội dung chi tiết bắt đầu từ section `Thiết lập tiêu chí` (S-04) | Documentation | Low | ✅ | 07105#L124-L124 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- N/A — section này là tài liệu tham khảo, không có flow runtime.

### Luồng chuẩn (Happy Path) — Tra cứu workflow & wireframe
1. User đọc tài liệu QC v1.5.
2. Khi cần tra workflow → click link Drive (R002).
3. Khi cần tra wireframe → click link Figma (R003).
4. Khi cần xem yêu cầu chức năng chi tiết → đọc tiếp từ section `Thiết lập tiêu chí` trở đi (R004).

### Luồng rẽ nhánh (Alternative Paths)
- N/A.

### Luồng ngoại lệ (Exception Paths)
- **E1 — Link Drive/Figma không truy cập được:** user phải request quyền truy cập từ owner.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Bảng thuật ngữ | table | ❌ | Hiện tại trống — cần bổ sung định nghĩa các terms khi có (Q-004) |
| Workflow link | URL | ✅ | Phải là Drive Hasaki link hợp lệ |
| Wireframe link | URL | ✅ | Phải là Figma file `34. Quality Control` |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

- Không có error message — section overview không trigger lỗi runtime.

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Có bảng thuật ngữ trong doc**
  - **Given:** User mở tài liệu QC v1.5.
  - **When:** User cuộn đến section `Thuật ngữ & viết tắt`.
  - **Then:** Bảng terms hiển thị với header `# Code | Name | Desciption` và 5 row rỗng (R001).
- **AC-02 — Link Workflow truy cập được**
  - **Given:** User mở tài liệu QC v1.5.
  - **When:** User click link Drive ở section `Quy trình (Workflow)`.
  - **Then:** Trình duyệt mở `https://drive.hasaki.vn/d/d45615dafe0b441785ff/` (R002).
- **AC-03 — Link Wireframe truy cập được**
  - **Given:** User mở tài liệu QC v1.5.
  - **When:** User click link Figma ở section `Giao diện (Wireframe)`.
  - **Then:** Trình duyệt mở Figma file `34. Quality Control`, focus node `366-229` (R003).
- **AC-04 — Heading Yêu cầu chức năng có trong doc**
  - **Given:** Tài liệu QC v1.5.
  - **When:** User đọc tới sau section `Giao diện (Wireframe)`.
  - **Then:** Heading `Yêu cầu chức năng` xuất hiện và bắt đầu nội dung detail từ `Thiết lập tiêu chí` (R004).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R002 | Workflow Drive link có nội dung gì cụ thể? Có phải BPMN diagram hay flowchart không? Có sync với raw doc không (nếu update Drive thì cập nhật doc không)? | PO | Open | | | |
| Q-002 | R003 | Wireframe Figma — node `366-229` cover toàn bộ feature QC hay chỉ 1 màn hình chính? Có version control giữa raw doc v1.5 và wireframe? | UX | Open | | | |
| Q-003 | R001 | Header bảng terms ghi `Desciption` (sai chính tả) — đây là typo cần fix trong doc, hay là 1 ký hiệu intentional? | PO | Open | | | |
| Q-004 | R001 | Bảng thuật ngữ đang rỗng 5 dòng — có dự định bổ sung không? Các thuật ngữ nào trong doc cần định nghĩa (vd `UID group`, `Group UID`, `VAS`, `Tiêu chí 4 điểm`, `Xã vải`)? | PO/BA | Open | | | |
| Q-005 | All R | Section overview có scope sinh test case không? Hay đây là metadata-only và test suite tương ứng (`test_stub_qc_overview`) sẽ bị mark `N/A` / không cần thiết kế? | QA Lead | Open | | | |
| Q-006 | R004 | Heading `Yêu cầu chức năng` có structure phân cấp con không (vd `Yêu cầu chức năng > Thiết lập tiêu chí > ...`) hay flat? | PO | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-00, S-01, S-02, S-03 | 1.5 (stub) | 1.5 | All R + AC | Draft |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_qc_overview | test_stub_qc_overview | Add (cân nhắc N/A — Q-005) | All QC stubs (vì là gateway section) | Q-001..Q-006 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R004, AC-01..AC-04 | | ⏳ Chưa thiết kế | Section metadata — có thể skip test case hoặc chỉ smoke validate link (Q-005) |

## 🚧 Blocked Coverage

- R001 — chờ Q-003 (typo fix), Q-004 (bổ sung term)
- R002, R003 — chờ Q-001, Q-002 (scope Drive/Figma link)
- All R — chờ Q-005 (scope test cho section overview)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 18:45:00 | v1.1 | Refine stub → full spec: 4 R-ID, 4 AC, 3 BR, 0 messages, 6 questions Open. Section là metadata header — content tối thiểu, scope test có thể là N/A. `partial_read: false`. | refine-batch-3-2026-05-30 |
