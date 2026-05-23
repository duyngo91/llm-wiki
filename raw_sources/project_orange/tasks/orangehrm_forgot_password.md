# Task: CR-ORANGE-205 — Tích hợp tính năng Quên Mật Khẩu (Forgot Password)

## 🎯 Mô tả nghiệp vụ thô
Chúng ta cần làm tính năng Quên mật khẩu cho hệ thống Portal OrangeHRM.
Người dùng từ màn hình Login click vào link "Forgot your password?".
Hệ thống sẽ điều hướng sang màn hình `/web/index.php/auth/requestPasswordResetCode`.
Giao diện yêu cầu:
- Title màn hình: "Reset Password"
- Mô tả ngắn: "Please enter your username to identify your account and receive a password reset link."
- 1 ô nhập: Username (bắt buộc nhập, validate client không được rỗng)
- 2 nút:
  - "Cancel": click sẽ quay lại màn hình Login `/web/index.php/auth/login`.
  - "Reset Password": click sẽ kiểm tra, validate Username. Nếu trống báo lỗi "Required" màu đỏ dưới ô nhập. Nếu hợp lệ, gửi request POST lên API `/auth/requestResetPassword` kèm payload Username.
  
Phản hồi Server:
- Nếu Username tồn tại hoặc thành công: chuyển sang trang `/web/index.php/auth/sendPasswordReset` hiển thị thông điệp màu xanh lá: "A reset password link has been sent to your email on file. Please check your inbox."
- Nếu có lỗi hệ thống hoặc lỗi khác, hiển thị thông báo lỗi chung.

Độ ưu tiên: High. Dev phụ trách: Dev_Backend_Lead.
