---
aliases: [Inbound Shipment Hasaki, Nhận hàng PO Web, hasaki-receiving-inbound]
tags: [qa/requirement, qa/feature-group/receiving-po]
status: Draft
created: 2026-05-23
updated: 2026-05-23
feature: hasaki_receiving_inbound_shipment
project: project_hasaki
source_version: v2.17
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Inbound Shipment & ASN — Web Portal (Hasaki WMS)

## Tổng quan
- **Mã tính năng:** hasaki_receiving_inbound_shipment
- **Feature:** Quản lý Inbound Shipment & ASN trên Web WMS
- **Mô tả ngắn:** Màn hình quản lý danh sách phiếu nhập kho (Inbound Shipment) và phiên nhận hàng (ASN) trên web portal WMS, bao gồm filter nâng cao, thông tin đồng kiểm, trạng thái WMS riêng, theo dõi thời gian nhận hàng và giải trình PO bị treo.
- **Source chính:** `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.pdf` — version 2.17 (cập nhật 17-05-2026)
- **Đối tượng sử dụng (Actors):** Quản lý kho (WMS user), QA kiểm kho
- **Test Suite tương ứng:** [[wiki/project_hasaki/test_suites/test_hasaki_receiving_inbound_shipment|test_hasaki_receiving_inbound_shipment]]
- **Mối quan hệ:**
  - ➡️ [[wiki/project_hasaki/features/hasaki_receiving_po_app|#2 App PO Receiving]] — PO/ASN trên web là đầu vào cho luồng nhận hàng trên App
  - ➡️ [[wiki/project_hasaki/features/hasaki_receiving_vas|#3 VAS]] — ASN kết thúc phiên nhận → tự sinh VAS
  - ➡️ [[wiki/project_hasaki/features/hasaki_receiving_packing_list|#4 Packing List]] — PO vải cần có Packing List Approved trước khi nhận
  - ℹ️ [[wiki/project_hasaki/features/hasaki_qc_setup|#5 QC Setup]] / [[wiki/project_hasaki/features/hasaki_qc_evaluation|#6 QC Evaluation]] — PO Sample phải QC pass trước khi cho phép nhận PO Gốc (max 30% lần đầu)

---

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | PDF | `07062_Receiving_PO_Docs_ver2.17.pdf` | v2.17 | ✅ Hiện hành |
| 2 | Figma | Figma Receiving PO Update (URL nội bộ) | — | ✅ Hiện hành |
| 3 | Workflow | Drive Hasaki (URL nội bộ) | — | ✅ Hiện hành |

---

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Filter "Đồng kiểm / Check of goods" (Yes/No) trong More Filter của trang Inbound Shipment | Functional | High | ✅ | PDF v2.17, mục Inbound Shipment Filter |
| R2 | Filter "Đủ điều kiện nhận / Eligible to receive" (Yes/No) trong More Filter | Functional | High | ✅ | PDF v2.17, mục Inbound Shipment Filter |
| R3 | Filter "Trạng thái WMS / WMS Status" (multi-select: Open/Receiving/Received/Completed/Canceled) — chỉ áp dụng cho Type = PO | Functional | High | ✅ | PDF v2.17, mục Inbound Shipment Filter |
| R4 | Listing hiển thị cột "Đồng kiểm / Check of goods" — lấy từ lựa chọn khi user scan nhận PO | Functional | High | ✅ | PDF v2.17, mục Inbound Shipment Listing |
| R5 | Listing hiển thị cột "Đủ điều kiện nhận / Eligible to receive" (Yes/No) | Functional | High | ✅ | PDF v2.17, mục Inbound Shipment Listing |
| R6 | Listing hiển thị cột "Mô tả / Description" — lý do khi PO không đủ điều kiện nhận | Functional | High | ✅ | PDF v2.17, mục Inbound Shipment Listing |
| R7 | Listing hiển thị cột "Trạng thái / Status" mapping 2 chiều giữa Inside và WMS; hỗ trợ chọn nhiều | Functional | High | ✅ | PDF v2.17, mục Status Mapping |
| R8 | Listing hiển thị cột "Trạng thái WMS / WMS Status" — status riêng của WMS, chỉ cho Type=PO | Functional | High | ✅ | PDF v2.17, mục WMS Status |
| R9 | PO có WMS Status = "Receiving" hiển thị thêm thời gian đã bao lâu chưa hoàn thành nhận hàng (tính từ khi bắt đầu scan) | Functional | Medium | ✅ | PDF v2.17, ghi chú Status Receiving |
| R10 | Inbound Shipment Detail bổ sung header: "Đủ điều kiện nhận / Eligible to receive" và "Mô tả / Description" | Functional | High | ✅ | PDF v2.17, mục Inbound Shipment Detail |
| R11 | Inbound Shipment Detail — danh sách sản phẩm đổi tên và bổ sung cột: Qty confirm (SL xác nhận), Qty received (SL đã nhận), Qty missing (SL thiếu = confirm - received) | Functional | High | ✅ | PDF v2.17, mục Inbound Shipment Detail |
| R12 | Inbound Shipment Detail — mục "Giải trình lý do treo PO": ô Comment (luôn hiển thị, button Thêm), bảng gồm No / Content / Created by / Created date; sắp xếp mới nhất trước | Functional | Medium | ✅ | PDF v2.17, mục Giải trình lý do treo PO |
| R13 | ASN Filter: bổ sung/cập nhật thứ tự các trường — ASN number, Inbound shipment, Inbound source, Outbound order, Outbound source, Warehouse (multi-select, gợi ý 3 ký tự), SKU/Barcode, Type (multi-select), Owner (multi-select), Status (multi-select), Check of goods (Yes/No), From date/To date | Functional | High | ✅ | PDF v2.17, mục ASN Filter |
| R14 | ASN Listing: bổ sung 2 tùy chọn in biên bản — "In tất cả sản phẩm" (mặc định: chỉ thiếu/SPKPH) và "Thiết lập khổ giấy" (A5 / In Bill, lưu theo máy local) | Functional | Medium | ✅ | PDF v2.17, mục ASN Listing |
| R15 | ASN Listing: các cột bao gồm ASN number, Warehouse, Type, Inbound shipment, Inbound source, Outbound order, Outbound source, Owner, Check of goods, Camera code, Location code, Cart code, Created date, Updated date, Status, Action | Functional | High | ✅ | PDF v2.17, mục ASN Listing |
| R16 | ASN Listing Action — Nút ReOpen: chuyển ASN từ "Receiving" về "Open" và xóa nhân viên khỏi ASN; chỉ hiển thị khi Status = Receiving VÀ chưa scan item nào | Functional | Medium | ✅ | PDF v2.17, mục ASN Listing Action |
| R17 | ASN Listing Action — Nút In biên bản: chỉ hiển thị khi Status = Receiving hoặc Received | Functional | Medium | ✅ | PDF v2.17, mục ASN Listing Action |
| R18 | ASN Listing Action — Nút xem biên bản giao hàng đã upload | Functional | Low | ✅ | PDF v2.17, mục ASN Listing Action |
| R19 | ASN Detail — bổ sung thêm thông tin header: Đồng kiểm, Camera, Mã vị trí | Functional | Medium | ✅ | PDF v2.17, mục ASN Detail |
| R20 | ASN Detail — danh sách sản phẩm: SKU, Barcode, Product name, Qty confirm, Qty received (theo phiên), Qty missing (còn lại), Location, Description (lý do thiếu từ App), Status; bổ sung Group UID (update 16-09-2025) | Functional | High | ✅ | PDF v2.17, mục ASN Detail |

---

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User đã đăng nhập WMS với quyền truy cập module Inbound.
- PO đã được tạo trên hệ thống Inside và đồng bộ qua WMS.

---

### Luồng chuẩn (Happy Path) — Xem danh sách Inbound Shipment

1. User vào menu **Inbound / Inbound Shipment**.
2. Hệ thống hiển thị danh sách Inbound Shipment với các cột chuẩn kèm cột mới: Check of goods, Eligible to receive, Description, Status (Inside mapping), WMS Status.
3. User mở **More Filter** và chọn filter "WMS Status" = Receiving.
4. Hệ thống lọc danh sách; với mỗi PO có WMS Status = Receiving, hiển thị thêm thời gian đã bao lâu chưa hoàn thành nhận hàng.
5. User click vào một PO để xem chi tiết.

### Luồng chuẩn (Happy Path) — Xem Inbound Shipment Detail

1. Màn hình detail hiển thị header bổ sung: **Eligible to receive** và **Description**.
2. Danh sách sản phẩm hiển thị cột: **Qty confirm** (SL theo PO), **Qty received** (SL đã scan), **Qty missing** (Qty confirm - Qty received).
3. Section **"Giải trình lý do treo PO"** luôn hiển thị ô Comment và button "Thêm".

### Luồng chuẩn (Happy Path) — Thêm giải trình PO bị treo

1. User ở màn hình Inbound Shipment Detail của PO giao trong ngày chưa chuyển trạng thái "Received".
2. User nhập nội dung vào ô Comment và nhấn **Thêm**.
3. Hệ thống lưu comment với email Hasaki và thời gian tạo.
4. Comment xuất hiện đầu bảng (sắp xếp giảm dần theo thời gian tạo).

### Luồng chuẩn (Happy Path) — ReOpen ASN

1. User ở màn hình ASN Listing, thấy ASN có Status = Receiving và chưa scan item nào.
2. User click nút **ReOpen**.
3. Hệ thống hiển thị xác nhận: "Do you want to ReOpen for ticket ASN [mã ASN]?"
4. User xác nhận → ASN chuyển về Status = Open, nhân viên được xóa khỏi ASN.

### Luồng chuẩn (Happy Path) — In biên bản nhận hàng ASN

1. User ở ASN Listing hoặc ASN Detail, ASN có Status = Receiving hoặc Received.
2. User click nút **In biên bản**.
3. Hệ thống hiển thị tùy chọn: in tất cả sản phẩm hay chỉ sản phẩm thiếu/SPKPH; chọn khổ giấy A5 hoặc In Bill (lưu theo máy local).
4. Hệ thống render biên bản theo template tương ứng.

---

### Luồng rẽ nhánh (Alternative Paths)

- **Alt-Flow 1 — PO đủ điều kiện nhận:** Cột Eligible to receive = Yes, Description trống.
- **Alt-Flow 2 — PO có đồng kiểm:** Cột Check of goods = Yes (lấy từ lựa chọn khi scan PO trên App).
- **Alt-Flow 3 — PO có nhiều phiên nhận:** Qty received trong ASN Detail chỉ ghi nhận từng phiên; Qty missing = số còn thiếu còn lại sau phiên hiện tại.
- **Alt-Flow 4 — In biên bản khổ In Bill:** Thông tin Số hoá đơn lấy từ cột "Taxcode" trên Inside; có thể trùng nếu là PO gift và PO gốc.

---

### Luồng ngoại lệ (Exception Paths)

- **Exc-Flow 1 — PO không đủ điều kiện nhận:** Eligible to receive = No, Description hiển thị lý do tương ứng (xem bảng Error Messages).
- **Exc-Flow 2 — ASN Status không phải Receiving/Received:** Nút in biên bản ẩn.
- **Exc-Flow 3 — ASN Status = Receiving nhưng đã scan ít nhất 1 item:** Nút ReOpen ẩn.
- **Exc-Flow 4 — Filter WMS Status cho Type ≠ PO:** Filter WMS Status không áp dụng / không hiển thị kết quả.

---

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------|:---------|:----------|:-------------------------------|
| WMS Status (filter) | Multi-select | Không | Chỉ áp dụng cho Type = PO. Giá trị: Open / Receiving / Received / Completed / Canceled |
| Check of goods | Yes / No | — | Lấy từ lựa chọn của user khi scan nhận PO trên App; không tự động tính |
| Eligible to receive | Yes / No | — | Tự động tính theo điều kiện nghiệp vụ; xem bảng Description |
| WMS Status (listing) | Text | — | Chỉ hiển thị cho Type = PO; là status riêng của WMS, khác với cột Status (Inside mapping) |
| Thời gian chờ (Receiving) | Thời lượng (ví dụ: "2h 30m") | — | Chỉ hiển thị khi WMS Status = Receiving; tính từ thời điểm user scan PO để nhận trên App |
| Qty confirm | Số nguyên | — | Bằng SL xác nhận theo PO (không thay đổi sau khi nhận) |
| Qty received | Số nguyên | — | Tổng SL đã scan nhận theo tất cả ASN của PO |
| Qty missing | Số nguyên | — | = Qty confirm − Qty received |
| Comment (giải trình) | Text | Không | Luôn hiển thị button "Thêm" ở mọi status của PO; sắp xếp mới nhất lên đầu |
| ASN — Warehouse filter | Multi-select, gợi ý từ 3 ký tự | Không | Load danh sách kho theo location và phân quyền user |
| ASN — Khổ giấy in | A5 / In Bill | — | Lưu theo máy local; mặc định A5 nếu chưa chọn |

**Mapping Status Inside ↔ WMS:**

| Inside Status | Chiều | WMS Status |
|:-------------|:-----:|:-----------|
| Verified | → | Mới / Open |
| Receiving | ← | Đang nhận hàng / Receiving |
| Received | ← | Đã nhận hàng / Received |
| Cancel | → | Đã huỷ / Canceled |

---

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Ngữ cảnh | Thông báo (VN) | Thông báo (EN) |
|:---------|:--------------|:---------------|
| PO không đủ điều kiện — chưa xác nhận | PO chưa được xác nhận | PO not verified |
| PO không đủ điều kiện — chưa duyệt | PO chưa được duyệt | PO not approved |
| PO không đủ điều kiện — chưa xác nhận hoá đơn | PO chưa được xác nhận hoá đơn | PO not yet verified invoice |
| PO không đủ điều kiện — SKU tester chưa khai báo SKU gốc | SKU tester [SKU] chưa khai báo SKU gốc | SKU Tester [SKU] does not have original SKU |
| ReOpen ASN | Bạn có muốn ReOpen cho phiếu ASN [mã]? | Do you want to ReOpen for ticket ASN [mã]? |

---

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01: Hiển thị filter WMS Status trên Inbound Shipment**
  - **Given:** User đang ở trang Inbound Shipment, mở More Filter
  - **When:** User thấy filter "WMS Status"
  - **Then:** Filter hiển thị các giá trị Open / Receiving / Received / Completed / Canceled; hỗ trợ chọn nhiều; chỉ lọc cho Type = PO

- **AC-02: Hiển thị thời gian chờ cho PO đang nhận**
  - **Given:** Có PO với WMS Status = Receiving trong danh sách
  - **When:** User xem listing
  - **Then:** Cột WMS Status hiển thị thêm thời gian đã bao lâu chưa hoàn thành (tính từ khi bắt đầu scan)

- **AC-03: Hiển thị Eligible to receive = No + Description**
  - **Given:** PO chưa được duyệt
  - **When:** User xem listing Inbound Shipment
  - **Then:** Cột "Eligible to receive" = No; cột "Description" = "PO not approved"

- **AC-04: Qty confirm / received / missing trong Inbound Shipment Detail**
  - **Given:** PO có 10 SKU A cần nhận, đã nhận 7
  - **When:** User mở Inbound Shipment Detail
  - **Then:** Qty confirm = 10, Qty received = 7, Qty missing = 3

- **AC-05: Thêm comment giải trình PO bị treo**
  - **Given:** PO giao trong ngày chưa chuyển Received
  - **When:** User nhập comment và nhấn "Thêm"
  - **Then:** Comment lưu thành công với email Hasaki và thời gian tạo; hiển thị đầu bảng (mới nhất trước)

- **AC-06: ReOpen ASN**
  - **Given:** ASN có Status = Receiving, chưa scan item nào
  - **When:** User click ReOpen và xác nhận
  - **Then:** ASN chuyển về Status = Open; nhân viên bị xóa khỏi ASN

- **AC-07: Nút ReOpen ẩn khi đã scan item**
  - **Given:** ASN có Status = Receiving và đã scan ít nhất 1 item
  - **When:** User xem ASN Listing
  - **Then:** Nút ReOpen không hiển thị

- **AC-08: In biên bản theo khổ giấy**
  - **Given:** ASN có Status = Receiving hoặc Received
  - **When:** User chọn khổ "In Bill" và click in biên bản
  - **Then:** Biên bản render theo template In Bill; lần sau mở lại vẫn nhớ lựa chọn "In Bill"

- **AC-09: ASN Detail hiển thị Group UID**
  - **Given:** ASN có SKU nhận theo Group UID
  - **When:** User mở ASN Detail
  - **Then:** Cột Group UID hiển thị thông tin đã scan

- **AC-10: Filter ASN theo Warehouse gợi ý từ 3 ký tự**
  - **Given:** User đang ở filter ASN, ô Warehouse
  - **When:** User nhập ít hơn 3 ký tự
  - **Then:** Hệ thống không gợi ý; khi nhập đủ 3 ký tự, dropdown hiển thị kho phù hợp theo phân quyền

---

## ❓ Câu hỏi chưa rõ

- [ ] ❓ **R3 / WMS Status filter:** Filter bao gồm "Completed" nhưng bảng WMS Status trong listing chỉ có 4 giá trị (Open/Receiving/Received/Canceled), không có "Completed". Completed có tồn tại như một WMS Status không? Cần xác nhận với Dev.
- [ ] ❓ **R9 — Thời gian chờ:** Format hiển thị cụ thể là gì? (VD: "2h 30m", "150 phút", hay tooltip?) Figma cần xem thêm.
- [ ] ❓ **R12 — Giải trình:** Button "Thêm" luôn hiển thị ở "bất kỳ status nào" — kể cả khi PO đã Canceled? Có cần restrict không?
- [ ] ❓ **Inbound Shipment Detail — Qty received:** Tổng theo tất cả ASN hay theo từng ASN của PO? (Spec ghi "tổng số lượng đã scan nhận theo ASN" — cần làm rõ nếu PO có nhiều ASN)
- [ ] ❓ **ASN Listing — Action button xem biên bản giao hàng:** Điều kiện hiển thị là gì? (Spec chỉ nói "xem biên bản giao hàng mà user upload lên khi nhận hàng cho PO")
- [ ] ❓ **R11 — Boundary Qty missing khi nhận đủ:** Trường hợp nhận đủ thì `Qty missing = 0` đã được hệ thống xác nhận chính thức chưa, hay chỉ là cách hiểu theo công thức?
- [ ] ❓ **R11/R18 — Qty missing khi nhận dư:** Nếu PO vải cho phép nhận dư, `Qty missing` có thể âm hay bị chặn ở 0? Cần rule hiển thị chính thức.

---

## 📝 Thay đổi so với version cũ

| # | Nội dung thay đổi | Version cũ | Version mới | Ảnh hưởng TC |
|:--|:------------------|:----------|:-----------|:-------------|
| 1 | Bỏ thông tin "Đồng kiểm" khỏi Inbound Shipment → chuyển sang ASN | v1.2 (07-10-2024) | v2.17 | Cập nhật TC filter Inbound Shipment |
| 2 | Bổ sung cột Qty received, Qty missing trong Inbound Shipment Detail | v1.2 (07-10-2024) | v2.17 | TC mới về hiển thị SL |
| 3 | Bổ sung mục "Giải trình lý do treo PO" | v1.2 | v2.17 | TC mới về comment |
| 4 | ASN Detail bổ sung Group UID (16-09-2025) | v2.11 | v2.17 | TC mới về Group UID |
| 5 | Import packing list, nhận SKU vải, nhiều user nhận cùng lúc, PO sample | v2.13–v2.16 | v2.17 | Nằm trong Feature riêng |

---

## Test Coverage
| Requirement | Test Case(s) | Status |
|:-----------|:------------|:-------|
| R1 | _(chờ thiết kế)_ | ⏳ |
| R2 | _(chờ thiết kế)_ | ⏳ |
| R3 | _(chờ thiết kế)_ | ⏳ |
| R4 | _(chờ thiết kế)_ | ⏳ |
| R5 | _(chờ thiết kế)_ | ⏳ |
| R6 | _(chờ thiết kế)_ | ⏳ |
| R7 | _(chờ thiết kế)_ | ⏳ |
| R8 | _(chờ thiết kế)_ | ⏳ |
| R9 | _(chờ thiết kế)_ | ⏳ |
| R10 | _(chờ thiết kế)_ | ⏳ |
| R11 | _(chờ thiết kế)_ | ⏳ |
| R12 | _(chờ thiết kế)_ | ⏳ |
| R13 | _(chờ thiết kế)_ | ⏳ |
| R14 | _(chờ thiết kế)_ | ⏳ |
| R15 | _(chờ thiết kế)_ | ⏳ |
| R16 | _(chờ thiết kế)_ | ⏳ |
| R17 | _(chờ thiết kế)_ | ⏳ |
| R18 | _(chờ thiết kế)_ | ⏳ |
| R19 | _(chờ thiết kế)_ | ⏳ |
| R20 | _(chờ thiết kế)_ | ⏳ |

---

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 21:49:34 | v1.1 | Bổ sung câu hỏi boundary Qty missing sau khi loại test case suy diễn khỏi Test Suite | [[wiki/project_hasaki/test_suites/test_hasaki_receiving_inbound_shipment\|test_hasaki_receiving_inbound_shipment]] |
| 2026-05-23 00:00:00 | v1.0 | Khởi tạo Feature Spec từ PDF v2.17 — Inbound Shipment & ASN Web | `07062_Receiving_PO_Docs_ver2.17.pdf` |

## ?? Impact Analysis & Regression Proposal

| Th?nh ph?n b? ?nh h??ng | M?c ?? | H?nh ??ng ?? xu?t |
|:------------------------|:-------|:------------------|
| Test Suites li?n quan | High | Khi requirement/answer thay ??i, c?p nh?t traceability tr??c r?i sinh/ch?y l?i test cases li?n quan |
| KANBAN TC count | Medium | ??ng b? l?i s? TC active sau m?i l?n th?m/x?a test case |
| Test Plan | Medium | R? l?i scope regression n?u c? thay ??i AC/lu?ng nghi?p v? |
