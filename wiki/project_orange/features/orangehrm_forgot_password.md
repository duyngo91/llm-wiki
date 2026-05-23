---
aliases: [forgot_password, Quên mật khẩu OrangeHRM, CR-ORANGE-205]
tags: [qa/requirement]
status: Draft
created: 2026-05-23
updated: 2026-05-23
feature: Quên mật khẩu OrangeHRM
project: OrangeHRM_Demo
source_version: v1.0
---

# 📋 REQ: Yêu cầu nghiệp vụ Quên Mật Khẩu (Forgot Password)

## Tổng quan
- **Mã tính năng:** `REQ-AUTH-02`
- **Feature:** Quên mật khẩu OrangeHRM
- **Mô tả ngắn:** Cho phép người dùng tự yêu cầu gửi liên kết đặt lại mật khẩu qua email khi quên thông tin đăng nhập.
- **Source chính:** [[raw_sources/project_orange/tasks/orangehrm_forgot_password|CR-ORANGE-205]]
- **Đối tượng sử dụng (Actors):** Tất cả người dùng (Admin, HR Manager, Employees).
- **Test Suite tương ứng:** [[wiki/project_orange/test_suites/test_orangehrm_forgot_password|test_orangehrm_forgot_password]]

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | Link | [[raw_sources/project_orange/tasks/orangehrm_forgot_password\|CR-ORANGE-205]] | v1.0 | ✅ Hiện hành |

## Phân rã Requirement
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| **R1** | Hiển thị màn hình Reset Password với title, mô tả, ô nhập Username và 2 nút Cancel, Reset Password. | Functional | High | ✅ | CR-ORANGE-205 |
| **R2** | Nút Cancel đưa người dùng quay lại màn hình Login `/auth/login`. | Functional | Medium | ✅ | CR-ORANGE-205 |
| **R3** | Validate bắt buộc nhập Username phía Client trước khi gửi request. | Security | High | ✅ | CR-ORANGE-205 |
| **R4** | Gửi request POST lên API `/auth/requestResetPassword` kèm payload Username khi hợp lệ. | Functional | Critical | ✅ | CR-ORANGE-205 |
| **R5** | Chuyển hướng sang trang `/auth/sendPasswordReset` hiển thị thông điệp thành công màu xanh lá khi gửi reset thành công. | Functional | High | ✅ | CR-ORANGE-205 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- Trình duyệt mở bình thường, đang ở màn hình Đăng nhập OrangeHRM.

### Luồng chuẩn (Happy Path)
1. Người dùng click vào link **"Forgot your password?"** trên màn hình Login.
2. Hệ thống điều hướng sang màn hình `/web/index.php/auth/requestPasswordResetCode`.
3. Người dùng nhập Username hợp lệ (ví dụ: `Admin`).
4. Người dùng click nút **"Reset Password"**.
5. Hệ thống gửi request POST `/auth/requestResetPassword` lên server.
6. Server xử lý thành công và trả về mã thành công.
7. Hệ thống chuyển hướng sang trang `/web/index.php/auth/sendPasswordReset` hiển thị thông báo màu xanh lá: `"A reset password link has been sent to your email on file. Please check your inbox."`

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 (Cancel flow):** 
  1. Tại màn hình Reset Password, người dùng click nút **"Cancel"**.
  2. Hệ thống hủy thao tác và điều hướng người dùng quay trở lại trang đăng nhập `/web/index.php/auth/login`.

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1 (Empty Username):** 
  1. Người dùng bỏ trống trường Username.
  2. Click nút **"Reset Password"**.
  3. Hệ thống chặn không gửi request lên server, viền đỏ trường nhập và hiển thị chữ báo lỗi màu đỏ: `"Required"` dưới ô nhập Username.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------|:---------|:----------|:-------------------------------|
| **Username** | Chuỗi văn bản | Có | Không được chứa khoảng trắng ở đầu/cuối, validate không được để trống khi click Reset Password. |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
- **Lỗi bỏ trống Username:** `"Required"` (hiển thị màu đỏ dưới ô Username).

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **Scenario 1: Điều hướng thành công từ Login sang Reset Password**
  - **Given:** Người dùng đang ở màn hình Đăng nhập OrangeHRM.
  - **When:** Người dùng click link "Forgot your password?".
  - **Then:** Hệ thống điều hướng người dùng sang trang `/web/index.php/auth/requestPasswordResetCode`.
  - **And:** Hiển thị màn hình "Reset Password" đúng mô tả.

- **Scenario 2: Đăng ký reset password thành công**
  - **Given:** Người dùng đang ở màn hình Reset Password.
  - **When:** Người dùng nhập Username là `Admin` và click "Reset Password".
  - **Then:** Hệ thống gửi request POST lên API xác thực.
  - **And:** Chuyển hướng sang trang `/web/index.php/auth/sendPasswordReset` với thông báo thành công màu xanh lá.

- **Scenario 3: Hủy thao tác yêu cầu reset password**
  - **Given:** Người dùng đang ở màn hình Reset Password.
  - **When:** Người dùng click nút "Cancel".
  - **Then:** Hệ thống điều hướng người dùng quay trở lại trang đăng nhập `/web/index.php/auth/login`.

- **Scenario 4: Bỏ trống Username khi yêu cầu reset**
  - **Given:** Người dùng đang ở màn hình Reset Password và ô Username để trống.
  - **When:** Người dùng click "Reset Password".
  - **Then:** Hệ thống hiển thị thông báo lỗi `"Required"` màu đỏ ngay dưới trường Username.
  - **And:** Ngăn chặn gửi request lên server.

## ❓ Câu hỏi chưa rõ
- [ ] ❓ Trong trường hợp nhập Username không tồn tại trong hệ thống, UI hiển thị lỗi báo không tồn tại hay vẫn hiển thị thông điệp thành công chung để bảo mật thông tin tài khoản? (QA khuyến nghị: Vẫn báo thành công chung để tránh dò quét Username).

## 📝 Thay đổi so với version cũ
*Đây là phiên bản khởi tạo ban đầu, không có lịch sử thay đổi.*

## Test Coverage
| Requirement | Test Case(s) | Status |
|:-----------|:------------|:-------|
| **R1** | [[wiki/project_orange/test_suites/test_orangehrm_forgot_password\|TC-OH-008]] | ⏳ |
| **R2** | [[wiki/project_orange/test_suites/test_orangehrm_forgot_password\|TC-OH-009]] | ⏳ |
| **R3** | [[wiki/project_orange/test_suites/test_orangehrm_forgot_password\|TC-OH-010]] | ⏳ |
| **R4 & R5** | [[wiki/project_orange/test_suites/test_orangehrm_forgot_password\|TC-OH-011]], [[wiki/project_orange/test_suites/test_orangehrm_forgot_password\|TC-OH-012]] | ⏳ |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 15:30:00 | v1.0 | Khởi tạo phiên bản đặc tả nghiệp vụ Quên mật khẩu đầu tiên. | [[raw_sources/project_orange/tasks/orangehrm_forgot_password\|CR-ORANGE-205]] |
