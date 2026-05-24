---
description: "Sync batch my open tasks from Hasaki and propagate raw/task-spec/traceability"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Command: Sync My Open Tasks

Use this command for on-demand batch synchronization of open tasks assigned to the current user.

## Trigger

- `sync my open tasks`
- `sync my open tasks --limit 20`
- `sync my open tasks --images`
- `sync my open tasks --dry-run`

## Execution

```powershell
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
python .claude/scripts/wiki_sync.py sync-my-open-tasks --limit 20 --dry-run
```

Apply mode:

```powershell
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
python .claude/scripts/wiki_sync.py sync-my-open-tasks --limit 20 --images
```

## Behavior

- Fetch `my-task` with status `_00_01` (Todo/Processing).
- Resolve relation `TBB2 <-> HSK` when possible.
- Append raw snapshot to `raw_sources/project_hasaki/tasks/<TASK_CODE>.md`.
- Upsert task spec for each `TBB2` under `wiki/project_hasaki/task_specs/`.
- Update machine-readable links in `traceability.json` and `project_registry.json`.
- Add Kanban TODO card for each `TBB2` when missing.
- Respect no-inference policy: unclear behavior stays in Questions/Blocked Coverage.
