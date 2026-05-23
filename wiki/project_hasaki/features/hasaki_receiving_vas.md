---
aliases: [VAS Hasaki, Xác nhận dán ID, hasaki-receiving-vas]
tags: [qa/requirement, qa/feature-group/receiving-po]
status: Draft
created: 2026-05-23
updated: 2026-05-23
feature: hasaki_receiving_vas
project: project_hasaki
source_version: v2.17
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: VAS — Xác nhận dán ID (Web + App)

## Tổng quan
- **Mã tính năng:** hasaki_receiving_vas
- **Feature:** Quản lý VAS (Value Added Service) — xác nhận dán ID Serial/IMEI/QRCode/RFID cho sản phẩm sau khi nhận hàng PO
- **Mô tả ngắn:** Quản lý danh sách VAS trên Web (filter/listing/detail/cập nhật QRCode & Serial), xác nhận dán ID trên App (scan PO → chọn phiên VAS → chụp hình → update Serial/IMEI/QRCode/RFID), tạo VAS thủ công, và update trạng thái VAS theo Quality Control. Bao gồm VAS cho CCDC, TSCĐ, SKU RFID từ vendor ngoài.
- **Source chính:** `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.pdf` — v2.17
- **Đối tượng sử dụng (Actors):** Nhân viên kho (app), Quản lý kho (web)
- **Test Suite tương ứng:** [[wiki/project_hasaki/test_suites/test_hasaki_receiving_vas|test_hasaki_receiving_vas]]
- **Mối quan hệ:**
  - ⬅️ [[wiki/project_hasaki/features/hasaki_receiving_po_app|#2 App PO Receiving]] — VAS được tự sinh sau khi kết thúc phiên nhận hàng PO
  - ➡️ [[wiki/project_hasaki/features/hasaki_qc_evaluation|#6 QC Evaluation]] — VAS type Quality Control kích hoạt luồng đánh giá chất lượng; trạng thái VAS thay đổi theo kết quả QC (Chờ duyệt → Nhận hàng/Trả NCC)
  - ℹ️ [[wiki/project_hasaki/features/hasaki_qc_setup|#5 QC Setup]] — QC Setup cập nhật VAS type mới (IMEI/RFID/Quality Control/Other) và bổ sung trạng thái VAS mới

---

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | PDF | `07062_Receiving_PO_Docs_ver2.17.pdf` | v2.17 | ✅ Hiện hành |
| 2 | PDF | `07105_Quality_Control_Docs_ver1.5.pdf` | v1.5 | ✅ Hiện hành |
| 3 | Figma | Figma Receiving PO (VAS section) | — | ✅ Hiện hành |

---

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | VAS tự động sinh khi ASN chuyển Received: CCDC/TSCĐ có Serial/RFID → VAS status Open; SKU Sức khoẻ-Làm đẹp có serial → VAS auto Completed | Functional | High | ✅ | PDF v2.17, mục VAS logic |
| R2 | VAS filter trên Web: VAS number, Inbound shipment, Inbound source, Outbound order, Outbound source, Type, Warehouse, SKU/Barcode, Owner, Status (Open/In-Progress/Completed/Canceled), From-To date | Functional | High | ✅ | PDF v2.17, mục VAS Filter |
| R3 | VAS Listing Web: các cột TT, VAS number, Warehouse, Type, ASN, Inbound shipment, Inbound source, Outbound order, Outbound source, Location, Created by, Implemented by, Updated date, Status, Action | Functional | High | ✅ | PDF v2.17, mục VAS Listing |
| R4 | VAS Listing Action: Button cập nhật Serial/IMEI/Label (chỉ show khi Open/In-Progress); Button xem chi tiết | Functional | Medium | ✅ | PDF v2.17 |
| R5 | VAS sinh tách: nếu 1 SKU nhận vào 2 location khác nhau trong cùng phiên → sinh 2 VAS riêng | Functional | Medium | ✅ | PDF v2.17 |
| R6 | VAS status đặc biệt từ QC: "Chờ duyệt / Waiting for approval" khi QC failed; "Chờ dán ID / Waiting for paste ID" khi passed và có IMEI/RFID | Functional | High | ✅ | PDF v1.5, mục VAS updated |
| R7 | VAS Detail Web — thông tin chung: Warehouse, Type, ASN, Inbound shipment/source, Outbound order/source, Location, Created/Updated; Danh sách sản phẩm chỉ hiện SKU required serial; các cột: SKU, Barcode, Product name, Qty received, Qty pasted, Image/Video, Action | Functional | High | ✅ | PDF v2.17, mục VAS Detail |
| R8 | VAS Detail Web — Group UID (update 16-09-2025): VAS Quality control với SKU vải lấy 10% Group UID để đánh giá (làm tròn lên); hiện Group UID và kết quả đánh giá | Functional | Medium | ✅ | PDF v2.17 |
| R9 | Cập nhật thông tin Serial/IMEI/QRCode trên Web: auto select thông tin cần update theo config SKU; CCDC → bật QRCode (hiện Serial luôn tắt phía BE); nếu có QRCode và valid thì tự focus sang ô Serial; hỗ trợ search gần đúng 3 ký tự | Functional | High | ✅ | PDF v2.17 |
| R10 | Validation cập nhật Serial/QRCode Web: Serial ≥16 ký tự; Serial không trùng trong danh sách; Serial không trùng hệ thống; QRCode không trùng danh sách; QRCode không trùng hệ thống; QRCode không tồn tại hệ thống HR | Functional | High | ✅ | PDF v2.17, mục Validation |
| R11 | Button Complete VAS: chỉ hiện khi Qty pasted = Qty received của tất cả SKU trong VAS; xác nhận "Do you want to confirm pasting ID completion?" → VAS = Completed, UID chuyển Received → In-Bin | Functional | High | ✅ | PDF v2.17 |
| R12 | App — Confirm Paste ID: scan mã PO; validate PO đã nhận hàng, thuộc kho, chưa hoàn thành dán; chọn phiên VAS cần dán | Functional | High | ✅ | PDF v2.17, mục Confirm paste ID |
| R13 | App — Danh sách phiên VAS: phân biệt màu (xám=Open, xanh dương=In-Progress, cam=chờ đánh giá QC); chỉ cho chọn VAS của user đó hoặc VAS Open; hỗ trợ nhiều user cùng dán | Functional | High | ✅ | PDF v2.17 |
| R14 | App — Chụp hình/video sản phẩm (áp dụng cho SKU required Serial và không thuộc Sức khoẻ Làm đẹp/Thuốc): max 5 hình, 1 video ≤15s; SKU không quản lý IMEI → sau chụp hình là Completed VAS | Functional | High | ✅ | PDF v2.17, Bước 3 |
| R15 | App — Cập nhật QRCode/Serial/IMEI: nếu 1 thông tin → auto add khi scan; nếu 2 thông tin → sau QRCode hợp lệ tự focus sang Serial; nếu chưa đủ SL → hiện xác nhận; IMEI có thể để trống | Functional | High | ✅ | PDF v2.17, Bước 4 |
| R16 | App — Scan RFID (vendor ngoài): scan từng barcode RFID hoặc hàng loạt; RFID phải chưa tồn tại hệ thống; nếu SL scan > SL cần khai báo → cảnh báo xoá bớt | Functional | High | ✅ | PDF v2.17, mục RFID vendor |
| R17 | App — VAS RFID nội bộ (Thời trang–Synctives): option scan nhiều SKU cùng lúc hoặc từng SKU; RFID đã define → Tab Hợp lệ / Không hợp lệ; RFID mới → chỉ Tab Hợp lệ | Functional | High | ✅ | PDF v2.17, Bước 4.1 |
| R18 | App — Xác nhận Hoàn thành: nếu chưa đủ SL → VAS giữ In-Progress, chỉ update QRCode/Serial; nếu đủ SL → VAS = Completed | Functional | High | ✅ | PDF v2.17, Bước 5 |
| R19 | Web — Tạo VAS thủ công (Manual): chọn kho, loại VAS (RFID/Serial), mã phiếu nhập nguồn (không bắt buộc); thêm SKU có config tương ứng + số lượng ≤ tồn kho In-Bin/Picklisted; xác nhận tạo → chuyển ngay vào bước khai báo | Functional | Medium | ✅ | PDF v2.17, mục Tạo thủ công VAS |
| R20 | Web — VAS Manual cho phép update lại Qty received (khi Open/In-Progress) do số lượng vật lý có thể không khớp | Functional | Low | ✅ | PDF v2.17, update 01-12-2025 |
| R21 | VAS Type "Manual" trong listing để phân biệt với VAS tự động | Functional | Low | ✅ | PDF v2.17 |

---

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- ASN đã có status = Received (hoặc Receiving) với SKU yêu cầu dán ID.
- VAS đã được sinh tự động sau khi ASN Received (hoặc tạo thủ công).

---

### Luồng chuẩn (Happy Path) — App Confirm Paste ID (SKU CCDC QRCode)

1. User vào **Purchase Order / Confirm Paste ID**, scan mã PO hợp lệ.
2. Danh sách phiên VAS hiển thị; user chọn phiên VAS status Open/In-Progress.
3. Hệ thống update VAS = In-Progress.
4. User thấy danh sách SKU cần dán; chọn SKU cần cập nhật.
5. Màn hình scan QRCode; user scan QRCode hợp lệ → tự động add vào danh sách.
6. Sau khi đủ số lượng, user nhấn **Lưu** → button "Complete" xuất hiện.
7. User nhấn **Complete** → xác nhận → VAS = Completed, UID chuyển In-Bin.

---

### Luồng rẽ nhánh (Alternative Paths)

- **Alt-Flow 1 — SKU yêu cầu chụp hình (required Serial, không phải Sức khoẻ Làm đẹp):** Bước 3 thêm màn hình chụp max 5 hình + 1 video 15s trước khi update QRCode.
- **Alt-Flow 2 — VAS RFID (vendor ngoài):** User scan từng barcode RFID chưa tồn tại hệ thống; tất cả hợp lệ → nhấn Lưu → Hoàn thành.
- **Alt-Flow 3 — VAS RFID nội bộ (Thời trang Synctives):** Scan hàng loạt RFID đã define; Tab Hợp lệ / Không hợp lệ; xác nhận từng SKU.
- **Alt-Flow 4 — Tạo VAS thủ công Web:** Chọn kho + loại VAS + thêm SKU → Tạo mới → chuyển ngay vào bước khai báo trên web.
- **Alt-Flow 5 — VAS Chờ duyệt (sau QC failed):** Quản lý vào web, chọn "Nhận hàng" để override pass, hoặc "Trả NCC" → VAS = Chờ NCC đến lấy.

---

### Luồng ngoại lệ (Exception Paths)

- **Exc-Flow 1 — PO chưa nhận hàng:** "PO [X] chưa được nhận hàng."
- **Exc-Flow 2 — PO đã hoàn thành dán:** "PO [X] đã hoàn thành việc dán ID cho sản phẩm."
- **Exc-Flow 3 — Serial đã tồn tại trong danh sách:** "Serial [X] đã tồn tại trong danh sách."
- **Exc-Flow 4 — Serial đã tồn tại hệ thống:** "Serial [X] đã tồn tại trên hệ thống."
- **Exc-Flow 5 — Serial < 16 ký tự:** "Serial [X] không hợp lệ (phải từ 16 ký tự)."
- **Exc-Flow 6 — QRCode không tồn tại hệ thống HR:** "QRCode [X] không tồn tại trên hệ thống HR."
- **Exc-Flow 7 — VAS đang In-Progress của user khác:** User thấy nhưng không chọn được (disabled).
- **Exc-Flow 8 — SL khai báo VAS manual > tồn kho:** "Số lượng cần khai báo ([X]) không được lớn hơn số lượng tồn kho trên hệ thống ([Y])."
- **Exc-Flow 9 — RFID scan > SL cần khai báo:** Hiện cảnh báo yêu cầu xoá bớt RFID dư.

---

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu

| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| Serial | String ≥16 ký tự | Theo config SKU | Không trùng danh sách, không trùng hệ thống |
| QRCode | Object (hệ thống tự cắt lấy trường "Code") | Theo config SKU | Không trùng danh sách, không trùng hệ thống, phải tồn tại hệ thống HR |
| IMEI | String | Theo config SKU | Không bắt buộc nhập (từ 22-05-2025); nếu nhập thì lưu |
| Serial auto-gen | [1023][YYMMDD][6 số tăng dần] | — | Tự sinh khi không có thông tin Serial |
| Video | 1 video | Theo category | Giới hạn 15 giây |
| Hình ảnh | Max 5 hình/tiêu chí | Theo category | — |
| Khổ giấy in biên bản ASN | A5 / In Bill | — | Lưu theo máy local |

---

## 🚨 Đặc Tả Thông Điệp Báo Lỗi

| Ngữ cảnh | Thông báo (VN) | Thông báo (EN) |
|:---------|:--------------|:---------------|
| PO chưa nhận | PO [X] chưa được nhận hàng | PO [X] has not received yet |
| PO đã hoàn thành dán | PO [X] đã hoàn thành việc dán ID cho sản phẩm | PO [X] has completed pasting ID for the products |
| PO không thuộc kho | PO [X] không thuộc kho đang xử lý | PO [X] is not in the warehouse being processed |
| Serial trùng danh sách | Serial [X] đã tồn tại trong danh sách | Serial [X] already exists in the list |
| Serial trùng hệ thống | Serial [X] đã tồn tại trên hệ thống | Serial [X] already exists on the system |
| Serial < 16 ký tự | Serial [X] không hợp lệ (phải từ 16 ký tự) | Serial [X] is invalid (must be 16 characters or more) |
| QRCode trùng hệ thống | QRCode [X] đã tồn tại trên hệ thống | QRCode [X] already exists on the system |
| QRCode trùng danh sách | QRCode [X] đã tồn tại trong danh sách | QRCode [X] already exists in the list |
| QRCode không có trên HR | QRCode [X] không tồn tại trên hệ thống HR | QRCode [X] does not exist on the HR system |
| Confirm paste completion | — | Do you want to confirm pasting ID completion? |
| SL khai báo > tồn kho | Số lượng cần khai báo ([X]) không được lớn hơn số lượng tồn kho trên hệ thống ([Y]) | — |
| VAS QC — chưa đánh giá | — | (Hiện thông báo không cho vào dán) |

---

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01: VAS tự động sinh cho CCDC sau ASN Received**
  - **Given:** ASN chuyển Received cho SKU CCDC có config serial
  - **When:** Hệ thống xử lý
  - **Then:** 1 VAS được sinh với status Open

- **AC-02: VAS auto Completed cho SKU Sức khoẻ Làm đẹp**
  - **Given:** ASN chuyển Received cho SKU Sức khoẻ Làm đẹp có serial
  - **When:** Hệ thống xử lý
  - **Then:** VAS tự động sinh và auto Completed ngay

- **AC-03: VAS tách khi 1 SKU nhận 2 location**
  - **Given:** 1 phiên nhận hàng, SKU A nhận vào Location 1 và Location 2
  - **When:** ASN Received
  - **Then:** Sinh 2 VAS riêng theo từng location

- **AC-04: Serial < 16 ký tự bị từ chối**
  - **Given:** User scan/nhập Serial 10 ký tự
  - **When:** Validate
  - **Then:** Thông báo "Serial [X] không hợp lệ (phải từ 16 ký tự)"

- **AC-05: VAS Completed sau đủ SL pasted**
  - **Given:** VAS có 5 SKU cần dán, user đã update đủ QRCode cho cả 5
  - **When:** User nhấn Complete và xác nhận
  - **Then:** VAS = Completed; tất cả UID liên quan chuyển từ Received → In-Bin

- **AC-06: User khác không chọn được VAS In-Progress**
  - **Given:** VAS đang In-Progress do User A thao tác
  - **When:** User B vào màn hình danh sách phiên
  - **Then:** VAS đó hiển thị nhưng disabled, User B không thể chọn

- **AC-07: Tạo VAS manual với SL vượt tồn kho**
  - **Given:** SKU A tồn kho 100, user nhập SL cần khai báo 150
  - **When:** Submit
  - **Then:** Thông báo "Số lượng cần khai báo (150) không được lớn hơn số lượng tồn kho (100)"

- **AC-08: RFID vendor ngoài — RFID đã tồn tại hệ thống**
  - **Given:** User scan RFID đã tồn tại trên hệ thống
  - **When:** Hệ thống validate
  - **Then:** RFID đó vào Tab Không hợp lệ

---

## ❓ Câu hỏi chưa rõ

- [ ] ❓ **R14 — Category áp dụng chụp hình:** Spec ghi "không bao gồm Sức khoẻ Làm đẹp, Thuốc, Thuốc (GPP)". Danh sách đầy đủ các category được miễn chụp hình là gì? (Spec ghi "có thể bổ sung thêm")
- [ ] ❓ **R6 — VAS Chờ dán ID vs Chờ đánh giá:** Thứ tự trạng thái khi vừa có QC vừa có RFID/IMEI là gì? QC trước hay dán ID trước?
- [ ] ❓ **R20 — VAS Manual update Qty received:** Chỉ Web hay App cũng cho update? Có cần approval không?
- [ ] ❓ **R8 — 10% Group UID làm tròn lên:** Nếu VAS sinh ra số lẻ (ví dụ 2.5 → 3), khi user đánh giá chỉ 2 group thì có cho Completed không?
- [ ] ❓ **R1 — VAS sinh cho TSCĐ:** TSCĐ (Tài sản cố định) khi ASN Received → VAS Open. Spec ghi cả TSCĐ, CCDC, CCDC PB — vậy điều kiện là "có quản lý Serial/IMEI/Label code" đúng không?
- [ ] ❓ **R10 — Boundary Serial 16 ký tự:** Spec có nêu lỗi khi Serial < 16 ký tự, nhưng chưa nêu rõ trường hợp Serial đúng 16 ký tự có luôn được chấp nhận không. Cần xác nhận expected result chính thức.

---

## 📝 Thay đổi so với version cũ

| # | Nội dung thay đổi | Version cũ | Version mới | Ảnh hưởng TC |
|:--|:------------------|:----------|:-----------|:-------------|
| 1 | Tách VAS theo location (1 SKU 2 location → 2 VAS) | v2.3 | v2.17 | TC tách VAS |
| 2 | IMEI không bắt buộc (chỉ lưu nếu nhập) | v2.8 | v2.17 | TC update IMEI |
| 3 | VAS Manual (RFID + Serial) | v2.12 | v2.17 | TC mới |
| 4 | VAS Group UID (QC 10% vải) | v2.11 | v2.17 | TC mới |

---

## Test Coverage
| Requirement | Test Case(s) | Status |
|:-----------|:------------|:-------|
| R1–R21 | _(chờ thiết kế)_ | ⏳ |

---

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 21:49:34 | v1.1 | Bổ sung câu hỏi boundary Serial 16 ký tự sau khi loại test case suy diễn khỏi Test Suite | [[wiki/project_hasaki/test_suites/test_hasaki_receiving_vas\|test_hasaki_receiving_vas]] |
| 2026-05-23 00:00:00 | v1.0 | Khởi tạo Feature Spec từ PDF v2.17 + v1.5 — VAS Web & App | `07062_Receiving_PO_Docs_ver2.17.pdf`, `07105_Quality_Control_Docs_ver1.5.pdf` |
