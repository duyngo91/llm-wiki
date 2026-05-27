---
status: Done
updated: 2026-05-25
---

# Evidence Matrix — Ingest 07062 + 07105

> Session: 2026-05-25 | Scope: receiving_po_inbound_shipment, quality_control_setup_criteria, quality_control_setup_sku (3 spec đầy đủ nhất)

## Receiving PO — Inbound Shipment

| Raw Evidence (path#line) | Wiki Claim (path#line) | Status | Action |
|:-------------------------|:----------------------|:-------|:-------|
| `07062#230`: "Đồng kiểm Check of goods Giá trị: Yes/No" trong More filter | `inbound_shipment#R1`: Filter Đồng kiểm Yes/No, More filter | SUPPORTED | Keep |
| `07062#232`: "Đủ điều kiện nhận Eligible to receive Giá trị : Yes/No" | `inbound_shipment#R2`: Filter Đủ điều kiện nhận Yes/No | SUPPORTED | Keep |
| `07062#233`: "Trạng thái WMS WMS status Status này chỉ sử dụng cho Type = PO" | `inbound_shipment#R3`: WMS status chỉ dùng Type=PO | SUPPORTED | Keep |
| `07062#235-239`: Giá trị **5 values**: Open, Receiving, Received, **Completed**, Canceled | `inbound_shipment#R3`: "giá trị: Open/Receiving/Received/Canceled" (4 values) | **INFERRED** ⚠️ | **Update R3 — thêm "Hoàn thành / Completed"** |
| `07062#231`: "- Move qua trang ASN" (ghi chú cho Đồng kiểm filter) | `inbound_shipment#R1`: không có ghi chú này | **UNCLEAR** | **Add note vào Business Rules** |
| `07062#245-246`: "Đồng kiểm — Lấy thông tin khi user chọn khi scan nhận PO" | `inbound_shipment#R4`: Listing Đồng kiểm lấy từ lựa chọn khi scan | SUPPORTED | Keep |
| `07062#264-271`: Bảng mapping Inside↔WMS (4 entries: Verified/Receiving/Received/Cancel) | `inbound_shipment#R7`: mapping 2 chiều | SUPPORTED | Keep |
| `07062#280-289`: WMS Status bảng (Open/Receiving/Received/Canceled) | `inbound_shipment#R8`: WMS Status 4 values | SUPPORTED | Keep — note: filter có thêm Completed nhưng bảng WMS status không có |
| `07062#291-295`: "Status Receiving thêm thời gian đã bao lâu chưa hoàn thành" | `inbound_shipment#R9`: Status Receiving + duration | SUPPORTED | Keep |
| `07062#255-262`: Bảng mô tả lý do không đủ điều kiện (4 case) | `inbound_shipment#R10`: 4 case lý do | SUPPORTED | Keep |
| `07062#319-321`: "Giải trình lý do treo PO — nếu PO giao trong ngày..." | `inbound_shipment_detail#R6`: Giải trình treo PO | SUPPORTED | Keep |
| `07062#326-333`: Bảng comment (Bình luận, TT, Nội dung, Người tạo, Ngày) | `inbound_shipment_detail#R8`: Listing comment | SUPPORTED | Keep |

## Quality Control — Setup Criteria

| Raw Evidence (path#line) | Wiki Claim (path#line) | Status | Action |
|:-------------------------|:----------------------|:-------|:-------|
| `07105#126-127`: "Menu: Inbound / Quality control — Tab Thiết lập tiêu chí" | `setup_criteria#R1` | SUPPORTED | Keep |
| `07105#134-135`: "Mã, tên tiêu chí — Tìm theo giá trị gần đúng, nhập từ 3 ký tự" | `setup_criteria#R2` | SUPPORTED | Keep |
| `07105#152`: "Mặc định khi tiêu chí mới được tạo thì sẽ ở trạng thái Active" | `setup_criteria#R6` | SUPPORTED | Keep |
| `07105#153`: "Khi muốn Active/Inactive thiết lập cho SKU thì hiện thông báo xác nhận" | `setup_criteria#R7` — nhưng đây là về SKU, không phải tiêu chí! | **UNCLEAR** ⚠️ | Raw line 153 ám chỉ SKU setup, không phải criteria listing — cần verify |
| `07105#159-160`: "Do you want to DEACTIVATE criterion 1001?" / "Do you want to ACTIVATE criterion 1001?" | `setup_criteria#R7`: confirm message criteria | SUPPORTED | Keep |
| `07105#163`: "Thời gian tạo: YYYY-MM-DD HH:SS" | `setup_criteria#R8`: format YYYY-MM-DD HH:SS | SUPPORTED | Keep — nhưng format có thể là typo (thiếu mm) → đã có Q-002 |
| `07105#175-188`: Mã tiêu chí bắt buộc, unique, error messages VN/EN | `setup_criteria#R11` | SUPPORTED | Keep |
| `07105#180-188`: Tên tiêu chí bắt buộc, unique, error messages | `setup_criteria#R12` | SUPPORTED | Keep |
| `07105#196-198`: "Lưu và đóng" / "Lưu và tiếp tục" / "Đóng" | `setup_criteria#R15-R17` | SUPPORTED | Keep |
| `07105#202-210`: Import validate — 4 loại lỗi (trùng mã/tên trong hệ thống/trong file) | `setup_criteria#R18` | SUPPORTED | Keep |

## Quality Control — Setup SKU

| Raw Evidence (path#line) | Wiki Claim (path#line) | Status | Action |
|:-------------------------|:----------------------|:-------|:-------|
| `07105#267`: "Mặc định khi SKU mới được tạo thì sẽ ở trạng thái Active" | `setup_sku#R6` (referenced from context) | SUPPORTED | Keep |
| `07105#270-271`: "Do you want to DEACTIVATE setup by SKU 422280022?" | `setup_sku#R5`: confirm message | SUPPORTED | Keep |
| `07105#272-273`: "tại 1 thời điểm 1 SKU không thể cùng active 2 thiết lập" | `setup_sku#R6`: Business Rule unique active | SUPPORTED | Keep |
| `07105#308-309`: "SKU 422280022 đã tồn tại và đang hoạt động trên hệ thống." | `setup_sku#R8`: error message | SUPPORTED | Keep |
| `07105#320-323`: "Khi nhận PO / Receiving PO (chưa hỗ trợ ở phase này)" | `setup_sku#R9`: phase note | SUPPORTED | Keep |
| `07105#333-338`: "Tất cả PO — Tự động sinh VAS" / "Ngẫu nhiên — chưa hỗ trợ" | `setup_sku#R10` | SUPPORTED | Keep |
| `07105#411-413`: "Hiện tại 1 tiêu chí chỉ hỗ trợ 1 điều kiện duy nhất" | `setup_sku#R16` | SUPPORTED | Keep |
| `07105#434-437`: Rules khi tiêu chí bị inactive (05-08-2025) | `setup_sku#R24,R25` | SUPPORTED | Keep |

## Tổng kết

| Metric | Giá trị |
|:-------|:--------|
| Tổng claims kiểm tra | 28 |
| SUPPORTED | 24 (86%) |
| UNCLEAR | 2 (7%) |
| INFERRED (lỗi thực sự) | 1 (4%) — R3 missing "Completed" |
| MISSING_DETAIL | 1 (4%) — R1 không ghi chú "Move qua trang ASN" |
