---
aliases: [Receiving PO Feature Group, Hasaki Receiving PO]
tags: [qa/feature-group-index, qa/feature-group/receiving-po]
status: Draft
project: project_hasaki
feature_group: receiving-po
created: 2026-05-24
updated: 2026-05-24
---

# 🧩 Feature Group: Receiving PO

## Tổng quan
- **Feature group:** `receiving-po`
- **Mục đích:** Gom các Feature Specs và Test Suites liên quan đến luồng nhận hàng PO, VAS, Packing List và Quality Control để đọc end-to-end.
- **Raw source chính:**
  - `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.pdf`
  - `raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.pdf`
- **Test Plan liên quan:** [[wiki/project_hasaki/test_plans/testplan_hasaki_2026_05|testplan_hasaki_2026_05]]

## Feature Specs Trong Group
| Feature | Vai trò trong group | Status | Gate | Ghi chú |
|:--------|:--------------------|:-------|:-----|:-------|
| [[wiki/project_hasaki/features/hasaki_receiving_inbound_shipment|Inbound Shipment & ASN Web]] | Tạo/xem ASN, đầu vào cho App Receiving và các luồng sau nhận hàng | Draft | Gate 1 | Còn câu hỏi mở trong Feature Spec |
| [[wiki/project_hasaki/features/hasaki_receiving_po_app|App PO Receiving]] | Luồng nhận hàng PO trên mobile app | Draft | Gate 1 | Còn câu hỏi mở trong Feature Spec |
| [[wiki/project_hasaki/features/hasaki_receiving_vas|VAS]] | Xác nhận dán ID, Serial/IMEI/QRCode/RFID sau nhận hàng | Draft | Gate 1 | Còn câu hỏi mở trong Feature Spec |
| [[wiki/project_hasaki/features/hasaki_receiving_packing_list|Packing List]] | Import Packing List và dữ liệu vải phục vụ nhận hàng/QC | Draft | Gate 1 | Còn câu hỏi mở trong Feature Spec |
| [[wiki/project_hasaki/features/hasaki_qc_setup|QC Setup]] | Thiết lập tiêu chí và cấu hình kiểm soát chất lượng | Draft | Gate 1 | Còn câu hỏi mở trong Feature Spec |
| [[wiki/project_hasaki/features/hasaki_qc_evaluation|QC Evaluation]] | Thực hiện đánh giá chất lượng và tác động tới VAS/nhận hàng | Draft | Gate 1 | Còn câu hỏi mở trong Feature Spec |

## Test Suites Trong Group
| Test Suite | Feature cover | Số TC hiện tại | Blocked coverage | Status |
|:-----------|:--------------|:---------------|:-----------------|:-------|
| [[wiki/project_hasaki/test_suites/test_hasaki_receiving_inbound_shipment|test_hasaki_receiving_inbound_shipment]] | [[wiki/project_hasaki/features/hasaki_receiving_inbound_shipment|hasaki_receiving_inbound_shipment]] | 23 | Có TC đang cover R còn question Open | Draft |
| [[wiki/project_hasaki/test_suites/test_hasaki_receiving_po_app|test_hasaki_receiving_po_app]] | [[wiki/project_hasaki/features/hasaki_receiving_po_app|hasaki_receiving_po_app]] | 39 | Có TC đang cover R còn question Open | Draft |
| [[wiki/project_hasaki/test_suites/test_hasaki_receiving_vas|test_hasaki_receiving_vas]] | [[wiki/project_hasaki/features/hasaki_receiving_vas|hasaki_receiving_vas]] | 26 | Có TC đang cover R còn question Open | Draft |
| [[wiki/project_hasaki/test_suites/test_hasaki_receiving_packing_list|test_hasaki_receiving_packing_list]] | [[wiki/project_hasaki/features/hasaki_receiving_packing_list|hasaki_receiving_packing_list]] | 25 | Có TC đang cover R còn question Open | Draft |
| [[wiki/project_hasaki/test_suites/test_hasaki_qc_setup|test_hasaki_qc_setup]] | [[wiki/project_hasaki/features/hasaki_qc_setup|hasaki_qc_setup]] | 31 | Có TC đang cover R còn question Open | Draft |
| [[wiki/project_hasaki/test_suites/test_hasaki_qc_evaluation|test_hasaki_qc_evaluation]] | [[wiki/project_hasaki/features/hasaki_qc_evaluation|hasaki_qc_evaluation]] | 32 | Có TC đang cover R còn question Open | Draft |

## API Specs Trong Group
| API Spec | Feature cover | API/Interface cover | Open questions | Status |
|:---------|:--------------|:--------------------|:---------------|:-------|
| Chưa có API Spec được tạo trong wiki hiện tại | receiving-po group | | Nếu PDF/task/API doc bổ sung endpoint/method/payload/status rõ ràng thì tạo `wiki/project_hasaki/api_specs/api_[feature].md` | Draft |

## Open Questions & Blocked Coverage
| Feature/Test Suite | Question/Blocked item | Owner | Trạng thái | Ghi chú |
|:-------------------|:----------------------|:------|:-----------|:-------|
| [[wiki/project_hasaki/features/hasaki_receiving_inbound_shipment|hasaki_receiving_inbound_shipment]] | Xem mục `## ❓ Câu hỏi chưa rõ` | PO/BA/Dev | Open | Chưa nên sinh thêm TC từ các điểm chưa rõ |
| [[wiki/project_hasaki/features/hasaki_receiving_po_app|hasaki_receiving_po_app]] | Xem mục `## ❓ Câu hỏi chưa rõ` | PO/BA/Dev | Open | Chưa nên sinh thêm TC từ các điểm chưa rõ |
| [[wiki/project_hasaki/features/hasaki_receiving_vas|hasaki_receiving_vas]] | Xem mục `## ❓ Câu hỏi chưa rõ` | PO/BA/Dev | Open | Chưa nên sinh thêm TC từ các điểm chưa rõ |
| [[wiki/project_hasaki/features/hasaki_receiving_packing_list|hasaki_receiving_packing_list]] | Xem mục `## ❓ Câu hỏi chưa rõ` | PO/BA/Dev | Open | Chưa nên sinh thêm TC từ các điểm chưa rõ |
| [[wiki/project_hasaki/features/hasaki_qc_setup|hasaki_qc_setup]] | Xem mục `## ❓ Câu hỏi chưa rõ` | PO/BA/Dev | Open | Chưa nên sinh thêm TC từ các điểm chưa rõ |
| [[wiki/project_hasaki/features/hasaki_qc_evaluation|hasaki_qc_evaluation]] | Xem mục `## ❓ Câu hỏi chưa rõ` | PO/BA/Dev | Open | Chưa nên sinh thêm TC từ các điểm chưa rõ |

## Impact & Regression Notes
| Change ID / Source | Feature(s) ảnh hưởng | Regression candidate | Trạng thái |
|:-------------------|:---------------------|:---------------------|:-----------|
| Governance update 2026-05-24 | Toàn bộ group `receiving-po` | Cần rà lại các TC đang cover R có question Open trước khi đề xuất regression chính thức | Draft |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-24 10:05:00 | v1.1 | Bổ sung vùng theo dõi API Specs cho group; hiện chưa có API Spec được tạo | [[WIKI_RULES]] |
| 2026-05-24 09:54:41 | v1.0 | Khởi tạo Feature Group MOC cho Hasaki Receiving PO | [[WIKI_RULES]] |
