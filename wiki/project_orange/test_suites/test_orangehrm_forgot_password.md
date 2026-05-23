---
aliases: [test_orangehrm_forgot_password, Test Cases Forgot Password Orange]
tags: [qa/test-suite]
status: Draft
feature: Quên mật khẩu OrangeHRM
requirement: [[wiki/project_orange/features/orangehrm_forgot_password|REQ: Quên mật khẩu OrangeHRM]]
dev: Dev_Backend_Lead
qa: QA_Lead
created: 2026-05-23
updated: 2026-05-23
---

# 🧪 Test Suite: Quên mật khẩu OrangeHRM

- **Feature liên quan:** [[wiki/project_orange/features/orangehrm_forgot_password|REQ: Quên mật khẩu OrangeHRM]]
- **Requirement:** [[wiki/project_orange/features/orangehrm_forgot_password|REQ: Quên mật khẩu OrangeHRM]]
- **Dev phụ trách:** Dev_Backend_Lead
- **QA phụ trách:** QA_Lead
- **Ngày cập nhật cuối:** 2026-05-23

## 📊 Tổng quan Test Coverage
| Loại Test | Số lượng TC | Pass | Fail | Blocked | Chưa test |
|:----------|:-----------|:-----|:-----|:--------|:----------|
| Happy Path | 3 | 0 | 0 | 0 | 3 |
| Negative | 2 | 0 | 0 | 0 | 2 |
| **Tổng** | **5** | **0** | **0** | **0** | **5** |

---

## ✅ Test Cases Chi Tiết

| Test ID | Tiêu đề kịch bản | Điều kiện tiên quyết | Các bước thực hiện | Kết quả mong đợi | Loại Test | Status |
|:--------|:-----------------|:---------------------|:-------------------|:-----------------|:----------|:-------|
| **TC-OH-008** | Kiểm tra hiển thị đầy đủ giao diện Quên mật khẩu | Đang ở trang Login: `https://opensource-demo.orangehrmlive.com/web/index.php/auth/login` | 1. Click vào đường link **"Forgot your password?"**.<br>2. Quan sát giao diện màn hình. | - Hệ thống điều hướng sang `/web/index.php/auth/requestPasswordResetCode`.<br>- Hiển thị đúng tiêu đề `"Reset Password"`.<br>- Hiển thị mô tả `"Please enter your username..."`.<br>- Có 1 ô nhập Username rỗng.<br>- Có đầy đủ 2 nút: "Cancel" và "Reset Password". | Happy Path | ⏳ |
| **TC-OH-009** | Kiểm tra chức năng nút Cancel quay lại trang Login | Đang đứng tại trang Reset Password: `/web/index.php/auth/requestPasswordResetCode` | 1. Click nút **"Cancel"** trên form. | - Hệ thống hủy thao tác.<br>- Điều hướng người dùng quay trở lại trang Login `/web/index.php/auth/login`. | Happy Path | ⏳ |
| **TC-OH-010** | Báo lỗi validate khi bỏ trống trường Username | Đang đứng tại trang Reset Password. | 1. Để trống ô nhập Username.<br>2. Click nút **"Reset Password"**. | - Hệ thống chặn không gửi API lên server.<br>- Ô nhập Username được viền đỏ.<br>- Dưới ô Username hiển thị thông báo lỗi màu đỏ: `"Required"`. | Negative | ⏳ |
| **TC-OH-011** | Đăng ký reset password thành công với tài khoản Sandbox Admin | Đang đứng tại trang Reset Password. Tài khoản sandbox hợp lệ: `Admin`. | 1. Nhập Username sandbox: `Admin`.<br>2. Click nút **"Reset Password"**. | - Hệ thống gửi request POST `/auth/requestResetPassword` thành công.<br>- Điều hướng sang trang `/web/index.php/auth/sendPasswordReset`.<br>- Hiển thị thông báo thành công màu xanh lá: `"A reset password link has been sent to your email on file. Please check your inbox."` | Happy Path | ⏳ |
| **TC-OH-012** | Reset password thành công với tài khoản không tồn tại (Bảo mật) | Đang đứng tại trang Reset Password. Tài khoản không tồn tại: `NonExistingUser`. | 1. Nhập Username không tồn tại: `NonExistingUser`.<br>2. Click nút **"Reset Password"**. | - Hệ thống gửi request POST `/auth/requestResetPassword` lên server.<br>- Server xử lý và trả về kết quả thành công giả (để bảo mật thông tin tài khoản).<br>- Điều hướng sang trang `/web/index.php/auth/sendPasswordReset`.<br>- Vẫn hiển thị thông điệp thành công chung màu xanh lá để tránh dò quét tài khoản. | Negative | ⏳ |

---

## 🚫 Test Cases Lỗi Thời (Deprecated)
*Hiện hành v1.0 — Chưa có test cases lỗi thời.*

---

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-23 15:35:00 | v1.0 | Khởi tạo bộ 5 kịch bản kiểm thử Quên mật khẩu theo thiết kế ISTQB. | [[wiki/project_orange/features/orangehrm_forgot_password\|REQ Quên mật khẩu OrangeHRM]] |
