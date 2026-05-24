---
description: "ISTQB Test Design — Thiết kế test cases/test suite có traceable từ Feature Spec đã duyệt trong wiki/[project]/test_suites/"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Wiki Test Designer

Bạn đang thực hiện **ISTQB Test Design**: quyết định **HOW to test** dựa trên Feature Spec đã được duyệt.

## Inputs bắt buộc — đọc trước khi viết bất kỳ test case nào

| File cần đọc | Mục đích |
|:-------------|:---------|
| `WIKI_RULES.md` | Tuân thủ format và quy tắc đặt tên |
| `templates/tpl_test_suite.md` | Giữ nguyên cấu trúc template |
| `wiki/[project]/features/[feature_name].md` | Lấy logic nghiệp vụ, luồng, ràng buộc dữ liệu |
| `wiki/[project]/api_specs/api_[feature_name].md` | Lấy method, endpoint, payload, response, error contract khi suite có phạm vi API |
| `wiki/[project]/operations/environments.md` | Lấy URL, tài khoản test thực tế |
| `wiki/[project]/operations/test_data.md` | Lấy dữ liệu test mẫu (SĐT, thẻ, payload) |
| `wiki/[project]/bugs_knowledge/` | Bổ sung Regression TC từ lỗi cũ (nếu có) |

## Workflow bắt buộc

1. Xác nhận: project, feature, task/CR nguồn, và đường dẫn test suite đích.
2. Xác nhận Feature Spec đã qua Gate 1: `status: Done` và có `approved_by`, `approved_at`, `approval_note`. Nếu chưa duyệt, chỉ được báo blocked, không sinh test case mới.
3. Trích xuất tất cả Requirement IDs (`R1`, `R2`...), BDD Acceptance Criteria và bảng `## ❓ Câu hỏi chưa rõ` từ Feature Spec. Nếu có API Spec được link hoặc người dùng yêu cầu API test, đọc thêm API Spec tương ứng.
4. Loại khỏi phạm vi sinh test mọi Requirement/AC/API còn câu hỏi `Open` liên quan trực tiếp. Ghi các mục này vào `Blocked Coverage`.
5. Thiết kế coverage bằng các kỹ thuật ISTQB phù hợp:
   - `Happy Path`
   - `Equivalence Partitioning`
   - `Boundary Value Analysis`
   - `Decision Table`
   - `State Transition`
   - `Error Guessing`
   - `Security`
   - `Regression`
6. Tạo hoặc cập nhật `wiki/[project]/test_suites/test_[feature_name].md`. Nếu chỉ cover API contract hoặc muốn tách rõ API suite, dùng `wiki/[project]/test_suites/test_[feature_name]_api.md`.
7. Khi update test suite, không xóa TC cũ; chuyển TC không còn áp dụng vào `Test Cases Lỗi Thời (Deprecated)`.
8. Nếu Test Suite có tag `qa/feature-group/...`, cập nhật `wiki/[project]/feature_groups/[feature_group].md` để group page phản ánh API Spec nếu có, số TC, blocked coverage và status mới.
9. Cập nhật `Regression Impact`, `index.md`, `KANBAN.md`, `log.md`, Test Plan liên quan theo `WIKI_RULES.md`.
10. Chạy validation: `python .claude/scripts/wiki_sync.py verify`.

## Quy tắc bắt buộc cho mỗi dòng test case

Mỗi test case **BẮT BUỘC** có đủ các cột:

- **AC/Req Cover:** Requirement ID (`R1`, `R2`...) và/hoặc AC/BDD Scenario (`AC-01`, `Scenario 1`).
- **Phạm vi:** `UI`, `API`, `Functional`, `UI+Functional`, `API+Functional`, `UI+API`, hoặc `E2E`.
- **Loại case:** `Positive` hoặc `Negative`. Regression/security/performance vẫn phải ghi rõ.
- **Kỹ thuật test:** kỹ thuật ISTQB đã dùng.
- **Nguồn:** Chỉ dùng `Explicit từ [nguồn]`.
- Không ghi `AI-Inferred` trong test suite.
- Không tạo TC từ question `Open`. Chỉ tạo TC từ question sau khi Feature Spec đã cập nhật câu trả lời `Answered` và AC/Requirement tương ứng đã rõ.
- Không tạo API TC nếu chưa có API Spec explicit hoặc câu trả lời `Answered` nêu rõ API ID/method/endpoint/payload/response/status/error. Nếu API contract còn thiếu, ghi vào API Spec Questions và `Blocked Coverage`.
- **Status:** mặc định `⏳` cho test case mới.

**KHÔNG tạo test case không có nguồn.** Nếu thiếu nguồn hoặc còn mơ hồ → ghi vào `Blocked Coverage` và/hoặc câu hỏi cần làm rõ trong Feature/API Spec.

## Guardrails

- Tuân thủ **HITL Gate 2**: sau khi tạo Test Suite, dừng lại và trình bày cho QA Lead review. Chỉ chuyển sang `Testing` khi QA Lead đã duyệt.
- Không tự đánh `✅ Pass` mà không có xác nhận chạy test thực tế từ con người (Gate 4).

## Output tóm tắt

Sau khi hoàn thành, báo cáo:
- Đường dẫn Test Suite và trạng thái
- Tổng số test case (Positive / Negative)
- Phân bố test theo phạm vi (`UI` / `API` / `Functional` / `UI+Functional` / `API+Functional` / `UI+API` / `E2E`)
- Kỹ thuật test đã dùng
- Coverage Requirement/AC
- Danh sách điểm chưa rõ đã chuyển về mục `## ❓ Câu hỏi chưa rõ` của Feature
- Danh sách API questions chưa rõ đã chuyển về API Spec nếu có
- Blocked Coverage do câu hỏi mở
- Regression Impact nếu là update
- Feature Group page đã cập nhật nếu có tag group
- Kết quả `python .claude/scripts/wiki_sync.py verify`
