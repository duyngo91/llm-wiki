---
spec: stub_qc_criteria_setup
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI, Functional]
---

# Test Suite — Thiết lập tiêu chí QC (Master + Per-SKU + Điều kiện + Phân loại)

## Phạm vi
- Source spec: [[stub_qc_criteria_setup]]
- Active requirements: 22 testable (R001, R003, R004, R005, R006, R007, R008, R009, R010, R011, R012, R014, R015, R016, R017, R018, R019, R020, R021, R022, R023, R025, R026, R027, R028, R030, R031, R032, R033, R034, R035, R036, R037, R038; excludes R002⚠️, R024⚠️)
- Blocked: 16 R/AC chờ open questions

**Note:** R002 (Q-016 raw typo) và R024 (Q-001 công thức rules Dev) là ⚠️ — không tạo TC cho 2 R-ID này.

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Loại case | Kỹ thuật | Pre-conditions | Các bước | Kết quả mong đợi | Nguồn | Status |
|-------|--------|---------|-------|-----------|----------|----------------|----------|------------------|-------|--------|
| TC-CRS-001 | Truy cập Tab Thiết lập tiêu chí | R001 | UI | Positive | Happy Path | User có quyền QC | 1. Vào `Inbound / Quality control`. 2. Click tab `Thiết lập tiêu chí`. | Tab mở, listing tiêu chí hiển thị | Explicit từ 07105#L126-L128 (R001) | ⏳ |
| TC-CRS-002 | Listing tiêu chí — có đủ các cột | R003 | UI | Positive | Happy Path | Có dữ liệu tiêu chí | 1. Quan sát listing. | Listing có cột: `TT`, `Mã tiêu chí`, `Tên tiêu chí`, `Mô tả`, `Hướng dẫn`, `Đang hoạt động`, `Người tạo`, `Người cập nhật`, `Thao tác` | Explicit từ 07105#L144-L170 (R003) | ⏳ |
| TC-CRS-003 | Active/Inactive tiêu chí — hiện confirm dialog | R004, AC-04 | Functional | Positive | Happy Path | Tiêu chí `T-001` Active | 1. Click toggle Inactive cho `T-001`. | MSG-CRS-011 confirm dialog hiển thị: `Do you want to DEACTIVATE criterion 1001?` | Explicit từ 07105#L152-L160 (R004) | ⏳ |
| TC-CRS-004 | Activate tiêu chí — hiện confirm dialog | R004 | Functional | Positive | Happy Path | Tiêu chí inactive | 1. Click toggle Active. | MSG-CRS-012: `Do you want to ACTIVATE criterion 1001?` | Explicit từ 07105#L159-L160 (R004) | ⏳ |
| TC-CRS-005 | Thao tác Update tiêu chí — không cho sửa mã | R005 | Functional | Negative | Error Guessing | Tiêu chí `T-001` tồn tại | 1. Click `Cập nhật` cho `T-001`. 2. Tìm field `Mã tiêu chí`. 3. Thử sửa. | Field `Mã tiêu chí` disabled, không cho sửa | Explicit từ 07105#L167-L170 (R005) | ⏳ |
| TC-CRS-006 | Tạo tiêu chí — mã hợp lệ và unique | R006, AC-01 | Functional | Positive | Happy Path | Mã `T-001` chưa tồn tại | 1. Click `Tạo mới`. 2. Nhập Mã = `T-001`. 3. Nhập Tên = `Kiểm tra ngoại quan`. 4. Click `Lưu và đóng`. | Tiêu chí tạo thành công, status Active | Explicit từ 07105#L171-L179 (R006) | ⏳ |
| TC-CRS-007 | Tạo tiêu chí — mã trùng | R006, AC-02 | Functional | Negative | Error Guessing | Mã `T-001` đã tồn tại | 1. Tạo mới với Mã = `T-001`. 2. Click Lưu. | ERR-CRS-001: `Mã tiêu chí đã tồn tại. / The criteria code already exists.` | Explicit từ 07105#L178-L179 (R006) | ⏳ |
| TC-CRS-008 | Tạo tiêu chí — tên trùng | R007, AC-03 | Functional | Negative | Error Guessing | Tên `Kiểm tra ngoại quan` đã tồn tại | 1. Tạo mới với Tên = `Kiểm tra ngoại quan`. 2. Click Lưu. | ERR-CRS-002: `Tên tiêu chí đã tồn tại. / The criteria name already exists.` | Explicit từ 07105#L185-L189 (R007) | ⏳ |
| TC-CRS-009 | Tạo tiêu chí — Mô tả và Hướng dẫn không bắt buộc | R008 | Functional | Positive | Happy Path | Mã và Tên mới | 1. Bỏ trống `Mô tả` và `Hướng dẫn`. 2. Click `Lưu và đóng`. | Tạo thành công | Explicit từ 07105#L190-L198 (R008) | ⏳ |
| TC-CRS-010 | Tạo tiêu chí — button Lưu và tiếp tục | R008 | Functional | Positive | Happy Path | Form tạo tiêu chí mở | 1. Điền đủ thông tin. 2. Click `Lưu và tiếp tục`. | Form lưu và clear thông tin để tạo tiếp | Explicit từ 07105#L196-L198 (R008) | ⏳ |
| TC-CRS-011 | Import tiêu chí — mã trùng hệ thống | R009, AC-07 | Functional | Negative | Error Guessing | File import có mã trùng hệ thống | 1. Upload file template. 2. Validate. | ERR-CRS-006: `Mã tiêu chí đã tồn tại trên hệ thống thống` (nội dung verbatim từ raw) | Explicit từ 07105#L203-L204 (R009) | ⏳ |
| TC-CRS-012 | Import tiêu chí — mã trùng file import | R009 | Functional | Negative | Error Guessing | File import có 2 dòng cùng mã | 1. Upload file. 2. Validate. | ERR-CRS-007: `Mã tiêu chí đã tồn tại trong file import` | Explicit từ 07105#L205-L206 (R009) | ⏳ |
| TC-CRS-013 | Import tiêu chí — tên trùng hệ thống | R009 | Functional | Negative | Error Guessing | File import có tên trùng hệ thống | 1. Upload file. 2. Validate. | ERR-CRS-008: `Tên tiêu chí đã tồn tại trên hệ thống thống` (verbatim raw) | Explicit từ 07105#L207-L208 (R009) | ⏳ |
| TC-CRS-014 | Import tiêu chí — tên trùng file import | R009 | Functional | Negative | Error Guessing | File import có 2 dòng cùng tên | 1. Upload file. 2. Validate. | ERR-CRS-009: `Tên tiêu chí đã tồn tại trong file import` | Explicit từ 07105#L209-L210 (R009) | ⏳ |
| TC-CRS-015 | Tab Thiết lập SKU — truy cập | R010 | UI | Positive | Happy Path | User có quyền | 1. Vào `Inbound / Quality control`. 2. Click tab `Thiết lập SKU`. | Tab Thiết lập SKU mở | Explicit từ 07105#L217-L220 (R010) | ⏳ |
| TC-CRS-016 | Filter SKU setup — filter theo Trạng thái | R011 | UI | Positive | Happy Path | Có dữ liệu SKU setup với nhiều status | 1. Chọn filter `Trạng thái`. 2. Apply với 1 value. | Listing lọc theo trạng thái đã chọn | Explicit từ 07105#L226-L250 (R011) | ⏳ |
| TC-CRS-017 | Listing SKU setup — có đủ các cột | R012 | UI | Positive | Happy Path | Có dữ liệu SKU setup | 1. Quan sát listing. | Listing có cột: `TT`, `Sản phẩm` (SKU – Tên), `Danh mục`, `Thương hiệu`, `Thời điểm`, `Tần suất`, `Số lượng tiêu chí`, `Đang hoạt động`, `Người tạo`, `Người cập nhật`, `Trạng thái`, `Thao tác` | Explicit từ 07105#L253-L283 (R012) | ⏳ |
| TC-CRS-018 | SKU setup Active/Inactive — confirm dialog | R013, AC-08 | Functional | Positive | Happy Path | Setup SKU Active | 1. Toggle Inactive. | MSG-CRS-013: `Do you want to DEACTIVATE setup by SKU 422280022?` | Explicit từ 07105#L267-L274 (R013) | ⏳ |
| TC-CRS-019 | SKU setup — 1 SKU không active 2 setup | R013, AC-08 | Functional | Negative | Error Guessing | SKU_A có setup_1 Active | 1. Cố Active setup_2 cho cùng SKU_A. | Hệ thống chặn; yêu cầu inactive setup_1 trước | Explicit từ 07105#L272-L274 (R013) | ⏳ |
| TC-CRS-020 | Button Cập nhật chỉ show khi status Mới | R014 | UI | Positive | State Transition | Có dòng status `Mới` và status khác | 1. Quan sát cột `Thao tác` từng dòng. | Button `Cập nhật` chỉ show khi status = `Mới (New)` | Explicit từ 07105#L281-L288 (R014) | ⏳ |
| TC-CRS-021 | Button Xoá thiết lập chỉ show khi status Mới | R014 | UI | Positive | State Transition | Như TC-CRS-020 | 1. Quan sát cột `Thao tác`. | Button `Xoá thiết lập` chỉ show khi status = `Mới` | Explicit từ 07105#L281-L288 (R014) | ⏳ |
| TC-CRS-022 | Tạo mới SKU setup — field Sản phẩm bắt buộc | R015 | Functional | Negative | Error Guessing | Modal Tạo mới mở | 1. Để trống `Sản phẩm`. 2. Click `Tiếp tục`. | ERR-CRS-010: `Thông tin này là bắt buộc.` | Explicit từ 07105#L289-L311 (R015) | ⏳ |
| TC-CRS-023 | Tạo mới SKU setup — SKU đã setup Active | R015, AC-08 | Functional | Negative | Error Guessing | SKU `422280022` đã Active | 1. Nhập `422280022`. | ERR-CRS-003: `SKU 422280022 đã tồn tại và đang hoạt động trên hệ thống.` | Explicit từ 07105#L305-L311 (R015) | ⏳ |
| TC-CRS-024 | Thời điểm đánh giá = Khi nhận PO không hỗ trợ (phase này) | R016, AC-09 | Functional | Negative | Error Guessing | Step 1 form mở | 1. Chọn `Thời điểm = Khi nhận PO`. | UI block / option disabled | Explicit từ 07105#L312-L323 (R016) | ⏳ |
| TC-CRS-025 | Thời điểm = Sau khi nhận PO hợp lệ | R016 | Functional | Positive | Happy Path | Step 1 form mở | 1. Chọn `Sau khi nhận PO`. | Option chọn được, form tiếp tục | Explicit từ 07105#L312-L323 (R016) | ⏳ |
| TC-CRS-026 | Tần suất = Ngẫu nhiên không hỗ trợ (phase này) | R017, AC-10 | Functional | Negative | Error Guessing | Step 1 form mở | 1. Chọn `Tần suất = Ngẫu nhiên`. | UI block / option disabled | Explicit từ 07105#L324-L338 (R017) | ⏳ |
| TC-CRS-027 | Tần suất = Tất cả PO hợp lệ | R017 | Functional | Positive | Happy Path | Step 1 form mở | 1. Chọn `Tất cả PO`. | Option chọn được | Explicit từ 07105#L324-L338 (R017) | ⏳ |
| TC-CRS-028 | Ghi chú không bắt buộc | R018 | UI | Positive | Happy Path | Step 1 form mở | 1. Bỏ trống `Ghi chú`. 2. Click `Tiếp tục`. | Tiếp tục thành công | Explicit từ 07105#L339-L344 (R018) | ⏳ |
| TC-CRS-029 | Tiếp tục — SKU đã Active block | R019, AC | Functional | Negative | Error Guessing | SKU đã setup Active | 1. Nhập SKU đã Active. 2. Click `Tiếp tục`. | ERR-CRS-004: `SKU đã được thiết lập và đang hoạt động.` | Explicit từ 07105#L345-L348 (R019) | ⏳ |
| TC-CRS-030 | Step 2 — field Tiêu chí đánh giá bắt buộc, search 3+ ký tự | R020, AC-05 | Functional | Positive | BVA | Step 2 mở | 1. Nhập 2 ký tự vào Tiêu chí. 2. Nhập 3 ký tự. | 2 ký tự: không trigger. 3 ký tự: danh sách tiêu chí hiển thị | Explicit từ 07105#L357-L368 (R020) | ⏳ |
| TC-CRS-031 | Yêu cầu chụp hình bắt buộc chọn | R021, AC-11 | UI | Positive | Happy Path | Form tiêu chí SKU mở | 1. Quan sát field `Yêu cầu chụp hình`. | Field bắt buộc; có 2 lựa chọn `Yes`/`No` | Explicit từ 07105#L369-L374 (R021) | ⏳ |
| TC-CRS-032 | Hình chụp mẫu max 3 — upload 3 thành công | R021, AC-11 | Functional | Positive | BVA | Hình chụp mẫu field | 1. Upload 3 hình. | 3 hình accept; button upload disabled | Explicit từ 07105#L369-L374 (R021) | ⏳ |
| TC-CRS-033 | Loại đánh giá Đạt/Không đạt default + Phân loại Bình thường disable | R022, AC-12 | UI | Positive | Happy Path | Form tiêu chí cho SKU mới mở | 1. Quan sát `Loại đánh giá` và `Phân loại`. | Default: Loại = `Đạt/Không đạt`; Phân loại = `Bình thường`; disabled | Explicit từ 07105#L375-L380 (R022) | ⏳ |
| TC-CRS-034 | Operator = → có field Sai số cho phép (optional) | R023, AC-13 | UI | Positive | Happy Path | Loại = Theo điều kiện, Operator = `=` | 1. Chọn `=`. 2. Quan sát form. | Field `Sai số cho phép` hiển thị (số > 0, optional) | Explicit từ 07105#L380-L406 (R023) | ⏳ |
| TC-CRS-035 | Operator = → Giá trị = 0 bị block | R023 | Functional | Negative | BVA | Operator = `=` | 1. Nhập `Giá trị = 0`. | Validation block (Giá trị phải > 0) | Explicit từ 07105#L383-L396 (R023) | ⏳ |
| TC-CRS-036 | Operator = → Giá trị = -5 bị block | R023 | Functional | Negative | BVA | Operator = `=` | 1. Nhập `Giá trị = -5`. | Validation block | Explicit từ 07105#L383-L396 (R023) | ⏳ |
| TC-CRS-037 | Operator Trong khoảng — đủ từ + đến + đơn vị | R023, AC-14 | Functional | Positive | EP (valid) | Operator = `Trong khoảng` | 1. Nhập `từ = 80`, `đến = 120`, `đơn vị = kg`. | Pass | Explicit từ 07105#L380-L406 (R023) | ⏳ |
| TC-CRS-038 | 1 tiêu chí 1 điều kiện — nút + disable sau add | R025, AC-15 | UI | Positive | Happy Path | Đã add 1 điều kiện | 1. Quan sát nút `Thêm (+)`. | Nút disabled | Explicit từ 07105#L410-L413 (R025) | ⏳ |
| TC-CRS-039 | Xoá điều kiện → nút + enable lại | R025 | Functional | Positive | State Transition | Nút + disabled (đã có 1 điều kiện) | 1. Xoá điều kiện. 2. Quan sát nút `+`. | Nút enable lại | Explicit từ 07105#L410-L413 (R025) | ⏳ |
| TC-CRS-040 | Phân loại — 3 values trong dropdown | R026 | UI | Positive | EP | Form tiêu chí mở | 1. Quan sát dropdown `Phân loại`. | Có đủ: `Bình thường/Normal`, `Lỗi 4 điểm/4 points error`, `Theo từng bước/Step by step` | Explicit từ 07105#L414-L420 (R026) | ⏳ |
| TC-CRS-041 | Thêm tiêu chí vào danh sách SKU | R027, AC-16 | Functional | Positive | Happy Path | TC001 chưa có trong danh sách | 1. Chọn TC001. 2. Click `Thêm`. | TC001 xuất hiện trong danh sách | Explicit từ 07105#L421-L427 (R027) | ⏳ |
| TC-CRS-042 | Tiêu chí đã có — ERR-CRS-005 | R027, AC-16 | Functional | Negative | Error Guessing | TC001 đã có trong danh sách | 1. Chọn TC001. 2. Click `Thêm` lần 2. | ERR-CRS-005: `Tiêu chí đã tồn tại trong danh sách. / Criteria already exists in the list.` | Explicit từ 07105#L425-L426 (R027) | ⏳ |
| TC-CRS-043 | Yêu cầu duyệt → status Chờ duyệt | R028, AC-17 | Functional | Positive | State Transition | Đã add ≥ 1 tiêu chí | 1. Click `Yêu cầu duyệt` / `Hoàn thành`. | Status SKU setup = `Chờ duyệt (Waiting for Approval)` | Explicit từ 07105#L428-L432 (R028) | ⏳ |
| TC-CRS-044 | Update 05-08-2025 — Tiêu chí inactive → xoá khỏi SKU Open | R029, AC-18 | Functional | Positive | State Transition | SKU_A setup status `Open`, có TC001 active | 1. Inactive TC001. | TC001 xoá khỏi danh sách tiêu chí của SKU_A | Explicit từ 07105#L433-L437 (R029) | ⏳ |
| TC-CRS-045 | Update 05-08-2025 — Tiêu chí inactive → ẩn (không hiển thị) khi SKU Approved | R029, AC-19 | Functional | Positive | State Transition | SKU_B setup status `Approved`, có TC001 active | 1. Inactive TC001. | TC001 không hiển thị cho SKU_B (nhưng vẫn lưu) | Explicit từ 07105#L433-L437 (R029) | ⏳ |
| TC-CRS-046 | Update 17-09-2025 — Phân loại Theo từng bước → auto chuyển màn setup bước | R030, AC-20 | Functional | Positive | Happy Path | Thêm tiêu chí phân loại `Theo từng bước` | 1. Add tiêu chí với `Theo từng bước`. | Hệ thống auto chuyển sang màn thiết lập các bước | Explicit từ 07105#L443-L450 (R030) | ⏳ |
| TC-CRS-047 | Bước (Step) max 10 — nhập 11 bị block | R031, AC-21 | Functional | Negative | BVA | Step setup mở | 1. Cố nhập Step = 11. | Block; chỉ cho 1-10 | Explicit từ 07105#L451-L467 (R031) | ⏳ |
| TC-CRS-048 | Số bước đã chọn — disable cho bước tiếp | R031, AC-22 | UI | Positive | Happy Path | Step 1 đã chọn | 1. Mở dropdown cho bước mới. | Số 1 disable không cho chọn lại | Explicit từ 07105#L451-L467 (R031) | ⏳ |
| TC-CRS-049 | Từ khoá auto in hoa + bỏ space | R032, AC-23 | Functional | Positive | Happy Path | Ghi nhận kết quả ≠ `Không` | 1. Nhập `abc def`. | Field hiển thị `ABCDEF` (in hoa + bỏ space) | Explicit từ 07105#L468-L475 (R032) | ⏳ |
| TC-CRS-050 | Từ khoá — ký tự đặc biệt cho phép `_`, `-`, `.` | R032 | Functional | Positive | EP | Từ khoá field | 1. Nhập `abc_def-g.h`. | Accept, không block | Explicit từ 07105#L468-L475 (R032) | ⏳ |
| TC-CRS-051 | Công thức hợp lệ → text xanh | R033, AC-24 | Functional | Positive | Happy Path | Field Công thức | 1. Nhập công thức hợp lệ. 2. Click `Kiểm tra định dạng`. | Text chuyển xanh lá | Explicit từ 07105#L476-L488 (R033) | ⏳ |
| TC-CRS-052 | Công thức không hợp lệ → text đỏ | R033, AC-24 | Functional | Negative | Error Guessing | Field Công thức | 1. Nhập công thức sai cú pháp. 2. Click `Kiểm tra định dạng`. | Text chuyển đỏ | Explicit từ 07105#L476-L488 (R033) | ⏳ |
| TC-CRS-053 | Lưu không show khi chưa có bước | R033, AC-25 | UI | Positive | Happy Path | Step setup mở, chưa nhập bước | 1. Quan sát nút `Lưu`. | Nút Lưu không hiển thị | Explicit từ 07105#L476-L488 (R033) | ⏳ |
| TC-CRS-054 | Lưu auto validate công thức chưa check | R033, AC-26 | Functional | Positive | Happy Path | Đã nhập công thức, chưa click Kiểm tra | 1. Click Lưu. | Hệ thống auto validate công thức trước khi lưu | Explicit từ 07105#L476-L488 (R033) | ⏳ |
| TC-CRS-055 | Phân loại Lỗi 4 điểm → auto mở màn setup | R034, AC-27 | Functional | Positive | Happy Path | Thêm tiêu chí phân loại `Lỗi 4 điểm` | 1. Add tiêu chí `Lỗi 4 điểm`. | Màn thiết lập Lỗi 4 điểm mở tự động | Explicit từ 07105#L493-L499 (R034) | ⏳ |
| TC-CRS-056 | Form Lỗi 4 điểm — không có field Step number | R035, AC-27 | UI | Positive | Happy Path | Form Lỗi 4 điểm mở | 1. Quan sát form. | Form giống Theo từng bước nhưng không có field `Bước` (Step) | Explicit từ 07105#L500-L525 (R035) | ⏳ |
| TC-CRS-057 | Update 11-02-2026 — Field QC xã vải hiện khi tạo tiêu chí | R036, AC-28 | UI | Positive | Happy Path | Form tạo tiêu chí mở | 1. Quan sát form tạo tiêu chí. | Field `QC xã vải` hiển thị trong form | Explicit từ 07105#L1081-L1097 (R036) | ⏳ |
| TC-CRS-058 | Update 10-05-2026 — Phân loại 4 điểm → auto mở màn thiết lập khi click Tạo | R037, AC-29 | Functional | Positive | Happy Path | User thiết lập tiêu chí, chọn `Lỗi 4 điểm` | 1. Chọn phân loại `Lỗi 4 điểm`. 2. Click `Tạo`. | Màn thiết lập nội dung 4 điểm mở | Explicit từ 07105#L1304-L1311 (R037) | ⏳ |
| TC-CRS-059 | Update 10-05-2026 — Auto inherit 4 điểm khi assign SKU | R037, AC-29 | Functional | Positive | Happy Path | Tiêu chí `T-4P` đã setup 4 điểm | 1. Assign `T-4P` cho SKU `SP-X`. | Hệ thống auto load thiết lập 4 điểm cho `SP-X`, không cần config lại | Explicit từ 07105#L1304-L1311 (R037) | ⏳ |
| TC-CRS-060 | Update 10-05-2026 — Phân loại Theo từng bước → auto mở màn khi Tạo | R038, AC-30 | Functional | Positive | Happy Path | User thiết lập tiêu chí `Theo từng bước` | 1. Click `Tạo`. | Màn thiết lập từng bước mở | Explicit từ 07105#L1312-L1321 (R038) | ⏳ |
| TC-CRS-061 | Update 10-05-2026 — Auto inherit Theo từng bước khi assign SKU | R038, AC-30 | Functional | Positive | Happy Path | Tiêu chí `T-Step` setup 3 bước | 1. Assign cho SKU `SP-Y`. | Auto load 3 bước cho `SP-Y` | Explicit từ 07105#L1312-L1321 (R038) | ⏳ |

## 🚧 Blocked Coverage

- **R024 — Toán tử Công thức**: chờ Q-001 (rules Dev). TC cho Công thức không thể tạo.
- **R023 — Toán tử `Trong khoảng` validation from ≥ to**: chờ Q-002 (block hay không). TC BVA `từ ≥ đến` không thể tạo.
- **ERR-CRS-006, ERR-CRS-008 — Typo `thống thống`**: chờ Q-003 (giữ verbatim hay fix). TC kiểm tra exact message VN không thể tạo.
- **R016 — Khi nhận PO phase 2**: chờ Q-004. TC scope phase 2 không thể tạo.
- **R017 — Ngẫu nhiên phase 2**: chờ Q-005. TC scope phase 2 không thể tạo.
- **R026 — Phân loại configurable**: chờ Q-006. TC thêm phân loại mới không thể tạo.
- **R029 — UI xem tiêu chí đã ẩn + reactivate behavior**: chờ Q-007, Q-013.
- **R031 — Step max 10 configurable**: chờ Q-008.
- **R032 — Từ khoá special chars đầy đủ**: chờ Q-009.
- **R033 — Lưu rule edge**: chờ Q-010 (1 bước + không có công thức → Lưu show không).
- **R035 — Hệ số 4 điểm**: chờ Q-011.
- **R037 — Override per SKU**: chờ Q-012.
- **R013 — Mutex active 2 setup edge case**: chờ Q-014 (ngoại lệ 2 phase).
- **R028 — Approval flow scope**: chờ Q-015.
- **R002 — Filter date range `Đến ngày ≥ Từ ngày`**: chờ Q-016 (raw typo L141). TC BVA date range không thể tạo.

## Regression Impact

- [[stub_qc_criteria_sku]]: Master tiêu chí được dùng trong setup SKU step 2.
- [[stub_qc_criteria_approval]]: Setup SKU sau Yêu cầu duyệt feed vào approval flow.
- [[stub_qc_evaluation_mobile]], [[stub_qc_evaluation_manual]]: Tiêu chí approved dùng trong đánh giá.
- [[stub_qc_uid_group]]: Flag `QC xã vải` (R036) trigger sinh yêu cầu đánh giá xã vải.

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec stub_qc_criteria_setup v1.2 (Verified). 61 TC active, 16 nhóm blocked.
