---
description: "Scan tất cả tasks Hasaki được assign cho yenngo, phát hiện NEW/UPDATED, hiển thị wiki impact, download raw files — HITL Gate 1/2 bắt buộc trước khi cập nhật Feature Spec/Test Suite. Delegate sang @hasaki-task-intake (haiku)."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Get My Tasks (router)

Delegate sang sub-agent **`hasaki-task-intake`** (model haiku).

Input từ user: $ARGUMENTS

Worker đọc `.claude/skills/hasaki-wiki/references/phase_task_intake.md` → **Workflow C** và thực thi: scan + diff (`hasaki_my_tasks.py` dry-run), hiển thị 4 nhóm NEW/UPDATED/CURRENT/ORPHAN + wiki impact, **HITL Gate** hỏi user trước khi download, download, báo cáo + log. **Chỉ cập nhật `raw_sources/`** — không tự cập nhật Feature/API Spec/Test Suite (cần Gate 1/2).
