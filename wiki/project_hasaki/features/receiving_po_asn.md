---
aliases: [ASN, Advanced Shipment Notice, Phiên nhận hàng]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: receiving_po_asn
project: project_hasaki
source_version: "07062 ver2.17"
partial_read: false
partial_read_note: ""
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: ASN – Quản lý Advanced Shipment Notice

## Tổng quan
- **Mã tính năng:** receiving_po_asn
- **Feature:** ASN Management (Web)
- **Mô tả ngắn:** Màn hình quản lý danh sách và chi tiết ASN (Advanced Shipment Notice) trên Web WMS — bổ sung filter, listing, biên bản nhận hàng và Group UID cho vải.
- **Source chính:** `07062_Receiving_PO_Docs_ver2.17.md` – section "ASN – Updated" và "ASN detail – Updated"
- **Đối tượng sử dụng (Actors):** Warehouse staff, Warehouse manager
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[receiving_po_inbound_shipment]] — Inbound Shipment sinh ra ASN
  - ➡️ [[receiving_po_vas]] — ASN received sinh ra VAS
  - ➡️ [[receiving_po_app]] — App scan PO tạo phiên ASN

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07062_Receiving_PO_Docs_ver2.17.md | ver2.17 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Không có API explicit | N/A |

## Phân rã Requirement

### Filter – ASN Listing
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-ASN-01 | Filter Mã ASN — tìm chính xác theo mã nhập vào | Functional | Medium | ✅ | 07062#358 |
| R-ASN-02 | Filter Kho — load danh sách kho theo location và phân quyền; hỗ trợ chọn nhiều, gợi ý từ 3 ký tự | Functional | High | ✅ | 07062#366-368 |
| R-ASN-03 | Filter SKU, Barcode — tìm theo SKU hoặc Barcode trong chi tiết ASN | Functional | Medium | ✅ | 07062#369-370 |
| R-ASN-04 | Filter Loại — giá trị: Purchase order, Customer return, Internal transfer, Adjustment; hỗ trợ chọn nhiều | Functional | High | ✅ | 07062#371-377 |
| R-ASN-05 | Filter Người sở hữu — giá trị: Hasaki Cosmetics, Hasaki WMS, Hasaki OMS; hỗ trợ chọn nhiều | Functional | Medium | ✅ | 07062#378-383 |
| R-ASN-06 | Filter Trạng thái — giá trị: Mới/Open, Đang nhận hàng/Receiving, Đã nhận hàng/Received, Đã huỷ/Canceled; hỗ trợ chọn nhiều | Functional | High | ✅ | 07062#384-390 |
| R-ASN-07 | Filter Đồng kiểm — giá trị: Yes/No | Functional | Medium | ✅ | 07062#396 |

### Listing – ASN
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-ASN-08 | Tuỳ chọn in "Tất cả sản phẩm / Print all product" — mặc định chỉ in SKU có khai báo thiếu hoặc SPKPH; nếu tick thì in hết | Functional | Medium | ✅ | 07062#403-406 |
| R-ASN-09 | Tuỳ chọn "Thiết lập khổ giấy / Set paper size" — giá trị: A5 (mặc định) và In Bill; lưu theo máy local | Functional | Low | ✅ | 07062#408-415 |
| R-ASN-10 | Listing gồm các cột: Mã ASN, Kho, Loại, Mã phiếu nhập, Phiếu nhập nguồn mapping, Mã phiếu xuất, Phiếu xuất nguồn mapping, Người sở hữu, Đồng kiểm, Mã camera, Mã vị trí, Mã giỏ, Ngày tạo, Người tạo, Ngày cập nhật, Trạng thái, Thao tác | Functional | High | ✅ | 07062#417-441 |
| R-ASN-11 | Action ReOpen — chỉ hiện khi status = Receiving VÀ user chưa scan nhận item nào; reopen về Open và xoá nhân viên ra khỏi ASN | Functional | High | ✅ | 07062#441-449 |
| R-ASN-12 | Confirm message ReOpen: "Do you want to ReOpen for ticket ASN [code]?" | Functional | High | ✅ | 07062#448-449 |
| R-ASN-13 | Action in biên bản — chỉ hiện khi status = Receiving hoặc Received | Functional | Medium | ✅ | 07062#450-454 |
| R-ASN-14 | Action xem biên bản giao hàng upload — xem biên bản mà user upload khi nhận hàng cho PO | Functional | Low | ✅ | 07062#453-454 |

### Chi tiết ASN
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-ASN-15 | Thông tin chung bổ sung: Đồng kiểm, Camera, Mã vị trí | Functional | Medium | ✅ | 07062#469-476 |
| R-ASN-16 | Danh sách sản phẩm — cột SL xác nhận (Qty confirm): số lượng SKU theo PO; nếu nhiều phiên nhận vẫn ghi nhận theo số lượng PO | Functional | High | ✅ | 07062#482-485 |
| R-ASN-17 | Cột SL thực nhận (Qty received): theo từng phiên nhận | Functional | High | ✅ | 07062#485-487 |
| R-ASN-18 | Cột SL thiếu (Qty missing): số lượng còn thiếu theo từng phiên (= SL PO − SL nhận phiên đó); ví dụ SKU A PO 10, lần 1 nhận 5 → thiếu 5, lần 2 nhận 3 → thiếu 2 | Functional | High | ✅ | 07062#488-495 |
| R-ASN-19 | Cột Vị trí / Location — mã bin user scan nhận cho Shop 170 và Kho 170; với Shop mặc định vào location mặc định | Functional | Medium | ✅ | 07062#496-499 |
| R-ASN-20 | Cột Mô tả / Description — hiện thông tin khai báo lý do thiếu: Lý do thiếu, Tình trạng hàng hoá, Nhà cung cấp giao bù, Ghi chú | Functional | Medium | ✅ | 07062#499-508 |
| R-ASN-21 | Update 16-09-2025: bổ sung thông tin Group UID đã nhận cho chi tiết ASN | Functional | High | ✅ | 07062#512-516 |

### Biên bản nhận hàng
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-ASN-22 | Template A5: biên bản nhận hàng PO theo ASN | Functional | Medium | ✅ | 07062#455 |
| R-ASN-23 | Template In Bill: thông tin Số hoá đơn lấy từ cột "Taxcode" trên Inside; Taxcode có thể trùng nếu là PO gift và PO gốc | Functional | Medium | ✅ | 07062#462-464 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User đã login WMS với quyền ASN.
- Đã có ASN được tạo từ phiên nhận PO.

### Luồng chuẩn (Happy Path)
1. User vào Menu: Inbound / ASN.
2. User filter theo Kho, Loại, Trạng thái.
3. Danh sách ASN hiển thị với các cột đầy đủ.
4. User chọn ASN để xem chi tiết (qty confirm / received / missing, location, description).
5. User in biên bản nếu cần (chọn khổ A5 hoặc In Bill).

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 – ReOpen ASN:** Status = Receiving, chưa scan item nào → user chọn ReOpen → confirm → ASN về Open, xoá nhân viên.
- **Alt-Flow 2 – In biên bản:** Status = Receiving/Received → user chọn in, tuỳ chọn khổ giấy được lưu theo máy local.

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1:** ReOpen khi đã scan ít nhất 1 item → button ReOpen không hiển thị.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| Qty missing | Số | Auto | = Qty PO − Qty received (tính theo từng phiên) |
| Set paper size | Enum (A5/In Bill) | Không | Lưu local, áp dụng cho tất cả lần sau trên cùng máy |
| ReOpen | Action | — | Chỉ khi status = Receiving VÀ chưa có item nào scan |
| Taxcode (In Bill) | Text | Auto | Lấy từ Inside; có thể trùng giữa PO gift và PO gốc |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
| Thao tác | Thông báo EN |
|:---------|:------------|
| ReOpen ASN | Do you want to ReOpen for ticket ASN [code]? |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-ASN-01: Filter Loại đa chọn hoạt động đúng**
  - **Given:** User ở màn hình ASN listing
  - **When:** User chọn filter Loại = "Purchase order" và "Customer return"
  - **Then:** Chỉ hiển thị ASN thuộc 2 loại đó

- **AC-ASN-02: ReOpen ASN chỉ hiện khi đủ điều kiện**
  - **Given:** ASN có status = Receiving
  - **When:** User chưa scan nhận bất kỳ item nào
  - **Then:** Button ReOpen hiển thị; sau xác nhận ASN về Open và xoá nhân viên

- **AC-ASN-03: ReOpen ASN không hiện khi đã scan**
  - **Given:** ASN có status = Receiving VÀ đã scan ít nhất 1 item
  - **When:** User xem row ASN này trong listing
  - **Then:** Button ReOpen không hiển thị

- **AC-ASN-04: Qty missing tính đúng theo từng phiên**
  - **Given:** SKU A PO qty = 10; phiên nhận 1 nhận 5, phiên nhận 2 nhận 3
  - **When:** User xem chi tiết từng ASN
  - **Then:** Phiên 1 qty missing = 5; phiên 2 qty missing = 2

- **AC-ASN-05: Khổ giấy lưu local**
  - **Given:** User chọn khổ giấy "In Bill"
  - **When:** User in biên bản lần tiếp theo trên cùng máy
  - **Then:** Hệ thống tự chọn lại "In Bill" mà không cần chọn lại

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-ASN-01 | R-ASN-09 | "Lưu theo máy tính local" — cơ chế lưu là localStorage / cookie / user setting? | Dev | Open | | | |
| Q-ASN-02 | R-ASN-21 | Group UID hiển thị trong chi tiết ASN gồm những thông tin cụ thể nào (cột nào)? Source chỉ nói "bổ sung thông tin Group UID" | BA | Open | | | |

## 📝 Thay đổi so với version cũ
| Change ID | Loại | Nội dung | Version cũ | Version mới | R/AC ảnh hưởng | Trạng thái |
|:----------|:-----|:---------|:-----------|:------------|:---------------|:-----------|
| CHG-ASN-01 | Add | Bổ sung filter: Kho, SKU/Barcode, Loại, Owner, Status, Đồng kiểm | <ver | ver2.17 | R-ASN-01~07 | Draft |
| CHG-ASN-02 | Add | Tuỳ chọn in tất cả SP và khổ giấy | <ver | ver2.17 | R-ASN-08~09 | Draft |
| CHG-ASN-03 | Add | Group UID trong chi tiết ASN | ver trước 16-09-2025 | ver2.17 | R-ASN-21 | Draft |

## 🔎 Impact Analysis & Regression Proposal
| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:-----|
| CHG-ASN-01 | receiving_po_asn | — | Add | Filter ASN | Blocked by Gate 1 |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-ASN-11 / AC-ASN-02 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-ASN-11 / AC-ASN-03 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-ASN-18 / AC-ASN-04 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-ASN-21 | | ❌ Blocked | Chờ Q-ASN-02 |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo spec từ 07062 ver2.17, section ASN | 07062#349-516 |
