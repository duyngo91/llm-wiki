---
name: hasaki-wiki
description: QA wiki orchestrator for project_hasaki — manages the full SDLC documentation cycle: requirement ingestion → Feature Spec → Test Suite → Kanban sync → CR go-live. Enforces HITL gates, no-inference policy, and traceability chain (TBB2 → HSK → Task Spec → Feature → R/AC → Testcase). Use when ingesting PDFs or Hasaki tasks (HSK/TBB2), creating or updating Feature Specs or API Specs, designing test suites from approved specs, running daily sync or lint/verify, managing bugs, or packaging CR go-live docs. Trigger phrases: "ingest file", "phân tích task", "import task HSK-", "tạo test suite", "lint và sync", "daily sync", "tạo CR golive", "chốt task", "chuyển sang Done", "sync my open tasks", "get my tasks".
metadata:
  author: Yen Ngo
  version: "3.2"
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

**Pattern:** Skill này là **playbook orchestrator** chạy trong main session. Mỗi phase có 1 worker sub-agent (`.claude/agents/hasaki-*.md`) tự gán model riêng. Việc route dựa trên cơ chế **auto-delegation native của Claude** (Claude chọn agent theo field `description`) — bảng dưới chỉ là bản đồ tường minh để main session/người dùng biết phase nào → agent nào → đọc reference nào. Mục tiêu: việc nặng chạy ở worker đúng model (haiku/sonnet/opus), không dồn mọi phase vào model đắt ở main session.

| Intent | Command | Worker sub-agent | Model | Đọc trước khi thực hiện |
|:-------|:--------|:-----------------|:-----:|:------------------------|
| Phân tích requirement / ingest PDF / task HSK | `/wiki-requirement-analyzer` | `@hasaki-ingest` | opus | `references/phase_ingest.md` |
| Thiết kế test suite từ Spec đã duyệt (Gate 1 xong) | `/wiki-test-designer` | `@hasaki-test-design` | sonnet | `references/phase_test_design.md` |
| Daily sync, lint, Kanban, verify, state transition | `/wiki-sync-helper` | `@hasaki-sync` | haiku | `references/phase_sync.md` |
| Scan / import / xem task Hasaki | `/get-my-tasks` · `/import-hasaki-task` · `/get-hasaki-task` · `/sync-my-open-tasks` | `@hasaki-task-intake` | haiku | `references/phase_task_intake.md` |
| Tạo CR Go-Live, Test Plan, Smoke Test Production | (via `/wiki-sync-helper` hoặc trực tiếp) | `@hasaki-golive` | sonnet | `references/phase_golive.md` |
| Kiểm tra MCP health | `/mcp-health-check` | (main session) | — | — |

**Quy tắc delegation:**

1. **Main session là orchestrator** — đọc intent, xác định phase, spawn đúng worker sub-agent qua Agent tool. Không tự làm phase công việc khi đã có worker tương ứng.
2. **Trừ khi user explicit override** ("không delegate", "tự làm đi"), main session **phải** route sang worker để khớp model phase.
3. **Worker sub-agents độc lập** — không spawn sub-agent khác. Khi worker cần phase khác (vd ingest xong cần verify), nó **suggest** main session gọi worker tiếp theo, không tự gọi.
4. **Chain workflow tiêu biểu:** `@hasaki-task-intake` (haiku, fetch raw) → `@hasaki-ingest` (opus, parse spec) → `@hasaki-verify-structural` → `@hasaki-verify-inference` → `@hasaki-test-design` (sonnet, sinh testcase) → `@hasaki-sync` (haiku, lint + Kanban) → `@hasaki-golive` (sonnet, CR package).

## Core Rules

> **Policy chuẩn = [`.claude/rules/*.md`](../../rules/)** (no-inference, encoding, timezone, SSOT, testcase, secret) + domain knowledge ở [`references/shared.md`](references/shared.md). Không lặp lại. Hai policy **riêng của wiki phase** (không có trong `rules/`) cần nhớ:

- **Large doc strategy:** Doc >50 trang (hoặc index có >5 sections) → chạy `plan_ingest_tasks.py` sinh task list per section, ép TaskCreate/TaskUpdate cho mỗi section trước khi viết spec. Feature chưa đọc đủ → `partial_read: true`, tạo stub, ghi Blocked Coverage.
- **Enum verify:** Mọi claim về list values → grep raw đếm đủ + ghi `#line`. Filter table và mapping table cùng feature có thể khác nhau — verify riêng.

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
