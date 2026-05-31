---
aliases: [stub_receiving_po_no_barcode]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_no_barcode
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L1762-L1805
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 22:50:00"
verification_status: Verified
approved_by:
approved_at:
approval_note:
---

# REQ: stub_receiving_po_no_barcode

## Tổng quan
- **Mã tính năng:** stub_receiving_po_no_barcode
- **Feature:** Nhận hàng SKU không barcode (App)
- **Mô tả ngắn:** Bổ sung tiện ích cho user nhận hàng các SKU không có barcode trong PO bằng cách chọn từ danh sách (kèm search theo SKU/tên) thay vì phải nhập SKU thủ công. Update 31-07-2025 đổi UI: ẩn SL cần nhận, đổi tên thành "Số lượng thực nhận", thêm flow cảnh báo khi SL thực nhận khác SL cần nhận.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Nhân viên kho dùng App nhận hàng.
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[ts_receiving_po_no_barcode]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_receiving_po_app]] (UI scan PO trên App). ℹ️ liên quan [[stub_receiving_po_date_rules]] (rules HSD/số lô).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07062_Receiving_PO_Docs_ver2.17.md | 2.17 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Raw không mô tả API explicit | N/A |

## Phân rã Requirement
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Trên App, tại màn hình scan SKU để nhận hàng, bổ sung option `Nhận SKU không barcode` áp dụng cho tất cả category | UI | High | ✅ | 07062#L1763-L1767 |
| R002 | Chọn `Nhận SKU không barcode` → show danh sách các SKU không có barcode trong PO cần nhận hàng | Functional | High | ✅ | 07062#L1765-L1767 |
| R003 | Hỗ trợ tìm kiếm sản phẩm trong danh sách theo `SKU` hoặc `tên sản phẩm` | Functional | High | ✅ | 07062#L1768 |
| R004 | Mỗi item trong danh sách hiển thị: `SKU - Tên sản phẩm` và `Số lượng cần nhận` (ban đầu — sau Update 31-07-2025 ẩn — xem R008) | UI | High | ✅ | 07062#L1769-L1771 |
| R005 | SKU không config HSD và không config số lô: cho user nhập số lượng thực nhận ngay dưới thông tin SKU; click button `Nhận hàng` để xác nhận | Functional | High | ✅ | 07062#L1772-L1775 |
| R006 | SKU có config HSD hoặc số lô: không hiện số lượng nhập ngay; click vào SKU mở popup nhập: `Số lượng đã nhận`, `Hạn sử dụng`, `Số lô`; click `Nhận hàng` để xác nhận | Functional | High | ✅ | 07062#L1779-L1785 |
| R007 | Sau khi xác nhận SKU, ghi nhận vào danh sách SKU đã nhận cho PO; nếu vẫn còn SKU không barcode chưa nhận thì giữ tooltip để user tiếp tục nhận; nhấn ngoài để thoát | UI + Functional | High | ✅ | 07062#L1786-L1789 |
| R008 | Update 31-07-2025: ẩn thông tin `Số lượng cần nhận`; đổi label `SL` → `Số lượng thực nhận` | UI | High | ✅ | 07062#L1795-L1796 |
| R009 | Update 31-07-2025: nếu `Số lượng thực nhận` = `Số lượng cần nhận` → cập nhật vào danh sách đã nhận; nếu còn SKU không barcode → user nhận tiếp (giữ behavior hiện tại) | Business rule | High | ✅ | 07062#L1797-L1798 |
| R010 | Update 31-07-2025: nếu `Số lượng thực nhận` > `Số lượng cần nhận` → hiển thị thông báo đã có (raw ghi "đã có" — xem Q-002 để định danh message gốc) | Validation rule | High | ✅ | 07062#L1799 |
| R011 | Update 31-07-2025: nếu `Số lượng thực nhận` < `Số lượng cần nhận` → hiển thị confirm dialog `"Số lượng thực nhận nhỏ hơn số lượng của PO (300/400). Bạn có muốn xác nhận không?"` | Validation rule | High | ✅ | 07062#L1803-L1804 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User đã login App, đã mở phiên nhận PO trên App.
- PO chứa ≥ 1 SKU không có barcode.

### Luồng chuẩn (Happy Path) — SKU không config HSD/số lô (R005)
1. Tại màn hình scan SKU, user click `Nhận SKU không barcode` (R001).
2. App show danh sách SKU không barcode trong PO (R002).
3. User search theo SKU hoặc tên nếu cần (R003).
4. App hiển thị `SKU - Tên sản phẩm` (R004) và label nhập `Số lượng thực nhận` (R008).
5. User nhập SL thực nhận.
6. **Trường hợp SL thực nhận = SL cần nhận:** click `Nhận hàng` (R005) → ghi nhận vào danh sách đã nhận (R009).
7. Nếu còn SKU không barcode → giữ tooltip để user nhận tiếp (R007, R009).

### Luồng rẽ nhánh (Alternative Paths) — SKU có HSD/số lô (R006)
1. Sau bước 3 (Happy Path), user click vào SKU có config HSD/số lô.
2. App mở popup nhập: `Số lượng đã nhận`, `Hạn sử dụng`, `Số lô`.
3. User nhập đầy đủ → click `Nhận hàng`.
4. App ghi nhận vào danh sách đã nhận; tiếp tục như Happy Path bước 7.

### Luồng ngoại lệ (Exception Paths)
- **E1 — SL thực nhận > SL cần nhận:** App hiển thị thông báo đã có (R010, xem Q-002). Behavior block hay confirm chưa rõ — xem Q-002.
- **E2 — SL thực nhận < SL cần nhận:** App hiển thị confirm dialog R011: `"Số lượng thực nhận nhỏ hơn số lượng của PO (300/400). Bạn có muốn xác nhận không?"`. User chọn `Có` → ghi nhận; chọn `Không` → quay lại nhập SL (assume — xem Q-003).
- **E3 — User muốn thoát giữa chừng:** nhấn ngoài tooltip để thoát (R007).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| `Số lượng thực nhận` (SKU không HSD/số lô) | numeric | ✅ | Input số nguyên dương; so sánh với `Số lượng cần nhận`: =, >, < tương ứng R009, R010, R011 |
| `Số lượng đã nhận` (popup HSD/số lô) | numeric | ✅ | Input bắt buộc trong popup R006 |
| `Hạn sử dụng` (popup) | date | ⚠️ | Bắt buộc nếu SKU có config HSD; raw không khẳng định bắt buộc trong popup — xem Q-001 |
| `Số lô` (popup) | string | ⚠️ | Bắt buộc nếu SKU có config số lô; raw không khẳng định bắt buộc — xem Q-001 |
| Search filter | string | ❌ | Match theo `SKU` hoặc `tên sản phẩm`; raw không nói exact/partial — xem Q-005 |
| Tooltip retention | rule | ✅ | Tooltip giữ lại đến khi user nhận hết SKU không barcode hoặc tap ngoài để thoát |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Trigger | Message VN | Message EN | Source |
|:-------|:--------|:-----------|:-----------|:-------|
| ERR-NBC-001 | `Số lượng thực nhận` > `Số lượng cần nhận` | (raw ghi "thông báo đã có" — verbatim message phải tra cứu từ feature khác — xem Q-002) | (chưa có) | 07062#L1799 |
| MSG-NBC-002 | `Số lượng thực nhận` < `Số lượng cần nhận` (confirm dialog) | `Số lượng thực nhận nhỏ hơn số lượng của PO ({sl_thuc_nhan}/{sl_can_nhan}). Bạn có muốn xác nhận không?` | (chưa có — Q-002) | 07062#L1804 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Hiển thị option `Nhận SKU không barcode`**
  - **Given:** User mở màn hình scan SKU trên App cho PO có ≥ 1 SKU không barcode.
  - **When:** User xem màn hình.
  - **Then:** Có option `Nhận SKU không barcode` hiển thị (R001).
- **AC-02 — Danh sách SKU không barcode + search**
  - **Given:** PO có 3 SKU không barcode: `SKU_A` (apple), `SKU_B` (banana), `SKU_C` (cherry).
  - **When:** User chọn `Nhận SKU không barcode`, nhập "an" vào search.
  - **Then:** Danh sách hiển thị `SKU_A` (apple) và `SKU_B` (banana) — match theo tên (R002, R003).
- **AC-03 — Nhận SKU không config HSD/số lô**
  - **Given:** `SKU_A` không config HSD và số lô; `Số lượng cần nhận` = 100.
  - **When:** User nhập 100 vào `Số lượng thực nhận` → click `Nhận hàng`.
  - **Then:** Ghi nhận `SKU_A` qty=100 vào danh sách đã nhận; tooltip giữ nguyên nếu còn SKU không barcode (R005, R007, R009).
- **AC-04 — Nhận SKU có HSD/số lô**
  - **Given:** `SKU_B` có config HSD; `Số lượng cần nhận` = 50.
  - **When:** User click vào `SKU_B` → popup hiện → nhập `Số lượng đã nhận` = 50, `HSD` = 2026-12-31, `Số lô` = LOT_X → click `Nhận hàng`.
  - **Then:** Ghi nhận `SKU_B` với qty, HSD, Số lô vào danh sách đã nhận (R006).
- **AC-05 — Update 31-07-2025: label "Số lượng thực nhận" + ẩn SL cần nhận**
  - **Given:** Màn hình `Nhận SKU không barcode` sau update 31-07-2025.
  - **When:** User xem item trong danh sách.
  - **Then:** Hiển thị `Số lượng thực nhận` (không hiển thị `Số lượng cần nhận`) (R008).
- **AC-06 — SL thực nhận > SL cần nhận**
  - **Given:** `SKU_A` có `Số lượng cần nhận` = 100.
  - **When:** User nhập 120 vào `Số lượng thực nhận` → click `Nhận hàng`.
  - **Then:** App hiển thị thông báo đã có (R010, ERR-NBC-001).
- **AC-07 — SL thực nhận < SL cần nhận (confirm dialog)**
  - **Given:** `SKU_A` có `Số lượng cần nhận` = 400.
  - **When:** User nhập 300 vào `Số lượng thực nhận` → click `Nhận hàng`.
  - **Then:** App hiển thị confirm `Số lượng thực nhận nhỏ hơn số lượng của PO (300/400). Bạn có muốn xác nhận không?` (R011, MSG-NBC-002).
- **AC-08 — Thoát tooltip**
  - **Given:** Tooltip danh sách SKU không barcode đang mở.
  - **When:** User tap ra ngoài tooltip.
  - **Then:** Tooltip đóng (R007).
- **AC-09 — Tooltip giữ lại khi còn SKU chưa nhận**
  - **Given:** PO có 3 SKU không barcode, user vừa nhận xong 1 SKU.
  - **When:** User xác nhận thành công cho SKU đầu.
  - **Then:** Tooltip vẫn hiển thị 2 SKU còn lại để user tiếp tục nhận (R007).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R006 | Trong popup HSD/số lô (R006), các field `Hạn sử dụng` và `Số lô` có bắt buộc nhập không? Có validate format date / regex số lô không? | PO/Dev | Open | | | |
| Q-002 | R010, ERR-NBC-001 | Verbatim message VN+EN khi SL thực nhận > SL cần nhận (raw ghi "đã có" — refer message tồn tại từ feature nào)? MSG-NBC-002 có bản EN tương đương không? | PO | Open | | | |
| Q-003 | R011, MSG-NBC-002 | Khi user chọn `Không` trong confirm dialog MSG-NBC-002 → behavior gì (quay lại nhập, đóng popup, ...)? Raw không mô tả. | UX | Open | | | |
| Q-004 | R008 | Sau Update 31-07-2025 (ẩn SL cần nhận), case popup HSD/số lô (R006) có còn hiển thị `Số lượng cần nhận` trong popup không, hay cũng bị ẩn? | UX | Open | | | |
| Q-005 | R003 | Search match theo SKU/tên: exact match hay partial / case-insensitive / diacritic-insensitive? | UX/Dev | Open | | | |
| Q-006 | R002 | Danh sách SKU không barcode trong PO có pagination/scroll khi PO nhiều SKU không? Có sort default không? | UX | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-36, S-37 | 2.17 (stub) | 2.17 | All R + AC | Draft |
| CHG-002 | Update | Update 31-07-2025: ẩn `SL cần nhận`, đổi `SL` → `Số lượng thực nhận`, thêm flow > / < với message | (trước 2.10) | 2.10 | R008, R009, R010, R011 | Done (đã trong raw v2.17) |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_no_barcode | test_stub_receiving_po_no_barcode | Add (chờ Gate 1B) | [[stub_receiving_po_app]] (UI parent), [[stub_receiving_po_date_rules]] (HSD/số lô) | Q-001..Q-006 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R011, AC-01..AC-09 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-006 |

## 🚧 Blocked Coverage

- R006 — chờ Q-001 (HSD/Số lô bắt buộc + validation)
- R010, ERR-NBC-001 — chờ Q-002 (verbatim message > case)
- R011 — chờ Q-003 (behavior khi chọn `Không`)
- R008 — chờ Q-004 (popup vẫn hiển thị SL cần nhận không)
- R003 — chờ Q-005 (search semantics)
- R002 — chờ Q-006 (pagination + sort)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:36:55 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 15:55:00 | v1.1 | Refine stub → full spec: 11 R-ID, 9 AC, 6 BR, 2 messages (1 verbatim VN), 6 questions Open. `partial_read: false`. | refine-batch-1-2026-05-30 |
