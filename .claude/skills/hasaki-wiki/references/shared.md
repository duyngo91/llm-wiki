---
tags: [wiki-rules, reference, shared]
status: Done
updated: 2026-05-30
---

# Shared Reference — Hasaki Wiki

> Tài liệu dùng chung cho mọi phase. Phase files chỉ link tới các section ở đây, không lặp lại nội dung.

---

## Cấu trúc thư mục chuẩn

```
llm-wiki/
├── index.md · KANBAN.md · log.md
├── raw_sources/[project]/{tasks/, requirements/, issues/, assets/}   ← CHỈ ĐỌC
├── templates/
└── wiki/[project]/
    ├── features/ · api_specs/ · feature_groups/
    ├── test_suites/ · test_plans/ · releases/
    ├── task_specs/
    ├── bugs_knowledge/
    ├── refiner/
    └── operations/{environments.md · test_data.md · team_contacts.md · daily_notes/}
```

Project active: `project_hasaki`.

---

## Naming Conventions

Tên file viết **thường, không dấu**, nối bằng `_`.

| Thư mục | Định dạng | Ví dụ |
|:--------|:----------|:------|
| `features/` | `[feature]_[mucnho].md` | `auth_login.md` |
| `api_specs/` | `api_[feature]_[mucnho].md` | `api_auth_login.md` |
| `feature_groups/` | `[feature_group].md` | `receiving_po.md` |
| `task_specs/` | `task_[tbb2_code].md` | `task_TBB2-12345.md` |
| `test_suites/` | `test_[feature]_[mucnho].md` | `test_auth_login.md` |
| `test_plans/` | `testplan_cr_[project]_[id].md` | `testplan_cr_hasaki_200.md` |
| `releases/` | `cr_[cr_id]_golive_[ddMMyyyy].md` | `cr_hasaki_golive_30052026.md` |
| `raw_sources/.../tasks/` | `HSK-xxxxx.md` | `HSK-12345.md` |

Mỗi `features/` phải có test suite tương ứng. Có API explicit → tạo thêm `api_specs/` và link 2 chiều.

---

## Tags chuẩn

| Tag | Thư mục áp dụng |
|:----|:----------------|
| `#qa/requirement` | `features/` |
| `#qa/api-spec` | `api_specs/` |
| `#qa/test-suite` | `test_suites/` |
| `#qa/test-plan` | `test_plans/` |
| `#qa/release` | `releases/` |
| `#qa/bug/open` | `bugs_knowledge/` (Open/Fixed/Retest) |
| `#qa/bug/fixed` | `bugs_knowledge/` (Closed) |
| `#qa/daily` | `operations/daily_notes/` |
| `#qa/operations` | `operations/` (non-daily) |
| `#qa/feature-group/[slug]` | file thuộc một group (slug dùng `-`, file dùng `_`) |
| `#qa/feature-group-index` | trang group MOC (`feature_groups/`) |

**Double-linking:** Dùng `[[Tên Trang]]` kết nối Feature ↔ Test Suite ↔ Daily Note. Feature có quan hệ phụ thuộc → thêm `Mối quan hệ` trong Tổng quan: `➡️` (output), `⬅️` (input), `ℹ️` (gián tiếp).

---

## HITL Gates

| Gate | Điều kiện tiếp |
|:-----|:---------------|
| **Pre-Gate** — Spec Verify | Chạy `hasaki-spec-verifier` chỉ sau khi sinh/cập nhật claim từ raw: ingest PDF (2.1), ingest version mới (2.1b), task change (2.2), stub→full promotion. Verdict ≠ `FAIL` mới trình Gate 1. **Không áp dụng cho Test Design / daily sync / state transition / CR Go-Live.** |
| **Gate 1A** — Feature Spec Approval cho specs đầy đủ | Spec `partial_read: false`, `Draft` → `Done` · tiến sang Test Design không cần chờ STUB |
| **Gate 1B** — Feature Spec Approval cho STUB | Từng STUB khi hoàn thiện → Gate riêng · không gộp với Gate 1A |
| **Gate 2** — Test Cases Review (QA Lead) | Suite `Draft` → `Testing` · xong mới chạy test |
| **Gate 3** — Bug Triage (QA Lead + Tech Lead) | Bug `Open` hợp lệ · xác nhận RCA + Severity |
| **Gate 4** — Test Execution Approval | Người confirm kết quả thực tế · xong mới sync wiki status |
| **Gate 5** — Go/No-Go (PO + QA Lead ký) | Xong mới close CR |

**Approval Evidence (Gate 1A/1B/2/5):** 3 trường bắt buộc trong frontmatter: `approved_by` · `approved_at: YYYY-MM-DD HH:mm:ss` · `approval_note`.

---

## Status Lifecycle

| Loại file | Status hợp lệ |
|:----------|:--------------|
| Feature Spec | `Draft` → `Done` (Gate 1) |
| API Spec | `Draft` → `Done` (Gate 1) |
| Test Suite | `Draft` → `Testing` (Gate 2) → `Passed` / `Failed` (Gate 4) |
| Test Plan | `Draft` → `Testing` → `Passed` / `Outdated` |
| CR / Release | `Draft` → `Testing` → `Done` (Gate 5) |
| Bug | `Open` → `Fixed` → `Retest` → `Closed` |
| Feature Group | `Draft` → `Done` |
| Test Case (icon) | `⏳` / `✅` / `❌` / `🚫 Blocked` |
| Question | `Open` / `Answered` / `Deferred` |
| Raw task file | `Todo` (status=0) · `Processing` (status=1) · `Done` (status=2) |
| KANBAN column | `## TODO` / `## InProgress` / `## Done` |

**Không được dùng:** `Approved`, `Active`, `Review`, `Final` cho Feature/API Spec.

---

## Knowledge Scope

- **Allowed:** `wiki/`, `raw_sources/`, `templates/`, `.claude/commands/`, `.claude/scripts/`, root docs (`KANBAN.md`, `index.md`, `log.md`, `README.md`, `CLAUDE.md`), `.claude/skills/hasaki-wiki/references/`
- **Excluded by default:** `.obsidian/`, `.smart-env/`, `.karate_cache/`, `.git/`, `__pycache__/`, `*.sqlite`, `*.sqlite-shm`, `*.sqlite-wal`

Excluded scope chỉ dùng khi task explicitly nhắm tool/config troubleshooting.

---

## Core Rules

> **Normative source = [`.claude/rules/*.md`](../../../rules/)** (no-inference, encoding, timezone, SSOT, testcase, secret). Không lặp lại ở đây — đọc trực tiếp `rules/`. Chỉ giữ 2 nhắc vận hành:
> - **Timestamp format:** `YYYY-MM-DD HH:mm:ss` theo `UTC+07:00` (`Asia/Ho_Chi_Minh`).
> - **Windows Python:** set `$env:PYTHONUTF8 = "1"` trước khi chạy mọi script `.py`.

---

## Source Reference Format (SSOT)

Mọi cột `Source` / `Nguồn` trong Feature Spec / API Spec / evidence_index phải dùng **canonical format**:

```
{doc_short_name}#L{start}-L{end}
```

**Quy ước:**
- `doc_short_name`: prefix file raw (vd `07062`, `07105`) — **không** kèm `_converted.md`.
- Line numbers: **one-based**, **ASCII hyphen** (`-`, không phải en-dash `–`).
- Luôn có prefix `L` cho mỗi số.
- Đơn dòng → `end = start`, vẫn ghi đầy đủ: `07062#L234-L234` (hoặc rút gọn `07062#L234`).

**Multi-range trong cùng 1 cell:** ngăn cách bằng `,` + space:
```
07062#L234-L239, 07062#L500-L502
```

| Pattern | Valid? | Note |
|:---|:---:|:---|
| `07062#L234-L239` | ✅ Canonical | Always use this |
| `07062#L234` | ✅ Single line | end suy ra = start |
| `07062#L234-L239, 07062#L500-L502` | ✅ Multi-range | Comma-space separator |
| `07062#234-239` | ⚠️ Tolerated | Parser chấp nhận, nhưng rewrite về canonical |
| `07062#L234–L239` | ❌ Invalid | En-dash, parser fail |
| `theo trang 24` | ❌ Invalid | Không có regex match |
| `07062_converted.md#L234` | ❌ Invalid | Dùng short_name, không kèm extension |
| `raw_sources/.../07062.md#L234` | ❌ Invalid | Không kèm path |

**Regex chuẩn (single source of truth):**

```python
SOURCE_REF_RE = re.compile(r"([A-Za-z0-9_.]+)#L(\d+)(?:-L(\d+))?")
# Multi-range: split cell by r",\s*" trước rồi áp regex
```

**Convention line numbering (từ `index_skeleton.py`):**
- `index.json.sections[].start_line` / `end_line`: **zero-based internal** (dùng cho Python slicing).
- `index.json.sections[].source_ref`: **one-based display** (giống Read tool output).
- `Feature Spec` cột Source: **luôn dùng one-based display**, khớp với `source_ref`.

**Lưu ý phantom evidence:** `start_line` trong index thường là dòng heading. Khi viết Source cho R-ID, AI phải đọc raw range, xác định **dòng đầu tiên chứa rule actual** (không phải heading), rồi ghi `#L{actual_line}`. Verify lại bằng Read trước khi commit.

---

## Field Ownership Matrix

Để tránh wiki và refiner cùng ghi 1 field (race condition / drift), mỗi field có **owner write** duy nhất:

| Field | File chứa | Owner write | Owner read | Lifecycle |
|:------|:----------|:------------|:-----------|:----------|
| `source_ref` | `index.json` | `index_skeleton.py` (auto) | wiki + refiner | Generated; AI chỉ verify trên review |
| `start_line` / `end_line` | `index.json` | `index_skeleton.py` (auto) + `index_diff_patch.py` (offset shift) | wiki + refiner | Script own |
| `coverage_status` | `index.json` | wiki khi tạo/cập nhật Feature Spec | refiner L2 | `unmapped` → `full`/`partial`/`stub` |
| `range_status` | `index.json` | `index_skeleton.py` set `needs_review`; **refiner L3 set `verified`** sau khi spot-check OK | wiki dùng để biết section nào cần đọc kỹ | `needs_review` → `verified` |
| `mapped_feature` | `index.json` | wiki khi tạo Feature Spec | refiner | wiki own |
| `topic_types` / `flags.*` | `index.json` | wiki khi điền semantic sau khi script tạo skeleton | refiner L2 đọc để decide verify scope | wiki own |
| `last_verified_version` | `index.json` | **refiner sau session PASS/CONDITIONAL** | wiki dùng để biết stale | refiner own |
| `change_history` | `index.json` | `index_diff_patch.py` (script) khi raw version mới | refiner L2 đọc để filter delta scope | Script own |
| `read_log` (`claims_extracted`, `last_read_at`, `last_read_session`) | `index.json` per section | wiki khi hoàn thành đọc 1 section trong ingest | refiner check `SUSPECT_UNREAD` khi `coverage_status: full` mà `read_log: null` | wiki own |
| `partial_read` | Feature Spec frontmatter | wiki khi viết spec/stub | refiner trust (cross-check với `coverage_status`) | wiki own |
| `source_version` | Feature Spec frontmatter | wiki khi viết spec | refiner so với `last_verified_version` của index | wiki own |
| `last_verified_at` | Feature Spec frontmatter | **refiner sau verify session** | wiki dùng để biết stale | refiner own |
| `verification_status` | Feature Spec frontmatter | wiki set `Pending` khi tạo; **refiner đổi `Verified`/`Stale` sau verify** | wiki dùng để route Gate 1 | wiki init → refiner update |
| Cột `Source` (bảng Requirement) | Feature Spec body | wiki khi viết R-ID | refiner L1 (format) + L3 (verify nội dung) | wiki own |
| `approved_by` / `approved_at` / `approval_note` | Feature/Test Suite frontmatter | wiki sau Gate 1/2/5 (do user/PO/QA Lead xác nhận) | refiner trust | wiki own |

**Quy tắc:** nếu một thay đổi yêu cầu ghi vào field thuộc skill khác, **không tự ghi** — chỉ emit `FIX-NNN` suggestion (refiner) hoặc câu hỏi cho user (wiki) và chờ confirm.

---

## Phân loại task Hasaki

| Code | Vai trò | Lưu |
|:-----|:--------|:----|
| `HSK-xxxxx` | Task cha chứa requirement/implementation detail | `raw_sources/project_hasaki/tasks/HSK-xxxxx.md` |
| `TBB2-xxxxx` | Test request liên kết HSK cha qua `parent_id` | Embed vào section `## Test Requests (TBB2)` trong file HSK — không tạo file TBB2 riêng |

Wiki impact check và KANBAN card dùng HSK code (không phải TBB2 code).

---

## Scripts available

| Script | Mục đích |
|:-------|:---------|
| `py .claude/scripts/wiki_sync.py verify` | Lint + audit toàn bộ vault (audit-only) |
| `py .claude/scripts/wiki_sync.py sync` | Sync sau Gate 4 |
| `py .claude/scripts/wiki_sync.py repair` | Tự sửa các lỗi format gặp thường |
| `py .claude/scripts/wiki_sync.py daily-sync --project <p> --date <YYYY-MM-DD>` | Sync daily note |
| `py .claude/scripts/wiki_sync.py sync-my-open-tasks [--limit N] [--images] [--dry-run]` | Sync open tasks từ Hasaki Workplace |
| `py .claude/scripts/index_skeleton.py <converted.md> --version <ver>` | Tạo skeleton index JSON từ converted PDF MD |
| `py .claude/scripts/plan_ingest_tasks.py --project <p> [--max-group 6]` | Sinh `wiki/<p>/refiner/ingest_plan.json` từ `*_index.json` — cluster sections theo `parent_id` thành groups, mỗi section = 1 task cho `TaskCreate`. Status derive từ `coverage_status`+`read_log`, idempotent. Dùng ở Bước 1.5 của Workflow 2.1 |
| `py .claude/scripts/evidence_index.py --project <p>` | Build evidence index (R-ID + AC + API + Business Rule → doc#line). Schema v2.0 — hỗ trợ multi-range, `coverage_class` |
| `py .claude/scripts/verify_source_refs.py --project <p>` | Validate cột Source vs raw thật. Flag `INVALID_FORMAT` / `OUT_OF_RANGE` / `STALE` / `PHANTOM_EVIDENCE` / `MISSING_SOURCE` / `RAW_NOT_FOUND`. Exit 2 nếu có critical |
| `py .claude/scripts/coverage_gap_estimator.py --project <p> [--threshold 0.5]` | Per section: count modal/action/conditional/constraint signals, compare evidence count. Flag `UNDERREPORTED_COVERAGE` / `UNMAPPED` / `NO_SIGNALS`. Exit 2 nếu có critical |
| `py .claude/scripts/check_ingest.py --project <p>` | **Wrapper one-shot** chạy 4 script trên (verify + evidence_index + verify_source_refs + coverage_gap_estimator). Exit = max severity. Dùng ở Bước 3 của Workflow 2.1 |
| `py .claude/scripts/change_impact.py --project <p>` | Tính change-impact report |
| `py .claude/scripts/generate_stub_features_from_index.py` | Sinh stub Feature Spec từ index sections |
| `py .claude/scripts/spec_status_dashboard.py --project <p> [--json]` | **Dashboard:** đếm specs theo status (stub / refined_pending / verified / stale) per feature group. Markdown bảng + per-spec listing. Dùng để overview tiến độ refine + verify. |
| `py .claude/scripts/refiner_writeback.py --project <p> --specs s1,s2 --verdict PASS [--approval-note "..."]` | **Spec-verifier:** sau verify, update spec frontmatter (`last_verified_at`, `verification_status`) + raw `*_index.json` sections (`range_status`, `last_verified_version`). Idempotent. Verdict PASS/CONDITIONAL → Verified; FAIL → Stale. |
| `py .claude/scripts/index_flag_updater.py --project <p> [--specs s1,s2] [--apply]` | **Spec-verifier:** scan spec content → auto-detect critical flags (enum / error_messages / business_rule / validation_rule / formula / state_transition) → propagate vào `index.json` sections. Default dry-run. |
| `py .claude/scripts/refiner_findings_diag.py --project <p> [--json]` | **Spec-verifier:** pretty-print non-OK findings từ `source_refs_report.json` (PHANTOM_EVIDENCE / STALE / INVALID_FORMAT) — debug phantom nhanh. |
| `py .claude/scripts/index_diff_patch.py <old.md> <new.md> [--index <index.json>]` | Diff 2 version raw MD → output line-offset patches + apply vào index sections start_line/end_line. Dùng khi ingest version mới (PDF 2.17 → 2.18). |

Windows: luôn set `$env:PYTHONUTF8 = "1"` trước khi chạy.
