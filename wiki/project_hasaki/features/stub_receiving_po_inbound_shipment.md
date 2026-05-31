---
aliases: [stub_receiving_po_inbound_shipment]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_inbound_shipment
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L224-L347
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 21:52:17"
verification_status: Verified
approved_by:
approved_at:
approval_note:
last_verified_source_version: 2.17

---

# REQ: stub_receiving_po_inbound_shipment

## Tổng quan
- **Mã tính năng:** stub_receiving_po_inbound_shipment
- **Feature:** Inbound Shipment listing + detail (Web)
- **Mô tả ngắn:** Cập nhật màn hình `Inbound / Inbound Shipment` (listing + detail). Bổ sung filter, listing columns, mapping status PO Inside ↔ WMS, WMS status riêng, sample description messages khi PO không đủ điều kiện nhận; detail bổ sung `Đủ điều kiện nhận`, `Mô tả`, đổi label SL, thêm section `Giải trình lý do treo PO`.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Quản lý kho (xem listing + detail), User scan nhận (giải trình trong detail).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[ts_receiving_po_inbound_shipment]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ➡️ feed [[stub_receiving_po_asn]] (filter `Đồng kiểm` move qua ASN). ⬅️ phụ thuộc Inside (mapping status), [[stub_receiving_po_invoice]] (PO chưa xác nhận hoá đơn).

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
| R001 | Màn hình `Inbound / Inbound Shipment` bổ sung filter `Đồng kiểm` (Check of goods) trong more filter; giá trị Yes/No; filter này được move qua trang ASN | UI filter | High | ✅ | 07062#L227-L231 |
| R002 | Bổ sung filter `Đủ điều kiện nhận` (Eligible to receive) trong more filter; giá trị Yes/No | UI filter | High | ✅ | 07062#L232 |
| R003 | Bổ sung filter `Trạng thái WMS` (WMS status), chỉ áp dụng cho `Type = PO`, hỗ trợ chọn nhiều; values: `Mới/Open`, `Đang nhận hàng/Receiving`, `Đã nhận hàng/Received`, `Hoàn thành/Completed`, `Đã huỷ/Canceled` | UI filter | High | ✅ | 07062#L233-L240 |
| R004 | Listing column `Đồng kiểm` (Check of goods): hiển thị PO có đồng kiểm hay không, lấy thông tin từ lựa chọn của user khi scan nhận PO | UI listing | High | ✅ | 07062#L244-L246 |
| R005 | Listing column `Đủ điều kiện nhận` (Eligible to receive): hiển thị Yes/No | UI listing | High | ✅ | 07062#L247-L248 |
| R006 | Listing column `Mô tả` (Description): mô tả lý do PO không đủ điều kiện nhận, hỗ trợ song ngữ VN/EN | UI listing | High | ✅ | 07062#L249-L250 |
| R007 | Hỗ trợ sample messages cho `Mô tả` (case không đủ điều kiện nhận): `PO chưa được xác nhận / PO not verifed`; `PO chưa được duyệt / PO not approved`; `PO chưa được xác nhận hoá đơn / PO not yet verified invoice`; `SKU tester {sku_code} chưa khai báo SKU gốc / SKU Tester {sku_code} does not have original SKU` | Enum / messages | High | ✅ | 07062#L255-L262 |
| R008 | Listing column `Trạng thái` (Status): bổ sung đầy đủ status PO trên Inside; hỗ trợ chọn nhiều (filter) | UI listing | High | ✅ | 07062#L264-L272 |
| R009 | Mapping status PO Inside ↔ WMS theo bảng: `Verified` >> `Mới/Open`; `Receiving` << `Đang nhận hàng/Receiving`; `Received` << `Đã nhận hàng/Received`; `Cancel` >> `Đã huỷ/Canceled` | Business rule | High | ✅ | 07062#L266-L271 |
| R010 | Với status `Receiving` của PO: hệ thống bổ sung hiển thị thời gian đã bao lâu chưa hoàn thành nhận hàng (tính từ thời điểm bắt đầu scan PO); mục đích là quản lý thời gian nhận hàng để cuối ngày user phải giải trình | UI + Business rule | High | ✅ | 07062#L273-L276, 07062#L291-L295 |
| R011 | Listing column `Trạng thái WMS` (WMS status): chỉ sử dụng cho `Type = PO`, là status riêng của WMS (khác Inside status) | UI listing | High | ✅ | 07062#L277-L278 |
| R012 | Định nghĩa WMS status (cho Type=PO): `Mới/Open` (PO được tạo mới trên WMS); `Đang nhận hàng/Receiving` (user scan PO để nhận hàng trên App); `Đã nhận hàng/Received` (PO hoàn thành nhận hàng trên App); `Đã huỷ/Canceled` (PO bị huỷ trên Inside) | Enum + state transition | High | ✅ | 07062#L279-L290 |
| R013 | Inbound shipment detail — Thông tin chung bổ sung 2 field mới: `Đủ điều kiện nhận / Eligible to receive` và `Mô tả / Description` | UI | High | ✅ | 07062#L303-L307 |
| R014 | Inbound shipment detail — Danh sách sản phẩm: đổi column `Số lượng` thành `Số lượng xác nhận / Qty confirm` (theo inbound) | UI | High | ✅ | 07062#L310-L315 |
| R015 | Inbound shipment detail — Danh sách sản phẩm column `Số lượng đã nhận / Qty received`: tổng SL đã scan nhận theo ASN | UI | High | ✅ | 07062#L316 |
| R016 | Inbound shipment detail — Danh sách sản phẩm column `Số lượng thiếu / Qty missing`: = `Số lượng xác nhận` − `Số lượng đã nhận` | Formula | High | ✅ | 07062#L317 |
| R017 | Inbound shipment detail — Section `Giải trình lý do treo PO`: nếu PO giao trong ngày nhưng vẫn chưa chuyển `Đã nhận hàng` → user vào giải trình lý do PO bị treo receiving | Functional | High | ✅ | 07062#L320-L321 |
| R018 | Giải trình section — sắp xếp giảm dần theo thời gian tạo | UI | Medium | ✅ | 07062#L322 |
| R019 | Giải trình section — column `Bình luận / Comment`: user nhập nội dung; button `Thêm` để cập nhật. Button `Thêm` hiện ở bất kỳ status PO nào | Functional | High | ✅ | 07062#L326-L329 |
| R020 | Giải trình section — columns: `TT/No` (STT tăng dần), `Nội dung/Content` (nội dung đã thêm), `Người tạo/Created by` (Email HSK), `Ngày tạo/Created date` (thời gian thêm) | UI | High | ✅ | 07062#L330-L339 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- Inbound shipment đã được tạo trên Inside / WMS.
- User có quyền truy cập menu `Inbound / Inbound Shipment`.

### Luồng chuẩn (Happy Path) — Listing
1. User vào menu `Inbound / Inbound Shipment`.
2. Click `More filter` → áp filter `Đồng kiểm = Yes` (R001), `Đủ điều kiện nhận = Yes` (R002), `Trạng thái WMS = Đang nhận hàng` (R003 — multi-select cho phép thêm value khác).
3. Hệ thống trả về listing với các columns: `Đồng kiểm`, `Đủ điều kiện nhận`, `Mô tả`, `Trạng thái`, `Trạng thái WMS` (R004-R006, R008, R011).
4. Mỗi PO đang `Receiving` hiển thị thời gian đã bao lâu chưa hoàn thành (R010).

### Luồng chuẩn (Happy Path) — Detail
1. User click vào 1 PO trong listing → mở Inbound shipment detail.
2. Section `Thông tin chung` hiển thị 2 field mới `Đủ điều kiện nhận`, `Mô tả` (R013).
3. Section `Danh sách sản phẩm` hiển thị columns `Số lượng xác nhận`, `Số lượng đã nhận`, `Số lượng thiếu` (R014-R016).
4. Nếu PO giao trong ngày mà chưa `Đã nhận hàng` → user click `Thêm` trong section `Giải trình lý do treo PO`, nhập comment, submit (R017, R019).
5. Comment được hiển thị sắp xếp giảm dần theo thời gian tạo, kèm `TT`, `Nội dung`, `Người tạo`, `Ngày tạo` (R018, R020).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — PO không đủ điều kiện nhận:** column `Đủ điều kiện nhận = No`, `Mô tả` hiển thị 1 trong các message R007 (vd `PO chưa được duyệt`).
- **A2 — Filter `Trạng thái WMS` áp dụng cho non-PO type:** filter không có effect (chỉ áp cho Type=PO theo R011).
- **A3 — Inside `Verified` chuyển WMS `Mới/Open`:** transition theo R009 mapping table.

### Luồng ngoại lệ (Exception Paths)
- **E1 — Cuối ngày user chưa giải trình PO `Receiving`:** raw không mô tả enforcement (block / nhắc nhở / báo cáo). Xem Q-002.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Filter `Đồng kiểm` | enum | ❌ | Values: `Yes` / `No` (R001) |
| Filter `Đủ điều kiện nhận` | enum | ❌ | Values: `Yes` / `No` (R002) |
| Filter `Trạng thái WMS` (Type=PO only) | multi-select enum | ❌ | Values: `Mới/Open`, `Đang nhận hàng/Receiving`, `Đã nhận hàng/Received`, `Hoàn thành/Completed`, `Đã huỷ/Canceled`. **Inconsistency:** filter có 5 values nhưng định nghĩa WMS status (R012) chỉ có 4 values (không có `Hoàn thành/Completed`) → Q-001 |
| `Đủ điều kiện nhận` (listing column) | enum | ✅ | `Yes` hoặc `No` |
| `Mô tả` (listing column) | enum / dynamic text | ⚠️ | Hiển thị 1 trong 4 sample messages R007; `SKU tester {sku_code}` có placeholder dynamic — Q-003 |
| Mapping Inside ↔ WMS status | rule | ✅ | Theo bảng R009. `>>` = Inside push tới WMS; `<<` = WMS push lại Inside |
| Hiển thị thời gian status `Receiving` | UI calculation | ✅ | Format chưa rõ — Q-004; tính từ thời điểm scan PO đầu tiên |
| Giải trình trigger condition | rule | ✅ | "PO giao trong ngày" — định nghĩa ngày — Q-005 |
| Button `Thêm` (giải trình) | UI rule | ✅ | Hiện ở mọi status PO |
| `Số lượng thiếu` | formula | ✅ | = `Số lượng xác nhận` − `Số lượng đã nhận` |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

> Section S-05 không có error message — chỉ có sample text cho column `Mô tả` (đã liệt kê trong R007 và bảng dưới đây).

| Mã message | Loại | Trigger | Message VN | Message EN | Source |
|:-----------|:-----|:--------|:-----------|:-----------|:-------|
| DESC-INS-001 | Description (Eligible=No) | PO chưa xác nhận | `PO chưa được xác nhận` | `PO not verifed` | 07062#L255 |
| DESC-INS-002 | Description (Eligible=No) | PO chưa duyệt | `PO chưa được duyệt` | `PO not approved` | 07062#L257 |
| DESC-INS-003 | Description (Eligible=No) | PO chưa xác nhận hoá đơn | `PO chưa được xác nhận hoá đơn` | `PO not yet verified invoice` | 07062#L258-L259 |
| DESC-INS-004 | Description (Eligible=No) | SKU tester chưa có SKU gốc | `SKU tester {sku_code} chưa khai báo SKU gốc` | `SKU Tester {sku_code} does not have original SKU` | 07062#L260-L262 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Filter `Đồng kiểm` Yes/No**
  - **Given:** Listing có PO_A `Đồng kiểm = Yes` và PO_B `Đồng kiểm = No`.
  - **When:** User áp filter `Đồng kiểm = Yes` trong more filter.
  - **Then:** Chỉ PO_A xuất hiện (R001).
- **AC-02 — Filter `Đủ điều kiện nhận` Yes/No**
  - **Given:** PO_A `Eligible = Yes`, PO_B `Eligible = No`.
  - **When:** Filter `Đủ điều kiện nhận = No`.
  - **Then:** Chỉ PO_B xuất hiện (R002).
- **AC-03 — Filter `Trạng thái WMS` multi-select cho Type=PO**
  - **Given:** PO_A WMS `Open`, PO_B WMS `Receiving`, Non-PO_C status không có WMS status.
  - **When:** Filter chọn `Open` + `Receiving`.
  - **Then:** Listing trả PO_A và PO_B; Non-PO_C không xuất hiện (R003, R011).
- **AC-04 — Listing column `Mô tả` cho PO Eligible=No**
  - **Given:** PO_X `Eligible = No` do chưa duyệt.
  - **When:** User mở listing.
  - **Then:** Column `Mô tả` hiển thị `PO chưa được duyệt / PO not approved` (R006, R007 DESC-INS-002).
- **AC-05 — Mapping Inside Verified → WMS Open**
  - **Given:** PO trên Inside chuyển sang status `Verified`.
  - **When:** Inside sync WMS.
  - **Then:** PO trên WMS có status = `Mới/Open` (R009).
- **AC-06 — Hiển thị thời gian PO `Receiving`**
  - **Given:** PO_Y bắt đầu scan nhận lúc 08:00, hiện 14:00.
  - **When:** User mở listing.
  - **Then:** Cột thời gian hiển thị `6 giờ` (hoặc format tương đương theo Q-004) (R010).
- **AC-07 — Detail bổ sung field `Đủ điều kiện nhận` + `Mô tả`**
  - **Given:** PO `Eligible = No`, `Mô tả = PO chưa được duyệt`.
  - **When:** User mở Inbound shipment detail.
  - **Then:** Section `Thông tin chung` hiển thị 2 field này với giá trị tương ứng (R013).
- **AC-08 — Detail formula `Số lượng thiếu`**
  - **Given:** SKU_A: `Số lượng xác nhận` = 100, `Số lượng đã nhận` = 60.
  - **When:** User xem danh sách sản phẩm trong detail.
  - **Then:** `Số lượng thiếu` = 40 (R016).
- **AC-09 — Giải trình section — nhập comment**
  - **Given:** PO bị treo `Receiving`.
  - **When:** User click `Thêm`, nhập "Chờ NCC giao tiếp", submit.
  - **Then:** Comment xuất hiện với `TT`, `Nội dung`, `Người tạo` (email HSK), `Ngày tạo` (R019, R020).
- **AC-10 — Giải trình section — sort giảm dần theo thời gian tạo**
  - **Given:** 3 comments tạo lúc T1, T2, T3 (T1 < T2 < T3).
  - **When:** User mở detail.
  - **Then:** Order hiển thị: T3, T2, T1 (R018).
- **AC-11 — Button `Thêm` hiện ở mọi status**
  - **Given:** PO có status `Đã nhận hàng / Received`.
  - **When:** User mở detail.
  - **Then:** Button `Thêm` vẫn hiển thị (R019).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R003 vs R012 | Filter WMS status có 5 values (`Hoàn thành/Completed` + 4 còn lại) nhưng bảng định nghĩa WMS status (R012) chỉ có 4 values (không có `Hoàn thành/Completed`). `Hoàn thành/Completed` có là WMS status thật hay chỉ là alias hiển thị của 1 status khác? | PO/Dev | Open | | | |
| Q-002 | R010, E1 | Cuối ngày nếu user chưa giải trình PO `Receiving` — hệ thống có chặn thao tác nào, nhắc nhở, hay report cho quản lý không? | PO | Open | | | |
| Q-003 | R007 DESC-INS-004 | `SKU tester {sku_code}` có placeholder dynamic — `{sku_code}` lấy từ SKU nào của PO (đầu tiên / tất cả)? Multi-SKU thì format thế nào? | PO/Dev | Open | | | |
| Q-004 | R010 | Format hiển thị "thời gian đã bao lâu" cho PO `Receiving` (HH:MM, số phút, số giờ, hay "X giờ Y phút")? | UX | Open | | | |
| Q-005 | R017 | "PO giao trong ngày" định nghĩa thế nào — ngày tạo PO, ngày dự kiến giao, hay ngày scan đầu tiên? | PO | Open | | | |
| Q-006 | R009 | Mapping status có direction `>>` (Inside push WMS) vs `<<` (WMS push Inside) — có conflict (vd Inside `Verified` sang WMS thành `Open`, nhưng nếu user WMS chuyển Open → Receiving thì Inside có cập nhật ngược không)? Logic sync 2 chiều rõ ràng chưa? | Dev | Open | | | |
| Q-007 | R004 | `Đồng kiểm` "lấy thông tin khi user chọn khi scan nhận PO" — input ở đâu trên App, mặc định Yes hay No, có sửa được không? | UX | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-05, S-06 | 2.17 (stub) | 2.17 | All R + AC | Draft |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_inbound_shipment | test_stub_receiving_po_inbound_shipment | Add (chờ Gate 1B) | [[stub_receiving_po_asn]] (filter Đồng kiểm move qua ASN), [[stub_receiving_po_invoice]] (PO chưa xác nhận hoá đơn) | Q-001..Q-007 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R020, AC-01..AC-11 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-007 |

## 🚧 Blocked Coverage

- R003, R012 — chờ Q-001 (resolve `Hoàn thành/Completed` enum inconsistency)
- R010, R017 — chờ Q-002 (enforcement giải trình), Q-004 (format thời gian), Q-005 (định nghĩa "trong ngày")
- R007 (DESC-INS-004) — chờ Q-003 (placeholder `{sku_code}` logic multi-SKU)
- R009 — chờ Q-006 (sync direction conflict)
- R004 — chờ Q-007 (Đồng kiểm input UI)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:36:55 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 16:05:00 | v1.1 | Refine stub → full spec: 20 R-ID, 11 AC, 10 BR, 4 description messages verbatim, 7 questions Open. `partial_read: false`. | refine-batch-2-2026-05-30 |
