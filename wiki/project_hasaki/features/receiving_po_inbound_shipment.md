---
aliases: [Inbound Shipment, Phiếu nhập]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: receiving_po_inbound_shipment
project: project_hasaki
source_version: "07062 ver2.17"
partial_read: false
partial_read_note: ""
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Inbound Shipment – Quản lý danh sách và chi tiết phiếu nhập

## Tổng quan
- **Mã tính năng:** receiving_po_inbound_shipment
- **Feature:** Inbound Shipment (Web)
- **Mô tả ngắn:** Màn hình quản lý danh sách phiếu nhập (Inbound Shipment) và chi tiết phiếu nhập trên Web WMS, bổ sung filter/listing mới và tính năng giải trình lý do treo PO.
- **Source chính:** `07062_Receiving_PO_Docs_ver2.17.md` – section "Inbound Shipment – Updated" và "Inbound shipment detail – Update"
- **Đối tượng sử dụng (Actors):** Warehouse staff, Warehouse manager
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A *(không có API explicit trong source)*
- **Mối quan hệ:**
  - ➡️ [[receiving_po_asn]] — Inbound Shipment liên kết với ASN
  - ➡️ [[receiving_po_app]] — App scan PO tạo ra Inbound Shipment

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07062_Receiving_PO_Docs_ver2.17.md | ver2.17 | ✅ Hiện hành |
| 2 | Link | Figma (old visily): https://app.visily.ai/projects/... | — | ❓ Chưa đọc được |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Không có API explicit | N/A |

## Phân rã Requirement

### Filter – Inbound Shipment Listing
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-IS-01 | Filter "Đồng kiểm / Check of goods" với giá trị Yes/No (move qua trang ASN) | Functional | High | ✅ | 07062#229 |
| R-IS-02 | Filter "Đủ điều kiện nhận / Eligible to receive" với giá trị Yes/No | Functional | High | ✅ | 07062#231 |
| R-IS-03 | Filter "Trạng thái WMS / WMS status" chỉ áp dụng cho Type = PO, gồm: Mới/Open, Đang nhận hàng/Receiving, Đã nhận hàng/Received, Hoàn thành/Completed, Đã huỷ/Canceled; hỗ trợ chọn nhiều | Functional | High | ✅ | 07062#232-240 |

### Listing – Inbound Shipment
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-IS-04 | Cột "Đồng kiểm / Check of goods" — lấy thông tin khi user chọn khi scan nhận PO | Functional | Medium | ✅ | 07062#244-245 |
| R-IS-05 | Cột "Đủ điều kiện nhận / Eligible to receive" — Yes: đủ điều kiện; No: không đủ | Functional | High | ✅ | 07062#246-248 |
| R-IS-06 | Cột "Mô tả / Description" — mô tả lý do không đủ điều kiện nhận; các giá trị: "PO not verified", "PO not approved", "PO not yet verified invoice", "SKU Tester does not have original SKU" | Functional | High | ✅ | 07062#249-262 |
| R-IS-07 | Cột "Trạng thái / Status" — hiển thị đầy đủ status PO từ Inside, mapping: Verified→Open, Receiving→Receiving, Received→Received, Cancel→Canceled; hỗ trợ chọn nhiều | Functional | High | ✅ | 07062#263-271 |
| R-IS-08 | Với Status = Receiving: bổ sung thêm thời gian đã bao lâu chưa hoàn thành nhận hàng (tính từ khi bắt đầu scan PO) | Functional | Medium | ✅ | 07062#272-275 |
| R-IS-09 | Cột "Trạng thái WMS / WMS status" — chỉ dành cho type PO; trạng thái riêng của WMS: Mới/Open, Đang nhận hàng/Receiving, Đã nhận hàng/Received, Đã huỷ/Canceled | Functional | High | ✅ | 07062#276-289 |

### Chi tiết Inbound Shipment
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-IS-10 | Thông tin chung bổ sung: "Đủ điều kiện nhận / Eligible to receive" và "Mô tả / Description" | Functional | Medium | ✅ | 07062#303-307 |
| R-IS-11 | Danh sách sản phẩm: đổi tên "Số lượng" → "Số lượng xác nhận / Qty confirm" (theo inbound) | Functional | Low | ✅ | 07062#312-313 |
| R-IS-12 | Danh sách sản phẩm: bổ sung "Số lượng đã nhận / Qty received" — tổng số lượng đã scan nhận theo ASN | Functional | High | ✅ | 07062#316 |
| R-IS-13 | Danh sách sản phẩm: bổ sung "Số lượng thiếu / Qty missing" = Qty confirm – Qty received | Functional | High | ✅ | 07062#317 |
| R-IS-14 | Tính năng giải trình lý do treo PO: nếu PO giao trong ngày nhưng chưa chuyển "Đã nhận hàng" thì user nhập Comment giải trình; sắp xếp giảm dần theo thời gian tạo | Functional | Medium | ✅ | 07062#319-343 |
| R-IS-15 | Comment section gồm: Nội dung, Người tạo (email HSK), Ngày tạo; Button "Thêm" hiện ở bất kỳ status nào | Functional | Medium | ✅ | 07062#326-342 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User đã login WMS với quyền xem Inbound Shipment.
- PO đã được tạo trên Inside.

### Luồng chuẩn (Happy Path)
1. User vào Menu: Inbound / Inbound Shipment.
2. User áp dụng filter (WMS Status, Eligible to receive, Check of goods, ...).
3. Danh sách hiển thị các cột đã bổ sung.
4. User chọn 1 dòng để xem chi tiết.
5. Màn hình chi tiết hiển thị thông tin chung (eligible, description) và danh sách sản phẩm với qty confirm / qty received / qty missing.

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1:** PO Status = Receiving và đã quá ngày giao — user nhập comment giải trình lý do treo PO.

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1:** PO không đủ điều kiện nhận (No) — cột Mô tả hiển thị lý do cụ thể.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| WMS Status | Enum | Không (filter) | Chỉ áp dụng cho Type = PO |
| Qty missing | Số | Auto | = Qty confirm − Qty received |
| Comment (giải trình) | Text | Không (khi cần giải trình) | Có thể thêm ở bất kỳ status |
| Thời gian treo PO | Duration | Auto | Tính từ thời điểm bắt đầu scan PO |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
*(Không có error message explicit trong source cho section này)*

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-IS-01: Filter WMS Status hoạt động đúng**
  - **Given:** User ở màn hình Inbound Shipment listing
  - **When:** User chọn filter WMS Status = "Đang nhận hàng"
  - **Then:** Chỉ hiển thị các PO có WMS status = Receiving và Type = PO

- **AC-IS-02: Hiển thị thời gian treo PO**
  - **Given:** PO có status = Receiving
  - **When:** User xem listing Inbound Shipment
  - **Then:** Cột Status hiển thị kèm thời gian đã bao lâu chưa hoàn thành (tính từ lúc bắt đầu scan)

- **AC-IS-03: Qty missing tính đúng**
  - **Given:** User xem chi tiết 1 Inbound Shipment
  - **When:** SKU A có Qty confirm = 10, Qty received = 7
  - **Then:** Qty missing hiển thị = 3

- **AC-IS-04: Giải trình lý do treo PO**
  - **Given:** PO giao trong ngày nhưng chưa chuyển "Đã nhận hàng"
  - **When:** User nhập comment và chọn "Thêm"
  - **Then:** Comment được lưu với thông tin người tạo (email HSK) và thời gian tạo

- **AC-IS-05: PO không đủ điều kiện nhận**
  - **Given:** PO có Eligible to receive = No
  - **When:** User xem listing
  - **Then:** Cột Mô tả hiển thị lý do tương ứng (VD: "PO not approved")

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-IS-01 | R-IS-03 | WMS Status "Hoàn thành/Completed" mapping với status nào bên Inside? Source chỉ liệt kê Verified/Receiving/Received/Cancel | BA/Dev | Open | | | |
| Q-IS-02 | R-IS-14 | Điều kiện chính xác để bắt buộc giải trình là gì? "Giao trong ngày nhưng chưa Received" — ngày ở đây là ngày dự kiến giao hay ngày tạo PO? | BA | Open | | | |

## 📝 Thay đổi so với version cũ
| Change ID | Loại | Nội dung | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:-----|:---------|:-----------|:------------|:--------------------------|:-----------|
| CHG-IS-01 | Add | Bổ sung filter Đồng kiểm, Eligible to receive, WMS Status | <ver mới | ver2.17 | R-IS-01~03 | Draft |
| CHG-IS-02 | Add | Bổ sung cột Đồng kiểm, Eligible, Mô tả, WMS status trong listing | <ver mới | ver2.17 | R-IS-04~09 | Draft |
| CHG-IS-03 | Add | Chi tiết: bổ sung Eligible, Description, Qty received, Qty missing | <ver mới | ver2.17 | R-IS-10~13 | Draft |
| CHG-IS-04 | Add | Giải trình lý do treo PO | <ver mới | ver2.17 | R-IS-14~15 | Draft |

## 🔎 Impact Analysis & Regression Proposal
| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:-----|
| CHG-IS-01 | receiving_po_inbound_shipment | — | Add | Filter logic PO | Blocked by Gate 1 |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-IS-01 / AC-IS-01 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-IS-02 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-IS-03 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-IS-14 / AC-IS-04 | | ❌ Chưa tạo | Blocked by Q-IS-02 |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo spec từ 07062 ver2.17, section Inbound Shipment | 07062#222-343 |
