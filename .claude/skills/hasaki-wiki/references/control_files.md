---
tags: [wiki-rules, reference]
status: Done
created: 2026-05-24
---

# 📄 Các File Điều Khiển — QA LLM Wiki

> Dùng bởi: `wiki-sync-helper` và bất kỳ thao tác nào cần KANBAN syntax, log format, hoặc update propagation.

---

## 4.1 `index.md` — Bản đồ điều hướng

Liệt kê tất cả trang wiki + link `[[...]]` + mô tả 1 dòng, phân loại theo Feature Groups / Features / API Specs / Test Suites / Bugs / Operations. Đọc đầu tiên khi xử lý bất kỳ request nào. Cập nhật ngay khi có trang mới.

---

## 4.2 `KANBAN.md` — Kanban Task Board

3 cột: `## TODO` · `## InProgress` · `## Done`. Không ghi Changelog — mọi change → `log.md`.

**Cú pháp card theo loại:**

| Loại | Cú pháp |
|:-----|:--------|
| Task test | `- [ ] [[raw_sources/[p]/tasks/MÃ\|MÃ]] ➔ [[wiki/[p]/test_suites/test_X\|Test X]] [Priority]` |
| QA Internal | `- [ ] [QA Internal] [[wiki/[p]/test_plans/testplan_X\|Test Plan X]] ➔ Mô tả` |
| Release | `- [ ] [Release] [[wiki/[p]/releases/cr_X\|CR-X]] ➔ Smoke Test Prod [DD/MM/YYYY]` |
| Bug retest | `- [ ] [[wiki/[p]/bugs_knowledge/bug_X\|BUG-xxx]] ➔ Retest [Priority]` |
| Blocked | thêm `(🔴 [[wiki/[p]/bugs_knowledge/bug_X\|BUG-xxx]])` vào cuối card |

**Khi Sprint planning:** `testplan` → `InProgress`; task test + `Release` → `TODO`.
**Khi ingest Specs (PDF/task):** chèn card task test mới vào `## TODO`.
**Khi get-my-tasks download NEW HSK task:** chèn card `## TODO` với HSK code — chờ user confirm trước khi `/wiki-requirement-analyzer`.
**Khi get-my-tasks phát hiện UPDATED HSK task:** di chuyển card tương ứng sang `## InProgress` sau khi user xác nhận cần cập nhật Spec.
**Khi Daily Sync:** di chuyển card theo kết quả báo cáo.

---

## 4.3 `log.md` — Audit Trail

Format (mới nhất lên đầu): `- [YYYY-MM-DD HH:mm:ss] [action-type] | Mô tả ngắn`

Action types: `[ingest]` `[task-update]` `[sync-daily]` `[lint-sync]` `[test-progress]` `[test-run]` `[test-blocked]` `[create]`

---

## 4.4 Changelog (trong feature/API Spec/test suite)

Format bảng (mới nhất lên đầu): `| YYYY-MM-DD HH:mm:ss | vX.X | Nội dung | Nguồn-link |`
Nguồn phải là link rõ: Task ID, Daily Note, hoặc tên file PDF.

---

## 4.5 Git

Sau mỗi batch xử lý: chạy `git status`. Commit nhỏ, message rõ nghiệp vụ:
- `docs: update feature spec for CR-X`
- `test: add regression cases for BUG-X`

Không sửa file ngoài phạm vi yêu cầu. Chỉ push khi người dùng yêu cầu.

---

## 4.6 Update Propagation Checklist

Khi có thay đổi requirement/task/TC, cập nhật đủ các nơi:
- `raw_sources/[p]/...` — lưu raw mới nếu có
  - Hasaki: raw file lưu theo HSK code (`HSK-xxxxx.md`), TBB2 embed bên trong — không tạo file riêng TBB2
  - Sau khi download HSK raw → KANBAN card (NEW) hoặc Impact Analysis (UPDATED) trước khi chạm wiki/
- `features/` — R/AC, Questions, Impact, Regression, Coverage, Changelog
- `api_specs/` — API contract, Questions, Coverage, Changelog (nếu API thay đổi)
- `feature_groups/` — nếu feature/spec/suite trong group bị ảnh hưởng
- `task_specs/` — cập nhật Task Spec khi TBB2 thay đổi hoặc Feature Spec/test suite liên quan được cập nhật
- `test_suites/` — add/update/deprecate TC, Blocked Coverage, Regression Impact, TC count, Changelog
- `test_plans/` — In-Scope, Regression Scope, Coverage nếu phạm vi thay đổi
- `KANBAN.md` — card + TC count
- `index.md` — thêm/xóa link
- `log.md` — 1 dòng audit với timestamp UTC+07
- `git status` — kiểm tra cuối batch, không revert file ngoài phạm vi
