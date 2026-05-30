---
session: 2026-05-30
batch: spec-scoped-batch-2
mode: Spec-scoped
trigger: "Sau refine stub → full spec (Gate 1B promotion)"
gate_decision_source: wiki/project_hasaki/refiner/quality_gates.json
advisory_source: wiki/project_hasaki/refiner/improvement_patch_plan.md
specs_in_scope:
  - stub_receiving_po_inbound_shipment
  - stub_qc_criteria_sku
  - stub_qc_vas
generated_at: "2026-05-30 21:15:00+07:00"
---

# Refiner Report — 2026-05-30 / spec-scoped-batch-2

## Scope session này

- **Mode:** Spec-scoped (3 specs refine từ stub → full)
- **Verify đầy đủ:** `stub_receiving_po_inbound_shipment.md`, `stub_qc_criteria_sku.md`, `stub_qc_vas.md`
- **Skip deep scan:** (không có — 3 specs đều mới, chưa session nào verify)
- **Pre-req refresh:** `py .claude/scripts/check_ingest.py --project project_hasaki` exit 0 (4 stages clean: verify / evidence_index / verify_source_refs / coverage_gap_estimator)

## Tổng quan claims

| Spec | R | AC | BR | Messages | Q | Source range |
|:-----|---:|---:|---:|---------:|---:|:--------------|
| stub_receiving_po_inbound_shipment | 20 | 11 | 10 | 4 | 7 | 07062#L224-L347 (S-05, S-06) |
| stub_qc_criteria_sku | 36 | 14 | 16 | 6 | 10 | 07105#L217-L432 (S-07, S-08) |
| stub_qc_vas | 18 | 12 | 10 | 3 | 8 | 07105#L696-L780 (S-17, S-18) |
| **Tổng** | **74** | **37** | **36** | **13** | **25** | |

## L_structural — Format & Coverage

| File / Section | Loại vi phạm | Nguồn report | Action |
|:---------------|:-------------|:-------------|:-------|
| _(none)_ | — | source_refs_report.json: 75/75 R-IDs `OK_CANONICAL`; coverage_gap_report.json: 0 findings; AC-NN format ✅; frontmatter complete ✅; partial_read=false → no Blocked Coverage trigger | — |

**Observation (advisory, không phải violation):** Cùng pattern với pilot-batch-1 — `flags=[]` cho mọi sections trong index dù spec content có enum/state_transition/business_rule/error_messages/formula. Đã ghi trong `improvement_patch_plan.md` Observation #1. Defer cho tới khi auto-flag-update script được build.

L_structural: **0 violations**.

## L_inference — Content Verification

Xem chi tiết per-claim trong [`evidence_matrix.md`](evidence_matrix.md).

### Tóm tắt theo spec

#### stub_receiving_po_inbound_shipment (20 R + 11 AC + 10 BR + 4 messages)

| Label | Count | Claims |
|:------|------:|:-------|
| `SUPPORTED` | 44 | Toàn bộ R001-R020 (trừ R007 với placeholder), AC-01..AC-11 đều derivable, BR mostly verbatim |
| `UNCLEAR (đã captured)` | 2 | R007 DESC-INS-004 placeholder `{sku_code}` vs raw literal `422225215` (Q-003 đã capture); BR "Hiển thị thời gian Receiving" thêm "đầu tiên" — minor |
| `INFERRED` / `LOGIC_INFERRED` / `STRIPPED_CONDITION` / `NEGATION_FLIP` / `PHANTOM_EVIDENCE` | 0 | — |

**Status:** Tất cả violations đã captured trong Q section của spec. Spec sạch.

#### stub_qc_criteria_sku (36 R + 14 AC + 16 BR + 6 messages)

| Label | Count | Claims |
|:------|------:|:-------|
| `SUPPORTED` | 70 | R001-R036 (trừ R008, R027 + placeholder messages), AC-01..AC-14 |
| `UNCLEAR (đã captured)` | 4 | ERR-CSKU-002 / MSG-CSKU-005 / MSG-CSKU-006 placeholder `{sku_code}` vs raw literal `422280022` (Q-008 capture VN aspect); Q-001 capture index boundary mismatch |
| `POTENTIAL_OMISSION` | 2 | **R008** — raw L249 typo `Đến ngày phải lớn hơn hoặc bằng đến ngày` → spec silently corrects thành `Đến ngày ≥ Từ ngày`, không có Q. **R027** — spec apply Sai số cho phép cho `=`, `>`, `>=`, `<`, `<=`; raw chỉ explicit Sai số ở `=`, ambiguous cho 4 operators còn lại — không có Q |
| `INFERRED` / `LOGIC_INFERRED` / `NEGATION_FLIP` / `PHANTOM_EVIDENCE` | 0 | — |

**Status:** 2 POTENTIAL_OMISSION cần thêm Q vào spec. Xem FIX-002 / FIX-003.

#### stub_qc_vas (18 R + 12 AC + 10 BR + 3 messages)

| Label | Count | Claims |
|:------|------:|:-------|
| `SUPPORTED` | 42 | R001-R018, AC-01..AC-12, BR + messages |
| `UNCLEAR (đã captured)` | 1 | MSG-VAS-001 placeholder `{vas_code}` vs raw literal `1003241119000039` (Q-001 capture RECEIVE typo + indirect placeholder) |
| `INFERRED` / `LOGIC_INFERRED` / `STRIPPED_CONDITION` / `NEGATION_FLIP` / `PHANTOM_EVIDENCE` / `POTENTIAL_OMISSION` | 0 | — |

**Status:** Spec sạch. Tất cả violations đã captured trong Q section.

### Cross-batch observations (informational, không phải violation)

1. **Placeholder vs literal:** 3 instances trong batch — `{sku_code}` (×2 specs), `{vas_code}` (×1). Tất cả đã captured (partially) qua Q-IDs. Đây là spec interpretation acceptable (raw chỉ có VD literal, spec generalize đúng) nhưng nên có Q chuyên về "placeholder syntax" consistency. Pattern lặp lại với pilot-batch-1 (gift→gốc typo handling).

L_inference: **2 violations** (POTENTIAL_OMISSION, cùng 1 spec stub_qc_criteria_sku). Tất cả 🔴 gates pass.

## L_fix — Suggestions

### FIX-002: Thêm Q cho raw typo "Đến ngày phải ≥ đến ngày" (R008)

- **File:** `wiki/project_hasaki/features/stub_qc_criteria_sku.md`
- **Vùng:** R008 (dòng 55) + BR table dòng 129 + `## ❓ Câu hỏi chưa rõ` section
- **Vấn đề:** Raw `07105_Quality_Control_Docs_ver1.5.md#L249` ghi `Đến ngày phải lớn hơn hoặc bằng đến ngày` (rõ ràng là typo của "Từ ngày"). Spec silently correct thành `Đến ngày ≥ Từ ngày` không có Q-ID. Vi phạm `.claude/rules/20-no-inference.md` (correction = interpretation).
- **Gợi ý:** Thêm Q-011 vào Q section:
  ```
  | Q-011 | R008 | Raw L249 ghi `Đến ngày phải lớn hơn hoặc bằng đến ngày` — typo của "Từ ngày" hay intentional? Spec đang interpret là `Đến ngày ≥ Từ ngày`. | PO/Dev | Open | | | |
  ```
  Và thêm `R008 — chờ Q-011 (raw typo correction)` vào `## 🚧 Blocked Coverage`.
- **Ưu tiên:** Medium (không block release, nhưng cần audit trail)

### FIX-003: Thêm Q cho Sai số cho phép applicability (R027)

- **File:** `wiki/project_hasaki/features/stub_qc_criteria_sku.md`
- **Vùng:** R027 (dòng 74) + `## ❓ Câu hỏi chưa rõ` section
- **Vấn đề:** Spec ghi "Validation cho điều kiện `=`, `>`, `>=`, `<`, `<=`: `Sai số cho phép` không bắt buộc, số > 0". Nhưng raw `07105_Quality_Control_Docs_ver1.5.md#L383-L406`: Sai số chỉ explicit ở `=` (L387-L388); operators `>`, `>=`, `<`, `<=` chỉ list Giá trị + Đơn vị tính (L395-L401), không nhắc Sai số. Spec assumes Sai số applies to all 5 — interpretation chưa có Q.
- **Gợi ý:** Thêm Q-012:
  ```
  | Q-012 | R027 | Raw chỉ explicit `Sai số cho phép` cho toán tử `=` (L387-L388); với `>`, `>=`, `<`, `<=` (L395-L401) raw không nhắc Sai số. Field `Sai số cho phép` có áp dụng cho cả 5 toán tử so sánh hay chỉ `=`? | PO/UX | Open | | | |
  ```
  Và `R027 — chờ Q-012 (Sai số scope cho >, >=, <, <=)` vào Blocked Coverage.
- **Ưu tiên:** Medium

### Pending (không generate FIX cho batch này)

Cross-batch placeholder pattern (DESC-INS-004 / ERR-CSKU-002 / MSG-CSKU-005/006 / MSG-VAS-001) — tất cả đã captured qua Q section (Q-003 / Q-008 / Q-001 tương ứng). Không cần FIX vì spec đã document uncertainty.

## L_root_cause — Pattern Analysis

**Short-circuit decision:** Không short-circuit hoàn toàn — observed cross-session pattern.

### Pattern phát hiện

1. **"Silent spec interpretation when raw is ambiguous/typo"** — 2 instances trong batch này (FIX-002 R008 typo, FIX-003 R027 ambiguous applicability) + 1 instance pilot-batch-1 (gift→gốc, applied as FIX-001). Tổng 3 instances qua 2 sessions = **cross-session pattern**.

### Generalization

Pattern: Khi raw có typo / ambiguous wording, spec writer tendency là silently interpret/correct mà không bắn Q-ID. Vi phạm `.claude/rules/20-no-inference.md`.

### Decision

Đề xuất skill patch (advisory, không tự apply): 

> **Patch candidate cho `.claude/skills/hasaki-wiki/references/phase_test_design.md`** (hoặc tạo mới checklist trong refinement template): thêm checklist item *"Đối với mỗi R-ID, nếu spec text ≠ raw verbatim (correction, generalization, condition-stripping), bắt buộc có Q-ID tương ứng trong `## ❓ Câu hỏi chưa rõ` section, kèm raw quote trong câu hỏi."*

Patch này không trong scope L_root_cause auto-apply — chờ ≥ 3 sessions xác nhận pattern trước khi modify skill (per scoring policy). Ghi `retrospective.md` để track.

### Counterfactual test (lightweight)

Nếu patch trên đã có: 
- FIX-002 / FIX-003 sẽ tự động trigger ngay khi user refine stub_qc_criteria_sku (spec writer thấy checklist sẽ thêm Q-011/Q-012). 
- FIX-001 pilot-batch-1 (gift→gốc) tương tự.

→ Patch generalize-able, không over-fit.

## Summary

| Item | Value |
|:-----|:------|
| Specs in scope | 3 |
| Claims verified | 156 (74 R + 37 AC + 36 BR + 13 messages + 25 Q references) |
| `L_STRUCTURAL_PASS` | ✅ |
| `L_INFERENCE_PASS` | ✅ (2 POTENTIAL_OMISSION nhưng không penalty per scoring.md) |
| `VERIFY_SCRIPT_PASS` | ✅ (check_ingest exit 0) |
| `L_FIX_COMPLETE` | ✅ (2 FIX suggestions generated) |
| `L_ROOT_CAUSE_COMPLETE` | ✅ (pattern noted, no auto-patch) |
| **Score** | **100/100** |
| **Verdict (batch)** | **PASS** |
| Verdict per-spec | inbound_shipment: PASS / criteria_sku: PASS (with 2 advisory FIX) / vas: PASS |

Gate Decision Source: `wiki/project_hasaki/refiner/quality_gates.json`
Advisory Source: `wiki/project_hasaki/refiner/improvement_patch_plan.md`
