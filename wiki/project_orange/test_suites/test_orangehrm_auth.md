---
aliases: [test_orangehrm_auth, Test Suite OrangeHRM, Test Cases Login Orange]
tags: [qa/test-suite]
status: Passed
feature: Đăng nhập & Đăng xuất OrangeHRM
requirement: [[wiki/project_orange/features/orangehrm_auth|REQ: Đăng nhập & Đăng xuất OrangeHRM]]
dev: Dev_Frontend_Lead
qa: QA_Lead
created: 2026-05-23
updated: 2026-05-23
---

# 🧪 Test Suite: Đăng nhập & Đăng xuất OrangeHRM

> **Kịch bản kiểm thử (Test Cases):** Bộ kịch bản chi tiết bao phủ toàn bộ nghiệp vụ từ giao diện, validate client/server đến bảo mật phiên đăng nhập của OrangeHRM Portal.

---

## 📊 Tổng quan Test Coverage
| Loại Test | Số lượng TC | Pass | Fail | Blocked | Chưa test |
|:----------|:-----------|:-----|:-----|:--------|:----------|
| Happy Path | 3 | 3 | 0 | 0 | 0 |
| Negative | 3 | 3 | 0 | 0 | 0 |
| Security | 1 | 1 | 0 | 0 | 0 |
| **Tổng** | **7** | **7** | **0** | **0** | **0** |

---

## ✅ Test Cases Chi Tiết

| Test ID | Tiêu đề kịch bản | Điều kiện tiên quyết | Các bước thực hiện | Kết quả mong đợi | Loại Test | Status |
|:--------|:-----------------|:---------------------|:-------------------|:-----------------|:----------|:-------|
| **TC-OH-001** | Kiểm tra hiển thị đầy đủ giao diện Đăng nhập | Trình duyệt mở bình thường, chưa đăng nhập hệ thống. | 1. Truy cập `https://opensource-demo.orangehrmlive.com/`<br>2. Quan sát giao diện màn hình. | - Hiển thị logo OrangeHRM.<br>- Có đầy đủ ô nhập Username, Password.<br>- Nút "Login" hiển thị rõ ràng.<br>- Có link "Forgot your password?". | Happy Path | ✅ Pass |
| **TC-OH-002** | Báo lỗi khi bỏ trống trường Username | Đang ở trang Đăng nhập, các ô nhập rỗng. | 1. Nhập Password đúng: `admin123`. Lần này để trống Username.<br>2. Click nút **"Login"**. | - Không gửi request lên server.<br>- Ô nhập Username được viền đỏ.<br>- Dòng lỗi chữ đỏ hiển thị dưới ô Username: `"Required"`. | Negative | ✅ Pass |
| **TC-OH-003** | Báo lỗi khi bỏ trống trường Password | Đang ở trang Đăng nhập, các ô nhập rỗng. | 1. Nhập Username đúng: `Admin`. Lần này để trống Password.<br>2. Click nút **"Login"**. | - Không gửi request lên server.<br>- Ô nhập Password được viền đỏ.<br>- Dòng lỗi chữ đỏ hiển thị dưới ô Password: `"Required"`. | Negative | ✅ Pass |
| **TC-OH-004** | Báo lỗi khi nhập sai Username hoặc Password | Đang ở trang Đăng nhập. | 1. Nhập sai Username (ví dụ: `WrongUser`) hoặc sai Password (ví dụ: `wrongpass`).<br>2. Click nút **"Login"**. | - Gửi request POST lên server.<br>- Server trả về lỗi xác thực.<br>- Màn hình hiển thị thông báo lỗi màu đỏ ở đầu Form: `"Invalid credentials"`. | Negative | ✅ Pass |
| **TC-OH-005** | Đăng nhập thành công với tài khoản Sandbox | Có tài khoản test hợp lệ: `Admin` / `admin123`. | 1. Nhập đúng Username `Admin` và Password `admin123`.<br>2. Click nút **"Login"**. | - Gửi request POST xác thực thành công.<br>- Điều hướng người dùng về trang Dashboard chính `/web/index.php/dashboard/index`. | Happy Path | ✅ Pass |
| **TC-OH-006** | Đăng xuất thành công khỏi hệ thống | Người dùng đã đăng nhập và đang ở trang Dashboard. | 1. Click vào Avatar / Tên User ở góc trên cùng bên phải.<br>2. Click chọn **"Logout"** trong Dropdown Menu. | - Xóa cookies session trên trình duyệt.<br>- Điều hướng người dùng quay trở lại trang đăng nhập `/web/index.php/auth/login`. | Happy Path | ✅ Pass |
| **TC-OH-007** | Bảo mật: Chặn truy cập Dashboard bằng nút Back sau Logout | Đã click Logout thành công và đang đứng ở màn hình Login. | 1. Nhấp nút **"Back" (Quay lại)** trên trình duyệt. | - Hệ thống ngăn chặn không cho truy cập lại trang Dashboard.<br>- Tự động redirect giữ người dùng ở trang Login `/auth/login`. | Security | ✅ Pass |

---

## 🚫 Test Cases Lỗi Thời (Deprecated)
*Hiện hành v1.0 — Chưa có test cases lỗi thời.*

---

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-23 14:35:00 | v1.0 | Khởi tạo Test Suite đầu tiên bao gồm 7 kịch bản cho Đăng nhập & Đăng xuất OrangeHRM. | [[wiki/project_orange/features/orangehrm_auth\|REQ Đăng nhập & Đăng xuất]] |
