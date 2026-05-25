---
tags: [qa/requirement, qa/feature-group/receiving-po]
status: Draft
created: 2026-05-25
updated: 2026-05-25
feature: receiving_po_inbound_shipment_detail
project: project_hasaki
source_version: v2.17
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Inbound Shipment Detail (Web)

## Tổng quan
- **Mã tính năng:** receiving_po_inbound_shipment_detail
- **Feature:** Chi tiết phiếu nhập — xem thông tin PO, danh sách sản phẩm, giải trình lý do treo PO
- **Mô tả ngắn:** Màn hình chi tiết của một Inbound Shipment — bổ sung thông tin Đủ điều kiện nhận/Mô tả, cập nhật cột danh sách sản phẩm (Qty confirm/received/missing), và tính năng giải trình lý do treo PO.
- **Source chính:** `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.md` — mục "Inbound shipment detail – Update", "Giải trình lý do treo PO"
- **Đối tượng sử dụng (Actors):** Nhân viên kho, Quản lý kho
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** —
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[wiki/project_hasaki/features/receiving_po_inbound_shipment|Inbound Shipment]] — navigate từ listing vào detail

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted from PDF) | `07062_Receiving_PO_Docs_ver2.17.md` | v2.17 | ✅ Hiện hành |
| 2 | Figma | `https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO_Update` | — | ❓ Chưa đọc được |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Thông tin chung bổ sung: Đủ điều kiện nhận (Eligible to receive) | Functional | High | ✅ | v2.17, Inbound shipment detail |
| R2 | Thông tin chung bổ sung: Mô tả (Description) — lý do không đủ điều kiện nếu có | Functional | High | ✅ | v2.17, Inbound shipment detail |
| R3 | Danh sách sản phẩm — đổi tên cột "Số lượng" thành "Số lượng xác nhận" (Qty confirm) — là số lượng confirm theo inbound | Functional | High | ✅ | v2.17, Danh sách sản phẩm |
| R4 | Danh sách sản phẩm — bổ sung cột "Số lượng đã nhận" (Qty received) — tổng số đã scan nhận theo ASN | Functional | High | ✅ | v2.17, Danh sách sản phẩm |
| R5 | Danh sách sản phẩm — bổ sung cột "Số lượng thiếu" (Qty missing) = Qty confirm – Qty received | Functional | High | ✅ | v2.17, Danh sách sản phẩm |
| R6 | Giải trình lý do treo PO: nếu PO giao trong ngày nhưng chưa chuyển "Đã nhận hàng" → user giải trình | Functional | High | ✅ | v2.17, Giải trình lý do treo PO |
| R7 | Giải trình: Button "Thêm" comment hiện ở bất kỳ status nào | Functional | Medium | ✅ | v2.17, Giải trình |
| R8 | Giải trình: Danh sách comment gồm TT (tăng dần), Nội dung, Người tạo (email), Ngày tạo; sắp xếp giảm dần theo thời gian tạo | Functional | Medium | ✅ | v2.17, Giải trình |

## 🔄 Luồng Nghiệp Vụ Chi Tiết

### Luồng chuẩn (Happy Path)
1. User click vào một PO từ danh sách Inbound Shipment
2. Màn hình detail hiển thị thông tin chung (gồm Đủ điều kiện nhận, Mô tả)
3. Danh sách sản phẩm hiển thị với Qty confirm, Qty received, Qty missing
4. Nếu PO bị treo (giao trong ngày chưa hoàn thành), user nhập comment giải trình và nhấn "Thêm"

### Luồng ngoại lệ
- **Exc-Flow 1:** PO đủ điều kiện nhận — cột Mô tả không có giá trị (hoặc rỗng)

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu

| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| Qty missing | Số | — | = Qty confirm – Qty received; có thể âm nếu nhận dư |
| Comment | Text | Không | Không giới hạn độ dài (chưa rõ trong doc) |
| Người tạo | Email | — | Email Hasaki của người nhập comment |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi
- Không có error message explicit trong source cho màn hình này.

## 🏁 Tiêu Chí Nghiệm Thu (BDD)

- **Scenario 1: Qty missing tính đúng**
  - **Given:** PO có Qty confirm = 100, Qty received = 80
  - **When:** User xem detail
  - **Then:** Qty missing = 20

- **Scenario 2: Giải trình treo PO**
  - **Given:** PO giao trong ngày nhưng WMS status = Receiving
  - **When:** User nhập comment và nhấn "Thêm"
  - **Then:** Comment được thêm vào danh sách, hiển thị đúng người tạo và ngày giờ, sắp xếp mới nhất trên cùng

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:--------------|:--------|:-------|:-----------|
| Q-001 | R5 | Qty missing có thể âm (nhận dư) không? Nếu có thì hiển thị như thế nào? | PO/BA | Open |
| Q-002 | R6 | "PO giao trong ngày" — điều kiện xác định "trong ngày" là theo múi giờ nào, theo ngày tạo PO hay ngày hẹn giao? | PO/BA | Open |
| Q-003 | R7 | Comment có giới hạn ký tự không? | PO/Dev | Open |
| Q-004 | — | Figma chưa đọc được — bố cục toàn bộ màn hình detail cần confirm | Designer | Open |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:----------------------|
| CHG-001~003 | Inbound Shipment Detail | — | Add (mới) | — | Q-001, Q-002 |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R1–R8 | — | ❌ Blocked | Chờ Gate 1 |
| R5 (Qty âm) | — | ❌ Blocked | Chờ Q-001 |
| R6 (điều kiện treo) | — | ❌ Blocked | Chờ Q-002 |

## 📅 Changelog
| Thời gian | Version | Nội dung | Nguồn |
|:----------|:--------|:---------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo | Raw ingest |
