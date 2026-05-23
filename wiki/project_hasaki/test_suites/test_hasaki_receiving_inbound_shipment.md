---
aliases: [Test Inbound Shipment Hasaki, test-hasaki-inbound]
tags: [qa/test-suite, qa/feature-group/receiving-po]
status: Draft
feature: hasaki_receiving_inbound_shipment
requirement: wiki/project_hasaki/features/hasaki_receiving_inbound_shipment
dev:
qa:
created: 2026-05-23
updated: 2026-05-23
approved_by:
approved_at:
approval_note:
---

# 🧪 Test Suite: Inbound Shipment & ASN Web (Hasaki WMS)

- **Feature liên quan:** [[wiki/project_hasaki/features/hasaki_receiving_inbound_shipment|hasaki_receiving_inbound_shipment]]
- **Requirement:** R1–R20, AC-01–AC-10
- **Dev phụ trách:** *(cập nhật)*
- **QA phụ trách:** *(cập nhật)*
- **Ngày cập nhật cuối:** 2026-05-23

## 📊 Tổng quan Test Coverage

| Loại Test | Số lượng TC | Pass | Fail | Blocked | Chưa test |
|:----------|:-----------|:-----|:-----|:--------|:----------|
| Happy Path | 8 | | | | 8 |
| Negative | 9 | | | | 9 |
| Boundary | 1 | | | | 1 |
| State Transition | 3 | | | | 3 |
| Error Guessing | 2 | | | | 2 |
| **Tổng** | **23** | | | | **23** |

## ✅ Test Cases

| Test ID | Tiêu đề | AC/Req Cover | Loại case | Kỹ thuật test | Điều kiện tiên quyết | Các bước thực hiện | Kết quả mong đợi | Nguồn | Status |
|:--------|:--------|:-------------|:----------|:--------------|:--------------------|:-------------------|:-----------------|:-----------------|:-------|
| TC-INB-001 | Filter WMS Status hiển thị đúng 5 giá trị | AC-01 / R3 | Positive | Happy Path | User đã login WMS, có PO type=PO | 1. Vào Inbound / Inbound Shipment 2. Mở More Filter 3. Tìm filter "WMS Status" | Filter hiển thị đúng 5 giá trị: Open, Receiving, Received, Completed, Canceled; hỗ trợ chọn nhiều | Explicit từ PDF v2.17 R3 | ⏳ |
| TC-INB-002 | Filter WMS Status chỉ áp dụng cho Type=PO | AC-01 / R3 | Negative | Equivalence Partitioning | Có Inbound Shipment loại Transfer | 1. Filter WMS Status = "Receiving" 2. Xem kết quả listing | Chỉ hiển thị các PO có type=PO; các type khác (Transfer...) không xuất hiện trong kết quả | Explicit từ PDF v2.17 R3 | ⏳ |
| TC-INB-003 | Cột WMS Status hiển thị thời gian chờ khi Receiving | AC-02 / R9 | Positive | Happy Path | Có PO với WMS Status=Receiving đã bắt đầu scan | 1. Filter WMS Status = "Receiving" 2. Xem cột WMS Status trong listing | Cột WMS Status hiển thị thêm thời lượng đã bao lâu chưa hoàn thành (VD: "2h 30m") | Explicit từ PDF v2.17 R9 | ⏳ |
| TC-INB-004 | PO không đủ điều kiện — Eligible=No + Description đúng | AC-03 / R2 R5 R6 | Negative | Happy Path | Có PO chưa được duyệt trên Inside | 1. Xem listing Inbound Shipment 2. Tìm PO chưa duyệt | Cột "Eligible to receive"=No; Cột "Description"="PO not approved" | Explicit từ PDF v2.17 AC-03 | ⏳ |
| TC-INB-005 | Eligible=No khi PO chưa verify hoá đơn | R2 R5 R6 | Negative | Equivalence Partitioning | Có PO yêu cầu VAT chưa verify hoá đơn | 1. Xem listing 2. Tìm PO chưa verify hoá đơn | Eligible to receive=No; Description="PO not yet verified invoice" | Explicit từ PDF v2.17 Error Map | ⏳ |
| TC-INB-006 | Eligible=No khi SKU Tester chưa khai báo SKU gốc | R2 R5 R6 | Negative | Error Guessing | Có PO chứa SKU Tester chưa khai báo gốc | 1. Xem listing Inbound Shipment | Eligible to receive=No; Description="SKU Tester [X] does not have original SKU" | Explicit từ PDF v2.17 Error Map | ⏳ |
| TC-INB-007 | Filter "Check of goods" = Yes lọc đúng PO | R1 / R4 | Positive | Equivalence Partitioning | Có PO đồng kiểm và PO không đồng kiểm | 1. More Filter → Check of goods = Yes 2. Xem kết quả | Chỉ hiển thị PO có cột Check of goods=Yes | Explicit từ PDF v2.17 R1 R4 | ⏳ |
| TC-INB-008 | Filter "Eligible to receive" = No lọc đúng | R2 | Positive | Equivalence Partitioning | Có PO không đủ điều kiện và đủ điều kiện | 1. More Filter → Eligible to receive = No 2. Xem kết quả | Chỉ hiển thị PO Eligible=No | Explicit từ PDF v2.17 R2 | ⏳ |
| TC-INB-009 | Inbound Detail hiển thị đúng Qty confirm / received / missing | AC-04 / R11 | Positive | Happy Path | PO có 10 SKU A, đã nhận 7 | 1. Click vào PO để xem detail 2. Xem cột Qty | Qty confirm=10, Qty received=7, Qty missing=3; missing=confirm−received | Explicit từ PDF v2.17 AC-04 | ⏳ |
| TC-INB-012 | Giải trình PO: thêm comment thành công | AC-05 / R12 | Positive | Happy Path | PO đang ở bất kỳ status nào, user có quyền | 1. Mở Inbound Detail 2. Nhập nội dung vào ô Comment 3. Nhấn "Thêm" | Comment lưu thành công với email Hasaki + thời gian; hiển thị đầu bảng (mới nhất trước) | Explicit từ PDF v2.17 AC-05 | ⏳ |
| TC-INB-013 | Giải trình PO: nhiều comment sắp xếp mới nhất lên đầu | R12 | Positive | State Transition | Đã có sẵn 1 comment trong PO | 1. Thêm 1 comment mới 2. Xem bảng comment | Comment mới hiển thị ở hàng đầu tiên; comment cũ bên dưới | Explicit từ PDF v2.17 R12 | ⏳ |
| TC-INB-014 | ASN ReOpen thành công khi chưa scan item | AC-06 / R16 | Positive | Happy Path | ASN Status=Receiving, chưa scan item nào | 1. Vào ASN Listing 2. Click ReOpen 3. Xác nhận "Yes" | ASN chuyển Status=Open; nhân viên bị xóa khỏi ASN | Explicit từ PDF v2.17 AC-06 | ⏳ |
| TC-INB-015 | Nút ReOpen ẩn khi đã scan ít nhất 1 item | AC-07 / R16 | Negative | State Transition | ASN Status=Receiving, đã scan 1 item | 1. Vào ASN Listing 2. Tìm ASN đã scan item | Nút ReOpen không hiển thị trong cột Action | Explicit từ PDF v2.17 AC-07 | ⏳ |
| TC-INB-016 | Nút ReOpen ẩn khi ASN không phải Receiving | R16 | Negative | State Transition | ASN Status=Open / Received / Completed | 1. Xem cột Action cho các ASN status khác | Nút ReOpen không hiển thị | Explicit từ PDF v2.17 R16 | ⏳ |
| TC-INB-017 | In biên bản — nút chỉ hiện khi Receiving hoặc Received | AC-08 / R17 | Positive | Happy Path | ASN Status=Received | 1. Vào ASN Listing 2. Kiểm tra cột Action | Nút "In biên bản" hiển thị | Explicit từ PDF v2.17 R17 | ⏳ |
| TC-INB-018 | In biên bản — nút ẩn khi ASN status khác | R17 | Negative | Equivalence Partitioning | ASN Status=Open hoặc Completed | 1. Xem cột Action | Nút "In biên bản" không hiển thị | Explicit từ PDF v2.17 R17 | ⏳ |
| TC-INB-019 | In biên bản — chọn khổ In Bill, hệ thống nhớ lựa chọn | AC-08 / R14 | Positive | Happy Path | ASN Status=Receiving | 1. Click In biên bản 2. Chọn "In Bill" 3. In xong 4. Mở lại In biên bản | Lần tiếp theo mở biên bản, khổ giấy mặc định vẫn là "In Bill" (lưu theo máy local) | Explicit từ PDF v2.17 R14 | ⏳ |
| TC-INB-020 | In biên bản — option "In tất cả" vs "Chỉ thiếu/SPKPH" | R14 | Positive | Equivalence Partitioning | ASN có cả SKU đủ và SKU thiếu | 1. Click In biên bản 2. Chọn "In tất cả" → kiểm tra nội dung 3. Chọn "Thiếu/SPKPH" → kiểm tra nội dung | "In tất cả" hiển thị đủ SKU; "Thiếu/SPKPH" chỉ hiển thị SKU có số lượng thiếu hoặc SPKPH | Explicit từ PDF v2.17 R14 | ⏳ |
| TC-INB-021 | ASN Detail — header hiển thị Đồng kiểm, Camera, Mã vị trí | R19 | Positive | Happy Path | ASN có đầy đủ thông tin | 1. Mở ASN Detail | Header hiển thị: Đồng kiểm (Yes/No), Camera code, Location code | Explicit từ PDF v2.17 R19 | ⏳ |
| TC-INB-022 | ASN Detail — danh sách SKU hiển thị Group UID | AC-09 / R20 | Positive | Happy Path | ASN có SKU vải nhận theo Group UID | 1. Mở ASN Detail của PO vải 2. Xem cột Group UID | Cột Group UID hiển thị mã nhóm UID đã scan | Explicit từ PDF v2.17 AC-09 | ⏳ |
| TC-INB-023 | Filter ASN — Warehouse gợi ý từ đủ 3 ký tự | AC-10 / R13 | Positive | Boundary Value Analysis | Tồn tại kho "Hà Nội" trong hệ thống | 1. Vào ASN Filter → ô Warehouse 2. Nhập "Hà" (2 ký tự) → quan sát 3. Nhập "Hà N" (3 ký tự) → quan sát | 2 ký tự: không có gợi ý; 3 ký tự: dropdown hiển thị kho phù hợp theo phân quyền | Explicit từ PDF v2.17 AC-10 | ⏳ |
| TC-INB-024 | Status mapping Inside → WMS hiển thị đúng | R7 | Positive | Happy Path | PO có status "Verified" trên Inside | 1. Xem listing Inbound Shipment 2. Tìm PO đó 3. Kiểm tra cột Status và WMS Status | Cột Status = "Verified"; WMS Status = "Open" | Explicit từ PDF v2.17 R7 | ⏳ |
| TC-INB-025 | Cột listing ASN có đủ các cột theo spec | R15 | Positive | Happy Path | Có ASN trong hệ thống | 1. Vào ASN Listing 2. Kiểm tra tiêu đề cột | Đủ các cột: ASN number, Warehouse, Type, Inbound shipment, Inbound source, Outbound order, Outbound source, Owner, Check of goods, Camera code, Location code, Cart code, Created date, Updated date, Status, Action | Explicit từ PDF v2.17 R15 | ⏳ |

## 🚫 Test Cases Lỗi Thời (Deprecated)

| Test ID | Tiêu đề | Lý do deprecated | Ngày | Nguồn |
|:--------|:--------|:-----------------|:-----|:------|
| — | — | — | — | — |

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 21:49:34 | v1.1 | Loại TC-INB-010/011 vì boundary suy diễn; chuyển câu hỏi về Feature questions; đổi cột nguồn về `Nguồn` | [[WIKI_RULES]] |
| 2026-05-23 00:10:00 | v1.0 | Khởi tạo Test Suite từ Feature Spec v1.0 — 25 test cases | [[wiki/project_hasaki/features/hasaki_receiving_inbound_shipment\|hasaki_receiving_inbound_shipment]] |
