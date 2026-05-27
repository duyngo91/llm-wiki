---
aliases: [Quality Control, Kiểm soát chất lượng, quality-control]
tags: [qa/feature-group-index, qa/feature-group/quality_control]
status: Draft
project: project_hasaki
feature_group: quality_control
created: 2026-05-26
updated: 2026-05-26
---

# 🧩 Feature Group: Quality Control (Kiểm soát chất lượng)

## Tổng quan
- **Feature group:** `quality_control`
- **Mục đích:** Gom toàn bộ Feature Specs và Test Suites liên quan đến module Quality Control trong WMS — thiết lập tiêu chí, đánh giá sản phẩm trên Web và App, quản lý kết quả đánh giá và tích hợp với VAS.
- **Raw source chính:** `raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.md`
- **Test Plan liên quan:** *(chưa có)*

## Feature Specs Trong Group
| Feature | Vai trò trong group | Status | Gate | Ghi chú |
|:--------|:--------------------|:-------|:-----|:-------|
| [[quality_control_criteria_setup]] | Thiết lập và quản lý tiêu chí đánh giá (Web) | Draft | Gate 1 | Đọc đủ |
| [[quality_control_sku_setup]] | Thiết lập tiêu chí cho từng SKU (Web) | Draft | Gate 1 | Đọc đủ |
| [[quality_control_approval]] | Duyệt/Từ chối thiết lập tiêu chí cho SKU | Draft | Gate 1 | Đọc đủ |
| [[quality_control_assessment_result]] | Xem và quản lý kết quả đánh giá (Web) | Draft | Gate 1 | Đọc đủ |
| [[quality_control_vas_update]] | Cập nhật trạng thái VAS liên quan đến QC | Draft | Gate 1 | Đọc đủ |
| [[quality_control_mobile]] | Đánh giá chất lượng sản phẩm trên App | Draft | Gate 1 | Đọc đủ |
| [[quality_control_fabric_mobile]] | Đánh giá chất lượng vải nguyên vật liệu trên App | Draft | Gate 1 | Đọc đủ |
| [[quality_control_manual_assessment]] | Tạo mới đánh giá Manual trên App | Draft | Gate 1 | Đọc đủ |

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
| [[quality_control_sku_setup]] | Giá trị enum "Loại đánh giá" — "Công thức" chưa có rules đầy đủ ("sẽ bổ sung rules sau khi trao đổi với Dev") | BA/Dev | Open | 07105#408-409 |
| [[quality_control_criteria_setup]] | Workflow & Figma links không truy cập được | BA | Open | 07105#113-118 |
| [[quality_control_mobile]] | Điều kiện thiết lập PO sample map với PO chính chưa rõ ràng | BA | Open | 07105#1160-1168 |

## Impact & Regression Notes
| Change ID / Source | Feature(s) ảnh hưởng | Regression candidate | Trạng thái |
|:-------------------|:---------------------|:---------------------|:-----------|
| ver1.5 Update 20-04-2026 | SKU phụ liệu Failed → tạo Adjustment trả NCC | [[quality_control_mobile]], [[quality_control_assessment_result]] | Draft |
| ver1.5 Update 20-04-2026 | Blocked UID group + chuyển Damaged cho SKU vải | [[quality_control_fabric_mobile]], [[quality_control_assessment_result]] | Draft |
| ver1.5 Update 10-05-2026 | Thiết lập tiêu chí 4 điểm & từng bước từ màn hình tiêu chí | [[quality_control_criteria_setup]], [[quality_control_sku_setup]] | Draft |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo Feature Group từ 07105_Quality_Control_Docs_ver1.5 | 07105#58-95 |
