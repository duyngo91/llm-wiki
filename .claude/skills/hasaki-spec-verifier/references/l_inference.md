---
tags: [wiki-rules, reference]
status: Done
updated: 2026-05-31
---

# L_inference — Content Verification (chi tiết)

> Tách từ `hasaki-spec-verifier/SKILL.md` (token optimization): chỉ `@hasaki-verify-inference` (opus) cần đọc file này. `@hasaki-verify-structural` (haiku) KHÔNG load.
> Pre-scan / L_structural / scoring / write-back / tooling: ở SKILL.md.

## Tầng L_inference — Content Verification

**Mục tiêu:** Verify từng claim trong spec có bằng chứng explicit trong raw. Đây là tầng AI work chính — đọc raw, so nội dung.

### Phạm vi verify (filter theo flag để giảm IO)

**Spec `partial_read: false`:** verify theo priority:

1. **Bắt buộc verify 100%** (claims mapped đến section có flag critical):
   - `has_enum: true` → toàn bộ enum/list values
   - `has_error_messages: true` → toàn bộ Error Messages
   - `has_business_rule` / `has_validation_rule: true` → toàn bộ Business Rules
   - `has_formula` / `has_state_transition: true` → toàn bộ Formula/State Transition
   - `has_api_contract: true` → toàn bộ API endpoint/payload/contract (đối chiếu từng field request/response với raw); nếu raw có API mà spec ghi "N/A" → `POTENTIAL_OMISSION`
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
