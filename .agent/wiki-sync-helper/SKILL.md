---
name: wiki-sync-helper
description: Use this skill when running QA LLM Wiki maintenance commands: daily note sync, Kanban sync, test coverage recalculation, task Done synchronization, broken-link audits, status validation, or release/go-live housekeeping through scripts/wiki_manager.py and scripts/verify_wiki.py.
metadata:
  short-description: Sync and audit the wiki vault
---

# Wiki Sync Helper

Use for deterministic wiki maintenance. Prefer scripts over manual markdown edits when a supported command exists.

## Commands

Run from the vault root.

Daily note sync:
```powershell
python scripts/wiki_manager.py daily-sync --project <project_name> --date <YYYY-MM-DD>
```

Kanban + coverage sync:
```powershell
python scripts/wiki_manager.py sync
```

Audit only:
```powershell
python scripts/verify_wiki.py
```

## Workflow

1. Read `../../WIKI_RULES.md` and the relevant files (`../../KANBAN.md`, `../../log.md`, target daily note or test suite).
2. Run the appropriate command from the vault root.
3. Report the command outcome, files affected, and any unresolved audit errors.
4. Do not mark tests as passed unless the user has confirmed real execution results.

## Output

Summarize:
- command run;
- tasks moved or suites updated;
- bugs created or linked;
- audit result from `verify_wiki.py`;
- next human gate, if any.
