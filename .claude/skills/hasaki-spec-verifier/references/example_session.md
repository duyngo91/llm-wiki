---
tags: [wiki-rules, reference, refiner, example]
status: Done
updated: 2026-05-30
---

# Refiner Worked Example — Spec-scoped batch 3 specs

> Walkthrough thực tế của 1 session refiner, từ trigger đến write-back. Dùng làm reference khi AI mới invoke skill chưa rõ workflow order. Case study dựa trên session 2026-05-30 spec-scoped-batch-2.

---

## Bối cảnh

User vừa refine 3 stubs xong: `stub_receiving_po_inbound_shipment` (07062 v2.17), `stub_qc_criteria_sku` (07105 v1.5), `stub_qc_vas` (07105 v1.5). Mỗi spec ~20-36 R-IDs với enum / state transition / error messages / formula. User gọi:

```
/hasaki-spec-verifier Spec-scoped 3 stubs: stub_receiving_po_inbound_shipment, stub_qc_criteria_sku, stub_qc_vas
```

**Trigger:** "Sau refine stub → full spec (Gate 1B promotion)" → **Mode: Spec-scoped**.

---

## Bước 1 — Pre-req existence + freshness check

AI Glob 4 file pipeline reports:

```bash
ls wiki/project_hasaki/evidence_index.json \
   wiki/project_hasaki/refiner/source_refs_report.json \
   wiki/project_hasaki/refiner/coverage_gap_report.json \
   wiki/project_hasaki/refiner/quality_gates.json
```

Existence: ✅ all 4. **Step 2 freshness check:**

```python
# Inspect evidence_index for our 3 specs
for spec in ['stub_receiving_po_inbound_shipment', 'stub_qc_criteria_sku', 'stub_qc_vas']:
    matches = [r for r in evidence_index['records'] if r['feature'] == spec]
    # → 0 matches for all 3 (stale — chỉ có pilot-batch-1 data)
```

**Stale detected** → AI tự chạy `py .claude/scripts/check_ingest.py --project project_hasaki` (read-only, không cần user confirm). Exit 0. 4 stages clean.

**Refresh xong:** evidence_index có 49 + 76 + 48 = 173 records cho 3 specs. source_refs có 21 + 36 + 18 = 75 findings `OK_CANONICAL`. Tiếp tục.

---

## Bước 2 — Pre-scan delta

AI đọc `quality_gates.json` session gần nhất (pilot-batch-1). Cho mỗi spec trong scope:

| Spec | source_version | last_verified_source_version | verification_status | Trong session trước? | Phân loại |
|:-----|:--------------:|:----------------------------:|:--------------------|:--------------------:|:----------|
| stub_receiving_po_inbound_shipment | 2.17 | (missing) | Pending | ❌ | Verify đầy đủ |
| stub_qc_criteria_sku | 1.5 | (missing) | Pending | ❌ | Verify đầy đủ |
| stub_qc_vas | 1.5 | (missing) | Pending | ❌ | Verify đầy đủ |

Tất cả 3 specs cần verify đầy đủ — ghi scope vào header `refiner_report.md`.

---

## Bước 3 — L_structural

AI **không tự đọc raw** ở tầng này — chỉ đọc reports đã pre-computed.

**Inputs đọc:**
- `evidence_index.json` (1531 records, filter 173 cho 3 specs)
- `source_refs_report.json` summary: `{"OK_CANONICAL": 528}` → 75 findings cho 3 specs đều OK
- `coverage_gap_report.json`: `findings: []` (no gaps)

**Checks:**

| Check | Kết quả |
|:------|:--------|
| Source format invalid (INVALID_FORMAT / RAW_NOT_FOUND) | 0 cho 3 specs |
| Source line out of range (OUT_OF_RANGE) | 0 |
| Section unmapped | 0 |
| Section underreported (gap_ratio < 0.5) | 0 |
| Section `coverage_status: full` mà `read_log: null` | 0 (read_log.claims_extracted > 0) |
| AC ID format `AC-NN` | ✅ 37 AC pass |
| Stub `partial_read: false` → không trigger Blocked Coverage requirement | OK |
| Flag `has_enum: true` vs spec | ⚠️ **Note (advisory, không phải violation):** index `flags=[]` cho mọi sections nhưng spec content có enum / state_transition / business_rule. Pattern lặp với pilot-batch-1. Defer cho `index_flag_updater.py` apply riêng. |

L_structural: **0 violations**. Output ghi vào `refiner_report.md` mục `## L_structural`.

---

## Bước 4 — L_inference

### 4.1 — Liệt kê claims

AI lấy danh sách claims từ `evidence_index.json` cho 3 specs:
- inbound_shipment: 20 R + 11 AC + 10 BR + 4 messages = 45 claims
- criteria_sku: 36 R + 14 AC + 16 BR + 6 messages = 72 claims
- vas: 18 R + 12 AC + 10 BR + 3 messages = 43 claims

**Tổng:** 160 claims.

### 4.2 — Verify scope filter

Index `flags=[]` (legacy gap) — AI manually treat enum / BR / formula / error / state_transition là critical claims → verify 100%. Non-critical (UI label trivial) → sampling 1/5.

### 4.3 — Đọc raw từng spec (raw-first, anti-bias)

Đọc range mapped:
- inbound_shipment: `07062.md` L223-L347 (S-05 + S-06)
- criteria_sku: `07105.md` L191-L432 (S-07 + S-08)
- vas: `07105.md` L695-L780 (S-17 + S-18)

**Quy tắc anti-bias:** trước khi đọc claim của spec, viết ra raw nói gì — không paraphrase spec.

### 4.4 — Apply decision tree

Ví dụ minh họa 4 claims:

**Claim 1 — inbound_shipment R007 DESC-INS-004**

Spec: `SKU tester {sku_code} chưa khai báo SKU gốc` (placeholder `{sku_code}`)
Raw L260-L262: `SKU tester 422225215 chưa khai báo SKU gốc` (literal SKU number)

Decision tree:
- Q1. #line đúng format, nội dung match chủ đề → tiếp Q2.
- Q2. Raw có statement support → tiếp Q3.
- Q3. Spec generalize literal "422225215" thành placeholder `{sku_code}` → match nhánh **"Raw có numerical value cụ thể; spec generalize thành placeholder" → INFERRED.**

**Nhưng** spec đã có Q-003 capture concern này trong "Câu hỏi chưa rõ" → softened to **UNCLEAR** (per UNCLEAR boundary rule). Penalty -1 thay vì -5.

Action: keep label, Q-003 stay, không cần FIX (đã captured).

---

**Claim 2 — criteria_sku R008 (filter date range)**

Spec: `Đến ngày phải ≥ Từ ngày` (business-logic standard)
Raw L249: `Đến ngày phải lớn hơn hoặc bằng đến ngày` (raw typo — should be "Từ ngày")

Decision tree:
- Q1. #line match chủ đề → tiếp Q2.
- Q2. Raw có statement → tiếp Q3.
- Q3. Spec không generalize, không drop modifier, không đảo logic, không miss detail → tiếp Q4.
- Q4. **Raw có typo (mâu thuẫn nội bộ)** → **UNCLEAR**.

**Nhưng** spec đã silent correct typo, KHÔNG có Q-ID capture → vi phạm "UNCLEAR must have Q-ID". Penalty -1 + FIX-002 generate Q-011.

Action: FIX-002 add Q-011 `Raw L249 có typo "Đến ngày ≥ đến ngày" — confirm interpretation`.

---

**Claim 3 — criteria_sku R027 (Sai số scope)**

Spec: "Sai số cho phép áp dụng cho `=`, `>`, `>=`, `<`, `<=`" (5 operators)
Raw L383-L406: chỉ explicit "Sai số cho phép" ở toán tử `=` (L387-L388); `>`, `>=`, `<`, `<=` (L395-L401) **không nhắc Sai số**.

Decision tree:
- Q1. #line match → tiếp Q2.
- Q2. Raw có statement về `=` Sai số, nhưng raw không nói gì về Sai số cho 4 operators còn lại → spec extend → tiếp Q3.
- Q3. Spec tự ghép "rule cho `=`" + "operators tương tự" → behavior full statement không có raw → **LOGIC_INFERRED**. Penalty -8.

Wait — kiểm tra lại: spec interpret raw structure (Sai số listed for `=`, omitted in `>` due to compact format). Có 2 cách interpret. Raw không clear → có thể là **UNCLEAR**.

Pick severity cao hơn theo tie-breaker: **LOGIC_INFERRED**. Penalty -8.

**Nhưng** spec không có Q-ID capture concern → FIX-003 generate Q-012 + softened to UNCLEAR (do raw thực sự ambiguous, không phải spec sai). Penalty -1.

Action: FIX-003 add Q-012 + lower R027 Testable ✅ → ⚠️.

---

**Claim 4 — vas R018 (10% group UID formula)**

Spec: `vas_count = ceil(group_uid_count × 0.10)` cho SKU vải, type QC. VD: 25 → 3.
Raw L775-L780: "Update 18-09-2025 — Update Group UID cho type Quality control với các SKU vải. 1 SKU nhận trong ASN theo group UID sẽ lấy ra 10% để thực hiện đánh giá. VD: SKUA nhận trong ASN là 25 group UID thì 10% là 2,5 làm tròn lên thành 3, tức sẽ có 3 dòng VAS cần đánh giá chất lượng cho SKUA"

Decision tree:
- Q1. #line match → tiếp Q2.
- Q2. Raw có statement → tiếp Q3.
- Q3. Spec verbatim match content + formula → tiếp Q4.
- Q4. Raw rõ ràng, spec rõ ràng → **SUPPORTED**.

Action: keep.

### 4.5 — Tổng hợp labels

Sau khi đi qua toàn bộ 160 claims:

| Spec | SUPPORTED | UNCLEAR | INFERRED | LOGIC_INFERRED | STRIPPED | NEGATION | PHANTOM | POTENTIAL | MISSING |
|:-----|:---------:|:-------:|:--------:|:--------------:|:--------:|:--------:|:-------:|:---------:|:-------:|
| inbound_shipment | 44 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| criteria_sku | 70 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| vas | 42 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

2 POTENTIAL_OMISSION trong criteria_sku → FIX-002 + FIX-003.

---

## Bước 5 — L_fix

Generate FIX-NNN cho 2 POTENTIAL_OMISSION theo template trong `templates/refiner_report.template.md`:

```
### FIX-002: Thêm Q-011 cho raw typo R008
- File: wiki/project_hasaki/features/stub_qc_criteria_sku.md
- Vùng: R008 (dòng 55) + Q section + Blocked Coverage
- Vấn đề: L_inference POTENTIAL_OMISSION — spec silent correct raw typo
- Gợi ý: Add Q-011 vào Q section; lower R008 Testable ✅→⚠️
- Ưu tiên: Medium

### FIX-003: Thêm Q-012 cho Sai số scope R027
- File: wiki/project_hasaki/features/stub_qc_criteria_sku.md
- Vùng: R027 (dòng 74) + Q section + Blocked Coverage
- Vấn đề: L_inference POTENTIAL_OMISSION — spec assume cho 5 operators, raw chỉ explicit 1
- Gợi ý: Add Q-012; lower R027 Testable ✅→⚠️
- Ưu tiên: Medium
```

**Không tự apply** — chờ user confirm. (Session này user said "apply FIX-002 và FIX-003" → AI apply sau, không phải trong session refiner gốc.)

---

## Bước 6 — L_root_cause (pattern analysis)

Đếm cùng-loại-violation:
- POTENTIAL_OMISSION = 2 trong cùng 1 spec (cùng spec, cùng kind nhưng khác cause). Không đủ trigger trong batch alone.
- Cross-session: pilot-batch-1 đã có FIX-001 (gift→gốc typo correction) cùng pattern. **2 sessions liên tiếp = pattern lặp.**

→ **Không short-circuit.** Apply L_root_cause Bước 0-5 từ `references/l5_root_cause.md`.

Bước 0 — Generalization: "Silent spec interpretation when raw is ambiguous/typo" — class of error covers (a) raw typo, (b) ambiguous boundary, (c) implicit scope. Mọi case spec làm rõ raw mà không Q-ID.

Bước 1 — Decision tree → "Khi AI đọc raw và VIẾT spec → Instruction ingest thiếu/mơ hồ → target `phase_test_design.md` checklist."

Bước 2 — Patch candidate: thêm checklist "Mỗi R-ID có spec text ≠ raw verbatim → bắt buộc có Q-ID kèm raw quote."

Bước 3 — Counterfactual: "Nếu patch đã có trước session 1, FIX-001 / FIX-002 / FIX-003 có xảy ra không?" → KHÔNG, spec writer sẽ thấy checklist và add Q ngay. Patch nhắm đúng root cause.

Bước 4 — Apply patch: **chờ thêm 1 session nữa xác nhận** (đã 2/3 sessions). Ghi vào `improvement_patch_plan.md` Pending observations.

Bước 5 — Retrospective: append entry vào `retrospective.md`.

---

## Bước 7 — Compute quality gates

Per `references/scoring.md`:

| Gate | Pass/Fail | Score |
|:-----|:---------:|:-----:|
| `L_STRUCTURAL_PASS` | ✅ | 40 |
| `L_INFERENCE_PASS` | ✅ (POTENTIAL_OMISSION có FIX) | 30 |
| `VERIFY_SCRIPT_PASS` | ✅ (check_ingest exit 0) | 15 |
| `L_FIX_COMPLETE` | ✅ (2 FIX generated) | 10 |
| `L_ROOT_CAUSE_COMPLETE` | ✅ (analyzed + deferred) | 5 |
| **Base** | | **100** |

Penalty:
- 2 POTENTIAL_OMISSION chưa fix in-session: -3 × 2 = **-6**
- 2 UNCLEAR có Q-ID kèm (Q-003 + V's Q-001): -0 (UNCLEAR penalty -1 chỉ khi không có Q-ID, đây có) = **0**

Bonus:
- Session này User confirm apply FIX → 2 POTENTIAL_OMISSION đã add R-ID trong cùng session (lượt sau của session): **+2**

**Score final = 100 - 6 + 2 = 96/100. Verdict: PASS.**

Per-spec verdict:
- inbound_shipment: PASS (clean)
- criteria_sku: PASS (2 FIX applied)
- vas: PASS (clean)

Append session vào `quality_gates.json`:

```json
{
  "session": "2026-05-30",
  "batch": "spec-scoped-batch-2",
  "mode": "Spec-scoped",
  "specs_in_scope": ["stub_receiving_po_inbound_shipment", "stub_qc_criteria_sku", "stub_qc_vas"],
  "score_after": 96,
  "gates": { ... all true ... },
  "violations": { "potential_omission": 2, "unclear": 2, ... },
  "verdict": "PASS",
  "verdict_per_spec": { ... all PASS ... },
  "fix_suggestions": ["FIX-002", "FIX-003"]
}
```

---

## Bước 8 — Write-back (state-changing, user confirm)

**STOP — yêu cầu user confirm verdict + scope trước khi chạy state-changing scripts.**

User OK → chạy:

```bash
# 1. Spec frontmatter + index sections
py .claude/scripts/refiner_writeback.py --project project_hasaki \
   --specs stub_receiving_po_inbound_shipment,stub_qc_criteria_sku,stub_qc_vas \
   --verdict PASS

# 2. Index flags propagate (sau khi spec nội dung đã refined)
py .claude/scripts/index_flag_updater.py --project project_hasaki \
   --specs stub_receiving_po_inbound_shipment,stub_qc_criteria_sku,stub_qc_vas \
   --apply

# 3. Final VERIFY_SCRIPT_PASS gate
py .claude/scripts/check_ingest.py --project project_hasaki
# Expect: worst_exit_code: 0
```

Sau đó:
- Spec frontmatter: `last_verified_at: 2026-05-30 21:25:00`, `verification_status: Verified`, `last_verified_source_version: 1.5` (hoặc 2.17 cho inbound_shipment).
- Raw `*_index.json` sections (S-05, S-06, S-07, S-08, S-17, S-18): `range_status: verified`, `last_verified_version: <version>`.

---

## Bước 9 — Apply FIX (separate user action)

User confirm "apply FIX-002 và FIX-003" → AI Edit `stub_qc_criteria_sku.md`:
- Add Q-011, Q-012 vào Q section
- Lower R008, R027 Testable ✅ → ⚠️
- Add 2 dòng vào Blocked Coverage
- Append v1.2 changelog entry

Re-run `check_ingest.py` → exit 0. Q count 246 → 248.

---

## Done Criteria

✅ `refiner_report.md` đầy đủ 4 mục (L_structural / L_inference / L_fix / Summary)
✅ `evidence_matrix.md` 160 claims per-claim
✅ `quality_gates.json` append session với score 96, verdict PASS
✅ Write-back applied vào index.json + spec frontmatter (qua scripts, không manual)
✅ FIX-002 + FIX-003 applied (user explicit confirm)
✅ `improvement_patch_plan.md` + `retrospective.md` ghi cross-session pattern

---

## Lessons cho session sau

1. **Pre-req freshness check là MANDATORY** — file tồn tại không đảm bảo data fresh. Inspect evidence_index records cho specs in scope; missing → auto-refresh.
2. **Glob `.claude/scripts/*.py` ĐẦU TIÊN** — đừng viết script tạm. Tonight có sẵn `refiner_writeback.py` + `index_flag_updater.py`.
3. **UNCLEAR boundary** — chỉ raw bất thường (typo, ambiguous). Spec interpret raw rõ → INFERRED hoặc LOGIC_INFERRED.
4. **POTENTIAL_OMISSION có penalty -3** — không phải free pass. Nếu in-session bổ sung Q-ID → bonus +1 offset partial.
5. **Cross-session pattern detect cần ≥ 2 sessions liên tiếp** trước khi propose skill patch chính thức.
