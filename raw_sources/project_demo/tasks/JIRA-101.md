---
tags: [task, raw-source]
status: 🌳 baseline
created: 2026-05-23
---

# 🎫 JIRA-101: Triển khai Đăng nhập bằng Email và Mật khẩu

- **Mã Task:** JIRA-101
- **Người yêu cầu:** PO (Product Owner)
- **Độ ưu tiên:** High
- **Mô tả yêu cầu:**
  Hệ thống cần cung cấp giao diện và API cho phép người dùng đăng nhập bằng tài khoản Email đã đăng ký.

## 📋 Chi tiết yêu cầu:
1. **Trường dữ liệu:**
   - **Email:** Phải đúng định dạng email (ví dụ: `user@example.com`). Không được để trống.
   - **Mật khẩu:** Tối thiểu 10 ký tự, phải chứa ít nhất 1 chữ hoa, 1 chữ thường và 1 ký tự đặc biệt. Không được để trống.
1. **Logic xử lý đăng nhập:**
   - Đăng nhập thành công: Chuyển hướng người dùng về trang Dashboard và cấp Access Token.
   - Đăng nhập thất bại (sai email hoặc mật khẩu): Hiển thị thông báo lỗi chung: `"Email hoặc mật khẩu không chính xác"`.
   - Tài khoản bị khóa: Nếu nhập sai mật khẩu quá **5 lần liên tiếp**, tài khoản sẽ bị khóa trong **15 phút**. Hiển thị thông báo: `"Tài khoản đã bị tạm khóa 15 phút do nhập sai quá nhiều lần"`.
3. **Yêu cầu UI:**
   - Có nút ẩn/hiện mật khẩu (biểu tượng con mắt).
   - Có link "Quên mật khẩu" trỏ sang trang khôi phục mật khẩu.
   - Có link "Đăng ký ngay" trỏ sang trang tạo tài khoản mới.
