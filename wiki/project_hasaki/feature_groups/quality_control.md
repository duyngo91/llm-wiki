---
aliases: [Quality Control, Kiểm soát chất lượng, quality-control]
tags: [qa/feature-group-index, qa/feature-group/quality-control]
status: Draft
project: project_hasaki
feature_group: quality_control
created: 2026-05-25
updated: 2026-05-25
---

# 🧩 Feature Group: Quality Control — Kiểm soát chất lượng

## Tổng quan
- **Feature group:** `quality_control`
- **Mục đích:** Quản lý quy trình đánh giá chất lượng sản phẩm trong WMS — từ thiết lập tiêu chí đánh giá, gán tiêu chí cho SKU, phê duyệt, đến thực hiện đánh giá trên App và xem kết quả trên Web.
- **Raw source chính:** `raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.md`
- **Test Plan liên quan:** —

## Feature Specs Trong Group
| Feature | Vai trò trong group | Status | Gate | Ghi chú |
|:--------|:--------------------|:-------|:-----|:-------|
| [[wiki/project_hasaki/features/quality_control_setup_criteria\|Thiết lập tiêu chí (Web)]] | Tạo/Import/Quản lý tiêu chí | Draft | Gate 1 | |
| [[wiki/project_hasaki/features/quality_control_setup_sku\|Thiết lập tiêu chí cho SKU (Web)]] | Gán tiêu chí cho SKU + approval flow | Draft | Gate 1 | |
| [[wiki/project_hasaki/features/quality_control_approve\|Duyệt/Từ chối tiêu chí SKU (Web)]] | Review và phê duyệt thiết lập | Draft | Gate 1 | Chưa đọc đầy đủ phần Duyệt/Từ chối |
| [[wiki/project_hasaki/features/quality_control_assessment_result\|Kết quả đánh giá (Web)]] | Xem kết quả đánh giá, chi tiết | Draft | Gate 1 | Chưa đọc đầy đủ |
| [[wiki/project_hasaki/features/quality_control_mobile\|Đánh giá chất lượng (App)]] | Luồng đánh giá QC trên App | Draft | Gate 1 | Chưa đọc đầy đủ |

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
| Setup Criteria | Thuật ngữ & viết tắt trong doc chưa được điền vào bảng (trống) | BA | Open |
| Setup SKU | "Khi nhận PO" — chưa hỗ trợ ở phase này → scope phase này là gì? | PO | Open |
| Setup SKU | "Ngẫu nhiên" — chưa hỗ trợ ở phase này → giữ lại UI hay ẩn? | PO | Open |
| Setup SKU | "Công thức" trong Loại đánh giá → "sẽ bổ sung rules sau khi trao đổi với Dev" | Dev/BA | Open |
| Duyệt/Từ chối | Chưa đọc đầy đủ section này trong doc | — | Open |
| Assessment Result | Chưa đọc đầy đủ section này trong doc | — | Open |
| Mobile (App) | Chưa đọc đầy đủ section này trong doc | — | Open |
| Figma | Link Figma `CLtzJtUv6sA4rxyaBPnbz5` chưa truy cập được | Designer | Open |
| Workflow | Link Drive `https://drive.hasaki.vn/d/d45615dafe0b441785ff/` chưa truy cập được | BA | Open |

## Impact & Regression Notes
| Change ID / Source | Feature(s) ảnh hưởng | Regression candidate | Trạng thái |
|:-------------------|:---------------------|:---------------------|:-----------|
| Doc v1.5 (mới nhất) | Tất cả 5 features | Receiving PO (sinh VAS auto sau nhận hàng) | Chờ spec duyệt |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo Feature Group từ 07105_Quality_Control_Docs_ver1.5.md | Raw ingest |
