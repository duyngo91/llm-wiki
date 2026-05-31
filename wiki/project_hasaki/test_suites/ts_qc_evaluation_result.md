---
spec: stub_qc_evaluation_result
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI, Functional]
---

# Test Suite — Kết quả đánh giá QC (Listing + Chi tiết Web + App)

## Phạm vi
- Source spec: [[stub_qc_evaluation_result]]
- Active requirements: 17 testable (R001, R004, R005, R006, R009, R011, R012, R013, R014, R015, R016, R017, R018, R019, R022, R023, R024, R026, R027, R028, R029 — sau khi loại blocked)
- Blocked: 10 nhóm chờ open questions

**Blocked analysis:**
- R020⚠️ (Q-001 service API), R021⚠️ (Q-002 format chi tiết Bình thường), R025/AC-15 (Q-003 công thức hệ số), R010/ERR-QCR-001 (Q-004 verbatim message), R007/R029/AC-05 (Q-005 cấu trúc cột Phân loại), R008 (Q-006 layout Người đánh giá), R019 (Q-007 icon Thao tác), R030 (Q-008/Q-009 rules state Failed + đánh giá lại), R002/R003 (Q-010 exact match semantics)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Loại case | Kỹ thuật | Pre-conditions | Các bước | Kết quả mong đợi | Nguồn | Status |
|-------|--------|---------|-------|-----------|----------|----------------|----------|------------------|-------|--------|
| TC-QCR-001 | Truy cập trang Kết quả đánh giá | R001, AC-01 | UI | Positive | Happy Path | User có quyền QC | 1. Vào `Menu: Inbound / Quality control`. 2. Click tab `Kết quả đánh giá`. | Trang listing kết quả đánh giá mở với toolbar filter | Explicit từ 07105#L571-L573 (R001) | ⏳ |
| TC-QCR-002 | Filter Kho ≥ 3 ký tự mới trigger | R004, AC-03 | Functional | Negative → Positive | BVA | Có Kho `Hà Nội` | 1. Nhập 2 ký tự `Hà`. 2. Nhập thêm `Hà N` (4 ký tự). | 2 ký tự: filter chưa trigger. 4 ký tự: trigger search | Explicit từ 07105#L583-L585 (R004) | ⏳ |
| TC-QCR-003 | Filter Mã PO — match exact | R005 | Functional | Positive | Happy Path | Có PO-001 và PO-001-X | 1. Nhập `PO-001` vào filter Mã PO. 2. Apply. | Chỉ kết quả với PO = exact `PO-001` hiển thị | Explicit từ 07105#L586-L588 (R005) | ⏳ |
| TC-QCR-004 | Filter Trạng thái — chọn Đang đánh giá | R006, AC-04 | Functional | Positive | EP | Có kết quả 3 status | 1. Chọn `Đang đánh giá`. 2. Apply. | Chỉ kết quả status `Processing` | Explicit từ 07105#L589-L595 (R006) | ⏳ |
| TC-QCR-005 | Filter Trạng thái — 3 values có sẵn | R006 | UI | Positive | EP | Listing mở | 1. Quan sát dropdown Trạng thái. | Có đủ: `Mới (New)`, `Đang đánh giá (Processing)`, `Hoàn thành (Completed)` | Explicit từ 07105#L589-L595 (R006) | ⏳ |
| TC-QCR-006 | Filter Có tiêu chí không đạt = Có | R009, AC-06 | Functional | Positive | EP | 5 kết quả, 3 có fail | 1. Filter `Có tiêu chí không đạt = Có`. 2. Apply. | 3 kết quả hiển thị | Explicit từ 07105#L612-L616 (R009) | ⏳ |
| TC-QCR-007 | Filter Có tiêu chí không đạt = Không | R009 | Functional | Positive | EP | Như trên | 1. Filter `Không`. 2. Apply. | 2 kết quả (không có fail) hiển thị | Explicit từ 07105#L612-L616 (R009) | ⏳ |
| TC-QCR-008 | Listing — cột VAS là hyperlink | R011, AC-08 | UI | Positive | Happy Path | Listing có dòng với VAS `VAS-001` | 1. Click cell `VAS-001`. | Chuyển sang trang detail VAS-001 | Explicit từ 07105#L629 (R011) | ⏳ |
| TC-QCR-009 | Listing — cột Kho hiển thị | R012 | UI | Positive | Happy Path | Listing có dữ liệu | 1. Quan sát cột `Kho`. | Cột Kho hiển thị trong listing | Explicit từ 07105#L630 (R012) | ⏳ |
| TC-QCR-010 | Listing — cột Sản phẩm format SKU – tên | R013, AC-10 | UI | Positive | Happy Path | SKU = `SKU-001`, tên = `Vải lụa` | 1. Quan sát cột `Sản phẩm`. | Cell = `SKU-001 – Vải lụa` | Explicit từ 07105#L632 (R013) | ⏳ |
| TC-QCR-011 | Listing — cột Tiêu chí đạt ratio | R014, AC-11 | UI | Positive | Happy Path | SKU 10 tiêu chí, 7 đạt, 3 không | 1. Quan sát cột `Tiêu chí đạt`. | `7/10` | Explicit từ 07105#L633 (R014) | ⏳ |
| TC-QCR-012 | Listing — cột Tiêu chí không đạt ratio | R015, AC-11 | UI | Positive | Happy Path | Như trên | 1. Quan sát cột `Tiêu chí không đạt`. | `3/10` | Explicit từ 07105#L634 (R015) | ⏳ |
| TC-QCR-013 | Listing — cột Phân loại hiển thị | R016 | UI | Positive | Happy Path | Listing có dữ liệu nhiều loại | 1. Quan sát cột `Phân loại`. | Cột hiển thị value enum theo loại kết quả | Explicit từ 07105#L635-L636 (R016) | ⏳ |
| TC-QCR-014 | Listing — cột Mã PO nguồn là hyperlink | R017, AC-09 | UI | Positive | Happy Path | Dòng có `PO-001` | 1. Click `PO-001`. | Chuyển sang trang detail PO-001 trên Inside | Explicit từ 07105#L637 (R017) | ⏳ |
| TC-QCR-015 | Listing — các cột thông tin SP | R018 | UI | Positive | Happy Path | Listing có dữ liệu | 1. Quan sát các cột. | Có cột: `Nhà cung cấp`, `Danh mục`, `Thương hiệu`, `Ghi chú`, `Người đánh giá`, `Trạng thái` | Explicit từ 07105#L638-L645 (R018) | ⏳ |
| TC-QCR-016 | Click icon Thao tác mở chi tiết kết quả | R019 | Functional | Positive | Happy Path | Listing có dữ liệu | 1. Click icon `Thao tác` trên 1 dòng. | Mở trang chi tiết kết quả đánh giá | Explicit từ 07105#L646-L647 (R019) | ⏳ |
| TC-QCR-017 | Xem chi tiết kết quả Type = Nhóm UID | R022, AC-13 | Functional | Positive | Happy Path | Dòng Type = `Nhóm UID` | 1. Click Thao tác → xem chi tiết. | Mở trang chi tiết kết quả **theo từng nhóm UID** | Explicit từ 07105#L665-L666 (R022) | ⏳ |
| TC-QCR-018 | Tiêu chí lỗi 4 điểm hiển thị riêng, có 4 group | R023, R024, AC-14 | UI | Positive | Happy Path | Kết quả có tiêu chí lỗi 4 điểm | 1. Xem chi tiết kết quả. 2. Quan sát phần tiêu chí lỗi 4 điểm. | Hiển thị thành 4 group (lỗi 1/2/3/4 điểm), có thể thu gọn/mở rộng | Explicit từ 07105#L667-L672 (R023, R024) | ⏳ |
| TC-QCR-019 | Lỗi 4 điểm — chi tiết từng lỗi: Loại/Hình ảnh/Ghi chú | R026, AC-14 | UI | Positive | Happy Path | Kết quả có tiêu chí lỗi 4 điểm | 1. Mở rộng group lỗi. 2. Quan sát từng lỗi. | Mỗi lỗi hiển thị: `Loại lỗi`, `Hình ảnh lỗi`, `Ghi chú` | Explicit từ 07105#L676-L684 (R026) | ⏳ |
| TC-QCR-020 | Tiêu chí theo bước — mỗi bước 1 nhóm thông tin | R027, AC-16 | UI | Positive | Happy Path | Kết quả có tiêu chí step-by-step 3 bước | 1. Xem chi tiết. 2. Quan sát phần tiêu chí theo bước. | Mỗi bước = 1 nhóm gồm `Hình ảnh`, `Kết quả ghi nhận`, `Ghi chú` | Explicit từ 07105#L685-L689 (R027) | ⏳ |
| TC-QCR-021 | Update S-25 — Chi tiết kết quả xã vải có SL cần đánh giá + Hình ảnh tem QC | R028, AC-17 | UI | Positive | Happy Path | Kết quả đánh giá xã vải, web | 1. Xem chi tiết trên Web. | Thêm `Số lượng cần đánh giá` và `Hình ảnh tem QC` trong chi tiết | Explicit từ 07105#L1103-L1106 (R028) | ⏳ |
| TC-QCR-022 | Update S-25 — Cột Phân loại có value Xã vải | R029, AC-05 | UI | Positive | EP | Có kết quả type Xã vải | 1. Filter Phân loại = `Xã vải`. 2. Apply. | Kết quả type `Fabric Relaxing` hiển thị | Explicit từ 07105#L1108-L1111 (R029) | ⏳ |
| TC-QCR-023 | UID group `Đánh giá đạt` default = No cho SKU vải | R030, AC-18 | Functional | Positive | State Transition | PO mới nhận, SKU Thời trang NVL, là SKU vải | 1. Vào `Inventory / Group UID / Tab Danh sách`. 2. Tìm UID group SKU vải. | Field `Đánh giá đạt` = `No` | Explicit từ 07105#L1112-L1123 (R030) | ⏳ |
| TC-QCR-024 | UID group `Đánh giá đạt` transition No → Yes sau đánh giá xã vải Đạt | R030, AC-19 | Functional | Positive | State Transition | UID group SKU vải `Đánh giá đạt = No` | 1. QC hoàn thành đánh giá xã vải kết quả Đạt. | Field transition `No → Yes` | Explicit từ 07105#L1112-L1123 (R030) | ⏳ |
| TC-QCR-025 | UID group `Đánh giá đạt` = N/A cho SKU không phải vải | R030, AC-20 | Functional | Positive | EP | SKU thuộc Mỹ phẩm | 1. Xem UID group SKU Mỹ phẩm. | Field `Đánh giá đạt` = `N/A`; không transition | Explicit từ 07105#L1112-L1123 (R030) | ⏳ |
| TC-QCR-026 | Filter Ngày đánh giá — Từ > Đến bị block | R010 | Functional | Negative | BVA | Listing mở | 1. Nhập Từ ngày `2026-05-30`. 2. Nhập Đến ngày `2026-05-29`. 3. Apply. | Hệ thống block apply filter (ERR-QCR-001 hoặc date picker block) | Explicit từ 07105#L617-L624 (R010) | ⏳ |

## 🚧 Blocked Coverage

- **R020⚠️ — Service ghi nhận kết quả**: chờ Q-001 (API endpoint / schema / internal queue). TC kiểm tra service không thể tạo.
- **R021⚠️, AC-12 — Chi tiết Type Bình thường**: chờ Q-002 (format/fields chi tiết). TC xem chi tiết Bình thường không thể tạo.
- **R025, AC-15 — Tổng điểm lỗi đã nhân hệ số**: chờ Q-003 (công thức hệ số 4 điểm). TC tính tổng điểm không thể tạo.
- **R010, ERR-QCR-001, AC-07 — Verbatim message**: chờ Q-004. TC kiểm tra exact message ngày Từ > Đến không thể tạo (TC-QCR-026 chỉ check behavior block, không check message text).
- **R007, R029, AC-05 — Cấu trúc cột Phân loại**: chờ Q-005 (1 cột 5 values hay 2 cột). TC verify exact column structure không thể tạo.
- **R008 — Layout Người đánh giá**: chờ Q-006 (2 dòng hay 1 dòng với separator). TC UI layout không thể tạo.
- **R019 — Icon Thao tác**: chờ Q-007 (icon cụ thể + số actions). TC kiểm tra icon không thể tạo.
- **R030 — Kết quả Không đạt → state gì**: chờ Q-008 (giữ `No` hay chuyển `Failed`). TC state transition after fail không thể tạo.
- **R030 — Đánh giá lại sau Yes**: chờ Q-009. TC re-evaluate không thể tạo.
- **R002, R003 — Exact match semantics**: chờ Q-010 (case-sensitive, trim, special chars). TC edge case search không thể tạo.

## Regression Impact

- [[stub_qc_criteria_setup]]: Tiêu chí lỗi 4 điểm + tiêu chí theo bước có format chuẩn ở chi tiết.
- [[stub_qc_evaluation_mobile]]: Kết quả từ App là input chính.
- [[stub_qc_evaluation_manual]]: Kết quả từ Manual evaluation.
- [[stub_qc_vas]]: Hyperlink VAS detail.
- [[stub_qc_uid_group]]: UID group state `Đánh giá đạt`.

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec stub_qc_evaluation_result v1.1 (Verified). 26 TC active, 10 nhóm blocked.
