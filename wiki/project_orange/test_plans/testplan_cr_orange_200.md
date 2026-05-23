---
aliases: [testplan_cr_orange_200, Kế hoạch test OrangeHRM, Test Plan OrangeHRM]
tags: [qa/test-plan]
status: Testing
project: project_orange
created: 2026-05-23
updated: 2026-05-23
---

# 📋 TEST PLAN: Kế hoạch Kiểm thử module Đăng nhập & Đăng xuất OrangeHRM

> **Kế hoạch kiểm thử:** Định hình phạm vi, chiến lược, môi trường, dữ liệu kiểm thử và tiêu chí đạt chất lượng (Exit Criteria) cho đợt kiểm thử module Đăng nhập & Đăng xuất của trang OrangeHRM Portal.

---

## 🔍 1. Phạm vi Kiểm thử (Testing Scope)

### 1.1. Trong phạm vi kiểm thử (In-Scope)
- **Các tính năng kiểm thử mới / thay đổi:**
  - [[wiki/project_orange/features/orangehrm_auth|orangehrm_auth]] — Nghiệp vụ xác thực tài khoản, kiểm tra validate form login và luồng đăng xuất bảo mật.
- **Phạm vi kiểm thử hồi quy (Regression Scope):**
  - Chạy lại kiểm thử giao diện Dashboard chính để đảm bảo việc phân quyền hoạt động đúng sau khi đăng nhập thành công.

### 1.2. Ngoài phạm vi kiểm thử (Out-of-Scope)
- **Những phần tạm thời không kiểm thử (và lý do):**
  - Tính năng "Forgot Password" gửi mail thực tế (chưa cấu hình máy chủ SMTP trên môi trường Staging).

---

## 🛠️ 2. Chiến lược & Môi trường Kiểm thử

### 2.1. Thiết bị & Trình duyệt
- Web: Google Chrome (Bản mới nhất), Mozilla Firefox, Apple Safari (kiểm tra cross-browser).

### 2.2. Môi trường Test chính
- [[wiki/project_orange/operations/environments|🌐 Cấu hình Môi trường Test Staging/UAT]] (Staging: `https://opensource-demo.orangehrmlive.com`)

### 2.3. Dữ liệu Test yêu cầu (Test Data Required)
- [[wiki/project_orange/operations/test_data|📦 Kho dữ liệu test mẫu]]
- Dữ liệu chi tiết: Tài khoản đăng nhập sandbox mặc định: `Admin` / `admin123`.

---

## 📈 3. Test Coverage & Độ phủ kịch bản
| Module / Yêu cầu | Test Suite tương ứng | Số kịch bản | Trạng thái kịch bản |
|:-----------------|:---------------------|:------------|:-------------------|
| REQ-AUTH-01 Đăng nhập & Đăng xuất | [[wiki/project_orange/test_suites/test_orangehrm_auth|test_orangehrm_auth]] | 7 kịch bản | ⏳ Đang chạy test |

---

## 🏁 4. Tiêu chí dừng kiểm thử (Exit Criteria)
- [ ] 100% các kịch bản test thuộc [[wiki/project_orange/test_suites/test_orangehrm_auth|test_orangehrm_auth]] đạt trạng thái **`✅ Pass`** trên Staging (Hiện tại: 0/7 cases Pass - Đang trong giai đoạn chạy test).
- [ ] Không còn tồn đọng lỗi nghiêm trọng (`Blocker`, `Critical`, `Major`).
- [ ] Mọi trường hợp edge case được ghi nhận và thống nhất phương án xử lý với Dev.

---

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Người thực hiện |
|:----------|:--------|:------------------|:----------------|
| 2026-05-23 14:38:40 | v1.0 | Khởi tạo Kế hoạch kiểm thử (Test Plan) chi tiết. | QA_Lead |
