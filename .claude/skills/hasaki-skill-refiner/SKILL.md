---
name: hasaki-skill-refiner
description: Vòng lặp QA kiểm chứng ngược claim → raw evidence cho wiki Hasaki. Chỉ chạy khi AI vừa sinh hoặc cập nhật claim từ raw source. 4 trigger points — sau ingest PDF fresh, sau ingest version mới, sau task change update spec, sau refine stub→full spec. 3 tầng — L_structural (script-driven, AI đọc reports), L_inference (content match), L_root_cause (short-circuit). KHÔNG chạy sau /wiki-test-designer, daily sync, state transition, CR Go-Live.
metadata:
  author: Yen Ngo
  version: "3.0"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
---

# Hasaki Skill Refiner

## Mục tiêu

Kiểm chứng ngược từng claim trong wiki so với raw source, phát hiện gap coverage, lỗi suy diễn, và đề xuất patch có kiểm soát.

**3 tầng tuần tự — `L_structural` → `L_inference` → `L_root_cause`.** L_root_cause có **short-circuit**: skip khi không có pattern lặp.

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

Trước khi chạy, đảm bảo các artifact tồn tại (được sinh trong Bước 3 của Workflow 2.1):

| File | Sinh bởi | Refiner dùng ở |
|:-----|:---------|:---------------|
| `raw_sources/.../{tên_file}_index.json` | `index_skeleton.py` | Tất cả tầng |
| `wiki/[project]/evidence_index.json` | `evidence_index.py` | L_structural, L_inference scope |
| `wiki/[project]/refiner/source_refs_report.json` | `verify_source_refs.py` | L_structural (format/line accuracy) |
| `wiki/[project]/refiner/coverage_gap_report.json` | `coverage_gap_estimator.py` | L_structural (underreport detect) |

Thiếu file nào → yêu cầu user chạy `py .claude/scripts/check_ingest.py --project <p>` trước. **Không tự gọi script** — chờ user confirm.

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

---

## Pre-scan — Session Delta

Chạy trước L_structural.

1. Đọc `quality_gates.json` — lấy session gần nhất.
2. Với từng spec trong batch hiện tại, so:
   - `source_version` trong frontmatter
   - `last_verified_version` trong index JSON
3. Phân loại:
   - **Cần verify đầy đủ:** spec mới, `source_version` thay đổi, session trước FAIL/CONDITIONAL.
   - **Skip deep scan:** version khớp + session trước PASS — L_structural chạy nhanh, L_inference bỏ qua.
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

**Bước 3 — So sánh (5 checks cùng pass):**

| Check | Phát hiện | Label |
|:------|:----------|:------|
| **Count & value match** (enum/list) | Đếm values trong raw, so từng value với claim. Khác → | `INFERRED` |
| **Verbatim match** (số ngưỡng, count, length, %, datetime, regex, error code) | Spec ≠ raw verbatim → `INFERRED`; raw bất thường → | `UNCLEAR` |
| **Formula full statement** | Chỉ thấy thành phần riêng lẻ, raw không nêu công thức → | `LOGIC_INFERRED` |
| **Behavior full statement** (auto-transition, trigger, validation, side effect) | Tự ghép A + B, raw không nêu hành vi → | `LOGIC_INFERRED` |
| **Modifier check** (condition / negation / actor) | Raw có Khi/Nếu/Chỉ khi/Trừ khi mà spec drop → `STRIPPED_CONDITION`. Raw phủ định mà spec đảo → | `NEGATION_FLIP` |
| **Source line content match** | Pre-verdict `PHANTOM_EVIDENCE` từ report → label trực tiếp. Verdict `OK_*` → spot-check 20% content match | `PHANTOM_EVIDENCE` (nếu fail) |
| **Error message text** (VN/EN) | Khác text exact → | `INFERRED` |

### Labels

| Label | Định nghĩa | Action |
|:------|:-----------|:-------|
| `SUPPORTED` | Có bằng chứng explicit | Keep |
| `UNCLEAR` | Raw mơ hồ hoặc section boundary không rõ | Move to `## ❓ Câu hỏi chưa rõ` |
| `INFERRED` | Không có bằng chứng hoặc enum thiếu values | Remove khỏi mô tả chính |
| `LOGIC_INFERRED` | Bằng chứng có thật nhưng kết luận không được raw nêu | Remove khỏi mô tả chính |
| `STRIPPED_CONDITION` | Claim đúng content nhưng condition/actor bị drop | Add modifier back |
| `NEGATION_FLIP` | Spec đảo ngược logic của raw | Reverse claim |
| `PHANTOM_EVIDENCE` | `#line` đúng format nhưng nội dung tại dòng đó không support claim | Fix reference hoặc reclassify |
| `POTENTIAL_OMISSION` | Raw có statements như requirement nhưng không có R-ID tương ứng | Review và thêm vào spec |
| `MISSING_DETAIL` | Claim đúng nhưng thiếu note/side effect quan trọng | Add detail |

> **Khi gặp nghi ngờ — hỏi 3 câu:**
> 1. *"Raw có câu nào nói chính xác điều này không, hay tôi đang ghép A + B?"* (→ LOGIC_INFERRED)
> 2. *"Raw có từ khoá Khi/Nếu/Chỉ khi/Trừ khi, phủ định không/chưa/KHÔNG, hay chỉ định actor mà spec đã bỏ mất không?"* (→ STRIPPED_CONDITION / NEGATION_FLIP)
> 3. *"Nội dung tại dòng này có nói về đúng claim này không?"* (→ PHANTOM_EVIDENCE)

### Output L_inference

Cập nhật `evidence_matrix.md`:

| Raw Evidence (path#line) | Wiki Claim (path#line) | Status | Action |
|:-------------------------|:-----------------------|:-------|:-------|

---

## L_fix — Fix Suggestions (auto-template)

**Skip khi:** `L_structural.violations + L_inference.violations = 0`. Ghi `## L_fix: none required`.

### Quy trình

1. Tổng hợp tất cả violations từ L_structural + L_inference.
2. Với mỗi violation, generate suggestion theo template:

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
- Không tự gọi `check_ingest.py` — yêu cầu user chạy trước khi refiner start.
- Testcase chỉ sinh từ R/AC explicit đã được Gate 1 duyệt.
- Nội dung dựa trên Open question phải nằm ở `Blocked Coverage`.
