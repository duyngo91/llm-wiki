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

**Bước 2 — Feature Spec (Bước A — ISTQB Test Analysis):**

**2a — Đọc raw (bắt buộc trước khi viết):**
- Đọc TOC → lập danh sách sections cần cover → đọc hết từng section → mới viết spec cho section đó.
- **Không viết spec khi chưa đọc xong section.** Doc >50 trang: đọc từng phần, set `partial_read: true` cho feature chưa đọc đủ.
- Với mọi field có danh sách values ("Giá trị:", "Value:", enum): grep raw đếm đủ values, ghi `#line` reference trước khi claim SUPPORTED.
- Đọc 2-3 dòng context sau mỗi field definition — notes nhỏ (navigation, business rule) thường nằm ở đây.

**2b — Viết spec:**
- Trùng cũ → Diff, cập nhật Spec, ghi Changelog.
- Mới → Tạo `[feature]_[mucnho].md` trong `features/` dùng `tpl_requirement.md`, phân rã R-IDs, vạch flows, status `Draft`.
- Source column trong bảng Requirement: dùng format `[doc_name]#[line]` (ví dụ: `07062#234-239`).
- Nếu có API explicit → tạo `api_specs/api_[feature]_[mucnho].md` dùng `tpl_api_spec.md`; chưa rõ endpoint/payload → ghi câu hỏi, không suy diễn.
- **🤝 Gate 1:** Dừng, trình bày Spec cho PO/QA Lead. Chờ duyệt trước khi sang Test Design.

**Bước 3:** Thêm card Kanban `## TODO`, ghi log `[ingest]`.

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
