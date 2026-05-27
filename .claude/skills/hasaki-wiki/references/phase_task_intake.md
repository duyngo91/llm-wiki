---
tags: [wiki-rules, reference]
status: Done
updated: 2026-05-24
---

# Phase: Task Intake — Hasaki Workplace

> Dùng bởi: `/get-my-tasks`, `/import-hasaki-task`, `/get-hasaki-task`, `/sync-my-open-tasks`.

---

## Phân loại task Hasaki

| Code | Vai trò | Xử lý |
|:-----|:--------|:------|
| `HSK-xxxxx` | Task cha: chứa requirement/implementation detail | Nguồn chính để phân tích Feature Spec |
| `TBB2-xxxxx` | Test request liên kết HSK cha qua `parent_id` | Trigger QA nhận việc test |

**Lưu raw:** `raw_sources/project_hasaki/tasks/HSK-xxxxx.md`. TBB2 embed vào `## Test Requests (TBB2)` bên trong — không tạo file TBB2 riêng. Wiki impact check và KANBAN card dùng HSK code.

---

## Workflow: /get-my-tasks

1. Script `hasaki_my_tasks.py` fetch tất cả tasks open được assign, tách HSK (cha) và TBB2 (test request).
2. Với mỗi TBB2: resolve HSK cha qua `parent_id`. Group: mỗi HSK kèm danh sách TBB2 liên kết.
3. Diff với raw files đã có trong `raw_sources/project_hasaki/tasks/`:
   - 🆕 **NEW** — task chưa có raw file
   - 🔄 **UPDATED** — `updated_at` thay đổi, kèm wiki impact analysis
   - ✅ **CURRENT** — không thay đổi
4. **🤝 HITL Gate:** Hiển thị kết quả, hỏi user xác nhận trước khi download.
5. Sau download: ghi log `[ingest]`.
   - **NEW task:** Tạo KANBAN card `## TODO` với HSK code. Sau đó dùng `/import-hasaki-task` hoặc `/wiki-requirement-analyzer`.
   - **UPDATED task có wiki impact:** Gợi ý chạy Workflow 2.2 (Task Change) với raw file mới — xem `phase_ingest.md`.
   - **Không tự cập nhật Feature Spec/Test Suite** — user phải chỉ định rõ và có Gate 1/2.

---

## Workflow: /import-hasaki-task HSK-XXXXX

1. Fetch chi tiết task HSK + TBB2 liên kết từ Hasaki Workplace API.
2. Lưu/cập nhật `raw_sources/project_hasaki/tasks/HSK-xxxxx.md` với đầy đủ thông tin + section `## Test Requests (TBB2)`.
3. Extract AC list từ task description.
4. Kiểm tra wiki impact: task đã có Feature Spec chưa?
   - Chưa có → gợi ý tạo KANBAN card + chạy `/wiki-requirement-analyzer`.
   - Đã có → báo wiki impact, gợi ý chạy Workflow 2.2 nếu có thay đổi.
5. Ghi log `[ingest]`.

---

## KANBAN card cho task mới (HSK)

```
- [ ] [[raw_sources/project_hasaki/tasks/HSK-xxxxx|HSK-xxxxx]] ➔ [[wiki/project_hasaki/test_suites/test_X|Test X]] [Priority]
```

Thêm vào `## TODO`. Chờ user confirm trước khi chạy `/wiki-requirement-analyzer`.

---

## Raw file status (phản ánh Hasaki Workplace)

| Frontmatter `status` | Nguồn |
|:---------------------|:------|
| `Todo` | API status = 0 |
| `Processing` | API status = 1 |
| `Done` | API status = 2 |

Raw file chỉ đọc từ góc nhìn wiki. Cập nhật qua script `hasaki_my_tasks.py`, không sửa tay.

## Task Spec Stub Rule (2026-05-27d)

- Sau reset, cho phép tạo `task_spec` dạng stub để giữ traceability ngay lập tức.
- Stub task_spec bắt buộc có tối thiểu:
  - `tbb2_code`, `hsk_parent`
  - link raw HSK source
  - link feature specs liên quan (nếu đã có)
  - trạng thái blocked rõ ràng nếu chưa đủ source
- Stub task_spec không được coi là hoàn tất workflow task intake.
- Trước khi đưa task vào execution-ready, phải refine task_spec thành bản đầy đủ theo rule no-inference.
