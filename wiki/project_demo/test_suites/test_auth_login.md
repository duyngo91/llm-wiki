---
aliases:
  - test_auth_login
  - Test Suite Đăng nhập
  - Test Login
tags:
  - qa/test-suite
status: Passed
feature: Đăng nhập bằng Email và Mật khẩu
requirement:
  - - wiki/project_demo/features/auth_login|REQ: Đăng nhập
dev: Dev_Backend_Lead
qa: Ngo Van Duy
created: 2026-05-23
updated: 2026-05-23
---

# 🧪 Test Suite: Đăng nhập bằng Email và Mật khẩu

- **Feature liên quan:** [[wiki/project_demo/features/auth_login|📋 REQ: Đăng nhập]]
- **Requirement:** [[wiki/project_demo/features/auth_login|REQ: Đăng nhập]]
- **Dev phụ trách:** Dev_Backend_Lead
- **QA phụ trách:** Ngo Van Duy
- **Ngày cập nhật cuối:** 2026-05-23

## 📊 Tổng quan Test Coverage
| Loại Test | Số lượng TC | Pass | Fail | Blocked | Chưa test |
|:----------|:-----------|:-----|:-----|:--------|:----------|
| Happy Path | 1 | 1 | 0 | 0 | 0 |
| Negative | 3 | 3 | 0 | 0 | 0 |
| Security | 1 | 1 | 0 | 0 | 0 |
| **Tổng** | **5** | **5** | **0** | **0** | **0** |

## ✅ Test Cases

| Test ID | Tiêu đề | Điều kiện tiên quyết | Các bước thực hiện | Kết quả mong đợi | Loại Test | Status |
|:--------|:--------|:--------------------|:-------------------|:-----------------|:----------|:-------|
| **TC-001** | Đăng nhập thành công với tài khoản Staging | 1. Có tài khoản test hợp lệ trên môi trường [[wiki/project_demo/operations/environments\|Staging]]: `test_exist@mailinator.com` / `ValidPass@123`. | 1. Truy cập `https://staging.example.com`<br>2. Nhập Email và Mật khẩu đúng.<br>3. Click "Đăng nhập". | Đăng nhập thành công, điều hướng về `/dashboard`, có Access Token trong Session. | Happy Path | ✅ Pass |
| **TC-002** | Báo lỗi khi nhập sai Mật khẩu | 1. Tài khoản `test_exist@mailinator.com` tồn tại.<br>2. Truy cập trang đăng nhập Staging. | 1. Nhập Email: `test_exist@mailinator.com`<br>2. Nhập Mật khẩu sai: `WrongPass@1`<br>3. Click "Đăng nhập". | Hiển thị thông báo lỗi: `"Email hoặc mật khẩu không chính xác"`. Không chuyển hướng. | Negative | ✅ Pass |
| **TC-003** | Validate định dạng Email không hợp lệ | 1. Truy cập trang đăng nhập Staging. | 1. Nhập Email sai định dạng: `invalid-email.com`<br>2. Nhập Mật khẩu hợp lệ.<br>3. Click "Đăng nhập". | Hệ thống hiển thị thông báo lỗi validate ngay trên form: `"Email không đúng định dạng"`. | Negative | ✅ Pass |
| **TC-004** | Khóa tài khoản sau 5 lần nhập sai liên tiếp | 1. Tài khoản `test_exist@mailinator.com` đang hoạt động bình thường. | 1. Nhập liên tiếp 5 lần mật khẩu sai `WrongPass@1` cho Email `test_exist@mailinator.com`. Click "Đăng nhập" ở mỗi lần. | Lần 1-4: Báo lỗi sai tài khoản/mật khẩu.<br>Lần 5: Tài khoản bị khóa, hiển thị lỗi `"Tài khoản đã bị tạm khóa 15 phút do nhập sai quá nhiều lần"`. | Security | ✅ Pass |
| **TC-005** | Báo lỗi khi nhập mật khẩu dưới 10 ký tự | 1. Có tài khoản test hợp lệ.<br>2. Truy cập trang đăng nhập Staging. | 1. Nhập Email đúng.<br>2. Nhập Mật khẩu 9 ký tự (ví dụ: `Pass@1234` - chứa chữ hoa, thường, số, đặc biệt nhưng thiếu độ dài).<br>3. Click "Đăng nhập". | Hệ thống hiển thị thông báo lỗi validate ngay trên form: `"Mật khẩu phải tối thiểu 10 ký tự"`. Không gửi request lên server. | Negative | ✅ Pass |

## 🚫 Test Cases Lỗi Thời (Deprecated)
*Các test case không còn áp dụng do thay đổi requirement. Lưu lại để tham khảo.*

| Test ID | Tiêu đề | Lý do deprecated | Ngày | Nguồn |
|:--------|:--------|:-----------------|:-----|:------|
| | | | | |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 10:38:09 | v1.2 | Hoàn thành toàn bộ kiểm thử, 5/5 cases PASS, chuyển Test Suite sang evergreen sau khi task được lưu trữ | [[wiki/project_demo/features/auth_login|REQ Đăng nhập]] |
| 2026-05-23 10:29:33 | v1.1 | Thêm TC-005 kiểm tra độ dài mật khẩu tối thiểu 10 ký tự do thay đổi Specs | [[wiki/project_demo/features/auth_login|REQ Đăng nhập]] |
| 2026-05-23 10:10:29 | v1.0 | Khởi tạo Test Suite đầu tiên cho tính năng Đăng nhập Email | [[wiki/project_demo/features/auth_login|REQ Đăng nhập]] |
