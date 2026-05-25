---
aliases: [Receiving PO, Nhận hàng PO, receiving-po]
tags: [qa/feature-group-index, qa/feature-group/receiving-po]
status: Draft
project: project_hasaki
feature_group: receiving_po
created: 2026-05-25
updated: 2026-05-25
---

# 🧩 Feature Group: Receiving PO — Nhận hàng PO

## Tổng quan
- **Feature group:** `receiving_po`
- **Mục đích:** Quản lý toàn bộ quy trình nhận hàng PO trên hệ thống WMS — từ quản lý danh sách phiếu nhập (Inbound Shipment), ASN, VAS, đến nhận hàng thực tế trên App và quản lý packing list.
- **Raw source chính:** `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.md`
- **Test Plan liên quan:** —

## Feature Specs Trong Group
| Feature | Vai trò trong group | Status | Gate | Ghi chú |
|:--------|:--------------------|:-------|:-----|:-------|
| [[wiki/project_hasaki/features/receiving_po_inbound_shipment\|Inbound Shipment (Web)]] | Quản lý danh sách PO inbound | Draft | Gate 1 | |
| [[wiki/project_hasaki/features/receiving_po_inbound_shipment_detail\|Inbound Shipment Detail (Web)]] | Chi tiết phiếu nhập + giải trình | Draft | Gate 1 | |
| [[wiki/project_hasaki/features/receiving_po_asn\|ASN Management (Web)]] | Quản lý ASN, in biên bản | Draft | Gate 1 | |
| [[wiki/project_hasaki/features/receiving_po_vas\|VAS Management (Web)]] | Quản lý VAS dán tem, xác nhận | Draft | Gate 1 | Phần App chưa đọc đầy đủ |
| [[wiki/project_hasaki/features/receiving_po_app\|Receiving PO App (Mobile)]] | Luồng scan nhận hàng trên App | Draft | Gate 1 | Phần lớn chưa đọc — nhiều open question |
| [[wiki/project_hasaki/features/receiving_po_packing_list\|Import Packing List]] | Import packing list, validate | Draft | Gate 1 | |

## Test Suites Trong Group
| Test Suite | Feature cover | Số TC | Blocked coverage | Status |
|:-----------|:--------------|:------|:-----------------|:-------|
| — | — | — | — | Chờ Gate 1 |

## API Specs Trong Group
| API Spec | Feature cover | API/Interface cover | Open questions | Status |
|:---------|:--------------|:--------------------|:---------------|:-------|
| N/A | — | Không có API contract explicit trong source | — | N/A |

## Open Questions & Blocked Coverage
| Feature | Question/Blocked item | Owner | Trạng thái |
|:--------|:----------------------|:------|:-----------|
| App (Mobile) | Luồng App chiếm ~70 trang trong doc, chưa đọc đầy đủ — cần review thêm | PO/BA | Open |
| VAS | Rules VAS chi tiết cho App chưa đọc đầy đủ | PO/BA | Open |
| Figma | Link Figma `T103qrHGDj4oGCu88fCU2C` chưa truy cập được — UI/UX còn thiếu | BA/Designer | Open |
| Workflow | Link Drive `https://drive.hasaki.vn/f/6fecf6ac99424782b12a/` chưa truy cập được | BA | Open |

## Impact & Regression Notes
| Change ID / Source | Feature(s) ảnh hưởng | Regression candidate | Trạng thái |
|:-------------------|:---------------------|:---------------------|:-----------|
| Doc v2.17 (mới nhất) | Tất cả 6 features | — | Chờ spec duyệt |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo Feature Group từ 07062_Receiving_PO_Docs_ver2.17.md | Raw ingest |
