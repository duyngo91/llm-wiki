---
description: "Bảo trì wiki: daily note sync, Kanban sync, test coverage, audit broken links, state transition, release/go-live qua wiki_sync.py. Delegate sang @hasaki-sync (haiku)."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Wiki Sync Helper (router)

Delegate yêu cầu này sang sub-agent **`hasaki-sync`** (model haiku, phase sync của skill `hasaki-wiki`).

Input từ user: $ARGUMENTS

Worker sẽ đọc `.claude/skills/hasaki-wiki/references/phase_sync.md` (single source: KANBAN cú pháp, log format, Update Propagation Checklist, Workflow 2.3 Daily Sync / 2.4 Lint & Sync / 2.5 State Transition) và thực thi qua `.claude/scripts/wiki_sync.py`.

**Mặc định:** "lint và sync toàn bộ wiki" → chạy `verify` (audit-only). Chỉ chạy `sync` khi user đã xác nhận Gate 4 (test thực tế pass). Tuân thủ `.claude/rules/40-sync-governance.md`.

Batch open tasks → `/sync-my-open-tasks` (phase task-intake, Workflow D).

Nếu user yêu cầu "không delegate" → main session tự đọc `phase_sync.md` và thực thi.
