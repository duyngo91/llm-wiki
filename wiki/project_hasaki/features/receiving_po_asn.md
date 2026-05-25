---
tags: [qa/requirement, qa/feature-group/receiving-po]
status: Draft
created: 2026-05-25
updated: 2026-05-25
feature: receiving_po_asn
project: project_hasaki
source_version: v2.17
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: ASN Management (Web)

## Tổng quan
- **Mã tính năng:** receiving_po_asn
- **Feature:** Quản lý ASN (Advanced Shipment Notice) trên Web — filter, listing, in biên bản
- **Mô tả ngắn:** Menu Inbound / ASN — cập nhật filter và tính năng in biên bản với tùy chọn khổ giấy và phạm vi in.
- **Source chính:** `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.md` — mục "ASN – Updated", "ASN detail – Updated"
- **Đối tượng sử dụng (Actors):** Nhân viên kho, Quản lý kho
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** —
- **API Spec liên quan:** N/A

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted from PDF) | `07062_Receiving_PO_Docs_ver2.17.md` | v2.17 | ✅ Hiện hành |
| 2 | Figma | `https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO_Update` | — | ❓ Chưa đọc được |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Filter: Mã ASN (tìm chính xác), Mã phiếu nhập, Phiếu nhập nguồn mapping, Mã phiếu xuất, Phiếu xuất nguồn mapping | Functional | High | ✅ | v2.17, ASN Filter |
| R2 | Filter: Kho — load theo location + phân quyền, hỗ trợ chọn nhiều, gợi ý từ 3 ký tự | Functional | High | ✅ | v2.17, ASN Filter |
| R3 | Filter: SKU/Barcode — tìm theo SKU hoặc Barcode trong chi tiết ASN | Functional | Medium | ✅ | v2.17, ASN Filter |
| R4 | Filter: Loại (Type) — Purchase order / Customer return / Internal transfer / Adjustment; hỗ trợ chọn nhiều | Functional | Medium | ✅ | v2.17, ASN Filter |
| R5 | Filter: Người sở hữu (Owner) — Hasaki Cosmetics / Hasaki WMS / Hasaki OMS; hỗ trợ chọn nhiều | Functional | Medium | ✅ | v2.17, ASN Filter |
| R6 | Filter: Trạng thái — Open / Receiving / Received / Canceled; hỗ trợ chọn nhiều | Functional | Medium | ✅ | v2.17, ASN Filter |
| R7 | Filter: Đồng kiểm (Yes/No), Từ ngày…Đến ngày | Functional | Low | ✅ | v2.17, ASN Filter |
| R8 | In biên bản — tùy chọn "In tất cả sản phẩm": mặc định chỉ in SP có thiếu/SPKPH; nếu tích chọn → in hết tất cả đã nhận | Functional | High | ✅ | v2.17, ASN Listing |
| R9 | In biên bản — tùy chọn "Khổ giấy": A5 (mặc định) hoặc In Bill; lưu theo máy local (không cần chọn lại lần sau) | Functional | Medium | ✅ | v2.17, ASN Listing |
| R10 | ASN detail — phần chi tiết và 16-09-2025 update: chưa đọc đầy đủ | Functional | — | ❓ | v2.17, ASN detail |

## 🔄 Luồng Nghiệp Vụ

### Luồng chuẩn — In biên bản (Happy Path)
1. User ở danh sách ASN, chọn ASN cần in
2. Chọn tùy chọn in: "In tất cả sản phẩm" (tick/untick), "Khổ giấy" (A5/In Bill)
3. Hệ thống lưu khổ giấy theo local, in biên bản theo template tương ứng

## ⚙️ Quy Tắc Nghiệp Vụ

| Rule | Mô tả |
|:-----|:------|
| Khổ giấy | Lưu theo máy local — chọn 1 lần, áp dụng cho các lần sau đến khi thay đổi |
| In mặc định | Chỉ in SP có khai báo thiếu hoặc SPKPH |
| In tất cả | In hết tất cả SP đã nhận trong ASN |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi
- Không có error message explicit trong source cho màn hình này.

## 🏁 Tiêu Chí Nghiệm Thu (BDD)

- **Scenario 1: Khổ giấy được lưu local**
  - **Given:** User chọn khổ giấy "In Bill" lần đầu
  - **When:** User thoát và quay lại chọn in lần sau
  - **Then:** Khổ giấy mặc định vẫn là "In Bill"

- **Scenario 2: In tất cả sản phẩm**
  - **Given:** ASN có 5 SP, trong đó 2 SP có thiếu
  - **When:** User tick "In tất cả sản phẩm" và in
  - **Then:** Biên bản in 5 SP

- **Scenario 3: In mặc định (không tick)**
  - **Given:** ASN có 5 SP, trong đó 2 SP có thiếu
  - **When:** User không tick và in
  - **Then:** Biên bản in 2 SP có thiếu

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:--------------|:--------|:-------|:-----------|
| Q-001 | R10 | ASN detail (16-09-2025 update) chưa đọc — cần đọc thêm phần này trong raw source | — | Open |
| Q-002 | R9 | "Lưu theo máy local" — mechanism là gì? localStorage, cookie, hay server-side per user? | Dev | Open |
| Q-003 | R8 | SPKPH là viết tắt của gì? Chưa có trong bảng thuật ngữ (bảng trống trong doc) | BA | Open |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:----------------------|
| CHG-001~009 | receiving_po_asn | — | Add (mới) | — | Q-002, Q-003 |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R1–R9 | — | ❌ Blocked | Chờ Gate 1 |
| R10 | — | ❌ Blocked | Chưa đọc đủ — Blocked Coverage |

## 📅 Changelog
| Thời gian | Version | Nội dung | Nguồn |
|:----------|:--------|:---------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo | Raw ingest |
