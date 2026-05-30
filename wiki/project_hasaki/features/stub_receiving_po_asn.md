---
aliases: [stub_receiving_po_asn]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_asn
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L349-L520
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 17:00:00"
verification_status: Pending
approved_by:
approved_at:
approval_note:
---

# REQ: stub_receiving_po_asn

## Tổng quan
- **Mã tính năng:** stub_receiving_po_asn
- **Feature:** ASN list + detail + xem chi tiết sản phẩm
- **Mô tả ngắn:** Cập nhật màn `Inbound / ASN` (listing + detail). Listing bổ sung filter, columns, action button (`ReOpen`, in biên bản A5/Bill, xem biên bản upload), tuỳ chọn `In tất cả sản phẩm` và `Thiết lập khổ giấy`. Detail bổ sung `Đồng kiểm`, `Camera`, `Mã vị trí`; danh sách sản phẩm có rules `SL xác nhận/thực nhận/thiếu` theo phiên nhận. Update 16-09-2025: bổ sung Group UID đã nhận cho ASN.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Quản lý kho (xem listing + in biên bản), User scan nhận hàng (detail), Admin (ReOpen).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[test_stub_receiving_po_asn]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_receiving_po_inbound_shipment]] (filter `Đồng kiểm` move qua). ➡️ feed [[stub_qc_vas]] (Group UID ASN cho VAS).

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
| R001 | Màn `Inbound / ASN` với giao diện cập nhật filter + listing | UI | High | ✅ | 07062#L349-L351 |
| R002 | Filter `Mã ASN` (ASN number): tìm chính xác theo mã nhập vào | UI filter | High | ✅ | 07062#L358 |
| R003 | Filter `Mã phiếu nhập` (Inbound shipment), `Phiếu nhập nguồn` (Inbound source mapping), `Mã phiếu xuất` (Outbound order), `Phiếu xuất nguồn` (Outbound source mapping) | UI filter | High | ✅ | 07062#L359-L365 |
| R004 | Filter `Kho` (Warehouse): load theo location + phân quyền user; hỗ trợ chọn nhiều; gợi ý khi user nhập ≥ 3 ký tự | UI filter | High | ✅ | 07062#L366-L368 |
| R005 | Filter `SKU, Barcode`: tìm theo SKU hoặc Barcode trong chi tiết của ASN | UI filter | High | ✅ | 07062#L369-L370 |
| R006 | Filter `Loại` (Type): multi-select; values `Purchase order`, `Customer return`, `Internal transfer`, `Adjustment` | UI filter | High | ✅ | 07062#L371-L377 |
| R007 | Filter `Người sở hữu` (Owner): multi-select; values `Hasaki Cosmetics`, `Hasaki WMS`, `Hasaki OMS` | UI filter | High | ✅ | 07062#L378-L383 |
| R008 | Filter `Trạng thái` (Status): multi-select; values `Mới/Open`, `Đang nhận hàng/Receiving`, `Đã nhận hàng/Received`, `Đã huỷ/Canceled` | UI filter | High | ✅ | 07062#L384-L395 |
| R009 | Filter `Đồng kiểm` (Check of goods): values Yes/No (move sang ASN từ Inbound shipment per `stub_receiving_po_inbound_shipment` R001) | UI filter | High | ✅ | 07062#L396 |
| R010 | Filter `Từ ngày…Đến ngày` (From date…To date) | UI filter | High | ✅ | 07062#L398 |
| R011 | Listing bổ sung tuỳ chọn `In tất cả sản phẩm` (Print all product): mặc định chỉ in những sản phẩm có khai báo thiếu hoặc SPKPH; nếu tích chọn thì in hết tất cả sản phẩm đã nhận trong ASN | UI + Business rule | High | ✅ | 07062#L402-L406 |
| R012 | Listing bổ sung tuỳ chọn `Thiết lập khổ giấy` (Set paper size): values `A5` (template A5) và `In Bill` (template in Bill); default `A5` | UI + Enum | High | ✅ | 07062#L407-L414 |
| R013 | Lưu chọn khổ giấy theo máy tính local (1 lần chọn áp dụng cho sau đó cho tới khi thay đổi) | Business rule | Medium | ✅ | 07062#L415-L416 |
| R014 | Listing columns: `Mã ASN`, `Kho`, `Loại`, `Mã phiếu nhập`, `Phiếu nhập nguồn`, `Mã phiếu xuất`, `Phiếu xuất nguồn`, `Người sở hữu`, `Đồng kiểm`, `Mã camera`, `Mã vị trí`, `Mã giỏ`, `Ngày tạo` (format `YYYY-MM-DD HH:MM`; người tạo email Hasaki), `Ngày cập nhật`, `Trạng thái`, `Thao tác` | UI | High | ✅ | 07062#L417-L443 |
| R015 | Listing column `Thao tác` (Action) — button **ReOpen**: reopen ASN về trạng thái `Open` và xoá nhân viên ra khỏi ASN. Chỉ show khi trạng thái = `Receiving` **và** user chưa scan nhận item nào. Confirm dialog EN: `Do you want to ReOpen for ticket ASN {asn_code}?` | Functional + State | High | ✅ | 07062#L441-L449 |
| R016 | Listing column `Thao tác` — button **In biên bản xác nhận nhận hàng** với nhà cung cấp. Chỉ show khi trạng thái = `Receiving` hoặc `Received` | Functional | High | ✅ | 07062#L450-L452 |
| R017 | Listing column `Thao tác` — button **Xem biên bản giao hàng** mà user upload lên khi nhận hàng cho PO | Functional | High | ✅ | 07062#L453-L454 |
| R018 | Template biên bản: A5 và In Bill. Lưu ý: thông tin `Số hoá đơn` trong template lấy cột `Taxcode` trên Inside. Taxcode có thể trùng nếu là PO gift và PO gốc | Business rule | High | ✅ | 07062#L455-L465 |
| R019 | ASN detail — Thông tin chung bổ sung 3 field: `Đồng kiểm / Check of goods`, `Camera`, `Mã vị trí / Location code` | UI | High | ✅ | 07062#L468-L476 |
| R020 | ASN detail — Danh sách sản phẩm columns: `SKU`, `Barcode`, `Sản phẩm/Product name`, `SL xác nhận/Qty confirm`, `SL thực nhận/Qty received`, `SL thiếu/Qty missing`, `Vị trí/Location`, `Mô tả/Description`, `Trạng thái/Status` | UI | High | ✅ | 07062#L477-L510 |
| R021 | ASN detail — `SL xác nhận`: SL của SKU theo PO; nếu 1 PO có nhiều phiên nhận thì vẫn ghi nhận theo SL trên PO (không bị giảm dần qua phiên) | Business rule | High | ✅ | 07062#L482-L484 |
| R022 | ASN detail — `SL thực nhận`: SL thực nhận theo phiên nhận hàng (per-session, không cumulative) | Business rule | High | ✅ | 07062#L485-L487 |
| R023 | ASN detail — `SL thiếu`: SL còn thiếu so với PO; nếu 1 PO có nhiều phiên nhận thì ghi nhận SL thiếu còn lại theo phiên nhận (decremental). VD: SKU PO=10, lần 1 giao 5 → SL thiếu = 5; lần 2 giao 3 → SL thiếu = 2 | Formula + Business rule | High | ✅ | 07062#L488-L495 |
| R024 | ASN detail — `Vị trí`: mã bin user scan để nhận hàng với Shop 170 và Kho 170; với Shop thì default chuyển vào location mặc định | Business rule | High | ✅ | 07062#L496-L498 |
| R025 | ASN detail — `Mô tả`: hiện thông tin khi user khai báo lý do thiếu trên App, gồm `Lý do thiếu`, `Tình trạng hàng hoá (nếu có)`, `Nhà cung cấp giao bù`, `Ghi chú` | UI | High | ✅ | 07062#L499-L508 |
| R026 | Update 16-09-2025: ASN detail bổ sung thông tin `Group UID đã nhận` cho ASN | Functional | High | ✅ | 07062#L512-L513 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- ASN đã được tạo trên WMS từ luồng scan nhận PO.
- User có quyền truy cập menu `Inbound / ASN`.

### Luồng chuẩn (Happy Path) — Listing + Action
1. User vào menu `Inbound / ASN`.
2. Áp filter (R002-R010) — vd: `Mã ASN` = `1002240906000004`, `Trạng thái` = `Receiving`, `Đồng kiểm` = `Yes`.
3. Hệ thống trả listing với 16 columns (R014).
4. User chọn tuỳ chọn `Thiết lập khổ giấy = In Bill` (R012) → setting lưu local (R013).
5. Click action `In biên bản xác nhận nhận hàng` cho 1 ASN (R016) → in theo template `In Bill` (R018).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — ReOpen ASN:** ASN status `Receiving` **và** user chưa scan item nào → button ReOpen show → click → dialog `Do you want to ReOpen for ticket ASN {asn_code}?` → confirm → ASN về `Open` + xoá employee assignment (R015).
- **A2 — In tất cả sản phẩm:** tích `In tất cả sản phẩm` → biên bản in cả những SKU không có khai báo thiếu/SPKPH (R011).
- **A3 — Xem biên bản giao hàng upload:** click action xem (R017).
- **A4 — Detail Group UID (Update 16-09-2025):** ASN detail có thêm thông tin Group UID đã nhận (R026).

### Luồng ngoại lệ (Exception Paths)
- **E1 — Cố ReOpen ASN sau khi đã scan item:** button ReOpen không show (R015); user phải undo từng item trước (raw không mô tả undo flow — Q-001).
- **E2 — Taxcode trùng giữa PO gift và PO gốc:** Số hoá đơn trong biên bản hiển thị cùng giá trị; raw không mô tả disambiguate — Q-002.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Filter `Mã ASN` | string | ❌ | Tìm exact match |
| Filter `Kho` | multi-select | ❌ | Load theo location + phân quyền; gợi ý từ 3 ký tự |
| Filter `Loại` enum | enum | ❌ | 4 values: PO, CR, IT, Adjustment |
| Filter `Người sở hữu` enum | enum | ❌ | 3 values: Hasaki Cosmetics, WMS, OMS |
| Filter `Trạng thái` enum | enum | ❌ | 4 values: Open, Receiving, Received, Canceled |
| Listing options | rule | ❌ | `In tất cả sản phẩm` default OFF; `Thiết lập khổ giấy` default A5; lưu local |
| ReOpen condition | rule | ✅ | Status = `Receiving` **AND** chưa scan item |
| In biên bản — visibility | rule | ✅ | Show khi status ∈ {`Receiving`, `Received`} |
| Số hoá đơn trong biên bản | rule | ✅ | Map từ Inside `Taxcode`; có thể trùng giữa PO gift và PO gốc |
| `SL xác nhận` (per SKU) | rule | ✅ | = SL trên PO (không decrement theo phiên) |
| `SL thực nhận` (per phiên) | rule | ✅ | Theo phiên nhận, không cumulative |
| `SL thiếu` (per phiên) | formula | ✅ | = (SL PO - sum(SL thực nhận đã có)) — decremental qua các phiên |
| Vị trí default Shop | rule | ✅ | Shop → default location mặc định; Kho → user scan bin |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã thông điệp | Loại | Trigger | Message VN | Message EN | Source |
|:-------------|:-----|:--------|:-----------|:-----------|:-------|
| MSG-ASN-001 | Confirm | Click ReOpen cho ASN `Receiving` chưa scan item | (chưa có VN — Q-005) | `Do you want to ReOpen for ticket ASN {asn_code}?` | 07062#L448-L449 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Filter Mã ASN exact match**
  - **Given:** Listing có ASN_1002240906000004 và ASN_1002240906000005.
  - **When:** User nhập `1002240906000004`.
  - **Then:** Chỉ ASN_1002240906000004 xuất hiện (R002).
- **AC-02 — Filter Kho gợi ý từ 3 ký tự**
  - **Given:** Filter Kho mở.
  - **When:** User nhập "K1" (2 chars).
  - **Then:** Chưa gợi ý; nhập "K10" (3 chars) → suggestion xuất hiện (R004).
- **AC-03 — Filter Loại multi-select**
  - **Given:** ASN_A type PO, ASN_B type Customer return.
  - **When:** Filter chọn `Purchase order` + `Customer return`.
  - **Then:** Cả 2 xuất hiện (R006).
- **AC-04 — Filter Đồng kiểm Yes**
  - **Given:** ASN_X `Đồng kiểm = Yes`, ASN_Y = No.
  - **When:** Filter `Đồng kiểm = Yes`.
  - **Then:** Chỉ ASN_X (R009).
- **AC-05 — `In tất cả sản phẩm` default OFF**
  - **Given:** Listing options.
  - **When:** User chưa tích.
  - **Then:** Biên bản chỉ in SKU có khai báo thiếu hoặc SPKPH (R011).
- **AC-06 — Thiết lập khổ giấy lưu local**
  - **Given:** User chọn `In Bill` trên máy tính A.
  - **When:** User in biên bản lần 2.
  - **Then:** Áp dụng `In Bill` (R012, R013); trên máy B vẫn default `A5`.
- **AC-07 — ReOpen show khi Receiving + chưa scan**
  - **Given:** ASN_X status `Receiving`, chưa scan item.
  - **When:** User mở listing.
  - **Then:** Button ReOpen show (R015).
- **AC-08 — ReOpen ẩn khi đã scan**
  - **Given:** ASN_Y status `Receiving`, đã scan 1 item.
  - **When:** User mở listing.
  - **Then:** Button ReOpen không show (R015).
- **AC-09 — ReOpen confirm dialog**
  - **Given:** User click ReOpen cho ASN_X.
  - **When:** Dialog MSG-ASN-001 → click `Yes`.
  - **Then:** ASN_X về `Open` + xoá employee assignment (R015).
- **AC-10 — In biên bản A5 default**
  - **Given:** ASN status `Received`, khổ giấy default A5.
  - **When:** User click `In biên bản`.
  - **Then:** Print template A5 (R012, R016).
- **AC-11 — Số hoá đơn từ Taxcode**
  - **Given:** PO_A có Taxcode `TX-001`.
  - **When:** User in biên bản.
  - **Then:** Số hoá đơn = `TX-001` (R018).
- **AC-12 — Detail thông tin chung bổ sung**
  - **Given:** ASN_X có `Đồng kiểm = Yes`, Camera, Mã vị trí.
  - **When:** User mở ASN detail.
  - **Then:** Section Thông tin chung hiển thị 3 field (R019).
- **AC-13 — SL xác nhận giữ nguyên qua phiên**
  - **Given:** PO_A có SKU_X SL = 10; phiên 1 nhận 5.
  - **When:** User mở ASN detail phiên 2.
  - **Then:** SL xác nhận = 10 (R021).
- **AC-14 — SL thực nhận per phiên**
  - **Given:** PO_A SKU_X PO=10. Phiên 1 nhận 5, phiên 2 nhận 3.
  - **When:** User mở ASN detail phiên 2.
  - **Then:** SL thực nhận = 3 (R022).
- **AC-15 — SL thiếu decremental**
  - **Given:** Như AC-14.
  - **When:** User mở ASN detail phiên 2.
  - **Then:** SL thiếu = 10 - 5 - 3 = 2 (R023).
- **AC-16 — Vị trí default cho Shop**
  - **Given:** Shop 170 không yêu cầu scan bin.
  - **When:** ASN tạo cho Shop 170.
  - **Then:** Vị trí default = location mặc định (R024).
- **AC-17 — Mô tả khai báo thiếu**
  - **Given:** User trên App đã khai báo 4 thông tin (lý do, tình trạng, NCC giao bù, ghi chú).
  - **When:** Mở ASN detail.
  - **Then:** Column Mô tả hiển thị đủ 4 thông tin (R025).
- **AC-18 — Detail Group UID (Update 16-09-2025)**
  - **Given:** ASN_X có Group UID UID-G-1, UID-G-2.
  - **When:** Mở ASN detail.
  - **Then:** Hiển thị Group UID đã nhận (R026).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R015, E1 | ASN đã scan item, user muốn ReOpen — workflow undo item như thế nào (xoá từng item, hay phải cancel ASN tạo mới)? | PO | Open | | | |
| Q-002 | R018, E2 | Khi Taxcode trùng giữa PO gift và PO gốc, biên bản hiển thị thế nào — gom chung số hoá đơn hay hiển thị label riêng (PO gift/gốc)? | PO | Open | | | |
| Q-003 | R007 | Owner enum `Hasaki Cosmetics`, `Hasaki WMS`, `Hasaki OMS` — còn entity nào khác (vd `Hasaki Inside`) hay chỉ 3? | PO | Open | | | |
| Q-004 | R013 | "Lưu theo máy tính local" — cookie / localStorage / IndexedDB? Scope theo user account hay theo browser session? | Dev | Open | | | |
| Q-005 | R015, MSG-ASN-001 | Verbatim VN cho confirm dialog ReOpen (raw chỉ EN). | PO | Open | | | |
| Q-006 | R019 | `Camera` field trong ASN detail — lưu mã camera đã scan QC, hay flag Yes/No đã chụp? | PO | Open | | | |
| Q-007 | R023 | Formula `SL thiếu` per phiên — nếu phiên 3 NCC giao bù phần thiếu phiên 1, SL thiếu được tính lại ngược ra sao? | PO | Open | | | |
| Q-008 | R024 | "Shop 170 và Kho 170" — hardcoded hay là 2 trong số nhiều Shop/Kho áp rule này? Config danh sách? | PO/Dev | Open | | | |
| Q-009 | R026 | Update 16-09-2025 "Group UID đã nhận" — chỉ display in detail, hay có filter/search Group UID? | UX | Open | | | |
| Q-010 | R025 | Khi không có khai báo lý do thiếu (PO bình thường), Mô tả trống hay placeholder text? | UX | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-07, S-08, S-09 | 2.17 (stub) | 2.17 | All R + AC | Draft |
| CHG-002 | Update | Update 16-09-2025: bổ sung Group UID đã nhận cho ASN | (trước 2.4) | 2.4 | R026, AC-18 | Done (đã trong raw v2.17) |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_asn | test_stub_receiving_po_asn | Add (chờ Gate 1B) | [[stub_receiving_po_inbound_shipment]] (filter Đồng kiểm), [[stub_qc_vas]] (Group UID feed), [[stub_receiving_po_invoice]] (Taxcode trong biên bản) | Q-001..Q-010 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R026, AC-01..AC-18 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-010 |

## 🚧 Blocked Coverage

- R015, E1 — chờ Q-001 (undo flow)
- R018, E2 — chờ Q-002 (Taxcode duplicate handling)
- R007 — chờ Q-003 (Owner enum đầy đủ)
- R013 — chờ Q-004 (storage mechanism)
- R015, MSG-ASN-001 — chờ Q-005 (verbatim VN)
- R019 — chờ Q-006 (Camera field semantics)
- R023 — chờ Q-007 (formula SL thiếu boundary)
- R024 — chờ Q-008 (Shop/Kho 170 scope)
- R026 — chờ Q-009 (filter/search Group UID)
- R025 — chờ Q-010 (Mô tả khi không khai báo)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:36:55 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 17:00:00 | v1.1 | Refine stub → full spec: 26 R-ID, 18 AC, 13 BR, 1 message (EN-only), 10 questions Open. `partial_read: false`. | refine-batch-2-2026-05-30 |
