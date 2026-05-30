---
aliases: [stub_qc_vas]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_qc_vas
project: project_hasaki
source_version: 1.5
source_doc: 07105_Quality_Control_Docs_ver1.5.md
source_range: 07105#L696-L780
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 16:30:00"
verification_status: Pending
approved_by:
approved_at:
approval_note:
---

# REQ: stub_qc_vas

## Tổng quan
- **Mã tính năng:** stub_qc_vas
- **Feature:** QC VAS updated — VAS type, status mở rộng, action `Mở lại`/`Nhận hàng`/`Trả nhà cung cấp`, group UID 10% cho SKU vải
- **Mô tả ngắn:** Cập nhật VAS list, detail, status enum, và 3 action chính (`Mở lại`, `Nhận hàng`, `Trả nhà cung cấp`) cho VAS `Chờ duyệt`. Bổ sung `VAS type` (IMEI, RFID, Quality Control, Other), filter + column data table. Update 18-09-2025: lấy 10% group UID của SKU vải để đánh giá CL.
- **Source chính:** 07105_Quality_Control_Docs_ver1.5.md (v1.5)
- **Đối tượng sử dụng (Actors):** QC user (đánh giá CL), Warehouse user (nhận hàng / trả NCC).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** [[test_stub_qc_vas]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_qc_evaluation_result]] (kết quả đánh giá đầu vào). ➡️ feed [[stub_receiving_po_confirm_paste_id]] (status `Chờ dán ID`). ⬅️ phụ thuộc [[stub_receiving_po_inbound_shipment]] (ASN cho 10% group UID).

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
| R001 | Bổ sung trường `Loại VAS` (VAS type) cho VAS mới tạo, gồm 4 values: `IMEI`, `RFID`, `Quality Control`, `Other` | Enum | High | ✅ | 07105#L697-L706 |
| R002 | Filter VAS theo `VAS type` (multi-select) | UI filter | High | ✅ | 07105#L700-L707 |
| R003 | Data table VAS bổ sung column `VAS type` | UI | High | ✅ | 07105#L708-L710 |
| R004 | Display VAS type multi-value: nếu VAS vừa có `Quality control` vừa có `RFID` hoặc `IMEI` → hiển thị cả 2 thông tin, cách nhau bởi dấu phẩy | UI rule | High | ✅ | 07105#L711-L712 |
| R005 | Bổ sung status enum cho VAS: `Mới/Open`, `Đang xử lý/In-Progress`, `Hoàn thành/Completed`, `Đã huỷ/Canceled`, `Chờ duyệt/Waiting for approval`, `Chờ dán ID/Wating for paste ID`, `Chờ đánh giá/Waiting quality control`, `Chờ NCC đến lấy/Waiting vendor to pick`, `Đã trả NCC/Returned to vendor` | Enum + state transition | High | ✅ | 07105#L713-L728 |
| R006 | Status `Đang xử lý/In-Progress` semantics: VAS đang được đánh giá hoặc đang thực hiện dán ID | Definition | High | ✅ | 07105#L719 |
| R007 | Status `Chờ duyệt/Waiting for approval` semantics: VAS sau khi đánh giá CL và có tiêu chí không đạt → chuyển trạng thái này | Definition + transition | High | ✅ | 07105#L722-L723 |
| R008 | Status `Chờ dán ID/Wating for paste ID` semantics: VAS chờ dán ID cho phiên nhận có SKU required IMEI hoặc RFID | Definition | High | ✅ | 07105#L724-L725 |
| R009 | Status `Chờ NCC đến lấy/Waiting vendor to pick` semantics: khi VAS được chọn (action Trả nhà cung cấp) | Definition + transition | High | ✅ | 07105#L727 |
| R010 | Với VAS status `Chờ duyệt`, user chọn mã VAS để vào detail xác nhận kết quả đánh giá; có 3 actions: `Mở lại (Re-Open)`, `Nhận hàng (Receive)`, `Trả nhà cung cấp (Return to vendor)` | Functional | High | ✅ | 07105#L734-L755 |
| R011 | Action `Mở lại (Re-Open)`: hiện confirm dialog `Do you want to confirm RECEIVE for the quality control of VAS {vas_code}?` (lưu ý từ "RECEIVE" trong dialog Re-Open — Q-001); chọn `Xác nhận` → kết quả đánh giá revert về `Mới (Open)` để đánh giá lại | Functional + State | High | ✅ | 07105#L737-L742 |
| R012 | Action `Nhận hàng (Receive)`: chọn `Xác nhận nhận hàng` → xác nhận tất cả tiêu chí Đạt (interpret = QC pass); cho phép xác nhận ngay cả khi vẫn có tiêu chí không đạt trong kết quả đánh giá | Functional + Business rule | High | ✅ | 07105#L743-L751 |
| R013 | Sau action `Nhận hàng (Receive)`: nếu SKU `required IMEI` hoặc `required RFID` → VAS chuyển status `Chờ dán ID / Wating for paste ID`; nếu không required → `Completed` | State transition | High | ✅ | 07105#L752-L754 |
| R014 | Action `Trả nhà cung cấp (Return to vendor)` mở dialog: nhập số lượng cần trả NCC; phase này mặc định trả hết SL đã nhận trong ASN (= SL đã nhận) và disable input | Functional + Business rule | High | ✅ | 07105#L755-L759 |
| R015 | Sau `Xác nhận` Trả nhà cung cấp: ghi nhận SL khai báo VAS và SL trả NCC; chuyển VAS status → `Chờ NCC đến lấy` | State transition | High | ✅ | 07105#L760-L762 |
| R016 | Sau khi NCC đến lấy hàng, user cập nhật VAS từ `Chờ NCC đến lấy` → `Đã trả NCC`; đồng thời tạo Outbound type `Return vendor` với info tương ứng | Functional + State | High | ✅ | 07105#L763-L767 |
| R017 | Yêu cầu tạo Adjustment type `Vendor Return` để out hàng khỏi kho — hiện tại Dev xác nhận **chưa thể tạo Adjustment cho case này** (gap đã biết) | Business rule | Medium | ⚠️ | 07105#L768-L771 |
| R018 | Update 18-09-2025: với SKU vải, type Quality control áp dụng tỉ lệ **10% group UID** trong ASN để đánh giá CL; làm tròn lên (ceil). VD: 25 group UID → 10% = 2.5 → 3 dòng VAS | Business rule + Formula | High | ✅ | 07105#L775-L780 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- VAS đã được tạo từ phiên nhận PO (xem [[stub_receiving_po_vas]]).
- Kết quả đánh giá CL đã được nhập (xem [[stub_qc_evaluation_result]]).

### Luồng chuẩn (Happy Path) — VAS `Chờ duyệt` → `Nhận hàng`
1. User vào danh sách VAS, filter `VAS type = Quality Control` + status `Chờ duyệt` (R002, R005).
2. Click mã VAS → mở detail (R010).
3. User review kết quả đánh giá. Tất cả tiêu chí Đạt hoặc user muốn vẫn nhận hàng dù có tiêu chí không đạt.
4. Click `Nhận hàng` → dialog confirm → click `Xác nhận nhận hàng` (R012).
5. **Branch theo SKU:**
   - SKU `required IMEI`/`required RFID` → VAS status → `Chờ dán ID / Wating for paste ID` (R013).
   - SKU không required → VAS status → `Completed` (R013).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — `Mở lại (Re-Open)`:** từ status `Chờ duyệt`, click `Mở lại` → dialog `Do you want to confirm RECEIVE for the quality control of VAS {vas_code}?` → `Xác nhận` → kết quả đánh giá revert về `Mới (Open)`, đánh giá lại (R011).
- **A2 — `Trả nhà cung cấp`:** click `Trả nhà cung cấp` → dialog hiện SL cần trả (mặc định = SL đã nhận, disable) → `Xác nhận` → VAS status `Chờ NCC đến lấy` (R014, R015).
- **A3 — `Đã trả NCC`:** sau khi NCC lấy hàng, user cập nhật status `Chờ NCC đến lấy` → `Đã trả NCC`; tạo Outbound type Return vendor (R016).
- **A4 — Multi VAS type (Quality Control + RFID/IMEI):** data table column `VAS type` hiển thị cả 2 cách nhau bởi dấu phẩy, vd `Quality Control, RFID` (R004).
- **A5 — SKU vải, áp 10% group UID:** tạo VAS đánh giá CL theo công thức `ceil(group_uid_count × 0.10)` (R018).

### Luồng ngoại lệ (Exception Paths)
- **E1 — Adjustment Vendor Return không tạo được:** workaround manual — current gap (R017). Q-003.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| `VAS type` | enum | ✅ | Values: `IMEI`, `RFID`, `Quality Control`, `Other` |
| Multi VAS type display | rule | ✅ | Multi-value: join bằng `, ` (dấu phẩy + space) |
| VAS status | enum | ✅ | 9 values: `Mới/Open`, `Đang xử lý/In-Progress`, `Hoàn thành/Completed`, `Đã huỷ/Canceled`, `Chờ duyệt/Waiting for approval`, `Chờ dán ID/Wating for paste ID`, `Chờ đánh giá/Waiting quality control`, `Chờ NCC đến lấy/Waiting vendor to pick`, `Đã trả NCC/Returned to vendor` |
| Transition `Chờ duyệt` → `Mở lại` | rule | ✅ | Dialog confirm; revert kết quả về `Mới (Open)`, không completed |
| Transition `Chờ duyệt` → `Nhận hàng` | rule | ✅ | Cho phép xác nhận pass dù có tiêu chí không đạt |
| Branch sau Nhận hàng | rule | ✅ | SKU required IMEI/RFID → `Chờ dán ID`; non-required → `Completed` |
| Số lượng trả NCC (phase 1) | rule | ✅ | Default = SL đã nhận trong ASN, **disable input** (user không thay đổi được) |
| Transition `Chờ NCC đến lấy` → `Đã trả NCC` | rule | ✅ | User manual cập nhật; tạo Outbound type `Return vendor` |
| Adjustment Vendor Return | rule | ⚠️ | Chưa tạo được, workaround chưa rõ — Q-003 |
| 10% group UID cho SKU vải | formula | ✅ | `vas_count = ceil(group_uid_count × 0.10)` cho SKU vải, type QC |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã thông điệp | Loại | Trigger | Message VN | Message EN | Source |
|:-------------|:-----|:--------|:-----------|:-----------|:-------|
| MSG-VAS-001 | Confirm | Click `Mở lại` cho VAS `Chờ duyệt` | (chưa có VN — Q-007) | `Do you want to confirm RECEIVE for the quality control of VAS {vas_code}?` (lưu ý từ "RECEIVE" — Q-001) | 07105#L739-L740 |
| MSG-VAS-002 | Confirm | Click `Nhận hàng` cho VAS `Chờ duyệt` | (chưa có — Q-007) | (chưa có — Q-007) | 07105#L743-L744 |
| MSG-VAS-003 | Confirm | Click `Trả nhà cung cấp` | (chưa có — Q-007) | (chưa có — Q-007) | 07105#L755-L756 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Filter VAS type multi-select**
  - **Given:** Listing có VAS_A type `IMEI`, VAS_B type `Quality Control`, VAS_C type `Other`.
  - **When:** Filter chọn `IMEI` + `Quality Control`.
  - **Then:** Listing trả VAS_A và VAS_B; VAS_C bị filter out (R002).
- **AC-02 — Multi VAS type display**
  - **Given:** VAS_D vừa là `Quality Control` vừa là `RFID`.
  - **When:** User xem column `VAS type`.
  - **Then:** Hiển thị `Quality Control, RFID` (R004).
- **AC-03 — VAS sau đánh giá có tiêu chí không đạt → Chờ duyệt**
  - **Given:** VAS_E đang `Đang xử lý`, vừa đánh giá xong có ≥ 1 tiêu chí không đạt.
  - **When:** Submit kết quả.
  - **Then:** Status chuyển sang `Chờ duyệt / Waiting for approval` (R007).
- **AC-04 — Mở lại revert về Mới**
  - **Given:** VAS_E status `Chờ duyệt`.
  - **When:** User vào detail → click `Mở lại` → dialog MSG-VAS-001 → `Xác nhận`.
  - **Then:** Kết quả đánh giá revert; VAS chuyển status về `Mới (Open)` (R011).
- **AC-05 — Nhận hàng dù có tiêu chí không đạt**
  - **Given:** VAS_E status `Chờ duyệt`, có 2 tiêu chí không đạt.
  - **When:** User click `Nhận hàng` → `Xác nhận nhận hàng`.
  - **Then:** Hệ thống chấp nhận; VAS tiến bước tiếp theo (R012).
- **AC-06 — Nhận hàng + SKU required IMEI → Chờ dán ID**
  - **Given:** VAS_E của SKU `required IMEI`.
  - **When:** User Nhận hàng.
  - **Then:** VAS chuyển status `Chờ dán ID / Wating for paste ID` (R013).
- **AC-07 — Nhận hàng + SKU không required → Completed**
  - **Given:** VAS_E của SKU không required IMEI/RFID.
  - **When:** User Nhận hàng.
  - **Then:** VAS chuyển status `Completed` (R013).
- **AC-08 — Trả NCC default disable input SL**
  - **Given:** VAS_F status `Chờ duyệt`, ASN đã nhận 20 SL.
  - **When:** User click `Trả nhà cung cấp`.
  - **Then:** Dialog hiện SL = 20 (= SL đã nhận), input disable; user click `Xác nhận`.
  - **And:** VAS chuyển `Chờ NCC đến lấy`; ghi nhận SL khai báo VAS = 20 và SL trả NCC = 20 (R014, R015).
- **AC-09 — `Chờ NCC đến lấy` → `Đã trả NCC` + Outbound Return vendor**
  - **Given:** VAS_F status `Chờ NCC đến lấy`, NCC vừa lấy hàng.
  - **When:** User cập nhật VAS sang `Đã trả NCC`.
  - **Then:** Tạo Outbound type `Return vendor` với info tương ứng (R016).
- **AC-10 — Adjustment Vendor Return — current gap**
  - **Given:** Workflow sau A9 cần tạo Adjustment type `Vendor Return`.
  - **When:** Hệ thống trigger tạo Adjustment.
  - **Then:** **Hiện tại fail / not implemented** — gap đã biết (R017 + Q-003). Test case sẽ phải mark `Blocked` cho R017.
- **AC-11 — 10% group UID cho SKU vải**
  - **Given:** SKU vải có 25 group UID trong ASN, type Quality control.
  - **When:** Hệ thống tạo VAS đánh giá CL.
  - **Then:** Tạo 3 dòng VAS (= ceil(25 × 0.10) = ceil(2.5) = 3) (R018).
- **AC-12 — 10% group UID với số nhỏ**
  - **Given:** SKU vải có 1 group UID trong ASN.
  - **When:** Hệ thống tạo VAS đánh giá CL.
  - **Then:** Tạo 1 dòng VAS (= ceil(0.1) = 1) — Q-004 confirm boundary với count < 10.

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R011, MSG-VAS-001 | Dialog `Mở lại (Re-Open)` dùng từ "RECEIVE" trong message EN (`Do you want to confirm RECEIVE for the quality control...`) — typo hay intentional? Re-Open semantics khác với Receive nên có vẻ mâu thuẫn. | PO | Open | | | |
| Q-002 | R012 | "Có thể trong kết quả đánh giá vẫn có tiêu chí không đạt nhưng vẫn có thể xác nhận nhận hàng" — có require role manager override không? Có audit log lý do override không? | PO/Compliance | Open | | | |
| Q-003 | R017, AC-10 | Adjustment type `Vendor Return` chưa tạo được — workaround hiện tại là gì (manual? skip? defer)? Khi nào Dev sẽ implement? | Dev Lead | Open | | | |
| Q-004 | R018, AC-12 | 10% group UID rounding lên — với count < 10 (vd 1, 5) thì ceil ra 1 — đúng yêu cầu không? Có min/max bound (vd minimum 1 dòng VAS)? | PO | Open | | | |
| Q-005 | R009, R014 | "VAS được chọn" trong status `Chờ NCC đến lấy` — VAS được chọn ở đâu, do user chọn hay tự động sau Trả NCC? Raw chỉ đề cập "Khi VAS được chọn". | PO | Open | | | |
| Q-006 | R001, R004 | VAS type `Other` dùng trong trường hợp nào? Có rules mapping nào với SKU không? Multi-VAS type chỉ áp dụng với `Quality Control + RFID/IMEI` hay còn combination khác? | PO | Open | | | |
| Q-007 | MSG-VAS-001/002/003 | Verbatim message VN cho 3 dialog: `Mở lại`, `Nhận hàng`, `Trả nhà cung cấp`. Message EN cho `Nhận hàng` và `Trả NCC` cũng chưa được provide trong raw. | PO/UX | Open | | | |
| Q-008 | R005 typo | Spelling `Wating for paste ID` — typo của `Waiting for paste ID`? Có ảnh hưởng key/value mapping trong code không? | PO/Dev | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-17, S-18 | 1.5 (stub) | 1.5 | All R + AC | Draft |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_qc_vas | test_stub_qc_vas | Add (chờ Gate 1B) | [[stub_qc_evaluation_result]] (đánh giá CL upstream), [[stub_receiving_po_confirm_paste_id]] (Chờ dán ID downstream), [[stub_receiving_po_inbound_shipment]] (ASN cho 10% group UID) | Q-001..Q-008 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R018, AC-01..AC-12 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-008 |

## 🚧 Blocked Coverage

- R011, MSG-VAS-001, AC-04 — chờ Q-001 (typo RECEIVE/Re-Open clarification)
- R012, AC-05 — chờ Q-002 (manager override + audit)
- R017, AC-10 — chờ Q-003 (Adjustment workaround)
- R018, AC-11, AC-12 — chờ Q-004 (10% boundary với count nhỏ)
- R009, R014 — chờ Q-005 (chọn VAS để trả NCC)
- R001, R004 — chờ Q-006 (VAS type `Other` + combo rules)
- MSG-VAS-001/002/003 — chờ Q-007 (verbatim VN + 2 EN missing)
- R005 — chờ Q-008 (typo `Wating`)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:36:55 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 16:30:00 | v1.1 | Refine stub → full spec: 18 R-ID, 12 AC, 10 BR, 3 messages (1 EN-only), 8 questions Open. `partial_read: false`. | refine-batch-2-2026-05-30 |
