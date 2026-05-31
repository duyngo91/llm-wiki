---
tags: [wiki-rules, reference]
status: Done
updated: 2026-05-31
---

# Phase: Task Intake — Hasaki Workplace

> Single source of truth cho 4 entry point: `/get-hasaki-task`, `/import-hasaki-task`, `/get-my-tasks`, `/sync-my-open-tasks`.
> Các command này là **thin router** delegate sang `@hasaki-task-intake` (model haiku) — toàn bộ runbook nằm ở file này.
> Phân loại HSK/TBB2, raw file status, naming: [`shared.md`](shared.md). No-inference + encoding: `.claude/rules/`.

---

## Token (chung cho mọi workflow)

Token lưu tại `token.txt` (root vault). Hết hạn (exit code 2 / `401 Unauthorized`, >48h) → **dừng** và hướng dẫn:

> "Token đã hết hạn. Vui lòng:
> 1. Đăng nhập lại tại work.hasaki.vn
> 2. F12 → Application → Cookies → work.hasaki.vn
> 3. Copy giá trị cookie `wshr-token`
> 4. Paste vào `token.txt` (xoá nội dung cũ)"

Windows: luôn set `$env:PYTHONUTF8 = "1"; $env:PYTHONIOENCODING = "utf-8"` trước khi chạy script.

---

## Workflow A — `/get-hasaki-task` (lookup-only)

Tra cứu 1 task để **hiển thị**, không lưu markdown vào vault. Dùng `--images` mới tải ảnh về `raw_sources/project_hasaki/assets/`.

**Input:** task code (`HSK-40187ZYO`), numeric ID (`12032444`), hoặc URL (`https://work.hasaki.vn/tasks?...&task_id=...`).

```powershell
$env:PYTHONUTF8 = "1"
python ".claude/scripts/hasaki_task.py" <TASK_CODE_OR_ID>            # hiển thị
python ".claude/scripts/hasaki_task.py" <TASK_CODE_OR_ID> --json     # JSON để xử lý tiếp
python ".claude/scripts/hasaki_task.py" <TASK_CODE_OR_ID> --images --output "raw_sources/project_hasaki/assets"
```

Hiển thị output trực tiếp. Nếu user muốn phân tích + lưu đầy đủ → gợi ý `/import-hasaki-task`. Câu nói tự nhiên `get my task HSK-XXXXX` map vào chế độ tra cứu này.

---

## Workflow B — `/import-hasaki-task HSK-XXXXX` (fetch + extract AC + lưu raw)

Output là raw source trong `raw_sources/project_hasaki/tasks/`. Bước tiếp theo là `@hasaki-ingest` để tạo Feature Spec.

### Bước 1 — Fetch task data

```powershell
$env:PYTHONUTF8 = "1"
python ".claude/scripts/hasaki_task.py" <INPUT> --json --images --output "raw_sources/project_hasaki/assets"
```

Từ JSON, extract: `task.code`, `task.name`, `task.note`, `task.note_files`, `task.status`, `task.piority`, `task.date_end`, `task.created_at`, `task.prid` (project), `task.milestone.name`, `task.created_by_user` (assigner), `task.assign_to_user[]`, `task.data.subtasks[]`, `downloaded_images[]`.

### Bước 2 — Xác định Feature Spec liên quan

`Grep` trong `wiki/project_hasaki/features/` theo keyword từ task name. Đề xuất candidates, **đợi user confirm** trước khi tiếp. Chưa có Feature Spec nào → gợi ý chạy `@hasaki-ingest` (`/wiki-requirement-analyzer`) trước.

### Bước 3 — Đọc Feature Spec đã confirm (toàn bộ).

### Bước 4 — Extract AC List

**4a. AC tường minh** (từ `task.note`): trích từng hành vi hệ thống BA ghi rõ; quote nguyên văn vào cột **Nguồn**; status `✅ Confirmed`. `task.note` trống → ghi rõ "Không có AC tường minh".

**4b. Điểm chưa rõ:** KHÔNG tạo AC suy diễn. Behavior tiềm năng nhưng chưa rõ → đưa vào Questions (4c), chờ BA/PO/Dev xác nhận.

**4c. Sinh Questions:** mỗi điểm chưa rõ → `Q-ID` ổn định (`Q-001`...), link AC/R liên quan, format "Khi [điều kiện], hệ thống cần xử lý như thế nào?", câu hỏi kỹ thuật gắn nhãn Dev. Status mặc định `Open` — không sinh AC/test case từ question này tới khi `Answered`.

**4e. API/Interface explicit:** nếu task note mô tả API rõ → ghi method/endpoint/payload/response/status/error đúng task note. Không đoán theo convention REST. API nhắc nhưng thiếu contract → đưa vào Questions.

**4d. Trình bày + đợi confirm:**

> "AC List đã extract: Tường minh (✅): [N] · Chưa rõ (❓): [M] — cần BA/PO/Dev confirm. Bạn có muốn thêm/bỏ AC nào không?"

### Bước 5 — Lưu Task Note vào vault

**Đường dẫn:** `raw_sources/project_hasaki/tasks/<task-code>.md`. Dùng `Write`.

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

## QA Notes

Rủi ro, dependencies, edge case cần lưu ý.

## API / Interface Notes

Chỉ ghi API/interface explicit từ task.note/subtasks. Chưa rõ → link tới Questions.
```

Section **Task Data là read-only** — không chỉnh `task.note` nguyên văn. Ảnh tải vào `raw_sources/project_hasaki/assets/`.

### Bước 6 — KANBAN + log

Thêm card `## TODO`:
```
- [ ] [[raw_sources/project_hasaki/tasks/<task-code>|<task-code>]] ➔ [[wiki/project_hasaki/test_suites/test_<feature>|Test Suite <Feature>]] [High]
```
Ghi `log.md` prefix `[ingest]`: `- [YYYY-MM-DD HH:mm:ss] [ingest] | Import task <task-code>: <task.name>. AC: X confirmed, Y questions open.`

### Bước 7 — Hỏi bước tiếp

> "Đã lưu task note. QA Status: [trạng thái]. Còn Questions Open → gửi BA/PO/Dev. Tất cả AC Confirmed → `@hasaki-ingest` để tạo/cập nhật Feature Spec."

---

## Workflow C — `/get-my-tasks` (scan + diff + download)

**Không tự cập nhật Feature/API Spec/Test Suite** — chỉ cập nhật `raw_sources/`. Wiki update cần HITL Gate 1/2.

### Bước 1 — Scan + Diff (dry-run)

```powershell
$env:PYTHONUTF8 = "1"; $env:PYTHONIOENCODING = "utf-8"
python ".claude/scripts/hasaki_my_tasks.py"                 # full
python ".claude/scripts/hasaki_my_tasks.py" --check-updates # tóm tắt nhanh
python ".claude/scripts/hasaki_my_tasks.py" --status all     # kể cả Done
python ".claude/scripts/hasaki_my_tasks.py" --json           # JSON
```

Script fetch tasks open được assign, tách HSK (cha) / TBB2 (test request); với mỗi TBB2 resolve HSK cha qua `parent_id`; diff với `raw_sources/project_hasaki/tasks/`.

### Bước 2 — Hiển thị theo 4 nhóm (group theo HSK cha, TBB2 là sub-item)

- **🆕 NEW** — HSK chưa có raw file.
- **🔄 UPDATED** — `updated_at` thay đổi, kèm **wiki impact** (file Feature Spec/Test Suite reference HSK code này).
- **✅ CURRENT** — không thay đổi.
- **⚠️ ORPHAN TBB2** — TBB2 không resolve được HSK parent.

### Bước 3 — HITL Gate: hỏi user

> "Bạn muốn download task nào? `all` (NEW + UPDATED) · `[HSK-XXXXX]` (cụ thể) · `skip`. ⚠️ Download chỉ cập nhật `raw_sources/`. Cập nhật Feature Spec/Test Suite cần `@hasaki-ingest` SAU KHI PO/QA Lead duyệt (Gate 1/2)."

**Đợi user xác nhận** trước khi download.

### Bước 4 — Download

```powershell
$env:PYTHONUTF8 = "1"; $env:PYTHONIOENCODING = "utf-8"
python ".claude/scripts/hasaki_my_tasks.py" --download                # all new + updated
python ".claude/scripts/hasaki_my_tasks.py" --download HSK-40187ZYO   # cụ thể
```

### Bước 5 — Báo cáo + hỏi bước tiếp + log

Liệt kê file đã lưu. Ghi `log.md`: `- [YYYY-MM-DD HH:mm:ss] [ingest] | get-my-tasks: download X tasks (Y new, Z updated). Files: [codes]`.
- **NEW** → tạo KANBAN card `## TODO`, rồi `@hasaki-task-intake` (import) hoặc `@hasaki-ingest`.
- **UPDATED có wiki impact** → gợi ý Workflow 2.2 (Task Change) ở `phase_ingest.md`. **Không tự cập nhật Spec** — chờ Gate 1/2.

---

## Workflow D — `/sync-my-open-tasks` (batch)

Đồng bộ hàng loạt open tasks + propagate raw/task-spec/traceability.

```powershell
$env:PYTHONUTF8 = "1"; $env:PYTHONIOENCODING = "utf-8"
python .claude/scripts/wiki_sync.py sync-my-open-tasks --limit 20 --dry-run   # preview
python .claude/scripts/wiki_sync.py sync-my-open-tasks --limit 20 --images    # apply
```

Behavior:
- Fetch `my-task` status `_00_01` (Todo/Processing).
- Resolve `TBB2 ↔ HSK` khi có thể.
- Append raw snapshot vào `raw_sources/project_hasaki/tasks/<TASK_CODE>.md`.
- Upsert task spec cho mỗi `TBB2` dưới `wiki/project_hasaki/task_specs/`.
- Update link machine-readable trong `traceability.json` + `project_registry.json`.
- Thêm Kanban TODO card cho mỗi `TBB2` còn thiếu.
- No-inference: behavior chưa rõ → Questions/Blocked Coverage.

---

## Error handling (chung)

| Tình huống | Xử lý |
|-----------|-------|
| Token hết hạn (exit 2 / 401) | Hướng dẫn lấy token mới, **dừng** |
| Task không tìm thấy | Thử numeric ID trực tiếp; vẫn không có → báo user |
| `task.note` trống | Ghi "Không có AC tường minh"; qa-status = Questions Open |
| Không có task open | Thông báo "Không có task open nào được assign" |
| Wiki dir không tồn tại | Impact check trả rỗng — thông báo không tìm được reference |
| Task đã import rồi | Hỏi: cập nhật hay bỏ qua? |
| `UnicodeEncodeError` | Set `$env:PYTHONUTF8 = "1"; $env:PYTHONIOENCODING = "utf-8"` |

---

## KANBAN card cho task mới (HSK)

```
- [ ] [[raw_sources/project_hasaki/tasks/HSK-xxxxx|HSK-xxxxx]] ➔ [[wiki/project_hasaki/test_suites/test_X|Test X]] [Priority]
```

Thêm vào `## TODO`. Chờ user confirm trước khi chạy `@hasaki-ingest`.

---

## Guardrails (phase-specific)

- **KHÔNG tự cập nhật Feature/API Spec, Test Suite** — chỉ `raw_sources/`. Wiki update cần Gate 1/2.
- **KHÔNG tự chạy ingest** sau download — đợi user yêu cầu.
- **KHÔNG tạo AC/API contract suy diễn** — điểm chưa rõ → Questions.
- **Raw file lưu theo HSK code** (`HSK-xxxxx.md`); TBB2 embed vào `## Test Requests (TBB2)` — không tạo file riêng cho TBB2. Wiki impact check theo HSK code, không phải TBB2.
- **KHÔNG xóa raw file cũ** khi download bản mới — ghi đè là đủ.
- Mọi download/import ghi `log.md` prefix `[ingest]`.

---

## Task Spec stub

Khi task chưa đủ source để viết task_spec đầy đủ, cho phép tạo stub giữ traceability ngay. Stub tối thiểu: `tbb2_code`, `hsk_parent`, link raw HSK source, link feature specs liên quan (nếu có), trạng thái blocked rõ ràng. Stub task_spec là `trace-ready`, **không** hoàn tất workflow task intake — trước khi execution-ready phải refine đầy đủ theo no-inference.
