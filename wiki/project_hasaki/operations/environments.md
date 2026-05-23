---
tags: [qa/operations]
status: Done
updated: 2026-05-23
project: project_hasaki
---

# 🌐 Môi Trường & Hệ Thống — Hasaki

> Thông tin cấu hình các môi trường test của dự án Hasaki. AI sẽ đọc file này để lấy URL và tài khoản test thực tế khi thiết kế Test Cases hoặc chạy Automation.

---

## 🧪 Staging (Môi trường Test chính)
- **URL Web:** *(cập nhật URL staging)*
- **URL API:** *(cập nhật base URL API)*
- **Tài khoản test mẫu:**

| Vai trò | Username / Email | Password | Ghi chú |
|:--------|:----------------|:---------|:--------|
| Admin | *(cập nhật)* | *(cập nhật)* | Tài khoản test nội bộ |
| User thường | *(cập nhật)* | *(cập nhật)* | |

- **CI/CD Pipeline:** *(cập nhật)*

---

## 🚀 Production (Môi trường thực tế)
- **URL Web:** `https://hasaki.vn`
- **Workplace (Task Management):** `https://work.hasaki.vn`
- **⚠️ Quy định:** Không chạy automation test hoặc tạo dữ liệu rác trên Production.

---

## 📅 Changelog
| Ngày | Nội dung thay đổi |
|:-----|:------------------|
| 2026-05-23 | Khởi tạo cấu hình môi trường dự án Hasaki |
