---
spec: stub_qc_evaluation_manual
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI, Functional]
---

# Test Suite — Tạo mới đánh giá Manual + SKU phụ liệu Return + Blocked UID Damaged + Tiêu chí 4 điểm/Theo từng bước

## Phạm vi
- Source spec: [[stub_qc_evaluation_manual]]
- Active requirements: 16 testable (R004, R005, R006, R007, R008, R009, R011, R012, R013, R014, R015, R016, R017, R018, R019, R020, R021, R022, R023 — excludes R001⚠️ deprecated, R002⚠️ deprecated, R003⚠️ doc marker, R010⚠️ doc marker)
- Blocked: 16 nhóm chờ open questions

**Note:** R001, R002 deprecated (flow cũ bỏ) — không tạo TC. R003, R010 là heading markers — không testable.

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Loại case | Kỹ thuật | Pre-conditions | Các bước | Kết quả mong đợi | Nguồn | Status |
|-------|--------|---------|-------|-----------|----------|----------------|----------|------------------|-------|--------|
| TC-EVM-001 | Step 1 — Tìm SP theo SKU, load 10 PO gần nhất | R004, AC-01 | Functional | Positive | Happy Path | User QC, chọn kho A. SP `SP-A` có ≥ 1 PO | 1. Click `Tạo mới`. 2. Nhập SKU `SP-A`. | Hệ thống load 10 PO gần nhất của `SP-A` theo kho A | Explicit từ 07105#L1176-L1187 (R004) | ⏳ |
| TC-EVM-002 | Step 1 — Tìm SP theo barcode | R004 | Functional | Positive | Happy Path | SP có barcode | 1. Nhập barcode vào tìm kiếm. | Hệ thống tìm được SP từ barcode | Explicit từ 07105#L1176-L1187 (R004) | ⏳ |
| TC-EVM-003 | Step 1 — Tìm mã PO chính xác | R004 | Functional | Positive | Happy Path | Biết mã PO chính xác | 1. Nhập mã PO chính xác. | PO hiển thị trong danh sách | Explicit từ 07105#L1176-L1187 (R004) | ⏳ |
| TC-EVM-004 | Step 2 — Field UID group bắt buộc | R005, AC-03 | Functional | Negative | Error Guessing | Form Step 2 mở | 1. Để trống UID group. 2. Click `Bắt đầu đánh giá`. | Validation block | Explicit từ 07105#L1190-L1206 (R005) | ⏳ |
| TC-EVM-005 | Step 2 — UID group không tồn tại | R006, AC-04 | Functional | Negative | Error Guessing | UID `UID-XYZ` không tồn tại | 1. Nhập `UID-XYZ`. 2. Click `Bắt đầu đánh giá`. | ERR-EVM-001: `Mã UID không tồn tại.` | Explicit từ 07105#L1201-L1202 (R006) | ⏳ |
| TC-EVM-006 | Step 2 — SL cần đánh giá > SL trong UID | R006, AC-05 | Functional | Negative | BVA | UID-001 SL = 100 | 1. Nhập SL = 150. 2. Click `Bắt đầu đánh giá`. | ERR-EVM-002: `Số lượng trong UID group không đủ số lượng yêu cầu.` | Explicit từ 07105#L1203-L1204 (R006) | ⏳ |
| TC-EVM-007 | Step 2 — SL hợp lệ (≤ SL trong UID) | R006 | Functional | Positive | BVA | UID-001 SL = 100 | 1. Nhập SL = 100. 2. Click `Bắt đầu đánh giá`. | Pass, chuyển Step 3 | Explicit từ 07105#L1201-L1205 (R006) | ⏳ |
| TC-EVM-008 | Step 3 — Thông tin UID group, lô, HSD, PO, NCC | R007 | UI | Positive | Happy Path | Step 3 mở | 1. Quan sát thông tin hiển thị. | Hiển thị: Nhóm UID, Số lượng đang có, Số lô, Hạn sử dụng, SL cần đánh giá, Mã PO, Nhà cung cấp, Sản phẩm, Ghi chú, Tiêu chí đạt/không đạt | Explicit từ 07105#L1210-L1222 (R007) | ⏳ |
| TC-EVM-009 | Step 3 — Tiêu chí Fail bắt buộc chụp hình + ghi chú | R008, AC-06 | Functional | Negative | Error Guessing | Tiêu chí A đánh Fail | 1. Đánh Fail tiêu chí A. 2. Cố chuyển sang tiêu chí khác. | Block; yêu cầu chụp hình + ghi chú | Explicit từ 07105#L1223-L1235 (R008) | ⏳ |
| TC-EVM-010 | Step 3 — Tiêu chí Fail max 5 hình | R008, AC-07 | Functional | Negative | BVA | Tiêu chí Fail | 1. Chụp 5 hình. 2. Cố chụp thêm. | Block thêm hình sau 5 | Explicit từ 07105#L1223-L1235 (R008) | ⏳ |
| TC-EVM-011 | Step 3 — Hoàn thành đánh giá | R009, AC-08 | Functional | Positive | Happy Path | Đã đánh giá tất cả tiêu chí | 1. Click `Hoàn thành`. | Đánh giá lưu thành công | Explicit từ 07105#L1237-L1238 (R009) | ⏳ |
| TC-EVM-012 | SKU phụ liệu (non-NVL, non-Vải) scope | R011, AC-09 | Functional | Positive | EP | SKU cate phụ liệu, kết quả Failed | 1. Hoàn thành đánh giá với kết quả Failed. | Confirm MSG-EVM-004 hiển thị (ADJ dialog) | Explicit từ 07105#L1243-L1246 (R011) | ⏳ |
| TC-EVM-013 | SKU Vải/NVL Failed — không hiện ADJ dialog | R011 | Functional | Negative | EP | SKU vải, kết quả Failed | 1. Hoàn thành đánh giá SKU vải. | ADJ dialog không xuất hiện (scope phụ liệu không áp dụng) | Explicit từ 07105#L1243-L1246 (R011) | ⏳ |
| TC-EVM-014 | SKU phụ liệu Failed → hiện dialog tạo ADJ | R012, R013, AC-09 | Functional | Positive | State Transition | SKU phụ liệu, kết quả Failed | 1. Hoàn thành đánh giá. | MSG-EVM-004 EN: `SKU 422280022 has evaluation criteria marked as FAILED. Do you want to create an adjustment voucher...?` hiển thị | Explicit từ 07105#L1247-L1255 (R012, R013) | ⏳ |
| TC-EVM-015 | Chọn `Để sau` đóng dialog, không tạo ADJ | R013, AC-10 | Functional | Positive | Happy Path | Dialog mở | 1. Click `Để sau`. | Dialog đóng; quay về danh sách SKU; không có ADJ | Explicit từ 07105#L1250-L1255 (R013) | ⏳ |
| TC-EVM-016 | Tạo ADJ — SL trả hợp lệ (< SL nhập PO) | R014, AC-11 | Functional | Positive | BVA | PO SL = 100. Dialog mở | 1. Nhập SL = 30. 2. Click `Xác nhận`. | ADJ tạo với SL = 30 | Explicit từ 07105#L1256-L1262 (R014) | ⏳ |
| TC-EVM-017 | Tạo ADJ — SL trả = SL nhập PO bị block | R014 | Functional | Negative | BVA | PO SL = 100 | 1. Nhập SL = 100. 2. Click `Xác nhận`. | Block (SL phải < SL nhập PO) | Explicit từ 07105#L1256-L1262 (R014) | ⏳ |
| TC-EVM-018 | Tạo ADJ — SL trả > SL nhập PO bị block | R014, AC-12 | Functional | Negative | BVA | PO SL = 100 | 1. Nhập SL = 150. | ERR-EVM-005 (R014) | Explicit từ 07105#L1256-L1262 (R014) | ⏳ |
| TC-EVM-019 | ADJ Require VAT = No | R015, AC-13 | Functional | Positive | EP | Form ADJ mở | 1. Chọn `No – Trả hàng không xuất hoá đơn`. 2. Tạo. | ADJ tạo với Require VAT = No | Explicit từ 07105#L1263-L1284 (R015) | ⏳ |
| TC-EVM-020 | ADJ Require VAT = Yes VAT Hasaki xuất | R015, AC-14 | Functional | Positive | EP | Form ADJ mở | 1. Chọn `Yes VAT - Hasaki xuất hoá đơn bán hàng cho NCC`. 2. Tạo. | ADJ tạo với rule Hasaki xuất | Explicit từ 07105#L1263-L1284 (R015) | ⏳ |
| TC-EVM-021 | ADJ Require VAT = Yes VAT NCC xuất | R015, AC-15 | Functional | Positive | EP | Form ADJ mở | 1. Chọn `Yes VAT – NCC xuất hoá đơn điều chỉnh cho HASAKI`. 2. Tạo. | ADJ tạo với rule NCC xuất | Explicit từ 07105#L1263-L1284 (R015) | ⏳ |
| TC-EVM-022 | ADJ fields auto-fill từ PO | R015, AC-16 | Functional | Positive | Happy Path | Source PO `PO-001` Vendor `V1` | 1. Tạo ADJ. 2. Quan sát các fields. | ADJ có: Vendor = `V1`, Source code = `PO-001`, Warehouse = kho đang xử lý, Type = `Export`, Reason = `Return to vendor`, Required picking = `No`, ADJ status = `Waiting for approval` | Explicit từ 07105#L1263-L1284 (R015) | ⏳ |
| TC-EVM-023 | ADJ SKU info từ Inside | R016, AC-17 | Functional | Positive | Happy Path | SKU `422280022` có VAT/Price trên Inside | 1. Tạo ADJ SL = 30. 2. Quan sát SKU info trong ADJ. | SKU info: SL = 30, VAT và Price lấy theo rules ADJ hiện tại | Explicit từ 07105#L1285-L1291 (R016) | ⏳ |
| TC-EVM-024 | S-35 SKU vải Failed → blocked tất cả UID group cùng PO + LOT | R017, AC-18 | Functional | Positive | State Transition | SKU Vải V1, PO `PO-X` LOT `LOT-A`, 5 UID groups UG-1..UG-5. Đánh giá UG-1 Failed | 1. Hoàn thành đánh giá UG-1 Failed. | Hệ thống auto blocked UG-1 đến UG-5 (cùng PO + LOT) | Explicit từ 07105#L1292-L1294 (R017) | ⏳ |
| TC-EVM-025 | S-35 — UID chuyển Damaged sau blocked | R018, AC-19 | Functional | Positive | State Transition | Sau TC-EVM-024 | 1. Quan sát product status các UID. | Tất cả UID trong UG-1..UG-5 → status `Damaged`; stock Available không cộng | Explicit từ 07105#L1295-L1297 (R018) | ⏳ |
| TC-EVM-026 | S-35 — UID Damaged không picklist | R018, AC-20 | Functional | Negative | Error Guessing | UID `U1` status `Damaged` | 1. Order/Receipt/IT try pick U1. | UID `U1` bị skip / không thể pick | Explicit từ 07105#L1295-L1297 (R018) | ⏳ |
| TC-EVM-027 | S-35 — Un-Blocked UID → Damaged → Normal | R019, AC-21 | Functional | Positive | State Transition | UID group UG-1 blocked, UID `U1` Damaged | 1. User Un-Blocked UG-1. | UG-1 → Available; `U1` status → `Normal` | Explicit từ 07105#L1298-L1300 (R019) | ⏳ |
| TC-EVM-028 | Update 10-05-2026 — Phân loại 4 điểm → mở màn setup khi Tạo | R020, AC-22 | Functional | Positive | Happy Path | Màn thiết lập tiêu chí | 1. Chọn `Lỗi 4 điểm`. 2. Click `Tạo`. | Màn thiết lập nội dung 4 điểm mở | Explicit từ 07105#L1304-L1308 (R020) | ⏳ |
| TC-EVM-029 | Update 10-05-2026 — Auto inherit 4 điểm khi assign SKU | R021, AC-23 | Functional | Positive | Happy Path | Tiêu chí `T4-1` (4 điểm) đã setup | 1. Assign `T4-1` cho SKU `SP-X`. | Hệ thống auto load thiết lập 4 điểm cho `SP-X` | Explicit từ 07105#L1309-L1311 (R021) | ⏳ |
| TC-EVM-030 | Update 10-05-2026 — Phân loại Theo từng bước → mở màn setup | R022, AC-24 | Functional | Positive | Happy Path | Màn thiết lập tiêu chí | 1. Chọn `Theo từng bước`. 2. Click `Tạo`. | Màn thiết lập từng bước mở | Explicit từ 07105#L1312-L1315 (R022) | ⏳ |
| TC-EVM-031 | Update 10-05-2026 — Auto inherit Theo từng bước khi assign SKU | R023, AC-25 | Functional | Positive | Happy Path | Tiêu chí `TBB-1` (3 bước) đã setup | 1. Assign cho SKU `SP-Y`. | Auto load 3 bước cho `SP-Y` | Explicit từ 07105#L1320-L1321 (R023) | ⏳ |

## 🚧 Blocked Coverage

- **R001, R002 — Deprecated flow**: không tạo TC. Chờ Q-008, Q-016 (legacy data + remove plan) nếu cần regression test.
- **R015, R018 — API endpoints**: chờ Q-002. TC kiểm tra API không thể tạo.
- **R004, MSG-EVM-003 — SKU chưa thiết lập tiêu chí verbatim**: chờ Q-003. TC kiểm tra exact message không thể tạo.
- **ERR-EVM-001, ERR-EVM-002 — Verbatim EN**: chờ Q-004. TC kiểm tra EN message không thể tạo.
- **R013, MSG-EVM-004 — Verbatim VN confirm dialog**: chờ Q-005. TC kiểm tra VN confirm không thể tạo.
- **R014, ERR-EVM-005 — Verbatim VN+EN cho SL > PO**: chờ Q-006. TC kiểm tra message này không thể tạo.
- **R019 — Un-Blocked sau vendor return đã Out**: chờ Q-007. TC edge case không thể tạo.
- **R011 — SKU phụ liệu definition**: chờ Q-009 (định nghĩa master data flag, overlap với phụ liệu vải). TC boundary SKU phụ liệu vs vải không thể tạo.
- **R012 — Threshold Failed**: chờ Q-010 (1/10 fail = toàn bộ Failed? hay có % threshold). TC kiểm tra threshold không thể tạo.
- **R015 — Rules ADJ hiện tại**: chờ Q-011. TC kiểm tra VAT/Price logic không thể tạo.
- **R017 — Định nghĩa LOT**: chờ Q-012 (LOT vs số lô). TC verify LOT grouping không thể tạo.
- **R018 — Product status enum đầy đủ**: chờ Q-013. TC kiểm tra status khác không thể tạo.
- **R021, R023 — Override per SKU**: chờ Q-014. TC override không thể tạo.
- **R007 — Số lô + HSD source**: chờ Q-015. TC verify data source không thể tạo.
- **L1128-L1147 App-side UID SL + tem QC** — POTENTIAL_OMISSION chờ Q-017 xác nhận ownership spec nào.
- **L1152-L1168 xã vải + PO sample** — MISSING_DETAIL chờ Q-018; liên quan [[stub_qc_uid_group]] và [[stub_receiving_po_po_sample]].

## Regression Impact

- [[stub_qc_criteria_setup]]: Tiêu chí 4 điểm + từng bước auto inherit.
- [[stub_qc_criteria_sku]]: Assign tiêu chí cho SKU.
- [[stub_qc_uid_group]]: UID group khai báo SL.
- [[stub_qc_evaluation_result]]: Kết quả tổng hợp.
- Adjustment system: Return to vendor Adjustment.
- Inventory system: UID Damaged stock impact.

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec stub_qc_evaluation_manual v1.2 (Verified). 31 TC active, 16 nhóm blocked. R001/R002 deprecated — skip TC.
