---
tags: [wiki-rules, reference, refiner]
status: Done
updated: 2026-05-30
---

# Refiner — Quality Gates & Scoring

> Load on-demand sau khi L_structural + L_inference xong và cần finalize verdict.

---

## Quality Gates (3-tier)

Chạy sau khi hoàn thành L_structural + L_inference. Gate 🔴 fail → ghi `FAIL`, không dừng — vẫn chạy L_fix + L_root_cause (nếu trigger short-circuit cho phép) để sinh fix suggestions.

| Gate | Bắt buộc | Kiểm tra | Điểm |
|:-----|:---------|:---------|:-----|
| `L_STRUCTURAL_PASS` | 🔴 | Không còn `FORMAT_VIOLATION`/`COVERAGE_GAP`/`SUSPECT_UNREAD` chưa xử lý. Reports `source_refs_report.json` + `coverage_gap_report.json` không có critical | 40 |
| `L_INFERENCE_PASS` | 🔴 | Không còn `INFERRED` / `LOGIC_INFERRED` trong mô tả chính | 30 |
| `VERIFY_SCRIPT_PASS` | 🔴 | `py .claude/scripts/check_ingest.py --project <p>` exit 0 (hoặc `wiki_sync.py verify` pass standalone) | 15 |
| `L_FIX_COMPLETE` | 🟡 | Mọi Critical violation có FIX suggestion | 10 |
| `L_ROOT_CAUSE_COMPLETE` | 🟡 | Phân tích nhóm lỗi đã ghi vào retrospective (hoặc skip do clean) | 5 |
| **Tổng** | | | **100** |

## Penalty

| Vi phạm | Penalty | Lý do |
|:--------|:-------:|:------|
| `NEGATION_FLIP` còn sót | **−8** | Đảo nghĩa — nguy hiểm nhất |
| `LOGIC_INFERRED` còn sót | **−8** | Spec tự ghép kết luận không có raw |
| `INFERRED` còn sót | **−5** | Generalize / rephrase không bằng chứng |
| `STRIPPED_CONDITION` còn sót | **−5** | Drop modifier (Khi/Nếu/actor) |
| `UNDERREPORTED_COVERAGE` chưa resolve | **−4** | Section gap_ratio < 0.5 |
| `PHANTOM_EVIDENCE` chưa fix | **−3** | `#line` không match content |
| `POTENTIAL_OMISSION` chưa add | **−3** | Raw có claim mà spec miss (silent gap, severity tương đương PHANTOM) |
| Section `unmapped` / `SUSPECT_UNREAD` không ghi chú | **−3** | Coverage gap không document |
| `MISSING_DETAIL` chưa bổ sung | **−2** | Spec thiếu side-effect / note phụ |
| `UNCLEAR` không có Q-ID kèm | **−1** | UNCLEAR phải có entry trong `## ❓ Câu hỏi chưa rõ` + Blocked Coverage |

## Bonus

- Mỗi `MISSING_DETAIL` đã bổ sung trong cùng session: **+1** (tối đa +5)
- Mỗi `POTENTIAL_OMISSION` đã add R-ID trong cùng session: **+1** (tối đa +5)

**Note:** Bonus chỉ áp dụng khi violation được fix TRONG CÙNG session (không phải session sau). Mục đích khuyến khích close loop ngay.

---

## Verdict

| Verdict | Điều kiện |
|:--------|:---------|
| `PASS` | score ≥ 85 **và** tất cả 🔴 pass |
| `CONDITIONAL` | score ≥ 70 **hoặc** có 🟡 fail (nhưng 🔴 pass) |
| `FAIL` | score < 70 **hoặc** có 🔴 fail |

Stub-only specs: classify `bootstrap-ready` (không `release-ready`). Refiner phải emit follow-up actions để chuyển section-title claims thành business-meaning claims trước final PASS.

Stub task_specs: classify `trace-ready` (không `execution-ready`). Stub-only (missing feature requirement linkage hoặc blocked rationale) → emit follow-up fixes, verdict không thể final PASS cho task-completion scope.

---

## quality_gates.json — Schema session

Append-only, tất cả sessions. Không ghi đè.

```json
{
  "sessions": [
    {
      "session": "2026-05-30",
      "batch": "ingest-07062-07105",
      "schema_version": "3.0",
      "score_before": 0,
      "score_after": 85,
      "gates": {
        "L_STRUCTURAL_PASS": true,
        "L_INFERENCE_PASS": true,
        "VERIFY_SCRIPT_PASS": true,
        "L_FIX_COMPLETE": true,
        "L_ROOT_CAUSE_COMPLETE": true
      },
      "violations": {
        "format_violation": 0,
        "coverage_gap": 0,
        "suspect_unread": 0,
        "underreported_coverage": 0,
        "inferred": 0,
        "logic_inferred": 0,
        "stripped_condition": 0,
        "negation_flip": 0,
        "phantom_evidence": 0,
        "potential_omission": 0,
        "missing_detail": 2
      },
      "mode": "Full",
      "verdict": "CONDITIONAL"
    }
  ]
}
```

---

## Gate SSOT

Nguồn gate quyết định duy nhất: `wiki/project_hasaki/refiner/quality_gates.json`.

`wiki/project_hasaki/reports/self_improve/*` chỉ là retrospective/advisory, không override verdict.

Trong mỗi refiner session summary phải có:
- `Gate Decision Source: refiner/quality_gates.json`
- `Advisory Source: reports/self_improve/*`

Nếu PASS/FAIL mismatch giữa 2 nguồn: follow refiner verdict và tạo action item trong `improvement_patch_plan.md`.
