---
batch: ""
session: "YYYY-MM-DD"
source_files: []
verdict: "FAIL"
score: 0
---

# Refiner Report — {batch_name}

> Session: YYYY-MM-DD | Batch: {batch_name}

---

## L1 — Format Violations

| File | Mục thiếu/sai | Loại vi phạm | Action |
|:-----|:-------------|:-------------|:-------|
| — | — | — | — |

**Tổng:** 0 violations

---

## L2 — Coverage Gaps

| Section ID | Title | Lines | coverage_status | Missing flags | Nội dung quan trọng chưa capture |
|:-----------|:------|:------|:----------------|:--------------|:---------------------------------|
| — | — | — | — | — | — |

**Tổng:** 0 gaps · 0 unmapped sections

---

## L3 — Summary

> Chi tiết xem `evidence_matrix.md`

| Label | Count |
|:------|:------|
| SUPPORTED | 0 |
| UNCLEAR | 0 |
| INFERRED | 0 |
| LOGIC_INFERRED | 0 |
| MISSING_DETAIL | 0 |

---

## L4 — Fix Suggestions

### FIX-001: [Mô tả ngắn]
- **File:** wiki/project_hasaki/features/xxx.md
- **Vùng:** mục / dòng cụ thể
- **Vấn đề:** [L1/L2/L3] — mô tả vi phạm
- **Gợi ý:** nội dung cần thêm/sửa/xóa
- **Ưu tiên:** Critical / High / Medium

---

## Summary

| Gate | Status | Score |
|:-----|:-------|:------|
| L1_FORMAT_PASS | ❌/✅ | /20 |
| L2_COVERAGE_PASS | ❌/✅ | /20 |
| L3_NO_INFERENCE_PASS | ❌/✅ | /30 |
| VERIFY_SCRIPT_PASS | ❌/✅ | /15 |
| L4_SUGGESTIONS_COMPLETE | ❌/✅ | /10 |
| L5_ROOT_CAUSE_COMPLETE | ❌/✅ | /5 |
| **Tổng** | **FAIL/CONDITIONAL/PASS** | **/100** |
