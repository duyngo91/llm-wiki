---
aliases: [stub_qc_criteria_approval]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_qc_criteria_approval
project: project_hasaki
source_version: 1.5
source_doc: 07105_Quality_Control_Docs_ver1.5.md
source_range: 07105#L533-L562
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 22:50:00"
verification_status: Verified
approved_by:
approved_at:
approval_note:
---

# REQ: stub_qc_criteria_approval

## Tổng quan
- **Mã tính năng:** stub_qc_criteria_approval
- **Feature:** Duyệt / Từ chối / Mở lại tiêu chí QC cho SKU
- **Mô tả ngắn:** Tại màn hình quản lý danh sách tiêu chí thiết lập cho SKU, người có quyền có thể Duyệt hoặc Từ chối (bulk hoặc single dòng) các tiêu chí đang `Chờ duyệt`; sau khi đã duyệt/từ chối có thể Mở lại (single) để revert về `Open`.
- **Source chính:** 07105_Quality_Control_Docs_ver1.5.md (v1.5)
- **Đối tượng sử dụng (Actors):** Quản lý QC (role có quyền duyệt), User setup tiêu chí.
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** [[test_stub_qc_criteria_approval]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_qc_criteria_setup]] (state nguồn `Chờ duyệt`). ➡️ unlock [[stub_qc_criteria_sku]] khi tiêu chí được Approved.

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07105_Quality_Control_Docs_ver1.5.md | 1.5 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Raw không mô tả API explicit | N/A |

## Phân rã Requirement
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Màn hình quản lý danh sách tiêu chí thiết lập cho SKU hiển thị các dòng có status `Chờ duyệt` để xử lý duyệt | UI | High | ✅ | 07105#L534-L535 |
| R002 | Hỗ trợ 2 phương thức duyệt: bulk (tích chọn nhiều dòng) và single (chọn từng dòng) | Functional | High | ✅ | 07105#L536-L547 |
| R003 | Bulk Duyệt: hiển thị confirm dialog. Chọn `Yes` chuyển status các dòng đã chọn → `Đã duyệt` (Approved) | Functional | High | ✅ | 07105#L537-L542 |
| R004 | Bulk Từ chối: hiển thị confirm dialog. Chọn `Yes` chuyển status các dòng đã chọn → `Từ chối` (Rejected) | Functional | High | ✅ | 07105#L543-L546 |
| R005 | Single Duyệt: hiển thị confirm dialog chứa mã SKU. Chọn `Yes` chuyển status dòng → `Đã duyệt` | Functional | High | ✅ | 07105#L552-L554 |
| R006 | Single Từ chối: hiển thị confirm dialog chứa mã SKU. Chọn `Yes` chuyển status dòng → `Từ chối` | Functional | High | ✅ | 07105#L555-L557 |
| R007 | Single Mở lại (Reopen): hiển thị confirm dialog chứa mã SKU. Chọn `Yes` revert status → `Open` để user cập nhật lại thiết lập | Functional | High | ✅ | 07105#L558-L561 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- Tiêu chí QC cho SKU đã được setup và submit (status `Chờ duyệt`).
- User có quyền duyệt (role/permission chi tiết — xem Q-003).

### Luồng chuẩn (Happy Path) — Bulk Duyệt
1. User vào màn hình quản lý danh sách tiêu chí thiết lập cho SKU.
2. Filter / view các dòng status `Chờ duyệt` (R001).
3. Tích chọn nhiều dòng (R002).
4. Click button `Duyệt` (Approve).
5. Hệ thống hiển thị confirm dialog: `Do you want to confirm APPROVE setting criteria for SKUs of all selected lines?` (R003).
6. User chọn `Yes`.
7. Tất cả dòng đã chọn chuyển status → `Đã duyệt` (Approved).

### Luồng rẽ nhánh (Alternative Paths)

- **A1 — Bulk Từ chối:** giống Happy Path nhưng dùng button `Từ chối`; dialog EN `Do you want to confirm REJECT setting criteria for SKUs of all selected lines?`; status → `Từ chối` (R004).
- **A2 — Single Duyệt:** user chọn 1 dòng → button `Duyệt`; dialog `Do you want to confirm APPROVE criteria setup for SKU {sku_code}?` → status → `Đã duyệt` (R005).
- **A3 — Single Từ chối:** giống A2 nhưng button `Từ chối`; dialog `Do you want to confirm REJECT criteria setup for SKU {sku_code}?` → status → `Từ chối` (R006).
- **A4 — Mở lại (Reopen):** trên dòng đã `Đã duyệt` hoặc `Từ chối` (Q-002 cần clarify), user click `Mở lại`; dialog `Do you want to confirm RE-OPEN criteria setup for SKU {sku_code}?` → status → `Open` (R007).

### Luồng ngoại lệ (Exception Paths)
- **E1 — User không có quyền:** raw không mô tả message khi non-authorized user click Duyệt/Từ chối/Mở lại. Xem Q-003.
- **E2 — User chọn `No` / huỷ dialog:** raw không mô tả; assume dialog đóng, status không đổi (cần confirm — Q-004).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Status tiêu chí | enum | ✅ | Values quan sát được trong section: `Chờ duyệt`, `Đã duyệt` (Approved), `Từ chối` (Rejected), `Open`. Liệt kê đầy đủ → xem Q-001 (Q-001 ở stub criteria_setup) |
| Transition Approve | rule | ✅ | `Chờ duyệt` → `Đã duyệt` (bulk hoặc single) |
| Transition Reject | rule | ✅ | `Chờ duyệt` → `Từ chối` (bulk hoặc single) |
| Transition Reopen | rule | ✅ | `Đã duyệt` (và/hoặc `Từ chối` — Q-002) → `Open`. Chỉ single, không bulk (R007 vs R003/R004) |
| Confirm dialog | rule | ✅ | Mọi action (Approve/Reject/Reopen) đều require confirm dialog Yes/No |
| Permission duyệt | rule | ✅ | Chỉ "quản lý có quyền" được thao tác (R001 phrasing "Có 2 cách để quản lý có quyền có thể duyệt"). Role + check logic — xem Q-003 |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

> ⚠️ Raw chỉ cung cấp message **EN** cho 5 dialog (3 single + 2 bulk). Message **VN** không có trong raw — verify khi clarify với BA.

| Mã thông điệp | Loại | Trigger | Message EN (raw) | Message VN | Source |
|:-------------|:-----|:--------|:-----------------|:-----------|:-------|
| MSG-APR-001 | Confirm | Bulk Duyệt | `Do you want to confirm APPROVE setting criteria for SKUs of all selected lines?` | (chưa có — Q-005) | 07105#L540-L541 |
| MSG-APR-002 | Confirm | Bulk Từ chối | `Do you want to confirm REJECT setting criteria for SKUs of all selected lines?` | (chưa có — Q-005) | 07105#L544-L545 |
| MSG-APR-003 | Confirm | Single Duyệt | `Do you want to confirm APPROVE criteria setup for SKU {sku_code}?` | (chưa có — Q-005) | 07105#L553 |
| MSG-APR-004 | Confirm | Single Từ chối | `Do you want to confirm REJECT criteria setup for SKU {sku_code}?` | (chưa có — Q-005) | 07105#L556 |
| MSG-APR-005 | Confirm | Single Mở lại | `Do you want to confirm RE-OPEN criteria setup for SKU {sku_code}?` | (chưa có — Q-005) | 07105#L559 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Bulk Duyệt**
  - **Given:** Có ≥ 2 dòng status `Chờ duyệt` trong danh sách.
  - **When:** User tích chọn các dòng → click `Duyệt` → dialog hiện → chọn `Yes`.
  - **Then:** Tất cả dòng chuyển status → `Đã duyệt`. Dialog hiển thị nội dung MSG-APR-001 (R002, R003).
- **AC-02 — Bulk Từ chối**
  - **Given:** Có ≥ 2 dòng status `Chờ duyệt`.
  - **When:** User tích chọn → click `Từ chối` → dialog MSG-APR-002 → chọn `Yes`.
  - **Then:** Các dòng đã chọn chuyển status → `Từ chối` (R004).
- **AC-03 — Single Duyệt**
  - **Given:** 1 dòng status `Chờ duyệt` cho SKU `297500046`.
  - **When:** User click dòng → button `Duyệt` → dialog MSG-APR-003 (chứa SKU code) → chọn `Yes`.
  - **Then:** Dòng chuyển status → `Đã duyệt` (R005).
- **AC-04 — Single Từ chối**
  - **Given:** 1 dòng status `Chờ duyệt`.
  - **When:** User click dòng → button `Từ chối` → dialog MSG-APR-004 → chọn `Yes`.
  - **Then:** Dòng chuyển status → `Từ chối` (R006).
- **AC-05 — Single Mở lại**
  - **Given:** 1 dòng status `Đã duyệt` (hoặc `Từ chối` — chờ Q-002).
  - **When:** User click dòng → button `Mở lại` → dialog MSG-APR-005 → chọn `Yes`.
  - **Then:** Dòng revert status → `Open` để user cập nhật lại tiêu chí (R007).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R007 | Mở lại có áp dụng từ cả `Đã duyệt` lẫn `Từ chối`, hay chỉ 1 trong 2? Raw chỉ ghi "revert thành Open để user cập nhật lại". | PO | Open | | | |
| Q-002 | R002, R007 | Có bulk Mở lại không? Raw chỉ liệt kê Mở lại cho single (R007), bulk chỉ có Duyệt/Từ chối (R003/R004). | PO/UX | Open | | | |
| Q-003 | R001 | Role/permission chi tiết: ai được Duyệt/Từ chối/Mở lại? Raw nói "quản lý có quyền". Có check role middleware không? Khi non-authorized user click → behavior gì? | PO/Dev | Open | | | |
| Q-004 | E2 | User chọn `No` / đóng dialog → status không đổi (assume) hay có behavior nào khác? Raw không mô tả. | PO/UX | Open | | | |
| Q-005 | All MSG-APR-* | Verbatim message VN cho 5 dialog (raw chỉ cung cấp EN). | PO/UX | Open | | | |
| Q-006 | R005-R007 | Sau khi Mở lại, có ghi history (audit trail) bản duyệt cũ — ai duyệt khi nào? Hoặc reset toàn bộ thông tin duyệt? | PO/Dev | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-13 | 1.5 (stub) | 1.5 | All R + AC | Draft |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_qc_criteria_approval | test_stub_qc_criteria_approval | Add (chờ Gate 1B) | [[stub_qc_criteria_setup]] (state nguồn), [[stub_qc_criteria_sku]] (unlock khi Approved) | Q-001..Q-006 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R007, AC-01..AC-05 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-006 |

## 🚧 Blocked Coverage

- R007, AC-05 — chờ Q-001 (Mở lại từ Đã duyệt và/hoặc Từ chối), Q-002 (bulk Mở lại có hay không), Q-006 (audit history)
- R001, R002 — chờ Q-003 (role/permission detail + behavior unauthorized)
- E2 — chờ Q-004 (behavior khi `No` / cancel)
- MSG-APR-001..005 — chờ Q-005 (verbatim message VN)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:36:55 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 15:40:00 | v1.1 | Refine stub → full spec: 7 R-ID, 5 AC, 6 BR, 5 confirm messages (EN only), 6 questions Open. `partial_read: false`. | refine-batch-1-2026-05-30 |
