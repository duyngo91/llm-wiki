---
aliases: [testplan_cr_101, Kế hoạch test JIRA-101, Test Plan Email Login]
tags: [qa/test-plan]
status: Passed
project: project_demo
created: 2026-05-23
updated: 2026-05-23
---

# 📋 TEST PLAN: Kế hoạch Kiểm thử tính năng Đăng nhập Email

> **Kế hoạch kiểm thử:** Chiến lược, phạm vi, môi trường, dữ liệu và tiêu chí chất lượng cho đợt kiểm thử tính năng Đăng nhập bằng Email và Mật khẩu (Mật khẩu tối thiểu 10 ký tự).

---

## 🔍 1. Phạm vi Kiểm thử (Testing Scope)

### 1.1. Trong phạm vi kiểm thử (In-Scope)
- **Các tính năng kiểm thử mới / thay đổi:**
  - [[wiki/project_demo/features/auth_login|auth_login]] — Cập nhật logic validate mật khẩu tối thiểu 10 ký tự (thay vì 8 ký tự như cũ).
- **Phạm vi kiểm thử hồi quy (Regression Scope):**
  - Chạy lại toàn bộ kịch bản đăng nhập cơ bản để đảm bảo không bị lỗi ảnh hưởng phụ:
    - Đăng nhập thành công với mật khẩu đúng (>= 10 ký tự).
    - Đăng nhập thất bại khi sai tài khoản / mật khẩu.
    - Khóa tài khoản sau 5 lần nhập sai liên tiếp.

### 1.2. Ngoài phạm vi kiểm thử (Out-of-Scope)
- Luồng Quên mật khẩu / Reset password qua Email (không bị ảnh hưởng bởi thay đổi validate ở màn hình Login).

---

## 🛠️ 2. Chiến lược & Môi trường Kiểm thử

### 2.1. Thiết bị & Trình duyệt
- Web: Google Chrome (Bản mới nhất), Safari trên macOS.

### 2.2. Môi trường Test chính
- [[wiki/project_demo/operations/environments|🌐 Cấu hình Môi trường Test Staging/UAT]] (Staging: `https://staging.example.com`)

### 2.3. Dữ liệu Test yêu cầu (Test Data Required)
- [[wiki/project_demo/operations/test_data|📦 Kho dữ liệu test mẫu]] (Tài khoản mẫu: `test_exist@mailinator.com`)

---

## 📈 3. Test Coverage & Độ phủ kịch bản
| Module / Yêu cầu | Test Suite tương ứng | Số kịch bản | Trạng thái kịch bản |
|:-----------------|:---------------------|:------------|:-------------------|
| FEAT-AUTH-01 Đăng nhập Email | [[wiki/project_demo/test_suites/test_auth_login|test_auth_login]] | 5 kịch bản | ✅ Passed |

---

## 🏁 4. Tiêu chí dừng kiểm thử (Exit Criteria)
- [x] 100% các kịch bản test thuộc [[wiki/project_demo/test_suites/test_auth_login|test_auth_login]] đạt trạng thái **`✅ Pass`** trên Staging (Đã đạt: 5/5 cases Pass).
- [x] Không còn tồn đọng lỗi nghiêm trọng (`Blocker`, `Critical`, `Major`).
- [x] Specs nghiệp vụ và Test cases được đồng bộ hóa hoàn toàn trên hệ thống.

---

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Người thực hiện |
|:----------|:--------|:------------------|:----------------|
| 2026-05-23 10:38:09 | v1.1 | Chạy hồi quy thành công, cập nhật trạng thái thông qua. | QA_Lead |
| 2026-05-23 10:10:29 | v1.0 | Khởi tạo Kế hoạch kiểm thử (Test Plan). | QA_Lead |
