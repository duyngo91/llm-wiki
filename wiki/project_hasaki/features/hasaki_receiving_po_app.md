---
aliases: [Receiving PO App Hasaki, Nhận hàng PO App, hasaki-receiving-po-app]
tags: [qa/requirement, qa/feature-group/receiving-po]
status: Draft
created: 2026-05-23
updated: 2026-05-23
feature: hasaki_receiving_po_app
project: project_hasaki
source_version: v2.17
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Nhận hàng PO — Mobile App (Hasaki WMS)

## Tổng quan
- **Mã tính năng:** hasaki_receiving_po_app
- **Feature:** Nhận hàng PO trên App WMS (Purchase Order / Receiving PO)
- **Mô tả ngắn:** Luồng nhận hàng PO từ nhà cung cấp trực tiếp trên app WMS: scan PO, chọn loại nhận, scan camera/vị trí, scan sản phẩm (có HSD/serial/combo/RFID/Group UID/SKU không barcode), khai báo thiếu/SPKPH, cập nhật biên bản, thêm hoá đơn, hoàn thành PO. Bao gồm case PO thường, PO Gift, PO vải Group UID và nhiều user nhận cùng lúc.
- **Source chính:** `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.pdf` — v2.17
- **Đối tượng sử dụng (Actors):** Nhân viên kho (dùng app), Quản lý kho
- **Test Suite tương ứng:** [[wiki/project_hasaki/test_suites/test_hasaki_receiving_po_app|test_hasaki_receiving_po_app]]
- **Mối quan hệ:**
  - ⬅️ [[wiki/project_hasaki/features/hasaki_receiving_inbound_shipment|#1 Inbound Shipment]] — PO/ASN tạo từ web là đầu vào cho App nhận hàng
  - ➡️ [[wiki/project_hasaki/features/hasaki_receiving_vas|#3 VAS]] — Kết thúc phiên nhận hàng → hệ thống tự sinh VAS cho SKU có yêu cầu
  - ⬅️ [[wiki/project_hasaki/features/hasaki_receiving_packing_list|#4 Packing List]] — App gợi ý Roll code từ Packing List khi nhận SKU vải; UID group và quy đổi đơn vị theo packing list
  - ➡️ [[wiki/project_hasaki/features/hasaki_qc_evaluation|#6 QC Evaluation]] — PO Sample: nhận max 30% phiên đầu, QC phải pass trước khi nhận tiếp; PO Gốc cần check QC pass

---

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | PDF | `07062_Receiving_PO_Docs_ver2.17.pdf` | v2.17 | ✅ Hiện hành |
| 2 | Figma | Figma Receiving PO Update (URL nội bộ) | — | ✅ Hiện hành |

---

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Scan mã PO: validate PO thuộc kho, VAT verify, PO đã received; hiển thị thông tin PO + tạo ASN tương ứng | Functional | High | ✅ | PDF v2.17, Bước 2 |
| R2 | Chọn loại nhận hàng: Có đồng kiểm (bỏ qua scan camera) / Không đồng kiểm (yêu cầu scan camera nếu kho bật config Required camera) | Functional | High | ✅ | PDF v2.17, Bước 3 |
| R3 | Scan camera: validate mã camera thuộc kho; nếu shop quản lý location thì chuyển sang scan vị trí/giỏ | Functional | High | ✅ | PDF v2.17, Bước 4 |
| R4 | Scan vị trí/giỏ: validate vị trí hợp lệ; PO zone chỉ nhận vào bin Di động; PO thường không nhận vào bin Di động | Functional | High | ✅ | PDF v2.17, Bước 5 |
| R5 | Scan SKU thường: validate SKU có trong PO, số lượng không vượt SL confirm; nếu không có barcode hỗ trợ luồng SKU không barcode | Functional | High | ✅ | PDF v2.17, Case 1 Bước 1 |
| R6 | SKU có HSD: validate HSD ≥ HSD tối thiểu = [% Allowed Shelf Life] × [Shelf Life]; HSD không vượt vòng đời sản phẩm; PO tester: HSD ≥ 3 tháng | Functional | High | ✅ | PDF v2.17, mục HSD |
| R7 | SKU có HSD + số lô: validate số lô không trùng trên hệ thống | Functional | High | ✅ | PDF v2.17, mục HSD+số lô |
| R8 | SKU có Serial/IMEI (CCDC): mỗi lần scan chỉ nhận SL=1; validate serial không trùng trên hệ thống | Functional | High | ✅ | PDF v2.17, mục Serial |
| R9 | SKU có RFID (Thời trang – Synctives): scan RFID khi nhận, auto VAS; bỏ qua khai báo serial riêng | Functional | High | ✅ | PDF v2.17, mục RFID |
| R10 | SKU combo: nếu con lẻ có required date → popup nhập date theo con lẻ; nếu combo required date mà con lẻ không → popup theo combo | Functional | Medium | ✅ | PDF v2.17, update 30-05-2025 |
| R11 | SKU vải (Thời trang NVL): nhận theo Group UID hoặc số lượng; 1 SKU không thể vừa khai báo UID group vừa số lượng; Nhóm UID phải status New; hỗ trợ RFID mapping | Functional | High | ✅ | PDF v2.17, mục Nhận hàng Vải |
| R12 | SKU không barcode: luồng riêng từ màn hình scan, chọn SKU từ danh sách; validate SL thực nhận so với SL cần nhận | Functional | Medium | ✅ | PDF v2.17, update 22-05-2025 |
| R13 | Khai báo thiếu hàng / SPKPH từng sản phẩm: lý do thiếu (Giao thiếu hàng / Sản phẩm không phù hợp), tình trạng hàng, Nhà cung cấp giao bù, ghi chú, ảnh (SPKPH bắt buộc ảnh) | Functional | High | ✅ | PDF v2.17, Bước 2.2 |
| R14 | Khai báo thiếu hàng cho tất cả SKU: lý do mặc định "Giao thiếu", NCC giao bù mặc định "Có"; hỗ trợ "Xoá tất cả" khai báo | Functional | Medium | ✅ | PDF v2.17, Bước 2.3 |
| R15 | Xoá sản phẩm đã scan: xoá toàn bộ SL đã scan + khai báo thiếu của SKU đó | Functional | Medium | ✅ | PDF v2.17, Bước 2.4 |
| R16 | Kết thúc nhận hàng: button "Kết thúc nhận hàng" hiện khi SL đã đủ hoặc tất cả thiếu đã khai báo; khi này mới gọi API update PO Inside thành Receiving | Functional | High | ✅ | PDF v2.17, Bước 3 |
| R17 | Cập nhật biên bản giao hàng: chụp max 2 hình; Đồng kiểm → biên bản giao nhận; Không đồng kiểm → biên bản bàn giao kiện; bắt buộc trước khi Hoàn thành PO | Functional | High | ✅ | PDF v2.17, Bước 4 |
| R18 | Hoàn thành PO vs Hoàn thành phiên nhận hàng: "Hoàn thành PO" khi đủ SL hoặc tất cả thiếu có NCC giao bù = No; "Hoàn thành phiên" khi ngược lại; xác nhận → update PO=Received, ASN=Received, sync Inside | Functional | High | ✅ | PDF v2.17, Bước 5 |
| R19 | Thêm hoá đơn: Tax code (1-8 ký số, bắt buộc), Serial/Ký hiệu (1-8 ký số, bắt buộc), Form (bắt buộc), Total (chênh lệch ≤1000đ so với PO), Ngày (hiện tại hoặc quá khứ), ảnh hoá đơn; hỗ trợ nhiều hoá đơn | Functional | High | ✅ | PDF v2.17, mục Thêm hoá đơn |
| R20 | Case PO Gift chung PO thường: cảnh báo khi scan PO gốc nếu có gift; SKU trùng ưu tiên gift trước; 1 PO gốc nhiều gift → phải nhận hết gift trước | Functional | High | ✅ | PDF v2.17, Case 2 |
| R21 | Case PO Gift riêng: 1 PO gốc 1 gift → có thể nhận chung hoặc riêng; 1 PO gốc nhiều gift → bắt buộc nhận riêng từng gift trước | Functional | High | ✅ | PDF v2.17, update 25-11-2024 |
| R22 | Nhiều user cùng nhận (PO được bật cờ force): mỗi user tạo ASN riêng; 1 SKU normal nhiều ASN; cảnh báo nếu trùng số lô + mã cuộn | Functional | Medium | ✅ | PDF v2.17, update 17-05-2026 |
| R23 | PO Sample → PO Gốc: phải completed PO Sample + QC Passed trước; lần đầu nhận PO gốc max 30%; khi chưa QC xong UID ở trạng thái Received | Functional | High | ✅ | PDF v2.17, update 17-05-2026 |
| R24 | Validate scan PO với Packing list: nếu Packing list Waiting Approval → không cho nhận; nếu chưa import → không cho nhận (trừ trường hợp Approved không có data) | Functional | High | ✅ | PDF v2.17, mục Packing list validate |

---

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User đã login app với tài khoản được cung cấp và có phân quyền nhận hàng PO.
- PO đã được tạo trên Inside và đồng bộ sang WMS.
- Kho đã được cấu hình (có/không quản lý location, Required camera, v.v.).

---

### Luồng chuẩn (Happy Path) — Case 1: Nhận PO thường có đồng kiểm, đủ hàng

1. User vào **Purchase Order / Receiving PO**, scan mã PO hợp lệ.
2. Hệ thống hiển thị thông tin PO, tạo ASN status = Receiving.
3. User chọn **Có đồng kiểm** → bỏ qua bước scan camera.
4. Nếu shop quản lý location: user scan mã vị trí/giỏ hợp lệ.
5. User scan SKU, nhập số lượng (và HSD/số lô nếu yêu cầu).
6. Sau khi nhận đủ tất cả SKU → user xem danh sách sản phẩm xác nhận.
7. User chọn **Kết thúc nhận hàng** → hệ thống gọi API update PO = Receiving trên Inside.
8. User chụp 2 hình biên bản giao nhận và nhấn **Lưu**.
9. Nếu PO yêu cầu hoá đơn: user nhập thông tin hoá đơn và upload ảnh.
10. User chọn **Hoàn thành PO** → xác nhận → PO = Received, ASN = Received, update tồn kho, sync Inside.

---

### Luồng rẽ nhánh (Alternative Paths)

- **Alt-Flow 1 — Không đồng kiểm, có Required camera:** User scan camera trước khi chuyển sang bước scan location/sản phẩm.
- **Alt-Flow 2 — Nhận thiếu:** User khai báo lý do thiếu cho tất cả SKU chưa nhận đủ → button "Hoàn thành phiên nhận hàng" xuất hiện thay vì "Hoàn thành PO".
- **Alt-Flow 3 — SKU có HSD:** Sau scan SKU xuất hiện popup nhập HSD; validate theo rules tối thiểu.
- **Alt-Flow 4 — SKU vải Group UID:** User scan Nhóm UID + nhập SL (Kg/Mét) + HSD/số lô → xác nhận; không thể vừa khai báo UID vừa số lượng cho cùng 1 SKU.
- **Alt-Flow 5 — PO Gift chung PO gốc:** Scan PO gốc → cảnh báo yêu cầu scan PO Gift; nhận xen kẽ; hoàn thành cả 2.
- **Alt-Flow 6 — PO Sample:** PO sample phải được completed và QC Passed trước khi nhận PO gốc; lần đầu max 30%.

---

### Luồng ngoại lệ (Exception Paths)

- **Exc-Flow 1 — PO không thuộc kho:** Thông báo lỗi, không cho nhận.
- **Exc-Flow 2 — PO yêu cầu VAT chưa verify:** Thông báo "PO chưa được xác nhận hoá đơn".
- **Exc-Flow 3 — SKU không có trong PO:** "SKU [X] không có trong PO."
- **Exc-Flow 4 — SL vượt SL confirm:** "Số lượng của SKU [X] lớn hơn số lượng cần nhận trong PO."
- **Exc-Flow 5 — HSD thấp hơn tối thiểu:** "Hạn sử dụng nhỏ hơn yêu cầu được phép nhận hàng của PO ([HSD tối thiểu])."
- **Exc-Flow 6 — HSD vượt vòng đời sản phẩm:** "Hạn sử dụng lớn hơn vòng đời được thiết lập của sản phẩm ([X] tháng)."
- **Exc-Flow 7 — Số lô trùng:** "Số lô của sản phẩm đã tồn tại trên hệ thống."
- **Exc-Flow 8 — Serial/IMEI trùng:** "Serial/Imei của sản phẩm đã tồn tại trên hệ thống."
- **Exc-Flow 9 — Vị trí không hợp lệ / Giỏ không Available:** Thông báo tương ứng.
- **Exc-Flow 10 — Chưa cập nhật biên bản giao hàng khi Hoàn thành:** "Please update the delivery document image."
- **Exc-Flow 11 — Packing list chưa được duyệt:** "PO chưa được duyệt Packing list nên không thể nhận hàng."
- **Exc-Flow 12 — PO Sample chưa completed/QC Passed:** Thông báo không cho nhận PO gốc.

---

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| Loại nhận hàng | Có đồng kiểm / Không đồng kiểm | ✅ | Chọn 1 lần khi bắt đầu phiên |
| Camera | Mã camera | Theo config kho | Chỉ bắt buộc nếu Không đồng kiểm + kho bật Required camera |
| Vị trí/giỏ | Mã bin / mã giỏ | Theo config kho | PO Zone: chỉ bin Di động; PO thường: không cho bin Di động |
| HSD tối thiểu | Ngày | Theo rule | [% Allowed Shelf Life PO] × [Product Shelf Life] tháng + ngày nhận |
| Tax code | 1–8 ký tự chữ số | ✅ (nếu PO yêu cầu VAT) | Không ký tự đặc biệt |
| Serial hoá đơn | 1–8 ký tự chữ số | ✅ | Không ký tự đặc biệt |
| Total hoá đơn | Số tiền | ✅ | Chênh lệch ≤ 1.000đ so với tổng PO (tổng tất cả hoá đơn) |
| Ngày hoá đơn | YYYY-MM-DD | ✅ | Chỉ hiện tại hoặc quá khứ, không cho ngày tương lai |
| SL nhận 1 lần scan | 1 (cho SKU CCDC có serial) | ✅ | Không cho nhập SL > 1 |
| Số lô combo vải | Số nguyên dương | ✅ | Tổng SL thực nhận khai báo UID group phải là số nguyên dương |
| PO Sample | — | — | Phải completed + QC Passed trước khi nhận PO gốc; lần đầu max 30% packing list |

---

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Ngữ cảnh | Thông báo (VN) | Thông báo (EN) |
|:---------|:--------------|:---------------|
| SKU không có trong PO | SKU [X] không có trong PO | SKU [X] is not in PO |
| SL vượt SL confirm | Số lượng của SKU [X] lớn hơn số lượng cần nhận trong PO | The quantity of SKU [X] is greater than the quantity required in the PO |
| HSD thấp hơn tối thiểu | Hạn sử dụng nhỏ hơn yêu cầu được phép nhận hàng của PO ([ngày]) | Expiration date is less than the PO permission request ([ngày]) |
| HSD vượt vòng đời | Hạn sử dụng lớn hơn vòng đời được thiết lập của sản phẩm ([X] tháng) | Expiration date is greater than the product shelf life ([X] months) |
| Số lô trùng | Số lô của sản phẩm đã tồn tại trên hệ thống | Batch code of product already exists in the system |
| Mã camera không hợp lệ | Mã camera không hợp lệ hoặc không tồn tại trên hệ thống | Camera code is invalid or does not exist on the system |
| Vị trí không hợp lệ | Vị trí không hợp lệ hoặc không tồn tại trên hệ thống | Location code is invalid or does not exist on the system |
| Giỏ trạng thái không hợp lệ | Mã giỏ [X] có trạng thái không hợp lệ | Cart code [X] has invalid status |
| Chưa update biên bản | — | Please update the delivery document image |
| Hoàn thành PO xác nhận | — | Do you want to confirm completion of PO [X]? |
| Packing list chưa duyệt | PO chưa được duyệt Packing list nên không thể nhận hàng | — |
| Packing list chưa import | PO chưa import Packing list nên không thể nhận hàng | — |
| SL thực nhận SKU không barcode < SL PO | Số lượng thực nhận nhỏ hơn số lượng của PO ([X]/[Y]). Bạn có muốn xác nhận không? | — |
| SL vượt 10% Packing list vải | Số lượng thực nhận lớn hơn 10% so với Packing list | The actual received quantity exceeds the packing list by more than 10%. Do you want to confirm? |
| PO gốc có nhiều Gift | PO [X] có nhiều hơn 1 PO gift ([Y],[Z]), vui lòng hoàn thành tất cả PO gift trước khi nhận PO gốc | PO [X] has more than 1 gift PO ([Y],[Z]), please complete all gift PO before receiving original PO |
| PO Sample chưa passed | PO mẫu thử [X] của PO gốc [Y] chưa được nhận hàng hoặc kết quả đánh giá chất lượng KHÔNG ĐẠT nên không thể nhận hàng cho PO gốc | Sample PO [X] of original PO [Y] has not been received or the quality evaluation result is FAILED |
| Max 30% PO gốc lần đầu | PO chỉ cho nhận tối đa 30% cuộn vải theo từng lô cho phiên nhận đầu tiên | The PO only allows receiving up to 30% of the fabric rolls per batch for the first receiving session |

---

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01: Scan PO không thuộc kho**
  - **Given:** User scan mã PO không thuộc kho đang xử lý
  - **When:** Hệ thống validate
  - **Then:** Hiện thông báo lỗi, không cho chuyển sang bước tiếp

- **AC-02: Nhận hàng không đồng kiểm, kho bật Required camera**
  - **Given:** User chọn "Không đồng kiểm", kho có config Required camera = Yes
  - **When:** Hệ thống chuyển bước
  - **Then:** Yêu cầu user scan camera; nếu mã camera không hợp lệ hiện thông báo lỗi

- **AC-03: Validate HSD thấp hơn tối thiểu**
  - **Given:** SKU có Allowed Shelf Life 80%, Shelf Life 12 tháng → HSD tối thiểu = 9.6 tháng
  - **When:** User nhập HSD thấp hơn mức tối thiểu
  - **Then:** Hiện thông báo lỗi với ngày tối thiểu được tính

- **AC-04: Nhận SKU combo có con lẻ required date**
  - **Given:** SKU combo có ít nhất 1 con lẻ required date
  - **When:** User scan SKU combo
  - **Then:** Popup hiện để nhập date cho con lẻ theo số lượng combo

- **AC-05: Khai báo thiếu hàng và hoàn thành phiên**
  - **Given:** PO có 10 SKU A, user chỉ nhận được 7, NCC không giao bù
  - **When:** User khai báo lý do thiếu 3 SKU A với NCC giao bù = No → chọn Hoàn thành PO
  - **Then:** ASN = Received, PO config = Waiting Adj Invoice, sync Inside

- **AC-06: Thêm hoá đơn — Tax code vượt 8 ký tự**
  - **Given:** User nhập Tax code 9 ký tự
  - **When:** Submit form
  - **Then:** Hiện thông báo "Mã số thuế phải từ 1 đến 8 chữ số"

- **AC-07: Hoàn thành PO với tổng hoá đơn lệch > 1000đ**
  - **Given:** PO tổng tiền 1.000.000đ, user nhập hoá đơn 998.000đ
  - **When:** Submit
  - **Then:** Hiện cảnh báo "Tổng số tiền trên hoá đơn không hợp lệ"

- **AC-08: SKU không barcode, SL thực nhận < SL PO**
  - **Given:** SKU không có barcode, SL PO = 400, user nhập 300
  - **When:** User submit
  - **Then:** Hiện cảnh báo "Số lượng thực nhận nhỏ hơn số lượng của PO (300/400). Bạn có muốn xác nhận không?"

- **AC-09: PO Sample phải QC passed trước PO gốc**
  - **Given:** PO gốc có PO Sample chưa completed
  - **When:** User scan PO gốc để nhận
  - **Then:** Hiện thông báo không cho nhận PO gốc

- **AC-10: Packing list Waiting Approval → không cho nhận**
  - **Given:** PO vải có Packing list status = Waiting Approval
  - **When:** User scan PO để nhận
  - **Then:** Hiện thông báo không cho nhận

---

## ❓ Câu hỏi chưa rõ

- [ ] ❓ **R2 — Required camera:** Nếu kho có config Required camera = No thì luồng Không đồng kiểm có bỏ qua bước camera như đồng kiểm không? (Spec ghi "bypass bước scan camera giống case PO Đồng kiểm" — cần xác nhận)
- [ ] ❓ **R11 — SKU vải RFID mapping:** Nếu RFID đã tồn tại trên hệ thống thì hệ thống suggest SL theo UID group — user có được edit số lượng này không? (Spec ghi "cho phép user edit số lượng")
- [ ] ❓ **R23 — 30% làm tròn:** 30% của 18 cây = 5.4 cây → làm tròn lên 6. Nhưng nếu khai báo theo Kg thì 30% tính theo Kg hay theo số cuộn?
- [ ] ❓ **R19 — Nhiều hoá đơn:** Khi PO có PO Gift + PO gốc đều yêu cầu VAT, mỗi PO có hoá đơn riêng? Tổng tiền validate per PO hay cộng tổng 2 PO?
- [ ] ❓ **R22 — Nhiều user cùng nhận:** Cờ "Cho phép nhiều người cùng nhận" chỉ set được trên Web (Inbound detail) hay app cũng có?

---

## 📝 Thay đổi so với version cũ

| # | Nội dung thay đổi | Version cũ | Version mới | Ảnh hưởng TC |
|:--|:------------------|:----------|:-----------|:-------------|
| 1 | Gọi API Inside update Receiving khi kết thúc (không phải khi scan PO) | v1.3 | v2.17 | TC về timing API call |
| 2 | Bổ sung rules HSD tối thiểu tính theo % Shelf Life | v1.0 | v2.17 | TC validate HSD |
| 3 | Bổ sung luồng SKU combo có required date | v2.9 | v2.17 | TC mới cho SKU combo |
| 4 | PO Sample → PO Gốc | v2.17 | v2.17 (mới) | TC mới |

---

## Test Coverage
| Requirement | Test Case(s) | Status |
|:-----------|:------------|:-------|
| R1–R24 | _(chờ thiết kế)_ | ⏳ |

---

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 00:00:00 | v1.0 | Khởi tạo Feature Spec từ PDF v2.17 — App Receiving PO | `07062_Receiving_PO_Docs_ver2.17.pdf` |
