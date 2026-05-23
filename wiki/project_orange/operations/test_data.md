---
tags: [qa/operations]
status: Done
updated: 2026-05-23
project: project_orange
---

# 📦 Kho Dữ Liệu Test Mẫu — OrangeHRM Portal

> AI sẽ đọc file này để lấy dữ liệu test thực tế khi thiết kế Test Cases hoặc viết script Automation cho dự án OrangeHRM Portal.

---

## 🔐 Tài khoản Sandbox mặc định
| Username | Password | Quyền truy cập | Kết quả mong đợi |
|:---------|:---------|:---------------|:------------------|
| `Admin` | `admin123` | Toàn quyền (Admin) | Đăng nhập thành công, điều hướng về Dashboard |
| `WrongUser` | `wrongpass` | Không hợp lệ | Đăng nhập thất bại, báo lỗi "Invalid credentials" |

---

## 📄 API Test Payloads (POST /auth/validate)
*Payload JSON mẫu giả lập xác thực API:*

```json
{
  "username": "Admin",
  "password": "admin123"
}
```

---

## 📅 Changelog
| Ngày | Nội dung thay đổi |
|:-----|:------------------|
| 2026-05-23 | Khởi tạo kho dữ liệu test mẫu chuẩn OrangeHRM Portal |
