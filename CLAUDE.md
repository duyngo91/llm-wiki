# QA LLM Wiki - Claude Instructions

## Active project
- Hasaki: `wiki/project_hasaki/`, `raw_sources/project_hasaki/`

## Rules chot
- Timezone mac dinh: `Asia/Saigon` (UTC+07:00).
- Markdown/JSON phai UTF-8, khong tao mojibake.
- Khong suy dien requirement, AC, API contract, test case.
- Neu thong tin chua ro: ghi vao Question, khong dua vao mo ta chinh.
- Test case chi duoc tao tu requirement/AC explicit da mo ta ro.
- Noi dung dua tren Open question phai nam o `Blocked Coverage`.
- AI chi doc knowledge trong allowed scope, bo qua cache/plugin by default.

## Claude structure map
- Skill: `.claude/skills/hasaki-wiki/SKILL.md`
- Skill search: `.claude/skills/obsidian-search/SKILL.md`
- Rules: `.claude/rules/*.md`
- Research: `.claude/research/hasaki-research-playbook.md`
- Team config: `.claude/team/hasaki-team-config.json`
- Enterprise controls: `.claude/enterprise/controls.md`
- Manifests: `.claude/manifests/*.json`

## Slash commands
- `/wiki-requirement-analyzer` — phân tích requirement → Feature Spec
- `/wiki-test-designer` — thiết kế test suite từ Spec đã duyệt
- `/wiki-sync-helper` — daily sync, lint, Kanban, verify
- `/get-hasaki-task` — lấy thông tin task Hasaki (xem)
- `/import-hasaki-task` — import task + extract AC list vào vault
- `/get-my-tasks` — scan tất cả tasks được assign, phát hiện NEW/UPDATED
- `/sync-my-open-tasks` — sync open tasks từ Hasaki Workplace
- `/mcp-health-check` — kiểm tra MCP health
- `/obsidian-search` — tìm kiếm note trong vault (Omnisearch MCP → HTTP API → Grep)
