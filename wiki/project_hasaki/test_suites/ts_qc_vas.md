---
spec: stub_qc_vas
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI, Functional]
---

# Test Suite — QC VAS updated — VAS type, status mở rộng, action Mở lại / Nhận hàng / Trả NCC

## Phạm vi
- Source spec: [[stub_qc_vas]]
- Active requirements: 10 testable (R002, R003, R004, R005, R006, R007, R008, R009, R010, R013, R015, R016 — nhưng nhiều bị block bởi open questions)
- Blocked: 8 nhóm chờ open questions

**Phân tích blocked:**
- R001 (Q-006), R004 (R004 depends on R001 multi-value — Q-006 applies), R005 (Q-008 typo), R009/R014 (Q-005), R011/AC-04 (Q-001 typo RECEIVE), R012/AC-05 (Q-002 override), R017/AC-10 (Q-003), R018/AC-11/AC-12 (Q-004), MSG-VAS-001/002/003 (Q-007)
- R002, R003, R006, R007, R008, R010, R013, R015, R016 còn testable sau khi loại trừ

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Loại case | Kỹ thuật | Pre-conditions | Các bước | Kết quả mong đợi | Nguồn | Status |
|-------|--------|---------|-------|-----------|----------|----------------|----------|------------------|-------|--------|
| TC-VAS-001 | Filter VAS theo VAS type multi-select | R002, AC-01 | UI | Positive | Happy Path | Có VAS với nhiều type | 1. Mở filter VAS. 2. Chọn `IMEI` + `Quality Control`. 3. Apply. | Listing trả VAS type IMEI và Quality Control; type khác bị filter | Explicit từ 07105#L700-L707 (R002) | ⏳ |
| TC-VAS-002 | Cột VAS type có trong data table | R003 | UI | Positive | Happy Path | Có VAS trong listing | 1. Xem data table VAS. 2. Kiểm tra có cột `VAS type`. | Cột `VAS type` hiển thị trong data table | Explicit từ 07105#L708-L710 (R003) | ⏳ |
| TC-VAS-003 | Status enum — 9 values tồn tại trong hệ thống | R005 | UI | Positive | EP | Có VAS ở nhiều status | 1. Xem filter Status VAS. 2. Quan sát các values có sẵn. | Có đủ: `Mới/Open`, `Đang xử lý/In-Progress`, `Hoàn thành/Completed`, `Đã huỷ/Canceled`, `Chờ duyệt/Waiting for approval`, `Chờ dán ID`, `Chờ đánh giá`, `Chờ NCC đến lấy`, `Đã trả NCC` | Explicit từ 07105#L713-L728 (R005) | ⏳ |
| TC-VAS-004 | Status Đang xử lý — VAS đang được đánh giá CL | R006 | UI | Positive | Happy Path | VAS đang đánh giá | 1. Tìm VAS đang được đánh giá CL. 2. Quan sát status. | Status = `Đang xử lý/In-Progress` | Explicit từ 07105#L719 (R006) | ⏳ |
| TC-VAS-005 | VAS có tiêu chí không đạt sau đánh giá → Chờ duyệt | R007, AC-03 | Functional | Positive | State Transition | VAS đang `Đang xử lý`, có ≥ 1 tiêu chí không đạt | 1. Submit kết quả đánh giá với ≥ 1 tiêu chí không đạt. | VAS status chuyển → `Chờ duyệt/Waiting for approval` | Explicit từ 07105#L722-L723 (R007) | ⏳ |
| TC-VAS-006 | Status Chờ dán ID — VAS phiên nhận có SKU required IMEI/RFID | R008 | UI | Positive | Happy Path | VAS sau khi Nhận hàng SKU required IMEI | 1. Quan sát VAS sau hành động Nhận hàng cho SKU required IMEI. | Status = `Chờ dán ID/Wating for paste ID` | Explicit từ 07105#L724-L725 (R008) | ⏳ |
| TC-VAS-007 | Vào detail VAS status Chờ duyệt — có 3 action buttons | R010 | UI | Positive | Happy Path | VAS ở status `Chờ duyệt` | 1. Click mã VAS status `Chờ duyệt`. 2. Vào trang detail. 3. Quan sát buttons. | Hiển thị đủ 3 buttons: `Mở lại (Re-Open)`, `Nhận hàng (Receive)`, `Trả nhà cung cấp (Return to vendor)` | Explicit từ 07105#L734-L755 (R010) | ⏳ |
| TC-VAS-008 | Nhận hàng dù có tiêu chí không đạt | R012, AC-05 | Functional | Positive | Happy Path | VAS status `Chờ duyệt`, có 2 tiêu chí không đạt | 1. Vào detail VAS. 2. Click `Nhận hàng`. 3. Click `Xác nhận nhận hàng`. | Hệ thống chấp nhận xác nhận nhận hàng dù có tiêu chí không đạt; VAS tiến bước tiếp | Explicit từ 07105#L743-L751 (R012) | ⏳ |
| TC-VAS-009 | Nhận hàng + SKU required IMEI → Chờ dán ID | R013, AC-06 | Functional | Positive | State Transition | VAS của SKU `required IMEI` | 1. Nhận hàng + xác nhận. | VAS status → `Chờ dán ID / Wating for paste ID` | Explicit từ 07105#L752-L754 (R013) | ⏳ |
| TC-VAS-010 | Nhận hàng + SKU không required IMEI/RFID → Completed | R013, AC-07 | Functional | Positive | State Transition | VAS của SKU không required IMEI/RFID | 1. Nhận hàng + xác nhận. | VAS status → `Completed` | Explicit từ 07105#L752-L754 (R013) | ⏳ |
| TC-VAS-011 | Trả NCC — SL default = SL đã nhận, input disabled | R014, AC-08 | Functional | Positive | Happy Path | VAS `Chờ duyệt`, ASN đã nhận 20 SL | 1. Click `Trả nhà cung cấp`. 2. Quan sát dialog SL. | Dialog hiện SL = 20 (= SL đã nhận); input field disabled, user không thay đổi được | Explicit từ 07105#L755-L759 (R014) | ⏳ |
| TC-VAS-012 | Xác nhận Trả NCC — VAS chuyển Chờ NCC đến lấy | R015, AC-08 | Functional | Positive | State Transition | Dialog Trả NCC mở | 1. Click `Xác nhận` trong dialog Trả NCC. | VAS status → `Chờ NCC đến lấy`; ghi nhận SL khai báo VAS và SL trả NCC | Explicit từ 07105#L760-L762 (R015) | ⏳ |
| TC-VAS-013 | Cập nhật VAS từ Chờ NCC đến lấy → Đã trả NCC + Outbound | R016, AC-09 | Functional | Positive | State Transition | VAS status `Chờ NCC đến lấy`, NCC vừa lấy hàng | 1. User cập nhật VAS sang `Đã trả NCC`. | VAS status = `Đã trả NCC`; Outbound type `Return vendor` được tạo với info tương ứng | Explicit từ 07105#L763-L767 (R016) | ⏳ |

## 🚧 Blocked Coverage

- **R001, R004 — VAS type `Other` + combo rules**: chờ Q-006 (khi nào dùng `Other`; multi-VAS type combinations ngoài `Quality Control + RFID/IMEI`). TC kiểm tra `Other` và combos không thể tạo.
- **R005 — Typo `Wating for paste ID`**: chờ Q-008 (typo ảnh hưởng key/value mapping). TC kiểm tra exact key spelling không thể tạo.
- **R009, R014 — Semantics VAS được chọn**: chờ Q-005 (VAS được chọn ở đâu → trigger `Chờ NCC đến lấy`). TC kiểm tra transition này không thể tạo độc lập.
- **R011, AC-04 — Mở lại + dialog MSG-VAS-001**: chờ Q-001 (dialog dùng từ "RECEIVE" cho Re-Open — typo hay intentional?). TC kiểm tra action Mở lại không thể tạo.
- **R012, AC-05 — Override + audit**: chờ Q-002 (manager override + audit log khi nhận hàng dù có fail). TC kiểm tra audit trail không thể tạo.
- **R017, AC-10 — Adjustment Vendor Return**: chờ Q-003 (workaround cho gap chưa implement). TC cho R017 bị blocked hoàn toàn.
- **R018, AC-11, AC-12 — 10% group UID boundary**: chờ Q-004 (ceil với count < 10; min/max bound). TC boundary cho VAS count không thể tạo.
- **MSG-VAS-001/002/003 — Verbatim VN + 2 EN missing**: chờ Q-007. TC kiểm tra message content không thể tạo.

## Regression Impact

- [[stub_qc_evaluation_result]]: Kết quả đánh giá CL là upstream trigger cho VAS `Chờ duyệt`.
- [[stub_receiving_po_confirm_paste_id]]: VAS `Chờ dán ID` feed vào confirm paste ID flow.
- [[stub_receiving_po_inbound_shipment]]: ASN cho 10% group UID affect số lượng VAS.

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec stub_qc_vas v1.1 (Verified). 13 TC active, 8 nhóm blocked.
