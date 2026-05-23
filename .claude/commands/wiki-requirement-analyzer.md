---
description: "ISTQB Test Analysis — Phân tích requirement từ raw_sources và tạo/cập nhật Feature Spec trong wiki/[project]/features/"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Wiki Requirement Analyzer

Bạn đang thực hiện **ISTQB Test Analysis**: quyết định **WHAT to test** trước khi thiết kế test case.

## Workflow bắt buộc

1. Đọc `WIKI_RULES.md`, `USER_COMMANDS.md`, và raw source liên quan trong `raw_sources/`.
2. Xác định project đích. Nếu không rõ project → hỏi người dùng trước khi tạo file.
3. Đọc `templates/tpl_requirement.md` và giữ nguyên cấu trúc template.
4. Tạo hoặc cập nhật `wiki/[project]/features/[feature_name].md`.
5. Viết Feature Spec đầy đủ theo chuẩn:
   - **YAML frontmatter:** `tags: [qa/requirement]`, `status: Draft`, `project`, `feature`, `source_version`.
   - **Requirement IDs:** `R1`, `R2`, `R3`...
   - **User Flows:** Happy Path, Alternative Paths, Exception Paths.
   - **Business rules**, validation rules, error message map.
   - **BDD Acceptance Criteria** (Given-When-Then) mà wiki-test-designer sẽ cover sau.
   - **Câu hỏi làm rõ** cho các điểm mập mờ từ PO/Dev.
   - **Changelog** mới nhất lên đầu.
6. Cập nhật `index.md`, `KANBAN.md`, `log.md` theo đúng quy tắc trong `WIKI_RULES.md`.

## Guardrails

- **KHÔNG viết test case** trong skill này. Chỉ viết Feature Spec. Chuyển sang `wiki-test-designer` SAU khi Spec được duyệt.
- **KHÔNG tự chốt nghiệp vụ** khi còn điểm mập mờ — ghi vào mục "Câu hỏi chưa rõ".
- **KHÔNG suy diễn requirement/AC** nếu nguồn chưa mô tả rõ. Chỉ ghi thông tin explicit từ tài liệu gốc.
- **KHÔNG sửa file trong `raw_sources/`** — chỉ đọc.
- Mọi Requirement ID phải truy ngược về tài liệu nguồn hoặc ghi rõ là assumption.
- Tuân thủ **HITL Gate 1**: sau khi tạo Spec, dừng lại và trình bày cho PO/QA Lead duyệt. Không tiếp tục sang thiết kế test nếu chưa có approval.

## Output tóm tắt

Sau khi hoàn thành, báo cáo:
- Đường dẫn Feature Spec và trạng thái
- Danh sách Requirement IDs đã trích xuất
- Số lượng Acceptance Criteria
- Câu hỏi chưa giải quyết
- Các file đã cập nhật
