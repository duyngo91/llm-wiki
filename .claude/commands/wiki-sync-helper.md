---
description: "Bảo trì wiki: daily note sync, Kanban sync, tính test coverage, audit broken links, quản lý release/go-live qua .claude/scripts/wiki_sync.py"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Wiki Sync Helper

Dùng cho **bảo trì wiki xác định** (deterministic maintenance). Ưu tiên chạy script thay vì sửa markdown thủ công khi có lệnh script hỗ trợ.

Logic sync/audit dùng chung nằm tại `.claude/scripts/wiki_sync_core.py`. Script entrypoint là `.claude/scripts/wiki_sync.py`.

## Các lệnh chạy từ vault root

**User command mapping:**
- Khi người dùng nói `lint và sync toàn bộ wiki`, mặc định chạy audit-only bằng `python .claude/scripts/wiki_sync.py verify` nếu chưa có xác nhận Gate 4.
- Chỉ chạy `python .claude/scripts/wiki_sync.py sync` khi người dùng đã xác nhận test thực tế đã hoàn tất/pass và cho phép đồng bộ trạng thái `Done/Passed`.

**Daily note sync:**
```powershell
python .claude/scripts/wiki_sync.py daily-sync --project <project_name> --date <YYYY-MM-DD>
```

**Kanban + coverage sync:**
```powershell
python .claude/scripts/wiki_sync.py sync
```

**Audit only:**
```powershell
python .claude/scripts/wiki_sync.py verify
```

**Repair + Verify (recommended when gặp lỗi BOM/TC count drift):**
```powershell
python .claude/scripts/wiki_sync.py repair
```

## Workflow bắt buộc

1. Đọc `.claude/skills/hasaki-wiki/references/phase_sync.md`, sau đó đọc các file liên quan (`KANBAN.md`, `log.md`, daily note hoặc test suite đích).
2. Tuân thủ nguyên tắc **Scan Live trước**: đọc file trực tiếp từ đĩa, không dựa vào ngữ cảnh hội thoại cũ.
3. Với yêu cầu lint chung, chạy `verify` trước. Chỉ chạy `sync` nếu có xác nhận Gate 4 rõ ràng.
4. Báo cáo kết quả lệnh, file bị ảnh hưởng, và lỗi audit chưa giải quyết.

## Guardrails

- **KHÔNG đánh Pass test case** nếu người dùng chưa xác nhận chạy test thực tế (HITL Gate 4).
- **KHÔNG tự di chuyển task sang Done** trên Kanban mà không có bằng chứng thực thi.
- Khi daily sync tạo Bug RCA mới → phải thông báo cho QA Lead & Tech Lead để thực hiện Bug Triage (Gate 3).
- Verify phải báo lỗi nếu Test Suite thiếu cột `Phạm vi`, có nguồn không explicit, có `AI-Inferred`/`suy diễn`, hoặc TC cover Requirement/AC/API đang có question `Open`.
- Verify phải báo lỗi nếu Kanban ghi số TC khác số TC thực tế trong test suite.
- Verify phải báo lỗi nếu Feature/Test Suite thiếu `Changelog` hoặc Test Suite thiếu `Blocked Coverage`/`Regression Impact` theo template mới.
- Verify phải chấp nhận scope API (`API`, `API+Functional`, `UI+API`, `E2E`) nhưng API TC vẫn phải có nguồn explicit từ API Spec/Feature Spec và không được cover API/R/AC còn question `Open`.
- Verify phải báo lỗi nếu API Spec thiếu `qa/api-spec`, thiếu `Changelog`, sai status hoặc thiếu Feature Group page khi có tag `qa/feature-group/...`.
- Verify phải báo lỗi nếu API Spec thiếu các section contract bắt buộc hoặc API test case/suite không link được API Spec.
- Verify phải báo lỗi nếu có tag `qa/feature-group/...` nhưng thiếu group page tương ứng trong `wiki/[project]/feature_groups/`.
- Verify phải báo lỗi nếu phát hiện dấu hiệu mojibake/lỗi font trong Markdown.
- Tất cả timestamp khi sync/log/changelog phải dùng `UTC+07:00` (`Asia/Ho_Chi_Minh`).
- Mọi file markdown phải ghi `UTF-8`; khi chạy Python trên Windows phải set:
  - `$env:PYTHONUTF8 = "1"`
  - `$env:PYTHONIOENCODING = "utf-8"`
- Nếu thấy dấu hiệu lỗi font, dừng sync và sửa encoding trước khi chạy tiếp.
- Mọi thay đổi phải được ghi vào `log.md` với đúng prefix action-type.

## Output tóm tắt

Sau khi hoàn thành, báo cáo:
- Lệnh đã chạy
- Tasks đã di chuyển hoặc suites đã cập nhật
- Bugs đã tạo hoặc đã link
- Kết quả audit từ `python .claude/scripts/wiki_sync.py verify`
- Human gate tiếp theo (nếu có)

## Batch Open Tasks

For Hasaki open-task orchestration, use:
python .claude/scripts/wiki_sync.py sync-my-open-tasks --limit 20 --dry-run`r
python .claude/scripts/wiki_sync.py sync-my-open-tasks --limit 20 --images

