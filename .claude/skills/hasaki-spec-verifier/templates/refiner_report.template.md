---
session: "YYYY-MM-DD"
batch: ""
mode: "Full | Delta | Spec-scoped"
trigger: ""
gate_decision_source: wiki/<project>/refiner/quality_gates.json
advisory_source: wiki/<project>/refiner/improvement_patch_plan.md
specs_in_scope: []
generated_at: "YYYY-MM-DD HH:MM:SS+07:00"
---

# Refiner Report — YYYY-MM-DD / {batch_name}

## Scope session này

- **Mode:** Full / Delta / Spec-scoped
- **Verify đầy đủ:** [list specs cần verify deep]
- **Skip deep scan:** [list specs đã PASS session trước + version khớp]
- **Pre-req refresh:** `py .claude/scripts/check_ingest.py --project <p>` exit ?

## Tổng quan claims

| Spec | R | AC | BR | Messages | Q | Source range |
|:-----|---:|---:|---:|---------:|---:|:--------------|
| ... | | | | | | |
| **Tổng** | | | | | | |

## L_structural — Format & Coverage

| File / Section | Loại vi phạm | Nguồn report | Action |
|:---------------|:-------------|:-------------|:-------|
| _(none)_ | — | — | — |

L_structural: **N violations**.

## L_inference — Content Verification

Xem chi tiết per-claim trong [`evidence_matrix.md`](evidence_matrix.md).

### Tóm tắt theo spec

#### {spec_name}

| Label | Count | Claims |
|:------|------:|:-------|
| `SUPPORTED` | | |
| `UNCLEAR (đã captured)` | | |
| `INFERRED` / `LOGIC_INFERRED` / `STRIPPED_CONDITION` / `NEGATION_FLIP` / `PHANTOM_EVIDENCE` / `POTENTIAL_OMISSION` / `MISSING_DETAIL` | | |

**Status:** [PASS sạch / CONDITIONAL có FIX / FAIL]

L_inference: **N violations**. Gates: [✅ / 🔴 / 🟡].

## L_fix — Suggestions

### FIX-NNN: [Mô tả ngắn]
- **File:** `wiki/project_hasaki/features/xxx.md`
- **Vùng:** dòng hoặc section cụ thể
- **Vấn đề:** [L_structural / L_inference] — mô tả vi phạm + ref report finding
- **Gợi ý:** nội dung cụ thể cần thêm/sửa/xóa
- **Ưu tiên:** Critical / High / Medium

## L_root_cause — Pattern Analysis

**Short-circuit decision:** [skip / not skip + lý do]

### Pattern phát hiện
[Nếu có pattern lặp ≥ 2 — apply L_root_cause Bước 0-5; nếu không — ghi "no new patterns"]

## Summary

| Item | Value |
|:-----|:------|
| Specs in scope | |
| Claims verified | |
| `L_STRUCTURAL_PASS` | ✅ / 🔴 |
| `L_INFERENCE_PASS` | ✅ / 🔴 |
| `VERIFY_SCRIPT_PASS` | ✅ / 🔴 |
| `L_FIX_COMPLETE` | ✅ / 🟡 |
| `L_ROOT_CAUSE_COMPLETE` | ✅ / 🟡 |
| **Score** | **N/100** |
| **Verdict (batch)** | **PASS / CONDITIONAL / FAIL** |
| Verdict per-spec | |

Gate Decision Source: `wiki/<project>/refiner/quality_gates.json`
Advisory Source: `wiki/<project>/refiner/improvement_patch_plan.md`
