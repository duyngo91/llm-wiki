---
tags: [qa/requirement, qa/feature-group/receiving-po]
status: Draft
created: 2026-05-25
updated: 2026-05-25
feature: receiving_po_vas
project: project_hasaki
source_version: v2.17
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: VAS Management (Web + App)

## Tổng quan
- **Mã tính năng:** receiving_po_vas
- **Feature:** VAS (Value Added Service) — Quản lý dán tem, xác nhận UID, RFID, Serial/IMEI cho SKU khi nhận PO
- **Mô tả ngắn:** Quản lý VAS trên Web (danh sách, detail) và App (dán tem theo location, tách VAS, chụp hình/video). Tính năng phức tạp với nhiều sub-flow: VAS auto, VAS manual, Group UID, RFID.
- **Source chính:** `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.md` — mục "VAS – Updated", "VAS detail – Updated", "Cập nhật thông tin Serial/Imei/Label code", "16-09-2025: update rules VAS"
- **Đối tượng sử dụng (Actors):** Nhân viên kho (App + Web)
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** —
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[wiki/project_hasaki/features/receiving_po_app|Receiving PO App]] — App trigger VAS sau khi scan nhận
  - ⬅️ [[wiki/project_hasaki/features/quality_control_setup_sku|QC Setup SKU]] — QC sinh VAS auto sau nhận (All PO)

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted from PDF) | `07062_Receiving_PO_Docs_ver2.17.md` | v2.17 | ✅ Hiện hành (chưa đọc đầy đủ) |
| 2 | Figma | `https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO_Update` | — | ❓ Chưa đọc được |

## ⚠️ Trạng thái phân tích

> **Lưu ý:** Phần VAS trong raw source rất dài và chưa được đọc đầy đủ. Spec này là **stub** dựa trên TOC và revision history. Cần đọc thêm các mục: VAS – Updated, VAS detail – Updated, 16-09-2025, 01-12-2025 Create/Update VAS manual, 2.10–2.12 (RFID, Group UID, Serial) trước khi hoàn chỉnh spec.

## Phân rã Requirement (Đã xác định từ Revision History)

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | VAS theo location: tách VAS nếu 1 ASN, 1 SKU nhận vào 2 location khác nhau | Business Rule | High | ✅ | v2.17, rev 2.3 05-02-2025 |
| R2 | App dán VAS cũng tách theo location | Functional | High | ✅ | v2.17, rev 2.3 05-02-2025 |
| R3 | Chụp hình/quay video sản phẩm trong VAS cho một số category yêu cầu | Functional | High | ✅ | v2.17, rev 2.4 18-02-2025 |
| R4 | SKU có required IMEI: bật nhập IMEI nhưng không bắt buộc (optional) | Functional | High | ✅ | v2.17, rev 2.8 22-05-2025 |
| R5 | SKU có RFID (Category Thời trang, Brand Synctives): scan nhận RFID khi nhận PO, bỏ qua VAS auto | Business Rule | High | ✅ | v2.17, rev 2.10 28-07-2025 |
| R6 | VAS manual: user tạo thủ công VAS cho SKU có RFID và Serial (khi nhận chưa config hoặc thiếu thông tin) | Functional | High | ✅ | v2.17, rev 2.12 02-12-2025 |
| R7 | Cập nhật thông tin VAS cho SKU có required Serial/IMEI | Functional | High | ✅ | v2.17, rev 2.12 23-12-2025 |
| R8–Rx | Chi tiết VAS filter/listing/detail Web, flow App | Functional | — | ❓ | v2.17, mục VAS — chưa đọc đầy đủ |

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:--------------|:--------|:-------|:-----------|
| Q-001 | R3 | Danh sách category nào yêu cầu chụp hình/quay video? Trong doc có không? | BA | Open |
| Q-002 | R5 | Điều kiện RFID: chỉ "Category Thời trang + Brand Synctives" hay có thêm điều kiện khác? | BA | Open |
| Q-003 | R8+ | Toàn bộ phần VAS Web (filter, listing, detail) chưa đọc — cần đọc thêm raw source | — | Open |
| Q-004 | — | SPKPH là gì? (xuất hiện trong context VAS và ASN) | BA | Open |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:----------------------|
| CHG-001~007 | receiving_po_vas | — | Add (mới) | — | Q-001~004 |

## Blocked Coverage
Toàn bộ requirement R8 trở đi bị blocked do chưa đọc đầy đủ raw source. Cần đọc thêm trước khi tạo test cases.

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R1–R7 | — | ❌ Blocked | Chờ Gate 1 |
| R8+ | — | ❌ Blocked | Blocked Coverage — chưa đọc đủ source |

## 📅 Changelog
| Thời gian | Version | Nội dung | Nguồn |
|:----------|:--------|:---------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo stub — chưa đọc đầy đủ VAS section | Raw ingest |
