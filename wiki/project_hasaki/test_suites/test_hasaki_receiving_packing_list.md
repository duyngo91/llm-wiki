---
aliases: [Test Packing List Hasaki, test-hasaki-packing-list]
tags: [qa/test-suite, qa/feature-group/receiving-po]
status: Draft
feature: hasaki_receiving_packing_list
requirement: wiki/project_hasaki/features/hasaki_receiving_packing_list
dev:
qa:
created: 2026-05-23
updated: 2026-05-23
approved_by:
approved_at:
approval_note:
---

# 🧪 Test Suite: Import Packing List PO (Hasaki WMS)

- **Feature liên quan:** [[wiki/project_hasaki/features/hasaki_receiving_packing_list|hasaki_receiving_packing_list]]
- **Requirement:** R1–R20, AC-01–AC-07
- **Dev phụ trách:** *(cập nhật)*
- **QA phụ trách:** *(cập nhật)*
- **Ngày cập nhật cuối:** 2026-05-23

## 📊 Tổng quan Test Coverage

| Loại Test | Số lượng TC | Pass | Fail | Blocked | Chưa test |
|:----------|:-----------|:-----|:-----|:--------|:----------|
| Happy Path | 8 | | | | 8 |
| Negative | 10 | | | | 10 |
| Boundary | 2 | | | | 2 |
| State Transition | 3 | | | | 3 |
| Error Guessing | 2 | | | | 2 |
| **Tổng** | **25** | | | | **25** |

## ✅ Test Cases

| Test ID | Tiêu đề | AC/Req Cover | Loại case | Kỹ thuật test | Điều kiện tiên quyết | Các bước thực hiện | Kết quả mong đợi | Nguồn | Status |
|:--------|:--------|:-------------|:----------|:--------------|:--------------------|:-------------------|:-----------------|:-----------------|:-------|
| TC-PL-001 | Import Packing List hợp lệ — tự động Approved | AC-01 / R1 R7 | Positive | Happy Path | PO vải tồn tại; tổng Qty request ≤ ±5% Qty PO | 1. Vào Inbound / Packing list PO 2. Nhấn Import 3. Upload file Excel hợp lệ theo template | Packing list status = Approved; cột Inbound Listing hiển thị "Approved" kèm hyperlink | Explicit từ PDF v2.17 AC-01 | ⏳ |
| TC-PL-002 | Import Packing List vượt ±5% — Waiting for Approval | AC-02 / R4 R7 | Positive | Happy Path | PO vải có Qty PO = 100; file import Qty = 110 (chênh 10%) | 1. Import file với Qty vượt ±5% 2. Xác nhận Import | Status = Waiting for Approval; cột Inbound Listing hiển thị "Waiting for Approval" kèm button Approve | Explicit từ PDF v2.17 AC-02 | ⏳ |
| TC-PL-003 | Import vượt ±5% — action Kiểm tra lại không lưu | R4 | Negative | Happy Path | PO vải có Qty PO = 100; file import Qty = 111 | 1. Import file 2. Nhận cảnh báo ±5% 3. Chọn "Kiểm tra lại" | Không lưu; user quay lại màn hình import để sửa file | Explicit từ PDF v2.17 R4 | ⏳ |
| TC-PL-004 | App không cho nhận khi Packing list Waiting Approval | AC-03 / R9 / Exc-Flow 6 | Negative | State Transition | PO vải có Packing list status = Waiting for Approval | 1. Vào App nhận hàng 2. Scan mã PO vải | Thông báo "PO chưa được duyệt Packing list nên không thể nhận hàng." | Explicit từ PDF v2.17 AC-03 | ⏳ |
| TC-PL-005 | BOD Approve Packing list từ Inbound Detail | R11 | Positive | Happy Path | Packing list status = Waiting for Approval | 1. Mở Inbound Detail của PO vải 2. Nhấn button Approve 3. Xác nhận "Bạn có chắc chắn..." 4. Chọn Yes | Status chuyển = Approved; App cho phép nhận hàng PO | Explicit từ PDF v2.17 R11 | ⏳ |
| TC-PL-006 | Validate import — PO code trống | R2 | Negative | Equivalence Partitioning | File import có dòng PO code bỏ trống | 1. Upload file có dòng PO code trống | Lỗi dòng tương ứng "Dòng N – Mã PO không được để trống" | Explicit từ PDF v2.17 R2 | ⏳ |
| TC-PL-007 | Validate import — PO code không tồn tại hệ thống | R2 | Negative | Equivalence Partitioning | File import chứa PO code không có trên hệ thống | 1. Upload file có PO code sai | Lỗi "Dòng N – Mã PO không tồn tại trên hệ thống" | Explicit từ PDF v2.17 R2 | ⏳ |
| TC-PL-008 | Validate import — SKU không có trong PO | R2 | Negative | Equivalence Partitioning | File import chứa SKU không thuộc PO | 1. Upload file với SKU không trong PO | Lỗi "Dòng N – SKU không tồn tại trong PO" | Explicit từ PDF v2.17 R2 | ⏳ |
| TC-PL-009 | Validate import — Qty request âm | R2 | Negative | Boundary Value Analysis | File import có dòng Qty = -1 | 1. Upload file với Qty = -1 | Lỗi "Dòng N – Số lượng yêu cầu không hợp lệ" | Explicit từ PDF v2.17 R2 | ⏳ |
| TC-PL-011 | Validate import — trùng dữ liệu giữa các dòng trong file | R2 | Negative | Error Guessing | File import có 2 dòng cùng PO code + SKU + Roll code + Batch code | 1. Upload file có dòng trùng | Lỗi "Dòng N – Dữ liệu đã tồn tại trên file import" | Explicit từ PDF v2.17 R2 | ⏳ |
| TC-PL-012 | Import lại — trùng khóa → update Qty request (không tạo mới) | R3 | Positive | State Transition | Đã có Packing list với Roll code A, Batch code 01 | 1. Import lại file với Roll code A, Batch code 01, Qty mới = 20 | Qty request của dòng đó cập nhật = 20; không sinh thêm dòng mới | Explicit từ PDF v2.17 R3 | ⏳ |
| TC-PL-013 | Delivery method Partial — không validate ±5% | R5 | Positive | Equivalence Partitioning | PO vải; file import có Delivery method = Partial; Qty = 150% Qty PO | 1. Import file Partial 2. Xem kết quả | Không có cảnh báo ±5%; chỉ cần Qty ≤ Qty PO là chấp nhận | Explicit từ PDF v2.17 R5 | ⏳ |
| TC-PL-014 | Re-import Approved → vượt ±5% → Waiting for Approval | AC-07 / R12 | Positive | State Transition | Packing list PO đang Approved | 1. Import lại file với Qty vượt ±5% 2. Xác nhận Import | Status Packing list chuyển về Waiting for Approval | Explicit từ PDF v2.17 AC-07 | ⏳ |
| TC-PL-015 | Filter Inbound theo Packing list = Waiting Approve | R10 | Positive | Equivalence Partitioning | Có cả PO Waiting Approval và Approved | 1. Vào Inbound Listing → More Filter 2. Chọn Packing list = Waiting Approve | Chỉ hiển thị PO có Packing list Waiting Approval | Explicit từ PDF v2.17 R10 | ⏳ |
| TC-PL-016 | App nhận hàng SKU vải — suggest Roll code từ Packing list | R14 | Positive | Happy Path | Packing list Approved; PO vải có Roll code A/B/C | 1. Scan PO trên App 2. Nhập số lô | Hệ thống gợi ý Roll code từ Packing list tương ứng số lô | Explicit từ PDF v2.17 R14 | ⏳ |
| TC-PL-017 | App — Quy đổi Kg → Yard | AC-04 / R17 | Positive | Happy Path | SKU đặt theo Yard; Width = 1.5m, GSM = 200g/m², nhập Weight = 15Kg | 1. Nhập số lượng thực nhận 15Kg trên App 2. Xác nhận | Hệ thống hiển thị và tính Yard = 15*1000/(1.5*200*0.9144) ≈ 54.68 Yard | Explicit từ PDF v2.17 AC-04 | ⏳ |
| TC-PL-018 | App — Trừ lõi tự động từ Packing list, disabled không cho edit | AC-05 / R16 | Positive | Happy Path | Gross Qty = 15.3 Kg, Net Qty = 15 Kg trong Packing list | 1. Vào màn hình khai báo UID group 2. Kiểm tra trường Trừ lõi | Trừ lõi = 0.3 Kg; trường bị disable (không thể chỉnh) | Explicit từ PDF v2.17 AC-05 | ⏳ |
| TC-PL-019 | App — SL thực nhận > 10% Packing list → cảnh báo | AC-06 / R19 | Positive | Boundary Value Analysis | Packing list Qty = 10; nhập thực nhận = 11.1 (>10%) | 1. Nhập SL thực nhận = 11.1 2. Nhấn Xác nhận | Cảnh báo "Số lượng thực nhận lớn hơn 10% so với Packing list, bạn có muốn xác nhận nhận hàng không?" | Explicit từ PDF v2.17 AC-06 | ⏳ |
| TC-PL-021 | App — SL thực nhận > SL packing list → ghi nhận theo packing list + ADJ | R18 | Positive | Happy Path | Packing list Roll A = 10m; nhập thực nhận = 12m | 1. Nhập SL = 12m 2. Xác nhận | Ghi nhận 10m theo packing list; 2m dư sinh ADJ tự động (cần Dev confirm) | Explicit từ PDF v2.17 R18 | ⏳ |
| TC-PL-022 | App — SL thực nhận < SL packing list → ghi nhận theo SL thực | R18 | Positive | Happy Path | Packing list Roll A = 10m; nhập thực nhận = 8m | 1. Nhập SL = 8m 2. Xác nhận | Ghi nhận 8m; Nhận lệch = 8 - 10 = -2m | Explicit từ PDF v2.17 R18 | ⏳ |
| TC-PL-023 | Trang quản lý Packing list — hiển thị đúng cột file import | R13 | Positive | Happy Path | Đã import Packing list thành công | 1. Vào Menu Inbound / Packing list PO 2. Xem listing | Listing hiển thị đầy đủ cột tương ứng file import (PO code, SKU, Roll code, Batch code, Qty, ...) | Explicit từ PDF v2.17 R13 | ⏳ |
| TC-PL-024 | Trang Packing list — xóa nhiều dòng cùng lúc (PO chưa Received) | R13 | Positive | Happy Path | PO vải chưa có ASN Received | 1. Chọn nhiều dòng 2. Nhấn Xóa | Các dòng được xóa khỏi Packing list | Explicit từ PDF v2.17 R13 | ⏳ |
| TC-PL-025 | Ghi nhận thông tin sau khi nhận từng cuộn vải | R20 | Positive | Happy Path | Đã nhận cuộn vải Roll A | 1. Xem chi tiết sau khi nhận 2. Kiểm tra thông tin hiển thị | Ghi nhận đủ: Mã cuộn, Nhóm UID, Hình ảnh, Số lô, SL yêu cầu, SL thực nhận, Nhận lệch, HSD | Explicit từ PDF v2.17 R20 | ⏳ |
| TC-PL-026 | PO đã Receiving — import thêm packing list auto Approved | R8 | Positive | State Transition | PO vải đã chuyển sang Receiving | 1. Import Packing list mới cho PO đang Receiving | Packing list mới tự động Approved (không qua Waiting) | Explicit từ PDF v2.17 R8 | ⏳ |
| TC-PL-027 | Validate Roll code trống trong file import | R2 | Negative | Error Guessing | File import có dòng Roll code bỏ trống | 1. Upload file có Roll code trống | Lỗi "Dòng N – Mã cuộn không được để trống" | Explicit từ PDF v2.17 R2 | ⏳ |

## 🚫 Test Cases Lỗi Thời (Deprecated)

| Test ID | Tiêu đề | Lý do deprecated | Ngày | Nguồn |
|:--------|:--------|:-----------------|:-----|:------|
| — | — | — | — | — |

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 21:49:34 | v1.1 | Loại TC-PL-010/020 vì boundary suy diễn; chuyển câu hỏi về Feature questions; đổi cột nguồn về `Nguồn` | [[WIKI_RULES]] |
| 2026-05-23 00:20:00 | v1.0 | Khởi tạo Test Suite từ Feature Spec v1.0 — 27 test cases | [[wiki/project_hasaki/features/hasaki_receiving_packing_list\|hasaki_receiving_packing_list]] |
