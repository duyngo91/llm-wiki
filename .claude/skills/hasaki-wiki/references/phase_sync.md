---
tags: [wiki-rules, reference]
status: Done
updated: 2026-05-30
---

# Phase: Sync, Lint & State Control

> Dùng bởi: `/wiki-sync-helper` — daily sync, lint/verify, Kanban management, state transitions, bug lifecycle.
> Naming/Tags/Status/Gates: [`shared.md`](shared.md).

---

## KANBAN.md — Cú pháp card

3 cột: `## TODO` · `## InProgress` · `## Done`. Không có Changelog — mọi thay đổi → `log.md`.

| Loại card | Cú pháp |
|:----------|:--------|
| Task test | `- [ ] [[raw_sources/[p]/tasks/MÃ\|MÃ]] ➔ [[wiki/[p]/test_suites/test_X\|Test X]] [Priority]` |
| QA Internal | `- [ ] [QA Internal] [[wiki/[p]/test_plans/testplan_X\|Test Plan X]] ➔ Mô tả` |
| Release | `- [ ] [Release] [[wiki/[p]/releases/cr_X\|CR-X]] ➔ Smoke Test Prod [DD/MM/YYYY]` |
| Bug retest | `- [ ] [[wiki/[p]/bugs_knowledge/bug_X\|BUG-xxx]] ➔ Retest [Priority]` |
| Blocked | thêm `(🔴 [[wiki/[p]/bugs_knowledge/bug_X\|BUG-xxx]])` vào cuối card |

**Chuyển card:** Sprint planning → testplan `InProgress`, task test + Release → `TODO`. Daily sync → theo kết quả báo cáo.

---

## log.md — Audit Trail

Format (mới nhất lên đầu): `- [YYYY-MM-DD HH:mm:ss] [action-type] | Mô tả ngắn`

Action types: `[ingest]` `[task-update]` `[sync-daily]` `[lint-sync]` `[test-progress]` `[test-run]` `[test-blocked]` `[create]`

---

## Changelog (trong feature/API Spec/test suite)

Format bảng (mới nhất lên đầu): `| YYYY-MM-DD HH:mm:ss | vX.X | Nội dung | Nguồn-link |`

Nguồn phải là link rõ: Task ID, Daily Note, hoặc tên file PDF.

---

## Git

Commit sau mỗi batch. Message rõ nghiệp vụ:
- `docs: update feature spec for CR-X`
- `test: add regression cases for BUG-X`

Không sửa file ngoài phạm vi yêu cầu. Không push khi chưa được yêu cầu.

---

## Update Propagation Checklist

Khi có thay đổi requirement/task/TC, cập nhật đủ:
- `raw_sources/` → lưu raw mới (HSK code, TBB2 embed bên trong)
- `features/` → R/AC, Questions, Impact, Regression, Coverage, Changelog
- `api_specs/` → nếu API thay đổi
- `feature_groups/` → nếu feature/spec/suite trong group bị ảnh hưởng
- `task_specs/` → khi TBB2 hoặc Feature Spec/test suite liên quan thay đổi
- `test_suites/` → add/update/deprecate TC, Blocked Coverage, Regression Impact, TC count, Changelog
- `test_plans/` → In-Scope, Regression Scope nếu phạm vi thay đổi
- `KANBAN.md` → card + TC count
- `index.md` → thêm/xóa link
- `log.md` → 1 dòng audit với timestamp UTC+07
- `git status` → kiểm tra cuối batch

---

## Workflow 2.3: Daily Sync

**Kích hoạt:** User yêu cầu sync Daily Note hoặc Meeting Note.

```
py .claude/scripts/wiki_sync.py daily-sync --project <project> --date <YYYY-MM-DD>
```

1. Đọc `wiki/[project]/operations/daily_notes/YYYY-MM-DD.md`.
2. Script cập nhật trạng thái task trong `KANBAN.md`.
3. "Khó khăn/Blocked" → tạo `bug_[mota_ngan].md` trong `bugs_knowledge/` (status `Open`, dùng `tpl_bug_rca.md`), gắn `🔴` link vào Kanban card.
4. **Gate 3:** Thông báo QA Lead + Tech Lead triage: xác nhận tái hiện, điền RCA, Severity (Blocker/Critical/Major/Minor).
5. Thay đổi requirement từ daily → AI đề xuất Impact Analysis → **HITL Gate** (QA Lead + PO xác nhận) trước khi sửa file.
6. Đổi Daily Note status → `Synced`. Ghi log `[sync-daily]`.

---

## Workflow 2.4: Lint & Sync

**Kích hoạt:** User yêu cầu "lint & sync". Mặc định chạy `verify` (audit-only). Chỉ `sync` khi có Gate 4.

```
py .claude/scripts/wiki_sync.py verify
```

Kiểm tra (xem `shared.md#tags-chuẩn` cho tag → folder mapping):
- Tag phân cấp chuẩn, Feature Group page tương ứng
- Broken links, orphan notes
- Mỗi Feature có Test Suite, API Spec có tag bắt buộc
- Test Suite có cột `Phạm vi`, mọi TC có nguồn explicit
- Không TC cover R/AC còn câu hỏi `Open`
- Governance: Kanban TC count, Changelog, Blocked Coverage, Regression Impact, secret/token, UTF-8/mojibake, status frontmatter

Báo cáo kết quả. Ghi log `[lint-sync]`.

Nếu `change_impact_report.json` có feature `Stale` hoặc `has_open_question=true`:
- Phải cập nhật Impact Analysis trước.
- Testcase liên quan phải giữ Blocked cho đến khi câu hỏi được đóng.

---

## Workflow 2.5: State Transition

**InProgress:**
- Card đúng cột `## InProgress`. TC chưa sẵn sàng → nhắc hoặc sinh nháp. Ghi log `[test-progress]`.

**Done (test hoàn tất — cần Gate 4):**
- Test Suite: `⏳` → `✅`/`❌`, status → `Passed`, cập nhật thống kê Pass/Fail/Blocked.
- Feature: status → `Done`. Test Plan: status → `Passed`.
- Log: `- [YYYY-MM-DD HH:mm:ss] [test-run] | Hoàn thành chạy test [MÃ-TASK]. Kết quả: X/Y PASS.`

**Blocked:**
- Tạo bug RCA (`tpl_bug_rca.md`) trong `bugs_knowledge/`, gắn `🔴` link vào card.
- Ghi log `[test-blocked]`.
- **Bug lifecycle:** `Open → Fixed → Retest → Closed`. Dev fix → `Fixed` (ghi bằng chứng build/PR). QA retest pass → `Closed`. Fail → `Open`, cập nhật RCA/Changelog.
