---
name: hasaki-skill-refiner
description: Vòng lặp QA kiểm chứng ngược cho wiki Hasaki — đối soát wiki claims vs raw sources, chạy quality gates, và đề xuất patch skill/rule/template. Chạy sau mỗi batch import hoặc khi phát hiện lỗi lặp lại. Hai phase độc lập: Phase A (verify batch hiện tại) và Phase B (meta-improve khi có pattern lỗi).
---

# Hasaki Skill Refiner

## Mục tiêu

Kiểm chứng ngược từng claim trong wiki so với raw source, phát hiện lỗi suy diễn (INFERRED, LOGIC_INFERRED) và thiếu chi tiết (MISSING_DETAIL), sau đó đề xuất patch có kiểm soát vào skills/rules/templates.

---

## Hai phase độc lập

| Phase | Chạy khi nào | Thời gian ước tính |
|:------|:-------------|:-------------------|
| **Phase A — Verify** | Sau mỗi batch import/ingest | 20–40 phút |
| **Phase B — Meta-improve** | Khi cùng một loại lỗi xuất hiện ≥ 2 lần | 30–60 phút |

Có thể chạy Phase A đơn lẻ (verify nhanh). Phase B chỉ cần chạy khi Phase A liên tục báo cùng loại vấn đề — đây là dấu hiệu skill/rule cần sửa, không phải lỗi thực thi đơn lẻ.

---

## Đầu vào bắt buộc

- Raw source trong `raw_sources/project_hasaki/` — `tasks/` (HSK export) hoặc `requirements/` (PDF converted).
- File wiki đã tạo/cập nhật trong `wiki/project_hasaki/` (Feature Spec, Task Spec, test suite).
- Rule hiện hành: `.claude/rules/*.md` và `SKILL.md` liên quan.

---

## Phase A — Verify

### A1. Xác định phạm vi đối soát

**Spec đầy đủ (`partial_read: false`):** Verify tất cả Requirement và AC.

**Stub spec (`partial_read: true`):** Chỉ verify phần đã đọc. Đánh dấu phần chưa đọc trong evidence_matrix:
```
| [STUB — section chưa đọc] | — | — | Không verify |
```

**Sampling cho doc lớn (raw source > 50 trang):** Verify theo thứ tự ưu tiên sau:
1. **Toàn bộ** claim có enum/list values — đây là nguồn lỗi phổ biến nhất.
2. **Toàn bộ** claim trong Business Rules & Validation.
3. **Cứ mỗi 5 requirement, chọn 1** từ các claim còn lại (bắt đầu từ R1, lấy R1, R6, R11, ...) — quy tắc này tái lặp được.

### A2. Thu thập cặp đối soát (đọc theo thứ tự này)

**Bước 1 — Đọc Feature Spec trước:** Liệt kê tất cả claim cần verify (mỗi dòng trong bảng Requirement, mỗi Business Rule, mỗi AC, mỗi Error Message).

**Bước 2 — Grep raw cho từng claim:**
- Enum/list values: grep `Giá trị:` / `Value:` / `status:` trong raw → đếm values → so sánh với claim. Nếu count khác → `INFERRED`.
- Filter table và mapping table của cùng feature có thể có số values khác nhau — verify riêng từng bảng.
- Đọc 2–3 dòng context sau mỗi field definition — notes nhỏ (navigation, side effect) thường nằm ở đây.
- Verify `#line` reference: không có anchor = không verify được → bổ sung line hoặc đánh dấu `UNCLEAR`.

**Kiểm tra đặc biệt cho claim mô tả hành vi hệ thống (behavior claims):**

Claim mô tả *hành vi* (auto-transition, trigger, validation rule, side effect, điều kiện bật/tắt) dễ bị `LOGIC_INFERRED` — tức là LLM ghép hai sự kiện thật lại và tự rút ra kết luận không được raw nêu.

Quy trình verify behavior claim:
1. Tìm câu raw nêu **đúng hành vi đó** (không phải chỉ tìm các thành phần liên quan).
2. Nếu chỉ tìm được thành phần (field A tồn tại + button B tồn tại) nhưng không có câu nào nối chúng → đánh dấu `LOGIC_INFERRED`.
3. Nếu có câu raw nhưng nằm ở section khác → kiểm tra context, đọc heading của section đó trước khi accept.

Ví dụ phân biệt:
- Raw#45: "Status: Received" + Raw#89: "button Save" → claim "khi Save, Status → Received": **LOGIC_INFERRED** (không có câu nào nối).
- Raw#112: "Nhấn Save → hệ thống cập nhật Status = Received" → claim trên: **SUPPORTED**.

**Không đọc raw trước rồi mới đọc spec** — hướng ngược lại dễ bỏ sót claim không có trong raw.

### A3. Đánh dấu từng claim

| Label | Định nghĩa | Hành động |
|:------|:-----------|:----------|
| `SUPPORTED` | Có bằng chứng explicit trong raw, có `#line` | Keep |
| `UNCLEAR` | Raw chưa rõ hoặc section boundary mơ hồ (PDF) | Move to Câu hỏi chưa rõ |
| `INFERRED` | Không có bằng chứng nào cả, hoặc enum thiếu values | Remove khỏi mô tả chính |
| `LOGIC_INFERRED` | Bằng chứng có thật nhưng kết luận không được raw nêu rõ — LLM tự ghép logic | Remove khỏi mô tả chính (nguy hiểm hơn INFERRED vì khó phát hiện) |
| `MISSING_DETAIL` | Claim đúng nhưng thiếu note/side effect từ raw | Add detail |

> `LOGIC_INFERRED` thường xuất hiện ở: auto-transition trạng thái, validation rule tự suy ra, trigger/side effect, điều kiện enable/disable field. Khi thấy claim dạng này — luôn hỏi: *"Raw có câu nào nói điều này không, hay tôi đang ghép A + B?"*

### A4. Chạy quality gates

Chạy theo thứ tự — gate bắt buộc (🔴) fail → dừng, không tính score.

| Gate | Bắt buộc | Kiểm tra |
|:-----|:---------|:---------|
| `NO_INFERENCE_PASS` | 🔴 | Không còn claim `INFERRED` hoặc `LOGIC_INFERRED` trong phần mô tả chính |
| `TRACEABILITY_PASS` | 🔴 | Xem bảng traceability theo giai đoạn bên dưới |
| `VERIFY_PASS` | 🔴 | `$env:PYTHONUTF8 = "1"; py .claude/scripts/wiki_sync.py verify` pass |
| `QUESTION_ROUTING_PASS` | 🟡 | Tất cả UNCLEAR nằm đúng section `## ❓ Câu hỏi chưa rõ` |
| `BLOCKED_COVERAGE_PASS` | 🟡 | Nội dung dựa trên Open question nằm trong `Blocked Coverage` |
| `UTF8_PASS` | 🟡 | File Markdown/JSON UTF-8, không mojibake |

**Định nghĩa TRACEABILITY_PASS theo giai đoạn:**

| Giai đoạn | Chain tối thiểu để PASS |
|:----------|:------------------------|
| Chỉ ingest PDF (chưa có HSK task) | `Raw Source → Feature Spec (R/AC)` |
| Có HSK task, chưa có test suite | `Raw Source → Feature Spec → Task Spec` |
| Có test suite | `Raw Source → Feature Spec (R/AC) → Test Suite (TC)` |
| Có TBB2 | `TBB2 → HSK → Task Spec → Feature → R/AC → TC` — đầy đủ |

Chỉ yêu cầu chain đúng với giai đoạn hiện tại — không phạt vì chưa có test suite khi chưa đến giai đoạn test design.

### A5. Tính score

**Bảng trọng số cố định:**

| Gate | Điểm tối đa | Ghi chú |
|:-----|:-----------|:--------|
| `NO_INFERENCE_PASS` | 30 | Bắt buộc — fail = 0 điểm gate này |
| `VERIFY_PASS` | 25 | Bắt buộc |
| `TRACEABILITY_PASS` | 15 | Bắt buộc |
| `QUESTION_ROUTING_PASS` | 15 | |
| `BLOCKED_COVERAGE_PASS` | 10 | |
| `UTF8_PASS` | 5 | |
| **Tổng** | **100** | |

**Điều chỉnh bonus/penalty (cộng/trừ vào tổng sau khi tính gates):**
- Mỗi `INFERRED` violation còn sót: −5 điểm.
- Mỗi `LOGIC_INFERRED` violation còn sót: −8 điểm (nặng hơn vì khó phát hiện, dễ qua gate nếu không check kỹ).
- Tỷ lệ testcase map explicit AC ≥ 80%: +5 điểm.
- Mỗi `MISSING_DETAIL` đã bổ sung: +1 điểm (tối đa +5).

**Ghi score vào `quality_gates.json`** với cả `score_before` (trước fix) và `score_after` (sau fix).

### A6. Output Phase A

- `evidence_matrix.md` — cập nhật hoặc tạo mới.
- `quality_gates.json` — append session mới (không ghi đè — xem format bên dưới).

---

## Phase B — Meta-improve

Chỉ chạy khi Phase A báo cùng loại lỗi ≥ 2 lần liên tiếp. Mục tiêu: sửa skill/rule để lần sau không lặp lại.

### B1. Phân tích root cause

Phân loại lỗi theo nhóm:

| Nhóm | Dấu hiệu | Patch target |
|:-----|:---------|:-------------|
| Rule thiếu | Gate fail vì không có rule tương ứng | `.claude/rules/*.md` |
| Skill instruction chưa đủ | LLM bỏ qua bước do instruction mơ hồ | `SKILL.md` |
| Template thiếu cột | Claim bị bỏ qua vì template không có chỗ ghi | `templates/` |
| Command flow thiếu gate | Finalize xảy ra trước khi verify xong | `.claude/commands/` |

### B2. Đề xuất patch tối thiểu

Mỗi patch theo format:

```
## PATCH-NNN: [Tên ngắn]
- **File:** đường dẫn file cần sửa
- **Loại thay đổi:** Add / Update / Remove
- **Nội dung:** mô tả cụ thể sẽ thêm/sửa gì
- **Lý do:** root cause dẫn đến lỗi
- **Expected impact:** gate nào sẽ cải thiện
- **Trạng thái:** Pending
```

### B3. Keep/Discard

- Chỉ giữ patch khi `score_after > score_before` và không vi phạm gate bắt buộc.
- Fail gate bắt buộc → discard, ghi bài học vào retrospective.
- Sau khi apply: đổi `Trạng thái: Pending` → `Trạng thái: ✅ Done`.

### B4. Output Phase B

- `improvement_patch_plan.md` — danh sách PATCH-NNN theo format trên.
- `retrospective.md` — bài học + patch tracking table.

---

## Format các file output

### evidence_matrix.md

```markdown
| Raw Evidence (path#line) | Wiki Claim (path#line) | Status | Action |
| --- | --- | --- | --- |
| raw/07062#234 "Giá trị: Open, Receiving, Received, Completed, Canceled" | features/receiving_po.md#R3 "5 values" | SUPPORTED | Keep |
| — | features/receiving_po.md#R3 "Completed" bị bỏ sót | INFERRED | Remove/Fix |
| raw/07062#45 "Status: Received" + raw/07062#89 "button Save" | features/receiving_po.md#R5 "khi Save → Status = Received" | LOGIC_INFERRED | Remove — ghép logic, raw không nêu trigger |
| raw/07062#153 (section boundary mơ hồ) | features/qc_criteria.md#R7 | UNCLEAR | Move to Q-004 |
| raw/07062#231 "Move qua trang ASN" | features/receiving_po.md#R1 (thiếu note) | MISSING_DETAIL | Add detail |
| [STUB — section VAS chưa đọc] | — | — | Không verify |
```

### quality_gates.json

File này **append** — mỗi session thêm một entry vào array `sessions`, không ghi đè:

```json
{
  "sessions": [
    {
      "session": "YYYY-MM-DD",
      "batch": "tên batch (ví dụ: ingest-07062-07105)",
      "score_before": 83,
      "score_after": 85,
      "gates": {
        "NO_INFERENCE_PASS": true,
        "QUESTION_ROUTING_PASS": true,
        "BLOCKED_COVERAGE_PASS": true,
        "TRACEABILITY_PASS": true,
        "UTF8_PASS": true,
        "VERIFY_PASS": true
      },
      "violations": [],
      "traceability_phase": "Chỉ ingest PDF",
      "verdict": "PASS / CONDITIONAL / FAIL"
    }
  ]
}
```

Khi đọc file cũ để append: dùng Read tool đọc JSON hiện có, thêm entry mới vào array `sessions`, ghi lại toàn bộ.

### improvement_patch_plan.md (Phase B)

```markdown
---
status: Active
updated: YYYY-MM-DD
---

# Improvement Patch Plan

| Patch | File | Loại | Expected impact | Trạng thái |
|:------|:-----|:-----|:----------------|:-----------|
| PATCH-001 | ... | Add | ... | ✅ Done |
| PATCH-002 | ... | Update | ... | Pending |

## Chi tiết

### PATCH-001: [Tên]
...
```

---

## Done criteria

**Phase A hoàn thành khi:**
- `evidence_matrix.md` có đủ claims theo phạm vi đã xác định.
- `quality_gates.json` được append session mới với `score_before` và `score_after`.
- Mọi `INFERRED` và `LOGIC_INFERRED` đã được remove/fix; mọi `UNCLEAR` đã được routing đúng.
- `VERIFY_PASS` xác nhận bằng output thực tế của script.

**Phase B hoàn thành khi:**
- `improvement_patch_plan.md` có đủ PATCH-NNN với format chuẩn.
- `retrospective.md` ghi bài học có thể tái sử dụng lần sau.
- Tất cả patch đã apply được đánh dấu `✅ Done`.

---

## Hard guardrails

- Không suy diễn requirement, AC, API contract, testcase.
- Không đưa thông tin chưa rõ vào mô tả chính; đưa vào `Câu hỏi chưa rõ`.
- Testcase chỉ sinh từ R/AC explicit đã được Gate 1 duyệt.
- Nội dung dựa trên Open question phải nằm ở `Blocked Coverage`.
- Không auto-apply patch nếu chưa pass quality gates.

---

## Tần suất chạy

- **Phase A:** Sau mỗi batch import/ingest.
- **Phase B:** Khi lỗi lặp ≥ 2 lần, hoặc sau khi sửa skill/rule lớn.
- **Regression:** Hằng tuần, chọn 3–5 Feature Spec đại diện (1 full + 2 stub + 1–2 có test suite).
