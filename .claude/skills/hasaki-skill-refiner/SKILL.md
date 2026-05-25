---
name: hasaki-skill-refiner
description: Vòng lặp tự cải tiến cho skill Hasaki bằng cách đối soát raw sources với spec/test đã tạo và chỉ giữ thay đổi khi vượt quality gates.
---

# Hasaki Skill Refiner

## Mục tiêu
Tạo vòng lặp self-improve cho các skill Hasaki bằng cách đối soát `raw_sources` với nội dung đã tạo trong `wiki`, sau đó đề xuất sửa skill/rule/template có kiểm soát.

## Dùng skill này khi nào
- Muốn giảm lỗi lặp lại sau mỗi đợt chạy `/import-hasaki-task` -> `/wiki-requirement-analyzer` -> `/wiki-test-designer`.
- Muốn nâng chất lượng theo metric thay vì đánh giá cảm tính.
- Muốn cập nhật skill cũ nhưng vẫn giữ no-inference guardrails.

## Đầu vào bắt buộc
- Snapshot raw task source trong `raw_sources/project_hasaki/tasks/`.
- File đã tạo/cập nhật trong `wiki/project_hasaki/` (Task Spec, Feature Spec, test suite, traceability).
- Rule hiện hành: `WIKI_RULES.md`, `.Codex/rules/*.md`, và các `SKILL.md` liên quan.

## Vòng lặp cải tiến
1. Thu thập cặp đối soát Raw Evidence -> Wiki Claim theo từng requirement/AC/testcase.
2. Đánh dấu từng claim:
- `SUPPORTED`: truy ngược được về bằng chứng explicit trong raw.
- `UNCLEAR`: raw chưa rõ; phải đưa vào `Câu hỏi chưa rõ`.
- `INFERRED`: không có bằng chứng; không được để ở mô tả chính.
3. Chạy quality gates:
- `NO_INFERENCE_PASS`: không còn claim inferred trong phần chính.
- `QUESTION_ROUTING_PASS`: tất cả unclear item nằm ở `Câu hỏi chưa rõ`.
- `BLOCKED_COVERAGE_PASS`: nội dung dựa trên open question nằm trong `Blocked Coverage`.
- `TRACEABILITY_PASS`: giữ đủ chuỗi `TBB2 -> HSK -> Task Spec -> Feature Spec -> Requirement/AC -> Testcase`.
- `UTF8_PASS`: file Markdown/JSON UTF-8, không mojibake.
- `VERIFY_PASS`: `python .Codex/scripts/wiki_sync.py verify` pass.
4. Phân tích root cause theo nhóm:
- Rule thiếu/chưa rõ.
- Skill instruction chưa đầy đủ.
- Template thiếu cột traceability/question.
- Command flow thiếu gate trước khi finalize.
5. Đề xuất patch tối thiểu (minimal) vào skill/rule/template.
6. Keep/Discard:
- Chỉ giữ thay đổi khi tổng điểm tăng và không vi phạm gate bắt buộc.
- Nếu fail gate bắt buộc, discard đề xuất và ghi bài học vào retrospective.

## Output chuẩn
- `wiki/project_hasaki/reports/self_improve/retrospective.md`
- `wiki/project_hasaki/reports/self_improve/improvement_patch_plan.md`
- `wiki/project_hasaki/reports/self_improve/quality_gates.json`
- `wiki/project_hasaki/reports/self_improve/evidence_matrix.md`

## Format bảng Evidence Matrix
Dùng bảng sau trong `evidence_matrix.md`:

| Raw Evidence (path#line) | Wiki Claim (path#line) | Status | Action |
| --- | --- | --- | --- |
| ... | ... | SUPPORTED/UNCLEAR/INFERRED | Keep/Move to Question/Remove |

## Scoring (ví dụ)
- Bắt buộc: `NO_INFERENCE_PASS`, `TRACEABILITY_PASS`, `VERIFY_PASS`.
- Điểm tổng: 100
- Cộng điểm khi giảm `INFERRED`, tăng tỷ lệ testcase map explicit AC, giảm số blocked item bị đặt sai vị trí.
- Trừ điểm mạnh nếu có vi phạm gate bắt buộc.

## Hard guardrails
- Không suy diễn requirement, AC, API contract, testcase.
- Không đưa thông tin chưa rõ vào mô tả chính; đưa vào `Câu hỏi chưa rõ`.
- Testcase chỉ sinh từ requirement/AC explicit.
- Nội dung dựa trên open question phải nằm ở `Blocked Coverage`.
- Không auto-merge patch nếu chưa pass quality gates.

## Tần suất chạy gợi ý
- Chạy sau mỗi batch import task mới.
- Chạy lại sau khi sửa skill/rule lớn.
- Chạy regression hằng tuần cho 3-5 task đại diện.

## Done criteria
- Có đủ 4 artifact output.
- Tất cả gate bắt buộc pass.
- Patch plan rõ file cần sửa + lý do + expected impact.
- Bài học được ghi để tái sử dụng ở lần chạy sau.
