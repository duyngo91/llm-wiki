---
tags: [qa/requirement, qa/feature-group/receiving-po]
status: Draft
created: 2026-05-25
updated: 2026-05-25
feature: receiving_po_inbound_shipment
project: project_hasaki
source_version: v2.17
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Inbound Shipment (Web) — Nhận hàng PO

## Tổng quan
- **Mã tính năng:** receiving_po_inbound_shipment
- **Feature:** Inbound Shipment — Quản lý danh sách phiếu nhập hàng PO trên Web
- **Mô tả ngắn:** Cập nhật màn hình Inbound Shipment (Menu: Inbound / Inbound Shipment) — bổ sung filter, cột listing, mapping WMS status, và tính năng giải trình lý do treo PO.
- **Source chính:** `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.md` — mục "Inbound Shipment – Updated" và "Inbound shipment detail – Update"
- **Đối tượng sử dụng (Actors):** Nhân viên kho (Warehouse staff), Quản lý kho
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** —
- **API Spec liên quan:** N/A *(không có API contract explicit trong source)*
- **Mối quan hệ:**
  - ➡️ [[wiki/project_hasaki/features/receiving_po_inbound_shipment_detail|Inbound Shipment Detail]] — click vào row mở detail
  - ➡️ [[wiki/project_hasaki/features/receiving_po_asn|ASN]] — từ Inbound Shipment navigate sang ASN

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted from PDF) | `07062_Receiving_PO_Docs_ver2.17.md` | v2.17 | ✅ Hiện hành |
| 2 | Figma | `https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO_Update` | — | ❓ Chưa đọc được |
| 3 | Workflow | `https://drive.hasaki.vn/f/6fecf6ac99424782b12a/` | — | ❓ Chưa đọc được |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | — | — | Không có API explicit | N/A |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Filter bổ sung: Đồng kiểm (Check of goods) — Giá trị Yes/No, hiển thị trong More filter; chọn Đồng kiểm → move sang trang ASN | Functional | High | ✅ | v2.17, mục Inbound Shipment Filter (line 230-231) |
| R2 | Filter bổ sung: Đủ điều kiện nhận (Eligible to receive) — Giá trị Yes/No, hiển thị trong More filter | Functional | High | ✅ | v2.17, mục Inbound Shipment Filter |
| R3 | Filter bổ sung: Trạng thái WMS (WMS status) — chỉ dùng cho Type = PO, hỗ trợ chọn nhiều, giá trị: Open / Receiving / Received / **Completed** / Canceled | Functional | High | ✅ | v2.17, mục Inbound Shipment Filter (line 235-239) |
| R4 | Listing bổ sung cột: Đồng kiểm (Check of goods) — lấy từ lựa chọn user khi scan nhận PO | Functional | High | ✅ | v2.17, mục Inbound Shipment Listing |
| R5 | Listing bổ sung cột: Đủ điều kiện nhận (Eligible to receive) — Yes/No | Functional | High | ✅ | v2.17, mục Inbound Shipment Listing |
| R6 | Listing bổ sung cột: Mô tả (Description) — mô tả lý do không đủ điều kiện nhận | Functional | Medium | ✅ | v2.17, mục Inbound Shipment Listing |
| R7 | Cột Status hiển thị đầy đủ các status của PO trên Inside, mapping 2 chiều giữa Inside và WMS | Functional | High | ✅ | v2.17, bảng mapping Inside ↔ WMS |
| R8 | WMS Status riêng cho type PO: Open / Receiving / Received / Canceled (không hiển thị ở type khác) | Functional | High | ✅ | v2.17, bảng WMS status |
| R9 | Status Receiving hiển thị thêm thời gian đã bao lâu chưa hoàn thành (tính từ khi bắt đầu scan PO) | Functional | Medium | ✅ | v2.17, mục WMS status |
| R10 | Mô tả lý do không đủ điều kiện nhận: hiển thị đúng theo case (PO chưa xác nhận / PO chưa duyệt / PO chưa xác nhận hoá đơn / SKU Tester chưa khai báo SKU gốc) | Functional | High | ✅ | v2.17, bảng mô tả điều kiện |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User đã đăng nhập WMS với quyền truy cập Inbound
- Tồn tại ít nhất 1 PO trên hệ thống

### Luồng chuẩn (Happy Path)
1. User vào menu Inbound / Inbound Shipment
2. Dùng filter để lọc danh sách PO (có thể filter theo WMS status, Đồng kiểm, Đủ điều kiện nhận)
3. Danh sách hiển thị các cột bao gồm: Đồng kiểm, Đủ điều kiện nhận, Mô tả, Status (WMS + Inside mapping)
4. PO có Status = Receiving hiển thị thêm thời gian chưa hoàn thành
5. User click vào PO để xem detail

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 — PO không đủ điều kiện nhận:** Cột Đủ điều kiện nhận = No, Cột Mô tả hiển thị lý do tương ứng (4 case đã định nghĩa)
- **Alt-Flow 2 — Filter WMS status chỉ hiện với type PO:** Nếu user chọn type khác, filter WMS status không hiển thị hoặc disabled

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1:** Không có PO nào thỏa điều kiện filter → danh sách rỗng, không lỗi

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu

| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| WMS status filter | Select (multi) | Không | Chỉ áp dụng khi Type = PO |
| Đồng kiểm | Yes/No | — | Lấy từ lựa chọn user khi scan PO trên App |
| Đủ điều kiện nhận | Yes/No | — | Tính tự động theo điều kiện hệ thống |
| Status Receiving | Text + duration | — | Duration tính từ thời điểm bắt đầu scan PO |

**Mapping Inside ↔ WMS Status:**

| Inside | WMS |
|:-------|:----|
| Verified | >> Mới / Open |
| Receiving | << Đang nhận hàng / Receiving |
| Received | << Đã nhận hàng / Received |
| Cancel | >> Đã huỷ / Canceled |

**Lý do không đủ điều kiện nhận:**

| VN | EN |
|:---|:---|
| PO chưa được xác nhận | PO not verified |
| PO chưa được duyệt | PO not approved |
| PO chưa được xác nhận hoá đơn | PO not yet verified invoice |
| SKU tester [mã] chưa khai báo SKU gốc | SKU Tester [mã] does not have original SKU |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi
- Không có error message explicit trong source cho màn hình listing.

## 🏁 Tiêu Chí Nghiệm Thu (BDD)

- **Scenario 1: Hiển thị filter WMS status chỉ khi type = PO**
  - **Given:** User ở màn hình Inbound Shipment, chọn Type = PO trong filter
  - **When:** User mở More filter
  - **Then:** Filter "Trạng thái WMS" hiển thị với các giá trị: Open, Receiving, Received, Canceled; hỗ trợ chọn nhiều

- **Scenario 2: Cột Mô tả hiển thị lý do không đủ điều kiện**
  - **Given:** Tồn tại PO có Đủ điều kiện nhận = No
  - **When:** User xem danh sách Inbound Shipment
  - **Then:** Cột Mô tả hiển thị đúng lý do theo case (VN/EN tùy ngôn ngữ)

- **Scenario 3: Status Receiving hiển thị thời gian treo PO**
  - **Given:** PO có WMS Status = Receiving
  - **When:** User xem danh sách
  - **Then:** Status Receiving kèm theo thời gian đã bao lâu chưa hoàn thành (tính từ lúc bắt đầu scan)

- **Scenario 4: Filter Đồng kiểm**
  - **Given:** User ở màn hình Inbound Shipment
  - **When:** User chọn filter Đồng kiểm = Yes
  - **Then:** Danh sách chỉ hiển thị các PO có Đồng kiểm = Yes

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn | Ngày |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:------|:-----|
| Q-001 | R9 | Duration hiển thị status Receiving — format hiển thị là gì? (hh:mm, "X giờ Y phút", "X ngày") | PO/BA | Open | | | |
| Q-002 | R3 | Filter WMS status: khi không chọn type PO thì filter ẩn hoàn toàn hay disabled? | PO/Dev | Open | | | |
| Q-003 | R7 | Status "Completed / Hoàn thành" xuất hiện trong WMS status listing nhưng không có trong bảng mapping Inside↔WMS — mapping của "Completed" là gì? | PO/BA | Open | | | |
| Q-004 | R4-R6 | Figma chưa đọc được — bố cục cột listing cuối cùng và thứ tự cột cần xác nhận theo Figma | Designer | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | R/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:---------------|:-----------|
| CHG-001 | Add | Filter: Đồng kiểm, Đủ điều kiện nhận, WMS status | — | v2.17 | R1, R2, R3 | Draft |
| CHG-002 | Add | Listing: cột Đồng kiểm, Đủ điều kiện nhận, Mô tả | — | v2.17 | R4, R5, R6 | Draft |
| CHG-003 | Add | WMS Status mapping + Receiving duration | — | v2.17 | R7, R8, R9 | Draft |
| CHG-004 | Add | 4 case mô tả không đủ điều kiện nhận | — | v2.17 | R10 | Draft |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:----------------------|
| CHG-001~004 | Inbound Shipment listing | — | Add (mới) | Không có suite cũ | Q-001, Q-002, Q-003 |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R1 | — | ❌ Blocked | Chờ Gate 1 |
| R2 | — | ❌ Blocked | Chờ Gate 1 |
| R3 | — | ❌ Blocked | Chờ Q-002, Gate 1 |
| R4 | — | ❌ Blocked | Chờ Gate 1 |
| R5 | — | ❌ Blocked | Chờ Gate 1 |
| R6 | — | ❌ Blocked | Chờ Gate 1 |
| R7 | — | ❌ Blocked | Chờ Gate 1 |
| R8 | — | ❌ Blocked | Chờ Gate 1 |
| R9 | — | ❌ Blocked | Chờ Q-001, Gate 1 |
| R10 | — | ❌ Blocked | Chờ Gate 1 |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo từ 07062_Receiving_PO_Docs_ver2.17.md | Raw ingest |
