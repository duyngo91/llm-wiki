---
tags: [qa/requirement, qa/feature-group/receiving-po]
status: Draft
created: 2026-05-25
updated: 2026-05-25
feature: receiving_po_app
project: project_hasaki
source_version: v2.17
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Receiving PO App (Mobile)

## Tổng quan
- **Mã tính năng:** receiving_po_app
- **Feature:** Nhận hàng PO trên App HSK Work (Mobile) — scan PO, scan SKU, xử lý các case đặc biệt
- **Mô tả ngắn:** Luồng nhận hàng chính trên App — chiếm phần lớn tài liệu (~70+ trang). Bao gồm: nhận PO thường, PO Gift, PO vải (Group UID), SKU không barcode, confirm unsuitable product, PO Sample, multi-user receiving.
- **Source chính:** `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.md` — mục "Receiving PO (App)", "Case 1", "Case 2", "Nhận hàng Vải", "Nhận hàng SKU không barcode", "Confirm paste ID", "PO sample & PO chính", "Cho nhiều user cùng nhận"
- **Đối tượng sử dụng (Actors):** Nhân viên kho (Mobile App)
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** —
- **API Spec liên quan:** N/A

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted from PDF) | `07062_Receiving_PO_Docs_ver2.17.md` | v2.17 | ✅ Hiện hành (chưa đọc đầy đủ) |
| 2 | Figma | `https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO_Update` | — | ❓ Chưa đọc được |

## ⚠️ Trạng thái phân tích

> **Lưu ý:** Đây là phần lớn nhất của tài liệu, chưa được đọc đầy đủ. Spec này là **stub** dựa trên TOC (trang 5-6) và revision history. Cần đọc toàn bộ các mục App trong raw source trước khi hoàn chỉnh.

## Sub-features đã xác định từ TOC

| Sub-feature | Trang trong doc | Trạng thái phân tích |
|:-----------|:----------------|:--------------------|
| Case 1: Nhận PO thường (không có PO Gift) | ~41-62 | Chưa đọc |
| Thêm hoá đơn cho PO | ~62-67 | Chưa đọc |
| Case 2: Nhận PO Gift chung với PO thường | ~68-73 | Chưa đọc |
| Nhận hàng Vải (Group UID) | ~74-78 | Chưa đọc |
| Nhận PO gift riêng | ~79 | Chưa đọc |
| Nhận SKU không barcode | ~80-83 | Chưa đọc |
| Confirm paste ID (App) | ~84-95 | Chưa đọc |
| Nhận PO SKU có RFID | ~97-98 | Chưa đọc |
| Nhận PO SKU vải theo packing list | ~106-115 | Chưa đọc |
| PO Sample & PO chính | ~118-119 | Chưa đọc |
| Cho nhiều user cùng nhận cùng lúc | ~119 | Chưa đọc |

## Requirement đã xác định từ Revision History

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Bỏ qua scan location nếu nhận PO zone ở kho 170 | Business Rule | High | ✅ | v2.17, rev 1.5 |
| R2 | Hỗ trợ khai báo thiếu hàng cho tất cả SKU chưa nhận đủ SL theo PO | Functional | High | ✅ | v2.17, rev 1.6 |
| R3 | Biên bản nhận hàng cho PO Gift kèm PO gốc | Functional | High | ✅ | v2.17, rev 1.6 |
| R4 | Xác nhận dán ID cho SKU là Tài sản cố định có quản lý Serial/IMEI | Functional | High | ✅ | v2.17, rev 1.6 |
| R5 | Nhận riêng PO gift — nếu PO gốc có nhiều PO gift: phải nhận hết PO gift trước khi nhận PO gốc | Business Rule | High | ✅ | v2.17, rev 1.7 |
| R6 | Xoá sản phẩm đã scan nhận trước đó | Functional | Medium | ✅ | v2.17, rev 1.8 |
| R7 | PO không đồng kiểm: bỏ qua scan camera nếu kho bật config "Required camera" | Business Rule | High | ✅ | v2.17, rev 2.4 18-02-2025 |
| R8 | PO không đồng kiểm + khai báo SPKPH → sinh return vendor | Business Rule | High | ✅ | v2.17, rev 2.5 28-02-2025 |
| R9 | Nhận SKU không barcode | Functional | High | ✅ | v2.17, rev 2.8 22-05-2025 |
| R10 | Nhận SKU combo + con lẻ có required date | Functional | High | ✅ | v2.17, rev 2.9 |
| R11 | Nhận SKU có RFID: scan RFID khi nhận PO, bỏ qua VAS auto (điều kiện: Category Thời trang, Brand Synctives) | Business Rule | High | ✅ | v2.17, rev 2.10 |
| R12 | Nhận hàng khai báo Group UID cho sản phẩm Vải NVL | Functional | High | ✅ | v2.17, rev 2.11 |
| R13 | Import packing list + validate | Functional | High | ✅ | v2.17, rev 2.12-2.16 |
| R14 | PO Sample: cần ghi nhận thông tin PO "Sample" thuộc PO chính (mới nhất — rev 2.17) | Functional | High | ✅ | v2.17, rev 2.17 |
| R15 | Cho nhiều user cùng nhận cùng lúc (mới nhất — rev 2.17) | Functional | High | ✅ | v2.17, rev 2.17 |
| R16–Rx | Chi tiết flow App (screen-by-screen) | Functional | — | ❓ | v2.17 — chưa đọc |

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:--------------|:--------|:-------|:-----------|
| Q-001 | R5 | "Nhiều PO gift" — nếu user cố nhận PO gốc trước: lỗi gì? Block hay cảnh báo? | PO/BA | Open |
| Q-002 | R7 | Config "Required camera" ở đâu (Warehouse config)? Scope áp dụng của config này? | Dev/BA | Open |
| Q-003 | R8 | SPKPH = gì? Return vendor flow cụ thể như thế nào? | BA | Open |
| Q-004 | R14 | PO Sample: "cần ghi nhận thông tin PO Sample thuộc PO chính" — field nào, bắt buộc hay optional? | BA | Open |
| Q-005 | R15 | Multi-user receiving: conflict resolution khi 2 user scan cùng SKU cùng lúc? | Dev | Open |
| Q-006 | All R16+ | Toàn bộ flow App chi tiết chưa đọc | — | Open |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:----------------------|
| CHG-001~015 | receiving_po_app | — | Add (mới) | — | Q-001~006 |

## Blocked Coverage
R16 trở đi bị blocked — chưa đọc phần App chi tiết trong raw source. Cần đọc thêm ~70 trang trong doc.

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R1–R15 | — | ❌ Blocked | Chờ Gate 1 |
| R16+ | — | ❌ Blocked | Blocked Coverage — chưa đọc source |

## 📅 Changelog
| Thời gian | Version | Nội dung | Nguồn |
|:----------|:--------|:---------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo stub | Raw ingest |
