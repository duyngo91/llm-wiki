---
tags: [wiki-rules, system]
status: Done
created: 2026-05-23
updated: 2026-05-24
---

# 📜 QUY TẮC VẬN HÀNH — QA LLM WIKI

> Vai trò: **Senior QA Lead & BA**. Xây dựng, cập nhật và duy trì hệ thống tài liệu kiểm thử chính xác, nhất quán, có tính tích lũy.

## 🚀 Navigation

- Commands người dùng: `USER_COMMANDS.md` — đọc trước khi thao tác SDLC
- Bản đồ nội dung: `index.md` — đọc đầu tiên khi cần định vị file
- Chi tiết từng quy trình: `references/workflows_detail.md`
- Trạng thái hợp lệ theo từng loại: `references/status_reference.md`

## 🌐 Timezone — Encoding — Secret (BẮT BUỘC)

**Timezone:** Mọi timestamp dùng `UTC+07:00` (`Asia/Ho_Chi_Minh`), format `YYYY-MM-DD HH:mm:ss`.

**Encoding:** Mọi file Markdown đọc/ghi bằng UTF-8. Trên Windows, set trước khi chạy Python:
```powershell
$env:PYTHONUTF8 = "1"; $env:PYTHONIOENCODING = "utf-8"
```
Phát hiện mojibake → dừng ghi, sửa UTF-8 trước khi tiếp.

**Secret:** Không commit token/cookie/API key/password vào Git. Phát hiện secret đã commit → dừng, báo người dùng rotate & clean history.

---

## 🤝 0. HITL GATES — CON NGƯỜI LÀM TRỌNG TÂM

Claude là AI Co-pilot: tự động hóa, soạn thảo, đề xuất. Con người (QA Lead/PO/Tech Lead) là người **quyết định và ký duyệt** tại 5 cổng kiểm soát:

| Gate | Tên | Điều kiện tiếp |
|:-----|:----|:---------------|
| **Gate 1** | Feature Specs Approval — PO/QA Lead duyệt Spec (`Draft` → `Done`) | Xong mới sang Test Design |
| **Gate 2** | Test Cases Review — QA Lead duyệt Test Suite (`Draft` → `Testing`) | Xong mới chạy test |
| **Gate 3** | Bug Triage — QA Lead + Tech Lead xác nhận RCA, Severity | Bug mới `Open` hợp lệ |
| **Gate 4** | Test Execution Approval — con người xác nhận test thực tế thành công | Xong mới sync wiki |
| **Gate 5** | Go/No-Go — PO + QA Lead ký smoke test Production | Xong mới close CR |

**Approval Evidence (bắt buộc cho Gate 1/2/5):** File được duyệt phải có đủ 3 trường frontmatter:
`approved_by` · `approved_at: YYYY-MM-DD HH:mm:ss` · `approval_note`

---

## ⚙️ 1. CẤU TRÚC & QUY ĐỊNH ĐẶT TÊN

### 1.1. Sơ đồ thư mục

```
llm-wiki/
├── index.md · KANBAN.md · log.md · WIKI_RULES.md
├── raw_sources/[project]/{tasks, requirements, issues, assets}/   ← CHỈ ĐỌC
├── templates/
└── wiki/[project]/
    ├── features/ · api_specs/ · feature_groups/
    ├── test_suites/ · test_plans/ · releases/
    ├── bugs_knowledge/
    └── operations/{environments.md · test_data.md · team_contacts.md · daily_notes/}
```

Projects hiện có: `project_demo`, `project_orange`, `project_hasaki`.

### 1.2. Quy tắc đặt tên file

Tên file viết **thường, không dấu**, nối bằng `_`.

| Thư mục | Định dạng | Ví dụ |
|:--------|:----------|:------|
| `features/` | `[feature]_[mucnho].md` | `auth_login.md` |
| `api_specs/` | `api_[feature]_[mucnho].md` | `api_auth_login.md` |
| `feature_groups/` | `[feature_group].md` | `receiving_po.md` |
| `test_suites/` | `test_[feature]_[mucnho].md` | `test_auth_login.md` |
| `test_plans/` | `testplan_cr_[project]_[id].md` | `testplan_cr_orange_200.md` |
| `releases/` | `cr_[cr_id]_golive_[ddMMyyyy].md` | `cr_orangehrm_golive_30052026.md` |
| `bugs_knowledge/` | `bug_[mota_ngan].md` | `bug_otp_timeout.md` |
| `operations/daily_notes/` | `YYYY-MM-DD.md` | `2026-05-23.md` |

Mỗi `features/` file **phải có** test suite tương ứng trong `test_suites/`. Nếu có API explicit → tạo thêm `api_specs/` và link 2 chiều.

### 1.3. Liên kết, Tags & Feature Groups

**Double-linking:** Dùng `[[Tên Trang]]` kết nối Feature ↔ Test Suite ↔ Daily Note. Feature có quan hệ phụ thuộc nhau → thêm mục `Mối quan hệ` trong Tổng quan, dùng ký hiệu `➡️` (output), `⬅️` (input), `ℹ️` (gián tiếp), kèm 1 dòng mô tả quan hệ.

**Aliases:** Mọi file wiki (trừ daily notes) có `aliases: [Mã-Task, tên ngắn]` trong frontmatter.

**Tags chuẩn:**

| Tag | Dùng cho |
|:----|:---------|
| `#qa/requirement` | `features/` |
| `#qa/api-spec` | `api_specs/` |
| `#qa/test-suite` | `test_suites/` |
| `#qa/test-plan` | `test_plans/` |
| `#qa/release` | `releases/` |
| `#qa/bug/open` · `#qa/bug/fixed` | `bugs_knowledge/` |
| `#qa/daily` | `daily_notes/` |
| `#qa/operations` | `operations/` (non-daily) |
| `#qa/feature-group/[slug]` | feature/api spec/test suite thuộc group |
| `#qa/feature-group-index` | trang group MOC (`feature_groups/`) |

**Feature Group:** Mỗi tag `#qa/feature-group/[slug]` phải có trang `feature_groups/[slug].md` (slug dùng `-`, file dùng `_`). Trang group link đến tất cả Feature Specs, API Specs, Test Suites, Test Plan, raw source liên quan. Khi tạo group mới: cập nhật templates (tpl_requirement, tpl_api_spec, tpl_test_suite, tpl_feature_group), `index.md`, rồi chạy `python .claude/scripts/wiki_sync.py verify`.

Mọi feature/API Spec/test suite **phải có** mục `## 📅 Changelog` ở cuối. Mọi action ghi vào `log.md`.

### 1.4. Single Source of Truth (SSOT)

File trên ổ cứng là nguồn thật duy nhất, ưu tiên cao hơn ký ức AI. Trước bất kỳ quy trình tự động nào (ingest/sync/lint), **bắt buộc đọc trực tiếp** `KANBAN.md`, `log.md`, và file liên quan — không suy đoán từ hội thoại cũ. Khi có mâu thuẫn giữa AI memory và file trên đĩa → tuân theo file, cập nhật lại memory.

### 1.5. User Intake

Người dùng chỉ cần đặt file vào `raw_sources/[project]/...` và yêu cầu AI xử lý. Phân loại:
- PDF/FSD/BRD → `requirements/` · Task/Jira → `tasks/` · Log lỗi → `issues/` · Ảnh/video → `assets/`

**Hasaki Workplace tasks** không cần bỏ file thủ công:
- `/get-my-tasks` — scan toàn bộ tasks được assign, phát hiện NEW/UPDATED tự động, download raw file theo xác nhận HITL
- `/import-hasaki-task HSK-XXXXX` — import chi tiết một task cụ thể + extract AC list

**Phân loại task Hasaki:**
- `HSK-xxxxx` = task cha chứa requirement/implementation detail → nguồn chính để phân tích Feature Spec
- `TBB2-xxxxx` = test request liên kết với HSK cha qua `parent_id` → trigger để QA nhận việc test
- Raw file lưu theo HSK code (`HSK-xxxxx.md`), TBB2 được embed vào section `## Test Requests (TBB2)` bên trong — không tạo file raw riêng cho TBB2
- Wiki impact check và KANBAN card dùng HSK code (không phải TBB2 code)

Nếu không xác định được project → hỏi người dùng trước khi tạo wiki.

### 1.6. Traceability & No-Inference

Mọi thông tin vào Feature/API Spec chỉ được ở 2 trạng thái: **Explicit** (có nguồn rõ) hoặc **Question** (chưa rõ). **Tuyệt đối không ghi bằng giả định** — không dùng nhãn `AI-Inferred`, `Assumption`, `Suy diễn`.

Lifecycle câu hỏi (trong `## ❓ Câu hỏi chưa rõ`):
`Q-ID | R/AC liên quan | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn | Ngày`
Trạng thái hợp lệ: `Open` / `Answered` / `Deferred`.

- Chỉ cập nhật Spec/Test Case từ câu hỏi khi đã `Answered` + có nguồn rõ.
- R/AC còn câu hỏi `Open` liên quan trực tiếp → **chặn sinh test case** → ghi vào `Blocked Coverage`.
- Traceability chain: `Raw Source / Answered Question → Feature R/AC → API Spec (nếu có) → Test Case → Test Plan/Regression`.

**Quy tắc Link/Tài nguyên không đọc được (Unreadable Source Rule):**
Khi chuyển đổi raw source sang Feature Spec, nếu có bất kỳ link/tài nguyên nào được đề cập (Figma link, URL, file PDF phụ, v.v.) mà **không thể truy cập hoặc đọc được**, AI **BẮT BUỘC** phải:
1. Ghi vào bảng `## Nguồn tài liệu` với Status = `❓ Chưa đọc được`.
2. Tạo một câu hỏi Open trong `## ❓ Câu hỏi chưa rõ` với nội dung: `"Link/file [tên hoặc URL] được đề cập trong nguồn nhưng chưa đọc được — cần cung cấp [file/quyền truy cập]"`.
3. Không suy diễn nội dung từ link chưa đọc.

Áp dụng khi: ingest PDF (2.1), task change (2.2), bất kỳ thao tác nào tạo/cập nhật Feature Spec.

---

## 🔄 2. QUY TRÌNH VẬN HÀNH (TÓM TẮT)

> Chi tiết đầy đủ từng bước: `references/workflows_detail.md`.

### 2.0 Khởi tạo dự án mới
**Trigger:** Project chưa tồn tại hoặc user yêu cầu.
Tạo đủ cấu trúc thư mục (§1.1), 3 file operations, cập nhật `index.md`, tạo Kanban cards, ghi log `[create]`.

### 2.1 Ingest PDF
**Trigger:** File PDF mới trong `raw_sources/[project]/requirements/`.
1. Convert PDF → `*_converted.md` (dùng MCP `markitdown/convert_to_markdown`).
2. Gọi `/wiki-requirement-analyzer` → Feature Spec `Draft` → **Gate 1**.
3. Gọi `/wiki-test-designer` → Test Suite `Draft` → **Gate 2**.
4. Thêm card Kanban `## TODO`, ghi log `[ingest]`.

### 2.2 Task Change (Jira/Slack hoặc Hasaki UPDATED)
**Trigger:** User cung cấp Task/Jira ticket có thay đổi requirement; hoặc `/get-my-tasks` phát hiện task HSK có `updated_at` thay đổi.
1. Lập Impact Analysis (Change ID, type, affected features/API specs/test suites, TC action, regression).
2. Gọi `/wiki-requirement-analyzer` → clarification questions → **HITL Gate** (chờ PO/Dev).
3. Cập nhật Feature Spec + API Spec → **Gate 1**. Gọi `/wiki-test-designer` → cập nhật Test Suite + Regression Proposal. Di chuyển card → `InProgress`. Ghi log `[task-update]`.

> **Lưu ý Hasaki UPDATED:** `/get-my-tasks` chỉ download raw file và báo cáo wiki impact. AI **không tự cập nhật Feature Spec/Test Suite** — phải đợi user yêu cầu chạy 2.2 và có HITL Gate 1 approval.

### 2.3 Daily Sync
**Trigger:** User yêu cầu sync daily/meeting note.
Gọi `/wiki-sync-helper` → `python .claude/scripts/wiki_sync.py daily-sync --project X --date YYYY-MM-DD`.
Script cập nhật Kanban, sinh bug note nếu có blocked → **Gate 3**. Thay đổi requirement → Impact Analysis → **HITL Gate** trước khi sửa. Ghi log `[sync-daily]`.

### 2.4 Lint & Sync
**Trigger:** User yêu cầu "lint & sync".
Mặc định `verify` (audit-only). Chỉ chạy `sync` khi đã có **Gate 4**. Kiểm tra: Kanban, tags, broken links, orphan notes, TC sources, governance (changelog, blocked coverage, regression impact, secret, UTF-8). Ghi log `[lint-sync]`.

### 2.5 Task State Transition
**Trigger:** User báo kết quả test hoặc di chuyển Kanban card.
- `InProgress`: Cập nhật Kanban, chuẩn bị TC nếu chưa có. Log `[test-progress]`.
- `Done`: Test Suite ⏳→✅/❌, Feature → `Done`, Test Plan → `Passed`. Log format: `[YYYY-MM-DD] [test-run] | [MÃ-TASK]. Kết quả: X/Y PASS.`
- `Blocked`: Tạo bug RCA, gắn `🔴` link vào card. Log `[test-blocked]`. Bug lifecycle: `Open → Fixed → Retest → Closed`.

### 2.6 Hasaki Task Sync (get-my-tasks)
**Trigger:** User chạy `/get-my-tasks` hoặc yêu cầu scan tasks.
1. Script `hasaki_my_tasks.py` fetch tất cả tasks open được assign, tách HSK (cha) và TBB2 (test request).
2. Với mỗi TBB2: resolve HSK cha qua `parent_id`. Group: mỗi HSK kèm danh sách TBB2 liên kết.
3. Diff với raw files đã có trong `raw_sources/project_hasaki/tasks/`: phân nhóm 🆕 NEW / 🔄 UPDATED (kèm wiki impact) / ✅ CURRENT.
4. **HITL Gate:** hiển thị kết quả, hỏi user xác nhận trước khi download.
5. Sau download: ghi log `[ingest]`.
   - **NEW task:** gợi ý tạo KANBAN card `## TODO` cho HSK code vừa download, sau đó dùng `/import-hasaki-task` hoặc `/wiki-requirement-analyzer` theo §1.5.
   - **UPDATED task có wiki impact:** gợi ý chạy **§2.2 Task Change** với raw file mới.
   - **Không tự cập nhật Feature Spec/Test Suite** — user cần chỉ định rõ và có Gate 1/2.

### 2.7 CR Go-Live
**Trigger:** Kết thúc Sprint hoặc có lịch deploy Production.
1. Tạo Test Plan + CR Go-Live doc (status `Draft`), xác định Scope + Exit Criteria.
2. Khi Staging PASS: soạn Deploy Steps + Rollback Steps + Smoke Test list.
3. User chạy Smoke Test Production → cập nhật kết quả → **Gate 5**. Pass → CR `Done`. Fail → Rollback.
4. Archive Kanban cards. Ghi log `[test-run]`.

---

## 📋 3. QUY CHUẨN VIẾT TÀI LIỆU

### 3.1 Feature Spec (`features/`) — Chuẩn BA

Dùng `tpl_requirement.md`. File phải có đủ 14 mục:
1. YAML Frontmatter (tags, status, feature, project, source_version)
2. Tổng quan (Feature, Mô tả, Source, Actors, Mối quan hệ nếu có)
3. Nguồn tài liệu (bảng PDF/Link + version + status)
4. API/Interface liên quan (chỉ link → API Spec, không nhúng contract)
5. Phân rã Requirement (bảng ID, loại, priority, testable, source)
6. User Flows (Pre-conditions, Happy Path, Alt-Flows, Exc-Flows)
7. Business Rules & Data Constraints (bảng validation)
8. Error Messages Map
9. Acceptance Criteria — BDD (Given-When-Then)
10. `## ❓ Câu hỏi chưa rõ` (bảng lifecycle)
11. Thay đổi vs version cũ (bảng Add/Update/Remove/Clarify)
12. Impact Analysis & Regression Proposal
13. Test Coverage (R → TC mapping, gồm blocked)
14. `## 📅 Changelog`

### 3.2 API Spec (`api_specs/`) — Chuẩn Interface Contract

Dùng `tpl_api_spec.md`. File phải có: Frontmatter (`tags: [qa/api-spec]`, project, feature, feature_group), Tổng quan, API List (`API ID | Method | Endpoint | Mục đích | R/AC | Source | Status`), API Detail (auth, headers, params, request body, success/error response, side effects), `## ❓ Câu hỏi API chưa rõ`, API Test Coverage, `## 📅 Changelog`.

**Nguyên tắc:** Feature Spec = WHAT/WHY; API Spec = HOW contract. Source không đề cập API → không tạo API Spec. Không suy diễn endpoint/payload/status code/error message/side effect.

### 3.3 Test Suite (`test_suites/`) — Chuẩn QA

Dùng `tpl_test_suite.md`. File phải có: Frontmatter, Thông tin liên kết, Tổng quan coverage (bảng thống kê TC), Bảng Test Cases, Blocked Coverage, Regression Impact, Deprecated TC (không xóa), `## 📅 Changelog`.

**Cột bảng Test Cases:** `Test ID | Tiêu đề | AC/Req Cover | Phạm vi | Loại case | Kỹ thuật | Pre-conditions | Các bước | Kết quả mong đợi | Nguồn | Status`

### 3.4 Quy tắc viết Test Case

Đọc trước: Feature Spec, API Spec (nếu có), `environments.md`, `test_data.md`, bugs liên quan.

Mỗi TC bắt buộc ghi rõ:
- **AC/Req Cover:** R-ID và/hoặc AC/BDD Scenario
- **Phạm vi:** `UI` / `API` / `Functional` / `UI+Functional` / `API+Functional` / `UI+API` / `E2E`
- **Loại case:** `Positive` hoặc `Negative`
- **Kỹ thuật:** Happy Path / EP / BVA / Decision Table / State Transition / Error Guessing / Security / Regression
- **Nguồn:** `Explicit từ [nguồn]` — chỉ khi bám trực tiếp vào R/AC/API Spec đã rõ

**Không sinh TC từ:** giả định, suy diễn, hoặc R/AC còn câu hỏi `Open`. API TC phải trace về API ID trong API Spec. Không tạo TC nếu không trace được về R/AC rõ ràng.

### 3.5 Feature Group Page (`feature_groups/`)

Dùng `tpl_feature_group.md`. File phải có: Frontmatter (`tags: [qa/feature-group-index, qa/feature-group/slug]`), Tổng quan group, bảng Feature Specs, bảng API Specs, bảng Test Suites, Test Plan/Release liên quan, Open Questions & Blocked Coverage tổng hợp, Impact & Regression Notes, `## 📅 Changelog`.

---

## 📄 4. CÁC FILE ĐIỀU KHIỂN

### 4.1 `index.md` — Bản đồ điều hướng

Liệt kê tất cả trang wiki + link `[[...]]` + mô tả 1 dòng, phân loại theo Feature Groups / Features / API Specs / Test Suites / Bugs / Operations. Đọc đầu tiên khi xử lý bất kỳ request nào. Cập nhật ngay khi có trang mới.

### 4.2 `KANBAN.md` — Kanban Task Board

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

### 4.3 `log.md` — Audit Trail

Format (mới nhất lên đầu): `- [YYYY-MM-DD HH:mm:ss] [action-type] | Mô tả ngắn`

Action types: `[ingest]` `[task-update]` `[sync-daily]` `[lint-sync]` `[test-progress]` `[test-run]` `[test-blocked]` `[create]`

### 4.4 Changelog (trong feature/API Spec/test suite)

Format bảng (mới nhất lên đầu): `| YYYY-MM-DD HH:mm:ss | vX.X | Nội dung | Nguồn-link |`
Nguồn phải là link rõ: Task ID, Daily Note, hoặc tên file PDF.

### 4.5 Git

Sau mỗi batch xử lý: chạy `git status`. Commit nhỏ, message rõ nghiệp vụ:
- `docs: update feature spec for CR-X`
- `test: add regression cases for BUG-X`

Không sửa file ngoài phạm vi yêu cầu. Chỉ push khi người dùng yêu cầu.

### 4.6 Update Propagation Checklist

Khi có thay đổi requirement/task/TC, cập nhật đủ các nơi:
- `raw_sources/[p]/...` — lưu raw mới nếu có
  - Hasaki: raw file lưu theo HSK code (`HSK-xxxxx.md`), TBB2 embed bên trong — không tạo file riêng TBB2
  - Sau khi download HSK raw → KANBAN card (NEW) hoặc Impact Analysis (UPDATED) trước khi chạm wiki/
- `features/` — R/AC, Questions, Impact, Regression, Coverage, Changelog
- `api_specs/` — API contract, Questions, Coverage, Changelog (nếu API thay đổi)
- `feature_groups/` — nếu feature/spec/suite trong group bị ảnh hưởng
- `test_suites/` — add/update/deprecate TC, Blocked Coverage, Regression Impact, TC count, Changelog
- `test_plans/` — In-Scope, Regression Scope, Coverage nếu phạm vi thay đổi
- `KANBAN.md` — card + TC count
- `index.md` — thêm/xóa link
- `log.md` — 1 dòng audit với timestamp UTC+07
- `git status` — kiểm tra cuối batch, không revert file ngoài phạm vi
