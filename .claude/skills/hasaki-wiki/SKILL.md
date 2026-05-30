---
name: hasaki-wiki
description: QA wiki orchestrator for project_hasaki — manages the full SDLC documentation cycle: requirement ingestion → Feature Spec → Test Suite → Kanban sync → CR go-live. Enforces HITL gates, no-inference policy, and traceability chain (TBB2 → HSK → Task Spec → Feature → R/AC → Testcase). Use when ingesting PDFs or Hasaki tasks (HSK/TBB2), creating or updating Feature Specs or API Specs, designing test suites from approved specs, running daily sync or lint/verify, managing bugs, or packaging CR go-live docs. Trigger phrases: "ingest file", "phân tích task", "import task HSK-", "tạo test suite", "lint và sync", "daily sync", "tạo CR golive", "chốt task", "chuyển sang Done", "sync my open tasks", "get my tasks".
metadata:
  author: Yen Ngo
  version: "3.1"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
---

# Hasaki Wiki Skill

> Naming, Tags, Status, HITL Gates, Knowledge Scope, Scripts available: [`references/shared.md`](references/shared.md). Trước khi thực hiện bất kỳ phase nào, đọc phase reference tương ứng.

## Workflow Routing

| Intent | Command | Đọc trước khi thực hiện |
|:-------|:--------|:------------------------|
| Phân tích requirement / ingest PDF / task HSK | `/wiki-requirement-analyzer` | `references/phase_ingest.md` |
| Thiết kế test suite từ Spec đã duyệt (Gate 1 xong) | `/wiki-test-designer` | `references/phase_test_design.md` |
| Daily sync, lint, Kanban, verify, state transition | `/wiki-sync-helper` | `references/phase_sync.md` |
| Scan / import / xem task Hasaki | `/get-my-tasks` · `/import-hasaki-task` · `/get-hasaki-task` · `/sync-my-open-tasks` | `references/phase_task_intake.md` |
| Tạo CR Go-Live, Test Plan, Smoke Test Production | (via `/wiki-sync-helper` hoặc trực tiếp) | `references/phase_golive.md` |
| Kiểm tra MCP health | `/mcp-health-check` | — |

## Core Rules (tóm tắt — full ở `shared.md#core-rules-quick-reference`)

- **Timezone:** `UTC+07:00` (`Asia/Ho_Chi_Minh`), format `YYYY-MM-DD HH:mm:ss`.
- **No-Inference:** Requirement/AC/API/testcase phải explicit từ nguồn duyệt. Chưa rõ → `## ❓ Câu hỏi chưa rõ` + `Blocked Coverage`.
- **Large doc strategy:** Doc >50 trang → đọc TOC trước, lập section list, đọc hết section trước khi viết spec. Feature chưa đọc đủ → `partial_read: true`, tạo stub, ghi Blocked Coverage.
- **Enum verify:** Mọi claim về list values → grep raw đếm đủ + ghi `#line`. Filter table và mapping table cùng feature có thể khác nhau — verify riêng.
- **SSOT:** File trên đĩa là nguồn thật. Đọc trực tiếp trước mỗi thao tác.
- **Test Case:** Chỉ tạo từ R/AC explicit đã duyệt (Gate 1). R/AC có question `Open` → `Blocked Coverage`.

## Traceability Chain

```
Raw Source (PDF/HSK task) → Feature Spec (R/AC) → API Spec (nếu có)
    → Task Spec (task_<tbb2>.md) → Test Suite → Test Plan/CR
```

TBB2 resolve HSK cha qua `parent_id`. Raw file lưu theo HSK code (`HSK-xxxxx.md`). TBB2 embed vào `## Test Requests (TBB2)` bên trong HSK raw file.

## Feature Spec Frontmatter (tối thiểu bắt buộc)

`feature` · `project` · `source_version` · `source_doc` · `source_range` · `partial_read` · `last_verified_at` · `verification_status`

Source quyết định pass/fail chính thức: `wiki/project_hasaki/refiner/quality_gates.json`.

## Done Criteria

`py .claude/scripts/wiki_sync.py verify` passes. Tất cả artifacts đã cập nhật: feature / api_spec / task_spec / test_suite / test_plan / kanban / log / traceability.
