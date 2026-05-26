---
name: hasaki-wiki
description: QA wiki orchestrator for project_hasaki — manages the full SDLC documentation cycle: requirement ingestion → Feature Spec → Test Suite → Kanban sync → CR go-live. Enforces HITL gates, no-inference policy, and traceability chain (TBB2 → HSK → Task Spec → Feature → R/AC → Testcase). Use when ingesting PDFs or Hasaki tasks (HSK/TBB2), creating or updating Feature Specs or API Specs, designing test suites from approved specs, running daily sync or lint/verify, managing bugs, or packaging CR go-live docs. Trigger phrases: "ingest file", "phân tích task", "import task HSK-", "tạo test suite", "lint và sync", "daily sync", "tạo CR golive", "chốt task", "chuyển sang Done", "sync my open tasks", "get my tasks".
metadata:
  author: Yen Ngo
  version: "3.0"
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

| Intent | Command | Đọc trước khi thực hiện |
|:-------|:--------|:------------------------|
| Phân tích requirement / ingest PDF / task HSK | `/wiki-requirement-analyzer` | `references/phase_ingest.md` |
| Thiết kế test suite từ Spec đã duyệt (Gate 1 xong) | `/wiki-test-designer` | `references/phase_test_design.md` |
| Daily sync, lint, Kanban, verify, state transition | `/wiki-sync-helper` | `references/phase_sync.md` |
| Scan / import / xem task Hasaki | `/get-my-tasks` · `/import-hasaki-task` · `/get-hasaki-task` · `/sync-my-open-tasks` | `references/phase_task_intake.md` |
| Tạo CR Go-Live, Test Plan, Smoke Test Production | (via `/wiki-sync-helper` hoặc trực tiếp) | `references/phase_golive.md` |
| Kiểm tra MCP health | `/mcp-health-check` | — |

**Rule:** Trước khi thực hiện bất kỳ phase nào, đọc phase reference tương ứng.

## HITL Gates

| Gate | Điều kiện tiếp |
|:-----|:---------------|
| **Pre-Gate** — Refiner Verify | Chạy `hasaki-skill-refiner` sau ingest · verdict ≠ `FAIL` mới trình Gate 1 |
| **Gate 1A** — Feature Spec Approval cho specs đầy đủ | Spec `partial_read: false`, `Draft` → `Done` · tiến sang Test Design không cần chờ STUB |
| **Gate 1B** — Feature Spec Approval cho STUB | Từng STUB khi hoàn thiện → Gate riêng · không gộp với Gate 1A |
| **Gate 2** — Test Cases Review (QA Lead) | Suite `Draft` → `Testing` · xong mới chạy test |
| **Gate 3** — Bug Triage (QA Lead + Tech Lead) | Bug `Open` hợp lệ · xác nhận RCA + Severity |
| **Gate 4** — Test Execution Approval (con người confirm) | Xong mới sync wiki status |
| **Gate 5** — Go/No-Go (PO + QA Lead ký) | Xong mới close CR |

**Approval Evidence (Gate 1A/1B/2/5):** 3 trường bắt buộc trong frontmatter: `approved_by` · `approved_at: YYYY-MM-DD HH:mm:ss` · `approval_note`

## Core Rules

- **Timezone:** `UTC+07:00` (`Asia/Ho_Chi_Minh`), format `YYYY-MM-DD HH:mm:ss` cho mọi timestamp.
- **Encoding:** UTF-8 cho mọi file Markdown. Windows: `$env:PYTHONUTF8 = "1"` trước khi chạy Python.
- **No-Inference:** Requirement/AC/API/testcase phải explicit từ nguồn đã duyệt. Chưa rõ → ghi `## ❓ Câu hỏi chưa rõ` + `Blocked Coverage`. Không dùng `AI-Inferred`, `Assumption`, `Suy diễn`.
- **Large doc strategy:** Doc >50 trang → đọc TOC trước, lập danh sách sections, đọc hết từng section trước khi viết spec. Không viết spec khi chưa đọc xong section. Feature chưa đọc đủ → set `partial_read: true`, tạo stub, ghi Blocked Coverage.
- **Enum verify:** Mọi claim về list values (status, dropdown, giá trị hợp lệ) → grep raw đếm đủ + ghi `#line` reference. Filter table và mapping table cùng feature có thể khác nhau — verify riêng.
- **SSOT:** File trên đĩa là nguồn thật. Đọc trực tiếp trước mỗi thao tác — không suy đoán từ hội thoại cũ.
- **Secret:** Không commit token/cookie/API key/password. Phát hiện → dừng, báo user rotate & clean history.
- **Test Case:** Chỉ tạo từ R/AC explicit đã duyệt (Gate 1). R/AC có question `Open` → `Blocked Coverage`, không sinh TC.

## Traceability Chain

```
Raw Source (PDF/HSK task) → Feature Spec (R/AC) → API Spec (nếu có)
    → Task Spec (task_<tbb2>.md) → Test Suite → Test Plan/CR
```

TBB2 resolve HSK cha qua `parent_id`. Raw file lưu theo HSK code (`HSK-xxxxx.md`). TBB2 embed vào `## Test Requests (TBB2)` bên trong HSK raw file.

## Knowledge Scope

- **Allowed:** `wiki/`, `raw_sources/`, `templates/`, `.claude/commands/`, `.claude/scripts/`, root docs (`KANBAN.md`, `index.md`, `log.md`, `README.md`, `CLAUDE.md`), `.claude/skills/hasaki-wiki/references/`
- **Excluded:** `.obsidian/`, `.smart-env/`, `.karate_cache/`, `.git/`, `__pycache__/`, `*.sqlite`, `*.sqlite-shm`, `*.sqlite-wal`

## Done Criteria

`python .claude/scripts/wiki_sync.py verify` passes. Tất cả artifacts đã cập nhật: feature / api_spec / task_spec / test_suite / test_plan / kanban / log / traceability.
