---
aliases: [QC VAS Update, VAS Quality Control]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: quality_control_vas_update
project: project_hasaki
source_version: "07105 ver1.5"
partial_read: false
partial_read_note: ""
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Cập nhật trạng thái VAS liên quan đến Quality Control

## Tổng quan
- **Mã tính năng:** quality_control_vas_update
- **Feature:** VAS Updates for QC
- **Mô tả ngắn:** Bổ sung thông tin Loại VAS (VAS type), trạng thái VAS mới cho luồng QC, và quy trình xử lý sau đánh giá (nhận hàng, trả nhà cung cấp, mở lại).
- **Source chính:** `07105_Quality_Control_Docs_ver1.5.md` – section "VAS updated"
- **Đối tượng sử dụng (Actors):** Warehouse Manager, QC Manager
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[quality_control_mobile]] — App kết thúc đánh giá, VAS chuyển "Chờ duyệt"
  - ⬅️ [[receiving_po_vas]] — Cùng module VAS

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07105_Quality_Control_Docs_ver1.5.md | ver1.5 | ✅ Hiện hành |

## Phân rã Requirement

### Bổ sung Loại VAS (VAS Type)
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-VASQC-01 | Thêm filter VAS Type khi tạo VAS mới; giá trị: IMEI, RFID, Quality Control, Other; hỗ trợ chọn nhiều | Functional | High | ✅ | 07105#699-707 |
| R-VASQC-02 | Data table: bổ sung cột VAS type; nếu VAS có cả QC và RFID/IMEI thì hiển thị cả 2, cách nhau bởi dấu phẩy | Functional | High | ✅ | 07105#709-711 |

### Trạng thái VAS mới
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-VASQC-03 | Danh sách đầy đủ trạng thái VAS: Mới/Open, Đang xử lý/In-Progress, Hoàn thành/Completed, Đã huỷ/Canceled, Chờ duyệt/Waiting for approval, Chờ dán ID/Waiting for paste ID, Chờ đánh giá/Waiting quality control, Chờ NCC đến lấy/Waiting vendor to pick, Đã trả NCC/Returned to vendor | Functional | High | ✅ | 07105#714-728 |
| R-VASQC-04 | VAS sau khi đánh giá QC có tiêu chí không đạt → chuyển trạng thái "Chờ duyệt/Waiting for approval" | Functional | High | ✅ | 07105#721-722 |

### Xử lý VAS trạng thái Chờ duyệt
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-VASQC-05 | Action "Mở lại (Re-Open)": confirm "Do you want to confirm RECEIVE for the quality control of VAS [code]?" → Xác nhận → kết quả đánh giá về Mới/Open để đánh giá lại | Functional | High | ✅ | 07105#737-742 |
| R-VASQC-06 | Action "Nhận hàng (Receive)": confirm → Xác nhận nhận hàng → xác nhận tất cả tiêu chí Đạt (dù có tiêu chí không đạt vẫn có thể xác nhận); chuyển bước tiếp theo | Functional | High | ✅ | 07105#743-754 |
| R-VASQC-07 | Sau Nhận hàng: nếu SKU required IMEI/RFID → chuyển "Chờ dán ID/Waiting for paste ID"; nếu không required → chuyển Completed | Functional | High | ✅ | 07105#752-754 |
| R-VASQC-08 | Action "Trả nhà cung cấp (Return to vendor)": nhập số lượng cần trả (phase này = số lượng đã nhận, disabled); Xác nhận → ghi nhận số lượng VAS và số lượng trả NCC; chuyển trạng thái "Chờ NCC đến lấy" | Functional | High | ✅ | 07105#755-762 |
| R-VASQC-09 | Sau khi NCC đến lấy: user vào cập nhật trạng thái VAS từ "Chờ NCC đến lấy" → "Đã trả NCC"; tạo Outbound type Return vendor + Adjustment type Vendor Return | Functional | High | ✅ | 07105#763-768 |
| R-VASQC-10 | Lưu ý: hiện tại Dev xác nhận chưa thể tạo Adjustment cho case này | Functional | High | ⚠️ UNCLEAR | 07105#769-771 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Luồng chuẩn (Happy Path) — Nhận hàng sau QC
1. App đánh giá xong → nếu có tiêu chí không đạt → VAS chuyển "Chờ duyệt".
2. Manager vào VAS detail → xem kết quả đánh giá.
3. Chọn "Nhận hàng" → confirm → tất cả tiêu chí coi như Đạt.
4. Nếu SKU required IMEI/RFID → "Chờ dán ID"; ngược lại → Completed.

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 – Trả NCC:** Manager chọn "Trả nhà cung cấp" → nhập số lượng → Xác nhận → chuyển "Chờ NCC đến lấy".
- **Alt-Flow 2 – Mở lại:** Manager chọn "Mở lại" → kết quả đánh giá về Open để đánh giá lại.

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1:** Tạo Adjustment cho case Trả NCC — hiện tại Dev chưa hỗ trợ (R-VASQC-10).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Điều kiện | Kết quả |
|:----------|:--------|
| QC có tiêu chí không đạt | VAS → Chờ duyệt |
| Nhận hàng (dù có tiêu chí không đạt) | VAS tiếp tục quy trình |
| SKU required IMEI/RFID sau Nhận hàng | VAS → Chờ dán ID |
| SKU không required | VAS → Completed |
| Trả NCC | VAS → Chờ NCC đến lấy |
| NCC đã lấy | VAS → Đã trả NCC |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
| Thao tác | Confirm message EN |
|:---------|:------------------|
| Mở lại VAS | Do you want to confirm RECEIVE for the quality control of VAS [code]? |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-VASQC-01: VAS chuyển Chờ duyệt khi có tiêu chí không đạt**
  - **Given:** App hoàn thành đánh giá QC và có ≥1 tiêu chí không đạt
  - **When:** User chọn "Hoàn thành" trên App
  - **Then:** VAS chuyển trạng thái "Chờ duyệt / Waiting for approval"

- **AC-VASQC-02: Nhận hàng khi có tiêu chí không đạt**
  - **Given:** VAS ở trạng thái Chờ duyệt, trong kết quả có tiêu chí không đạt
  - **When:** Manager chọn "Nhận hàng" và xác nhận
  - **Then:** VAS vẫn được nhận hàng, chuyển sang bước tiếp theo

- **AC-VASQC-03: VAS type hiển thị nhiều giá trị**
  - **Given:** VAS có cả Quality Control và RFID
  - **When:** Manager xem data table VAS
  - **Then:** Cột VAS type hiển thị "Quality Control, RFID"

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-VASQC-01 | R-VASQC-10 | Adjustment type Vendor Return cho case Trả NCC — có timeline dự kiến hỗ trợ không? Cần viết test case blocked không? | BA/Dev | Open | | | |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-VASQC-04 / AC-VASQC-01 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-VASQC-06 / AC-VASQC-02 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-VASQC-02 / AC-VASQC-03 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-VASQC-10 | | ❌ Blocked | Chờ Q-VASQC-01 |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo spec từ 07105 ver1.5, section VAS updated | 07105#696-771 |
