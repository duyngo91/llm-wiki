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

## Claude structure map (5 layer — mỗi nội dung 1 nhà, không duplicate)
- **Policy (SSOT chuẩn):** `.claude/rules/*.md` — no-inference, encoding, timezone, SSOT, testcase, secret. Mọi nơi khác chỉ tham chiếu.
- **Shared domain knowledge:** `.claude/skills/hasaki-wiki/references/shared.md` — naming, tags, status, gates, traceability, field-ownership, source-ref, scripts.
- **Playbook (main session):** `.claude/skills/hasaki-wiki/SKILL.md` (SDLC pipeline) + `.claude/skills/hasaki-spec-verifier/SKILL.md` (verify 3 tầng). Chỉ chuỗi + gate + bản đồ phase→agent.
- **Worker (1 nhà cho workflow chi tiết mỗi phase):** `.claude/agents/hasaki-*.md` (thin, gán model riêng) + `references/phase_*.md` (chi tiết). 7 agent: ingest(opus), test-design(sonnet), task-intake(haiku), sync(haiku), golive(sonnet), verify-structural(haiku), verify-inference(opus).
- **Entry point (thin router):** `.claude/commands/*.md` — delegate sang `@hasaki-<phase>` đúng model.
- Skill search: `.claude/skills/obsidian-search/SKILL.md` · Research: `.claude/research/hasaki-research-playbook.md` · Team config: `.claude/team/hasaki-team-config.json` · Enterprise: `.claude/enterprise/controls.md` · Manifests: `.claude/manifests/*.json`

> Pipeline tuần tự + HITL gate → dùng **subagents** (đúng chuẩn Claude), KHÔNG dùng agent-teams. Route dựa trên auto-delegation theo `description` của agent.

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
