---
tags: [qa/operations]
status: Done
updated: 2026-05-23
project: project_orange
---

# 🌐 Môi Trường & Hệ Thống — OrangeHRM Portal

> Thông tin cấu hình các môi trường test của dự án OrangeHRM Portal. AI sẽ đọc file này để lấy URL và tài khoản test thực tế khi thiết kế Test Cases hoặc chạy Automation.

---

## 🧪 Staging (Môi trường Test chính)
- **URL Web:** `https://opensource-demo.orangehrmlive.com/web/index.php/auth/login`
- **Tài khoản test mẫu:**

| Vai trò | Email / Username | Password | Ghi chú |
|:--------|:----------------|:---------|:--------|
| Quản trị viên (Admin) | `Admin` | `admin123` | Tài khoản Sandbox mặc định |

- **CI/CD Pipeline:** GitHub Actions

---

## 🚀 Production (Môi trường thực tế)
- **URL:** `https://opensource-demo.orangehrmlive.com/` (Đang chạy chung live demo)
- **⚠️ Quy định:** Tuyệt đối không được spam đổi mật khẩu hoặc chạy automation test xóa dữ liệu lớn trên môi trường Live Demo.

---

## 📅 Changelog
| Ngày | Nội dung thay đổi |
|:-----|:------------------|
| 2026-05-23 | Khởi tạo cấu hình môi trường chuẩn OrangeHRM Portal |
