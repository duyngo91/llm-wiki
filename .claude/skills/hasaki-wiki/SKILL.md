---
name: hasaki-wiki
description: QA wiki orchestrator for project_hasaki — manages the full SDLC documentation cycle: requirement ingestion → Feature Spec → Test Suite → Kanban sync → CR go-live. Enforces HITL gates, no-inference policy, and traceability chain (TBB2 → HSK → Task Spec → Feature → R/AC → Testcase). Use when ingesting PDFs or Hasaki tasks (HSK/TBB2), creating or updating Feature Specs or API Specs, designing test suites from approved specs, running daily sync or lint/verify, managing bugs, or packaging CR go-live docs. Trigger phrases: "ingest file", "phân tích task", "import task HSK-", "tạo test suite", "lint và sync", "daily sync", "tạo CR golive", "chốt task", "chuyển sang Done", "sync my open tasks", "get my tasks".
metadata:
  author: Yen Ngo
  version: "2.0"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
---

# Hasaki Wiki Skill

## Workflow Routing

| Intent | Command |
|:-------|:--------|
| Phân tích requirement / ingest PDF / task | `/wiki-requirement-analyzer` |
| Thiết kế test suite từ Spec đã duyệt | `/wiki-test-designer` |
| Daily sync, lint, Kanban, verify | `/wiki-sync-helper` |
| Lấy thông tin task Hasaki (xem) | `/get-hasaki-task` |
| Import task + extract AC list vào vault | `/import-hasaki-task` |
| Scan tất cả tasks được assign | `/get-my-tasks` |
| Sync open tasks từ Hasaki Workplace | `/sync-my-open-tasks` |
| Kiểm tra MCP health | `/mcp-health-check` |

## Core Guardrails

- Timezone: `Asia/Saigon` (`UTC+07:00`) cho mọi timestamp.
- Không suy diễn requirement/AC/API/testcase từ nguồn không rõ.
- Thông tin chưa rõ → ghi vào `## ❓ Câu hỏi chưa rõ` + `Blocked Coverage`.
- Test case chỉ được tạo từ requirement/AC explicit đã được duyệt (Gate 1).
- Không tự sync status `Done/Passed` khi chưa có Gate 4 confirmation.

## Traceability Chain

```
Raw Source (PDF/task) → Feature Spec (R/AC) → API Spec (nếu có)
    → Task Spec (task_<tbb2>.md) → Test Suite → Test Plan/CR
```

TBB2 task: resolve HSK cha qua `parent_id`. Raw file lưu theo HSK code (`HSK-xxxxx.md`).

## Knowledge Scope

- **Allowed:** `wiki/`, `raw_sources/`, `templates/`, `.claude/commands/`, `.claude/scripts/`, root control docs
- **Excluded:** `.obsidian/`, `.smart-env/`, `.karate_cache/`, `.git/`, `__pycache__/`, plugin/cache/db

## Done Criteria

- `python .claude/scripts/wiki_sync.py verify` passes without guardrail errors.
- All linked artifacts updated: feature / api_spec / task_spec / test_suite / test_plan / kanban / log / traceability.

## Reference Docs

| File | Dùng khi | Command |
|:-----|:---------|:--------|
| `references/wiki_rules.md` | Foundation: HITL gates, structure, naming, traceability, workflows | tất cả |
| `references/doc_standards.md` | Chuẩn viết Feature Spec, API Spec, Test Suite, TC | analyzer, designer |
| `references/control_files.md` | KANBAN syntax, log format, propagation checklist | sync-helper |
| `references/workflows_detail.md` | Chi tiết từng bước workflow 2.0–2.7 | khi cần tra cứu sâu |
| `references/status_reference.md` | Bảng status hợp lệ theo từng loại file | khi cần validate status |
| `.claude/rules/*.md` | Normative policy (luôn active) | — |
