---
tags: [wiki-rules, reference]
status: Done
updated: 2026-05-24
---

# Phase: Requirement Analysis & Ingest

> Dùng bởi: `/wiki-requirement-analyzer` — ingest PDF, import task HSK, xử lý task change.

---

## Cấu trúc thư mục chuẩn

```
llm-wiki/
├── index.md · KANBAN.md · log.md
├── raw_sources/[project]/{tasks/, requirements/, issues/, assets/}   ← CHỈ ĐỌC
├── templates/
└── wiki/[project]/
    ├── features/ · api_specs/ · feature_groups/
    ├── test_suites/ · test_plans/ · releases/
    ├── task_specs/
    ├── bugs_knowledge/
    └── operations/{environments.md · test_data.md · team_contacts.md · daily_notes/}
```

Project đang hoạt động: `project_hasaki`.

## Quy tắc đặt tên file

Tên file viết **thường, không dấu**, nối bằng `_`.

| Thư mục | Định dạng | Ví dụ |
|:--------|:----------|:------|
| `features/` | `[feature]_[mucnho].md` | `auth_login.md` |
| `api_specs/` | `api_[feature]_[mucnho].md` | `api_auth_login.md` |
| `feature_groups/` | `[feature_group].md` | `receiving_po.md` |
| `raw_sources/.../tasks/` | `HSK-xxxxx.md` | `HSK-12345.md` |

Mỗi `features/` file **phải có** test suite tương ứng. Nếu có API explicit → tạo thêm `api_specs/` và link 2 chiều.

**Tags bắt buộc:**
- `#qa/requirement` cho `features/`
- `#qa/api-spec` cho `api_specs/`
- `#qa/feature-group/[slug]` khi feature thuộc một group (slug dùng `-`, file dùng `_`)

## Phân loại task Hasaki

- `HSK-xxxxx` = task cha chứa requirement/implementation detail → nguồn chính phân tích Feature Spec.
- `TBB2-xxxxx` = test request liên kết với HSK cha qua `parent_id` → trigger để QA nhận việc test.
- Raw file lưu theo HSK code. TBB2 embed vào `## Test Requests (TBB2)` bên trong — không tạo file TBB2 riêng.
- Wiki impact check và KANBAN card dùng HSK code (không phải TBB2 code).

## Unreadable Source Rule

Khi raw source đề cập link/tài nguyên (Figma, URL, PDF phụ) **không thể truy cập**:
1. Ghi vào `## Nguồn tài liệu` với `Status = ❓ Chưa đọc được`.
2. Tạo câu hỏi `Open` trong `## ❓ Câu hỏi chưa rõ`: `"Link/file [X] được đề cập nhưng chưa đọc được — cần cung cấp [file/quyền]"`.
3. Không suy diễn nội dung từ link chưa đọc.

## Question Lifecycle

Bảng `## ❓ Câu hỏi chưa rõ`: `Q-ID | R/AC liên quan | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn | Ngày`

Trạng thái: `Open` / `Answered` / `Deferred`.
- R/AC còn `Open` liên quan trực tiếp → chặn sinh test case → ghi vào `Blocked Coverage`.
- Chỉ cập nhật Spec/TC khi câu hỏi `Answered` + có nguồn rõ.
- **Giá trị trông bất thường:** Khi raw ghi bất kỳ giá trị nào trông inconsistent với standard thông thường của loại dữ liệu đó — format string thiếu component, số ngưỡng không hợp lý, enum value không theo pattern của cùng nhóm, pattern/code trông như typo — mark `UNCLEAR`, thêm câu hỏi cho người có thẩm quyền. Không assume raw là correct khi giá trị trông bất thường; test data sai format hoặc sai ngưỡng sẽ không catch bug.

---

## Workflow 2.0: Khởi tạo dự án mới

**Kích hoạt:** Project chưa tồn tại hoặc user yêu cầu.

1. Tạo cấu trúc thư mục đầy đủ theo sơ đồ trên.
2. Khởi tạo 3 file operations: `environments.md`, `test_data.md`, `team_contacts.md`.
3. Cập nhật `index.md`, tạo Kanban cards khởi tạo Sprint, ghi log `[create]`.

---

## Workflow 2.1: Ingest PDF

**Kích hoạt:** File PDF mới trong `raw_sources/[project]/requirements/`.

**Bước 1 — Convert PDF:**
- Dùng MCP `markitdown/convert_to_markdown` → lưu `*_converted.md` cạnh PDF gốc trong `requirements/`.
- Không sửa raw PDF, không ghi đè file raw đã lưu.

**Bước 1b — Tạo Index JSON (bắt buộc sau convert):**

Tạo skeleton index bằng script trước, sau đó AI điền phần semantic:

```
$env:PYTHONUTF8 = "1"
py .claude/scripts/index_skeleton.py <path_to_converted.md> --version <ver>
```

Script tạo `{tên_file}_index.json` với `id`, `title`, `start_line`, `end_line` tự động. AI hoàn thiện phần còn lại:
- `topic_types`: liệt kê từ `[ui_filter, ui_listing, business_rule, state_transition, validation_rule, error_messages, formula, enum_values, api_contract, actor_flow]`
- `flags`: set `true` nếu section có enum list / state transition / formula / error messages / validation rule
- `mapped_feature`: để `null` khi mới tạo — điền sau khi có Feature Spec
- `coverage_status`: `unmapped` → cập nhật thành `full`/`partial`/`stub` khi tạo Feature Spec

Cập nhật `mapped_feature` và `coverage_status` ngay sau khi tạo xong mỗi Feature Spec.

**Bước 2 — Feature Spec (Bước A — ISTQB Test Analysis):**

**2a — Đọc raw (bắt buộc trước khi viết):**
- Đọc TOC → lập danh sách sections cần cover → đọc hết từng section → mới viết spec cho section đó.
- **Không viết spec khi chưa đọc xong section.** Doc >50 trang: đọc từng phần, set `partial_read: true` cho feature chưa đọc đủ.
- Với mọi field có danh sách values ("Giá trị:", "Value:", enum): grep raw đếm đủ values, ghi `#line` reference trước khi claim SUPPORTED.
- Đọc 2-3 dòng context sau mỗi field definition — notes nhỏ (navigation, business rule) thường nằm ở đây.

**2b — Viết spec:**
- Trùng cũ → Diff, cập nhật Spec, ghi Changelog.
- Mới → Tạo `[feature]_[mucnho].md` trong `features/` dùng `tpl_requirement.md`, phân rã R-IDs, vạch flows, status `Draft`.
- **Stub (`partial_read: true`):** Phải có đủ 14 mục bắt buộc (theo `tpl_requirement.md`) — chỉ nội dung bên trong được thay bằng placeholder `> Chưa đủ dữ liệu — STUB, cần đọc trang [X–Y] của raw source`. Section headers không được bỏ qua. Cấu trúc template là bất biến bất kể đã đọc được bao nhiêu raw source — nội dung có thể Blocked, headers thì không.
- Source column trong bảng Requirement: dùng format `[doc_name]#[line]` (ví dụ: `07062#234-239`).
- Nếu có API explicit → tạo `api_specs/api_[feature]_[mucnho].md` dùng `tpl_api_spec.md`; chưa rõ endpoint/payload → ghi câu hỏi, không suy diễn.
- **Verify trước Gate 1:** Chạy `hasaki-skill-refiner` để verify batch. Gate 1 chỉ proceed khi refiner verdict ≠ `FAIL`.
- **🤝 Gate 1A:** Trình bày các Feature Spec `partial_read: false` cho PO/QA Lead duyệt. Specs đầy đủ tiến sang Test Design — không cần chờ STUB.
- **🤝 Gate 1B:** Khi hoàn thiện từng STUB spec → Gate 1 riêng cho spec đó. Không gộp với Gate 1A.

**Bước 3:** Thêm card Kanban `## TODO`, ghi log `[ingest]`.

---

## Workflow 2.1b: Ingest version mới (Incremental Update)

**Kích hoạt:** File raw source có version mới hơn `source_version` trong index JSON hiện tại.

**Bước 1 — Phát hiện thay đổi:**
- So sánh `source_version` trong `{tên_file}_index.json` với version ghi trong Revision History của file MD mới.
- Nếu giống nhau → không cần update.
- Nếu khác → đọc Revision History section (thường nằm trong ~150 dòng đầu file).

**Bước 2 — Xác định vùng bị ảnh hưởng:**
- Lấy tất cả entries mới trong Revision History kể từ `last_full_index_version`.
- Mỗi entry mô tả trang/tính năng bị ảnh hưởng → map về section ID trong index.
- Với mỗi section bị ảnh hưởng, xác định loại thay đổi:

| Loại thay đổi | Hành động với index |
|:-------------|:--------------------|
| Thêm section mới | Thêm entry mới, `coverage_status: "unmapped"`, `change_history: [new_version]` |
| Xóa section | Đổi `coverage_status: "deleted"` — giữ lại để audit |
| Sửa nội dung | Đổi `coverage_status: "partial"`, cập nhật `change_history` |
| Thêm content làm lệch line | Tính offset → cộng vào `start_line`/`end_line` các sections phía dưới |

**Bước 3 — Patch index JSON (không rebuild):**
- Cập nhật `source_version` và `indexed_at`.
- Cập nhật `last_full_index_version` = version cũ (giữ lại để biết base).
- Với sections không bị ảnh hưởng: giữ nguyên `last_verified_version` và `coverage_status`.
- Với sections bị ảnh hưởng: cập nhật `last_verified_version: null`, thêm version mới vào `change_history`.

**Bước 4 — Chỉ update Feature Spec bị ảnh hưởng:**
- Sections có `coverage_status: "partial"/"unmapped"` → cập nhật Feature Spec tương ứng.
- Sections có `coverage_status: "full"` và `last_verified_version` = version cũ → skip, không cần re-verify.
- Ghi Changelog trong Feature Spec với version source mới.
- **🤝 Gate 1:** Chờ PO/QA Lead duyệt lại chỉ những phần thay đổi.

---

## Workflow 2.2: Task Change

**Kích hoạt:** User cung cấp Task/Jira ticket có thay đổi requirement; hoặc `/get-my-tasks` phát hiện HSK có `updated_at` thay đổi.

**Bước 1 — Impact Analysis:**
- Đọc `index.md` định vị file liên quan. Quét `features/`, `api_specs/`, `test_suites/` xác định vùng bị ảnh hưởng.
- Ghi bảng Impact Analysis trước khi sửa:
  `Change ID | Change type (Add/Update/Remove/Clarify) | Affected R/AC | Affected Features | Affected API Specs | Affected Test Suites | TC action | Regression candidates | Open questions/Gate`

**Bước 2 — Clarification (HITL Gate A):**
- Soạn câu hỏi phân loại theo đối tượng (PO: nghiệp vụ; Dev Lead: kỹ thuật).
- **🤝 Dừng chờ phản hồi.** Không phỏng đoán nghiệp vụ.

**Bước 3 — Cập nhật (Gate 1 → Gate 2):**
- Nhận câu trả lời → cập nhật Feature Spec + API Spec, đổi status về `Draft`, ghi Changelog kèm mã Task.
- **🤝 Gate 1:** User ký duyệt Spec. Sau Gate 1 → gọi `/wiki-test-designer`.
- TC cũ hết hiệu lực → chuyển vào `Deprecated`, không xóa. Cập nhật `Regression Impact`.
- Di chuyển card Kanban → `## InProgress`, ghi log `[task-update]`.

---

## Chuẩn viết Feature Spec (`features/`)

Dùng `tpl_requirement.md`. 14 mục bắt buộc:

1. YAML Frontmatter (`tags`, `status`, `feature`, `project`, `source_version`, `partial_read`)
2. Tổng quan (Feature, Mô tả, Source, Actors, Mối quan hệ nếu có)
3. Nguồn tài liệu (bảng PDF/Link + version + status)
4. API/Interface liên quan (chỉ link → API Spec, không nhúng contract)
5. Phân rã Requirement (bảng R-ID, loại, priority, testable, source với line reference `#line`)
6. User Flows (Pre-conditions, Happy Path, Alt-Flows, Exc-Flows)
7. Business Rules & Data Constraints (bảng validation)
8. Error Messages Map
9. Acceptance Criteria — BDD (Given-When-Then)
10. `## ❓ Câu hỏi chưa rõ` (bảng lifecycle)
11. Thay đổi vs version cũ (bảng Add/Update/Remove/Clarify)
12. Impact Analysis & Regression Proposal
13. Test Coverage (R → TC mapping, gồm blocked)
14. `## 📅 Changelog`

---

## Chuẩn viết API Spec (`api_specs/`)

Dùng `tpl_api_spec.md`. Các mục bắt buộc:
- Frontmatter: `tags: [qa/api-spec]`, `project`, `feature`, `feature_group`
- Tổng quan, API List (`API ID | Method | Endpoint | Mục đích | R/AC | Source | Status`)
- API Detail: auth, headers, params, request body, success/error response, side effects
- `## ❓ Câu hỏi API chưa rõ`, API Test Coverage, `## 📅 Changelog`

**Nguyên tắc:** Feature Spec = WHAT/WHY; API Spec = HOW contract. Nguồn không đề cập API → không tạo API Spec. Không suy diễn endpoint/payload/status code/error message/side effect.

---

## Reset-Ready Ingest Addendum (2026-05-27)

- Ngay sau khi ingest hoặc cập nhật feature spec, phải chạy `evidence-index` để đồng bộ machine-readable evidence.
- Requirement source không có `doc#line` hoặc `doc#line-line` là invalid cho Gate 1.
- Khi tạo mới feature spec, điền ngay các field:
  - `source_doc`
  - `source_range`
  - `last_verified_at`
  - `verification_status` (`Pending`/`Verified`/`Stale`)
- Nếu source chưa đủ rõ: giữ `coverage_status` ở `partial` hoặc `stub`; không nâng `full` bằng suy diễn.

## Reset-Ready Index Skeleton Notes (2026-05-27)

- `index_skeleton.py` now uses TOC dotted entries as the primary split source for converted PDF markdown.
- Footer/page-number handling must tolerate these cases:
  - same-line footer page number (`... POS 10`)
  - footer split across `Operation... Merchant,` and `POS 10`
  - standalone page number after footer
  - table-row page number after footer, but only as a low-confidence signal
- Low-confidence page numbers are repaired to the expected sequence when OCR/table extraction returns an impossible page jump.
- Body headings are intentionally narrow: `Update`, date update, `Case`, and `Web:` only. Generic bullets, table rows, OCR fragments, and uppercase table cells are not headings.
- Generated sections include `source_type`, `source_page`, `source_ref`, and `range_status` for traceability.

## Reset Baseline Notes (2026-05-27b)

- If project has just been reset, treat re-index output as structural baseline only.
- Before gate review, create minimum stub Feature Specs from TOC/index sections so evidence extraction can run.
- `evidence_index.json` with `records = 0` means ingest is not complete yet.
- Recommended immediate sequence after reset:
  1. Recreate `wiki/project_hasaki` folders
  2. Run `index_skeleton.py` for each requirement MD
  3. Create stub features with source references
  4. Run refiner

## Stub -> Full Spec Rule (2026-05-27c)

- After reset bootstrap, treat stubs as transition artifacts only.
- Required transition path:
  1. index from raw
  2. stub feature specs with source references
  3. refine stubs into full feature specs by domain
  4. run refiner and proceed Gate 1
- A batch with only stubs and no refinement log cannot be considered complete ingest.
