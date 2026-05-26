---
name: hasaki-skill-refiner
description: Vòng lặp QA kiểm chứng ngược cho wiki Hasaki — chạy 5 tầng tuần tự sau mỗi batch ingest hoặc update. Tầng 1 kiểm format, Tầng 2 kiểm coverage gap qua index JSON, Tầng 3 kiểm inference/hallucination, Tầng 4 sinh fix suggestions, Tầng 5 phân tích root cause skills. Luôn chạy đủ 5 tầng theo thứ tự. Trigger sau mỗi /wiki-requirement-analyzer hoặc /wiki-test-designer batch.
---

# Hasaki Skill Refiner

## Mục tiêu

Kiểm chứng ngược từng claim trong wiki so với raw source, phát hiện gap coverage, lỗi suy diễn, và đề xuất patch có kiểm soát.

**Luôn chạy đủ 5 tầng theo thứ tự — không bỏ qua tầng nào.**

---

## Pre-requisite: Raw Source Index

Trước khi chạy, kiểm tra index JSON đã tồn tại chưa:

```
raw_sources/project_hasaki/requirements/{tên_file}_index.json
```

Nếu chưa có: yêu cầu user chạy lại `/wiki-requirement-analyzer` (bước index được tạo trong phase ingest). Không tự tạo index — index phải được tạo trong quá trình ingest khi AI đọc raw source.

**Schema index:**
```json
{
  "source_file": "07062_converted.md",
  "source_version": "ver2.17",
  "indexed_at": "2026-05-26T09:00:00+07:00",
  "total_lines": 1500,
  "sections": [
    {
      "id": "S-01",
      "title": "Inbound Shipment (Web)",
      "start_line": 222,
      "end_line": 343,
      "depth": 1,
      "parent_id": null,
      "topic_types": ["ui_filter", "ui_listing", "business_rule", "formula"],
      "flags": {
        "has_enum": true,
        "has_state_transition": false,
        "has_formula": true,
        "has_error_messages": false,
        "has_validation_rule": true
      },
      "mapped_feature": "receiving_po_inbound_shipment.md",
      "coverage_status": "full"
    }
  ]
}
```

`topic_types` hợp lệ: `ui_filter` · `ui_listing` · `business_rule` · `state_transition` · `validation_rule` · `error_messages` · `formula` · `enum_values` · `api_contract` · `actor_flow`

`coverage_status`: `full` · `partial` · `stub` · `unmapped`

---

## Output mỗi session

```
wiki/project_hasaki/refiner/
├── YYYY-MM-DD_{batch_name}/
│   ├── refiner_report.md       ← L1 + L2 + L4 (format violations, gaps, fix suggestions)
│   └── evidence_matrix.md      ← L3 detail
├── quality_gates.json          ← append-only, tất cả sessions
├── improvement_patch_plan.md   ← L5, cập nhật khi có pattern mới
└── retrospective.md            ← L5, bài học tái sử dụng
```

---

## Pre-scan — Session Delta

Chạy trước L1. Mục đích: xác định đúng phạm vi cần verify, tránh re-scan không cần thiết.

1. **Đọc `quality_gates.json`** — lấy session gần nhất, ghi nhận batch và verdict của từng spec.
2. **Với từng feature spec trong batch hiện tại**, so sánh hai trường:
   - `source_version` trong frontmatter của spec
   - `last_verified_version` trong index JSON của raw source tương ứng
3. **Phân loại:**
   - **Cần verify đầy đủ:** spec mới tạo, `source_version` thay đổi, hoặc session trước verdict FAIL/CONDITIONAL trên spec đó.
   - **Skip deep scan:** `source_version` khớp `last_verified_version` **và** session trước PASS cho spec đó — L1 vẫn chạy nhanh, L2-L3 bỏ qua.
4. **Ghi scope ở đầu `refiner_report.md`** trước khi bắt đầu:

```
## Scope session này
- Verify đầy đủ: [danh sách files]
- Skip deep scan (unchanged + đã pass): [danh sách files]
```

L1–L4 chỉ chạy đầy đủ trên nhóm "Cần verify đầy đủ".

---

## Tầng 1 — Format & Structure

**Mục tiêu:** Phát hiện vi phạm cấu trúc trước khi verify nội dung.

### Kiểm tra Feature Spec (`features/`)

1. **Frontmatter bắt buộc:** `tags` · `status` · `feature` · `project` · `source_version` · `partial_read`
2. **14 mục bắt buộc** (từ `tpl_requirement.md`):
   - YAML Frontmatter · Tổng quan · Nguồn tài liệu · API/Interface · Phân rã Requirement
   - User Flows · Business Rules & Data Constraints · Error Messages Map · Acceptance Criteria (BDD)
   - `## ❓ Câu hỏi chưa rõ` · Thay đổi vs version cũ · Impact Analysis · Test Coverage · `## 📅 Changelog`
3. **Source column trong bảng Requirement:** phải có format `[doc_name]#[line]` — không có → `FORMAT_VIOLATION`
4. **Tag đúng:** `#qa/requirement` cho `features/`; `#qa/feature-group/[slug]` nếu thuộc group
5. **Traceability chain tối thiểu:** `Raw Source → Feature Spec` (link `Nguồn tài liệu` phải trỏ đúng file)

### Kiểm tra Task Spec (`task_specs/`)

1. **Frontmatter:** `tags` · `tbb2_code` · `hsk_parent` · `feature_group` · `status`
2. Link 2 chiều: Task Spec → Feature Spec → Feature Group
3. `TBB2 → HSK → Task Spec → Feature → R/AC` machine-readable

### Output L1

Ghi vào `refiner_report.md`, mục `## L1 — Format Violations`:

| File | Mục thiếu/sai | Loại vi phạm | Action |
|:-----|:-------------|:-------------|:-------|

---

## Tầng 2 — Coverage Gap

**Mục tiêu:** Phát hiện vùng raw chưa được cover trong wiki, dựa vào index.

### Quy trình

1. **Load index JSON** của từng raw source liên quan đến batch.
2. **Tìm sections chưa cover:**
   - `coverage_status: "unmapped"` → section không có feature nào map
   - `coverage_status: "stub"` → có feature nhưng chưa đọc thực
   - `coverage_status: "partial"` → đọc một phần, ghi nhận phần còn thiếu
3. **Check flags cho sections đã map:**
   - `has_enum: true` → Feature Spec phải có bảng enum đầy đủ với `#line` ref
   - `has_state_transition: true` → phải có bảng/flow state transition
   - `has_formula: true` → phải có công thức với source line
   - `has_error_messages: true` → phải có bảng Error Messages Map
   - `has_validation_rule: true` → phải có Business Rules & Data Constraints

3b. **Within-section spot check cho sections "full":** Với sections có `coverage_status: "full"` và flag quan trọng (`has_validation_rule: true`, `has_enum: true`, hoặc `has_business_rule: true`):
   - Đọc raw từ `start_line` đến `end_line`
   - Ước lượng số "requirement-looking statements": câu chứa action verb (hiển thị, validate, cập nhật, gửi, block, cho phép, từ chối, tính toán), modal keyword (phải, không được, bắt buộc, cấm, yêu cầu), hoặc conditional structure (Khi .../Nếu ...)
   - So sánh count estimate với số R-IDs trong spec tương ứng
   - Nếu estimate > R-count × 1.5 → flag `POTENTIAL_OMISSION` kèm danh sách các câu trông như requirement chưa được capture

4. **Đọc nội dung sections chưa mapped** (từ `start_line` đến `end_line` trong raw): tóm tắt ngắn nội dung quan trọng có thể cần capture.

### Output L2

Ghi vào `refiner_report.md`, mục `## L2 — Coverage Gaps`:

| Section ID | Title | Lines | coverage_status | Missing flags | Nội dung quan trọng chưa capture |
|:-----------|:------|:------|:----------------|:--------------|:---------------------------------|

---

## Tầng 3 — Inference & Rules Integrity

**Mục tiêu:** Verify từng claim trong wiki có bằng chứng explicit trong raw. Phát hiện INFERRED, LOGIC_INFERRED, MISSING_DETAIL.

### Phạm vi verify

**Spec đầy đủ (`partial_read: false`):** Verify tất cả R, AC, Business Rules, Error Messages.

**Stub (`partial_read: true`):** Chỉ verify phần đã đọc. Ghi `[STUB — section chưa đọc]` trong evidence_matrix.

**Sampling cho doc lớn (raw > 50 trang):** Ưu tiên:
1. Toàn bộ enum/list values (`has_enum: true` sections)
2. Toàn bộ Business Rules và Validation Rules
3. Toàn bộ Error Messages
4. Toàn bộ Formula/State Transition
5. Cứ 5 R còn lại, lấy 1 (R1, R6, R11, ...)

### Quy trình verify — Raw-first (chống confirmation bias)

Thứ tự quan trọng: **đọc raw trước, liệt kê những gì raw nói, rồi mới so sánh với spec.** Không làm ngược lại — đọc spec trước sẽ khiến não "tô màu" việc đọc raw theo hướng xác nhận claim, bỏ qua discrepancy nhỏ.

**Bước 1 — Đọc Feature Spec:** Liệt kê tất cả claims cần verify theo thứ tự ưu tiên sampling. Chỉ ghi nhận danh sách — chưa phân tích.

**Bước 2 — Đọc raw, ghi lại những gì raw nói:** Với mỗi claim, tra `mapped_feature` trong index → đọc đúng vùng raw (`start_line` → `end_line`). Viết ra *những gì raw thực sự nói* bằng lời của raw, không dùng ngôn ngữ của spec. Đây là bước quan trọng nhất — giữ đầu trống, đọc như lần đầu.

**Bước 3 — So sánh raw findings với spec claim:**
- **Enum/list:** đếm values trong raw findings, so sánh count và từng value với claim. Count hoặc value khác → `INFERRED`.
- **Giá trị chính xác (số, ngưỡng, pattern, format):** Với mọi giá trị machine-comparable — số ngưỡng (`> N`, `≥ N`, `= N`), count, length, percentage, datetime format, regex, error code — spec phải khớp verbatim với raw findings. Hai giá trị trông "gần giống" về mặt logic vẫn là hai test boundary khác nhau. Spec ≠ raw → `INFERRED`. Raw findings trông bất thường so với standard của loại dữ liệu → `UNCLEAR`.
- **Formula:** raw findings có nêu đúng công thức không? Nếu chỉ thấy các thành phần riêng lẻ → `LOGIC_INFERRED`.
- **Behavior claim** (auto-transition, trigger, validation, side effect): raw findings có câu nào nêu đúng hành vi đó không — không phải chỉ các thành phần riêng lẻ. Tự ghép A + B → `LOGIC_INFERRED`.
- **Error message:** so sánh text exact với raw findings (VN/EN). Bất kỳ khác biệt → `INFERRED`.
- **Modifier check — condition / negation / actor:** Với mỗi claim đã confirm có evidence, đọc lại raw finding và kiểm tra: raw có bao quanh statement đó bằng điều kiện (Khi/Nếu/Chỉ khi/Trừ khi), phủ định (không/chưa/KHÔNG), hoặc chỉ định actor (hệ thống/user/admin/warehouse) không? Spec bỏ mất condition hoặc actor → `STRIPPED_CONDITION`. Spec đảo ngược phủ định → `NEGATION_FLIP`. Lỗi này nguy hiểm vì claim trông có evidence hợp lệ — chỉ phát hiện được khi chủ động so modifier.
- **Source line spot-check (cứ 5 lấy 1):** Chọn ngẫu nhiên 20% source references → đọc actual line trong raw → kiểm tra nội dung tại dòng đó có thực sự support claim không. Line là heading, câu không liên quan, hoặc thuộc section khác → `PHANTOM_EVIDENCE`. Ghi rõ: dòng thực sự nói gì, và claim spec tuyên bố gì.

### Labels

| Label | Định nghĩa | Action |
|:------|:-----------|:-------|
| `SUPPORTED` | Có bằng chứng explicit, `#line` chính xác và nội dung tại dòng đó support claim | Keep |
| `UNCLEAR` | Raw mơ hồ hoặc section boundary không rõ | Move to `## ❓ Câu hỏi chưa rõ` |
| `INFERRED` | Không có bằng chứng hoặc enum thiếu values | Remove khỏi mô tả chính |
| `LOGIC_INFERRED` | Bằng chứng có thật nhưng kết luận không được raw nêu — AI tự ghép logic | Remove khỏi mô tả chính |
| `STRIPPED_CONDITION` | Claim đúng về content nhưng condition/actor từ raw đã bị drop trong spec | Add modifier back |
| `NEGATION_FLIP` | Spec đảo ngược logic của raw (raw: KHÔNG X → spec: X, hoặc ngược lại) | Reverse the claim |
| `PHANTOM_EVIDENCE` | Cột Source có `#line` nhưng nội dung tại dòng đó không support claim | Fix reference hoặc reclassify |
| `POTENTIAL_OMISSION` | Raw có statements trông như requirement nhưng không có R-ID tương ứng trong spec | Review và thêm vào spec |
| `MISSING_DETAIL` | Claim đúng nhưng thiếu note/side effect quan trọng từ raw | Add detail |

> `LOGIC_INFERRED` xuất hiện nhiều nhất ở: auto-transition trạng thái, validation rule tự rút ra, trigger/side effect, điều kiện enable/disable. Hỏi: *"Raw có câu nào nói chính xác điều này không, hay tôi đang ghép A + B?"*
>
> `STRIPPED_CONDITION` và `NEGATION_FLIP` xuất hiện nhiều ở: conditional display rules, access control, validation boundary. Hỏi: *"Raw có từ khoá Khi/Nếu/Chỉ khi/Trừ khi, phủ định không/chưa/KHÔNG, hay chỉ định actor cụ thể quanh câu này mà spec đã bỏ mất không?"*
>
> `PHANTOM_EVIDENCE` phổ biến khi spec được tạo nhanh: AI ghi #line của section heading thay vì dòng chứa actual rule, hoặc copy dòng từ section lân cận. Hỏi: *"Nội dung tại dòng này có nói về đúng claim này không?"*

### Output L3

Cập nhật `evidence_matrix.md`:

| Raw Evidence (path#line) | Wiki Claim (path#line) | Status | Action |
|:-------------------------|:-----------------------|:-------|:-------|

---

## Tầng 4 — Fix Suggestions

**Mục tiêu:** Biến kết quả L1+L2+L3 thành gợi ý sửa cụ thể, actionable.

### Quy trình

1. Tổng hợp toàn bộ violations từ L1, gaps từ L2, violations từ L3.
2. Với mỗi violation, tạo suggestion theo format:

```
### FIX-NNN: [Mô tả ngắn]
- **File:** wiki/project_hasaki/features/xxx.md
- **Vùng:** dòng hoặc section cụ thể
- **Vấn đề:** [L1/L2/L3] — mô tả vi phạm
- **Gợi ý:** nội dung cụ thể cần thêm/sửa/xóa
- **Ưu tiên:** Critical / High / Medium (Critical = gate bắt buộc fail)
```

3. **Không tự apply** — suggestions chỉ để user review. User confirm → mới sửa file.

### Output L4

Ghi vào `refiner_report.md`, mục `## L4 — Fix Suggestions`.

---

## Tầng 5 — Skill Root Cause Analysis

**Mục tiêu:** Phân tích tại sao lỗi xảy ra — do conflict skill, thiếu thông tin, hay instruction chưa rõ — và đề xuất patch vào skill/rule/template.

### Quy trình

**Bước 0 — Generalization check (làm trước mọi thứ):**
Trước khi phân tích bất kỳ violation nào, đặt câu hỏi này: *"Lỗi này đại diện cho một lớp tình huống, hay chỉ là case đặc thù của batch này?"* Câu trả lời quyết định liệu có nên viết patch hay không, và patch sẽ cover rộng đến đâu.

- **Tránh:** gắn patch vào tên field, feature, hay example cụ thể từ batch hiện tại.
- **Hướng tới:** mô tả *thuộc tính* của loại lỗi đó để patch áp dụng được cho mọi tình huống tương tự.
- **Ví dụ minh họa:** được phép trong patch, nhưng phải là ví dụ điển hình của lớp tình huống — không phải copy nguyên case vừa gặp.
- Nếu không tìm được cách diễn đạt tổng quát → ghi `scope: [hẹp]` để biết cần refactor sau.

---

**Bước 1 — Phân nhóm violations theo nguyên nhân gốc — Decision Tree:**

Với mỗi violation, đi qua các câu hỏi theo thứ tự:

```
Q1: Lỗi xảy ra ở giai đoạn nào?
├── Khi AI đọc raw và VIẾT spec
│   ├── Template không có chỗ ghi → target: templates/
│   └── Instruction ingest thiếu/mơ hồ → target: phase_ingest.md
├── Khi AI VERIFY spec vs raw (trong refiner này)
│   ├── Layer instruction thiếu rule → target: SKILL.md tầng tương ứng
│   └── Index không đủ thông tin để detect → target: ingest step (tạo index)
├── Khi AI chạy qua GATE / workflow
│   └── Gate bị bỏ qua hoặc thứ tự sai → target: commands/ hoặc hasaki-wiki/SKILL.md
└── Hai instructions MÂU THUẪN nhau
    └── → target: cả hai files, resolve conflict

Q2: Trong nhóm đó, instruction hiện tại đang ở trạng thái nào?
├── Chưa có instruction nào về trường hợp này → Add rule
├── Có instruction nhưng không đủ rõ → Clarify / strengthen
└── Có instruction nhưng bị override bởi context khác → Reorder hoặc emphasize
```

---

**Bước 2 — Đề xuất patch** (chỉ khi cùng loại lỗi ≥ 2 violations trong batch, hoặc ≥ 2 sessions liên tiếp):

```
## PATCH-NNN: [Tên ngắn — mô tả lớp lỗi, không phải case cụ thể]
- **File:** đường dẫn file cần sửa
- **Loại:** Add / Update / Remove
- **Nội dung:** mô tả cụ thể
- **Lý do:** root cause (giai đoạn + trạng thái instruction theo decision tree)
- **Expected impact:** gate nào cải thiện
- **Trạng thái:** Pending
```

---

**Bước 3 — Counterfactual test (bắt buộc trước khi finalize patch):**

Với mỗi patch đề xuất, trả lời: *"Nếu patch này đã tồn tại trước khi batch này chạy, violation có xảy ra không?"*

- Trace ngược: violation xảy ra tại bước nào → instruction nào đang thiếu/mơ hồ tại bước đó → patch có nhắm đúng chỗ đó không?
- Nếu câu trả lời là "không rõ" hoặc "có thể vẫn xảy ra" → patch đang sửa triệu chứng, không sửa nguyên nhân. Quay lại Bước 1.
- Ghi kết quả counterfactual vào patch: `**Counterfactual:** [mô tả ngắn cơ chế ngăn chặn]`

---

**Bước 4 — Apply patch** chỉ sau khi user confirm. Đổi `Trạng thái: Pending` → `Trạng thái: ✅ Done`.

**Bước 5 — Ghi retrospective:** bài học có thể tái sử dụng cho session sau.

### Output L5

- `improvement_patch_plan.md` — cập nhật danh sách PATCH
- `retrospective.md` — append bài học mới

---

## Quality Gates & Scoring

Chạy sau khi hoàn thành L1-L3. Gate 🔴 fail → ghi `FAIL`, không dừng — vẫn chạy L4+L5 để sinh fix suggestions.

| Gate | Bắt buộc | Kiểm tra | Điểm |
|:-----|:---------|:---------|:-----|
| `L1_FORMAT_PASS` | 🔴 | Không còn FORMAT_VIOLATION chưa xử lý | 20 |
| `L2_COVERAGE_PASS` | 🔴 | Không còn section `unmapped`; tất cả flags quan trọng được verify | 20 |
| `L3_NO_INFERENCE_PASS` | 🔴 | Không còn `INFERRED` hoặc `LOGIC_INFERRED` trong mô tả chính | 30 |
| `VERIFY_SCRIPT_PASS` | 🔴 | `$env:PYTHONUTF8 = "1"; py .claude/scripts/wiki_sync.py verify` pass | 15 |
| `L4_SUGGESTIONS_COMPLETE` | 🟡 | Mọi Critical violation có FIX suggestion | 10 |
| `L5_ROOT_CAUSE_COMPLETE` | 🟡 | Phân tích nhóm lỗi đã ghi vào retrospective | 5 |
| **Tổng** | | | **100** |

**Penalty:**
- Mỗi `NEGATION_FLIP` còn sót: −8 (đảo ngược nghĩa — nguy hiểm nhất)
- Mỗi `LOGIC_INFERRED` còn sót: −8
- Mỗi `INFERRED` còn sót: −5
- Mỗi `STRIPPED_CONDITION` còn sót: −5
- Mỗi `PHANTOM_EVIDENCE` chưa fix: −3
- Mỗi section `unmapped` không có ghi chú: −3

**Bonus:**
- Mỗi `MISSING_DETAIL` đã bổ sung: +1 (tối đa +5)

Ghi kết quả vào `quality_gates.json` (append — không ghi đè).

---

## quality_gates.json — format session

```json
{
  "sessions": [
    {
      "session": "2026-05-26",
      "batch": "ingest-07062-07105",
      "score_before": 0,
      "score_after": 85,
      "gates": {
        "L1_FORMAT_PASS": true,
        "L2_COVERAGE_PASS": false,
        "L3_NO_INFERENCE_PASS": true,
        "VERIFY_SCRIPT_PASS": true,
        "L4_SUGGESTIONS_COMPLETE": true,
        "L5_ROOT_CAUSE_COMPLETE": true
      },
      "violations": {
        "format": 0,
        "coverage_gaps": 3,
        "inferred": 0,
        "logic_inferred": 0,
        "stripped_condition": 0,
        "negation_flip": 0,
        "phantom_evidence": 0,
        "potential_omission": 0,
        "missing_detail": 2
      },
      "traceability_phase": "Chỉ ingest PDF",
      "verdict": "CONDITIONAL"
    }
  ]
}
```

`verdict`: `PASS` (≥85, tất cả 🔴 pass) · `CONDITIONAL` (≥70, có 🟡 fail) · `FAIL` (<70 hoặc có 🔴 fail)

---

## Done Criteria

Session hoàn thành khi:
- `refiner_report.md` có đủ 4 mục: L1 / L2 / L4 / Summary
- `evidence_matrix.md` có đủ claims theo phạm vi đã xác định
- `quality_gates.json` được append session mới
- Mọi `INFERRED` và `LOGIC_INFERRED` đã được remove/fix hoặc có FIX suggestion tương ứng
- `improvement_patch_plan.md` và `retrospective.md` đã cập nhật (dù không có patch mới, ghi "no new patterns")

---

## Hard Guardrails

- Không suy diễn requirement, AC, API contract, testcase.
- Không tự apply fix vào feature/task files — chỉ suggest, chờ user confirm.
- Không tự apply patch vào skill/rule/template khi chưa pass quality gates.
- Testcase chỉ sinh từ R/AC explicit đã được Gate 1 duyệt.
- Nội dung dựa trên Open question phải nằm ở `Blocked Coverage`.
