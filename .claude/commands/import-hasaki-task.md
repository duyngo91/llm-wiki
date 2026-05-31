---
description: "Import task từ Hasaki Workplace: fetch, extract AC list, lưu vào raw_sources/project_hasaki/tasks/ và cập nhật KANBAN. Delegate sang @hasaki-task-intake (haiku)."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Import Hasaki Task (router)

Delegate sang sub-agent **`hasaki-task-intake`** (model haiku).

Input từ user: $ARGUMENTS

Worker đọc `.claude/skills/hasaki-wiki/references/phase_task_intake.md` → **Workflow B** và thực thi đủ Bước 1-7: fetch (`hasaki_task.py`), xác định Feature Spec liên quan (đợi confirm), extract AC List (4a-4e, no-inference), lưu Task Note theo template, cập nhật KANBAN + log. Output là raw source; bước tiếp theo là `@hasaki-ingest` để tạo Feature Spec.
