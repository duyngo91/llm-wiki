---
status: Done
updated: 2026-05-25
---

# Improvement Patch Plan — Session 2026-05-25

## Bugs đã fix trong session này

| Bug | File | Mô tả | Trạng thái |
|:----|:-----|:------|:-----------|
| R3 thiếu "Hoàn thành/Completed" | `receiving_po_inbound_shipment.md` | Filter WMS status có 5 values, spec ghi 4 | ✅ Fixed |
| R1 thiếu ghi chú "Move qua trang ASN" | `receiving_po_inbound_shipment.md` | Đồng kiểm filter → navigate sang ASN page | ✅ Fixed |

---

## Patch đề xuất cho Skills/Rules

### PATCH-001: Skill `hasaki-wiki` — Bổ sung bước line-reference khi ghi Source

**Root cause:** Khi ghi Source trong cột R của bảng Requirement, không ghi line number cụ thể → khó verify sau này.

**Biểu hiện:** R3 (`receiving_po_inbound_shipment`) ghi "v2.17, mục Inbound Shipment Filter" nhưng không rõ dòng nào → dẫn đến bỏ sót 1 trong 5 giá trị.

**Đề xuất patch** vào `phase_ingest.md` — thêm rule:

```
Source format: `[doc_name]#[line_number_or_range]`
Ví dụ: `07062#234-239` thay vì `v2.17, mục Inbound Shipment Filter`
```

**Expected impact:** Giảm INFERRED claims do missed values. Reviewer có thể verify trực tiếp.

**Priority:** High

---

### PATCH-002: Skill `hasaki-wiki` — Stub spec phải có trạng thái `partial_read: true` trong frontmatter

**Root cause:** Stub files (VAS, App, Packing List, QC Approve, Assessment Result, Mobile) không có flag rõ ràng trong frontmatter — dễ nhầm là spec đầy đủ.

**Đề xuất patch** vào `tpl_requirement.md`:

```yaml
partial_read: false   # set true nếu raw source chưa đọc hết
partial_read_note: "" # ghi phần nào chưa đọc
```

**Expected impact:** Reviewer và công cụ verify có thể tự phân biệt spec đầy đủ vs stub.

**Priority:** Medium

---

### PATCH-003: Rule `20-no-inference.md` — Thêm rule "claim về enumeration phải liệt kê đủ tất cả values"

**Root cause:** Khi một field có list values (enum), việc đọc không hết dẫn đến claim partial list nhưng mark SUPPORTED.

**Đề xuất patch** vào `.claude/rules/20-no-inference.md`:

```
- Khi claim về enumeration (dropdown, status list, giá trị hợp lệ):
  phải liệt kê ĐỦ tất cả values từ source.
  Nếu không chắc đã đủ → đánh dấu UNCLEAR, ghi vào Câu hỏi.
```

**Expected impact:** Ngăn lỗi "missed enum value" như R3 trong session này.

**Priority:** High

---

### PATCH-004: Skill `hasaki-skill-refiner` — Bổ sung check enum completeness vào vòng lặp

**Đề xuất:** Khi chạy refiner, tự động grep tất cả "Giá trị:" trong raw source và đối chiếu với claims trong spec.

**Priority:** Low (cần script hỗ trợ)

---

## Keep/Discard

| Patch | Quyết định | Lý do |
|:------|:-----------|:------|
| PATCH-001 (line reference) | **Keep** | Tăng điểm traceability, không vi phạm gate nào |
| PATCH-002 (partial_read frontmatter) | **Keep** | Cải thiện QUESTION_ROUTING và không vi phạm gate |
| PATCH-003 (enum rule) | **Keep** | Trực tiếp fix root cause của INFERRED violation |
| PATCH-004 (auto enum check) | **Defer** | Cần tooling, không urgent |

---

## Áp dụng Patch

Patches 001-003 sẽ được áp dụng ngay trong session này sau khi retrospective được ghi nhận.
