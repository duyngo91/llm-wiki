---
tags: [wiki-rules, reference]
status: Done
updated: 2026-05-30
---

# Phase: CR Go-Live

> Dùng khi: kết thúc Sprint hoặc có lịch deploy Production dưới mã CR cụ thể.
> Naming/Status/Gates: [`shared.md`](shared.md).

---

## Workflow: CR Go-Live

**Bước 1 — Khởi tạo:**
- Tạo `testplan_cr_[ID].md` trong `test_plans/` (dùng `tpl_test_plan.md`, status `Draft`/`Testing`).
- Tạo `cr_[MÃ_CR]_golive_[ddMMyyyy].md` trong `releases/` (dùng `tpl_cr_golive.md`, status `Draft`).
- Xác định Scope: link Features/API Specs/Test Suites liên quan.
- Định nghĩa Exit Criteria Staging: 100% TC Passed, không còn bug Critical/Blocker.

**Bước 2 — Đóng gói kỹ thuật (khi Staging PASS):**
- Soạn Deploy Steps (môi trường, thứ tự service, migrations, config).
- Soạn Rollback Steps (kịch bản và điều kiện kích hoạt).
- Lập Smoke Test list cho Production (các TC quan trọng nhất, thực hiện nhanh được).
- Cập nhật Release status → `Testing`.

**Bước 3 — Production Smoke Test:**
- User chạy Smoke Test Production, cập nhật `✅`/`❌` vào bảng CR.
- Pass → CR status `Done`. Fail → kích hoạt Rollback Steps, ghi kết quả.
- **Gate 5:** PO + QA Lead ký duyệt — bắt buộc `approved_by` · `approved_at` · `approval_note`.

**Bước 4:** Archive Kanban cards (di chuyển → `## Done`). Ghi log `[test-run]`.

---

## Double-linking bắt buộc

CR Go-Live doc phải link đến:
- Tất cả Feature Specs trong scope: `[[wiki/project_hasaki/features/X]]`
- Test Suites tương ứng
- Test Plan liên kết
- Daily Notes quan trọng trong Sprint

Feature Spec và Test Suite được đưa vào CR scope phải có link ngược lại CR doc trong mục `## Impact Analysis & Regression Proposal`.
