---
aliases: [orangehrm_auth, OrangeHRM Đăng nhập, Login OrangeHRM]
tags: [qa/requirement]
status: Done
created: 2026-05-23
updated: 2026-05-23
feature: Đăng nhập & Đăng xuất OrangeHRM
project: OrangeHRM_Demo
source_version: v1.0
---

# 📋 REQ: Nghiệp vụ Đăng nhập & Đăng xuất OrangeHRM

> **Tài liệu đặc tả nghiệp vụ (BA Specs):** Mô tả chi tiết luồng đăng nhập, đăng xuất, các ràng buộc dữ liệu, thông điệp báo lỗi và tiêu chí nghiệm thu của hệ thống OrangeHRM.

---

## 🧭 1. Tổng quan Nghiệp vụ
- **Mã tính năng:** `REQ-AUTH-01`
- **Mô tả ngắn:** Cho phép nhân sự đăng nhập vào hệ thống quản lý nhân sự OrangeHRM bằng tài khoản đã được cấp để làm việc, và đăng xuất an toàn để bảo mật thông tin.
- **URL kiểm thử:** `https://opensource-demo.orangehrmlive.com/web/index.php/auth/login`
- **Đối tượng sử dụng (Actors):** Tất cả nhân viên trong doanh nghiệp (Admin, HR Manager, Employees).
- **Test Suite tương ứng:** [[wiki/project_orange/test_suites/test_orangehrm_auth|test_orangehrm_auth]]

---

## 📄 2. Nguồn tài liệu & Kỹ thuật
| # | Loại | Tên / Link | Version | Trạng thái |
|:--|:-----|:-----------|:--------|:-----------|
| 1 | Link | [OrangeHRM Portal](https://opensource-demo.orangehrmlive.com/) | Live Demo | ✅ Hiện hành |
| 2 | JSON | [[raw_sources/assets/orangehrm_api_logs.json\|API Network Logs]] | POST /auth/validate | ✅ Hiện hành |

---

## 🔍 3. Phân rã Requirement (Requirements Breakdown)
| ID | Requirement | Loại | Độ ưu tiên | Testable? | Nguồn |
|:---|:------------|:-----|:-----------|:----------|:------|
| **R1** | Hiển thị đầy đủ form đăng nhập (Username, Password, nút Login, link Forgot Password). | Functional | High | ✅ | OrangeHRM Portal |
| **R2** | Validate bắt buộc nhập cả Username và Password phía Client. | Security | High | ✅ | OrangeHRM Portal |
| **R3** | Xác thực thông tin tài khoản qua API Backend POST `/auth/validate`. | Functional | Critical | ✅ | orangehrm_api_logs.json |
| **R4** | Điều hướng về trang Dashboard khi đăng nhập thành công. | Functional | Critical | ✅ | orangehrm_api_logs.json |
| **R5** | Cho phép đăng xuất thông qua menu góc trên bên phải. | Functional | High | ✅ | OrangeHRM Portal |
| **R6** | Hủy hoàn toàn session và token sau khi đăng xuất thành công. | Security | Critical | ✅ | OrangeHRM Portal |

---

## 🔄 4. Luồng Nghiệp Vụ Chi Tiết (User Flows)

### 4.1. Điều kiện tiên quyết (Pre-conditions)
- Thiết bị có kết nối Internet ổn định.
- Tài khoản người dùng đã được tạo và kích hoạt sẵn trên hệ thống (Mặc định: `Admin` / `admin123`).

### 4.2. Luồng chuẩn: Đăng nhập thành công (Happy Path - Login)
1. Người dùng truy cập URL: `https://opensource-demo.orangehrmlive.com/web/index.php/auth/login`.
2. Hệ thống hiển thị Form đăng nhập.
3. Người dùng nhập Username: `Admin`.
4. Người dùng nhập Password: `admin123`.
5. Người dùng click nút **"Login"**.
6. Hệ thống gửi request POST `/auth/validate` kèm payload mã hóa form-urlencoded.
7. Server kiểm tra thông tin hợp lệ ➔ Trả về mã redirect `302 Found`.
8. Hệ thống thiết lập session cookie (`orangehrm`) và điều hướng người dùng về trang Dashboard `/web/index.php/dashboard/index`.

### 4.3. Luồng chuẩn: Đăng xuất thành công (Happy Path - Logout)
1. Người dùng đang ở màn hình Dashboard (đã đăng nhập).
2. Click vào Avatar hoặc Tên User ở góc trên bên phải màn hình.
3. Hệ thống mở Dropdown Menu.
4. Người dùng click **"Logout"**.
5. Hệ thống gửi request hủy session, xóa cookies trên trình duyệt.
6. Hệ thống điều hướng người dùng quay trở lại trang Đăng nhập ban đầu `/web/index.php/auth/login`.

### 4.4. Luồng ngoại lệ: Nhập sai tài khoản (Exception Path 1)
- **Khi:** Người dùng nhập sai Username hoặc sai Password ➔ Click "Login".
- **Hệ thống xử lý:** Server trả về lỗi xác thực ➔ Form hiển thị thông báo lỗi màu đỏ ở đầu trang: `"Invalid credentials"`. Người dùng giữ lại ở trang đăng nhập.

### 4.5. Luồng ngoại lệ: Bỏ trống trường bắt buộc (Exception Path 2)
- **Khi:** Người dùng để trống Username hoặc Password hoặc cả hai ➔ Click "Login".
- **Hệ thống xử lý:** Client validate lập tức trước khi gửi API ➔ Hiển thị dòng chữ validate lỗi màu đỏ ngay dưới trường bị bỏ trống: `"Required"`. Nút Login bị chặn gửi request.

### 4.6. Luồng bảo mật: Chặn truy cập lại sau khi Logout (Security Path)
- **Khi:** Người dùng đã Logout thành công về trang Login ➔ Nhấn nút "Back" (Quay lại) trên trình duyệt.
- **Hệ thống xử lý:** Hệ thống chặn không cho quay lại Dashboard, tự động redirect giữ người dùng ở trang Login `/auth/login` (vì Session cũ đã bị hủy hoàn toàn trên Server).

---

## ⚙️ 5. Ràng buộc dữ liệu & Validation Rules
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc logic |
|:-----------|:----------|:----------|:----------------|
| **Username**| Chuỗi văn bản | Có | Không được chứa khoảng trắng ở đầu/cuối, phân biệt chữ hoa chữ thường. |
| **Password**| Chuỗi mật khẩu | Có | Phân biệt chữ hoa chữ thường, ẩn dưới dạng dấu chấm `●●●●●●`. |

---

## 🚨 6. Bản đồ Thông điệp Báo lỗi (Error Messages Map)
- **Lỗi để trống Username/Password:** `"Required"` (hiển thị màu đỏ ngay dưới input).
- **Lỗi sai tài khoản hoặc mật khẩu:** `"Invalid credentials"` (hiển thị trong khung đỏ đầu Form).

---

## 🏁 7. Tiêu chí nghiệm thu BDD (Acceptance Criteria)

### Scenario 1: Đăng nhập thành công với tài khoản quản trị viên
- **Given** Người dùng truy cập trang Đăng nhập OrangeHRM.
- **When** Người dùng nhập Username là `Admin` và Password là `admin123`.
- **And** Click nút "Login".
- **Then** Người dùng được chuyển hướng thành công đến trang Dashboard chính và nhìn thấy thanh Menu quản lý.

### Scenario 2: Bỏ trống trường dữ liệu bắt buộc
- **Given** Người dùng đang ở màn hình Đăng nhập.
- **When** Người dùng để trống trường "Username" và nhập Password hợp lệ.
- **And** Click nút "Login".
- **Then** Hệ thống hiển thị lỗi `"Required"` ngay bên dưới ô nhập Username.
- **And** Không gửi bất kỳ yêu cầu xác thực nào lên server.

### Scenario 3: Đăng xuất an toàn khỏi hệ thống
- **Given** Người dùng đã đăng nhập thành công và đang ở trang Dashboard.
- **When** Người dùng click Avatar ở góc phải và chọn "Logout".
- **Then** Hệ thống hủy Session trên server và chuyển hướng người dùng về trang Login.
- **And** Nhấn nút "Back" trên trình duyệt không thể quay trở lại Dashboard.

---

## 📈 8. Độ phủ kiểm thử (Test Coverage Mapping)
| Requirement ID | Kịch bản kiểm thử (Test Cases) | Trạng thái |
|:---------------|:-------------------------------|:-----------|
| **R1** (Giao diện) | [[wiki/project_orange/test_suites/test_orangehrm_auth\|TC-OH-001]] | ✅ Pass |
| **R2** (Validate Client)| [[wiki/project_orange/test_suites/test_orangehrm_auth\|TC-OH-002]], [[wiki/project_orange/test_suites/test_orangehrm_auth\|TC-OH-003]] | ✅ Pass |
| **R3 & R4** (Luồng Login)| [[wiki/project_orange/test_suites/test_orangehrm_auth\|TC-OH-004]], [[wiki/project_orange/test_suites/test_orangehrm_auth\|TC-OH-005]] | ✅ Pass |
| **R5 & R6** (Luồng Logout)| [[wiki/project_orange/test_suites/test_orangehrm_auth\|TC-OH-006]], [[wiki/project_orange/test_suites/test_orangehrm_auth\|TC-OH-007]] | ✅ Pass |

---

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-23 14:34:00 | v1.0 | Khởi tạo bảng đặc tả nghiệp vụ Đăng nhập & Đăng xuất OrangeHRM. | [[raw_sources/project_orange/tasks/orangehrm_auth\|orangehrm_auth]] |
