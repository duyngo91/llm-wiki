---
aliases: [Mã-CR Go-Live, Release-vX.Y.Z]
tags: [qa/release]
status: Draft       # Draft | Testing | Done
cr_id: CR-xxx
golive_date: {{date:YYYY-MM-DD}}
deploy_window: 22:00 - 23:00
approver: PO_Name
project: 
---

# 🚀 CHANGE REQUEST: {{title}}

> **Biên bản Go-Live (Deployment Hub):** Quản lý kỹ thuật và nghiệm thu thực tế trên môi trường Production cho đợt Change Request (CR) này.

---

## 📋 1. Phạm vi & Sự chuẩn bị (Prerequisites)
- **Kế hoạch kiểm thử Staging đã đạt Exit Criteria:** [[wiki/project_name/test_plans/testplan_xxx|Test Plan Staging]] (Trạng thái: `Passed` / `Done`).
- **Mã Jira/Specs liên quan:**
  - [[wiki/project_name/features/feature_name|Feature Specs]] — Trạng thái: `Done`.
  - [[wiki/project_name/test_suites/test_xxx|Test Suite]] — Trạng thái: `Passed`.

---

## 🚀 2. Kịch bản Triển khai từng bước (Deploy Steps)

*QA phối hợp với Dev/DevOps điền thông tin này khi Specs đã đạt trạng thái Passed trên Staging và được duyệt deploy.*

| Bước | Thời gian | Người thực hiện | Hành động chi tiết | Kết quả mong đợi |
| :--- | :--- | :--- | :--- | :--- |
| **1** | 22:00 | DevOps | Backup Database Production hiện tại. | Backup thành công, lưu file an toàn. |
| **2** | 22:15 | Dev Backend | Chạy SQL Script Migration (cập nhật DB). | DB cập nhật không lỗi schema. |
| **3** | 22:30 | DevOps | Deploy Backend API (Docker/CI-CD). | API khởi chạy thành công, status `200 OK`. |
| **4** | 22:45 | DevOps | Deploy Frontend Web/App. | Giao diện mới hiển thị, không lỗi caching. |

---

## 🚫 3. Kịch bản Khôi phục (Rollback Steps — Đề phòng sự cố)
> [!CAUTION]
> Kích hoạt kịch bản khôi phục ngay lập tức nếu thời gian downtime vượt quá 30 phút hoặc phát hiện lỗi nghiêm trọng không thể sửa nhanh (hotfix) trên Production.

1. **Khôi phục database:** Restore database từ bản backup tạo lúc 22:00.
2. **Revert source code:** Revert commit code trên Git của cả Backend và Frontend về tag ổn định gần nhất (`vX.Y.Z_stable`).
3. **Deploy rollback:** Trigger CI/CD deploy lại phiên bản cũ lên Production.
4. **Kiểm tra nhanh:** Chạy Smoke Test bản cũ để đảm bảo hệ thống hoạt động bình thường trở lại.

---

## 🏁 4. Biên bản Smoke Test trên Production (Prod Verification)
*Thực hiện ngay sau khi kết thúc Deploy Steps. QA chạy thử trực tiếp trên môi trường Production bằng tài khoản thật.*

| Mã TC | Tiêu đề kịch bản nghiệm thu | Tài khoản / Data test Prod | Kết quả thực tế | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| **ST-01** | ... | ... | ... | ⏳ |
| **ST-02** | ... | ... | ... | ⏳ |

---

## 📅 Nhật ký cập nhật CR
| Thời gian | Trạng thái CR | Nội dung hoạt động | Người thực hiện |
| :--- | :--- | :--- | :--- |
| {{date:YYYY-MM-DD HH:mm:ss}} | Draft | Khởi tạo Biên bản CR Go-Live. | QA_Lead |
