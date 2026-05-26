---
aliases: [Confirm Paste ID, Xác nhận dán ID App]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: receiving_po_confirm_paste_id
project: project_hasaki
source_version: "07062 ver2.17"
partial_read: true
partial_read_note: "Chưa đọc section 'Confirm paste ID (App)' từ trang 84–95. Cần đọc thêm raw source."
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Confirm Paste ID (App) — Xác nhận dán ID trên App

## Tổng quan
- **Mã tính năng:** receiving_po_confirm_paste_id
- **Feature:** Confirm Paste ID (App)
- **Mô tả ngắn:** Luồng xác nhận dán ID (Serial/IMEI/RFID/Label) cho sản phẩm vật lý trên App WMS, sau khi hoàn thành nhận hàng PO. **Spec này là STUB — chưa đọc đủ section từ trang 84.**
- **Source chính:** `07062_Receiving_PO_Docs_ver2.17.md` – section "Confirm paste ID (App)" trang 84–95
- **Đối tượng sử dụng (Actors):** Warehouse staff (App user)
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[receiving_po_app]] — Sau khi nhận hàng PO xong
  - ⬅️ [[receiving_po_vas]] — VAS Web quản lý kết quả dán ID

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07062_Receiving_PO_Docs_ver2.17.md | ver2.17 | ✅ Hiện hành |

## Phân rã Requirement
> ⚠️ **STUB — partial_read: true.** Chưa đọc section này. Toàn bộ requirement bị Blocked.

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| Tất cả | | ❌ Blocked | partial_read — chưa đọc trang 84–95 của raw source |

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:--------------|:--------|:-------|:-----------|
| Q-PID-01 | (chung) | Toàn bộ nội dung section Confirm paste ID (App) chưa được đọc — cần đọc trang 84–95 | BA | Open |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Tạo STUB — partial_read. Chưa đọc trang 84–95 | 07062 TOC#163 |
