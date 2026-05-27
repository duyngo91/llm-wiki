---
aliases: [Fabric UID Group, Nhận hàng vải Group UID]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: receiving_po_fabric_uid_group
project: project_hasaki
source_version: "07062 ver2.17"
partial_read: true
partial_read_note: "Đã đọc ngữ cảnh về Group UID trong section VAS (trang 27) và ASN (trang 19). Chưa đọc đủ section 'Nhận hàng Vải khai báo Group UID' (trang 74–78) và 'Nhận hàng PO cho SKU vải theo packing list' (trang 106–110), 'Update rules nhận dư PO vải 20-04-2026' (115–117). Cần đọc thêm raw source."
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Nhận hàng vải khai báo Group UID

## Tổng quan
- **Mã tính năng:** receiving_po_fabric_uid_group
- **Feature:** Receiving Fabric with Group UID
- **Mô tả ngắn:** Luồng đặc thù nhận hàng vải nguyên vật liệu (category Thời trang NVL) — khai báo Group UID khi nhận PO, tách 10% để đánh giá QC, thêm thông tin "Trừ lõi". **Spec này là STUB — chưa đọc đủ section.**
- **Source chính:** `07062_Receiving_PO_Docs_ver2.17.md` – section "Nhận hàng Vải khai báo Group UID" trang 74–78, "02-04-2026: Bổ sung thông tin Trừ lõi" trang 109–110, "Update 16-04-2026" trang 113–117
- **Đối tượng sử dụng (Actors):** Warehouse staff (App)
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ➡️ [[receiving_po_vas]] — Sinh VAS QC 10% group UID
  - ➡️ [[quality_control_fabric_mobile]] — Đánh giá vải sau khi nhận

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07062_Receiving_PO_Docs_ver2.17.md | ver2.17 | ✅ Hiện hành |

## Phân rã Requirement (ngữ cảnh đã đọc)
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-FUG-01 | SKU vải nhận trong ASN theo Group UID: lấy 10% (làm tròn lên) để đánh giá QC | Functional | High | ✅ | 07062#738-741 |
| R-FUG-02 | Ví dụ: 25 group UID × 10% = 2.5 → làm tròn lên = 3 VAS QC | Functional | High | ✅ | 07062#739-741 |
| R-FUG-03 | Chi tiết ASN bổ sung thông tin Group UID đã nhận (16-09-2025) | Functional | Medium | ✅ | 07062#512-516 |

> ⚠️ Các requirement chi tiết luồng App (trang 74–78, 109–117) chưa đọc — Blocked Coverage.

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-FUG-01~03 | | ❌ Chưa tạo | Chờ Gate 1 |
| Luồng App chi tiết (trang 74–78) | | ❌ Blocked | partial_read |
| Trừ lõi (trang 109–110) | | ❌ Blocked | partial_read |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Tạo STUB — partial_read. Ghi nhận context từ section VAS/ASN đã đọc | 07062#738-741, #512-516 |
