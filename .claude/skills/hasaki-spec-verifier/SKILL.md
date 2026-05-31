---
name: hasaki-spec-verifier
description: QA verifier kiểm chứng ngược claim wiki → raw evidence. Chạy sau ingest fresh / ingest version mới / task change update spec / refine stub→full. 3 tầng L_structural → L_inference → L_root_cause. Output `wiki/<project>/refiner/`.
metadata:
  author: Yen Ngo
  version: "3.3"
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

## Delegation Routing (orchestrator pattern)

Skill này là **orchestrator** chạy trong main session. **Main session phải delegate** từng tầng sang worker sub-agent đúng model — KHÔNG tự chạy cả 3 tầng bằng main session model (lãng phí Opus cho L_structural).

| Tầng / Phase | Worker sub-agent | Model | Lý do model |
|:-------------|:-----------------|:-----:|:------------|
| Pre-scan delta + Pre-requisite refresh (`check_ingest.py` nếu thiếu) | `@hasaki-verify-structural` | haiku | Script-driven, lookup `quality_gates.json` |
| **L_structural** — Format & Coverage check từ 4 reports pre-computed | `@hasaki-verify-structural` | haiku | Lookup verdict table, không reasoning sâu |
| **L_inference** — Verify claim→raw, decision tree Q1-Q4, 9 labels | `@hasaki-verify-inference` | opus | Phase AI work chính, anti-confirmation-bias, đọc raw cẩn thận |
| **L_fix** (substep, chung pass với L_inference) | `@hasaki-verify-inference` | opus | Same context với L_inference |
| **L_root_cause** (khi không short-circuit) | `@hasaki-verify-inference` | opus | Meta-reasoning về pattern lặp |
| Write-back cuối session (`refiner_writeback.py`, `index_flag_updater.py --apply`, `check_ingest.py`) | `@hasaki-verify-structural` | haiku | Chạy scripts, không reasoning |

**Workflow chuẩn 1 session refiner (cost-optimized):**

```
1. @hasaki-verify-structural   → Pre-scan + L_structural   (haiku)
2. @hasaki-verify-inference    → L_inference + L_fix       (opus)  ← AI work chính
   [user review verdict, confirm PASS/CONDITIONAL/FAIL]
3. @hasaki-verify-structural   → Write-back 3 scripts       (haiku)
```

**Quy tắc delegation:**

1. **Main session không tự chạy L_inference** khi đã có `@hasaki-verify-inference` worker. Đây là điểm tiết kiệm cost lớn nhất — L_inference đòi Opus, nhưng nếu chạy ở main session cũng tốn Opus → có vẻ giống nhau, nhưng worker có context riêng, không pollute main session với evidence_matrix khổng lồ.
2. **Main session không tự chạy L_structural / write-back bằng Opus.** Đây là chỗ tiết kiệm rõ nhất — `@hasaki-verify-structural` chạy haiku ~5% cost.
3. **State-changing scripts** (`refiner_writeback.py`, `index_flag_updater.py --apply`) — worker chỉ chạy khi user explicit confirm verdict.
4. **Workers không spawn worker khác** — sau khi `@hasaki-verify-structural` xong L_structural, nó **suggest** main session gọi `@hasaki-verify-inference`, không tự gọi.

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

## Tầng L_inference + L_fix + L_root_cause

> **Chi tiết đầy đủ ở [`references/l_inference.md`](references/l_inference.md)** — decision tree Q1–Q4, 9 label + severity, tie-breaker, UNCLEAR rule, L_fix skeleton, L_root_cause short-circuit. **`@hasaki-verify-inference` (opus) BẮT BUỘC Read file đó trước khi label claim.** Tách ra để `@hasaki-verify-structural` (haiku) không gánh ~150 dòng decision tree mỗi spawn.

- **L_inference:** verify từng claim có evidence explicit trong raw (tầng AI work chính). Output → `evidence_matrix.md`.
- **L_fix:** substep chung pass với L_inference — tổng hợp violations → `FIX-NNN` suggestions, không tự apply.
- **L_root_cause:** short-circuit (skip khi không có pattern lặp ≥2); khi chạy load `references/l5_root_cause.md`.

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

> No-inference / testcase / blocked-coverage / encoding: theo [`.claude/rules/*.md`](../../rules/). Dưới đây chỉ là guardrail **riêng của verifier**:

- **Không tự apply fix** vào feature/task/test files — chỉ emit `FIX-NNN`, chờ user confirm.
- **Không tự apply patch** skill/rule/template khi chưa pass quality gates (L_root_cause).
- **Auto vs ask scripts:** read-only (`check_ingest.py`, `refiner_findings_diag.py`, `spec_status_dashboard.py`, `index_flag_updater.py` dry-run) → AI tự chạy. State-changing (`refiner_writeback.py`, `index_flag_updater.py --apply`) → chỉ chạy khi user confirm verdict + scope. (Chi tiết ở mục Tooling.)
