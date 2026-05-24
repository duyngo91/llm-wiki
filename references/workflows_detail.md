---
tags: [wiki-rules, reference]
status: Done
created: 2026-05-24
---

# 📋 Chi Tiết Quy Trình Vận Hành — QA LLM Wiki

> File tham khảo chi tiết cho Section 2 của `WIKI_RULES.md`. Claude đọc file này khi cần tra cứu đầy đủ các bước của từng quy trình.

---

## Quy trình 2.0: Khởi tạo dự án mới (New Project Setup)

**Kích hoạt:** Dự án chưa tồn tại trong `wiki/` hoặc người dùng yêu cầu tạo project mới.

**Các bước:**

1. **Tạo cấu trúc chuẩn:**
   - `raw_sources/[project]/{tasks,requirements,issues,assets}/`
   - `wiki/[project]/{features,api_specs,feature_groups,test_suites,test_plans,releases,bugs_knowledge}/`
   - `wiki/[project]/operations/` và `wiki/[project]/operations/daily_notes/`

2. **Khởi tạo file operations tối thiểu:**
   - `wiki/[project]/operations/environments.md`
   - `wiki/[project]/operations/test_data.md`
   - `wiki/[project]/operations/team_contacts.md`

3. **Đăng ký điều hướng:**
   - Cập nhật `index.md` thêm khu vực project mới.
   - Tạo ít nhất một Feature Group page nếu project có nhiều feature cùng domain.
   - Tạo Kanban cards khởi tạo Sprint theo quy tắc §4.2 trong WIKI_RULES.md.
   - Ghi log `[create]`.

---

## Quy trình 2.1: Ingest Tài Liệu PDF Lớn (Baseline PDF)

**Kích hoạt:** File PDF mới trong `raw_sources/[project]/requirements/`.

**⚠️ Quy trình 2 bước ISTQB — bắt buộc tách biệt:**
- Bước A: Test Analysis → skill `wiki-requirement-analyzer`
- Bước B: Test Design → skill `wiki-test-designer`

**Bước 1 — Convert PDF:**
- Dùng MCP `markitdown/convert_to_markdown` chuyển PDF → Markdown.
- Lưu `*_converted.md` hoặc `*_ai_readable.md` cạnh file PDF gốc trong `requirements/`.
- Không sửa raw PDF, không ghi đè file raw đã lưu.

**Bước 2 — Phân tích & Tách:**
- Đọc Markdown đã convert, tách theo feature/module.
- Mỗi Feature Spec tham chiếu rõ PDF gốc + Markdown AI-readable đã dùng.

**Bước 3 — ISTQB 2 bước có HITL:**

- **Bước A (wiki-requirement-analyzer):**
  - Trùng cũ → Diff, cập nhật Spec, ghi Changelog.
  - Mới → Tạo `[feature]_[mucnho].md` trong `features/` theo `tpl_requirement.md`, phân rã R-IDs, vạch flows, status `Draft`. Nếu có API explicit → tạo `api_specs/api_[feature]_[mucnho].md` theo `tpl_api_spec.md`; chưa rõ endpoint/payload → ghi câu hỏi, không suy diễn.
  - **🤝 Gate 1:** Dừng, trình bày Spec cho PO/QA Lead. Chờ duyệt (`status: Done`) trước khi sang Bước B.

- **Bước B (wiki-test-designer):**
  - Đọc Feature Spec đã duyệt + `test_data.md` + `environments.md`.
  - Tạo/cập nhật `test_[feature]_[mucnho].md` trong `test_suites/`, status `Draft`, TC ký hiệu `⏳`.
  - **🤝 Gate 2:** Dừng, trình bày Test Suite cho QA Lead. Chờ duyệt (`status: Testing`) trước khi đưa vào hàng đợi test.

**Bước 4:** Thêm card vào `KANBAN.md` `## TODO`, ghi log `[ingest]`.

---

## Quy trình 2.2: Xử Lý Task Thay Đổi Từ Jira/Slack (Task Change Workflow)

**Kích hoạt:** User cung cấp Task/Jira Ticket có yêu cầu thay đổi.

**⚠️ Thực thi chuẩn ISTQB:** Cập nhật Spec trước (Bước A) → cập nhật Test Cases sau (Bước B).

**Bước 1 — Impact Analysis:**
- Đọc `index.md` định vị file liên quan.
- Quét `features/`, `api_specs/`, `test_suites/` xác định vùng bị ảnh hưởng.
- Ghi bảng Impact Analysis trước khi sửa:
  `Change ID/Source | Change type (Add/Update/Remove/Clarify) | Affected R/AC | Affected Features | Affected API Specs | Affected Test Suites | TC action | Regression candidates | Open questions/Gate`

**Bước 2 — Clarification Questions (Gate A):**
- Dùng `wiki-requirement-analyzer` phát hiện kẽ hở.
- Soạn câu hỏi phân loại theo đối tượng (PO: nghiệp vụ; Dev Lead: kỹ thuật).
- **🤝 HITL Gate:** Dừng chờ phản hồi. Không phỏng đoán nghiệp vụ.

**Bước 3 — Cập nhật có HITL:**
- **Bước A:** Nhận câu trả lời → cập nhật Feature Spec + API Spec, đổi status về `Draft`, ghi Changelog kèm mã Task. → **Gate 1** (người dùng ký duyệt Spec).
- **Bước B:** Gọi `wiki-test-designer` → cập nhật Test Suite. TC cũ hết hiệu lực → chuyển vào `Deprecated`, không xóa. Chỉ sinh TC cho R/AC đã rõ, không còn câu hỏi `Open`.
- **Bước C:** Cập nhật `Regression Impact` trong Feature/Test Suite/Test Plan.
- Di chuyển card Kanban → `## InProgress`.

**Bước 4:** Ghi log `[task-update]`.

---

## Quy trình 2.3: Đồng Bộ Daily Note (Daily Sync Workflow)

**Kích hoạt:** User yêu cầu sync Daily Note hoặc Meeting Note.

**⚠️ Thực thi:** Dùng skill `wiki-sync-helper`:
```
python .claude/scripts/wiki_sync.py daily-sync --project <project_name> --date <YYYY-MM-DD>
```

**Bước 1:** Đọc `wiki/[project]/operations/daily_notes/YYYY-MM-DD.md`.

**Bước 2 — Daily Standup & Bug (có Gate):**
- Script cập nhật trạng thái task trong `KANBAN.md`.
- Nếu "Khó khăn/Blocked" ghi lỗi cụ thể → script tạo `bug_[mota_ngan].md` trong `bugs_knowledge/` (`tpl_bug_rca.md`, status: `Open`) + gắn link `🔴` vào Kanban card.
- **🤝 Gate 3:** Thông báo QA Lead + Tech Lead triage: xác nhận tái hiện, điền RCA, Severity (Blocker/Critical/Major/Minor).
- Đổi Daily Note status → `Synced`.

**Bước 3 — Thay đổi Requirement từ Daily:**
- Với mỗi quyết định thay đổi nghiệp vụ: AI đề xuất Impact Analysis + Regression Proposal.
- **🤝 HITL Gate:** QA Lead + PO xác nhận trước khi AI sửa file. Changelog ghi nguồn `Theo Daily Note [[YYYY-MM-DD]]`.

**Bước 4:** Ghi log `[sync-daily]`.

---

## Quy trình 2.4: Lint & Auto-Sync Workflow

**Kích hoạt:** User yêu cầu "lint & sync".

**⚠️ Mặc định:** Chạy `verify` (audit-only) trước. Chỉ chạy `sync` khi đã có Gate 4 rõ ràng.
**🤝 Gate 4:** AI tuyệt đối không tự sync nếu con người chưa xác nhận test thực tế thành công.

**Các bước:**
1. `python .claude/scripts/wiki_sync.py verify` (hoặc `sync` nếu đã có Gate 4).
2. Đồng bộ Kanban: task `Done` (có Gate 4) → cập nhật Feature/Test Suite `Done`/`Passed`; `InProgress`/`TODO` → kiểm tra phản ánh thực tế.
3. Đồng bộ Go-Live: quét `releases/`, nếu test `Passed` + có Gate 4/5 → cập nhật Release → `Testing`, thông báo QA Lead.
4. Kiểm định Tag & cấu trúc: tag phân cấp chuẩn, Feature Group page tương ứng.
5. Kiểm tra Link & độ phủ: broken links, orphan notes, mỗi Feature có Test Suite, API Spec có tag bắt buộc, Test Suite có cột `Phạm vi`, mọi TC có nguồn explicit, không có TC cover R/AC còn câu hỏi `Open`.
6. Governance: Kanban TC count, Changelog, Blocked Coverage, Regression Impact, secret/token, UTF-8/mojibake, status frontmatter, links index/log/KANBAN.
7. Báo cáo kết quả `verify` đính kèm phản hồi cho user.
8. Ghi log `[lint-sync]`.

---

## Quy trình 2.5: Task State Transition Workflow

**Kích hoạt:** User báo di chuyển task trên Kanban hoặc yêu cầu cập nhật trạng thái test.

**InProgress:**
- Đảm bảo card đúng cột `## InProgress`.
- Nếu Test Cases chưa sẵn sàng → nhắc hoặc sinh nháp.
- Ghi log `[test-progress]`.

**Done (test hoàn tất):**
- Test Suite: ⏳ → ✅ Pass (hoặc theo kết quả thực tế), status → `Passed`, cập nhật bảng thống kê Pass/Fail/Blocked.
- Feature: status → `Done`.
- Test Plan: status → `Passed`.
- Ghi log `[test-run]`: `- [YYYY-MM-DD] [test-run] | Hoàn thành chạy test [MÃ-TASK]. Kết quả: X/Y PASS.`

**Blocked:**
- Tạo bug RCA (`tpl_bug_rca.md`) trong `bugs_knowledge/`.
- Gắn link `(🔴 [[wiki/[p]/bugs_knowledge/bug_X|BUG-xxx]])` vào Kanban card.
- Ghi log `[test-blocked]`.

**Bug lifecycle:** `Open → Fixed → Retest → Closed`
- Dev fix: status `Fixed`, ghi bằng chứng build/PR.
- QA retest pass → `Closed`. Fail → `Open`, cập nhật RCA/Changelog.

---

## Quy trình 2.6: CR Go-Live (Hybrid Model)

**Kích hoạt:** Kết thúc Sprint hoặc có lịch deploy Production dưới mã CR cụ thể.

**Bước 1 — Khởi tạo:**
- Tạo `testplan_cr_[ID].md` trong `test_plans/` (`tpl_test_plan.md`, status `Draft`/`Testing`).
- Tạo `cr_[MÃ_CR]_golive_[ddMMyyyy].md` trong `releases/` (`tpl_cr_golive.md`, status `Draft`).
- Xác định Scope, link Features/API Specs/Test Suites. Định nghĩa Exit Criteria Staging (100% Passed, không còn bug nghiêm trọng).

**Bước 2 — Đóng gói kỹ thuật (khi Staging PASS):**
- Soạn Deploy Steps + Rollback Steps.
- Thiết lập Smoke Test list cho Production.

**Bước 3 — Production Smoke Test:**
- User chạy Smoke Test Production, cập nhật ✅/❌ vào bảng CR.
- Pass → CR status `Done`. Fail → kích hoạt Rollback Steps.
- **🤝 Gate 5:** PO + QA Lead ký duyệt.

**Bước 4:** Archive Kanban cards. Ghi log `[test-run]`.
