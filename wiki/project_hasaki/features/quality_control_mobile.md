---
aliases: [QC Mobile, Đánh giá chất lượng App]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: quality_control_mobile
project: project_hasaki
source_version: "07105 ver1.5"
partial_read: false
partial_read_note: ""
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Đánh giá chất lượng sản phẩm (App) — Luồng bình thường

## Tổng quan
- **Mã tính năng:** quality_control_mobile
- **Feature:** Quality Control – Mobile Assessment (SKU thường)
- **Mô tả ngắn:** Luồng đánh giá chất lượng sản phẩm trên App WMS — chọn VAS, đánh giá từng SKU theo tiêu chí đã thiết lập, chụp hình, hoàn thành đánh giá. Update 20-04-2026: thêm option tạo Adjustment trả NCC khi SKU thường bị Failed.
- **Source chính:** `07105_Quality_Control_Docs_ver1.5.md` – section "Đánh giá chất lượng sản phẩm - Mobile" và "Update 20-04-2026 Đánh giá SKU phụ liệu"
- **Đối tượng sử dụng (Actors):** Warehouse staff (App)
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[quality_control_sku_setup]] — Lấy danh sách tiêu chí đã thiết lập cho SKU
  - ➡️ [[quality_control_vas_update]] — Kết quả đánh giá cập nhật VAS status
  - ➡️ [[quality_control_assessment_result]] — Kết quả được ghi vào web

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07105_Quality_Control_Docs_ver1.5.md | ver1.5 | ✅ Hiện hành |

## Phân rã Requirement

### Bước 1 – Vào tính năng Quality Control
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-MOB-01 | Menu: Purchase Order / Quality Control trên App | Functional | High | ✅ | 07105#795 |
| R-MOB-02 | Chọn kho → hiển thị các VAS có type Quality Control có trạng thái Open hoặc In-Progress | Functional | High | ✅ | 07105#796-799 |
| R-MOB-03 | Hỗ trợ tìm kiếm theo mã PO và VAS | Functional | Medium | ✅ | 07105#800 |

### Bước 2 – Chọn VAS, xem sản phẩm cần đánh giá
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-MOB-04 | Chọn VAS → hiển thị: Shop, VAS, Tổng SKU, Mã PO, Tổng sản phẩm | Functional | High | ✅ | 07105#802-811 |
| R-MOB-05 | Tìm kiếm sản phẩm theo SKU, Barcode hoặc tên (tìm gần đúng) | Functional | Medium | ✅ | 07105#809 |
| R-MOB-06 | Danh sách sản phẩm với màu phân biệt: xám nhạt (chưa đánh giá), xanh dương nhạt (đang đánh giá chưa hoàn thành), xanh lá nhạt (đã đánh giá) | Functional | High | ✅ | 07105#816-820 |

### Bước 3 – Đánh giá sản phẩm
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-MOB-07 | Màn hình đánh giá gồm: Sản phẩm (SKU – tên), PO, Số lượng, Nhà cung cấp (từ PO), Ghi chú (mặc định trống, user edit được), Tiêu chí đạt, Tiêu chí không đạt | Functional | High | ✅ | 07105#823-831 |
| R-MOB-08 | Danh sách tiêu chí cần đánh giá: lấy từ thiết lập cho SKU | Functional | High | ✅ | 07105#831-840 |
| R-MOB-09 | Thông tin từng tiêu chí: Thứ tự, Tên, Mô tả, Mô tả điều kiện, Hình chụp mẫu, Đạt/Không đạt | Functional | High | ✅ | 07105#835-840 |
| R-MOB-10 | Nhập kết quả đánh giá theo điều kiện: nhập giá trị >0 → Enter hoặc dấu tích → hệ thống so sánh với điều kiện config để xác định Đạt/Không đạt; user có thể edit lại và xác nhận lại | Functional | High | ✅ | 07105#841-853 |
| R-MOB-11 | Chụp hình: dựa theo config yêu cầu chụp hình; tiêu chí Fail → bắt buộc chụp hình VÀ nhập ghi chú; hỗ trợ tối đa 5 hình cho 1 tiêu chí | Functional | High | ✅ | 07105#854-860 |
| R-MOB-12 | Sau khi đánh giá tất cả tiêu chí → chọn "Hoàn thành" để xác nhận | Functional | High | ✅ | 07105#862-863 |

### Bước 4 – Hoàn thành VAS
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-MOB-13 | Nếu VAS có nhiều sản phẩm → cần đánh giá tất cả → "Hoàn thành đánh giá" cho toàn VAS | Functional | High | ✅ | 07105#864-869 |

### Update 20-04-2026: SKU phụ liệu (SKU thường) bị Failed
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-MOB-14 | Áp dụng cho SKU KHÔNG PHẢI category Thời trang (NVL) và không phải là Vải | Functional | High | ✅ | 07105#1246 |
| R-MOB-15 | Sau khi đánh giá xong SKU, nếu kết quả Failed (có ≥1 failed) → hiển thị màn hình xác nhận số lượng trả NCC | Functional | High | ✅ | 07105#1247-1252 |
| R-MOB-16 | Confirm message EN: "SKU [code] has evaluation criteria marked as FAILED. Do you want to create an adjustment voucher to export the failed quantity for return to vendor?" | Functional | High | ✅ | 07105#1250-1252 |
| R-MOB-17 | Option "Để sau (Later)" — tắt thông báo, về danh sách SKU cần đánh giá | Functional | Medium | ✅ | 07105#1253-1254 |
| R-MOB-18 | Option "Tạo phiếu điều chỉnh (Create adjustment)": nhập số lượng cần trả (< số lượng nhập hàng PO); Xác nhận → tạo Adjustment với các thông tin: Warehouse (kho phát sinh), Type (Export), Reason (Return to vendor), Vendor (từ source PO), Require VAT (3 option), Source code (mã PO), Required picking (No), ADJ status (Waiting for approval) | Functional | High | ✅ | 07105#1255-1284 |
| R-MOB-19 | Require VAT — 3 giá trị: No – Trả hàng không xuất hoá đơn; Yes VAT - Hasaki xuất hoá đơn bán hàng cho NCC; Yes VAT – NCC xuất hoá đơn điều chỉnh cho HASAKI | Functional | High | ✅ | 07105#1277-1280 |
| R-MOB-20 | Thông tin SKU trong Adjustment: SKU từ user request, số lượng từ user input, VAT và Price theo thông tin SKU trên Inside theo rules Adjustment hiện tại | Functional | High | ✅ | 07105#1287-1291 |

### Chụp hình tem QC (Update 11-02-2026)
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-MOB-21 | Sau khi hoàn thành tất cả tiêu chí cho SKU, khi nhấn "Hoàn thành": bắt buộc chụp 1 hình tem QC Pass/Fail trước khi confirm | Functional | High | ✅ | 07105#1143-1147 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- SKU đã có thiết lập tiêu chí được Approved.
- VAS QC đã được sinh và có status Open hoặc In-Progress.

### Luồng chuẩn (Happy Path) — SKU thường Đạt
1. User vào App → Quality Control → chọn Kho.
2. Chọn VAS cần đánh giá.
3. Chọn SKU → đánh giá từng tiêu chí (Đạt/Không đạt, nhập giá trị nếu có điều kiện).
4. Chụp hình tem QC → Hoàn thành cho SKU.
5. Đánh giá tất cả SKU trong VAS → Hoàn thành VAS.

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 – SKU thường Failed:** Sau khi Hoàn thành → popup hỏi tạo Adjustment trả NCC; user chọn "Để sau" hoặc "Tạo phiếu điều chỉnh".
- **Alt-Flow 2 – Tiêu chí Fail:** Bắt buộc chụp hình và nhập ghi chú.

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1:** Tiêu chí Fail không chụp hình → không thể hoàn thành tiêu chí.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| Hình ảnh tiêu chí Fail | Image | Có | Tối đa 5 hình / tiêu chí |
| Ghi chú tiêu chí Fail | Text | Có | — |
| Hình tem QC | Image | Có | Đúng 1 hình |
| Số lượng trả NCC | Số | Có (nếu chọn tạo Adjustment) | < số lượng nhập hàng PO |
| Require VAT | Enum | Có (trong Adjustment) | 3 giá trị |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
| Tình huống | EN |
|:-----------|:---|
| SKU thường bị Failed | SKU [code] has evaluation criteria marked as FAILED. Do you want to create an adjustment voucher to export the failed quantity for return to vendor? |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-MOB-01: Màu sắc phân biệt trạng thái sản phẩm**
  - **Given:** VAS có 3 SKU: A (chưa đánh giá), B (đang đánh giá), C (đã đánh giá xong)
  - **When:** User xem danh sách sản phẩm trong VAS
  - **Then:** A = xám nhạt, B = xanh dương nhạt, C = xanh lá nhạt

- **AC-MOB-02: Tiêu chí Fail bắt buộc chụp hình và ghi chú**
  - **Given:** User đánh giá tiêu chí và chọn kết quả = Không đạt
  - **When:** User cố gắng chuyển qua tiêu chí tiếp mà không chụp hình
  - **Then:** Hệ thống yêu cầu chụp hình và nhập ghi chú

- **AC-MOB-03: Tem QC bắt buộc sau hoàn thành tất cả tiêu chí**
  - **Given:** User đã đánh giá xong tất cả tiêu chí cho SKU
  - **When:** User nhấn "Hoàn thành"
  - **Then:** Hệ thống yêu cầu chụp 1 hình tem QC trước khi xác nhận

- **AC-MOB-04: SKU thường Failed hiển thị popup tạo Adjustment**
  - **Given:** SKU thuộc category không phải Thời trang (NVL) và không phải Vải
  - **When:** Kết quả đánh giá có ≥1 tiêu chí Failed, user hoàn thành
  - **Then:** Popup hỏi tạo Adjustment với confirm message đúng

- **AC-MOB-05: Số lượng Adjustment < số lượng PO**
  - **Given:** User chọn "Tạo phiếu điều chỉnh"
  - **When:** User nhập số lượng trả ≥ số lượng nhập hàng PO
  - **Then:** Hệ thống không cho phép xác nhận

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-MOB-01 | R-MOB-10 | "User có thể edit lại kết quả đánh giá theo điều kiện và xác nhận lại" — có giới hạn số lần edit không? | BA | Open | | | |

## 📝 Thay đổi so với version cũ
| Change ID | Loại | Nội dung | Version cũ | Version mới | R/AC ảnh hưởng | Trạng thái |
|:----------|:-----|:---------|:-----------|:------------|:---------------|:-----------|
| CHG-MOB-01 | Add | Update 11-02-2026: Bắt buộc chụp tem QC sau hoàn thành | ver1.3 | ver1.4 | R-MOB-21 | Draft |
| CHG-MOB-02 | Add | Update 20-04-2026: SKU thường Failed → tạo Adjustment trả NCC | ver1.4 | ver1.5 | R-MOB-14~20 | Draft |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-MOB-06 / AC-MOB-01 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-MOB-11 / AC-MOB-02 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-MOB-21 / AC-MOB-03 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-MOB-15 / AC-MOB-04 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-MOB-18 / AC-MOB-05 | | ❌ Chưa tạo | Chờ Gate 1 |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo spec từ 07105 ver1.5, section Mobile Assessment + Update 20-04-2026 | 07105#790-869, #1141-1148, #1242-1291 |
