# QA LLM Wiki - Claude Instructions

Doc bat buoc: @WIKI_RULES.md

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
- Rules: `.claude/rules/*.md`
- Research: `.claude/research/hasaki-research-playbook.md`
- Team config: `.claude/team/hasaki-team-config.json`
- Enterprise controls: `.claude/enterprise/controls.md`
- Manifests: `.claude/manifests/*.json`

## Slash commands
- `/wiki-requirement-analyzer`
- `/wiki-test-designer`
- `/wiki-sync-helper`
- `/get-hasaki-task`
- `/import-hasaki-task`
- `/mcp-health-check`
