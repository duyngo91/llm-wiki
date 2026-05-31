---
description: "Tra cứu (lookup-only) 1 task Hasaki Workplace bằng task code, numeric ID hoặc URL — hiển thị, không lưu markdown. Delegate sang @hasaki-task-intake (haiku)."
allowed-tools: Read, Bash
---

# Get Hasaki Task (router)

Delegate sang sub-agent **`hasaki-task-intake`** (model haiku), chế độ **lookup-only**.

Input từ user: $ARGUMENTS

Worker đọc `.claude/skills/hasaki-wiki/references/phase_task_intake.md` → **Workflow A** (script `hasaki_task.py`, token check, error handling) và hiển thị task. Không lưu markdown vào vault (chỉ `--images` mới tải ảnh về `raw_sources/project_hasaki/assets/`). Muốn phân tích + lưu đầy đủ → `/import-hasaki-task`.
