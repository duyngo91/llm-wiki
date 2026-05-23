---
description: "Bảo trì wiki: daily note sync, Kanban sync, tính test coverage, audit broken links, quản lý release/go-live qua .claude/scripts/wiki_sync.py"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Wiki Sync Helper

Dùng cho **bảo trì wiki xác định** (deterministic maintenance). Ưu tiên chạy script thay vì sửa markdown thủ công khi có lệnh script hỗ trợ.

Logic sync/audit dùng chung nằm tại `.claude/scripts/wiki_sync_core.py`. Script entrypoint là `.claude/scripts/wiki_sync.py`.

## Các lệnh chạy từ vault root

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

## Workflow bắt buộc

1. Đọc `WIKI_RULES.md` và các file liên quan (`KANBAN.md`, `log.md`, daily note hoặc test suite đích).
2. Tuân thủ nguyên tắc **Scan Live trước**: đọc file trực tiếp từ đĩa, không dựa vào ngữ cảnh hội thoại cũ.
3. Chạy lệnh phù hợp từ vault root.
4. Báo cáo kết quả lệnh, file bị ảnh hưởng, và lỗi audit chưa giải quyết.

## Guardrails

- **KHÔNG đánh Pass test case** nếu người dùng chưa xác nhận chạy test thực tế (HITL Gate 4).
- **KHÔNG tự di chuyển task sang Done** trên Kanban mà không có bằng chứng thực thi.
- Khi daily sync tạo Bug RCA mới → phải thông báo cho QA Lead & Tech Lead để thực hiện Bug Triage (Gate 3).
- Mọi thay đổi phải được ghi vào `log.md` với đúng prefix action-type.

## Output tóm tắt

Sau khi hoàn thành, báo cáo:
- Lệnh đã chạy
- Tasks đã di chuyển hoặc suites đã cập nhật
- Bugs đã tạo hoặc đã link
- Kết quả audit từ `verify_wiki.py`
- Human gate tiếp theo (nếu có)
