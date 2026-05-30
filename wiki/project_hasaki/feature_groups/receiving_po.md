---
aliases: [receiving_po]
tags: [qa/feature-group-index, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
project: project_hasaki
---

# Feature Group: receiving_po

## Mục đích

Nhận hàng PO — gom các Feature Spec liên quan đến luồng nghiệp vụ này. Hiện toàn bộ là per-feature stub `partial_read: true`, cần refine từng spec đọc raw để promote về `partial_read: false` (Gate 1B).

## Specs hiện hành

| Spec | Mô tả ngắn | Status |
|:-----|:-----------|:-------|
| [[stub_receiving_po_overview]] | Tổng quan, thuật ngữ và workflow nhận hàng PO | Draft, partial_read: true |
| [[stub_receiving_po_inbound_shipment]] | Inbound Shipment và detail | Draft, partial_read: true |
| [[stub_receiving_po_asn]] | ASN list, detail và xem chi tiết sản phẩm | Draft, partial_read: true |
| [[stub_receiving_po_vas]] | VAS list, detail, Serial/Imei/Label code, group UID, không đồng kiểm SPKPH | Draft, partial_read: true |
| [[stub_receiving_po_app]] | Receiving PO trên App: confirm unsuitable, scan, update rules | Draft, partial_read: true |
| [[stub_receiving_po_date_rules]] | Rules tính ngày nhận, cập nhật date cho combo, status ASN, tồn kho | Draft, partial_read: true |
| [[stub_receiving_po_invoice]] | Thêm hoá đơn cho PO, PO Gift chung PO thường | Draft, partial_read: true |
| [[stub_receiving_po_fabric]] | Nhận hàng vải với khai báo Group UID | Draft, partial_read: true |
| [[stub_receiving_po_gift]] | Nhận riêng PO Gift | Draft, partial_read: true |
| [[stub_receiving_po_no_barcode]] | Nhận hàng SKU không barcode | Draft, partial_read: true |
| [[stub_receiving_po_confirm_paste_id]] | Confirm paste ID (App): VAS phiên, RFID cases | Draft, partial_read: true |
| [[stub_receiving_po_vas_manual]] | Create/Update VAS manual, RFID outside vendor, tạo thủ công VAS | Draft, partial_read: true |
| [[stub_receiving_po_packing_list]] | Import packing list, nhận PO vải theo packing list, returns, page quản lý | Draft, partial_read: true |
| [[stub_receiving_po_po_sample]] | PO sample và PO chính | Draft, partial_read: true |
| [[stub_receiving_po_concurrent]] | Nhiều user nhận cùng lúc | Draft, partial_read: true |

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Initial feature group sau khi tách monster stub | split-stubs-2026-05-30 |
