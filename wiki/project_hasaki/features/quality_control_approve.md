---
tags: [qa/requirement, qa/feature-group/quality-control]
status: Draft
created: 2026-05-25
updated: 2026-05-25
feature: quality_control_approve
project: project_hasaki
source_version: v1.5
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Quality Control — Duyệt/Từ chối tiêu chí SKU (Web)

## Tổng quan
- **Mã tính năng:** quality_control_approve
- **Feature:** Phê duyệt hoặc từ chối thiết lập tiêu chí QC cho SKU
- **Mô tả ngắn:** Màn hình Duyệt/Từ chối trong tab Thiết lập SKU — người có quyền duyệt review thiết lập "Chờ duyệt" và chuyển sang Approved hoặc Rejected.
- **Source chính:** `raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.md` — mục "Duyệt/Từ chối"
- **Đối tượng sử dụng (Actors):** QC Lead / Manager (Web)
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Mối quan hệ:**
  - ⬅️ [[wiki/project_hasaki/features/quality_control_setup_sku|Setup SKU]] — thiết lập "Chờ duyệt" mới đến đây

## ⚠️ Trạng thái phân tích

> **Lưu ý:** Mục "Duyệt/Từ chối" trong raw source chưa được đọc. Spec này là **stub**. Cần đọc thêm trang 19-21 trong doc trước khi hoàn chỉnh.

## Requirement đã xác định (từ context)

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Người dùng có quyền có thể xem detail thiết lập SKU ở trạng thái "Chờ duyệt" để Duyệt hoặc Từ chối | Functional | High | ✅ | v1.5, TOC mục Duyệt/Từ chối |
| R2–Rx | Chi tiết màn hình, fields, actions, error messages | Functional | — | ❓ | Chưa đọc |

## ❓ Câu hỏi chưa rõ

| Q-ID | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:--------|:-------|:-----------|
| Q-001 | Toàn bộ nội dung mục Duyệt/Từ chối chưa đọc — cần đọc trang 19-21 trong doc | — | Open |
| Q-002 | Khi Từ chối: có yêu cầu nhập lý do không? Thiết lập SKU chuyển về trạng thái nào? | PO | Open |
| Q-003 | Ai có quyền duyệt? Role cụ thể trong hệ thống? | PO/Dev | Open |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:----------------------|
| CHG-001 | quality_control_approve | — | Add (mới) | — | Q-001~003 |

## Blocked Coverage
Toàn bộ spec bị blocked — chưa đọc phần "Duyệt/Từ chối" trong raw source.

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R1 | — | ❌ Blocked | Chờ Gate 1 |
| R2+ | — | ❌ Blocked | Blocked Coverage — chưa đọc source |

## 📅 Changelog
| Thời gian | Version | Nội dung | Nguồn |
|:----------|:--------|:---------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo stub | Raw ingest |
