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
| `wiki/[project]/operations/environments.md` | Lấy URL, tài khoản test thực tế |
| `wiki/[project]/operations/test_data.md` | Lấy dữ liệu test mẫu (SĐT, thẻ, payload) |
| `wiki/[project]/bugs_knowledge/` | Bổ sung Regression TC từ lỗi cũ (nếu có) |

## Workflow bắt buộc

1. Xác nhận: project, feature, task/CR nguồn, và đường dẫn test suite đích.
2. Trích xuất tất cả Requirement IDs (`R1`, `R2`...) và BDD Acceptance Criteria từ Feature Spec.
3. Thiết kế coverage bằng các kỹ thuật ISTQB phù hợp:
   - `Happy Path`
   - `Equivalence Partitioning`
   - `Boundary Value Analysis`
   - `Decision Table`
   - `State Transition`
   - `Error Guessing`
   - `Security`
   - `Regression`
4. Tạo hoặc cập nhật `wiki/[project]/test_suites/test_[feature_name].md`.
5. Cập nhật `index.md`, `KANBAN.md`, `log.md` theo `WIKI_RULES.md`.
6. Chạy validation: `python .claude/scripts/wiki_sync.py verify`.

## Quy tắc bắt buộc cho mỗi dòng test case

Mỗi test case **BẮT BUỘC** có đủ các cột:

- **AC/Req Cover:** Requirement ID (`R1`, `R2`...) và/hoặc AC/BDD Scenario (`AC-01`, `Scenario 1`).
- **Loại case:** `Positive` hoặc `Negative`. Regression/security/performance vẫn phải ghi rõ.
- **Kỹ thuật test:** kỹ thuật ISTQB đã dùng.
- **Nguồn:** Chỉ dùng `Explicit từ [nguồn]`.
- Không ghi `AI-Inferred` trong test suite.
- **Status:** mặc định `⏳` cho test case mới.

**KHÔNG tạo test case không có nguồn.** Nếu thiếu nguồn → ghi vào câu hỏi cần làm rõ.

## Guardrails

- Tuân thủ **HITL Gate 2**: sau khi tạo Test Suite, dừng lại và trình bày cho QA Lead review. Chỉ chuyển sang `Testing` khi QA Lead đã duyệt.
- Không tự đánh `✅ Pass` mà không có xác nhận chạy test thực tế từ con người (Gate 4).

## Output tóm tắt

Sau khi hoàn thành, báo cáo:
- Đường dẫn Test Suite và trạng thái
- Tổng số test case (Positive / Negative)
- Kỹ thuật test đã dùng
- Coverage Requirement/AC
- Danh sách điểm chưa rõ đã chuyển về mục `## ❓ Câu hỏi chưa rõ` của Feature
- Kết quả `verify_wiki.py`
