# Core Rules

- Project active: `project_hasaki`.
- Timezone standard: `Asia/Saigon` (`UTC+07:00`).
- Markdown/JSON/YAML must be UTF-8.
- Do not trust memory over live files; files on disk are source of truth.
- Update propagation is mandatory when requirement/test scope changes.
- Rule precedence:
  - `.claude/rules/*.md` are normative policy.
  - `USER_COMMANDS.md` is user-facing usage guide.
  - `.claude/skills/hasaki-wiki/references/wiki_rules.md` is detailed process reference and must not contradict `.claude/rules`.
