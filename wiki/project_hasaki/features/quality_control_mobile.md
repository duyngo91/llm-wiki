---
tags: [qa/requirement, qa/feature-group/quality-control]
status: Draft
created: 2026-05-25
updated: 2026-05-25
feature: quality_control_mobile
project: project_hasaki
source_version: v1.5
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Quality Control — Đánh giá chất lượng (App)

## Tổng quan
- **Mã tính năng:** quality_control_mobile
- **Feature:** Đánh giá chất lượng sản phẩm trên App (Mobile)
- **Mô tả ngắn:** Luồng đánh giá QC trên App — scan UID group, nhập số lượng cần đánh giá, đánh giá theo tiêu chí (Pass/Fail hoặc theo điều kiện), chụp hình tem QC, đánh giá vải nguyên vật liệu.
- **Source chính:** `raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.md` — mục "Đánh giá chất lượng sản phẩm - Mobile", "Update 18-09-2025 – Đánh giá chất lượng vải", "Update 11-02-2026", "Update 20-04-2026"
- **Đối tượng sử dụng (Actors):** QC Staff (App Mobile)
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]

## ⚠️ Trạng thái phân tích

> **Lưu ý:** Chưa đọc phần Mobile QC trong raw source. Spec là **stub**.

## Requirement đã xác định (từ Revision History)

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Đánh giá theo điều kiện trên App — nhập kết quả để trả ra Đạt/Không đạt | Functional | High | ✅ | v1.5, rev 07-08-2025 |
| R2 | Hình chụp mẫu hiển thị trong màn hình đánh giá | Functional | Medium | ✅ | v1.5, rev 07-08-2025 |
| R3 | Đánh giá chất lượng vải nguyên vật liệu | Functional | High | ✅ | v1.5, rev 17-09-2025 |
| R4 | Bước scan UID group: bổ sung cho user cập nhật số lượng cần đánh giá | Functional | High | ✅ | v1.5, rev 23-02-2025 (Web update) |
| R5 | Sau khi "Hoàn thành" đánh giá: chụp hình tem QC | Functional | High | ✅ | v1.5, rev 23-02-2025 |
| R6 | Manual assessment: tạo mới đánh giá thủ công (v1.5 có update) | Functional | Medium | ✅ | v1.5, TOC trang 46+ |
| R7–Rx | Chi tiết flow đánh giá trên App | Functional | — | ❓ | Chưa đọc |

## ❓ Câu hỏi chưa rõ

| Q-ID | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:--------|:-------|:-----------|
| Q-001 | "Tạo mới đánh giá – Manual (bỏ)" trong TOC — tính năng này bị bỏ và thay bằng gì? | PO | Open |
| Q-002 | Flow đánh giá vải: khác gì so với đánh giá SKU thường? | BA | Open |
| Q-003 | Toàn bộ chi tiết flow App chưa đọc | — | Open |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:----------------------|
| CHG-001~006 | quality_control_mobile | — | Add (mới) | — | Q-001~003 |

## Blocked Coverage
Toàn bộ spec bị blocked do chưa đọc raw source.

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R1–R6 | — | ❌ Blocked | Chờ Gate 1 |
| R7+ | — | ❌ Blocked | Blocked Coverage |

## 📅 Changelog
| Thời gian | Version | Nội dung | Nguồn |
|:----------|:--------|:---------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo stub | Raw ingest |
