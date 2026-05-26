---
aliases: [Receiving PO App, Nhận hàng PO App]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: receiving_po_app
project: project_hasaki
source_version: "07062 ver2.17"
partial_read: true
partial_read_note: "Đã đọc section 'Receiving PO (App)' đến đầu Case 1 (trang 32–41). Chưa đọc đủ: Case 1 chi tiết (trang 41–61), Thêm hoá đơn (62–67), Case 2 PO Gift (68–73), Nhận hàng vải Group UID (74–78), Nhận hàng SKU không barcode (80–83), Update 17-05-2026 PO sample & PO chính (118). Cần đọc tiếp raw source."
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Nhận hàng PO (App) — Luồng chính

## Tổng quan
- **Mã tính năng:** receiving_po_app
- **Feature:** Receiving PO (App)
- **Mô tả ngắn:** Luồng nhận hàng PO trên App WMS — scan PO, scan sản phẩm, khai báo thiếu hàng/SPKPH, xác nhận nhận hàng. Gồm Case 1 (PO thường) và Case 2 (PO Gift). Spec hiện tại là STUB — chưa đọc đủ toàn bộ section.
- **Source chính:** `07062_Receiving_PO_Docs_ver2.17.md` – section "Receiving PO (App)" từ trang 32
- **Đối tượng sử dụng (Actors):** Warehouse staff (App user)
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ➡️ [[receiving_po_asn]] — App scan PO tạo ASN
  - ➡️ [[receiving_po_vas]] — ASN complete sinh VAS
  - ➡️ [[receiving_po_confirm_paste_id]] — Sau nhận hàng xác nhận dán ID

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07062_Receiving_PO_Docs_ver2.17.md | ver2.17 | ✅ Hiện hành |
| 2 | Link | Figma: https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO_Update | — | ❓ Chưa đọc được |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Không có API explicit | N/A |

## Phân rã Requirement

> ⚠️ **STUB — partial_read: true.** Chỉ ghi requirement từ phần đã đọc (trang 32–41). Các section chưa đọc sẽ được bổ sung sau khi đọc đủ raw source.

### Bước đầu – Scan PO
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-APP-01 | User login app → vào tính năng "Receiving PO" | Functional | High | ✅ | 07062#836-838 |
| R-APP-02 | Màn hình scan PO hiển thị hướng dẫn mặc định khi user mới vào | Functional | Low | ✅ | 07062#841-843 |
| R-APP-03 | User scan PO cần nhận hàng; validation: nếu PO không yêu cầu VAT thì bỏ qua bước check | Functional | High | ✅ | 07062#846-848 |

### Sections chưa đọc — Blocked Coverage
| Section chưa đọc | Trang raw source | Ghi chú |
|:-----------------|:-----------------|:--------|
| Case 1: Chỉ nhận riêng PO thường (chi tiết luồng scan sản phẩm, khai báo thiếu, xác nhận) | 07062 trang 41–61 | partial_read |
| Thêm hoá đơn cho PO | 07062 trang 62–67 | partial_read |
| Case 2: Nhận PO Gift chung với PO thường | 07062 trang 68–73 | partial_read |
| Nhận hàng SKU không barcode (update 22-05-2025) | 07062 trang 80–83 | partial_read |
| Update 17-05-2026: PO sample & PO chính | 07062 trang 118 | partial_read |
| Update 17-05-2026: Cho nhiều user cùng nhận cùng lúc | 07062 trang 119 | partial_read |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

> Chỉ mô tả bước đầu đã đọc. Phần còn lại chờ đọc thêm.

### Điều kiện tiên quyết (Pre-conditions)
- User đã login App WMS.
- PO đã được tạo và approved trên Inside.

### Luồng chuẩn (Happy Path) — stub
1. User vào tính năng "Receiving PO" trên App.
2. Hệ thống hiển thị hướng dẫn.
3. User scan mã PO.
4. *(Phần tiếp theo chưa đọc đủ — xem Blocked Coverage)*

### Luồng rẽ nhánh (Alternative Paths)
- *(Chưa đủ dữ liệu — blocked)*

### Luồng ngoại lệ (Exception Paths)
- *(Chưa đủ dữ liệu — blocked)*

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
> Chưa đủ dữ liệu — cần đọc thêm raw source.

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
> Chưa đủ dữ liệu — cần đọc thêm raw source.

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)
> Chưa đủ dữ liệu — blocked.

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-APP-01 | R-APP-03 | "PO không yêu cầu VAT thì bỏ qua bước check" — bước check là bước nào trong luồng? | BA | Open | | | |
| Q-APP-02 | (chung) | PO sample & PO chính (Update 17-05-2026): điều kiện cụ thể và luồng xử lý là gì? | BA | Open | | | |

## 📝 Thay đổi so với version cũ
> Chưa đủ dữ liệu để lập bảng đầy đủ.

## 🔎 Impact Analysis & Regression Proposal
| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:-----|
| Update 17-05-2026 | receiving_po_app | — | Blocked | PO sample flow | Chờ đọc đủ source |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-APP-01~03 | | ❌ Blocked | partial_read — cần đọc đủ raw source trước |
| Case 1 (trang 41-61) | | ❌ Blocked | Chưa đọc |
| Case 2 (trang 68-73) | | ❌ Blocked | Chưa đọc |
| Update 17-05-2026 | | ❌ Blocked | Chưa đọc |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Tạo STUB — partial_read. Đọc được trang 32–41 của 07062 ver2.17 | 07062#834-848 |
