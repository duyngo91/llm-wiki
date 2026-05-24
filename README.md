# LLM Wiki (Hasaki)

Kho tri thuc QA/Test theo mo hinh Obsidian-first cho du an Hasaki.

## Active project
- `project_hasaki` la project active duy nhat.
- `project_demo` va `project_orange` da duoc loai khoi active scope.

## Claude Code style structure
- `.claude/commands/`: workflow commands.
- `.claude/skills/`: orchestrator skill cho project.
- `.claude/rules/`: machine-friendly governance rules.
- `.claude/research/`: playbook cho task can source verification.
- `.claude/team/`: team config mapping command/skill.
- `.claude/enterprise/`: governance controls.
- `.claude/manifests/`: identity/package/tool manifest.
- `.claude/scripts/`: executable logic for sync/task flows.

## AI Knowledge Scope
- Allowed: `wiki/`, `raw_sources/`, `templates/`, `.claude/commands/`, `.claude/scripts/`, va cac file control root.
- Excluded by default: `.obsidian/`, `.smart-env/`, `.karate_cache/`, cache/plugin/db files.
- Rule: AI khong duoc suy dien requirement/test case tu du lieu ngoai allowed scope.

## Core docs
- `.claude/skills/hasaki-wiki/references/wiki_rules.md`
- `USER_COMMANDS.md`
- `index.md`
- `KANBAN.md`
- `wiki/project_hasaki/project_registry.json`
- `wiki/project_hasaki/traceability.json`
