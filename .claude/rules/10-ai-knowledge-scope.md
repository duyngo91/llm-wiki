# AI Knowledge Scope

## Allowed Scope
- `wiki/`
- `raw_sources/`
- `templates/`
- `.claude/commands/`
- `.claude/scripts/`
- Root control docs (`WIKI_RULES.md`, `USER_COMMANDS.md`, `KANBAN.md`, `index.md`, `log.md`, `README.md`, `CLAUDE.md`)

## Excluded By Default
- `.obsidian/`
- `.smart-env/`
- `.karate_cache/`
- `.git/`
- `__pycache__/`
- plugin/cache/runtime/database files (`*.sqlite`, `*.sqlite-shm`, `*.sqlite-wal`)

## Policy
- Do not infer requirement/test behavior from excluded scope.
- Use excluded scope only when task explicitly targets tool/config troubleshooting.
