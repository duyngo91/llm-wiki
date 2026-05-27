---
aliases: [QC Manual Assessment, Đánh giá Manual QC]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: quality_control_manual_assessment
project: project_hasaki
source_version: "07105 ver1.5"
partial_read: false
partial_read_note: ""
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Tạo mới đánh giá Manual (App)

## Tổng quan
- **Mã tính năng:** quality_control_manual_assessment
- **Feature:** Manual Assessment Creation (App)
- **Mô tả ngắn:** Luồng user tự tạo phiên đánh giá chất lượng thủ công trên App — chọn sản phẩm, chọn PO, khai báo UID group và số lượng cần đánh giá, sau đó thực hiện đánh giá theo tiêu chí đã thiết lập. Phần cũ đã bị "bỏ" (đánh dấu bỏ) và được cập nhật lại trong Update 11-02-2026.
- **Source chính:** `07105_Quality_Control_Docs_ver1.5.md` – section "Tạo mới đánh giá – Manual" (Update ngày 12-02-2026), trang 42–49
- **Đối tượng sử dụng (Actors):** Warehouse staff (App)
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[quality_control_sku_setup]] — Tiêu chí đánh giá đã được thiết lập cho SKU
  - ➡️ [[quality_control_assessment_result]] — Kết quả ghi lên Web

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07105_Quality_Control_Docs_ver1.5.md | ver1.5 | ✅ Hiện hành |
| 2 | Link | Figma: https://www.figma.com/design/CLtzJtUv6sA4rxyaBPnbz5/34.-Quality-Control?node-id=1946-1696 | — | ❓ Chưa đọc được |

## Phân rã Requirement

### Bước 1 – Tạo mới đánh giá
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-MAN-01 | Menu App: Purchase Order / Quality Control → chọn Kho → chọn "Tạo mới" | Functional | High | ✅ | 07105#1175-1178 |
| R-MAN-02 | Tìm sản phẩm cần đánh giá: hỗ trợ tìm theo SKU, barcode hoặc tên sản phẩm; chọn để mở modal tìm kiếm mở rộng | Functional | High | ✅ | 07105#1179-1181 |
| R-MAN-03 | Load danh sách 10 PO nhận gần nhất của SKU được chọn theo kho | Functional | High | ✅ | 07105#1182 |
| R-MAN-04 | Tìm mã PO chính xác theo mã nhập vào, tìm trong tất cả PO có chứa SKU đã chọn | Functional | Medium | ✅ | 07105#1183-1184 |
| R-MAN-05 | Chọn "Tiếp tục" → nếu SKU chưa có thiết lập tiêu chí → hiển thị thông báo | Functional | High | ✅ | 07105#1185-1186 |

### Bước 2 – Khai báo UID group và số lượng
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-MAN-06 | Màn hình gồm: SKU + tên, Mã PO đã chọn, Ngày nhận PO, Nhà cung cấp, Ghi chú | Functional | High | ✅ | 07105#1190-1195 |
| R-MAN-07 | UID group: bắt buộc; khai báo UID group cần đánh giá | Functional | High | ✅ | 07105#1195-1197 |
| R-MAN-08 | Số lượng cần đánh giá: bắt buộc; cập nhật số lượng cần đánh giá | Functional | High | ✅ | 07105#1198-1200 |
| R-MAN-09 | Chọn "Bắt đầu đánh giá" → validate: nếu UID group không tồn tại → "Mã UID không tồn tại."; nếu số lượng không đủ → "Số lượng trong UID group không đủ số lượng yêu cầu." | Functional | High | ✅ | 07105#1201-1205 |

### Bước 3 – Đánh giá chất lượng
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-MAN-10 | Màn hình đánh giá gồm: Nhóm UID, Số lượng đang có của nhóm UID, Số lô, Hạn sử dụng, SL cần đánh giá, Mã PO, Nhà cung cấp, Sản phẩm (SKU – tên), Ghi chú | Functional | High | ✅ | 07105#1209-1218 |
| R-MAN-11 | Danh sách tiêu chí: lấy từ thiết lập cho SKU; thông tin: Thứ tự, Tên, Mô tả, Mô tả điều kiện, Đạt/Không đạt, Hình ảnh theo config | Functional | High | ✅ | 07105#1221-1230 |
| R-MAN-12 | Tiêu chí Fail: bắt buộc chụp hình và nhập ghi chú; tối đa 5 hình | Functional | High | ✅ | 07105#1233-1235 |
| R-MAN-13 | Sau khi đánh giá tất cả tiêu chí → "Hoàn thành" | Functional | High | ✅ | 07105#1237-1238 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- SKU đã có thiết lập tiêu chí được Approved.
- User có quyền tạo Manual assessment trên App.

### Luồng chuẩn (Happy Path)
1. App → Quality Control → chọn Kho → "Tạo mới".
2. Tìm sản phẩm, chọn PO → "Tiếp tục".
3. Khai báo UID group và số lượng cần đánh giá → "Bắt đầu đánh giá".
4. Thực hiện đánh giá từng tiêu chí.
5. "Hoàn thành" → kết quả ghi nhận.

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1:** SKU chưa có thiết lập tiêu chí → thông báo khi chọn "Tiếp tục".
- **Exc-Flow 2:** UID group không tồn tại → "Mã UID không tồn tại."
- **Exc-Flow 3:** Số lượng không đủ → "Số lượng trong UID group không đủ số lượng yêu cầu."

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| UID group | Text | Có | Phải tồn tại trong hệ thống |
| Số lượng cần đánh giá | Số | Có | ≤ Số lượng trong UID group |
| Hình ảnh tiêu chí Fail | Image | Có | Tối đa 5 hình |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
| Tình huống | VN |
|:-----------|:---|
| UID group không tồn tại | Mã UID không tồn tại. |
| Số lượng không đủ | Số lượng trong UID group không đủ số lượng yêu cầu. |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-MAN-01: UID group không tồn tại**
  - **Given:** User nhập UID group không có trong hệ thống
  - **When:** User chọn "Bắt đầu đánh giá"
  - **Then:** Thông báo "Mã UID không tồn tại."

- **AC-MAN-02: Số lượng vượt UID group**
  - **Given:** UID group có qty = 100
  - **When:** User nhập số lượng cần đánh giá = 101
  - **Then:** Thông báo "Số lượng trong UID group không đủ số lượng yêu cầu."

- **AC-MAN-03: SKU chưa có tiêu chí**
  - **Given:** SKU chọn chưa được thiết lập tiêu chí QC
  - **When:** User chọn "Tiếp tục"
  - **Then:** Hiển thị thông báo về việc SKU chưa có thiết lập tiêu chí

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-MAN-01 | R-MAN-05 | Nội dung thông báo khi SKU chưa có thiết lập tiêu chí là gì? | BA | Open | | | |
| Q-MAN-02 | (chung) | Manual assessment type khi tạo xong sẽ là "Thủ công / Manual" trong kết quả đánh giá phải không? | BA | Open | | | |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-MAN-09 / AC-MAN-01 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-MAN-09 / AC-MAN-02 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-MAN-05 / AC-MAN-03 | | ❌ Blocked | Chờ Q-MAN-01 |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo spec từ 07105 ver1.5, section Tạo mới đánh giá Manual (update 12-02-2026) | 07105#1172-1238 |
