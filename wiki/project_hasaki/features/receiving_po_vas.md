---
aliases: [VAS, Value Added Service, Xác nhận dán ID Web]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: receiving_po_vas
project: project_hasaki
source_version: "07062 ver2.17"
partial_read: false
partial_read_note: ""
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: VAS – Quản lý Value Added Service trên Web

## Tổng quan
- **Mã tính năng:** receiving_po_vas
- **Feature:** VAS Management (Web)
- **Mô tả ngắn:** Màn hình quản lý danh sách và chi tiết VAS trên Web WMS — logic sinh VAS từ ASN, quản lý Serial/IMEI/Label code, QR code, và tích hợp Group UID cho SKU vải.
- **Source chính:** `07062_Receiving_PO_Docs_ver2.17.md` – section "VAS – Updated", "VAS detail – Updated", "Cập nhật thông tin Serial/Imei/Label code cho SKU", "16-09-2025: update rules VAS"
- **Đối tượng sử dụng (Actors):** Warehouse staff, Warehouse manager
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[receiving_po_asn]] — ASN received sinh ra VAS
  - ➡️ [[receiving_po_confirm_paste_id]] — App confirm paste ID liên kết với VAS
  - ➡️ [[receiving_po_vas_manual]] — Tạo VAS thủ công
  - ⬅️ [[quality_control_assessment_result]] — VAS Quality control liên kết kết quả đánh giá

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07062_Receiving_PO_Docs_ver2.17.md | ver2.17 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Không có API explicit | N/A |

## Phân rã Requirement

### Logic sinh VAS từ ASN
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-VAS-01 | SKU có category "Sức khoẻ - Làm đẹp" có quản lý serial/imei: khi ASN → Received thì hệ thống tự sinh VAS và auto Completed | Functional | High | ✅ | 07062#530-532 |
| R-VAS-02 | SKU có category TSCĐ, CCDC, CCDC PB có quản lý Serial/Imei/Label code: khi ASN → Received thì sinh VAS với status = Open | Functional | High | ✅ | 07062#533-536 |
| R-VAS-03 | Các UID của TSCĐ/CCDC/CCDC PB sau khi received: status = Received (chưa auto chuyển In-Bin); không được lấy pick cho order/receipt/IT | Functional | High | ✅ | 07062#537-540 |
| R-VAS-04 | Sau khi user xác nhận chụp hình hoặc dán ID cho từng UID (tuỳ category): status chuyển từ Received → In-Bin | Functional | High | ✅ | 07062#541-543 |
| R-VAS-05 | SKU nhận theo Group UID (10% để đánh giá): sinh VAS type Quality control; số lượng VAS = làm tròn lên của 10% group UID | Functional | High | ✅ | 07062#738-744 |

### Filter – VAS Listing
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-VAS-06 | Filter Mã VAS, Mã phiếu nhập, Phiếu nhập nguồn mapping, Mã phiếu xuất, Phiếu xuất nguồn mapping | Functional | Medium | ✅ | 07062#549-558 |
| R-VAS-07 | Filter Loại, Kho, SKU/Barcode, Người sở hữu | Functional | Medium | ✅ | 07062#559-563 |
| R-VAS-08 | Filter Trạng thái — mặc định Null; giá trị: Mới/Open, Đang xử lý/In-Progress, Hoàn thành/Completed, Đã huỷ/Canceled; hỗ trợ chọn nhiều | Functional | High | ✅ | 07062#564-575 |

### Listing – VAS
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-VAS-09 | Listing gồm: TT, Mã VAS, Kho, Loại, Mã ASN (hyperlink → ASN detail), Mã phiếu nhập (hyperlink → Inbound detail), Phiếu nhập nguồn (hyperlink → PO detail Inside), Mã phiếu xuất, Phiếu xuất nguồn, Vị trí, Người tạo, Người thực hiện, Ngày cập nhật, Trạng thái, Thao tác | Functional | High | ✅ | 07062#580-614 |
| R-VAS-10 | Vị trí / Location — nếu cùng 1 phiên mà 1 SKU nhận vào 2 location khác nhau thì sinh ra VAS tương ứng cho từng location | Functional | High | ✅ | 07062#594-598 |
| R-VAS-11 | SKU có yêu cầu serial: không hiển thị trong VAS detail listing, chỉ hiện các SKU có yêu cầu serial | Functional | Medium | ✅ | 07062#599-601 |
| R-VAS-12 | Trạng thái VAS: Open (khi ASN received), In-Progress (có ít nhất 1 SKU có SL đã dán > 0), Completed, Canceled | Functional | High | ✅ | 07062#607-614 |
| R-VAS-13 | Action button cập nhật Serial/Imei/Label — chỉ show cho VAS status Open hoặc In-Progress | Functional | High | ✅ | 07062#617-620 |

### Chi tiết VAS (VAS Detail)
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-VAS-14 | Thông tin chung dạng text: Kho, Loại, ASN, Mã phiếu nhập, Phiếu nhập nguồn, Mã phiếu xuất, Phiếu xuất nguồn, Vị trí, Ngày tạo, Người tạo, Ngày cập nhật | Functional | Medium | ✅ | 07062#630-652 |
| R-VAS-15 | Danh sách sản phẩm chỉ hiện các SKU có quản lý serial; cột: SKU, Barcode, Tên sản phẩm, SL thực nhận, SL đã dán, Hình ảnh/Video, Thao tác | Functional | High | ✅ | 07062#654-672 |

### Cập nhật Serial/Imei/QRCode
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-VAS-16 | Hệ thống auto chọn thông tin cần cập nhật cho SKU: nếu wms_product.wms_config&131072>0 → required QRCode; nếu wms_product.config&8>0 → required Serial/Imei | Functional | High | ✅ | 07062#677-681 |
| R-VAS-17 | Update 25-02-2025: luôn tắt option Serial dưới BE; user chỉ cần cập nhật QRCode; Serial nếu không có thì hệ thống tự gen theo rules [1023][YYMMDD][6 số tăng dần] | Functional | High | ✅ | 07062#683-690 |
| R-VAS-18 | QRCode khi scan: hệ thống cắt chuỗi để lấy trường "Code" trong object | Functional | High | ✅ | 07062#692-694 |
| R-VAS-19 | Nếu chỉ cập nhật 1 thông tin: scan → tự add; nhập tay → nhấn dấu + để add | Functional | Medium | ✅ | 07062#700-701 |
| R-VAS-20 | Nếu chọn cả QRCode và Serial/Imei: scan QRCode hợp lệ → tự chuyển focus sang ô Serial/Imei | Functional | Medium | ✅ | 07062#703 |
| R-VAS-21 | Validation Serial: đã tồn tại trong danh sách / trên hệ thống / không hợp lệ (phải ≥16 ký tự); Validation QRCode: đã tồn tại trong danh sách / trên hệ thống / không tồn tại trên HR | Functional | High | ✅ | 07062#704-716 |
| R-VAS-22 | Hỗ trợ search gần đúng (từ 3 ký tự) cho QRCode và Serial đã scan vào danh sách | Functional | Low | ✅ | 07062#722 |
| R-VAS-23 | Sau khi SL xác nhận dán = SL thực nhận của tất cả SKU trong VAS → button "Complete" xuất hiện; confirm: "Do you want to confirm pasting ID completion?" | Functional | High | ✅ | 07062#729-731 |
| R-VAS-24 | Group UID trong VAS Quality control (16-09-2025): hiển thị Group UID và kết quả đánh giá; chỉ cần 1 kết quả Failed → ghi nhận Failed | Functional | High | ✅ | 07062#736-747 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- ASN đã chuyển status Received.
- SKU có cấu hình quản lý Serial/Imei/QRCode hoặc Group UID.

### Luồng chuẩn (Happy Path) – Cập nhật QRCode
1. ASN Received → hệ thống sinh VAS (TSCĐ/CCDC category) với status Open.
2. User vào Menu: Inbound / VAS.
3. User chọn VAS cần xử lý.
4. User scan QRCode cho từng UID.
5. Sau khi SL dán = SL thực nhận → button Complete xuất hiện.
6. User chọn Complete → VAS Completed → UID chuyển In-Bin.

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 – Sức khoẻ Làm đẹp:** ASN Received → VAS tự sinh và auto Completed.
- **Alt-Flow 2 – 2 location:** 1 SKU nhận vào 2 location → sinh 2 VAS riêng.
- **Alt-Flow 3 – Quality control:** SKU vải nhận theo Group UID → sinh VAS QC với 10% group UID (làm tròn lên).

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1:** Serial < 16 ký tự → thông báo lỗi validation.
- **Exc-Flow 2:** QRCode không tồn tại trên hệ thống HR → thông báo lỗi.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| Serial | Text | Có (nếu category yêu cầu) | ≥16 ký tự; unique trong danh sách và trên hệ thống |
| QRCode | Text (Object "Code") | Có (nếu config) | Unique trong danh sách; phải tồn tại trên HR |
| Serial auto-gen | Text | Auto | Format: [1023][YYMMDD][6 số tăng dần] |
| VAS QC count | Số | Auto | = ROUNDUP(group_uid_count × 10%) |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
| Tình huống | VN | EN |
|:-----------|:---|:---|
| Serial đã tồn tại trong danh sách | Serial [X] đã tồn tại trong danh sách. | Serial [X] already exists in the list. |
| Serial đã tồn tại trên hệ thống | Serial [X] đã tồn tại trên hệ thống. | Serial [X] already exists on the system. |
| Serial không hợp lệ (<16 ký tự) | Serial [X] không hợp lệ (phải từ 16 ký tự) | Serial [X] is invalid (must be 16 characters or more) |
| QRCode đã tồn tại trên hệ thống | QRCode [X] đã tồn tại trên hệ thống. | QRCode [X] already exists on the system. |
| QRCode đã tồn tại trong danh sách | QRCode [X] đã tồn tại trong danh sách. | QRCode [X] already exists in the list. |
| QRCode không tồn tại trên HR | QRCode [X] không tồn tại trên hệ thống HR. | QRCode [X] does not exist on the HR system. |
| Complete pasting ID | — | Do you want to confirm pasting ID completion? |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-VAS-01: Auto sinh VAS cho Sức khoẻ Làm đẹp**
  - **Given:** ASN có SKU category "Sức khoẻ - Làm đẹp" có quản lý serial
  - **When:** ASN chuyển status Received
  - **Then:** Hệ thống tự sinh VAS và tự Completed ngay

- **AC-VAS-02: Serial validation ≥16 ký tự**
  - **Given:** User đang scan Serial vào VAS
  - **When:** Serial nhập vào có < 16 ký tự
  - **Then:** Hiển thị lỗi "Serial [X] không hợp lệ (phải từ 16 ký tự)"

- **AC-VAS-03: Button Complete xuất hiện đúng thời điểm**
  - **Given:** VAS có 2 SKU, mỗi SKU cần dán 5 UID
  - **When:** User đã dán đủ 10 UID cho cả 2 SKU
  - **Then:** Button Complete xuất hiện

- **AC-VAS-04: UID chuyển In-Bin sau Complete**
  - **Given:** User vừa Complete VAS của SKU TSCĐ
  - **When:** VAS status = Completed
  - **Then:** Tất cả UID liên quan chuyển từ Received sang In-Bin

- **AC-VAS-05: VAS QC 10% Group UID làm tròn lên**
  - **Given:** SKUA nhận 25 group UID trong ASN
  - **When:** ASN Received, SKU là vải category
  - **Then:** Sinh ra 3 dòng VAS QC (ROUNDUP(25×10%) = 3)

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-VAS-01 | R-VAS-17 | Serial auto-gen [1023][YYMMDD][6 số tăng dần] — "1023" là prefix cố định hay dynamic? | Dev | Open | | | |
| Q-VAS-02 | R-VAS-16 | Ngoài TSCĐ/CCDC/CCDC PB — còn category nào khác trigger luồng VAS không? | BA | Open | | | |

## 📝 Thay đổi so với version cũ
| Change ID | Loại | Nội dung | Version cũ | Version mới | R/AC ảnh hưởng | Trạng thái |
|:----------|:-----|:---------|:-----------|:------------|:---------------|:-----------|
| CHG-VAS-01 | Update | Cập nhật 25-02-2025: luôn tắt Serial option; auto-gen Serial | <ver2.5 | ver2.5 | R-VAS-17 | Draft |
| CHG-VAS-02 | Add | 16-09-2025: Group UID và QC results trong VAS | <ver2.11 | ver2.11 | R-VAS-24 | Draft |

## 🔎 Impact Analysis & Regression Proposal
| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:-----|
| CHG-VAS-02 | receiving_po_vas, quality_control_assessment_result | — | Add | VAS QC flow | Blocked by Gate 1 |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-VAS-01 / AC-VAS-01 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-VAS-21 / AC-VAS-02 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-VAS-23 / AC-VAS-03 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-VAS-24 / AC-VAS-05 | | ❌ Chưa tạo | Chờ Gate 1 |
| Q-VAS-01 liên quan | | ❌ Blocked | Chờ Q-VAS-01 |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo spec từ 07062 ver2.17, section VAS | 07062#519-747 |
