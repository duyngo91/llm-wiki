---
tags: [qa/requirement, qa/feature-group/receiving-po]
status: Draft
created: 2026-05-25
updated: 2026-05-25
feature: receiving_po_packing_list
project: project_hasaki
source_version: v2.17
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Import Packing List

## Tổng quan
- **Mã tính năng:** receiving_po_packing_list
- **Feature:** Import và quản lý packing list cho PO nhận hàng
- **Mô tả ngắn:** Chức năng import packing list từ file, validate, và quản lý page packing list. Áp dụng cho SKU vải và PO có packing list. Template import có 3 cột bổ sung (v2.16).
- **Source chính:** `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.md` — mục "Import packing list", "Update 29-01-2026", "Update 16-04-2026"
- **Đối tượng sử dụng (Actors):** Nhân viên kho, Quản lý kho
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** —
- **API Spec liên quan:** N/A

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted from PDF) | `07062_Receiving_PO_Docs_ver2.17.md` | v2.17 | ✅ Hiện hành (chưa đọc đầy đủ) |

## ⚠️ Trạng thái phân tích

> **Lưu ý:** Phần Import Packing List chưa được đọc đầy đủ. Spec này là **stub** dựa trên revision history và TOC. Cần đọc thêm mục "Import packing list" (~trang 102+), "Update 29-01-2026", "Update 16-04-2026" trong raw source.

## Requirement đã xác định từ Revision History

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Validate import packing list | Functional | High | ✅ | v2.17, rev 2.12 |
| R2 | Nhận hàng PO với SKU vải cho con lẻ và combo: update UI và rules | Functional | High | ✅ | v2.17, rev 2.13 |
| R3 | Validate khi scan nhận PO liên quan đến Packing list PO | Functional | High | ✅ | v2.17, rev 2.14 |
| R4 | Bổ sung thông tin "Trừ lõi" khi khai báo UID group khi nhận PO vải | Functional | Medium | ✅ | v2.17, rev 2.15 |
| R5 | Template import: bổ sung 3 cột (chưa rõ tên cột) | Functional | High | ✅ | v2.17, rev 2.16 |
| R6 | Rules validate khi import Packing list nhận 1 phần hay cả PO | Business Rule | High | ✅ | v2.17, rev 2.16 |
| R7 | Page quản lý Packing list | Functional | High | ✅ | v2.17, rev 2.16 TOC |
| R8 | Update UI nhận SKU có UID group | Functional | High | ✅ | v2.17, rev 2.16 |
| R9–Rx | Chi tiết rules import, validate, page quản lý | Functional | — | ❓ | Chưa đọc |

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:--------------|:--------|:-------|:-----------|
| Q-001 | R5 | 3 cột bổ sung trong template import là gì? | BA | Open |
| Q-002 | R4 | "Trừ lõi" là gì? Áp dụng cho loại vải nào? | BA | Open |
| Q-003 | R6 | Sự khác biệt validate khi import 1 phần vs cả PO? | BA/Dev | Open |
| Q-004 | R9+ | Toàn bộ phần chi tiết chưa đọc | — | Open |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:----------------------|
| CHG-001~008 | receiving_po_packing_list | — | Add (mới) | — | Q-001~003 |

## Blocked Coverage
R9+ bị blocked — chưa đọc phần chi tiết trong raw source.

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R1–R8 | — | ❌ Blocked | Chờ Gate 1 + Q-001, Q-002, Q-003 |
| R9+ | — | ❌ Blocked | Blocked Coverage |

## 📅 Changelog
| Thời gian | Version | Nội dung | Nguồn |
|:----------|:--------|:---------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo stub | Raw ingest |
