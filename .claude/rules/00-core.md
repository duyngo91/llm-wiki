# Core Rules

- Project active: `project_hasaki`.
- Timezone standard: `Asia/Saigon` (`UTC+07:00`).
- Markdown/JSON/YAML must be UTF-8 không BOM. Nội dung gen ra viết Tiếng Việt có dấu (xem `05-language-and-encoding.md`).
- Do not trust memory over live files; files on disk are source of truth.
- Update propagation is mandatory when requirement/test scope changes.
- Secret: không commit token/cookie/API key/password. Phát hiện → dừng, báo user rotate & clean history.
- Rule precedence:
  - `.claude/rules/*.md` are normative policy.
  - `USER_COMMANDS.md` is user-facing usage guide.
  - `.claude/skills/hasaki-wiki/references/phase_*.md` are phase-specific process references and must not contradict `.claude/rules`.
