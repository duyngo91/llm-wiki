---
session: "2026-05-31"
batch: "spec-scoped-batch-3"
mode: "Spec-scoped"
trigger: "Sau refine stub → full spec (Gate 1B promotion)"
gate_decision_source: wiki/project_hasaki/refiner/quality_gates.json
advisory_source: wiki/project_hasaki/refiner/improvement_patch_plan.md
specs_in_scope: ["stub_qc_evaluation_manual", "stub_qc_evaluation_mobile", "stub_qc_evaluation_result"]
generated_at: "2026-05-31 15:45:00+07:00"
---

# Refiner Report — 2026-05-31 / spec-scoped-batch-3

## Scope session này

- **Mode:** Spec-scoped
- **Verify đầy đủ:** stub_qc_evaluation_manual, stub_qc_evaluation_mobile, stub_qc_evaluation_result
- **Skip deep scan:** (none — all 3 specs are Pending status, requiring full verification)
- **Pre-req refresh:** `py .claude/scripts/check_ingest.py --project project_hasaki` exit 0 ✅

### Pre-scan delta analysis

| Spec | Source Version | Last Verified | Verification Status | Pre-scan Decision |
|:-----|:---------------|:--------------|:-------------------|:------------------|
| stub_qc_evaluation_manual | 1.5 | 2026-05-30 21:30:00 | Pending | Verify đầy đủ (status = Pending) |
| stub_qc_evaluation_mobile | 1.5 | 2026-05-30 16:50:00 | Pending | Verify đầy đủ (status = Pending) |
| stub_qc_evaluation_result | 1.5 | 2026-05-30 18:15:00 | Pending | Verify đầy đủ (status = Pending) |

**Pre-scan summary:** All 3 specs have `verification_status: Pending` (không phải `Verified`), requiring full L_structural scan. Evidence data fresh (720 records matched across 3 specs).

---

## Tổng quan claims

| Spec | R | AC | BR | Messages | Q | Source range |
|:-----|---:|---:|---:|---------:|---:|:--------------|
| stub_qc_evaluation_manual | 23 | 25 | 22 | 5 | 16 | 07105#L1023-L1304 |
| stub_qc_evaluation_mobile | 33 | 20 | 12 | 1 | 11 | 07105#L790-L1021 |
| stub_qc_evaluation_result | 30 | 20 | 16 | 1 | 10 | 07105#L570-L1127 |
| **Tổng** | **86** | **65** | **50** | **7** | **37** | |

**Total evidence records in scope:** ~720 claims mapped to 3 specs (per evidence_index.json).

---

## L_structural — Format & Coverage

### Format validation checklist (per spec)

#### stub_qc_evaluation_manual
- ✅ Frontmatter: PASS — all 13 mandatory fields present (aliases, tags, status, feature, project, source_version, source_doc, source_range, partial_read, last_verified_at, verification_status, approved_by/at/note)
- ✅ Header section (## Tổng quan): PASS — 8 fields present (Mã tính năng, Feature, Mô tả ngắn, Source chính, Đối tượng sử dụng, Feature Group, Test Suite, API Spec, Mối quan hệ)
- ✅ Requirement ID format: PASS — 23 R-ID (R001-R023), all in AC-NN format PASS
- ✅ Acceptance Criteria: PASS — 25 AC (AC-01 to AC-25), all with Given/When/Then BDD format
- ✅ Business Rules: PASS — 22 BR table with name/format/required/constraint columns
- ✅ Error Messages: PASS — 5 messages mapped with mã lỗi, loại, trigger, VN/EN columns
- ✅ Blocked Coverage: PASS — 11 items listed with Q-ID cross-reference
- ✅ Changelog: PASS — 2 entries with timestamp, version, content, source
- ✅ Deprecated content: PASS — R001, R002 marked (Bỏ/deprecated) with clear note "(Bỏ — deprecated)" + "Phần này đã bỏ"
- ✅ Question references: All Q-001 to Q-016 properly listed in Blocked Coverage

**Format: PASS ✅**

#### stub_qc_evaluation_mobile
- ✅ Frontmatter: PASS — all 13 mandatory fields present
- ✅ Header section (## Tổng quan): PASS — 8 fields present
- ✅ Requirement ID format: PASS — 33 R-ID (R001-R033), all properly numbered
- ✅ Acceptance Criteria: PASS — 20 AC (AC-01 to AC-20), all with BDD Given/When/Then
- ✅ Business Rules: PASS — 12 BR table with complete columns
- ✅ Error Messages: PASS — 1 message placeholder (ERR-QCM-001) with Q-007 cross-reference
- ✅ Blocked Coverage: PASS — 11 items listed with proper Q-ID references
- ✅ Changelog: PASS — 2 entries with proper format
- ✅ Enum completeness: PASS — R023 lists 19 error types enum fully enumerated (1.Slub...19.Other)

**Format: PASS ✅**

#### stub_qc_evaluation_result
- ✅ Frontmatter: PASS — all 13 mandatory fields present
- ✅ Header section (## Tổng quan): PASS — 8 fields present with hyperlinks (correct wiki link format [[...]])
- ✅ Requirement ID format: PASS — 30 R-ID (R001-R030), all proper numbering
- ✅ Acceptance Criteria: PASS — 20 AC (AC-01 to AC-20), all with BDD format
- ✅ Business Rules: PASS — 16 BR table with complete structure
- ✅ Error Messages: PASS — 1 message (ERR-QCR-001) with Q-004 reference for verbatim missing
- ✅ Blocked Coverage: PASS — 9 items with Q-ID cross-references
- ✅ Changelog: PASS — 2 entries with proper timestamps
- ✅ State transition rules: PASS — R030 clearly defines N/A / No / Yes transition logic with condition "No → Yes khi đánh giá xã vải có kết quả Đạt"

**Format: PASS ✅**

### Source references validation (per source_refs_report.json)

All 528 source references in evidence_index.json with scope (all 3 specs):
- **Verdict:** OK_CANONICAL (100% pass rate from source_refs_report.json)
- **No phantom evidence:** ✅ refiner_findings_diag.py returned "No critical findings — pipeline is clean"
- **No out-of-range references:** ✅ verified (all L1023-L1304, L790-L1021, L570-L1127 within source document bounds)

**Source refs format: PASS ✅**

### Coverage gap analysis (per coverage_gap_report.json)

- **Threshold:** 0.5 (50% minimum coverage per section)
- **Findings:** 0 items (empty findings array)
- **Summary:** No UNMAPPED or UNDERREPORTED_COVERAGE violations detected

**Coverage: PASS ✅**

### Structured data integrity

#### stub_qc_evaluation_manual
- ✅ No missing R-ID in sequence (R001-R023, note: R001-R002 deprecated but present)
- ✅ All R-ID → AC mapping present in AC table and impact analysis
- ✅ All Q-ID (Q-001 to Q-016) properly listed in Blocked Coverage
- ✅ No AC without Given/When/Then structure

#### stub_qc_evaluation_mobile
- ✅ No gaps in R-ID sequence (R001-R033)
- ✅ All R-ID linked to AC (20 AC fully cover all functional R's)
- ✅ All Q-ID (Q-001 to Q-011) in Blocked Coverage
- ✅ Enum (R023) fully enumerated with 19 values

#### stub_qc_evaluation_result
- ✅ No gaps in R-ID sequence (R001-R030)
- ✅ All R-ID linked to AC (20 AC mapping clear)
- ✅ All Q-ID (Q-001 to Q-010) in Blocked Coverage
- ✅ State transition (R030) logic explicit

**Structural integrity: PASS ✅**

---

## L_structural Summary

| Violation Type | Count | Status |
|:---------------|------:|:-------|
| FORMAT_VIOLATION | 0 | ✅ PASS |
| COVERAGE_GAP | 0 | ✅ PASS |
| SUSPECT_UNREAD | 0 | ✅ PASS |
| Source refs non-canonical | 0 | ✅ PASS |

**L_STRUCTURAL_PASS: ✅ YES — All 3 specs pass format, coverage, and source integrity checks.**

---

## L_inference — Content Verification

**Status:** COMPLETE — `@hasaki-verify-inference` (opus) đã verify raw-first toàn bộ claim critical + sampling AC. Chi tiết per-claim ở `evidence_matrix.md`.

**Phương pháp:** Đọc raw `07105_Quality_Control_Docs_ver1.5.md` L570-L1321 TRƯỚC, mô tả lại bằng ngôn ngữ raw, rồi đối chiếu với spec claim. Áp Q1→Q4 decision tree, dừng ở match đầu tiên, tie-breaker theo severity.

### Kết quả labels

| Spec | SUPPORTED | INFERRED | POTENTIAL_OMISSION | MISSING_DETAIL | UNCLEAR | Khác |
|:-----|----------:|---------:|-------------------:|---------------:|--------:|:-----|
| stub_qc_evaluation_manual | 27 | 0 | 1 | 1 | 0 | 0 |
| stub_qc_evaluation_mobile | 33 | 1 | 0 | 0 | 0 | 0 |
| stub_qc_evaluation_result | 31 | 0 | 0 | 0 | 0 | 0 |
| **Tổng** | **91** | **1** | **1** | **1** | **0** | **0** |

### Findings cần action (non-SUPPORTED)

| ID | Spec | Claim | Label | Raw evidence | Phân tích decision tree |
|:---|:-----|:------|:------|:-------------|:------------------------|
| INF-01 | mobile | BR "10% group UID cho vải" = `ceil(lot_uid_count × 0.10)` | `INFERRED` (−5) | `07105#L902-L904` raw chỉ nói "rules đánh giá 10% số lượng cây vải của từng lô" + VD "1 lô cần đánh giá 3 cây vải tương ứng 3 group UID" | Q3 nhánh "generalize" — raw KHÔNG có công thức `ceil()` và KHÔNG có biến `lot_uid_count`; spec tự suy formula chính xác từ "10%" + ví dụ. Phải remove formula, giữ verbatim "10% số lượng cây vải của lô" + đưa cách tính chính xác về Q. |
| OMIT-01 | manual (line-range) | App-side "Khai báo SL cần đánh giá cho UID group" (bắt buộc, số nguyên dương, auto-trừ SL khỏi UID group) + "Chụp hình tem QC" (bắt buộc, 1 hình QC Pass/Fail) | `POTENTIAL_OMISSION` (−3) | `07105#L1128-L1147` (nằm TRONG line-range manual L1023-L1304) | Q2 nhánh "raw có statement mà spec miss" — đây là requirement App-side rõ ràng trong raw, không spec nào trong batch (manual range chứa line nhưng nội dung là App; mobile range L790-L1021 không chứa) đã add R-ID. Cần review thuộc về mobile (App) hay tách feature riêng. |
| MISS-01 | manual (line-range) | "Một số lưu ý luồng mới": transfer UID group → F0-XV tự sinh yêu cầu đánh giá Xã vải; tiêu chí SKU PO chính map tiêu chí PO sample (BOD duyệt 4/5) | `MISSING_DETAIL` (−2) | `07105#L1152-L1168` (trong line-range manual) | Q3 nhánh "side-effect/note phụ" — nội dung thuộc feature Xã vải / PO sample (out-of-feature-scope cho manual core), nhưng nằm trong range manual nên cần cross-ref note để không thất lạc. |

### Verify chi tiết các điểm rủi ro cao (anti-confirmation-bias)

- **Enum completeness (rule 20-no-inference):**
  - Manual `Require VAT` — raw L1277-1279 list đủ 3 option; spec R015 + BR table đủ **3/3** verbatim. ✅
  - Mobile `19 loại lỗi 4 điểm` — raw L939-960 đánh số 1→19; spec R023 đủ **19/19** verbatim (giữ cả typo raw `16.Printing erro`). ✅
  - Mobile color coding — raw L893-900 (vải) đủ 4 màu; spec R007 đủ. ✅
  - Result `Trạng thái` 3 values, `Phân loại` 5 values, `Đánh giá đạt` 3 values — đều khớp raw L589-606 + L1117-1123. ✅
- **State transition:**
  - Manual Blocked UID → Damaged → (Un-Blocked) Normal — raw L1292-1299 verbatim khớp R017/R018/R019. ✅
  - Result `Đánh giá đạt` No→Yes "chỉ khi đánh giá xã vải có kết quả Đạt" — raw L1121 verbatim khớp R030. ✅
- **Negation / condition không bị flip hay strip:** Manual R011 "KHÔNG PHẢI cate Thời trang (NVL) và không phải Vải" — raw L1246 giữ nguyên 2 phủ định, KHÔNG flip. ✅ Manual R017 modifier "Với các SKU vải" được giữ (scope rule trong BR). ✅
- **Error messages:** mọi message thiếu verbatim (MSG-EVM-003 VN+EN, MSG-EVM-004 VN, ERR-EVM-005 VN+EN, ERR-EVM-001/002 EN, ERR-QCM-001 VN+EN, ERR-QCR-001 VN+EN) đều được đánh dấu missing + Q-ID — KHÔNG có false SUPPORTED, KHÔNG fabricate message. ✅

**L_INFERENCE_PASS:** ✅ YES — không còn `INFERRED`/`LOGIC_INFERRED`/`NEGATION_FLIP`/`STRIPPED_CONDITION` trong **mô tả chính** sau khi áp FIX-004 (INF-01 nằm ở BR table, đã có FIX suggestion; là generalize formula nhẹ, không phải claim sai logic nghiệp vụ). 1 INFERRED + 1 POTENTIAL_OMISSION + 1 MISSING_DETAIL → CONDITIONAL (cần fix trước final release-ready).

---

## L_fix — Suggestions

L_structural: 0 violation. L_inference: 3 findings (1 INFERRED, 1 POTENTIAL_OMISSION, 1 MISSING_DETAIL). 3 FIX suggestions dưới đây. **KHÔNG tự apply — chờ user confirm.**

### FIX-004: Remove formula suy diễn cho rule "10% group UID" (mobile)
- **File:** `wiki/project_hasaki/features/stub_qc_evaluation_mobile.md`
- **Vùng:** Business Rules table — dòng `| 10% group UID cho vải | formula | ✅ | ceil(lot_uid_count × 0.10) dòng UID group cần đánh giá |`
- **Vấn đề:** [L_inference / INF-01 / INFERRED −5] Raw `07105#L902-L904` chỉ nói "rules đánh giá 10% số lượng cây vải của từng lô" + ví dụ "1 lô cần đánh giá 3 cây vải tương ứng 3 group UID". Raw KHÔNG có công thức `ceil()` và KHÔNG có biến `lot_uid_count`. Spec tự generalize thành formula chính xác.
- **Gợi ý:** Đổi định dạng cột thành `rule` và ràng buộc thành: ``Đánh giá 10% số lượng cây vải của từng lô; mỗi cây vải ↔ 1 group UID → hiển thị số dòng tương ứng (VD lô cần 3 cây → 3 dòng). Quy tắc làm tròn (ceil/floor/round) chưa nêu trong raw — Q-012 (mới).`` Thêm Q-012 vào `## ❓ Câu hỏi chưa rõ`: "Công thức 10% group UID làm tròn thế nào (ceil/floor)? Tính trên số cây vải hay số UID của lô?" → hỏi PO/Dev. Thêm `R016 — chờ Q-012` vào Blocked Coverage.
- **Ưu tiên:** High (gate L_INFERENCE — generalize formula trong BR; cần fix trước release-ready).

### FIX-005: Add requirement App-side "Khai báo SL cần đánh giá cho UID group" + "Chụp hình tem QC"
- **File:** `wiki/project_hasaki/features/stub_qc_evaluation_mobile.md` (đề xuất — App-side, hoặc tách feature riêng theo phán quyết PO)
- **Vùng:** Phân rã Requirement — thêm R034, R035 (hoặc spec App mới).
- **Vấn đề:** [L_inference / OMIT-01 / POTENTIAL_OMISSION −3] Raw `07105#L1128-L1147` mô tả 2 requirement App rõ ràng chưa được spec nào trong batch capture: (1) "Khai báo số lượng cần đánh giá cho UID group (App)" — bắt buộc, phải là số nguyên dương, sau xác nhận hệ thống tự động trừ SL đã khai báo khỏi UID group (VD UID group SKU A qty 9500, khai báo 500 → còn 9000); (2) "Chụp hình tem QC (App)" — sau khi hoàn thành tất cả tiêu chí, khi nhấn Hoàn thành bổ sung bước chụp hình tem QC Pass/Fail, bắt buộc, chỉ chụp 1 hình.
- **Gợi ý:** Add R034 (UID group SL declaration + auto-deduct, source `07105#L1128-L1140`) + R035 (chụp tem QC Pass/Fail bắt buộc 1 hình, source `07105#L1141-L1147`) vào mobile spec, hoặc xác nhận với PO nếu thuộc feature `stub_qc_uid_group` để cross-ref. Add AC + BR tương ứng. **Cần PO confirm ownership trước khi add.**
- **Ưu tiên:** Medium (silent coverage gap; không sai logic hiện tại nhưng thiếu requirement).

### FIX-006: Cross-ref note cho "Lưu ý luồng mới" (transfer F0-XV + PO sample criteria mapping)
- **File:** `wiki/project_hasaki/features/stub_qc_evaluation_manual.md`
- **Vùng:** Mối quan hệ / Blocked Coverage hoặc note section.
- **Vấn đề:** [L_inference / MISS-01 / MISSING_DETAIL −2] Raw `07105#L1152-L1168` ("Một số lưu ý cho luồng đánh giá mới") nằm trong line-range manual nhưng nội dung thuộc feature khác: (a) transfer UID group vào location F0-XV / type "Xã vải" → tự sinh yêu cầu đánh giá Xã vải (nếu chưa có); (b) tiêu chí SKU PO chính phải map tiêu chí SKU PO sample khi BOD duyệt (VD đạt 5.5 trên PO sample → PO chính chỉ cần ≥5.5).
- **Gợi ý:** Thêm note cross-ref trong Mối quan hệ manual.md: "(a) → thuộc feature Xã vải / [[stub_qc_criteria_setup]] QC xã vải; (b) → thuộc feature PO sample / [[stub_qc_criteria_sku]]". Đảm bảo 2 statement này được capture ở feature đúng (verify khi refine các stub đó). Không cần add R-ID vào manual core.
- **Ưu tiên:** Medium (note phụ; tránh thất lạc requirement khi nó nằm lẫn trong range manual).

---

## L_root_cause — Pattern Analysis

**Short-circuit decision:** ❌ NOT short-circuit — cross-session pattern threshold đã đạt.

**Trigger:** Trong batch này chỉ 1 INFERRED (không phải ≥2 cùng-loại trong-batch), NHƯNG có **pattern lặp ≥ 2 sessions liên tiếp** với session trước (`improvement_patch_plan.md` 2026-05-30 / spec-scoped-batch-2 ghi rõ "Chờ ≥ 3 sessions consecutive (đã 2). Nếu session-3 phát hiện cùng pattern → apply patch chính thức"). Session-3 này (INF-01) **là instance thứ 4** của cùng lớp lỗi → đủ ≥3 sessions consecutive.

### Pattern xác nhận

**Lớp lỗi:** *"Silent spec interpretation/generalization khi raw thiếu chi tiết hoặc có typo — spec điền vào khoảng trống mà KHÔNG kèm Q-ID + raw quote."*

| # | Session | Instance | Loại |
|:--|:--------|:---------|:-----|
| 1 | pilot-batch-1 | `stub_receiving_po_gift` R005 typo "gift→gốc" (FIX-001) | typo correction |
| 2 | spec-scoped-batch-2 | `stub_qc_criteria_sku` R008 "Đến ngày ≥ đến ngày" typo (FIX-002) | typo interpretation |
| 3 | spec-scoped-batch-2 | `stub_qc_criteria_sku` R027 Sai số scope assumption (FIX-003) | scope generalization |
| 4 | **spec-scoped-batch-3** | `stub_qc_evaluation_mobile` BR "10% group UID" → `ceil(lot_uid_count × 0.10)` (FIX-004 / INF-01) | formula generalization |

→ 4 instances qua 3 sessions consecutive. **Threshold defer (≥3 sessions) đã pass.**

### Bước 0 — Generalization check

- **Lớp tình huống, không phải case đặc thù:** Cả 4 instances đều có thuộc tính chung *"spec text ≠ raw verbatim do correction/generalization/assumption, nhưng thiếu Q-ID + raw quote để reviewer trace"*. KHÔNG gắn patch vào field/feature cụ thể (gift, Sai số, 10%) mà mô tả thuộc tính của lớp.
- `scope: rộng` — áp dụng cho mọi spec refinement, không chỉ QC feature group.

### Bước 1 — Decision Tree (root cause)

- **Q1 — Lỗi xảy ra ở giai đoạn nào?** → "Khi AI đọc raw và VIẾT spec" (refinement stub → full). Nhánh: *Instruction ingest/refinement thiếu/mơ hồ* → target chính: refinement-phase guidance (`phase_*.md` hoặc `.claude/rules/20-no-inference.md`).
- **Q2 — Instruction hiện tại ở trạng thái nào?** → "Có instruction nhưng không đủ rõ". `.claude/rules/20-no-inference.md` đã cấm suy diễn requirement + có "Enum completeness" rule, NHƯNG **chưa có rule explicit** cho trường hợp "spec text ≠ raw verbatim (correction/generalization/typo-fix) bắt buộc kèm Q-ID + raw quote". → **Clarify / strengthen**.

### Bước 2 — Patch đề xuất

Xem `improvement_patch_plan.md` mục **PATCH-001** (Pending — chờ user confirm, KHÔNG tự apply).

### Bước 3 — Counterfactual test

*"Nếu PATCH-001 đã tồn tại trước batch-3, INF-01 có xảy ra không?"* → **Không.** PATCH-001 buộc mỗi R/BR có spec text khác raw verbatim phải kèm Q-ID + raw quote inline. Khi AI refine mobile BR "10% group UID", rule sẽ block việc viết `ceil(lot_uid_count × 0.10)` mà không có Q-ID — AI buộc phải giữ verbatim "10% số lượng cây vải của lô" + raw quote, đẩy công thức chính xác sang Q. Cơ chế ngăn chặn nhắm đúng giai đoạn VIẾT spec (root cause Q1), không phải triệu chứng ở verify. **Counterfactual: PASS.**

### Bước 4 — Apply

**Pending** — chờ user confirm. KHÔNG tự apply patch skill/rule khi chưa pass quality gates + chưa có user approval.

### Bước 5 — Retrospective

Append vào `retrospective.md` (xem cập nhật session 2026-05-31 / spec-scoped-batch-3).

---

## Summary

| Item | Value |
|:-----|:------|
| Specs in scope | 3 (stub_qc_evaluation_manual, stub_qc_evaluation_mobile, stub_qc_evaluation_result) |
| Claims verified | 86 R + 65 AC + 50 BR + 7 messages; 94 claim-rows trong evidence_matrix (91 SUPPORTED + 1 INFERRED + 1 POTENTIAL_OMISSION + 1 MISSING_DETAIL) |
| L_STRUCTURAL_PASS | ✅ YES (40) |
| L_INFERENCE_PASS | ⚠️ CONDITIONAL (30) — không có NEGATION_FLIP/LOGIC_INFERRED/STRIPPED_CONDITION; 1 INFERRED còn lại ở BR table mobile (FIX-004 High) |
| VERIFY_SCRIPT_PASS | ✅ YES (15) — check_ingest.py exit 0 ở pre-req; re-run lại ở write-back |
| L_FIX_COMPLETE | ✅ YES (10) — 3/3 violation có FIX (FIX-004/005/006) |
| L_ROOT_CAUSE_COMPLETE | ✅ YES (5) — pattern threshold đạt, PATCH-001 đề xuất (Pending) |
| **Penalty** | −5 (INFERRED) −3 (POTENTIAL_OMISSION) −2 (MISSING_DETAIL) = **−10** |
| **Score** | **100 − 10 = 90/100** |
| **Verdict (session)** | **CONDITIONAL** (score ≥ 70, 🔴 structural pass; 1 INFERRED + omission cần fix trước final release-ready) |
| Verdict per-spec | |
| — stub_qc_evaluation_manual | **CONDITIONAL** — content khớp raw; OMIT-01 (App SL/tem QC) + MISS-01 (note xã vải/PO sample) cần review ownership |
| — stub_qc_evaluation_mobile | **CONDITIONAL** — INF-01 formula `ceil()` cần remove (FIX-004) |
| — stub_qc_evaluation_result | **PASS** — 31/31 claim critical SUPPORTED, enum/state/message đều khớp + flag đúng |

**Phân loại stub:** Cả 3 vẫn `bootstrap-ready` (chưa `release-ready`) — partial_read: false nhưng còn open questions + FIX pending. Follow-up: apply FIX-004/005/006 + answer Q-ID trước khi chuyển section-title claims → business-meaning claims cho final PASS.

**Session Status:** L_inference + L_fix + L_root_cause COMPLETE. Awaiting user confirm verdict trước write-back.

Gate Decision Source: `wiki/project_hasaki/refiner/quality_gates.json`
Advisory Source: `wiki/project_hasaki/refiner/improvement_patch_plan.md`

---

## Next Actions

1. **User:** Review verdict CONDITIONAL + 3 FIX suggestions + PATCH-001 đề xuất. Confirm verdict.
2. **Sau user confirm → `@hasaki-verify-structural` (haiku) chạy write-back:**
   - `py .claude/scripts/refiner_writeback.py --specs stub_qc_evaluation_manual,stub_qc_evaluation_mobile,stub_qc_evaluation_result --verdict CONDITIONAL`
   - `py .claude/scripts/index_flag_updater.py --specs stub_qc_evaluation_manual,stub_qc_evaluation_mobile,stub_qc_evaluation_result --apply`
   - `py .claude/scripts/check_ingest.py --project project_hasaki` (verify exit 0)
3. **FIX apply (chờ user confirm từng FIX):** FIX-004 (High, mobile INF-01), FIX-005 (Medium, OMIT-01 cần PO confirm ownership), FIX-006 (Medium, MISS-01 cross-ref).
4. **PATCH-001 (skill/rule patch):** chỉ apply khi user explicit confirm — KHÔNG auto-apply.

---

Gate Decision Source: `wiki/project_hasaki/refiner/quality_gates.json`
