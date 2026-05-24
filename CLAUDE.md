# QA LLM Wiki — Claude Code Instructions

Đây là vault QA theo chuẩn ISTQB, vận hành bởi Claude Code với vai trò AI Co-pilot.

## Đọc bắt buộc trước mọi thao tác

@WIKI_RULES.md

## Điều hướng nhanh

- `index.md` — Bản đồ toàn bộ nội dung, đọc đầu tiên khi cần định vị file
- `KANBAN.md` — Trạng thái task hiện tại
- `log.md` — Audit trail, ghi mọi action vào đây

## Slash Commands có sẵn

- `/wiki-requirement-analyzer` — ISTQB Test Analysis: phân tích requirement → Feature Spec
- `/wiki-test-designer` — ISTQB Test Design: thiết kế test suite từ Spec đã duyệt
- `/wiki-sync-helper` — Sync Kanban, daily note, audit broken links
- `/get-hasaki-task` — Lấy task từ Hasaki Workplace
- `/import-hasaki-task` — Import task + extract AC list
- `/get-my-tasks` — Scan tất cả tasks được assign, phát hiện NEW/UPDATED, download raw files

## Projects đang hoạt động

| Project | Thư mục wiki | Raw sources |
|:--------|:-------------|:------------|
| Demo Email | `wiki/project_demo/` | `raw_sources/project_demo/` |
| OrangeHRM | `wiki/project_orange/` | `raw_sources/project_orange/` |
| Hasaki | `wiki/project_hasaki/` | `raw_sources/project_hasaki/` |

> Mỗi project có 4 subfolder: `tasks/` · `requirements/` · `issues/` · `assets/`
