---
name: wiki-sync-helper
description: Provides automation utilities for managing the QA LLM Wiki vault. Always consult this skill when the user asks to run a lint check, synchronize Kanban tasks, perform daily notes standup synchronization, process release go-lives, audit broken links/orphans, or when updating test cases, test suites, or requirement/feature files in the QA LLM Wiki. It runs the high-performance CLI synchronization tool (`wiki_manager.py` and `verify_wiki.py`) to execute these workflows instantly with 100% accuracy.
---

# 🤖 Wiki Sync Helper

This skill automates the tedious, error-prone, and repetitive processes defined in `WIKI_RULES.md` for the QA LLM Wiki vault, including:
1. **Daily Standup Sync (`daily-sync`)**: Automatically parses Daily Notes, moves Kanban tasks, extracts blockers to create standard Bug RCA files, and links them on Kanban.
2. **Kanban & Test Coverage Sync (`sync`)**: Scans completed tasks under the `## Done` column on Kanban, updates corresponding Test Suites and Features, converts remaining `⏳` to `✅ Pass`, recalculates the top Test Coverage tables, and runs the validation linter.
3. **Vault Integrity Audits (`verify_wiki`)**: Scans for broken links, orphan pages, and invalid frontmatter status values.

---

## 🧭 When to Trigger

Activate this skill when the user mentions:
- "sync daily", "đồng bộ daily", "standup sync"
- "sync kanban", "đồng bộ kanban", "chạy sync"
- "lint & sync", "dọn dẹp", "kiểm định", "verify wiki", "chạy linter"
- "hoàn thành task", "pass test cases", "cập nhật test coverage"
- "đóng sprint", "kết thúc sprint", "sắp deploy go-live"

---

## 🛠️ Execution Playbook

You MUST execute the following CLI commands on behalf of the user instead of doing manual markdown file search-and-replace, which is extremely token-expensive and prone to formatting drift.

### 1. Kanban and Test Coverage Auto-Sync (Quy trình 2.4 & 2.5)

Use this command when a task is completed, or during regular lint audits:
```powershell
python scripts/wiki_manager.py sync
```

**What this does automatically:**
- Scans `KANBAN.md` under the `## Done` column.
- Finds all completed Test Suite links (`wiki/[project]/test_suites/test_*.md`).
- Updates their YAML frontmatter status to `status: Passed`.
- Finds the related Feature (`wiki/[project]/features/*.md`), updates its status to `Done`, and marks the requirement checklist coverage icons from `⏳` to `✅ Pass`.
- Converts all `⏳` inside the Test Suite cases to `✅ Pass`.
- Parses the test cases, groups them, and reconstructs the **Tổng quan Test Coverage** summary table at the top of the Test Suite.
- Runs `python scripts/verify_wiki.py` to ensure zero broken links or invalid statuses exist.

### 2. Daily Standup & Bug Auto-Extraction (Quy trình 2.3)

Use this command when a Daily Note is updated or needs synchronization:
```powershell
python scripts/wiki_manager.py daily-sync --project <project_name> --date <YYYY-MM-DD>
```
*Example:* `python scripts/wiki_manager.py daily-sync --project project_orange --date 2026-05-24`

**What this does automatically:**
- Opens `wiki/[project]/operations/daily_notes/[date].md`.
- Parses the **Daily Standup** section:
  - Finds completed links in "Hôm qua đã làm" and moves the matching cards to `## Done` (with `[x]` checkbox) in `KANBAN.md`.
  - Parses "Khó khăn / Blocked". If a specific bug is written (e.g. `BUG-OH-999: Lỗi hiển thị avatar`), it auto-generates the RCA note `wiki/[project]/bugs_knowledge/bug_loi_hien_thi_avatar.md` based on `templates/tpl_bug_rca.md`.
  - Links the new bug back to the active Kanban card in `KANBAN.md` with a red link suffix: `(🔴 [[wiki/[project]/bugs_knowledge/bug_loi_hien_thi_avatar|BUG-OH-999]])`.
- Updates the Daily Note frontmatter to `status: Synced` and appends `#qa/daily/synced` tag to avoid double-processing.

### 3. Running Independent Vault Audits

To audit broken links, orphan pages, or status compliance without modifying anything:
```powershell
python scripts/verify_wiki.py
```

---

## 📋 Response Format

After executing the Python CLI commands, present a professional, visual summary of the results:

### Form 1: After Kanban Sync
```markdown
### 🔄 Đồng Bộ Hóa Kanban Thành Công
- **Test Suites Đã Chuyển Sang Passed:**
  - `[[wiki/project_orange/test_suites/test_orangehrm_auth|test_orangehrm_auth.md]]` (Đã pass 7/7 cases)
- **Features Đã Chuyển Sang Done:**
  - `[[wiki/project_orange/features/orangehrm_auth|orangehrm_auth.md]]`
- **Chỉ số kiểm thử:** Tự động tính toán lại bảng số liệu Test Coverage thành công.
- **Hoạt động hệ thống:** Đã ghi nhận lịch sử vào `log.md`.
```

### Form 2: After Daily Sync & Bug Creation
```markdown
### 📅 Đồng Bộ Daily Note Thành Công
- **Daily Note:** `[[wiki/project_orange/operations/daily_notes/2026-05-24|2026-05-24.md]]` (Trạng thái: `Synced` ✅)
- **Kanban Card Updates:** Di chuyển thẻ `CR-ORANGE-200` sang cột `## Done`.
- **Phát hiện Blocked Bug:** `BUG-OH-999: Lỗi hiển thị avatar`
  - 🚀 **Đã tự động khởi tạo Bug RCA:** `[[wiki/project_orange/bugs_knowledge/bug_loi_hien_thi_avatar|bug_loi_hien_thi_avatar.md]]` (status: `Open` 🔴)
  - 🔗 **Đã gắn link đỏ trên Kanban:** `CR-ORANGE-200 ➔ Test Suite OrangeHRM (🔴 [[wiki/project_orange/bugs_knowledge/bug_loi_hien_thi_avatar|BUG-OH-999]])`
```

Always run the `verify_wiki.py` script as a guardrail on every sync. Do not finish a sync session if there are unresolved broken links reported by the script.
