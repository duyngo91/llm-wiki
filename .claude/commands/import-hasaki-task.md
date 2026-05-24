---
description: "Import task từ Hasaki Workplace: fetch, extract AC list, lưu vào raw_sources/project_hasaki/tasks/ và cập nhật KANBAN"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Skill: Import Hasaki Task

Fetch task từ Hasaki Workplace, extract AC/API information tường minh, lưu vào `raw_sources/project_hasaki/tasks/`. Output là raw source — bước tiếp theo là `/wiki-requirement-analyzer` để tạo Feature Spec và API Spec nếu task có API/interface explicit.

## Trigger

- `/import-hasaki-task HSK-40187ZYO`
- `import task HSK-40187ZYO`
- `tôi cần test task HSK-XXXXX`
- `phân tích task [URL hoặc code]`

---

## Các bước thực hiện

### Bước 1 — Fetch task data

```powershell
$env:PYTHONUTF8 = "1"
python ".claude/scripts/hasaki_task.py" <INPUT> --json --images --output "raw_sources/project_hasaki/assets"
```

Nếu token hết hạn → dừng và hướng dẫn:
> "Token đã hết hạn. Đăng nhập work.hasaki.vn → F12 → Application → Cookies → `wshr-token` → paste vào `token.txt`"

Từ JSON output, extract:
- `task.code`, `task.name`, `task.note`, `task.note_files`
- `task.status`, `task.piority`, `task.date_end`, `task.created_at`
- `task.prid` → project name
- `task.milestone.name`
- `task.created_by_user` → assigner
- `task.assign_to_user[]` → assignees
- `task.data.subtasks[]`
- `downloaded_images[]`

---

### Bước 2 — Xác định Feature Spec liên quan

Dùng `Grep` tìm trong `wiki/project_hasaki/features/` theo keyword từ task name và nội dung. Đề xuất candidates:

> "Tôi tìm thấy Feature Spec có thể liên quan:
> 1. `wiki/project_hasaki/features/xxx.md` — mention '...'
> 2. `wiki/project_hasaki/features/yyy.md` — mention '...'
>
> Bạn confirm cái nào?"

**Đợi user confirm** trước khi tiếp tục. Nếu chưa có Feature Spec nào → thông báo, gợi ý chạy `/wiki-requirement-analyzer` trước.

---

### Bước 3 — Đọc Feature Spec đã confirm

Dùng `Read` đọc toàn bộ Feature Spec được confirm.

---

### Bước 4 — Extract AC List

#### 4a. AC Tường minh (từ task.note)

Trích từng hành vi hệ thống được BA ghi tường minh:
- Quote nguyên văn đoạn nguồn vào cột **Nguồn**
- Status: `✅ Confirmed`

Nếu `task.note` trống → ghi rõ "Không có AC tường minh".

#### 4b. Điểm chưa rõ / thiếu thông tin

Không tạo AC suy diễn.

Nếu có behavior tiềm năng nhưng task chưa mô tả rõ:
- Không ghi thành AC.
- Đưa vào phần câu hỏi làm rõ ở bước 4c.
- Chờ BA/PO/Dev xác nhận rồi mới cập nhật AC chính thức.

#### 4c. Sinh Questions cho điểm chưa rõ

Với mỗi điểm chưa rõ → tạo câu hỏi:
- Gán `Q-ID` ổn định (`Q-001`, `Q-002`...)
- Link tới AC/Requirement liên quan nếu có
- Format: "Khi [điều kiện], hệ thống cần xử lý như thế nào?"
- Câu hỏi kỹ thuật → gắn nhãn Dev Question
- Status mặc định: `Open`; không được sinh AC/test case từ question này cho tới khi có câu trả lời chính thức.

#### 4e. API / Interface explicit nếu có

Nếu task note có mô tả API rõ ràng:
- Ghi method, endpoint, payload, response/status/error đúng theo task note.
- Không tự đoán endpoint/status/payload theo convention REST.
- Nếu API behavior có nhắc nhưng thiếu contract, đưa vào Questions để `/wiki-requirement-analyzer` tạo hoặc cập nhật API Spec sau khi có câu trả lời.

#### 4d. Trình bày và chờ confirm

> "AC List đã extract:
> - **Tường minh (✅):** [N]
> - **Chưa rõ (❓):** [M] — cần BA/PO/Dev confirm
>
> Bạn có muốn thêm/bỏ AC nào không?"

**Đợi user confirm.**

---

### Bước 5 — Lưu Task Note vào vault

**Đường dẫn:** `raw_sources/project_hasaki/tasks/<task-code>.md`

**Nội dung file:**

```markdown
---
tags: [hasaki-task, raw-source]
task-code: <task.code>
task-id: <task.id>
task-name: <task.name>
project: project_hasaki
milestone: <task.milestone.name>
status: <task.status>
priority: <task.piority>
deadline: <task.date_end>
imported-date: <YYYY-MM-DD>
qa-status: <Ready for Analysis | Questions Open>
related-features: []
---

## Task Data (read-only — nguyên văn từ Hasaki)

[metadata + task.note nguyên văn + subtasks + links ảnh]

## AC List

| AC ID | Mô tả | Nguồn | Status |
|-------|-------|-------|--------|
| AC-01 | ... | Explicit từ task.note | ✅ Confirmed |
| AC-02 | ... | Feature-Spec [mục] | ❓ Cần làm rõ |

## Questions

| Q-ID | Liên kết AC/R | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|------|---------------|---------|--------|------------|-------------|---------------|--------------|
| Q-001 | AC-02 | Khi ..., hệ thống cần xử lý như thế nào? | BA/PO | Open | | | |
| Q-002 | | ... | Dev | Open | | | |

## QA Notes

Rủi ro, dependencies, edge case cần lưu ý.

## API / Interface Notes

Chỉ ghi API/interface explicit từ task.note/subtasks. Nếu chưa rõ, link tới Questions.
```

Dùng `Write` để lưu file.

---

### Bước 6 — Cập nhật KANBAN và log

Thêm thẻ vào cột `## TODO` trong `KANBAN.md`:
```
- [ ] [[raw_sources/project_hasaki/tasks/<task-code>|<task-code>]] ➔ [[wiki/project_hasaki/test_suites/test_<feature>|Test Suite <Feature>]] [High]
```

Ghi `log.md` với prefix `[ingest]`:
```
- [YYYY-MM-DD HH:mm:ss] [ingest] | Import task <task-code>: <task.name>. AC: X confirmed, Y questions open.
```

---

### Bước 7 — Hỏi bước tiếp theo

> "Đã lưu task note tại `raw_sources/project_hasaki/tasks/<task-code>.md`.
>
> **QA Status: [trạng thái]**
>
> Bước tiếp theo:
> - **Nếu còn Questions Open**: Gửi câu hỏi cho BA/PO/Dev, cập nhật Task Note khi có trả lời
> - **Nếu tất cả AC Confirmed**: `/wiki-requirement-analyzer` để tạo/cập nhật Feature Spec từ task này"

---

## Guardrails

- **Không tự tạo AC suy diễn** — điểm chưa rõ phải đưa vào Questions để xác nhận
- **Không tự tạo API contract suy diễn** — endpoint/method/payload/status/error chưa rõ phải đưa vào Questions
- **Không sinh test case từ question Open** — sau khi question được trả lời, cập nhật Task Note/Feature Spec trước rồi mới thiết kế test case
- **Không tự quyết định Feature Spec** khi ambiguous — hỏi user (Bước 2)
- Section Task Data là **read-only** — không chỉnh sửa `task.note` nguyên văn
- Ảnh download vào `raw_sources/project_hasaki/assets/`

## Xử lý lỗi

| Tình huống | Xử lý |
|-----------|-------|
| Token hết hạn | Hướng dẫn lấy token mới, dừng |
| Task không tìm thấy | Thử numeric ID; nếu vẫn không có → báo user |
| task.note trống | Ghi rõ "Không có AC tường minh"; qa-status = Questions Open |
| Chưa có Feature Spec | Thông báo, gợi ý `/wiki-requirement-analyzer` trước |
| Task đã import rồi | Hỏi: cập nhật hay bỏ qua? |
