# 📋 TASK: Kiểm thử chức năng Login & Logout OrangeHRM

- **Nguồn yêu cầu:** Khách hàng / PO
- **URL kiểm thử:** `https://opensource-demo.orangehrmlive.com/web/index.php/auth/login`
- **Mục tiêu:** Kiểm thử toàn bộ nghiệp vụ đăng nhập (Login) và đăng xuất (Logout) của hệ thống OrangeHRM Demo để chuẩn bị đóng gói phát hành (Go-Live) vào ngày **30/05/2026**.
- **Dữ liệu đăng nhập mặc định (Sandbox):**
  - **Username:** `Admin`
  - **Password:** `admin123`

---

## 🔍 Yêu cầu Nghiệp vụ Cơ bản

### 1. Chức năng Login (Đăng nhập):
- **Giao diện:** Chứa trường nhập Username, Password, nút "Login", và link "Forgot your password?".
- **Validate Client-side:**
  - Bỏ trống Username hoặc Password ➔ Hiển thị thông báo validate lỗi ngay dưới trường đó: `"Required"`.
- **Validate Server-side:**
  - Nhập sai Username hoặc Password ➔ Hiển thị thông báo lỗi chung trên form: `"Invalid credentials"`.
- **Luồng thành công:** 
  - Nhập đúng Username (`Admin`) và Password (`admin123`) ➔ Điều hướng về trang Dashboard (`/web/index.php/dashboard/index`).
  - Hệ thống ghi nhận session và trả về dữ liệu Dashboard.

### 2. Chức năng Logout (Đăng xuất):
- **Giao diện:** Người dùng nhấn vào Avatar/Tên User ở góc trên cùng bên phải màn hình ➔ Hiển thị Menu thả xuống (Dropdown) chứa mục "Logout".
- **Luồng thành công:**
  - Click "Logout" ➔ Hệ thống hủy Session/Cookies và điều hướng người dùng quay trở lại trang Đăng nhập (`/web/index.php/auth/login`).
  - Nhấn nút Back trên trình duyệt sau khi logout ➔ Tuyệt đối KHÔNG được truy cập lại Dashboard (phải bị chặn và giữ ở trang Login).
