---
aliases: [Nhận hàng PO, receiving-po]
tags: [qa/feature-group-index, qa/feature-group/receiving_po]
status: Draft
project: project_hasaki
feature_group: receiving_po
created: 2026-05-26
updated: 2026-05-26
---

# 🧩 Feature Group: Nhận hàng PO (Receiving PO)

## Tổng quan
- **Feature group:** `receiving_po`
- **Mục đích:** Gom toàn bộ Feature Specs và Test Suites liên quan đến luồng nhận hàng PO trên WMS — bao gồm quản lý Inbound Shipment, ASN, VAS trên Web và các luồng nhận hàng trên App.
- **Raw source chính:** `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.md`
- **Test Plan liên quan:** *(chưa có)*

## Feature Specs Trong Group
| Feature | Vai trò trong group | Status | Gate | Ghi chú |
|:--------|:--------------------|:-------|:-----|:-------|
| [[receiving_po_inbound_shipment]] | Quản lý danh sách và chi tiết Inbound Shipment trên Web | Draft | Gate 1 | |
| [[receiving_po_asn]] | Quản lý ASN (Advanced Shipment Notice) trên Web | Draft | Gate 1 | |
| [[receiving_po_vas]] | Quản lý VAS (Value Added Service) trên Web | Draft | Gate 1 | |
| [[receiving_po_app]] | Luồng nhận hàng PO trên App (Case 1 – PO thường, Case 2 – PO Gift) | Draft | Gate 1 | partial_read: true |
| [[receiving_po_confirm_paste_id]] | Xác nhận dán ID (Serial/IMEI/RFID) trên App | Draft | Gate 1 | partial_read: true |
| [[receiving_po_vas_manual]] | Tạo VAS thủ công trên Web/App | Draft | Gate 1 | partial_read: true |
| [[receiving_po_packing_list]] | Import và quản lý Packing List | Draft | Gate 1 | partial_read: true |
| [[receiving_po_fabric_uid_group]] | Nhận hàng vải khai báo Group UID | Draft | Gate 1 | partial_read: true |

## Test Suites Trong Group
| Test Suite | Feature cover | Số TC | Blocked coverage | Status |
|:-----------|:--------------|:------|:-----------------|:-------|
| *(chưa tạo)* | | | | |

## API Specs Trong Group
| API Spec | Feature cover | API/Interface cover | Open questions | Status |
|:---------|:--------------|:--------------------|:---------------|:-------|
| N/A | Không có API explicit trong source | — | — | — |

## Open Questions & Blocked Coverage
| Feature/Test Suite | Question/Blocked item | Owner | Trạng thái | Ghi chú |
|:-------------------|:----------------------|:------|:-----------|:-------|
| [[receiving_po_app]] | Chưa đọc đủ sections App (Case 1 – page 41 đến 118) | BA | Open | Cần đọc thêm raw source |
| [[receiving_po_confirm_paste_id]] | Chưa đọc đủ section Confirm paste ID (App) từ page 84 | BA | Open | partial_read |
| [[receiving_po_vas_manual]] | Chưa đọc đủ Create/Update VAS manual (page 96+) | BA | Open | partial_read |
| [[receiving_po_packing_list]] | Chưa đọc đủ Import packing list (page 102+) | BA | Open | partial_read |
| [[receiving_po_fabric_uid_group]] | Chưa đọc đủ Nhận hàng vải Group UID (page 74+) | BA | Open | partial_read |

## Impact & Regression Notes
| Change ID / Source | Feature(s) ảnh hưởng | Regression candidate | Trạng thái |
|:-------------------|:---------------------|:---------------------|:-----------|
| ver2.17 (17-05-2026) | PO sample & PO chính; Cho nhiều user cùng nhận cùng lúc | [[receiving_po_app]] | Draft |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo Feature Group từ 07062_Receiving_PO_Docs_ver2.17 | 07062#138-184 |
