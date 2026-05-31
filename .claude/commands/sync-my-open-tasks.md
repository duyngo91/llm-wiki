---
description: "Sync hàng loạt open tasks từ Hasaki + propagate raw/task-spec/traceability. Delegate sang @hasaki-task-intake (haiku)."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Sync My Open Tasks (router)

Delegate sang sub-agent **`hasaki-task-intake`** (model haiku).

Input từ user: $ARGUMENTS

Worker đọc `.claude/skills/hasaki-wiki/references/phase_task_intake.md` → **Workflow D** và chạy `wiki_sync.py sync-my-open-tasks` (mặc định `--dry-run` để preview; `--images` để apply): fetch open tasks `_00_01`, resolve TBB2↔HSK, append raw snapshot, upsert task_spec, update `traceability.json` + `project_registry.json`, thêm Kanban TODO. No-inference: behavior chưa rõ → Questions/Blocked Coverage.
