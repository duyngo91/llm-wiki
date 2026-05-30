---
tags: [wiki-rules, reference]
status: Done
updated: 2026-05-30
---

# Phase: Requirement Analysis & Ingest

> Dùng bởi: `/wiki-requirement-analyzer` — ingest PDF, import task HSK, xử lý task change.
> Tham chiếu cấu trúc thư mục, naming, tags, status, HITL Gates: [`shared.md`](shared.md).

---

## Unreadable Source Rule

Khi raw source đề cập link/tài nguyên (Figma, URL, PDF phụ) **không thể truy cập**:
1. Ghi vào `## Nguồn tài liệu` với `Status = ❓ Chưa đọc được`.
2. Tạo câu hỏi `Open`: `"Link/file [X] được đề cập nhưng chưa đọc được — cần cung cấp [file/quyền]"`.
3. Không suy diễn nội dung từ link chưa đọc.

## Question Lifecycle

Bảng `## ❓ Câu hỏi chưa rõ`: `Q-ID | R/AC liên quan | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn | Ngày`

Trạng thái: `Open` / `Answered` / `Deferred`.
- R/AC còn `Open` liên quan trực tiếp → chặn sinh test case → ghi vào `Blocked Coverage`.
- Chỉ cập nhật Spec/TC khi câu hỏi `Answered` + có nguồn rõ.
- **Giá trị trông bất thường:** Raw ghi giá trị inconsistent với standard (format string thiếu component, số ngưỡng không hợp lý, enum không theo pattern, code trông như typo) → mark `UNCLEAR`, thêm câu hỏi. Không assume raw là correct.

---

## Workflow 2.0: Khởi tạo dự án mới

**Kích hoạt:** Project chưa tồn tại hoặc user yêu cầu.

1. Tạo cấu trúc thư mục đầy đủ (xem `shared.md#cấu-trúc-thư-mục-chuẩn`).
2. Khởi tạo 3 file operations: `environments.md`, `test_data.md`, `team_contacts.md`.
3. Cập nhật `index.md`, tạo Kanban cards khởi tạo Sprint, ghi log `[create]`.

---

## Workflow 2.1: Ingest PDF (4 bước)

**Kích hoạt:** File PDF mới trong `raw_sources/[project]/requirements/`.

---

### Bước 1 — Prepare Raw (convert + index skeleton)

```
$env:PYTHONUTF8 = "1"
# 1.1 Convert PDF → markdown (MCP)
markitdown/convert_to_markdown  →  *_converted.md cạnh PDF gốc

# 1.2 Tạo index skeleton
py .claude/scripts/index_skeleton.py <path_to_converted.md> --version <ver>
```

Script ghi `{tên_file}_index.json` với `id`, `title`, `start_line`, `end_line`, `read_log: null`. AI hoàn thiện trước khi sang Bước 2 (đây là semantic markup, vẫn ở phase chuẩn bị):
- `topic_types`: chọn từ `[ui_filter, ui_listing, business_rule, state_transition, validation_rule, error_messages, formula, enum_values, api_contract, actor_flow]`
- `flags`: set `true` nếu section có enum / state transition / formula / error messages / validation rule
- `mapped_feature`: để `null` — sẽ điền ở Bước 2
- `coverage_status`: `unmapped` — sẽ điền ở Bước 2

**Index split priority:** Markdown headings → TOC dotted entries → strong body headings (`Update`, date update, `Case`, `Web:`) → page-marker fallback. Không dùng generic bullets, table rows, OCR fragments, uppercase table cells làm headings.

Mỗi section preserve trace fields: `source_type`, `source_page`, `source_ref`, `range_status`. `start_line`/`end_line` là zero-based internal; dùng `source_ref` cho human review và canonical `doc#L{start}-L{end}` evidence (xem `shared.md#source-reference-format-ssot`).

Không sửa raw PDF, không ghi đè file raw đã lưu.

---

### Bước 2 — Read & Extract loop (per section)

ISTQB Test Analysis. **Mỗi section trong index được xử lý theo cùng 1 micro-cycle** — không bay qua. Cycle:

**2.1 — Read section (must-read-to-end):**
- Dùng Read tool với `offset = section.start_line + 1`, `limit = (end_line - start_line) + 10` (10 dòng context buffer cho rule trải dài).
- Section >150 dòng: chia chunks, đọc tuần tự, không skip.
- Section có flag `has_enum / has_state_transition / has_formula / has_error_messages / has_validation_rule` → đọc **toàn bộ** section, không sampling.

**2.2 — Enumerate candidates (output trong cùng response trước khi viết spec):**

Sau khi đọc, AI phải list ra tất cả **candidate claims** (rule, constraint, behavior statement, error message, enum value) trong response trước khi mở Edit/Write spec. Format gợi ý:

```
Section S-NN candidates:
  C1 (L234): "Filter trạng thái có 5 giá trị: Draft/Pending/Approved/Rejected/Cancelled" → R-ID candidate
  C2 (L238): "Khi user click Approve, system phải tạo audit log" → R-ID candidate (conditional)
  C3 (L242): table cell pattern PO-\d{6} → Business Rule
  C4 (L250): "(Note: only Admin role can override)" → STRIPPED_CONDITION risk if missed
  C5 (L260): rule không có modal keyword nhưng implicit "Status converts to Done after 24h" → R-ID candidate
```

Mỗi candidate phải có **decision**: → R-ID / → AC-ID / → BR-ID / → API-ID / → Question / → Skip + reason. Không được "quên" sau enumeration. Đây là bằng chứng AI đã đọc hết section.

**2.3 — Write spec (chỉ từ candidates đã enumerate):**
- Trùng cũ → Diff, cập nhật Spec, ghi Changelog.
- Mới → Tạo `[feature]_[mucnho].md` trong `features/` dùng `tpl_requirement.md`, phân rã R-IDs, vạch flows, status `Draft`.
- **Frontmatter tối thiểu bắt buộc:** `feature`, `project`, `source_version`, `source_doc`, `source_range`, `partial_read`, `last_verified_at`, `verification_status` (`Pending` khi tạo).
- **Stub (`partial_read: true`):** Phải có đủ 14 mục bắt buộc (template). Nội dung có thể placeholder `> Chưa đủ dữ liệu — STUB, cần đọc trang [X–Y]`. **Section headers là bất biến.**
- Source column bảng Requirement và Source line trong AC-NN: canonical `{doc}#L{start}-L{end}` (xem `shared.md#source-reference-format-ssot`). Multi-range: `doc#L1-L5, doc#L20-L25`.
- Có API explicit → tạo `api_specs/api_[feature]_[mucnho].md` dùng `tpl_api_spec.md`.
- AC dùng `AC-NN` (không `Scenario N`) để evidence_index trace được.
- Question chưa rõ → `## ❓ Câu hỏi chưa rõ` + `Blocked Coverage`. Không suy diễn.

**2.4 — Update index sau spec:**
- `mapped_feature: "<feature_file_name>.md"`
- `coverage_status: "full"` (đọc hết + viết hết) / `"partial"` (đọc một phần) / `"stub"` (chưa đọc nội dung)
- `read_log`:
  ```json
  {
    "claims_extracted": <số R/AC/BR/API đã ghi vào spec từ section này>,
    "last_read_at": "<UTC+07 timestamp YYYY-MM-DD HH:mm:ss>",
    "last_read_session": "<batch name, vd ingest-07062-batch-1>"
  }
  ```

Section `coverage_status: "full"` mà `read_log: null` → refiner flag `SUSPECT_UNREAD`. Không skip update.

Lặp Bước 2 cho mọi section trong index trước khi sang Bước 3.

---

### Bước 3 — Quality pipeline (one-shot)

```
py .claude/scripts/check_ingest.py --project project_hasaki
```

Wrapper chạy 4 script tuần tự:
1. `wiki_sync.py verify` — format/governance
2. `evidence_index.py` — index R/AC/BR/API claims
3. `verify_source_refs.py` — line accuracy
4. `coverage_gap_estimator.py` — per-section expected vs actual claims

Exit 0 = sạch · exit 2 = có critical (ít nhất 1 stage báo critical findings).

Critical fail cases:
- `evidence_index.json` có `records = 0` → ingest chưa hoàn tất.
- `source_refs_report.json` có `INVALID_FORMAT` / `OUT_OF_RANGE` / `PHANTOM_EVIDENCE` / `STALE` / `RAW_NOT_FOUND` / `MISSING_SOURCE`.
- `coverage_gap_report.json` có `UNDERREPORTED_COVERAGE` (section `full` mà gap_ratio < 0.5) → quay lại Bước 2 đọc thêm.

Sau khi `check_ingest.py` exit 0, chạy `hasaki-skill-refiner` (mode `Full`). Verdict ≠ `FAIL` → trình Gate 1.

---

### Bước 4 — Gate 1 + Kanban + log

- **Gate 1A:** Trình Feature Spec `partial_read: false` cho PO/QA Lead. Specs đầy đủ tiến sang Test Design — không cần chờ STUB.
- **Gate 1B:** Khi hoàn thiện từng STUB spec → Gate 1 riêng. Không gộp với Gate 1A.
- Thêm card Kanban `## TODO`, ghi log `[ingest]`.

---

## Workflow 2.1b: Ingest version mới (Incremental Update)

**Kích hoạt:** File raw source có version mới hơn `source_version` trong index JSON hiện tại.

**Bước 1 — Phát hiện thay đổi:**
- So sánh `source_version` trong `{tên_file}_index.json` với version trong Revision History của file MD mới.
- Giống nhau → không cần update. Khác → đọc Revision History section (~150 dòng đầu file).

**Bước 2 — Xác định vùng bị ảnh hưởng:**

| Loại thay đổi | Hành động với index |
|:-------------|:--------------------|
| Thêm section mới | Thêm entry, `coverage_status: "unmapped"`, `change_history: [new_version]` |
| Xóa section | Đổi `coverage_status: "deleted"` — giữ lại để audit |
| Sửa nội dung | Đổi `coverage_status: "partial"`, cập nhật `change_history` |
| Thêm content làm lệch line | Tính offset → cộng vào `start_line`/`end_line` các sections phía dưới |

**Bước 3 — Patch index JSON (không rebuild):**
- Cập nhật `source_version` và `indexed_at`.
- `last_full_index_version` = version cũ (giữ lại để biết base).
- Sections không bị ảnh hưởng: giữ nguyên `last_verified_version` và `coverage_status`.
- Sections bị ảnh hưởng: `last_verified_version: null`, thêm version mới vào `change_history`.

**Bước 3b — Migrate Source references trong Feature Spec (bắt buộc khi line offset ≠ 0):**

Khi raw có content được chèn/xoá làm dịch chuyển line, cột `Source` trong bảng Requirement của Feature Spec (`#L{start}-L{end}`) trỏ tới content khác → claim trở thành PHANTOM. Phải migrate trước khi viết content mới:

1. **Build delta map:** với mỗi line N trong raw cũ → line N' tương ứng trong raw mới. Tham chiếu offset đã tính ở Bước 2 (mỗi section dịch theo offset section cha của nó).
2. **Quét Feature Spec** có frontmatter `source_doc` = doc đang update; với mỗi cell Source trong bảng Requirement (xem `shared.md#source-reference-format-ssot` cho canonical regex):
   - Parse mỗi `doc#L{start}-L{end}` (kể cả multi-range)
   - Nếu `start..end` thuộc section có `change_history` chứa version mới → không migrate, mark dòng R-ID đó là `🔄 cần re-verify` trong Changelog spec.
   - Nếu `start..end` thuộc section unchanged nhưng nằm sau insertion point → apply offset, rewrite cell.
   - Nếu `start..end` straddle (cắt qua) boundary section thay đổi → mark `⚠️ ambiguous`, ghi câu hỏi vào `## ❓ Câu hỏi chưa rõ`, không tự rewrite.
3. **Verify spot-check sau migrate:** dùng Read tool đọc 3 cell ngẫu nhiên ở các vị trí migrate khác nhau, đối chiếu nội dung tại line mới với claim. Lệch → revert migrate, mark `🔴 broken ref` để user resolve thủ công.
4. Ghi vào Changelog spec: `migrated source refs do raw v{old} → v{new}, offset map: [section_id → delta]`.

**Bước 4 — Chỉ update Feature Spec bị ảnh hưởng:**
- `coverage_status: "partial"/"unmapped"` → cập nhật Feature Spec tương ứng.
- `coverage_status: "full"` và `last_verified_version` = version cũ → skip content update nhưng vẫn áp dụng Bước 3b nếu offset ≠ 0.
- Ghi Changelog với version source mới.
- **Gate 1:** Chờ PO/QA Lead duyệt lại chỉ phần thay đổi.

**Bước 5 — Refiner pre-gate (delta mode):**
- Trigger `hasaki-skill-refiner` mode `Delta` — chỉ verify sections có `change_history` chứa version mới, plus claims có `🔄 cần re-verify` từ Bước 3b.
- Verdict ≠ FAIL → trình Gate 1.

---

## Workflow 2.2: Task Change

**Kích hoạt:** User cung cấp Task/Jira ticket có thay đổi requirement; hoặc `/get-my-tasks` phát hiện HSK có `updated_at` thay đổi.

**Bước 1 — Impact Analysis:**
- Đọc `index.md` định vị file liên quan. Quét `features/`, `api_specs/`, `test_suites/` xác định vùng bị ảnh hưởng.
- Ghi bảng Impact Analysis trước khi sửa:
  `Change ID | Change type (Add/Update/Remove/Clarify) | Affected R/AC | Affected Features | Affected API Specs | Affected Test Suites | TC action | Regression candidates | Open questions/Gate`

**Bước 2 — Clarification (HITL Gate A):**
- Soạn câu hỏi phân loại (PO: nghiệp vụ; Dev Lead: kỹ thuật).
- **Dừng chờ phản hồi.** Không phỏng đoán nghiệp vụ.

**Bước 3 — Cập nhật (Gate 1 → Gate 2):**
- Nhận câu trả lời → cập nhật Feature Spec + API Spec, đổi status về `Draft`, ghi Changelog kèm mã Task.
- **Gate 1:** User ký duyệt Spec. Sau Gate 1 → gọi `/wiki-test-designer`.
- TC cũ hết hiệu lực → chuyển vào `Deprecated`, không xóa. Cập nhật `Regression Impact`.
- Di chuyển card Kanban → `## InProgress`, ghi log `[task-update]`.

---

## Chuẩn viết Feature Spec (`features/`)

Dùng `tpl_requirement.md`. 14 mục bắt buộc:

1. YAML Frontmatter (xem frontmatter tối thiểu ở Workflow 2.1 Bước 2b)
2. Tổng quan (Feature, Mô tả, Source, Actors, Mối quan hệ nếu có)
3. Nguồn tài liệu (bảng PDF/Link + version + status)
4. API/Interface liên quan (chỉ link → API Spec, không nhúng contract)
5. Phân rã Requirement (bảng R-ID, loại, priority, testable, source với line reference `#line`)
6. User Flows (Pre-conditions, Happy Path, Alt-Flows, Exc-Flows)
7. Business Rules & Data Constraints (bảng validation)
8. Error Messages Map
9. Acceptance Criteria — BDD (Given-When-Then)
10. `## ❓ Câu hỏi chưa rõ` (bảng lifecycle)
11. Thay đổi vs version cũ (bảng Add/Update/Remove/Clarify)
12. Impact Analysis & Regression Proposal
13. Test Coverage (R → TC mapping, gồm blocked)
14. `## 📅 Changelog`

---

## Chuẩn viết API Spec (`api_specs/`)

Dùng `tpl_api_spec.md`. Các mục bắt buộc:
- Frontmatter: `tags: [qa/api-spec]`, `project`, `feature`, `feature_group`
- Tổng quan, API List (`API ID | Method | Endpoint | Mục đích | R/AC | Source | Status`)
- API Detail: auth, headers, params, request body, success/error response, side effects
- `## ❓ Câu hỏi API chưa rõ`, API Test Coverage, `## 📅 Changelog`

**Nguyên tắc:** Feature Spec = WHAT/WHY; API Spec = HOW contract. Nguồn không đề cập API → không tạo API Spec. Không suy diễn endpoint/payload/status code/error message/side effect.

---

## Stub Lifecycle

Khi feature có `partial_read: true` (chưa đọc đủ raw để viết spec đầy đủ), file đó là Feature Spec ở trạng thái bootstrap — **không phải deliverable cuối**.

**Mục đích stub:** tạo early traceability (`R-ID → doc#line-line`), đánh dấu unknowns không suy diễn, giữ section headers theo template.

**Transition path:**
1. Index từ raw (`index_skeleton.py`)
2. Stub feature spec với source references và placeholder content
3. Refine stub thành full feature spec theo domain (rules/flows/errors/AC từ raw, giữ explicit `doc#line-line` evidence, giảm `partial_read` scope, resolve open questions)
4. Run refiner → proceed Gate 1B cho spec đó

Test design ưu tiên `partial_read: false` specs (Gate 1A). Stub còn lại theo Gate 1B per spec.
