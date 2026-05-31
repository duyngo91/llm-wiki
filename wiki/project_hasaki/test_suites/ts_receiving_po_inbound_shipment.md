---
spec: stub_receiving_po_inbound_shipment
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI, Functional]
---

# Test Suite — Inbound Shipment listing + detail (Web)

## Phạm vi
- Source spec: [[stub_receiving_po_inbound_shipment]]
- Active requirements: 14 (R001, R002, R005, R006, R007-partial, R008, R011, R013, R014, R015, R016, R018, R019, R020 — phần không bị block hoàn toàn)
- Blocked: 7 R-ID/Q chờ open questions (R003+R012/Q-001, R010+R017/Q-002+Q-004+Q-005, R007/Q-003, R009/Q-006, R004/Q-007)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-INS-001 | Filter "Đồng kiểm" Yes/No trong More filter | R001 / AC-01 | UI | Listing có PO_A "Đồng kiểm=Yes", PO_B "Đồng kiểm=No"; Áp filter "Đồng kiểm=Yes" | Chỉ PO_A xuất hiện | High |
| TC-INS-002 | Filter "Đủ điều kiện nhận" Yes/No trong More filter | R002 / AC-02 | UI | PO_A Eligible=Yes, PO_B Eligible=No; Filter "Đủ điều kiện nhận=No" | Chỉ PO_B xuất hiện | High |
| TC-INS-003 | Listing column "Đủ điều kiện nhận" hiển thị Yes hoặc No | R005 | UI | Listing có PO với Eligible=Yes và PO khác Eligible=No | Cột "Đủ điều kiện nhận" hiển thị đúng Yes/No cho từng PO | High |
| TC-INS-004 | Listing column "Mô tả" hiển thị lý do PO không đủ điều kiện | R006 | UI | PO chưa được duyệt (Eligible=No) | Cột "Mô tả" hiển thị text mô tả lý do | High |
| TC-INS-005 | Mô tả DESC-INS-001 — PO chưa xác nhận | R007 / AC-04 | UI | PO status = chưa xác nhận, Eligible=No | Mô tả: `PO chưa được xác nhận` / `PO not verifed` | High |
| TC-INS-006 | Mô tả DESC-INS-002 — PO chưa duyệt | R007 / AC-04 | UI | PO status = chưa duyệt | Mô tả: `PO chưa được duyệt` / `PO not approved` | High |
| TC-INS-007 | Mô tả DESC-INS-003 — PO chưa xác nhận hoá đơn | R007 | UI | PO chưa verify invoice | Mô tả: `PO chưa được xác nhận hoá đơn` / `PO not yet verified invoice` | High |
| TC-INS-008 | Listing column "Trạng thái" bổ sung đầy đủ status PO Inside | R008 | UI | Listing | Cột Trạng thái hiển thị đủ các status PO Inside | High |
| TC-INS-009 | Mapping Inside Verified → WMS Mới/Open | R009 / AC-05 | Functional | PO Inside chuyển status Verified | PO WMS status = Mới/Open | High |
| TC-INS-010 | Mapping Inside Receiving → WMS Đang nhận hàng/Receiving | R009 | Functional | PO Inside chuyển Receiving | PO WMS = Đang nhận hàng/Receiving | High |
| TC-INS-011 | Inbound shipment detail — 2 field mới: "Đủ điều kiện nhận" + "Mô tả" | R013 / AC-07 | UI | PO Eligible=No, Mô tả="PO chưa được duyệt"; User mở detail | Section "Thông tin chung" hiển thị 2 field mới với giá trị đúng | High |
| TC-INS-012 | Detail — cột "Số lượng xác nhận / Qty confirm" | R014 | UI | Inbound shipment detail | Cột hiển thị "Số lượng xác nhận / Qty confirm" (không phải "Số lượng" cũ) | High |
| TC-INS-013 | Detail — cột "Số lượng đã nhận / Qty received" | R015 | UI | Inbound shipment detail có ASN đã nhận | Cột hiển thị tổng SL đã scan nhận theo ASN | High |
| TC-INS-014 | Detail — công thức "Số lượng thiếu" = Qty confirm − Qty received | R016 / AC-08 | Functional | SKU_A Qty confirm=100, Qty received=60 | Số lượng thiếu = 40 | High |
| TC-INS-015 | Giải trình — nhập comment | R019 / AC-09 | Functional | PO treo Receiving; User click "Thêm", nhập "Chờ NCC giao tiếp", submit | Comment xuất hiện với TT, Nội dung, Người tạo (email HSK), Ngày tạo | High |
| TC-INS-016 | Giải trình — sắp xếp giảm dần theo thời gian tạo | R018 / AC-10 | UI | 3 comments tạo T1, T2, T3 (T1 < T2 < T3) | Order hiển thị: T3, T2, T1 (mới nhất trước) | Medium |
| TC-INS-017 | Button "Thêm" hiển thị ở mọi status PO | R019 / AC-11 | UI | PO status = "Đã nhận hàng/Received"; Mở detail | Button "Thêm" vẫn hiển thị | High |
| TC-INS-018 | BVA — Số lượng thiếu = 0 (đã nhận đủ) | R016 | Functional | Qty confirm = Qty received = 50 | Số lượng thiếu = 0 | Medium |
| TC-INS-019 | Filter "Trạng thái WMS" chỉ áp dụng cho Type = PO | R003-partial / AC-03 | Functional | Listing có PO và non-PO type; Filter WMS status | Non-PO type không bị lọc/ảnh hưởng bởi filter WMS status | High |
| TC-INS-020 | Giải trình — columns đầy đủ: TT, Nội dung, Người tạo, Ngày tạo | R020 | UI | Xem section giải trình | 4 cột: TT/No, Nội dung/Content, Người tạo/Created by, Ngày tạo/Created date | High |

## 🚧 Blocked Coverage

- **R003, R012 (Q-001)** — chờ resolve inconsistency "Hoàn thành/Completed" có là WMS status thật hay không. Filter WMS status có 5 values nhưng định nghĩa R012 chỉ 4. Không thể test filter 5 values vs 4 values WMS status.
- **R010, R017 (Q-002)** — chờ xác nhận enforcement khi cuối ngày user chưa giải trình PO Receiving (block hay chỉ report). Không thể test enforcement.
- **R007 DESC-INS-004 (Q-003)** — chờ logic multi-SKU cho placeholder `{sku_code}` trong message DESC-INS-004 "SKU tester chưa khai báo SKU gốc". Không thể test message với PO có nhiều SKU tester.
- **R010 (Q-004)** — chờ format "thời gian đã bao lâu" (HH:MM hay số giờ). TC-INS hiện không có TC cho cột thời gian Receiving do chưa rõ format.
- **R017 (Q-005)** — chờ định nghĩa "PO giao trong ngày" (ngày tạo PO, ngày giao, hay ngày scan). Không thể test trigger giải trình.
- **R009 (Q-006)** — chờ xác nhận sync 2 chiều Inside ↔ WMS có conflict không. Không thể test sync direction.
- **R004 (Q-007)** — chờ xác nhận input "Đồng kiểm" ở đâu trên App (mặc định Yes/No, sửa được không). Không thể test data source cho cột Đồng kiểm.

## Regression Impact
- [[stub_receiving_po_asn]] — filter Đồng kiểm move qua ASN
- [[stub_receiving_po_invoice]] — PO chưa xác nhận hoá đơn (DESC-INS-003)

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.1. 20 TC active, 7 blocked coverage item.
