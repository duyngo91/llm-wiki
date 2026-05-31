---
spec: stub_receiving_po_concurrent
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [Functional, UI]
---

# Test Suite — Cho nhiều user cùng nhận PO cùng lúc

## Phạm vi
- Source spec: [[stub_receiving_po_concurrent]]
- Active requirements: 6 (R001, R002, R004, R009, R010, R011 — phần không bị block hoặc test được phần clear)
- Blocked: 6 R-ID chờ open questions (R003/Q-001+Q-002, R005/R007/R008/Q-003, R011/Q-005, R001+R002/Q-006)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-CONC-001 | Mỗi user scan nhận tạo 1 ASN riêng | R001 / AC-02 | Functional | User A và User B cùng scan nhận 1 PO có cờ force ON | Hệ thống tạo ASN-A riêng và ASN-B riêng, cả 2 status = Receiving | High |
| TC-CONC-002 | Nhiều ASN cùng Receiving cho 1 PO | R001 / AC-02 | Functional | 2 user scan cùng PO, mỗi người có ASN riêng | Cả 2 ASN trạng thái Receiving tồn tại đồng thời cho cùng PO | High |
| TC-CONC-003 | 1 SKU cho phép nhiều user cùng nhận | R002 / AC-02 | Functional | User A và User B cùng nhận SKU-X của cùng 1 PO | Cả 2 user đều có thể nhận SKU-X trong ASN riêng của mình | High |
| TC-CONC-004 | Button force chỉ active khi PO status = Open | R003 / AC-01 | UI | PO status = Open; Quản lý mở Inbound detail | Button "Cho phép nhiều người cùng nhận hàng" hiển thị và có thể click | High |
| TC-CONC-005 | Button force chỉ active khi PO status = Receiving | R003 / AC-01 | UI | PO status = Receiving; Quản lý mở Inbound detail | Button "Cho phép nhiều người cùng nhận hàng" hiển thị và có thể click | High |
| TC-CONC-006 | SKU có khai báo UID group — mapping theo Số Lot + Mã cuộn | R006 / AC-04 | Functional | PO cờ force ON; SKU có UID group; User A nhận Lot L1 cuộn C1; User B nhận Lot L1 cuộn C2 | Cả 2 mapping thành công theo packing list, lưu đúng (Lô, Mã cuộn) | High |
| TC-CONC-007 | Người nhận cuối complete PO khi tổng SL ≥ qty PO | R010 / AC-07 | Functional | Tổng SL nhiều user đã nhận = qty PO - 1; User Z submit thêm khiến tổng ≥ qty PO | User Z là người complete PO; PO chuyển sang status tiếp theo | High |
| TC-CONC-008 | PO không có cờ force — không cho nhiều user cùng nhận | R003 | Functional | PO không bật cờ force; User B cố scan nhận khi User A đang nhận | Hệ thống block User B, không tạo ASN thứ 2 | High |
| TC-CONC-009 | Khai báo thiếu NCC không giao lại — 1 user đại diện complete PO | R011 / AC-08 | Functional | PO cờ force; tổng SL thực nhận < qty PO; NCC không giao lại | 1 user bất kỳ vào khai báo SL thiếu → PO được complete | Medium |
| TC-CONC-010 | BVA — Tổng qty các user bằng đúng qty PO | R010 | Functional | Tổng SL từ nhiều user = qty PO chính xác | User submit last là người complete; không báo lỗi vượt qty | High |
| TC-CONC-011 | SKU combo — không check realtime khi khai báo | R008 / AC-06 | Functional | 2 user cùng khai báo (L1, C1) cho SKU combo | Không báo lỗi ngay tại bước khai báo | High |
| TC-CONC-012 | SKU combo — báo lỗi khi submit trùng Lô + Mã cuộn | R008 / AC-06 | Functional | User B submit cùng (L1, C1) đã được User A submit trước | Hệ thống báo lỗi tại bước submit (ERR-CONC-003 — verbatim chờ Q-003 nhưng behavior xác nhận) | High |

## 🚧 Blocked Coverage

- **R003 (Q-001)** — chờ tên field/storage cho cờ force trên PO master và log audit khi bật/tắt. Không thể test audit trail.
- **R003 (Q-002)** — chờ xác nhận button force áp dụng cho PO type nào (Normal only hay tất cả type). Không thể test cho type Gift, Sample.
- **R005 (Q-003)** — chờ verbatim error messages VN+EN cho 3 trigger: qty vượt PO, trùng Lô+Mã cuộn SKU con normal, trùng SKU combo. TC-CONC-012 test behavior nhưng không verify message text.
- **R007 (AC-05, Q-003)** — chờ verbatim message ERR-CONC-002 khi trùng Lô+Mã cuộn SKU con normal. Không thể test message text.
- **R011 (Q-005)** — chờ xác nhận "hiện tại không giới hạn ai khai báo" là lỏng lẻo vĩnh viễn hay sẽ có role-based. Không thể test role restriction.
- **R001, R002 (Q-006)** — chờ xác nhận UI display nhiều ASN đồng thời trên Inbound list. Không thể test UI hiển thị.

## Regression Impact
- [[stub_receiving_po_inbound_shipment]] — ASN model, nhiều ASN Receiving cùng lúc
- [[stub_receiving_po_packing_list]] — Lô + Mã cuộn từ packing list được dùng để mapping

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.1. 12 TC active, 6 blocked coverage item.
