---
status: Done
updated: 2026-05-25
---

# Retrospective — Ingest Session 2026-05-25

## Session summary

| Item | Giá trị |
|:-----|:--------|
| Raw sources | 07062 v2.17 (Receiving PO), 07105 v1.5 (Quality Control) |
| Feature Specs tạo | 11 (4 đầy đủ, 7 stub) |
| Claims kiểm tra | 28 |
| INFERRED violations | 1 |
| UNCLEAR items | 2 |
| Bugs fixed | 2 |
| Verify result | PASS |
| Quality score | 83/100 → **85/100** sau khi fix |

---

## Lỗi phát hiện

### 1. Missed enum value (R3 — WMS Status filter)

**Mô tả:** Raw source có 5 WMS Status values cho filter (Open, Receiving, Received, **Completed**, Canceled). Spec chỉ ghi 4 giá trị, bỏ sót "Hoàn thành / Completed".

**Root cause:** Khi đọc raw source không có line reference → không verify lại đủ. Bảng filter và bảng mapping có số values khác nhau (filter: 5, mapping: 4) nhưng không phát hiện sự khác biệt.

**Bài học:** Với mọi enum/list values trong spec, phải ghi `#line` reference và verify đếm đủ values so với raw.

**Fix:** Đã cập nhật R3 trong `receiving_po_inbound_shipment.md`.

---

### 2. Missing navigation note (R1 — Đồng kiểm filter)

**Mô tả:** Đồng kiểm filter trong More filter có ghi chú "Move qua trang ASN" — không capture vào spec.

**Root cause:** Note nhỏ ngay sau value description, dễ bỏ qua khi đọc nhanh.

**Bài học:** Các note/lưu ý trong doc thường nằm trên dòng riêng sau field definition — phải đọc 2-3 dòng context sau mỗi field.

**Fix:** Đã bổ sung vào R1.

---

### 3. UNCLEAR về line 153 QC doc (R7 setup_criteria)

**Mô tả:** Raw line 153 "Khi muốn Active/Inactive thiết lập cho SKU thì hiện thông báo xác nhận" nằm trong section Criteria listing nhưng text đề cập "thiết lập cho SKU" — có thể là context của section SKU được copy nhầm vị trí trong doc PDF.

**Root cause:** PDF conversion tạo ra text flow khó phân biệt section boundary.

**Bài học:** Khi raw source là PDF converted, cần cẩn thận với section boundaries. Luôn đọc heading trước để confirm context.

**Action:** Đã ghi vào Q-004 của setup_criteria.

---

## Điều đã làm tốt

1. **Stub files rõ ràng:** Tất cả 7 stub specs ghi rõ "chưa đọc đầy đủ", có Blocked Coverage, không sinh testcase.
2. **Question routing đúng:** 47 câu hỏi đều nằm đúng vào section Câu hỏi chưa rõ, không có câu hỏi nào lẫn vào mô tả chính.
3. **verify pass ngay lần đầu:** Chỉ cần fix 2 lỗi nhỏ (status frontmatter + Impact section) là verify pass.
4. **Error messages được capture đầy đủ** cho 2 spec đầy đủ (setup_criteria và setup_sku).
5. **Business Rules phân tách rõ** — bảng riêng, không lẫn vào requirements.

---

## Patches được áp dụng sau session

| Patch | File | Trạng thái |
|:------|:-----|:-----------|
| PATCH-001: Source format với line reference | `.claude/skills/hasaki-wiki/references/phase_ingest.md` | ✅ Done |
| PATCH-002: `partial_read` frontmatter | `templates/tpl_requirement.md` | ✅ Done |
| PATCH-003: Enum completeness rule | `.claude/rules/20-no-inference.md` | ✅ Done |
| PATCH-004: Fix outdated paths + sampling strategy | `.claude/skills/hasaki-skill-refiner/SKILL.md` | ✅ Done |

---

## Tái sử dụng cho lần sau

- Khi ingest doc PDF lớn: ưu tiên đọc đủ từng section trước khi sang section khác — không đọc overview rồi viết spec.
- Với bảng filter/listing có enum values: grep `Giá trị:` trong raw để count values trước khi ghi vào spec.
- Stub spec: thêm `partial_read: true` vào frontmatter để phân biệt.
