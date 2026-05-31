---
spec: stub_qc_evaluation_mobile
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI, Functional]
---

# Test Suite — Đánh giá chất lượng sản phẩm trên Mobile (General + Vải)

## Phạm vi
- Source spec: [[stub_qc_evaluation_mobile]]
- Active requirements: 16 testable (R001, R003, R004, R006, R007 partial, R008, R009, R010, R011 partial, R013, R014, R015, R016 partial, R017, R018, R019, R020, R021, R022, R023, R024, R026, R027, R028, R029, R030, R031, R032, R033)
- Blocked: 12 nhóm chờ open questions

**Blocked analysis:**
- R002 (Q-011 typo `Pruchase`), R005 (Q-008 fuzzy search), R007 partial (Q-006 Cam nhạt non-vải), R011/AC-06 (Q-009 audit log edit), R012/AC-07 (Q-001 config OFF behavior), R016 (Q-012 công thức làm tròn 10%), R018/ERR-QCM-001/AC-12 (Q-007 verbatim message), R023/AC-14 (Q-003 Other custom), R024 (Q-002 xoá lỗi đã ghi), R025/R027/AC-16/AC-17 (Q-004 hệ số nhân), R028-R030/AC-18 (Q-005 công thức step-by-step), R013/R014 (Q-010 Hoàn thành validation)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Loại case | Kỹ thuật | Pre-conditions | Các bước | Kết quả mong đợi | Nguồn | Status |
|-------|--------|---------|-------|-----------|----------|----------------|----------|------------------|-------|--------|
| TC-QCM-001 | App — Truy cập Quality Control qua menu | R001 | UI | Positive | Happy Path | Đã login App với account QC | 1. Mở App. 2. Vào menu `Purchase Order / Quality Control` (ghi chú: raw có typo `Pruchase` — Q-011 pending). | Tính năng Quality Control mở | Explicit từ 07105#L790-L795 (R001) | ⏳ |
| TC-QCM-002 | Step 1 — Chọn kho, hiển thị VAS Open + In-Progress | R002 (via R001 behavior), AC-01 | Functional | Positive | Happy Path | VAS_A Open, VAS_B Completed, VAS_C In-Progress cùng kho | 1. Chọn kho. | App show VAS_A, VAS_C; VAS_B bị filter | Explicit từ 07105#L797-L799 (R002) | ⏳ |
| TC-QCM-003 | Step 1 — Tìm kiếm theo PO/VAS | R003, AC-02 | Functional | Positive | Happy Path | Có VAS với PO_P1 | 1. Search "P1". | Chỉ VAS có PO_P1 xuất hiện | Explicit từ 07105#L800 (R003) | ⏳ |
| TC-QCM-004 | Step 2 — VAS header hiển thị Shop/VAS/Tổng SKU/Mã PO/Tổng SP | R004, AC-03 | UI | Positive | Happy Path | VAS_X có 5 SKU | 1. Click VAS_X. | Header: Shop, VAS, Tổng SKU=5, Mã PO, Tổng sản phẩm | Explicit từ 07105#L803-L808 (R004) | ⏳ |
| TC-QCM-005 | Step 2 — Danh sách sản phẩm: Tên/SKU-Barcode/SL | R006, AC-03 | UI | Positive | Happy Path | VAS có 5 SKU | 1. Quan sát danh sách. | Mỗi SP hiển thị: Tên sản phẩm, SKU – Barcode, Số lượng | Explicit từ 07105#L811-L815 (R006) | ⏳ |
| TC-QCM-006 | Color coding — Xám nhạt (chưa đánh giá), Xanh dương (đang), Xanh lá (đã xong) | R007, AC-04 | UI | Positive | Happy Path | 3 SKU: A chưa, B đang, C xong | 1. Quan sát màu các SKU. | SKU_A xám nhạt, SKU_B xanh dương nhạt, SKU_C xanh lá nhạt | Explicit từ 07105#L816-L820 (R007) | ⏳ |
| TC-QCM-007 | Step 3 general — thông tin SKU, PO, NCC, ghi chú | R008 | UI | Positive | Happy Path | SKU_A có dữ liệu PO | 1. Click SKU_A. | Hiển thị: Sản phẩm (SKU–Tên), PO, Số lượng, Nhà cung cấp, Ghi chú (default trống, editable), Tổng tiêu chí đạt, Không đạt | Explicit từ 07105#L824-L830 (R008) | ⏳ |
| TC-QCM-008 | Step 3 general — danh sách tiêu chí theo thiết lập SKU | R009 | UI | Positive | Happy Path | SKU có tiêu chí thiết lập | 1. Xem danh sách tiêu chí. | Mỗi tiêu chí: Thứ tự, Tên, Mô tả, Mô tả điều kiện, Hình chụp mẫu, Đạt/Không đạt | Explicit từ 07105#L831-L840 (R009) | ⏳ |
| TC-QCM-009 | Tiêu chí Theo điều kiện — nhập kết quả + Enter xác định Đạt/Không đạt | R010, AC-05 | Functional | Positive | Happy Path | Tiêu chí điều kiện `> 50` | 1. Nhập 60 → Enter. | Tiêu chí Đạt | Explicit từ 07105#L841-L846 (R010) | ⏳ |
| TC-QCM-010 | Tiêu chí điều kiện — giá trị 0 bị block | R010 | Functional | Negative | BVA | Tiêu chí điều kiện | 1. Nhập 0. | Validation block (Giá trị > 0) | Explicit từ 07105#L841-L846 (R010) | ⏳ |
| TC-QCM-011 | Edit kết quả đánh giá | R011, AC-06 | Functional | Positive | Happy Path | TC đã có kết quả 60 = Đạt | 1. Edit → nhập 30. 2. Xác nhận. | Hệ thống tính lại → Không Đạt | Explicit từ 07105#L847-L853 (R011) | ⏳ |
| TC-QCM-012 | Đánh giá xong tất cả tiêu chí → sản phẩm xanh lá | R013, AC-08 | Functional | Positive | State Transition | SKU_A có 3 tiêu chí | 1. Đánh giá xong 3 → `Hoàn thành`. | Sản phẩm → Xanh lá nhạt | Explicit từ 07105#L862-L863 (R013) | ⏳ |
| TC-QCM-013 | VAS multi-sản phẩm — phải đánh giá hết mới Hoàn thành | R014, AC-09 | Functional | Negative | Error Guessing | VAS_X có 5 SP, mới xong 4 | 1. Click `Hoàn thành đánh giá`. | App yêu cầu hoàn thành SP thứ 5 | Explicit từ 07105#L865-L868 (R014) | ⏳ |
| TC-QCM-014 | Step 2 vải — có cột Số lô và Hạn sử dụng | R015, AC-10 | UI | Positive | Happy Path | SKU vải trong VAS | 1. Mở VAS. 2. Quan sát danh sách SP vải. | Danh sách có Số lô và Hạn sử dụng | Explicit từ 07105#L888-L892 (R015) | ⏳ |
| TC-QCM-015 | Step 3 vải — scan UID group hợp lệ → Xác nhận | R017, R020, AC | Functional | Positive | Happy Path | SKU vải lô L1, UID_1 hợp lệ | 1. Click SP vải. 2. Scan `UID_1`. 3. Click `Xác nhận`. | Tiến sang bước đánh giá tiêu chí | Explicit từ 07105#L909-L915 (R017, R020) | ⏳ |
| TC-QCM-016 | Step 3 vải — suggest UID đã nhận theo lô | R019, AC-13 | UI | Positive | Happy Path | Lô L1 có 3 UID đã nhận | 1. Vào màn scan UID. | App suggest UID_1, UID_2, UID_3 để chọn nhanh | Explicit từ 07105#L912-L913 (R019) | ⏳ |
| TC-QCM-017 | Step 4 vải — 3 tiêu chí hiển thị với thông tin đầy đủ | R021 | UI | Positive | Happy Path | Sau scan UID hợp lệ | 1. Quan sát 3 tiêu chí. | Mỗi tiêu chí có: Tên (+ hướng dẫn modal), Mô tả, Điều kiện | Explicit từ 07105#L918-L928 (R021) | ⏳ |
| TC-QCM-018 | Lỗi 4 điểm — 4 mức điểm hiển thị | R022 | UI | Positive | Happy Path | Tiêu chí Kiểm tra lỗi 4 điểm mở | 1. Quan sát 4 mức. | Hiển thị: Lỗi 1 điểm (0–3"), 2 điểm (3–6"), 3 điểm (6–9"), 4 điểm (>9") | Explicit từ 07105#L930-L934 (R022) | ⏳ |
| TC-QCM-019 | Lỗi 4 điểm — chọn loại lỗi bắt buộc trong 19 values | R023, AC-14 | UI | Positive | EP | Tiêu chí Lỗi 4 điểm, click `+` | 1. Click `+`. 2. Quan sát dropdown. | Dropdown có 19 values theo enum trong R023; chọn bắt buộc | Explicit từ 07105#L935-L960 (R023) | ⏳ |
| TC-QCM-020 | Lỗi 4 điểm — chụp hình bắt buộc trước Xác nhận | R024, AC-15 | Functional | Negative | Error Guessing | Đã chọn loại lỗi, chưa chụp hình | 1. Click `Xác nhận`. | Block; yêu cầu chụp ≥ 1 hình (max 3) | Explicit từ 07105#L961-L966 (R024) | ⏳ |
| TC-QCM-021 | Lỗi 4 điểm — icon xem thông tin lỗi đã cập nhật | R026 | UI | Positive | Happy Path | Đã ghi nhận ≥ 1 lỗi | 1. Quan sát icon xem thông tin. | Icon hiển thị, click mở thông tin lỗi đã ghi | Explicit từ 07105#L974 (R026) | ⏳ |
| TC-QCM-022 | Step 5 vải — ≥ 1 tiêu chí Không Đạt → UID group Không Đạt | R032, AC-19 | Functional | Positive | Decision Table | UID_1 đánh giá: 1 tiêu chí Không Đạt | 1. Click `Hoàn thành`. | UID_1 kết quả = Không Đạt; màu `Cam nhạt` | Explicit từ 07105#L1017-L1018 (R032) | ⏳ |
| TC-QCM-023 | Step 5 vải — tất cả tiêu chí Đạt → UID group Đạt | R031, R032 | Functional | Positive | Decision Table | UID_2: tất cả tiêu chí Đạt | 1. Click `Hoàn thành`. | UID_2 kết quả = Đạt | Explicit từ 07105#L1016-L1018 (R031, R032) | ⏳ |
| TC-QCM-024 | Step 5 vải — tiếp tục các UID group còn lại | R033, AC-20 | Functional | Positive | Happy Path | Lô L1 có 3 UID, xong UID_1 | 1. Quay lại danh sách. | UID_2, UID_3 còn lại để đánh giá | Explicit từ 07105#L1019 (R033) | ⏳ |

## 🚧 Blocked Coverage

- **R002 — Spelling typo `Pruchase Order`**: chờ Q-011. TC kiểm tra menu path chính xác không thể tạo.
- **R005 — Search gần đúng semantics**: chờ Q-008 (fuzzy/partial/normalized). TC search semantics chi tiết không thể tạo.
- **R007 — Cam nhạt cho non-vải**: chờ Q-006. TC color coding Cam nhạt cho general flow không thể tạo.
- **R011, AC-06 — Audit log khi edit**: chờ Q-009. TC kiểm tra audit log không thể tạo.
- **R012, AC-07 — Config require image OFF behavior**: chờ Q-001 (optional chụp hay hide). TC cho config OFF không thể tạo.
- **R016 — 10% group UID làm tròn**: chờ Q-012 (ceil/floor/round khi kết quả lẻ). TC boundary làm tròn không thể tạo.
- **R018, ERR-QCM-001, AC-12 — Verbatim message UID invalid**: chờ Q-007. TC kiểm tra message không thể tạo.
- **R023, AC-14 — `Other` custom input**: chờ Q-003. TC cho lỗi `Other` không thể tạo.
- **R024 — Xoá/sửa lỗi đã ghi nhận**: chờ Q-002. TC edit lỗi không thể tạo.
- **R025, R027, AC-16, AC-17 — Hệ số nhân lỗi 4 điểm**: chờ Q-004. TC tính tổng điểm không thể tạo.
- **R028-R030, AC-18 — Công thức Độ co rút/Độ đồng màu**: chờ Q-005. TC step-by-step + công thức không thể tạo.
- **R013, R014 — Hoàn thành validation khi chưa đủ tiêu chí**: chờ Q-010 (block hay nhắc nhở). TC-QCM-013 assume block; cần confirm.

## Regression Impact

- [[stub_qc_vas]]: VAS là nguồn cho QC Mobile evaluation.
- [[stub_qc_criteria_sku]]: Tiêu chí thiết lập cho SKU là input đánh giá.
- [[stub_qc_evaluation_result]]: Kết quả đánh giá Mobile lưu vào evaluation result.

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec stub_qc_evaluation_mobile v1.2 (Verified). 24 TC active, 12 nhóm blocked.
