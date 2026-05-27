---
aliases: [QC Fabric Mobile, Đánh giá vải App]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: quality_control_fabric_mobile
project: project_hasaki
source_version: "07105 ver1.5"
partial_read: false
partial_read_note: ""
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Đánh giá chất lượng vải nguyên vật liệu (App)

## Tổng quan
- **Mã tính năng:** quality_control_fabric_mobile
- **Feature:** Fabric Quality Assessment (App)
- **Mô tả ngắn:** Luồng đánh giá chất lượng vải nguyên vật liệu trên App — đánh giá theo Group UID, thực hiện 3 tiêu chí (Lỗi 4 điểm, Kiểm tra độ co rút, Kiểm tra độ đồng màu). Update 20-04-2026: SKU vải Failed → tự động blocked UID group và chuyển product status = Damaged. Update 11-02-2026: quản lý cột "Đánh giá đạt" cho UID group.
- **Source chính:** `07105_Quality_Control_Docs_ver1.5.md` – section "Update 18-09-2025 – Đánh giá chất lượng vải", "Update 20-04-2026 Blocked UID group và chuyển Damaged", "Update 11-02-2026 UID group (Web)"
- **Đối tượng sử dụng (Actors):** Warehouse staff (App), Warehouse Manager (Web)
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[quality_control_sku_setup]] — Tiêu chí đánh giá vải (Lỗi 4 điểm, co rút, đồng màu)
  - ⬅️ [[receiving_po_fabric_uid_group]] — Nhận hàng vải khai báo Group UID
  - ➡️ [[quality_control_assessment_result]] — Kết quả ghi lên Web

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07105_Quality_Control_Docs_ver1.5.md | ver1.5 | ✅ Hiện hành |

## Phân rã Requirement

### Bước 1-2 – Vào tính năng, chọn VAS
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-FAB-01 | Menu App: Purchase Order / Quality Control → chọn kho → hiển thị VAS type QC có status Open/In-Progress | Functional | High | ✅ | 07105#875-878 |
| R-FAB-02 | Chọn VAS → hiển thị: Shop, VAS, Tổng SKU, Mã PO, Tổng sản phẩm | Functional | High | ✅ | 07105#879-890 |
| R-FAB-03 | Danh sách sản phẩm bổ sung: Số lô, Hạn sử dụng; màu sắc: xám nhạt (chưa đánh giá), xanh dương nhạt (đang đánh giá), xanh lá nhạt (đã đánh giá và Đạt), cam nhạt (đã đánh giá và Không Đạt) | Functional | High | ✅ | 07105#888-901 |
| R-FAB-04 | Đánh giá 10% số lượng cây vải của từng lô: 1 lô cần 3 cây vải (3 group UID) → 3 dòng riêng | Functional | High | ✅ | 07105#902-904 |

### Bước 3 – Scan Group UID
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-FAB-05 | Chọn sản phẩm → yêu cầu scan nhóm UID tương ứng với cây vải cần đánh giá | Functional | High | ✅ | 07105#909 |
| R-FAB-06 | Nếu nhóm UID không tồn tại hoặc không thuộc PO/số lô được yêu cầu → hiển thị thông báo lỗi | Functional | High | ✅ | 07105#910-912 |
| R-FAB-07 | Hỗ trợ suggest nhóm UID đã nhận cho sản phẩm theo lô để user chọn nhanh | Functional | Medium | ✅ | 07105#913 |
| R-FAB-08 | Sau khi scan/chọn UID hợp lệ → chọn "Xác nhận" để qua bước tiếp | Functional | High | ✅ | 07105#914-915 |

### Bước 4 – Đánh giá tiêu chí vải (3 tiêu chí)

#### Tiêu chí 1: Kiểm tra lỗi 4 điểm
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-FAB-09 | Hiển thị 4 loại lỗi: Lỗi 1 điểm (0–3"), Lỗi 2 điểm (3"–6"), Lỗi 3 điểm (6"–9"), Lỗi 4 điểm (>9") | Functional | High | ✅ | 07105#930-934 |
| R-FAB-10 | Khi phát hiện lỗi: chọn dấu + để thêm thông tin lỗi | Functional | High | ✅ | 07105#935 |
| R-FAB-11 | Chọn lỗi: bắt buộc; 19 giá trị: 1.Slub, 2.Foreign yarn, 3.Thin yarn/rough yarn, 4.Yarn knot, 5.Missing yarn, 6.Break yarn, 7.Needle line, 8.Dark line, 9.Scratch, 10.Staining, 11.Fade of color, 12.Dyeing block, 13.Color spot, 14.Dirty, 15.Hole, 16.Printing error, 17.Fold/crease, 18.Dead fold, 19.Other | Functional | High | ✅ | 07105#937-960 |
| R-FAB-12 | Ghi chú lỗi: không bắt buộc | Functional | Low | ✅ | 07105#961 |
| R-FAB-13 | Chụp hình ảnh lỗi: bắt buộc; tối đa 3 hình | Functional | High | ✅ | 07105#962-963 |
| R-FAB-14 | Sau khi ghi nhận tất cả lỗi: hiển thị Số lỗi từng loại, Tổng điểm lỗi (chưa nhân hệ số), Tổng điểm lỗi đã nhân hệ số | Functional | High | ✅ | 07105#967-973 |
| R-FAB-15 | Chọn "Hoàn thành" → lấy kết quả điểm đã nhân hệ số so sánh với điều kiện thiết lập → xác định Đạt/Không đạt; Kết quả = Tổng điểm lỗi đã nhân hệ số | Functional | High | ✅ | 07105#975-983 |

#### Tiêu chí 2: Kiểm tra độ co rút (Theo từng bước)
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-FAB-16 | Thiết lập theo từng bước: hiển thị từng bước với Thứ tự - Tên bước, Hình ảnh mẫu, Hướng dẫn, Yêu cầu chụp hình, Ghi nhận kết quả (Đạt/Không đạt hoặc Nhập giá trị) | Functional | High | ✅ | 07105#985-1000 |
| R-FAB-17 | Sau khi cập nhật xong bước → "Tiếp theo" → qua bước tiếp | Functional | High | ✅ | 07105#1005-1006 |
| R-FAB-18 | Sau bước cuối → "Hoàn thành" → dựa vào công thức thiết lập để tính kết quả, so sánh với điều kiện → Đạt/Không đạt | Functional | High | ✅ | 07105#1008-1012 |

#### Tiêu chí 3: Kiểm tra độ đồng màu
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-FAB-19 | Thực hiện tương tự như Kiểm tra độ co rút | Functional | High | ✅ | 07105#1013-1014 |

### Bước 5 – Ghi nhận kết quả nhóm UID
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-FAB-20 | Sau khi đánh giá xong tất cả tiêu chí → "Hoàn thành" | Functional | High | ✅ | 07105#1015-1016 |
| R-FAB-21 | Nếu có ≥1 tiêu chí không đạt → kết quả sản phẩm theo nhóm UID = Không đạt | Functional | High | ✅ | 07105#1017-1018 |
| R-FAB-22 | Tiếp tục các nhóm UID còn lại cho tới khi hoàn thành toàn bộ | Functional | High | ✅ | 07105#1019 |

### Update 20-04-2026: Blocked UID group + Damaged
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-FAB-23 | SKU vải bị Failed QC: hệ thống tự động blocked tất cả UID group của SKU nhận trong cùng PO và cùng LOT | Functional | High | ✅ | 07105#1293-1295 |
| R-FAB-24 | Đồng thời chuyển Product status của các UID trong các UID group đó thành Damaged → không cộng vào stock Available → không được IT | Functional | High | ✅ | 07105#1295-1297 |
| R-FAB-25 | Khi user Un-Blocked UID group: ngoài unblock về Available thì auto chuyển Product status từ Damaged → Normal | Functional | High | ✅ | 07105#1298-1300 |

### Update 11-02-2026: UID group (Web) – cột Đánh giá đạt
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-FAB-26 | Menu: Inventory / Group UID / Tab "Danh sách": bổ sung cột "Đánh giá đạt" | Functional | High | ✅ | 07105#1113-1115 |
| R-FAB-27 | Giá trị cột "Đánh giá đạt": N/A (SKU khai báo UID group nhưng không phải Thời trang NVL và không phải SKU vải), No (SKU vải sau khi nhận PO, mặc định No; sau khi đánh giá xã vải Đạt → chuyển Yes), Yes (sau đánh giá xã vải Đạt) | Functional | High | ✅ | 07105#1117-1123 |

### Khai báo số lượng cần đánh giá cho UID group (App — Update 11-02-2026)
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-FAB-28 | Ở bước scan UID group: bổ sung cập nhật số lượng cần đánh giá cho UID group; bắt buộc; phải là số nguyên dương | Functional | High | ✅ | 07105#1131-1134 |
| R-FAB-29 | Sau khi xác nhận: hệ thống trừ số lượng đã khai báo ra khỏi UID group (VD: UID group SKU A qty 9500, khai báo 500 → còn 9000) | Functional | High | ✅ | 07105#1135-1139 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- SKU vải (category Thời trang NVL) đã được nhận PO với Group UID.
- VAS QC đã được sinh (10% group UID, làm tròn lên).
- Tiêu chí đánh giá vải đã được thiết lập cho SKU.

### Luồng chuẩn (Happy Path)
1. User App → Quality Control → chọn Kho → chọn VAS vải.
2. Chọn sản phẩm (cây vải) cần đánh giá.
3. Scan Group UID tương ứng → khai báo số lượng cần đánh giá → Xác nhận.
4. Thực hiện 3 tiêu chí: Lỗi 4 điểm → Độ co rút → Độ đồng màu.
5. Hoàn thành tất cả tiêu chí → Hoàn thành cho nhóm UID đó.
6. Tiếp tục các nhóm UID còn lại cho đến khi xong VAS.

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1:** Scan Group UID không thuộc PO/lô → thông báo lỗi.
- **Exc-Flow 2:** Kết quả Failed → hệ thống tự động blocked UID group + chuyển Damaged.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| Chọn lỗi | Enum (19 giá trị) | Có | Danh sách cố định |
| Chụp hình lỗi | Image | Có | Tối đa 3 hình |
| Số lượng cần đánh giá | Số nguyên | Có | > 0 |
| Kết quả group UID | Đạt/Không đạt | Auto | ≥1 tiêu chí không đạt → Không đạt |
| Block UID khi Failed | Auto | — | Cùng PO + cùng LOT |
| Damaged → Normal khi Un-block | Auto | — | Trigger bởi Un-block action |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
| Tình huống | Mô tả |
|:-----------|:------|
| Group UID không tồn tại / không thuộc PO/lô | Hiển thị thông báo lỗi (nội dung chính xác chưa ghi rõ trong source) |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-FAB-01: Màu cam khi Không đạt**
  - **Given:** SKU vải đã được đánh giá và có kết quả Không đạt
  - **When:** User xem danh sách sản phẩm trong VAS
  - **Then:** SKU hiển thị màu cam nhạt

- **AC-FAB-02: Chọn lỗi bắt buộc khi thêm lỗi 4 điểm**
  - **Given:** User chọn dấu + để thêm lỗi
  - **When:** User không chọn loại lỗi
  - **Then:** Không thể xác nhận lỗi

- **AC-FAB-03: Blocked UID group khi Failed**
  - **Given:** SKU vải (cùng PO, cùng LOT) có kết quả đánh giá QC = Không đạt
  - **When:** Hệ thống xử lý kết quả
  - **Then:** Tất cả UID group của SKU trong cùng PO + LOT bị blocked; Product status = Damaged

- **AC-FAB-04: Un-block tự chuyển Damaged → Normal**
  - **Given:** UID group đang ở trạng thái blocked, Product status = Damaged
  - **When:** User thực hiện Un-Block UID group
  - **Then:** UID group về Available VÀ Product status chuyển về Normal

- **AC-FAB-05: Khai báo số lượng trừ khỏi UID group**
  - **Given:** UID group SKU A có qty = 9500
  - **When:** User khai báo số lượng cần đánh giá = 500
  - **Then:** Qty của SKU A trong UID group = 9000

- **AC-FAB-06: Cột Đánh giá đạt = N/A cho SKU không phải vải**
  - **Given:** SKU thuộc category không phải Thời trang NVL
  - **When:** User xem cột "Đánh giá đạt" trong màn hình Group UID
  - **Then:** Giá trị = N/A

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-FAB-01 | R-FAB-06 | Thông báo lỗi khi scan UID không hợp lệ — nội dung chính xác là gì? | BA | Open | | | |
| Q-FAB-02 | R-FAB-21 | "Nếu có ≥1 tiêu chí không đạt → Không đạt" — áp dụng cho kết quả của từng group UID hay toàn bộ VAS? | BA | Open | | | |

## 📝 Thay đổi so với version cũ
| Change ID | Loại | Nội dung | Version cũ | Version mới | R/AC ảnh hưởng | Trạng thái |
|:----------|:-----|:---------|:-----------|:------------|:---------------|:-----------|
| CHG-FAB-01 | Add | 18-09-2025: Quy trình đánh giá vải, 3 tiêu chí | ver1.1 | ver1.2 | R-FAB-01~22 | Draft |
| CHG-FAB-02 | Add | Update 11-02-2026: số lượng cần đánh giá, UID group Đánh giá đạt | ver1.3 | ver1.4 | R-FAB-26~29 | Draft |
| CHG-FAB-03 | Add | Update 20-04-2026: Blocked UID group + Damaged | ver1.4 | ver1.5 | R-FAB-23~25 | Draft |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-FAB-03 / AC-FAB-01 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-FAB-11 / AC-FAB-02 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-FAB-23 / AC-FAB-03 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-FAB-25 / AC-FAB-04 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-FAB-29 / AC-FAB-05 | | ❌ Chưa tạo | Chờ Gate 1 |
| Q-FAB-01 | | ❌ Blocked | Chờ câu trả lời |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo spec từ 07105 ver1.5, section Đánh giá vải + Update 11-02/20-04-2026 | 07105#872-1020, #1112-1139, #1292-1300 |
