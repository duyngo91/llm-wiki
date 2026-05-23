---
aliases: [CR-OrangeHRM Go-Live, Release-v2.0.0, cr_orangehrm_golive_30052026]
tags: [qa/release]
status: Draft
cr_id: CR-ORANGE-200
golive_date: 2026-05-30
deploy_window: 22:00 - 23:00
approver: PO_Lead
project: project_orange
---

# 🚀 CHANGE REQUEST: CR-ORANGE-200 Triển Khai Module Đăng Nhập & Đăng Xuất OrangeHRM

> **Biên bản Go-Live (Deployment Hub):** Quản lý kỹ thuật và nghiệm thu thực tế trên môi trường Production cho đợt Change Request (CR) **CR-ORANGE-200** — Module Đăng nhập & Đăng xuất.

---

## 📋 1. Phạm vi & Sự chuẩn bị (Prerequisites)
- **Kế hoạch kiểm thử Staging đã đạt Exit Criteria:** [[wiki/project_orange/test_plans/testplan_cr_orange_200|Test Plan Staging]] (Trạng thái: `Testing` - Đang chờ hoàn thành).
- **Mã Jira/Specs liên quan:**
  - [[wiki/project_orange/features/orangehrm_auth|orangehrm_auth (Specs)]] — Trạng thái: `Draft`.
  - [[wiki/project_orange/test_suites/test_orangehrm_auth|test_orangehrm_auth (Test Suite)]] — Trạng thái: `Testing`.

---

## 🚀 2. Kịch bản Triển khai từng bước (Deploy Steps)

*QA phối hợp với Dev/DevOps thực hiện vào khung giờ deploy: 22:00 ngày 30/05/2026.*

| Bước | Thời gian | Người thực hiện | Hành động chi tiết | Kết quả mong đợi |
| :--- | :--- | :--- | :--- | :--- |
| **1** | 22:00 | DevOps | Backup cơ sở dữ liệu và source code Production hiện tại. | Lưu bản backup an toàn trên Cloud Storage. |
| **2** | 22:15 | Dev Backend | Cập nhật DB Schema cho bảng User Session. | Database migration chạy thành công, không lỗi schema. |
| **3** | 22:30 | DevOps | Deploy API Backend phiên bản `v2.0.0`. | Service restarted, health status `200 OK`. |
| **4** | 22:45 | DevOps | Deploy Frontend Web portal phiên bản `v2.0.0` và xóa cache. | Giao diện đăng nhập mới hiển thị đúng, không bị cache CSS/JS. |

---

## 🚫 3. Kịch bản Khôi phục (Rollback Steps — Đề phòng sự cố)
> [!CAUTION]
> Kích hoạt kịch bản khôi phục ngay lập tức nếu thời gian downtime vượt quá 30% khung giờ deploy hoặc phát hiện lỗi nghiêm trọng không thể sửa nhanh (hotfix) trên Production.

1. **Khôi phục database:** Restore database từ bản backup tạo lúc 22:00 ngày 30/05/2026.
2. **Revert source code:** Revert commit code của cả Backend và Frontend về phiên bản ổn định cũ (`v1.9.5`).
3. **Deploy rollback:** Chạy deploy khôi phục phiên bản cũ lên Production.
4. **Kiểm tra nhanh:** Chạy nhanh Smoke Test phiên bản cũ để đảm bảo người dùng truy cập bình thường.

---

## 🏁 4. Biên bản Smoke Test trên Production (Prod Verification)
*Sẽ được thực hiện trực tiếp trên môi trường Production bởi QA ngay sau khi deploy xong lúc 22:50 ngày 30/05/2026.*

| Mã TC | Tiêu đề kịch bản nghiệm thu | Tài khoản / Data test Prod | Kết quả thực tế | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| **ST-OH-01** | Đăng nhập thành công bằng tài khoản thật trên Production | Tài khoản Prod thật được PO cấp | *Chưa thực hiện* | ⏳ |
| **ST-OH-02** | Validate báo lỗi "Required" khi để trống Username/Password | N/A | *Chưa thực hiện* | ⏳ |
| **ST-OH-03** | Đăng xuất thành công và chặn quay lại Dashboard bằng nút Back | Tài khoản Prod thật | *Chưa thực hiện* | ⏳ |

---

## 📅 Nhật ký cập nhật CR
| Thời gian | Trạng thái CR | Nội dung hoạt động | Người thực hiện |
| :--- | :--- | :--- | :--- |
| 2026-05-23 14:38:50 | Draft | Khởi tạo Biên bản CR Go-Live. | QA_Lead |
