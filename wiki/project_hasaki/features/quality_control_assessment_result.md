---
tags: [qa/requirement, qa/feature-group/quality-control]
status: Draft
created: 2026-05-25
updated: 2026-05-25
feature: quality_control_assessment_result
project: project_hasaki
source_version: v1.5
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Quality Control — Kết quả đánh giá (Web)

## Tổng quan
- **Mã tính năng:** quality_control_assessment_result
- **Feature:** Xem và quản lý kết quả đánh giá chất lượng sản phẩm trên Web
- **Mô tả ngắn:** Màn hình Kết quả đánh giá — xem chi tiết kết quả QC theo phiên, SKU, UID group, hình ảnh tem pass/fail.
- **Source chính:** `raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.md` — mục "Kết quả đánh giá", "18-09-2025: Chi tiết kết quả đánh giá", "Update 11-02-2026", "Update 20-04-2026"
- **Đối tượng sử dụng (Actors):** QC Staff, QC Lead, Quản lý kho (Web)
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]

## ⚠️ Trạng thái phân tích

> **Lưu ý:** Chưa đọc phần này trong raw source. Spec là **stub**.

## Requirement đã xác định (từ Revision History)

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Xem chi tiết kết quả đánh giá | Functional | High | ✅ | v1.5, rev 18-09-2025 |
| R2 | Bổ sung thông tin "SL cần đánh giá" trong chi tiết kết quả theo UID group | Functional | High | ✅ | v1.5, rev 23-02-2025 |
| R3 | Hình ảnh tem pass/fail sau khi hoàn thành đánh giá | Functional | High | ✅ | v1.5, rev 23-02-2025 |
| R4 | UID group: bổ sung cột "Đánh giá Đạt" — chặn IT nếu UID group chưa đánh giá | Business Rule | High | ✅ | v1.5, rev 23-02-2025 |
| R5 | SKU thường failed: option tạo Adjustment trả hàng nhà cung cấp | Functional | High | ✅ | v1.5, rev 20-04-2026 |
| R6 | Blocked UID group + chuyển product status = Damaged | Business Rule | High | ✅ | v1.5, rev 20-04-2026 |
| R7–Rx | Chi tiết màn hình kết quả | Functional | — | ❓ | Chưa đọc |

## ❓ Câu hỏi chưa rõ

| Q-ID | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:--------|:-------|:-----------|
| Q-001 | R4: "Chặn IT" — chặn gì? IT = Inbound Transfer? | BA | Open |
| Q-002 | R5: Adjustment trả hàng NCC — flow tiếp theo? Tạo phiếu xuất? | BA/Dev | Open |
| Q-003 | R6: Điều kiện blocked UID group và chuyển Damaged là gì? | BA | Open |
| Q-004 | Toàn bộ chi tiết màn hình chưa đọc | — | Open |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:----------------------|
| CHG-001~006 | quality_control_assessment_result | — | Add (mới) | — | Q-001~003 |

## Blocked Coverage
R7+ bị blocked. R5, R6 bị blocked do thiếu điều kiện rõ.

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R1–R6 | — | ❌ Blocked | Chờ Gate 1 + Q-001~003 |
| R7+ | — | ❌ Blocked | Blocked Coverage |

## 📅 Changelog
| Thời gian | Version | Nội dung | Nguồn |
|:----------|:--------|:---------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo stub | Raw ingest |
