---
tags: [qa/kanban]
project: project_hasaki
status: Done
updated: 2026-05-30
---

# Kanban — project_hasaki

## TODO

### Refine Feature Group [[receiving_po]] (15 per-feature stub)

- [x] [[stub_receiving_po_overview]] — tổng quan, thuật ngữ, workflow ✅ Refined 2026-05-30 (Q-001..Q-007 Open)
- [x] [[stub_receiving_po_inbound_shipment]] — Inbound Shipment list + detail ✅ Refined 2026-05-30 (Q-001..Q-007 Open)
- [x] [[stub_receiving_po_asn]] — ASN list/detail, xem chi tiết sản phẩm ✅ Refined 2026-05-30 (Q-001..Q-010 Open)
- [x] [[stub_receiving_po_vas]] — VAS list/detail, Serial/Imei/Label, group UID, SPKPH ✅ Refined 2026-05-30 (Q-001..Q-013 Open)
- [x] [[stub_receiving_po_app]] — Receiving PO trên App: confirm unsuitable, scan, update rules ✅ Refined 2026-05-30 (Q-001..Q-012 Open)
- [x] [[stub_receiving_po_date_rules]] — rules tính ngày nhận, combo date, ASN status, tồn kho ✅ Refined 2026-05-30 (Q-001..Q-016 Open)
- [x] [[stub_receiving_po_invoice]] — Thêm hoá đơn, PO Gift chung PO thường ✅ Refined 2026-05-30 (Q-001..Q-012 Open)
- [x] [[stub_receiving_po_fabric]] — Nhận hàng vải với khai báo Group UID ✅ Refined 2026-05-30 (Q-001..Q-010 Open)
- [x] [[stub_receiving_po_gift]] — Nhận riêng PO Gift ✅ Refined 2026-05-30 (Q-001..Q-005 Open)
- [x] [[stub_receiving_po_no_barcode]] — Nhận SKU không barcode ✅ Refined 2026-05-30 (Q-001..Q-006 Open)
- [x] [[stub_receiving_po_confirm_paste_id]] — Confirm paste ID, VAS phiên, RFID cases ✅ Refined 2026-05-30 (Q-001..Q-014 Open)
- [x] [[stub_receiving_po_vas_manual]] — Create/Update VAS manual, RFID outside vendor ✅ Refined 2026-05-30 (Q-001..Q-014 Open)
- [x] [[stub_receiving_po_packing_list]] — Import packing list, nhận PO vải, returns, page quản lý ✅ Refined 2026-05-30 (Q-001..Q-016 Open)
- [x] [[stub_receiving_po_po_sample]] — PO sample và PO chính ✅ Refined 2026-05-30 (Q-001..Q-006 Open)
- [x] [[stub_receiving_po_concurrent]] — Nhiều user nhận cùng lúc ✅ Refined 2026-05-30 (Q-001..Q-006 Open)

### Refine Feature Group [[quality_control]] (9 per-feature stub)

- [x] [[stub_qc_overview]] — tổng quan, thuật ngữ, workflow QC ✅ Refined 2026-05-30 (Q-001..Q-006 Open)
- [x] [[stub_qc_criteria_setup]] — Thiết lập tiêu chí, đánh giá từng bước, tiêu chí 4 điểm ✅ Refined 2026-05-30 (Q-001..Q-015 Open)
- [x] [[stub_qc_criteria_sku]] — Thiết lập tiêu chí cho SKU ✅ Refined 2026-05-30 (Q-001..Q-010 Open)
- [x] [[stub_qc_criteria_approval]] — Duyệt / Từ chối tiêu chí ✅ Refined 2026-05-30 (Q-001..Q-006 Open)
- [x] [[stub_qc_evaluation_result]] — Kết quả đánh giá (Web + App) ✅ Refined 2026-05-30 (Q-001..Q-010 Open)
- [x] [[stub_qc_vas]] — QC VAS updated ✅ Refined 2026-05-30 (Q-001..Q-008 Open)
- [x] [[stub_qc_evaluation_mobile]] — Đánh giá chất lượng SP trên Mobile (vải Web) ✅ Refined 2026-05-30 (Q-001..Q-011 Open)
- [x] [[stub_qc_evaluation_manual]] — Tạo đánh giá Manual, SKU phụ liệu, Blocked UID ✅ Refined 2026-05-30 (Q-001..Q-016 Open)
- [x] [[stub_qc_uid_group]] — UID group: khai báo SL App, tem QC, lưu ý ✅ Refined 2026-05-30 (Q-001..Q-009 Open)

### Test design (Gate 2)

- [ ] Chờ Gate 1B pass cho từng stub trên trước khi gọi `/wiki-test-designer`.

**24/24 stubs đã refine** ✅ — sẵn sàng cho Gate 1B review (PO + answer questions Q-001..Q-016 per spec). Sau Gate 1B → mới chạy `/wiki-test-designer`.

## InProgress

(none)

## Done

- [x] **Bootstrap ingest 2 raw docs** — 2026-05-30. Index skeleton 62 + 36 sections, evidence_index 98 R.
- [x] **Tách monster stub → per-feature stub** — 2026-05-30. 24 per-feature stub (15 receiving_po + 9 quality_control), 24 placeholder test suite, 2 feature group page (`receiving_po`, `quality_control`). `check_ingest.py` exit 0.
- [x] **Refine batch 1 (5 stub nhỏ nhất)** — 2026-05-30. po_sample, concurrent, qc_criteria_approval, gift, no_barcode. 47 R + 36 AC + 32 BR + 13 error/message rows + 29 questions Open. `check_ingest.py` exit 0.
- [x] **Refine batch 2 (6 stub vừa)** — 2026-05-30. inbound_shipment, qc_criteria_sku, qc_vas, qc_evaluation_mobile, asn, invoice. 161 R + 97 AC + 74 BR + 23 messages + 58 questions Open. Auto-fix 17 phantom evidence (heading-like start lines, shift +1). `check_ingest.py` exit 0.
- [x] **Refine batch 3 (5 stub vừa)** — 2026-05-30. fabric, qc_evaluation_result, qc_uid_group, qc_overview, receiving_po_overview. Tổng pipeline state sau batch 3: 333 R + 189 AC + 154 BR + 137 Q + 333/333 OK_CANONICAL. Auto-fix 1 phantom (qc_overview R004 L123 empty → shift +1). `check_ingest.py` exit 0.
- [x] **Refine batch 4 (4 stub vừa-lớn)** — 2026-05-30. receiving_po_vas, receiving_po_app, receiving_po_confirm_paste_id, receiving_po_vas_manual. Tổng pipeline state sau batch 4: 432 R + 292 AC + 235 BR + 186 Q + 432/432 OK_CANONICAL. Auto-fix 13 phantoms (PDF table row Step-numbered start lines, shift +1) + 2 INVALID_FORMAT (pipe `\|` trong claim_text bị parser nuốt → đổi sang dấu phẩy). `check_ingest.py` exit 0.
- [x] **Refine batch 5 (4 stub lớn nhất)** — 2026-05-30. receiving_po_date_rules, qc_evaluation_manual, qc_criteria_setup, receiving_po_packing_list. Tổng pipeline state sau batch 5: **528 R + 416 AC + 341 BR + 245 Q + 528/528 OK_CANONICAL**. Auto-fix 6 phantoms (5 PDF table row + 1 blank line). `check_ingest.py` exit 0. **🎉 Hoàn thành 24/24 stubs refine.**
- [x] **Fix recurring bugs trong evidence_index.py + verify_source_refs.py** — 2026-05-30. (1) `parse_table_rows` không honor `\|` escape → fix bằng placeholder swap. (2) `HEADING_RE` over-aggressive cho PDF table row numbered → tách thành `_looks_like_heading()` với content-marker heuristic (skip nếu line chứa `:`, ` - `, `/ ` — content markers).
