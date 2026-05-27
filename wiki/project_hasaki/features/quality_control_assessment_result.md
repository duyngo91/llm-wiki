---
aliases: [QC Assessment Result, Kết quả đánh giá QC]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: quality_control_assessment_result
project: project_hasaki
source_version: "07105 ver1.5"
partial_read: false
partial_read_note: ""
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Kết quả đánh giá chất lượng (Assessment Result) — Web

## Tổng quan
- **Mã tính năng:** quality_control_assessment_result
- **Feature:** Assessment Result (Web)
- **Mô tả ngắn:** Màn hình xem danh sách và chi tiết kết quả đánh giá chất lượng sản phẩm trên Web. Update 11-02-2026 bổ sung "Số lượng cần đánh giá" và "Hình ảnh tem QC" trong chi tiết; cột Type bổ sung giá trị "Xã vải".
- **Source chính:** `07105_Quality_Control_Docs_ver1.5.md` – section "Kết quả đánh giá", "18-09-2025: Chi tiết kết quả đánh giá", "Update 11-02-2026 Kết quả đánh giá (Web)"
- **Đối tượng sử dụng (Actors):** QC Manager, Warehouse Manager
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[quality_control_mobile]] — App ghi nhận kết quả đánh giá
  - ⬅️ [[quality_control_fabric_mobile]] — App đánh giá vải
  - ⬅️ [[quality_control_vas_update]] — VAS link qua Assessment Result

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07105_Quality_Control_Docs_ver1.5.md | ver1.5 | ✅ Hiện hành |

## Phân rã Requirement

### Filter – Kết quả đánh giá
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-AR-01 | Filter SKU, barcode — tìm theo mã chính xác | Functional | High | ✅ | 07105#578-579 |
| R-AR-02 | Filter VAS — tìm theo mã chính xác | Functional | Medium | ✅ | 07105#580-582 |
| R-AR-03 | Filter Kho — tìm theo tên kho từ 3 ký tự | Functional | Medium | ✅ | 07105#583-585 |
| R-AR-04 | Filter Mã PO — tìm theo mã PO nguồn (mã PO inside), tìm chính xác | Functional | Medium | ✅ | 07105#586-588 |
| R-AR-05 | Filter Trạng thái — giá trị: Mới/New, Đang đánh giá/Processing, Hoàn thành/Completed | Functional | High | ✅ | 07105#589-595 |
| R-AR-06 | Filter Phân loại (Type) — giá trị: Tự động/Automation, Thủ công/Manual, Bình thường/Normal, Nhóm UID/Group UID, Xã vải/Fabric Relaxing | Functional | High | ✅ | 07105#596-604 |
| R-AR-07 | Filter Người đánh giá — Email Hasaki + thời gian hoàn thành | Functional | Low | ✅ | 07105#607-611 |
| R-AR-08 | Filter "Có tiêu chí không đạt" — giá trị: Có (có ≥1 tiêu chí không đạt) / Không | Functional | Medium | ✅ | 07105#612-616 |
| R-AR-09 | Filter Ngày đánh giá — Từ ngày ≤ Đến ngày | Functional | Low | ✅ | 07105#617-624 |

### Listing – Kết quả đánh giá
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-AR-10 | Listing gồm: VAS (hyperlink → VAS detail), Kho, Sản phẩm (SKU – tên), Tiêu chí đạt, Tiêu chí không đạt, Phân loại, Mã PO nguồn (hyperlink → PO detail Inside), Nhà cung cấp, Danh mục, Thương hiệu, Ghi chú, Người đánh giá, Thời gian hoàn thành, Trạng thái, Thao tác | Functional | High | ✅ | 07105#627-647 |
| R-AR-11 | Cột Tiêu chí đạt: tổng tiêu chí đạt / tổng tiêu chí cần đánh giá | Functional | High | ✅ | 07105#633 |
| R-AR-12 | Cột Tiêu chí không đạt: tổng tiêu chí không đạt / tổng tiêu chí cần đánh giá | Functional | High | ✅ | 07105#634 |
| R-AR-13 | Action xem chi tiết kết quả đánh giá | Functional | High | ✅ | 07105#647 |

### Kiến trúc service ghi nhận kết quả
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-AR-14 | Dựng 1 service ghi nhận kết quả đánh giá để nhận thông tin từ nhiều nguồn; WMS ghi nhận kết quả cuối cùng | Functional | High | ⚠️ UNCLEAR | 07105#649-658 |
| R-AR-15 | VAS_ID + Group UID gắn với từng Service; mỗi service gồm: Group UID, Mã tiêu chí, Kết quả; mỗi service = 1 kết quả đánh giá của 1 group UID | Functional | High | ✅ | 07105#652-657 |

### Chi tiết kết quả đánh giá (18-09-2025)
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-AR-16 | Type = Bình thường: hiển thị chi tiết kết quả đánh giá chuẩn | Functional | High | ✅ | 07105#660-661 |
| R-AR-17 | Type = Nhóm UID: cho xem chi tiết kết quả theo từng nhóm UID | Functional | High | ✅ | 07105#664-666 |
| R-AR-18 | Type = Lỗi 4 điểm (đặc thù): lưu và hiển thị riêng; mỗi loại lỗi là 1 group (thu gọn/mở rộng); hiển thị Tổng điểm lỗi + Tổng điểm đã nhân hệ số | Functional | High | ✅ | 07105#667-684 |
| R-AR-19 | Chi tiết lỗi 4 điểm: Lỗi 1 điểm gồm Loại lỗi, Hình ảnh lỗi, Ghi chú; tương tự cho 2, 3, 4 điểm | Functional | High | ✅ | 07105#676-684 |
| R-AR-20 | Tiêu chí Theo từng bước: 1 bước = 1 nhóm thông tin gồm: Hình ảnh, Kết quả ghi nhận, Ghi chú | Functional | High | ✅ | 07105#685-690 |

### Update 11-02-2026
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-AR-21 | Chi tiết kết quả đánh giá: bổ sung "Số lượng cần đánh giá" | Functional | Medium | ✅ | 07105#1103-1105 |
| R-AR-22 | Chi tiết kết quả đánh giá: bổ sung "Hình ảnh tem QC" | Functional | Medium | ✅ | 07105#1106 |
| R-AR-23 | Cột Phân loại (Type) listing: bổ sung giá trị "Xã vải / Fabric Relaxing" | Functional | High | ✅ | 07105#1108-1111 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Luồng chuẩn (Happy Path)
1. User vào Menu: Inbound / Quality control → Tab "Kết quả đánh giá".
2. User filter theo Kho, Trạng thái, Phân loại.
3. Danh sách hiển thị với tiêu chí đạt/không đạt.
4. User click vào dòng để xem chi tiết kết quả.

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 – Lỗi 4 điểm:** Chi tiết hiển thị theo nhóm điểm, có thể thu gọn/mở rộng.
- **Alt-Flow 2 – Từng bước:** Mỗi bước hiển thị riêng với hình ảnh, kết quả, ghi chú.
- **Alt-Flow 3 – Nhóm UID:** Xem chi tiết kết quả theo từng nhóm UID.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Ràng buộc |
|:-----------|:---------|:----------|
| Trạng thái | Enum | Mới → Đang đánh giá → Hoàn thành |
| Filter Từ ngày | Date | Phải ≤ Đến ngày |
| Tiêu chí đạt/không đạt | Fraction | = tổng đạt / tổng cần đánh giá |
| Loại lỗi 4 điểm | Grouping | Mỗi nhóm = 1 loại lỗi; có thể thu gọn/mở rộng |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
*(Không có error message explicit trong source cho section này)*

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-AR-01: Filter phân loại hoạt động đúng**
  - **Given:** Có kết quả đánh giá nhiều loại
  - **When:** User filter Phân loại = "Xã vải"
  - **Then:** Chỉ hiển thị kết quả có Type = Fabric Relaxing

- **AC-AR-02: Chi tiết lỗi 4 điểm hiển thị đúng**
  - **Given:** Kết quả đánh giá type = Lỗi 4 điểm
  - **When:** User xem chi tiết
  - **Then:** Hiển thị 4 nhóm lỗi (1/2/3/4 điểm), mỗi nhóm có thể thu gọn/mở rộng với Tổng điểm và Tổng đã nhân hệ số

- **AC-AR-03: Hình ảnh tem QC hiển thị trong chi tiết**
  - **Given:** Kết quả đánh giá đã có chụp tem QC
  - **When:** User xem chi tiết kết quả
  - **Then:** Trường "Hình ảnh tem QC" hiển thị hình đã chụp

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-AR-01 | R-AR-14 | "Service ghi nhận kết quả" — là microservice riêng hay bảng DB? Có API spec không? | Dev | Open | | | |
| Q-AR-02 | R-AR-05 | Trạng thái "Đang đánh giá/Processing" — điều kiện trigger cụ thể là gì? | BA | Open | | | |

## 📝 Thay đổi so với version cũ
| Change ID | Loại | Nội dung | Version cũ | Version mới | R/AC ảnh hưởng | Trạng thái |
|:----------|:-----|:---------|:-----------|:------------|:---------------|:-----------|
| CHG-AR-01 | Add | 18-09-2025: Chi tiết kết quả theo loại (Bình thường/Nhóm UID/Lỗi 4 điểm/Từng bước) | ver1.0 | ver1.1 | R-AR-16~20 | Draft |
| CHG-AR-02 | Add | Update 11-02-2026: Số lượng cần đánh giá + Hình ảnh tem QC + Type Xã vải | ver1.3 | ver1.4 | R-AR-21~23 | Draft |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-AR-18 / AC-AR-02 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-AR-22 / AC-AR-03 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-AR-23 / AC-AR-01 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-AR-14 | | ❌ Blocked | Chờ Q-AR-01 |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo spec từ 07105 ver1.5, section Kết quả đánh giá | 07105#570-690, #1101-1111 |
