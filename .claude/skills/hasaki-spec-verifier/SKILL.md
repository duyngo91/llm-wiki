---
name: hasaki-spec-verifier
description: QA verifier kiểm chứng ngược claim wiki → raw evidence. Chạy sau ingest fresh / ingest version mới / task change update spec / refine stub→full. 3 tầng L_structural → L_inference → L_root_cause. Output `wiki/<project>/refiner/`.
metadata:
  author: Yen Ngo
  version: "3.2"
  renamed_from: hasaki-skill-refiner
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
---

# Hasaki Spec Verifier

> **Rename note (2026-05-30):** Trước đây tên `hasaki-skill-refiner`. Đổi thành `hasaki-spec-verifier` để phản ánh đúng workload chính (verify claim→raw, ~95%); L_root_cause skill self-patch là phần thiểu số (~5%). Output folder vẫn `wiki/<project>/refiner/` — không migrate paths.

## Mục tiêu

Kiểm chứng ngược từng claim trong wiki so với raw source, phát hiện gap coverage, lỗi suy diễn, và đề xuất patch có kiểm soát.

**3 tầng tuần tự — `L_structural` → `L_inference` → `L_root_cause`.** L_root_cause có **short-circuit**: skip khi không có pattern lặp.

---

## Tooling — Helper scripts (BẮT BUỘC dùng, không reinvent)

Trước khi viết bất kỳ script tạm hoặc edit file tay, **luôn dùng các script đã có sẵn dưới đây**. Cùng workflow đã chạy thành công nhiều session — đừng tái phát minh.

| Khi nào dùng | Script | Read-only? | Lệnh tiêu chuẩn |
|:-------------|:-------|:----------:|:-----------------|
| Pre-req refresh / cuối session VERIFY_SCRIPT_PASS gate | `check_ingest.py` | ✅ | `py .claude/scripts/check_ingest.py --project <p>` |
| L_structural phantom debug nhanh | `refiner_findings_diag.py` | ✅ | `py .claude/scripts/refiner_findings_diag.py --project <p> [--json]` |
| Cuối session — write-back verdict | `refiner_writeback.py` | ❌ state-changing | `py .claude/scripts/refiner_writeback.py --project <p> --specs s1,s2 --verdict PASS [--approval-note "..."]` |
| Cuối session — propagate flags vào raw index | `index_flag_updater.py` | ❌ state-changing (với `--apply`) | `py .claude/scripts/index_flag_updater.py --project <p> --specs s1,s2 [--apply]` (default dry-run) |
| Bất kỳ lúc nào — xem progress | `spec_status_dashboard.py` | ✅ | `py .claude/scripts/spec_status_dashboard.py --project <p>` |

**Rule auto vs ask:**
- Read-only scripts (`check_ingest`, `refiner_findings_diag`, `spec_status_dashboard`, dry-run `index_flag_updater`): **AI tự chạy** khi cần refresh hoặc debug.
- State-changing (`refiner_writeback`, `index_flag_updater --apply`): **chỉ chạy khi user confirm** verdict + scope.

**Workflow walkthrough đầy đủ:** xem `references/example_session.md` — case study 1 session refiner thật từ trigger → write-back, 9 bước cụ thể với 4 ví dụ decision tree, lessons rút ra.

---

## Khi nào chạy

Refiner chỉ có ý nghĩa khi AI vừa **sinh claim mới** hoặc **cập nhật claim cũ** dựa trên raw source.

| Trigger | Mode | Phạm vi verify |
|:--------|:-----|:---------------|
| Sau ingest PDF fresh (workflow 2.1) | **Full** | Toàn bộ Feature/API Spec trong batch |
| Sau ingest version mới (workflow 2.1b) | **Delta** | Chỉ sections có `change_history` mới |
| Sau task change (workflow 2.2) update spec | **Delta** | Chỉ Feature/API Spec bị task update |
| Sau refine stub → full spec (Gate 1B promotion) | **Spec-scoped** | Riêng spec vừa promote |

**Không chạy ở:** task intake, test design, daily sync, lint & sync, state transition, CR Go-Live.

### Mode behavior

- **Full:** Pre-scan delta xác định scope từ `quality_gates.json`; specs đã PASS ở session trước và `source_version` không đổi → skip deep scan.
- **Delta:** Chỉ load index sections có `change_history` ≠ empty hoặc spec có `last_verified_at` cũ hơn `updated_at`.
- **Spec-scoped:** Lock phạm vi vào đúng 1 spec.

---

## Pre-requisite

Trước khi chạy, đảm bảo các artifact tồn tại VÀ fresh cho specs trong scope (4 artifact sinh bởi `check_ingest.py` pipeline):

| File | Sinh bởi | Refiner dùng ở |
|:-----|:---------|:---------------|
| `raw_sources/.../{tên_file}_index.json` | `index_skeleton.py` | Tất cả tầng |
| `wiki/[project]/evidence_index.json` | `evidence_index.py` | L_structural, L_inference scope |
| `wiki/[project]/refiner/source_refs_report.json` | `verify_source_refs.py` | L_structural (format/line accuracy) |
| `wiki/[project]/refiner/coverage_gap_report.json` | `coverage_gap_estimator.py` | L_structural (underreport detect) |

### 2-step pre-req check

**Step 1 — Existence:** 4 file phải tồn tại. Thiếu file nào → AI tự chạy `py .claude/scripts/check_ingest.py --project <p>` (read-only) để sinh.

**Step 2 — Freshness (BẮT BUỘC):** Verify mỗi spec trong scope có data trong reports:

```python
# Pseudo-check (AI tự inline khi pre-scan):
for spec in scope:
    has_evidence = any(r['feature'] == spec for r in evidence_index['records'])
    has_refs = any(spec in f['spec_file'] for f in source_refs['findings'])
    if not (has_evidence and has_refs):
        # Stale reports — auto refresh
        refresh = True
```

Nếu **bất kỳ spec nào miss data** → AI tự chạy `check_ingest.py` (read-only, idempotent). Không cần user confirm cho read-only refresh.

**Common stale cause:** Spec mới refine từ stub xong nhưng quên chạy `check_ingest` — reports vẫn chứa data session trước.

---

## Output mỗi session

```
wiki/project_hasaki/refiner/
├── YYYY-MM-DD_{batch_name}/
│   ├── refiner_report.md       ← L_structural summary + L_inference issues
│   └── evidence_matrix.md      ← L_inference detail (per-claim)
├── quality_gates.json          ← append-only
├── improvement_patch_plan.md   ← L_root_cause patches (nếu có)
└── retrospective.md            ← L_root_cause lessons (hoặc "no new patterns")
```

**Templates** (start từ skeleton thay vì viết từ đầu):

| Output | Template path |
|:-------|:--------------|
| `refiner_report.md` | `.claude/skills/hasaki-spec-verifier/templates/refiner_report.template.md` |
| `evidence_matrix.md` | `.claude/skills/hasaki-spec-verifier/templates/evidence_matrix.template.md` |
| `quality_gates.json` (init lần đầu) | `.claude/skills/hasaki-spec-verifier/templates/quality_gates.template.json` |
| `improvement_patch_plan.md` (init) | `.claude/skills/hasaki-spec-verifier/templates/improvement_patch_plan.template.md` |
| `retrospective.md` (init) | `.claude/skills/hasaki-spec-verifier/templates/retrospective.template.md` |

Templates đã dùng đúng tên gate 3-tier (`L_STRUCTURAL_PASS` / `L_INFERENCE_PASS` / `VERIFY_SCRIPT_PASS` / `L_FIX_COMPLETE` / `L_ROOT_CAUSE_COMPLETE`).

---

## Pre-scan — Session Delta

Chạy trước L_structural.

1. Đọc `quality_gates.json` — lấy session gần nhất, extract `verdict_per_spec`.
2. Với từng spec trong batch hiện tại, đọc frontmatter và so:
   - `source_version` (current raw version)
   - `last_verified_source_version` (version đã verify thành công gần nhất; set bởi `refiner_writeback.py`)
   - `verification_status` (Verified / Stale / Pending)
3. Phân loại:
   - **Cần verify đầy đủ:**
     - `last_verified_source_version` missing (spec chưa verify lần nào) HOẶC
     - `source_version` ≠ `last_verified_source_version` (raw đã update) HOẶC
     - `verification_status == Stale` (session trước FAIL hoặc lệch) HOẶC
     - Session gần nhất trong `quality_gates.json` có verdict CONDITIONAL/FAIL cho spec này.
   - **Skip deep scan:**
     - `source_version == last_verified_source_version` AND `verification_status == Verified` AND session trước PASS — L_structural chạy nhanh, L_inference bỏ qua.
4. Ghi scope ở đầu `refiner_report.md`:

```
## Scope session này
- Verify đầy đủ: [files]
- Skip deep scan: [files]
```

---

## Tầng L_structural — Script-driven Quality Checks

**Mục tiêu:** AI đọc **reports đã pre-computed** trong Bước 3 của Workflow 2.1. **Không tự đọc raw để re-verify cấu trúc.**

### Inputs

- `wiki/[project]/evidence_index.json`
- `wiki/[project]/refiner/source_refs_report.json`
- `wiki/[project]/refiner/coverage_gap_report.json`
- `wiki/[project]/refiner/wiki_verify_report.*` (nếu `wiki_sync.py verify` ghi report file; nếu chỉ in stdout, AI tự re-run lấy output)

### Checks

| Check | Source | Verdict mapping |
|:------|:-------|:----------------|
| Format violations cấu trúc (14 mục thiếu, tag sai, frontmatter thiếu) | AI scan spec files theo template | `FORMAT_VIOLATION` |
| Source format invalid | `source_refs_report.json` verdict `INVALID_FORMAT` / `MISSING_SOURCE` / `RAW_NOT_FOUND` | `FORMAT_VIOLATION` |
| Source line out of range | `source_refs_report.json` verdict `OUT_OF_RANGE` | `FORMAT_VIOLATION` |
| Section unmapped | `coverage_gap_report.json` verdict `UNMAPPED` | `COVERAGE_GAP` |
| Section underreported (gap_ratio < 0.5) | `coverage_gap_report.json` verdict `UNDERREPORTED_COVERAGE` | `COVERAGE_GAP` |
| Section `coverage_status: full` mà `read_log: null` | AI scan `*_index.json` | `SUSPECT_UNREAD` (xếp vào COVERAGE_GAP) |
| Flag `has_enum: true` mà spec không có bảng enum | AI cross-check `evidence_index` `coverage_class: business_rule/requirement` | `COVERAGE_GAP` |
| AC thiếu ID format `AC-NN` | AI scan spec | `FORMAT_VIOLATION` |
| Stub `partial_read: true` không có Blocked Coverage entries | AI scan spec | `FORMAT_VIOLATION` |

### Output L_structural

Ghi vào `refiner_report.md`:

```
## L_structural — Format & Coverage

| File / Section | Loại vi phạm | Nguồn report | Action |
|:---------------|:-------------|:-------------|:-------|
```

Verdict `STALE` và `PHANTOM_EVIDENCE` từ `source_refs_report.json` → defer sang L_inference (cần đối chiếu nội dung).

---

## Tầng L_inference — Content Verification

**Mục tiêu:** Verify từng claim trong spec có bằng chứng explicit trong raw. Đây là tầng AI work chính — đọc raw, so nội dung.

### Phạm vi verify (filter theo flag để giảm IO)

**Spec `partial_read: false`:** verify theo priority:

1. **Bắt buộc verify 100%** (claims mapped đến section có flag critical):
   - `has_enum: true` → toàn bộ enum/list values
   - `has_error_messages: true` → toàn bộ Error Messages
   - `has_business_rule` / `has_validation_rule: true` → toàn bộ Business Rules
   - `has_formula` / `has_state_transition: true` → toàn bộ Formula/State Transition
2. **Sampling 1/5 cho claims còn lại** mapped đến section không có flag critical.
3. **Pre-flagged từ `source_refs_report.json`:**
   - Verdict `PHANTOM_EVIDENCE` → label trực tiếp `PHANTOM_EVIDENCE`, không spot-check.
   - Verdict `STALE` → re-verify content (raw có thể đã thay đổi nhưng spec chưa update).

**Stub (`partial_read: true`):** Chỉ verify phần đã đọc. Ghi `[STUB — section chưa đọc]` trong evidence_matrix.

### Quy trình verify

**Bước 1 — Liệt kê claims:** đọc `evidence_index.json`, lấy claims theo priority. Ghi nhận danh sách, chưa phân tích.

**Bước 2 — Đọc raw theo flag:**
- **Claim mapped đến section có flag critical (raw-first):** đọc raw range trước, viết ra những gì raw nói bằng lời của raw, không dùng ngôn ngữ của spec. Chống confirmation bias.
- **Claim trivial:** đã được L_structural cover. Skip read.

**Bước 3 — Label claim theo decision tree (single source of truth):**

Đi qua các nhánh theo thứ tự — dừng ở match đầu tiên. Decision tree này thay thế bảng "5 checks" + bảng "Labels" + heuristic "3 câu hỏi" cũ.

```
─ Q1. #line tham chiếu đúng format. Mở raw tại #line đó.
  Nội dung TẠI dòng đó có đề cập đến chủ đề của claim không?
  ├── KHÔNG (line nói chuyện khác / blank / heading khác)
  │   → PHANTOM_EVIDENCE  (Action: fix reference hoặc reclassify)
  └── CÓ → tiếp Q2.

─ Q2. Raw (tại range mapped) có statement support claim không?
  ├── KHÔNG có statement nào liên quan
  │   ├── Raw có statement TƯỚNG TỰ nhưng spec MISS (chưa add R-ID)
  │   │   → POTENTIAL_OMISSION  (Action: review + thêm vào spec)
  │   └── Hoàn toàn không có
  │       → INFERRED  (Action: remove khỏi mô tả chính)
  └── CÓ → tiếp Q3.

─ Q3. Spec rephrase / generalize / drop info gì từ raw không?
  ├── Raw có numerical/enum value cụ thể; spec generalize thành placeholder
  │   (vd raw "SKU 422280022", spec "{sku_code}"; raw "5 values", spec "4 values")
  │   → INFERRED  (Action: remove generalization, dùng verbatim)
  │
  ├── Raw có components A + B riêng; spec tự ghép thành behavior/formula
  │   (vd raw "field X bắt buộc", "field Y bắt buộc"; spec "X và Y validate cùng lúc")
  │   → LOGIC_INFERRED  (Action: remove conclusion không có raw)
  │
  ├── Raw có modifier (Khi/Nếu/Chỉ khi/Trừ khi/actor) mà spec DROP
  │   (vd raw "Khi user là Admin, được sửa"; spec "Được sửa")
  │   → STRIPPED_CONDITION  (Action: add modifier back)
  │
  ├── Raw phủ định (không/chưa/KHÔNG); spec đảo logic
  │   (vd raw "không cho sửa sau khi approve"; spec "cho sửa sau khi approve")
  │   → NEGATION_FLIP  (Action: reverse claim)
  │
  ├── Raw + spec match content; nhưng spec thiếu side-effect / note phụ
  │   (vd raw "submit + gửi email + ghi audit log"; spec "submit + gửi email")
  │   → MISSING_DETAIL  (Action: add detail vào spec)
  │
  └── Match verbatim, không rephrase → tiếp Q4.

─ Q4. Raw có ambiguous / typo / boundary không rõ?
  ├── Raw có typo / từ ngữ mâu thuẫn / boundary không rõ; spec làm rõ
  │   (vd raw "Đến ngày phải ≥ đến ngày" — typo; spec interpret "Đến ngày ≥ Từ ngày")
  │   → UNCLEAR  (Action: add Q-ID vào "Câu hỏi chưa rõ" + Blocked Coverage)
  └── Raw rõ ràng, spec rõ ràng, match
      → SUPPORTED  (Action: keep)
```

**Tie-breaker:** Nếu claim hit ≥ 2 nhánh, pick label có severity cao nhất (NEGATION_FLIP > STRIPPED_CONDITION > LOGIC_INFERRED > INFERRED > PHANTOM_EVIDENCE > POTENTIAL_OMISSION > MISSING_DETAIL > UNCLEAR > SUPPORTED).

**UNCLEAR boundary rule (quan trọng):** UNCLEAR CHỈ áp dụng khi **raw bất thường** (typo, ambiguous). Nếu **spec interpret/generalize** từ raw rõ ràng → label thành INFERRED hoặc LOGIC_INFERRED, KHÔNG phải UNCLEAR. Tránh dùng UNCLEAR làm "no penalty escape hatch".

### Labels summary

| Label | Severity (penalty/bonus) | Trigger nhánh | Action |
|:------|:------------------------:|:--------------|:-------|
| `SUPPORTED` | 0 | Q4 → match | Keep |
| `UNCLEAR` | 0 | Q4 → raw bất thường | Move to `## ❓ Câu hỏi chưa rõ` + Blocked Coverage |
| `MISSING_DETAIL` | -2 (chưa fix) / +1 (đã fix) | Q3 → spec thiếu detail | Add detail vào spec |
| `POTENTIAL_OMISSION` | -3 | Q2 → raw có claim mà spec miss | Review + thêm R-ID |
| `PHANTOM_EVIDENCE` | -3 | Q1 → #line không match content | Fix reference |
| `INFERRED` | -5 | Q2 / Q3 generalize | Remove khỏi mô tả |
| `STRIPPED_CONDITION` | -5 | Q3 modifier dropped | Add modifier back |
| `LOGIC_INFERRED` | -8 | Q3 spec tự ghép | Remove conclusion |
| `NEGATION_FLIP` | -8 | Q3 logic đảo | Reverse claim |

### Output L_inference

Cập nhật `evidence_matrix.md` theo template `templates/evidence_matrix.template.md`. Mỗi row: `Raw Evidence (path#line) | Wiki Claim (path#line) | Status (label từ decision tree) | Action`.

---

## L_fix — Fix Suggestions (auto-template)

**Skip khi:** `L_structural.violations + L_inference.violations = 0`. Ghi `## L_fix: none required`.

### Quy trình

1. Tổng hợp tất cả violations từ L_structural + L_inference.
2. Với mỗi violation, generate suggestion theo skeleton:

```
### FIX-NNN: [Mô tả ngắn]
- **File:** wiki/project_hasaki/features/xxx.md
- **Vùng:** dòng hoặc section cụ thể
- **Vấn đề:** [L_structural/L_inference] — mô tả vi phạm + link đến report finding
- **Gợi ý:** nội dung cụ thể cần thêm/sửa/xóa
- **Ưu tiên:** Critical / High / Medium (Critical = gate bắt buộc fail)
```

3. **Không tự apply** — chỉ suggest, chờ user confirm.

### Output L_fix

Ghi vào `refiner_report.md`, mục `## L_fix — Suggestions`.

L_fix là **substep của L_inference output**, không phải tầng riêng. Có thể chạy chung pass với L_inference.

---

## Tầng L_root_cause — Skill Patch Analysis (short-circuit)

**Skip toàn bộ L_root_cause khi:** không có `cùng-loại-violation ≥ 2` trong batch **và** không có pattern lặp giữa session này với session trước trong `quality_gates.json`. Ghi `no new patterns` 1 dòng vào `retrospective.md`.

**Khi không skip:** load `references/l5_root_cause.md` để thực hiện Bước 0-5 (Generalization check, Decision Tree, Counterfactual test, Apply patch).

---

## Quality Gates & Scoring

Sau L_structural + L_inference (+ L_fix nếu chạy) → load `references/scoring.md` để compute gates, penalty, bonus, verdict. Append session vào `quality_gates.json`.

### Mapping gates 5-tier → 3-tier

| Gate cũ (5 tầng) | Gate mới (3 tầng) |
|:------------------|:------------------|
| `L1_FORMAT_PASS` | `L_STRUCTURAL_PASS` (gộp format + coverage) |
| `L2_COVERAGE_PASS` | (cùng `L_STRUCTURAL_PASS`) |
| `L3_NO_INFERENCE_PASS` | `L_INFERENCE_PASS` |
| `L4_SUGGESTIONS_COMPLETE` | (substep, vẫn track riêng) |
| `L5_ROOT_CAUSE_COMPLETE` | `L_ROOT_CAUSE_COMPLETE` |

`scoring.md` có chi tiết điểm số và penalty/bonus.

---

## Write-back sau verify (bắt buộc)

Refiner là **owner write** của một số field (xem `hasaki-wiki/references/shared.md#field-ownership-matrix`). Sau khi compute verdict, **trước khi đóng session**, refiner phải cập nhật:

### Trong `index.json` của raw source liên quan

Cho mỗi `section` đã được verify trong L_inference:

| Field | Cập nhật khi | Giá trị mới |
|:------|:-------------|:------------|
| `range_status` | Spot-check 20% trong section pass (không có PHANTOM_EVIDENCE) | `verified` |
| `last_verified_version` | Toàn bộ claims mapped đến section đã verify PASS hoặc CONDITIONAL | = `source_version` của session hiện tại |

`range_status` giữ `needs_review` nếu có bất kỳ claim nào còn `INFERRED` / `LOGIC_INFERRED` / `PHANTOM_EVIDENCE`.

### Trong Feature Spec frontmatter

Cho mỗi spec trong scope verify:

| Field | Verdict spec đạt | Giá trị mới |
|:------|:----------------|:------------|
| `last_verified_at` | Mọi verdict (PASS/CONDITIONAL/FAIL) | Timestamp UTC+07 hiện tại |
| `verification_status` | PASS | `Verified` |
| `verification_status` | CONDITIONAL | `Verified` (kèm note Critical fixes trong refiner_report) |
| `verification_status` | FAIL hoặc `source_version` lệch | `Stale` |

**Không touch field khác** — đó là owner write của wiki (xem matrix).

### Helper scripts (BẮT BUỘC dùng, không reinvent)

`.claude/scripts/` đã có sẵn các script automate write-back. Không tự viết script tạm hoặc edit từng file tay.

| Script | Mục đích | Cách gọi |
|:-------|:---------|:---------|
| `refiner_writeback.py` | Update spec frontmatter (`last_verified_at`, `verification_status`, optional `approval_note`) + raw `*_index.json` sections (`range_status`, `last_verified_version`). Idempotent. | `py .claude/scripts/refiner_writeback.py --project <p> --specs s1,s2 --verdict PASS [--approval-note "..."] [--dry-run]` |
| `index_flag_updater.py` | Scan spec content → detect signatures (enum / error_messages / business_rule / validation_rule / formula / state_transition) → propagate vào `index.json` flags cho sections map tới spec. Cần chạy sau khi refine stub → full để pre-scan delta đúng ở session sau. | `py .claude/scripts/index_flag_updater.py --project <p> [--specs s1,s2] [--apply]` (default dry-run) |
| `refiner_findings_diag.py` | Pretty-print non-OK findings từ `source_refs_report.json` — debug phantom nhanh trước khi L_structural deep dive. | `py .claude/scripts/refiner_findings_diag.py --project <p> [--json]` |

**Workflow chuẩn cuối session:**

```
1. py .claude/scripts/refiner_writeback.py --project project_hasaki --specs s1,s2,s3 --verdict PASS
2. py .claude/scripts/index_flag_updater.py --project project_hasaki --specs s1,s2,s3 --apply
3. py .claude/scripts/check_ingest.py --project project_hasaki  # verify exit 0
```

Verdict mapping của `refiner_writeback.py`:
- `PASS` / `CONDITIONAL` → `verification_status: Verified` + `range_status: verified`
- `FAIL` (hoặc `source_version` lệch) → `verification_status: Stale`, `range_status` không đổi

---

## Done Criteria

Session hoàn thành khi:
- `refiner_report.md` có đủ mục `## L_structural` / `## L_inference` / `## L_fix` (hoặc `none required`) / `## Summary`
- `evidence_matrix.md` có đủ claims theo phạm vi đã xác định
- `quality_gates.json` được append session mới
- **Write-back đã apply** vào `index.json` và Feature Spec frontmatter — không sót spec nào trong scope
- Mọi `INFERRED` và `LOGIC_INFERRED` đã được remove/fix hoặc có FIX suggestion tương ứng
- `improvement_patch_plan.md` và `retrospective.md` đã cập nhật (hoặc ghi `no new patterns`)

---

## Hard Guardrails

- Không suy diễn requirement, AC, API contract, testcase.
- Không tự apply fix vào feature/task files — chỉ suggest, chờ user confirm.
- Không tự apply patch vào skill/rule/template khi chưa pass quality gates.
- Read-only scripts (`check_ingest.py`, `refiner_findings_diag.py`, `spec_status_dashboard.py`, `index_flag_updater.py` dry-run) — AI tự chạy không cần confirm.
- State-changing scripts (`refiner_writeback.py`, `index_flag_updater.py --apply`) — yêu cầu user confirm verdict + scope trước khi chạy.
- Testcase chỉ sinh từ R/AC explicit đã được Gate 1 duyệt.
- Nội dung dựa trên Open question phải nằm ở `Blocked Coverage`.
