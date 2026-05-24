---
aliases: [Test QC Setup Hasaki, test-hasaki-qc-setup]
tags: [qa/test-suite, qa/feature-group/receiving-po]
status: Draft
feature: hasaki_qc_setup
requirement: wiki/project_hasaki/features/hasaki_qc_setup
dev:
qa:
created: 2026-05-23
updated: 2026-05-23
approved_by:
approved_at:
approval_note:
---

# 🧪 Test Suite: Thiết lập Tiêu chí Kiểm soát Chất lượng (Hasaki WMS)

- **Feature liên quan:** [[wiki/project_hasaki/features/hasaki_qc_setup|hasaki_qc_setup]]
- **Requirement:** R1–R24, AC-01–AC-10
- **Dev phụ trách:** *(cập nhật)*
- **QA phụ trách:** *(cập nhật)*
- **Ngày cập nhật cuối:** 2026-05-23

## 📊 Tổng quan Test Coverage

| Loại Test | Số lượng TC | Pass | Fail | Blocked | Chưa test |
|:----------|:-----------|:-----|:-----|:--------|:----------|
| Happy Path | 10 | | | | 10 |
| Negative | 11 | | | | 11 |
| Boundary | 2 | | | | 2 |
| State Transition | 5 | | | | 5 |
| Error Guessing | 3 | | | | 3 |
| **Tổng** | **31** | | | | **31** |

## ✅ Test Cases

| Test ID | Tiêu đề | AC/Req Cover | Phạm vi | Loại case | Kỹ thuật test | Điều kiện tiên quyết | Các bước thực hiện | Kết quả mong đợi | Nguồn | Status |
|:--------|:--------|:-------------|:----------|:--------------|:--------------------|:-------------------|:-----------------|:-----------------|:-------| :--- |
| TC-QCS-001 | Tạo tiêu chí mới hợp lệ — Mã và Tên unique | AC-01 / R4 | UI+Functional | Positive | Happy Path | User đã login với quyền QC; Tab Thiết lập tiêu chí | 1. Nhấn Tạo mới 2. Nhập Mã tiêu chí unique, Tên unique 3. Nhấn "Lưu và đóng" | Tiêu chí được tạo, status Active, hiển thị trong danh sách | Explicit từ PDF v1.5 AC-01 | ⏳ |
| TC-QCS-002 | Tạo tiêu chí trùng Mã — báo lỗi | AC-02 / R4 | Functional | Negative | Equivalence Partitioning | Đã có tiêu chí mã "TC001" | 1. Tạo mới với mã "TC001" 2. Submit | Thông báo "Mã tiêu chí đã tồn tại."; không tạo mới | Explicit từ PDF v1.5 AC-02 | ⏳ |
| TC-QCS-003 | Tạo tiêu chí trùng Tên — báo lỗi | R4 | Functional | Negative | Equivalence Partitioning | Đã có tiêu chí tên "Kiểm tra nhãn" | 1. Tạo mới với tên "Kiểm tra nhãn" 2. Submit | Thông báo "Tên tiêu chí đã tồn tại."; không tạo mới | Explicit từ PDF v1.5 ERR-QCS-02 | ⏳ |
| TC-QCS-004 | Toggle Inactive tiêu chí có popup xác nhận | AC-03 / R3 | UI+Functional | Positive | Happy Path | Tiêu chí đang Active | 1. Nhấn toggle Inactive 2. Xem popup 3. Chọn Yes | Popup "Do you want to DEACTIVATE criterion ...?" → Yes → trạng thái = Inactive | Explicit từ PDF v1.5 AC-03 | ⏳ |
| TC-QCS-005 | Huỷ Toggle Inactive — giữ nguyên Active | R3 | Functional | Negative | State Transition | Tiêu chí đang Active | 1. Nhấn toggle Inactive 2. Popup xuất hiện 3. Chọn No | Trạng thái vẫn Active; không thay đổi | Explicit từ PDF v1.5 R3 | ⏳ |
| TC-QCS-006 | Filter Tab Tiêu chí — tìm gần đúng ≥3 ký tự | R1 | Functional | Positive | Boundary Value Analysis | Có tiêu chí tên "Kiểm tra màu sắc" | 1. Nhập 2 ký tự vào filter Tên 2. Nhập thêm 1 ký tự (tổng 3) | 2 ký tự: không có kết quả hoặc không trigger search; 3 ký tự: kết quả lọc xuất hiện | Explicit từ PDF v1.5 R1 | ⏳ |
| TC-QCS-007 | Import tiêu chí — trùng mã trong file | R5 | Functional | Negative | Error Guessing | File import có 2 dòng cùng mã tiêu chí | 1. Upload file import có mã trùng trong file | Lỗi "Mã tiêu chí đã tồn tại trong file import." | Explicit từ PDF v1.5 R5 | ⏳ |
| TC-QCS-008 | Import tiêu chí — trùng mã trên hệ thống | R5 | Functional | Negative | Error Guessing | Đã có tiêu chí mã "TC001" trên hệ thống | 1. Upload file import chứa mã "TC001" | Lỗi "Mã tiêu chí đã tồn tại trong file import." (hoặc "trên hệ thống") | Explicit từ PDF v1.5 R5 | ⏳ |
| TC-QCS-009 | Tạo thiết lập SKU — điền đủ bắt buộc, yêu cầu duyệt | AC-04 | UI+Functional | Positive | Happy Path | SKU chưa có thiết lập Active | 1. Tab Thiết lập SKU → Tạo mới 2. Chọn SKU, Thời điểm = Sau khi nhận PO, Tần suất = Tất cả PO 3. Thêm ≥1 tiêu chí 4. Nhấn "Yêu cầu duyệt" | Trạng thái chuyển "Chờ duyệt"; không hiện button Edit/Delete | Explicit từ PDF v1.5 AC-04 | ⏳ |
| TC-QCS-010 | Tạo thiết lập SKU — SKU đang có thiết lập Active | R8 | Functional | Negative | Equivalence Partitioning | SKU 422280022 đang có thiết lập Active | 1. Tạo mới thiết lập cho SKU 422280022 | Thông báo "SKU 422280022 đã tồn tại và đang hoạt động trên hệ thống." | Explicit từ PDF v1.5 ERR-QCS-06 | ⏳ |
| TC-QCS-011 | Approve thiết lập SKU | AC-05 | UI+Functional | Positive | Happy Path | Thiết lập SKU status Chờ duyệt; user là Approver | 1. Filter status = Chờ duyệt 2. Chọn thiết lập 3. Nhấn Duyệt → xác nhận Yes | Trạng thái chuyển "Đã duyệt"; hệ thống sẽ sinh VAS sau phiên nhận | Explicit từ PDF v1.5 AC-05 | ⏳ |
| TC-QCS-012 | Từ chối và Mở lại thiết lập SKU | AC-06 | UI+Functional | Positive | State Transition | Thiết lập SKU status Chờ duyệt | 1. Approver nhấn Từ chối → Yes 2. Status = Từ chối 3. QC Staff nhấn Mở lại | Sau Từ chối: status = Từ chối. Sau Mở lại: status = Open; có thể chỉnh sửa | Explicit từ PDF v1.5 AC-06 | ⏳ |
| TC-QCS-013 | Duyệt nhiều dòng cùng lúc | 🚫 | UI+Functional | Positive | Happy Path | Có 3 thiết lập SKU status Chờ duyệt | 1. Chọn 3 dòng bằng checkbox 2. Nhấn Duyệt → xác nhận | Cả 3 thiết lập chuyển status = Đã duyệt | Explicit từ PDF v1.5 R18 | 🚫 Blocked |
| TC-QCS-014 | Thêm tiêu chí Phân loại Bình thường vào SKU | R10 R11 R13 | Functional | Positive | Equivalence Partitioning | Thiết lập SKU đang Open, đã có tiêu chí Bình thường | 1. Thêm tiêu chí với Loại đánh giá = Đạt/Không đạt 2. Kiểm tra Phân loại | Phân loại tự động = Bình thường, không cho sửa | Explicit từ PDF v1.5 R11 | ⏳ |
| TC-QCS-015 | Thêm tiêu chí Phân loại Lỗi 4 điểm — mở modal thiết lập | R14 | UI+Functional | Positive | Happy Path | Thiết lập SKU đang Open | 1. Thêm tiêu chí với Phân loại = Lỗi 4 điểm 2. Nhấn Thêm | Modal thiết lập nội dung Lỗi 4 điểm tự mở (Content, Yêu cầu chụp hình, Ghi nhận KQ, Từ khoá, Hướng dẫn, Công thức) | Explicit từ PDF v1.5 R14 | ⏳ |
| TC-QCS-016 | Thêm tiêu chí Phân loại Theo từng bước — mở modal, Lưu ≥1 bước | AC-07 / R15 | UI+Functional | Positive | Happy Path | Thiết lập SKU đang Open | 1. Thêm tiêu chí Phân loại = Theo từng bước 2. Modal mở 3. Thiết lập ≥1 bước đầy đủ nội dung 4. Nhấn Lưu | Modal thiết lập bước hiện; sau Lưu tiêu chí xuất hiện trong danh sách SKU | Explicit từ PDF v1.5 AC-07 | ⏳ |
| TC-QCS-017 | Lưu thiết lập bước — công thức không hợp lệ | R16 | Functional | Negative | Error Guessing | Đang ở modal thiết lập bước | 1. Nhập công thức sai cú pháp 2. Nhấn Lưu | Công thức hiển thị chữ đỏ; không cho lưu; thông báo công thức không hợp lệ | Explicit từ PDF v1.5 R16 | ⏳ |
| TC-QCS-018 | Nút Lưu modal bước chỉ enable khi có ≥1 bước hợp lệ | R15 | Functional | Negative | Boundary Value Analysis | Modal thiết lập bước không có bước nào | 1. Mở modal Theo từng bước 2. Chưa thêm bước nào 3. Kiểm tra button Lưu | Button Lưu bị disable | Explicit từ PDF v1.5 R15 | ⏳ |
| TC-QCS-019 | Tiêu chí bị Inactive tự xóa khỏi SKU đang Open | AC-10 / R17 | Functional | Positive | State Transition | Thiết lập SKU Open có tiêu chí TC-X trong danh sách | 1. Inactive tiêu chí TC-X 2. Quay lại xem danh sách tiêu chí SKU | TC-X biến mất khỏi danh sách tiêu chí của SKU | Explicit từ PDF v1.5 AC-10 | ⏳ |
| TC-QCS-020 | Tiêu chí Inactive — SKU đang Approved giữ nguyên, tiêu chí không hiển thị | R17 | UI+Functional | Positive | State Transition | Thiết lập SKU status Approved, có tiêu chí TC-Y | 1. Inactive tiêu chí TC-Y 2. Xem chi tiết thiết lập SKU Approved | Thiết lập SKU vẫn Approved; tiêu chí TC-Y không hiển thị trong danh sách đánh giá | Explicit từ PDF v1.5 R17 | ⏳ |
| TC-QCS-021 | Thêm tiêu chí đã có trong danh sách SKU | R10 | Functional | Negative | Equivalence Partitioning | Thiết lập SKU đang Open, đã có tiêu chí TC001 | 1. Thêm lại tiêu chí TC001 vào danh sách | Thông báo "Tiêu chí đã tồn tại trong danh sách." | Explicit từ PDF v1.5 ERR-QCS-07 | ⏳ |
| TC-QCS-022 | VAS type Quality Control + RFID hiển thị đúng cột Type | AC-09 / R20 | UI+Functional | Positive | Happy Path | VAS có type Quality Control và RFID | 1. Vào VAS Listing 2. Kiểm tra cột Type | Cột Type = "Quality Control, RFID" (ngăn cách bởi dấu phẩy) | Explicit từ PDF v1.5 AC-09 | ⏳ |
| TC-QCS-023 | Filter VAS theo VAS type mới (IMEI, RFID, Quality Control, Other) | R20 | Functional | Positive | Equivalence Partitioning | Có VAS với các type mới | 1. Vào VAS Listing 2. Filter Type = Quality Control | Chỉ hiện VAS type Quality Control | Explicit từ PDF v1.5 R20 | ⏳ |
| TC-QCS-024 | VAS Chờ duyệt — action Nhận hàng → Chờ dán ID (nếu có IMEI/RFID) | 🚫 | Functional | Positive | State Transition | VAS status Chờ duyệt (QC failed); SKU có config IMEI | 1. Mở VAS status Chờ duyệt 2. Nhấn Nhận hàng → xác nhận Yes | VAS chuyển status "Chờ dán ID"; user cần dán IMEI trước khi Completed | Explicit từ PDF v1.5 R22 | 🚫 Blocked |
| TC-QCS-025 | VAS Chờ duyệt — action Trả NCC | 🚫 | UI+Functional | Positive | Happy Path | VAS status Chờ duyệt | 1. Nhấn Trả NCC 2. Xác nhận | VAS chuyển status "Chờ NCC đến lấy" | Explicit từ PDF v1.5 R22 | 🚫 Blocked |
| TC-QCS-026 | Cột QC xã vải bổ sung vào thiết lập tiêu chí | R23 | UI+Functional | Positive | Happy Path | Tab Thiết lập tiêu chí | 1. Xem listing tiêu chí 2. Tạo tiêu chí mới 3. Kiểm tra cột QC xã vải | Cột "QC xã vải" hiển thị; có thể bật/tắt per tiêu chí | Explicit từ PDF v1.5 R23 | ⏳ |
| TC-QCS-027 | Button Edit/Delete chỉ hiện với status Open | R19 | Functional | Positive | State Transition | Có thiết lập SKU status Open và status Chờ duyệt | 1. Xem cột Thao tác của từng trạng thái | Status Open: hiện Edit và Delete; Status Chờ duyệt: chỉ hiện Xem chi tiết và Duyệt | Explicit từ PDF v1.5 R19 | ⏳ |
| TC-QCS-028 | Loại đánh giá Theo điều kiện — cấu hình phép so sánh between | 🚫 | Functional | Positive | Equivalence Partitioning | Thiết lập SKU đang Open | 1. Thêm tiêu chí Loại đánh giá = Theo điều kiện 2. Chọn phép so sánh = between 3. Nhập Giá trị min và max | Form hiển thị 2 ô nhập giá trị; có Đơn vị tính và Sai số cho phép | Explicit từ PDF v1.5 R12 | 🚫 Blocked |
| TC-QCS-030 | Update 10-05-2026 — Tạo tiêu chí Lỗi 4 điểm ngay tại màn hình Tiêu chí | 🚫 | UI+Functional | Positive | Happy Path | User ở Tab Thiết lập tiêu chí | 1. Tạo mới tiêu chí với Phân loại = Lỗi 4 điểm 2. Modal thiết lập mở ngay tại màn hình Tiêu chí 3. Lưu | Nội dung Lỗi 4 điểm được lưu vào tiêu chí; khi add vào SKU hệ thống kế thừa thiết lập này | Explicit từ PDF v1.5 R24 update 10-05-2026 | 🚫 Blocked |
| TC-QCS-031 | Update 10-05-2026 — Kế thừa thiết lập khi add tiêu chí vào SKU | 🚫 | UI+Functional | Positive | Happy Path | Tiêu chí "Lỗi 4 điểm" đã có nội dung được thiết lập sẵn tại màn hình Tiêu chí | 1. Thêm tiêu chí đó vào SKU 2. Kiểm tra modal thiết lập | Modal hiển thị nội dung đã kế thừa từ thiết lập tiêu chí; không phải nhập lại từ đầu | Explicit từ PDF v1.5 R24 | 🚫 Blocked |
| TC-QCS-032 | Từ khoá trong thiết lập bước — tự động IN HOA, không khoảng trắng | R15 | Functional | Positive | Error Guessing | Modal thiết lập bước | 1. Nhập từ khoá "ket qua" (chữ thường, có khoảng trắng) 2. Blur khỏi ô | Từ khoá chuyển thành "KET_QUA" hoặc báo lỗi không cho khoảng trắng; chỉ chấp nhận `_`, `-`, `.` | Explicit từ PDF v1.5 R15 (Từ khoá tự động IN HOA, không khoảng trắng) | ⏳ |



## 🔁 Regression Impact

*Chưa có thay đổi requirement. Cập nhật khi có Task Change.*


## 🚧 Blocked Coverage

Các Requirement/AC chưa được sinh TC đầy đủ do còn câu hỏi Open trong Feature Spec:

| TC ID | Blocked R-IDs | Ghi chú |
|:------|:-------------|:--------|
| TC-QCS-013 | R18 | Only open refs — status set to Blocked |
| TC-QCS-024 | R22 | Only open refs — status set to Blocked |
| TC-QCS-025 | R22 | Only open refs — status set to Blocked |
| TC-QCS-028 | R12 | Only open refs — status set to Blocked |
| TC-QCS-030 | R24 | Only open refs — status set to Blocked |
| TC-QCS-031 | R24 | Only open refs — status set to Blocked |
## 🚫 Test Cases Lỗi Thời (Deprecated)

| Test ID | Tiêu đề | Phạm vi | Lý do deprecated | Ngày | Nguồn |
|:--------|:--------|:-----------------|:-----|:------| :--- |
| — | — | — | — | — |

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 21:49:34 | v1.1 | Loại TC-QCS-029 vì boundary suy diễn; chuyển câu hỏi về Feature questions; đổi cột nguồn về `Nguồn` | [[WIKI_RULES]] |
| 2026-05-23 00:25:00 | v1.0 | Khởi tạo Test Suite từ Feature Spec v1.0 — 32 test cases | [[wiki/project_hasaki/features/hasaki_qc_setup\|hasaki_qc_setup]] |