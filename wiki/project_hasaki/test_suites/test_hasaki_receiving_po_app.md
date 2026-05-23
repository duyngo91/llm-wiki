---
aliases: [Test App PO Hasaki, test-hasaki-po-app]
tags: [qa/test-suite, qa/feature-group/receiving-po]
status: Draft
feature: hasaki_receiving_po_app
requirement: wiki/project_hasaki/features/hasaki_receiving_po_app
dev:
qa:
created: 2026-05-23
updated: 2026-05-23
approved_by:
approved_at:
approval_note:
---

# 🧪 Test Suite: Nhận hàng PO — Mobile App (Hasaki WMS)

- **Feature liên quan:** [[wiki/project_hasaki/features/hasaki_receiving_po_app|hasaki_receiving_po_app]]
- **Requirement:** R1–R24, AC-01–AC-10
- **Dev phụ trách:** *(cập nhật)*
- **QA phụ trách:** *(cập nhật)*
- **Ngày cập nhật cuối:** 2026-05-23

## 📊 Tổng quan Test Coverage

| Loại Test | Số lượng TC | Pass | Fail | Blocked | Chưa test |
|:----------|:-----------|:-----|:-----|:--------|:----------|
| Happy Path | 10 | | | | 10 |
| Negative | 16 | | | | 16 |
| Boundary | 3 | | | | 3 |
| Decision Table | 4 | | | | 4 |
| State Transition | 3 | | | | 3 |
| Error Guessing | 3 | | | | 3 |
| **Tổng** | **39** | | | | **39** |

## ✅ Test Cases

| Test ID | Tiêu đề | AC/Req Cover | Loại case | Kỹ thuật test | Điều kiện tiên quyết | Các bước thực hiện | Kết quả mong đợi | Nguồn | Status |
|:--------|:--------|:-------------|:----------|:--------------|:--------------------|:-------------------|:-----------------|:-----------------|:-------|
| TC-PO-001 | Scan PO không thuộc kho — báo lỗi | AC-01 / R1 | Negative | Happy Path | PO tạo cho kho A, user đang ở kho B | 1. Vào App → PO / Receiving PO 2. Scan mã PO của kho A | Hệ thống hiển thị thông báo lỗi PO không thuộc kho, không cho chuyển bước | Explicit từ PDF v2.17 AC-01 | ⏳ |
| TC-PO-002 | Scan PO hợp lệ — tạo ASN và hiển thị thông tin | R1 | Positive | Happy Path | PO hợp lệ, thuộc kho, đã được xác nhận | 1. Scan mã PO hợp lệ | Hệ thống hiển thị thông tin PO (vendor, SKU list, SL); ASN được tạo với status=Receiving | Explicit từ PDF v2.17 R1 | ⏳ |
| TC-PO-003 | Scan PO đã Received — báo lỗi | R1 | Negative | State Transition | PO đã hoàn thành nhận (status=Received) | 1. Scan mã PO đã Received | Thông báo lỗi không cho nhận lại | Explicit từ PDF v2.17 R1 | ⏳ |
| TC-PO-004 | Không đồng kiểm + kho Required camera — bắt scan camera | AC-02 / R2 R3 | Negative | Decision Table | Kho có config Required camera=Yes | 1. Chọn "Không đồng kiểm" 2. Hệ thống chuyển bước scan camera 3. Không scan camera, thử chuyển bước | Hệ thống yêu cầu scan camera; không thể bỏ qua | Explicit từ PDF v2.17 AC-02 | ⏳ |
| TC-PO-005 | Scan camera mã không hợp lệ | R3 | Negative | Equivalence Partitioning | Đang ở bước scan camera | 1. Nhập mã camera không tồn tại trong hệ thống | Thông báo "Camera code is invalid or does not exist on the system" | Explicit từ PDF v2.17 Error Map | ⏳ |
| TC-PO-006 | Có đồng kiểm — bỏ qua bước scan camera | R2 | Positive | Happy Path | Kho bất kỳ | 1. Chọn "Có đồng kiểm" | Hệ thống không yêu cầu scan camera; chuyển thẳng sang bước scan location/SKU | Explicit từ PDF v2.17 R2 | ⏳ |
| TC-PO-007 | PO Zone — chỉ nhận vào bin Di động | R4 | Negative | Decision Table | PO Zone, có bin thường và bin Di động | 1. Scan vị trí bin thường | Thông báo không hợp lệ; chỉ cho scan bin Di động | Explicit từ PDF v2.17 R4 | ⏳ |
| TC-PO-008 | PO thường — không nhận vào bin Di động | R4 | Negative | Decision Table | PO thường, user scan bin Di động | 1. Scan mã bin Di động | Thông báo "Vị trí không hợp lệ" hoặc tương đương | Explicit từ PDF v2.17 R4 | ⏳ |
| TC-PO-009 | Scan SKU không có trong PO | R5 | Negative | Equivalence Partitioning | PO đang Receiving, scan SKU không thuộc PO | 1. Scan barcode SKU lạ | Thông báo "SKU [X] is not in PO" | Explicit từ PDF v2.17 Error Map | ⏳ |
| TC-PO-010 | Scan SKU vượt SL confirm | R5 | Negative | Boundary Value Analysis | PO có SKU A SL confirm=10, đã nhận 10 | 1. Scan thêm 1 SKU A | Thông báo "The quantity of SKU [X] is greater than the quantity required in the PO" | Explicit từ PDF v2.17 Error Map | ⏳ |
| TC-PO-011 | HSD thấp hơn tối thiểu — báo lỗi với ngày cụ thể | AC-03 / R6 | Negative | Boundary Value Analysis | SKU có Shelf Life 12 tháng, Allowed 80% → HSD tối thiểu=9.6 tháng | 1. Scan SKU 2. Nhập HSD thấp hơn mức tối thiểu | Thông báo "Expiration date is less than the PO permission request ([ngày tối thiểu])" | Explicit từ PDF v2.17 AC-03 | ⏳ |
| TC-PO-013 | HSD vượt vòng đời sản phẩm — báo lỗi | R6 | Negative | Boundary Value Analysis | SKU có Shelf Life 24 tháng | 1. Nhập HSD = ngày hôm nay + 25 tháng | Thông báo "Expiration date is greater than the product shelf life (24 months)" | Explicit từ PDF v2.17 Error Map | ⏳ |
| TC-PO-014 | Số lô trùng hệ thống — báo lỗi | R7 | Negative | Error Guessing | Số lô "LOT2024" đã tồn tại trong hệ thống | 1. Scan SKU 2. Nhập số lô "LOT2024" | Thông báo "Batch code of product already exists in the system" | Explicit từ PDF v2.17 Error Map | ⏳ |
| TC-PO-015 | Serial/IMEI trùng hệ thống — báo lỗi | R8 | Negative | Error Guessing | Serial "SN12345678" đã tồn tại | 1. Scan SKU CCDC 2. Nhập Serial "SN12345678" | Thông báo "Serial/Imei of product already exists in the system" | Explicit từ PDF v2.17 Error Map | ⏳ |
| TC-PO-016 | SKU CCDC — mỗi scan chỉ nhận SL=1 | R8 | Positive | Happy Path | SKU CCDC có Serial trong PO | 1. Scan SKU CCDC 2. Hệ thống hiển thị form nhập Serial | SL mặc định=1, không cho sửa > 1; sau nhập Serial hợp lệ ghi nhận thành công | Explicit từ PDF v2.17 R8 | ⏳ |
| TC-PO-017 | SKU combo có con lẻ required date — popup nhập date | AC-04 / R10 | Positive | Happy Path | SKU combo có con lẻ required date | 1. Scan SKU combo | Popup hiển thị yêu cầu nhập date cho con lẻ theo số lượng combo | Explicit từ PDF v2.17 AC-04 | ⏳ |
| TC-PO-018 | Khai báo thiếu — NCC giao bù = No → Hoàn thành PO | AC-05 / R13 R18 | Positive | Happy Path | PO có 10 SKU A, nhận 7 | 1. Khai báo thiếu 3 SKU A 2. Lý do: Giao thiếu, NCC giao bù=No 3. Chọn Hoàn thành PO | ASN=Received, PO=Received/Waiting Adj, sync Inside; SPKPH: bắt buộc upload ảnh | Explicit từ PDF v2.17 AC-05 | ⏳ |
| TC-PO-019 | SPKPH thiếu ảnh — không cho hoàn thành | R13 | Negative | Happy Path | User khai báo SPKPH nhưng không upload ảnh | 1. Chọn lý do "Sản phẩm không phù hợp" 2. Không chụp ảnh 3. Submit | Hệ thống không cho lưu; yêu cầu bắt buộc upload ảnh cho SPKPH | Explicit từ PDF v2.17 R13 | ⏳ |
| TC-PO-020 | Cập nhật biên bản — chưa upload ảnh → không Hoàn thành | R17 | Negative | State Transition | Đang ở bước cập nhật biên bản | 1. Không chụp ảnh 2. Chọn Hoàn thành PO | Thông báo "Please update the delivery document image" | Explicit từ PDF v2.17 Error Map | ⏳ |
| TC-PO-021 | Thêm hoá đơn — Tax code vượt 8 ký tự | AC-06 / R19 | Negative | Boundary Value Analysis | Đang ở màn hình thêm hoá đơn | 1. Nhập Tax code 9 ký tự số | Thông báo lỗi Tax code phải từ 1–8 chữ số | Explicit từ PDF v2.17 AC-06 | ⏳ |
| TC-PO-023 | Tổng hoá đơn lệch > 1000đ so với PO | AC-07 / R19 | Negative | Boundary Value Analysis | PO tổng tiền 1.000.000đ | 1. Nhập hoá đơn Total = 998.000đ (lệch 2.000đ) | Thông báo "Tổng số tiền trên hoá đơn không hợp lệ" | Explicit từ PDF v2.17 AC-07 | ⏳ |
| TC-PO-025 | SKU không barcode — SL thực < SL PO → cảnh báo xác nhận | AC-08 / R12 | Positive | Happy Path | SKU không barcode trong PO, SL PO=400 | 1. Chọn SKU không barcode từ danh sách 2. Nhập SL thực=300 3. Submit | Cảnh báo "Số lượng thực nhận nhỏ hơn số lượng của PO (300/400). Bạn có muốn xác nhận không?" | Explicit từ PDF v2.17 AC-08 | ⏳ |
| TC-PO-026 | PO vải — validate Packing list Waiting Approval | AC-10 / R24 | Negative | Decision Table | PO vải, Packing list status=Waiting Approval | 1. Scan PO vải | Thông báo "PO chưa được duyệt Packing list nên không thể nhận hàng" | Explicit từ PDF v2.17 AC-10 | ⏳ |
| TC-PO-027 | PO vải — validate Packing list chưa import | R24 | Negative | Decision Table | PO vải chưa import Packing list | 1. Scan PO vải | Thông báo "PO chưa import Packing list nên không thể nhận hàng" | Explicit từ PDF v2.17 R24 | ⏳ |
| TC-PO-028 | PO Sample chưa completed — không cho nhận PO gốc | AC-09 / R23 | Negative | State Transition | PO gốc có PO Sample chưa completed | 1. Scan PO gốc | Thông báo "Sample PO [X] of original PO [Y] has not been received or the quality evaluation result is FAILED" | Explicit từ PDF v2.17 AC-09 | ⏳ |
| TC-PO-029 | PO Sample QC Failed — không cho nhận PO gốc | R23 | Negative | State Transition | PO Sample completed nhưng QC Failed | 1. Scan PO gốc | Thông báo không cho nhận PO gốc | Explicit từ PDF v2.17 R23 | ⏳ |
| TC-PO-030 | PO gốc lần đầu — nhận vượt 30% → báo lỗi | R23 | Negative | Boundary Value Analysis | PO Sample QC Passed; PO gốc có 100 cuộn | 1. Cố nhận 31 cuộn lần đầu | Thông báo "The PO only allows receiving up to 30% of the fabric rolls per batch for the first receiving session" | Explicit từ PDF v2.17 R23 Error Map | ⏳ |
| TC-PO-031 | PO Gift chung PO gốc — cảnh báo nhận gift trước | R20 | Positive | Happy Path | PO gốc có 1 PO Gift chung | 1. Scan PO gốc | Cảnh báo yêu cầu scan PO Gift trước; SKU trùng ưu tiên gift | Explicit từ PDF v2.17 R20 | ⏳ |
| TC-PO-032 | PO gốc có nhiều Gift — phải nhận hết gift trước | R20 R21 | Negative | Error Guessing | PO gốc có 2 PO Gift | 1. Scan PO gốc 2. Cố hoàn thành PO gốc khi chưa hoàn thành cả 2 Gift | Thông báo "PO [X] has more than 1 gift PO ([Y],[Z]), please complete all gift PO before receiving original PO" | Explicit từ PDF v2.17 Error Map | ⏳ |
| TC-PO-033 | SKU vải Group UID — không thể vừa UID vừa số lượng | R11 | Negative | Equivalence Partitioning | SKU vải trong PO | 1. Khai báo UID group cho SKU vải 2. Cố nhập thêm số lượng thông thường | Hệ thống ngăn không cho vừa UID vừa số lượng cho cùng 1 SKU | Explicit từ PDF v2.17 R11 | ⏳ |
| TC-PO-034 | SKU vải Group UID — status phải là New | R11 | Negative | State Transition | UID group có status đã dùng (In-Bin) | 1. Nhập mã UID group status ≠ New | Thông báo lỗi UID group không hợp lệ | Explicit từ PDF v2.17 R11 | ⏳ |
| TC-PO-035 | Nhiều user cùng nhận — mỗi user tạo ASN riêng | R22 | Positive | Happy Path | PO có cờ force multiple users | 1. User A scan PO → tạo ASN1 2. User B scan cùng PO → tạo ASN2 | Mỗi user có ASN riêng; không conflict | Explicit từ PDF v2.17 R22 | ⏳ |
| TC-PO-036 | Nhiều user — cảnh báo trùng số lô + mã cuộn | R22 | Negative | Error Guessing | User A đã nhận roll R001 lô L001 | 1. User B nhận cùng roll R001 lô L001 | Hệ thống cảnh báo trùng số lô + mã cuộn | Explicit từ PDF v2.17 R22 | ⏳ |
| TC-PO-037 | Kết thúc nhận hàng — API update PO=Receiving trên Inside | R16 | Positive | Happy Path | User đã scan đủ SKU | 1. Chọn "Kết thúc nhận hàng" | API gọi sang Inside update PO status=Receiving; không gọi sớm hơn | Explicit từ PDF v2.17 R16 | ⏳ |
| TC-PO-038 | Hoàn thành PO — xác nhận popup | R18 | Positive | Happy Path | Tất cả SKU đủ hoặc thiếu đã khai báo | 1. Chọn "Hoàn thành PO" | Popup "Do you want to confirm completion of PO [X]?" → Yes → PO=Received, ASN=Received, sync Inside | Explicit từ PDF v2.17 R18 Error Map | ⏳ |
| TC-PO-039 | Hoàn thành phiên nhận hàng — khi còn SKU NCC giao bù | R18 | Positive | Happy Path | Một số SKU khai báo thiếu với NCC giao bù=Yes | 1. Chọn "Hoàn thành phiên" | ASN=Received nhưng PO chưa Received; phiên mới có thể được tạo | Explicit từ PDF v2.17 R18 | ⏳ |
| TC-PO-040 | Cập nhật biên bản Đồng kiểm — max 2 hình | R17 | Positive | Boundary Value Analysis | Đang ở bước cập nhật biên bản, chọn Đồng kiểm | 1. Chụp 2 hình biên bản giao nhận | Hệ thống chấp nhận; không cho upload hình thứ 3 | Explicit từ PDF v2.17 R17 | ⏳ |
| TC-PO-041 | Ngày hoá đơn tương lai — không chấp nhận | R19 | Negative | Boundary Value Analysis | Đang ở màn hình thêm hoá đơn | 1. Nhập Ngày hoá đơn = ngày mai | Hệ thống không cho chọn ngày tương lai | Explicit từ PDF v2.17 R19 | ⏳ |
| TC-PO-042 | Xoá sản phẩm đã scan — xoá cả khai báo thiếu | R15 | Positive | Happy Path | SKU A đã scan 5 và khai báo thiếu 3 | 1. Chọn xoá SKU A | Hệ thống xoá toàn bộ SL scan + khai báo thiếu của SKU A; SKU về trạng thái chưa nhận | Explicit từ PDF v2.17 R15 | ⏳ |

## 🚫 Test Cases Lỗi Thời (Deprecated)

| Test ID | Tiêu đề | Lý do deprecated | Ngày | Nguồn |
|:--------|:--------|:-----------------|:-----|:------|
| — | — | — | — | — |

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 21:49:34 | v1.1 | Loại TC-PO-012/022/024 vì boundary suy diễn; chuyển câu hỏi về Feature questions; đổi cột nguồn về `Nguồn` | [[WIKI_RULES]] |
| 2026-05-23 00:11:00 | v1.0 | Khởi tạo Test Suite từ Feature Spec v1.0 — 42 test cases | [[wiki/project_hasaki/features/hasaki_receiving_po_app\|hasaki_receiving_po_app]] |
