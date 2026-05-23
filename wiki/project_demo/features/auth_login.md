---
aliases: [JIRA-101, auth_login, Đăng nhập, Login]
tags: [qa/requirement]
status: Done
created: 2026-05-23
updated: 2026-05-23
feature: Đăng nhập bằng Email và Mật khẩu
project: QA LLM Wiki Demo
source_version: v1.0
---

# 📋 REQ: Đăng nhập bằng Email và Mật khẩu

## Tổng quan
- **Mã tính năng:** FEAT-AUTH-01
- **Feature:** Đăng nhập hệ thống (Authentication)
- **Mô tả ngắn:** Cho phép người dùng đăng nhập vào hệ thống bằng tài khoản email và mật khẩu đã đăng ký, đảm bảo bảo mật thông tin và điều hướng chính xác.
- **Source chính:** Ticket [[raw_sources/project_demo/tasks/JIRA-101|JIRA-101]]
- **Đối tượng sử dụng (Actors):** Khách hàng thường (User), Admin
- **Test Suite tương ứng:** [[wiki/project_demo/test_suites/test_auth_login|test_auth_login]]

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | Ticket | [[raw_sources/project_demo/tasks/JIRA-101|JIRA-101: Đăng nhập bằng Email và Mật khẩu]] | v1.0 | ✅ Hiện hành |

## Phân rã Requirement
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Đăng nhập thành công bằng email và mật khẩu đúng | Functional | High | ✅ | JIRA-101, mục 2 |
| R2 | Validate định dạng email và mật khẩu | Validation | High | ✅ | JIRA-101, mục 1 |
| R3 | Khóa tài khoản 15 phút nếu nhập sai quá 5 lần liên tiếp | Security | High | ✅ | JIRA-101, mục 2 |
| R4 | Giao diện hiển thị nút ẩn/hiện mật khẩu | UI/UX | Medium | ✅ | JIRA-101, mục 3 |
| R5 | Link hướng tới "Quên mật khẩu" và "Đăng ký" | UI/UX | Medium | ✅ | JIRA-101, mục 3 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- Người dùng đã mở trang Đăng nhập trên trình duyệt.
- Người dùng đã có tài khoản được kích hoạt trên hệ thống.

### Luồng chuẩn (Happy Path)
1. Người dùng nhập Email hợp lệ đã đăng ký (ví dụ: `test_user@example.com`).
2. Người dùng nhập Mật khẩu chính xác tương ứng.
3. Người dùng click nút **"Đăng nhập"**.
4. Hệ thống xác thực thông tin, cấp Access Token và điều hướng người dùng về trang **Dashboard**.

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1: Ẩn/Hiện mật khẩu**
  1. Người dùng nhập mật khẩu (dạng mặc định sẽ hiển thị dưới dạng dấu sao/chấm đen).
  2. Người dùng click vào biểu tượng **"Con mắt"** (Ẩn/Hiện mật khẩu).
  3. Hệ thống hiển thị mật khẩu dưới dạng văn bản thường. Click lại sẽ ẩn đi.
- **Alt-Flow 2: Khôi phục mật khẩu**
  1. Người dùng click vào link **"Quên mật khẩu"**.
  2. Hệ thống điều hướng người dùng sang trang **Yêu cầu khôi phục mật khẩu**.

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1: Nhập sai thông tin đăng nhập**
  1. Người dùng nhập sai Email hoặc Mật khẩu.
  2. Hệ thống hiển thị thông báo lỗi chung: `"Email hoặc mật khẩu không chính xác"`.
- **Exc-Flow 2: Tài khoản bị khóa do Brute Force**
  1. Người dùng nhập sai mật khẩu **5 lần liên tiếp** trên cùng một Email.
  2. Ở lần thứ 5, hệ thống khóa tài khoản trong **15 phút**.
  3. Hiển thị thông báo: `"Tài khoản đã bị tạm khóa 15 phút do nhập sai quá nhiều lần"`. Mọi nỗ lực đăng nhập trong thời gian này đều bị từ chối ngay lập tức.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------|:---------|:----------|:-------------------------------|
| Email | Chuỗi chữ (String) | ✅ Bắt buộc | Phải đúng định dạng RFC 5322 (ví dụ: có ký tự `@` và domain `.xxx`). |
| Mật khẩu | Chuỗi chữ (String) | ✅ Bắt buộc | Tối thiểu 10 ký tự, tối đa 32 ký tự. Phải chứa: ít nhất 1 chữ hoa, 1 chữ thường, 1 số và 1 ký tự đặc biệt (`!@#$%^&*`). |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
- **Bỏ trống Email:** `"Vui lòng nhập Email"`
- **Bỏ trống Mật khẩu:** `"Vui lòng nhập Mật khẩu"`
- **Định dạng Email sai:** `"Email không đúng định dạng"`
- **Mật khẩu không đủ 10 ký tự:** `"Mật khẩu phải tối thiểu 10 ký tự"`
- **Đăng nhập sai tài khoản/mật khẩu:** `"Email hoặc mật khẩu không chính xác"`
- **Bị khóa tài khoản:** `"Tài khoản đã bị tạm khóa 15 phút do nhập sai quá nhiều lần"`

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **Scenario 1: Đăng nhập thành công với tài khoản hợp lệ**
  - **Given:** Người dùng đang ở trang đăng nhập.
  - **When:** Người dùng nhập Email là `test_user@example.com` và Mật khẩu đúng.
  - **And:** Click nút **"Đăng nhập"**.
  - **Then:** Hệ thống xác thực thành công và chuyển hướng người dùng sang trang Dashboard.

- **Scenario 2: Báo lỗi khi để trống thông tin**
  - **Given:** Người dùng đang ở trang đăng nhập.
  - **When:** Người dùng để trống cả hai trường Email và Mật khẩu.
  - **And:** Click nút **"Đăng nhập"**.
  - **Then:** Hệ thống báo lỗi `"Vui lòng nhập Email"` và `"Vui lòng nhập Mật khẩu"`.

## ❓ Câu hỏi chưa rõ
- [ ] ❓ Nếu người dùng click "Đăng nhập" liên tục nhiều lần trong khi API đang loading thì hệ thống có disable nút Đăng nhập để chặn double-request không?
- [ ] ❓ Thời gian 15 phút khóa tài khoản được tính theo thời gian thực của Server hay Client?

## 📝 Thay đổi so với version cũ
| # | Nội dung thay đổi | Version cũ | Version mới | Ảnh hưởng TC |
|:--|:------------------|:----------|:-----------|:-------------|
| 1 | Khởi tạo Specs đầu tiên | Không có | v1.0 | Khởi tạo test suite ban đầu |

## Test Coverage
| Requirement | Test Case(s) | Status |
|:-----------|:------------|:-------|
| R1 (Đăng nhập đúng) | [[wiki/project_demo/test_suites/test_auth_login#TC-001|TC-001]] | ⏳ |
| R2 (Validate dữ liệu) | [[wiki/project_demo/test_suites/test_auth_login#TC-002|TC-002]], [[wiki/project_demo/test_suites/test_auth_login#TC-003|TC-003]] | ⏳ |
| R3 (Khóa tài khoản) | [[wiki/project_demo/test_suites/test_auth_login#TC-004|TC-004]] | ⏳ |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 10:29:33 | v1.1 | Cập nhật độ dài mật khẩu tối thiểu từ 8 lên 10 ký tự theo yêu cầu mới | [[raw_sources/project_demo/tasks/JIRA-101|JIRA-101]] |
| 2026-05-23 10:10:29 | v1.0 | Khởi tạo phiên bản đầu tiên của Specs | [[raw_sources/project_demo/tasks/JIRA-101|JIRA-101]] |
