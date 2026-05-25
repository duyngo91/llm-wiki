---
description: "ISTQB Test Analysis — Phân tích requirement từ raw_sources và tạo/cập nhật Feature Spec trong wiki/[project]/features/ và API Spec trong wiki/[project]/api_specs/ nếu có API explicit"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Wiki Requirement Analyzer

Bạn đang thực hiện **ISTQB Test Analysis**: quyết định **WHAT to test** trước khi thiết kế test case.

## Workflow bắt buộc

1. Đọc `.claude/skills/hasaki-wiki/references/phase_ingest.md`, sau đó đọc raw source liên quan trong `raw_sources/`.
2. Xác định project đích. Nếu không rõ project → hỏi người dùng trước khi tạo file.
3. Đọc `templates/tpl_requirement.md`; nếu raw source có API/interface explicit thì đọc thêm `templates/tpl_api_spec.md`.
4. Tạo hoặc cập nhật `wiki/[project]/features/[feature_name].md`.
5. Viết Feature Spec đầy đủ theo chuẩn:
   - **YAML frontmatter:** `tags: [qa/requirement]`, `status: Draft`, `project`, `feature`, `source_version`.
   - **Requirement IDs:** `R1`, `R2`, `R3`...
   - **User Flows:** Happy Path, Alternative Paths, Exception Paths.
   - **Business rules**, validation rules, error message map.
   - **BDD Acceptance Criteria** (Given-When-Then) mà wiki-test-designer sẽ cover sau.
   - **Câu hỏi làm rõ** theo bảng lifecycle: `Q-ID`, R/AC liên quan, trạng thái `Open/Answered/Deferred`, câu trả lời, nguồn trả lời.
   - **Impact Analysis & Regression Proposal** khi đây là update từ task/change request.
   - **Changelog** mới nhất lên đầu.
6. Nếu raw source có API/interface explicit, tạo hoặc cập nhật `wiki/[project]/api_specs/api_[feature_name].md`:
   - Chỉ ghi method, endpoint, auth, header, request, response, status code, error message và side effect khi source nêu rõ.
   - Nếu thiếu chi tiết contract, ghi vào `## ❓ Câu hỏi API chưa rõ` thay vì suy diễn theo convention REST.
   - Link API Spec từ Feature Spec và link ngược về Feature/Feature Group.
7. Nếu raw source là PDF đã convert, lưu/tham chiếu bản AI-readable markdown trong `raw_sources/[project]/requirements/`.
8. Nếu Feature có tag `qa/feature-group/...`, cập nhật hoặc tạo `wiki/[project]/feature_groups/[feature_group].md` để group page link tới Feature Spec, API Spec nếu có, và Test Suite liên quan.
9. Cập nhật `index.md`, `KANBAN.md`, `log.md`, Test Plan liên quan theo đúng Update Propagation Checklist trong `.claude/skills/hasaki-wiki/references/phase_sync.md`.

## Guardrails

- **KHÔNG viết test case** trong skill này. Chỉ viết Feature Spec. Chuyển sang `wiki-test-designer` SAU khi Spec được duyệt.
- **KHÔNG tự chốt nghiệp vụ** khi còn điểm mập mờ — ghi vào mục "Câu hỏi chưa rõ".
- **KHÔNG suy diễn requirement/AC** nếu nguồn chưa mô tả rõ. Chỉ ghi thông tin explicit từ tài liệu gốc.
- **Link/tài nguyên không đọc được:** Khi raw source đề cập link (Figma, URL, PDF phụ) mà không truy cập được, phải ghi vào bảng `## Nguồn tài liệu` với Status = `❓ Chưa đọc được` VÀ tạo câu hỏi Open: `"Link [X] chưa đọc được — cần cung cấp file/quyền truy cập"`. Không suy diễn nội dung từ link chưa đọc.
- **KHÔNG suy diễn API contract** nếu nguồn chưa mô tả rõ method/endpoint/payload/status/error. Chỉ tạo câu hỏi API.
- **KHÔNG sửa file trong `raw_sources/`** — chỉ đọc.
- Mọi Requirement ID phải truy ngược về tài liệu nguồn hoặc câu trả lời chính thức đã `Answered`. Không ghi `assumption`.
- Nếu có behavior tiềm năng nhưng chưa rõ, không tạo Requirement/AC; ghi thành Question `Open`.
- Tuân thủ **HITL Gate 1**: sau khi tạo Spec, dừng lại và trình bày cho PO/QA Lead duyệt. Không tiếp tục sang thiết kế test nếu chưa có approval.

## Output tóm tắt

Sau khi hoàn thành, báo cáo:
- Đường dẫn Feature Spec và trạng thái
- Đường dẫn API Spec và trạng thái nếu có API/interface explicit
- Danh sách Requirement IDs đã trích xuất
- Số lượng Acceptance Criteria
- Câu hỏi chưa giải quyết
- Impact Analysis / Regression Proposal nếu là update
- Feature Group page đã cập nhật nếu có tag group
- API questions chưa rõ nếu có
- Các file đã cập nhật
