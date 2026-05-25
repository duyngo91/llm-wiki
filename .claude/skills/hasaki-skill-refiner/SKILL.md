---
name: hasaki-skill-refiner
description: Vòng lặp tự cải tiến cho skill Hasaki bằng cách đối soát raw sources với spec/test đã tạo và chỉ giữ thay đổi khi vượt quality gates. Chạy sau mỗi batch import task hoặc khi muốn giảm lỗi lặp lại.
---

# Hasaki Skill Refiner

## Mục tiêu
Tạo vòng lặp self-improve cho các skill Hasaki bằng cách đối soát `raw_sources` với nội dung đã tạo trong `wiki`, sau đó đề xuất sửa skill/rule/template có kiểm soát.

## Dùng skill này khi nào
- Muốn giảm lỗi lặp lại sau mỗi đợt chạy `/import-hasaki-task` -> `/wiki-requirement-analyzer` -> `/wiki-test-designer`.
- Muốn nâng chất lượng theo metric thay vì đánh giá cảm tính.
- Muốn cập nhật skill cũ nhưng vẫn giữ no-inference guardrails.

## Đầu vào bắt buộc
- Raw source trong `raw_sources/project_hasaki/` — có thể là `tasks/` (HSK task export) hoặc `requirements/` (PDF converted).
- File đã tạo/cập nhật trong `wiki/project_hasaki/` (Task Spec, Feature Spec, test suite, traceability).
- Rule hiện hành: `.claude/rules/*.md` và các `SKILL.md` liên quan.

## Vòng lặp cải tiến

### Bước 1 — Xác định phạm vi đối soát

**Với spec đầy đủ (`partial_read: false`):** Đối soát tất cả Requirement và AC.

**Với stub spec (`partial_read: true`):** Chỉ verify phần đã đọc — KHÔNG tạo claim cho phần chưa đọc. Ghi rõ trong evidence_matrix: `"[STUB — chưa verify phần chưa đọc]"`.

**Sampling cho doc lớn (>50 trang raw):** Ưu tiên verify:
1. Mọi claim có enum/list values (rủi ro cao nhất).
2. Mọi claim trong phần Business Rules & Validation.
3. 20% ngẫu nhiên các claim còn lại.

### Bước 2 — Thu thập cặp đối soát Raw Evidence → Wiki Claim

**Kỹ thuật thu thập:**
- Với mọi claim có enum/list values: grep `Giá trị:` / `Value:` trong raw → so sánh count với claim. Nếu count khác → INFERRED.
- Đọc 2-3 dòng context sau mỗi field definition trong raw để bắt notes nhỏ (navigation, business rule phụ).
- Verify Source `#line` reference: nếu claim không có line → tìm lại raw, bổ sung. Không có anchor = không verify được.
- Filter table và mapping table của cùng feature có thể có số values khác nhau — verify riêng từng bảng.

### Bước 3 — Đánh dấu từng claim

- `SUPPORTED`: truy ngược được về bằng chứng explicit trong raw, có `#line`.
- `UNCLEAR`: raw chưa rõ hoặc section boundary mơ hồ (PDF converted); phải đưa vào `Câu hỏi chưa rõ`.
- `INFERRED`: không có bằng chứng hoặc enum thiếu values; không được để ở mô tả chính.
- `MISSING_DETAIL`: claim đúng nhưng thiếu detail/note từ raw (navigation, side effect nhỏ).

### Bước 4 — Chạy quality gates

- `NO_INFERENCE_PASS`: không còn claim INFERRED trong phần chính.
- `QUESTION_ROUTING_PASS`: tất cả UNCLEAR item nằm ở `Câu hỏi chưa rõ`.
- `BLOCKED_COVERAGE_PASS`: nội dung dựa trên open question nằm trong `Blocked Coverage`.
- `TRACEABILITY_PASS`: giữ đủ chuỗi `TBB2 -> HSK -> Task Spec -> Feature Spec -> Requirement/AC -> Testcase`.
- `UTF8_PASS`: file Markdown/JSON UTF-8, không mojibake.
- `VERIFY_PASS`: chạy `$env:PYTHONUTF8 = "1"; py .claude/scripts/wiki_sync.py verify` (Windows) — phải pass.

Sau khi fix lỗi: tính lại score và ghi vào `quality_gates.json` với `score_before` / `score_after`.

### Bước 5 — Phân tích root cause theo nhóm

- Rule thiếu/chưa rõ → đề xuất patch `.claude/rules/*.md`.
- Skill instruction chưa đầy đủ → đề xuất patch `SKILL.md`.
- Template thiếu cột traceability/question → đề xuất patch `templates/`.
- Command flow thiếu gate trước khi finalize.

### Bước 6 — Đề xuất patch tối thiểu (minimal)

Mỗi patch ghi rõ: file cần sửa + nội dung thay đổi + lý do + expected impact.

### Bước 7 — Keep/Discard

- Chỉ giữ thay đổi khi tổng điểm tăng và không vi phạm gate bắt buộc.
- Nếu fail gate bắt buộc, discard đề xuất và ghi bài học vào retrospective.
- Sau khi apply patch: cập nhật trạng thái patch trong `improvement_patch_plan.md` từ `Pending` → `Done`.

## Output chuẩn
- `wiki/project_hasaki/reports/self_improve/retrospective.md`
- `wiki/project_hasaki/reports/self_improve/improvement_patch_plan.md`
- `wiki/project_hasaki/reports/self_improve/quality_gates.json`
- `wiki/project_hasaki/reports/self_improve/evidence_matrix.md`

## Format bảng Evidence Matrix

```
| Raw Evidence (path#line) | Wiki Claim (path#line) | Status | Action |
| --- | --- | --- | --- |
| ... | ... | SUPPORTED/UNCLEAR/INFERRED/MISSING_DETAIL | Keep/Move to Question/Remove/Add detail |
```

Stub specs: thêm dòng `| [STUB] | [phần chưa đọc] | — | Không verify |` để đánh dấu vùng không thể kiểm.

## Format quality_gates.json

```json
{
  "session": "YYYY-MM-DD",
  "score_before": 0,
  "score_after": 0,
  "gates": {
    "NO_INFERENCE_PASS": true,
    "QUESTION_ROUTING_PASS": true,
    "BLOCKED_COVERAGE_PASS": true,
    "TRACEABILITY_PASS": true,
    "UTF8_PASS": true,
    "VERIFY_PASS": true
  },
  "violations": [],
  "notes": ""
}
```

## Scoring
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
- `quality_gates.json` có cả `score_before` và `score_after`.
- Patch plan rõ file cần sửa + lý do + expected impact, trạng thái cập nhật (Pending/Done).
- Bài học được ghi để tái sử dụng ở lần chạy sau.
