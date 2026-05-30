---
tags: [qa/log]
project: project_hasaki
status: Done
created: 2026-05-30
updated: 2026-05-30
---

# Activity Log — project_hasaki

> Timezone: UTC+07:00 (Asia/Ho_Chi_Minh). Format: `YYYY-MM-DD HH:mm:ss`.

## 2026-05-30

### [ingest] 2026-05-30 14:36:55 — Bootstrap ingest 2 raw docs

**Scope:** Fresh ingest 2 raw markdown sau khi project reset hoàn toàn (features/, KANBAN, log đều rỗng).

**Sources:**
- `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.md` (v2.17, 2667 lines, 62 sections)
- `raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.md` (v1.5, 1323 lines, 36 sections)

**Hành động:**
1. Tạo index skeleton bằng `index_skeleton.py` cho cả 2 doc → 98 sections tổng.
2. Sinh `wiki/project_hasaki/refiner/ingest_plan.json` (68 groups).
3. Gen 2 monster stub Feature Spec bằng `generate_stub_features_from_index.py`:
   - `wiki/project_hasaki/features/stub_07062_receiving_po_docs_ver2_17.md` (R001–R062, `partial_read: true`)
   - `wiki/project_hasaki/features/stub_07105_quality_control_docs_ver1_5.md` (R001–R036, `partial_read: true`)
4. Cập nhật mọi section trong 2 index: `mapped_feature` + `coverage_status: stub` + `read_log` (bootstrap session).
5. Tạo `wiki/project_hasaki/feature_groups/reset_bootstrap.md` để gom 2 stub.
6. Tạo placeholder test suite `test_stub_07062_*` + `test_stub_07105_*` (chờ Gate 1B per feature).
7. Fix source ref canonical: `07062_Receiving_PO_Docs_ver2.17.md#L...` → `07062#L...` (cả 2 stub).
8. Sửa header `## 📓 Changelog` → `## 📅 Changelog` để pass governance guardrail.
9. Thêm `## 🔁 Regression Impact` vào 2 test suite stub.

**Quality pipeline (`check_ingest.py`):** exit 0.
- `wiki_sync verify`: PASS (broken links 0, frontmatter 100%, guardrail 0 errors).
- `evidence_index`: 98 requirements + 2 business_rule + 2 questions.
- `verify_source_refs`: 98/98 OK_CANONICAL.
- `coverage_gap_estimator`: no critical.

**Refiner:** skip — stubs chưa có claim từ raw để verify. Refiner sẽ chạy per-stub khi refine stub→full spec (Gate 1B).

**Gate:** chưa trình Gate 1A — stubs cần refine thành per-feature spec trước.

### [rules] 2026-05-30 14:40:00 — Bổ sung rule encoding & ngôn ngữ

Tạo `.claude/rules/05-language-and-encoding.md` quy định:
- Nội dung gen phải Tiếng Việt có dấu.
- UTF-8 không BOM cho mọi `.md`/`.json`/`.yaml`.
- Cấm chain `Get-Content -Raw` + `Set-Content` trên PowerShell 5.1 (đã gây mojibake cho 2 stub trong session này, đã regenerate fix).

Cập nhật `00-core.md` reference rule mới.

### [refine] 2026-05-30 17:30 — Refine batch 2 (6 stub vừa)

**Scope:** Refine 6 stub kích thước vừa (50-250 lines) từ `partial_read: true` → `partial_read: false`.

**Refined:**
| Stub | Sections | R | AC | BR | Msg | Q Open |
|:-----|:---------|--:|---:|---:|--:|------:|
| `stub_receiving_po_inbound_shipment` | S-05, S-06 | 20 | 11 | 10 | 4 desc verbatim | 7 |
| `stub_qc_criteria_sku` | S-07, S-08 | 36 | 14 | 16 | 6 (4 verbatim) | 10 |
| `stub_qc_vas` | S-17, S-18 | 18 | 12 | 10 | 3 (1 EN-only) | 8 |
| `stub_qc_evaluation_mobile` | S-19, S-20 | 33 | 20 | 12 | 1 placeholder | 11 |
| `stub_receiving_po_asn` | S-07, S-08, S-09 (07062) | 26 | 18 | 13 | 1 (EN-only) | 10 |
| `stub_receiving_po_invoice` | S-28, S-29, S-30 | 28 | 22 | 13 | 8 (4 verbatim) | 12 |

**Total batch 2:** 161 R-ID, 97 AC, 74 BR, 23 messages, 58 questions Open.

**Cumulative (batch 1 + 2):** 208 R, 132 AC, 106 BR, 87 questions Open. 11/24 stubs đã `partial_read: false`.

**Index updates:** S-05/S-06 (07062), S-07/S-08/S-09 (07062), S-28/S-29/S-30 (07062), S-07/S-08 (07105), S-17/S-18 (07105), S-19/S-20 (07105) chuyển `coverage_status: full` + `read_log.claims_extracted`.

**Phantom fix:** 17 PHANTOM_EVIDENCE đã được auto-shift `+1` line cho các Source cell trỏ vào "heading-like" lines (table rows mash step+title+desc). Affected: `stub_qc_evaluation_mobile` (8 refs), `stub_receiving_po_invoice` (9 refs). Mọi cell vẫn nằm trong range section logical, chỉ skip heading line đầu.

**Quality pipeline (`check_ingest.py`):** exit 0.
- `wiki_sync verify`: PASS.
- `evidence_index`: 287 requirement + 119 business_rule + 133 ac + 100 question.
- `verify_source_refs`: 287/287 OK_CANONICAL.
- `coverage_gap_estimator`: no critical.

**Gate 1B:** chưa trình; 58 questions Open block một phần test coverage. Mỗi spec ghi rõ Blocked Coverage theo Q-ID.

**Còn lại:** 13/24 stubs vẫn `partial_read: true`. Thứ tự refine tiếp theo theo memory.

### [refine] 2026-05-30 15:55 — Refine batch 1 (5 stub nhỏ nhất)

**Scope:** Promote 5 per-feature stub từ `partial_read: true` → `partial_read: false` bằng cách đọc raw + enumerate candidates + viết R/AC/BR/Error/Question đầy đủ.

**Refined:**
| Stub | Sections | R | AC | BR | Error/Msg | Q Open |
|:-----|:---------|--:|---:|---:|:----------|------:|
| `stub_receiving_po_po_sample` | S-60 | 12 | 7 | 7 | 2 verbatim | 6 |
| `stub_receiving_po_concurrent` | S-61 | 11 | 8 | 7 | 3 (no verbatim) | 6 |
| `stub_qc_criteria_approval` | S-13 | 7 | 5 | 6 | 5 EN-only confirm dialogs | 6 |
| `stub_receiving_po_gift` | S-34, S-35 | 6 | 7 | 6 | 1 verbatim VN+EN | 5 |
| `stub_receiving_po_no_barcode` | S-36, S-37 | 11 | 9 | 6 | 2 (1 verbatim VN) | 6 |

**Total:** 47 R-ID, 36 AC, 32 BR, 13 error/message rows, 29 questions Open.

**Index updates:** S-13, S-34, S-35, S-36, S-37, S-60, S-61 chuyển `coverage_status: stub` → `full` + `read_log.claims_extracted` set theo R-count.

**Quality pipeline (`check_ingest.py`):** exit 0.
- `wiki_sync verify`: PASS.
- `evidence_index`: 138 requirement + 51 business_rule + 36 ac + 48 question.
- `verify_source_refs`: 138/138 OK_CANONICAL.
- `coverage_gap_estimator`: no critical.

**Gate 1B:** chưa trình; tất cả 5 spec có câu hỏi Open block một phần test coverage. Cần clarification từ PO/BA/Dev cho 29 câu hỏi trước Gate 1B (hoặc Gate 1B partial cho phần không bị block).

**Còn lại:** 19/24 stubs vẫn `partial_read: true`. Thứ tự refine tiếp theo theo memory `project_stub_refinement_progress.md`.

### [ingest-split] 2026-05-30 15:00 — Tách monster stub → 24 per-feature stub

**Trigger:** User yêu cầu tiếp tục sau bootstrap. Bước 2 Workflow 2.1 — tách 2 monster stub thành per-feature stub theo TOC.

**Mapping:**
- 07062 (62 sections) → 15 per-feature stub trong group [[receiving_po]]: overview, inbound_shipment, asn, vas, app, date_rules, invoice, fabric, gift, no_barcode, confirm_paste_id, vas_manual, packing_list, po_sample, concurrent.
- 07105 (36 sections) → 9 per-feature stub trong group [[quality_control]]: overview, criteria_setup, criteria_sku, criteria_approval, evaluation_result, vas, evaluation_mobile, evaluation_manual, uid_group.

**Output:**
- 24 file `wiki/project_hasaki/features/stub_*.md` (`partial_read: true`).
- 24 file `wiki/project_hasaki/test_suites/test_stub_*.md` (placeholder, chờ Gate 1B).
- 2 file `wiki/project_hasaki/feature_groups/{receiving_po,quality_control}.md`.
- Cập nhật `mapped_feature` cho mọi section trong 2 index JSON.

**Deprecated:** xoá monster stub `stub_07062_*` + `stub_07105_*`, placeholder test suite cũ, `feature_groups/reset_bootstrap.md`.

**Quality pipeline:** `check_ingest.py` exit 0 — 98 R + 24 BR + 24 Q, source refs 98/98 canonical, no critical.

**Next:** Refine từng stub đọc raw → R/AC/BR/API explicit → `partial_read: false` → Gate 1B per spec.

### [issue] 2026-05-30 13:50 — Mojibake do PowerShell

`Get-Content -Raw` đọc file UTF-8 bằng codepage CP1252 → mã hoá sai Tiếng Việt thành mojibake (`Tổng` → `Tá»•ng`). `Set-Content -Encoding utf8` còn thêm BOM (`EF BB BF`). Fix: regenerate bằng Python `encoding="utf-8"`, không qua PowerShell chain. Đã ghi vào memory `powershell-utf8-encoding` (ngoài vault).
