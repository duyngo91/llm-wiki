---
aliases: [QC Criteria Setup, Thiết lập tiêu chí QC]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: quality_control_criteria_setup
project: project_hasaki
source_version: "07105 ver1.5"
partial_read: false
partial_read_note: ""
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Thiết lập tiêu chí (Criteria Setup) — Web

## Tổng quan
- **Mã tính năng:** quality_control_criteria_setup
- **Feature:** Setup Criteria (Web)
- **Mô tả ngắn:** Quản lý danh sách tiêu chí đánh giá chất lượng trên Web — tạo mới, import, active/inactive tiêu chí. Từ Update 10-05-2026: bổ sung thiết lập nội dung tiêu chí "Lỗi 4 điểm" và "Theo từng bước" ngay từ màn hình tạo tiêu chí.
- **Source chính:** `07105_Quality_Control_Docs_ver1.5.md` – section "Thiết lập tiêu chí" và "Update 10-05-2026"
- **Đối tượng sử dụng (Actors):** QC Manager, Warehouse Manager
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ➡️ [[quality_control_sku_setup]] — Tiêu chí được dùng để thiết lập cho SKU

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07105_Quality_Control_Docs_ver1.5.md | ver1.5 | ✅ Hiện hành |
| 2 | Link | Workflow: https://drive.hasaki.vn/d/d45615dafe0b441785ff/ | — | ❓ Chưa đọc được |
| 3 | Link | Figma: https://www.figma.com/design/CLtzJtUv6sA4rxyaBPnbz5/34.-Quality-Control | — | ❓ Chưa đọc được |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Không có API explicit | N/A |

## Phân rã Requirement

### Filter – Danh sách tiêu chí
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-CS-01 | Filter "Mã, tên tiêu chí / Code, Criteria name" — tìm gần đúng, nhập tối thiểu 3 ký tự | Functional | High | ✅ | 07105#134-135 |
| R-CS-02 | Filter "Đang hoạt động / Active" | Functional | Medium | ✅ | 07105#137-138 |
| R-CS-03 | Filter "Từ ngày…đến ngày / From date…to date" — tìm theo ngày tạo; Đến ngày ≥ Từ ngày; mặc định không chọn ngày | Functional | Medium | ✅ | 07105#139-142 |

### Listing – Danh sách tiêu chí
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-CS-04 | Listing gồm: TT (số thứ tự tăng dần), Mã tiêu chí, Tên tiêu chí, Mô tả, Hướng dẫn, Đang hoạt động, Người tạo, Người cập nhật, Thao tác | Functional | High | ✅ | 07105#145-170 |
| R-CS-05 | Cột "Đang hoạt động / Active" — mặc định Active khi tiêu chí mới tạo | Functional | High | ✅ | 07105#152 |
| R-CS-06 | Active/Inactive tiêu chí: hiển thị popup xác nhận; confirm message: "Do you want to DEACTIVATE criterion [code]?" / "Do you want to ACTIVATE criterion [code]?" | Functional | High | ✅ | 07105#153-160 |
| R-CS-07 | Cột Người tạo — format: email Hasaki + thời gian tạo YYYY-MM-DD HH:SS | Functional | Medium | ✅ | 07105#161-163 |
| R-CS-08 | Cột Người cập nhật — format: email Hasaki + thời gian cập nhật cuối cùng YYYY-MM-DD HH:SS | Functional | Medium | ✅ | 07105#164-166 |
| R-CS-09 | Action Thao tác — cập nhật thông tin tiêu chí; không cho cập nhật Mã tiêu chí; các trường còn lại được phép cập nhật | Functional | High | ✅ | 07105#167-170 |

### Tạo tiêu chí
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-CS-10 | Mã tiêu chí: bắt buộc; không được trùng → thông báo VN: "Mã tiêu chí đã tồn tại." / EN: "The criteria code already exists." | Functional | High | ✅ | 07105#173-179 |
| R-CS-11 | Tên tiêu chí: bắt buộc; không được trùng → thông báo VN: "Tên tiêu chí đã tồn tại." / EN: "The criteria name already exists." | Functional | High | ✅ | 07105#180-189 |
| R-CS-12 | Mô tả: không bắt buộc | Functional | Low | ✅ | 07105#190-191 |
| R-CS-13 | Hướng dẫn: không bắt buộc | Functional | Low | ✅ | 07105#193-195 |
| R-CS-14 | Button "Đóng" — tắt popup | Functional | Low | ✅ | 07105#196 |
| R-CS-15 | Button "Lưu và đóng" — lưu tiêu chí và tắt popup | Functional | High | ✅ | 07105#197 |
| R-CS-16 | Button "Lưu và tiếp tục" — lưu tiêu chí và clear form để tiếp tục tạo | Functional | Medium | ✅ | 07105#198 |

### Import tiêu chí
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-CS-17 | Import dùng template import; validate: Mã tiêu chí đã tồn tại trên hệ thống / trong file; Tên tiêu chí đã tồn tại trên hệ thống / trong file | Functional | High | ✅ | 07105#199-211 |
| R-CS-18 | Validate messages: 4 loại lỗi với đầy đủ text VN/EN (mã trùng hệ thống, mã trùng file, tên trùng hệ thống, tên trùng file) | Functional | High | ✅ | 07105#202-210 |
| R-CS-19 | Luồng import sử dụng lại page import dùng chung cho các tính năng đã làm trước đó | Functional | Medium | ✅ | 07105#211 |

### Update 10-05-2026: Thiết lập nội dung từ màn hình Criteria
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-CS-20 | Khi tạo tiêu chí có phân loại "Lỗi 4 điểm": sau khi nhấn "Tạo" hệ thống mở thêm màn hình thiết lập nội dung (giống khi thiết lập tiêu chí cho SKU) | Functional | High | ✅ | 07105#1306-1308 |
| R-CS-21 | Khi tạo tiêu chí có phân loại "Theo từng bước": sau khi nhấn "Tạo" hệ thống mở thêm màn hình thiết lập nội dung từng bước | Functional | High | ✅ | 07105#1313-1315 |
| R-CS-22 | Khi thiết lập tiêu chí cho SKU, nếu chọn tiêu chí "Lỗi 4 điểm": hệ thống tự lấy thiết lập của tiêu chí để cập nhật cho SKU, không cần thiết lập lại từng SKU | Functional | High | ✅ | 07105#1309-1311 |
| R-CS-23 | Khi thiết lập tiêu chí cho SKU, nếu chọn tiêu chí "Theo từng bước": hệ thống tự lấy thiết lập của tiêu chí để cập nhật cho SKU, không cần thiết lập lại từng SKU | Functional | High | ✅ | 07105#1320-1321 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User đã login WMS với quyền QC Management.

### Luồng chuẩn (Happy Path) — Tạo tiêu chí
1. User vào Menu: Inbound / Quality control → Tab "Thiết lập tiêu chí".
2. User chọn "Tạo mới".
3. User nhập Mã tiêu chí, Tên tiêu chí (bắt buộc), Mô tả, Hướng dẫn (không bắt buộc).
4. Chọn "Lưu và đóng" hoặc "Lưu và tiếp tục".
5. Tiêu chí được tạo với trạng thái Active mặc định.

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 – Tiêu chí Lỗi 4 điểm:** Sau khi nhấn "Tạo" → hệ thống mở thêm màn hình thiết lập nội dung 4 điểm.
- **Alt-Flow 2 – Tiêu chí Theo từng bước:** Sau khi nhấn "Tạo" → hệ thống mở màn hình thiết lập từng bước.
- **Alt-Flow 3 – Import:** User import file theo template; validate lỗi trùng trước khi import.

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1:** Mã tiêu chí trùng → thông báo lỗi, không lưu.
- **Exc-Flow 2:** Tên tiêu chí trùng → thông báo lỗi, không lưu.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| Mã tiêu chí | Text | Có | Unique trên hệ thống; không được cập nhật sau khi tạo |
| Tên tiêu chí | Text | Có | Unique trên hệ thống |
| Mô tả | Text | Không | — |
| Hướng dẫn | Text | Không | — |
| Trạng thái | Active/Inactive | Auto | Mặc định Active khi tạo mới |
| Ngày tạo / cập nhật | YYYY-MM-DD HH:SS | Auto | — |
| Filter Đến ngày | Date | Không | Phải ≥ Từ ngày |
| Filter tìm kiếm | Text | Không | Nhập tối thiểu 3 ký tự |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
| Tình huống | VN | EN |
|:-----------|:---|:---|
| Mã tiêu chí trùng hệ thống | Mã tiêu chí đã tồn tại. | The criteria code already exists. |
| Tên tiêu chí trùng hệ thống | Tên tiêu chí đã tồn tại. | The criteria name already exists. |
| Deactivate tiêu chí | — | Do you want to DEACTIVATE criterion [code]? |
| Activate tiêu chí | — | Do you want to ACTIVATE criterion [code]? |
| Import – mã trùng hệ thống | Mã tiêu chí đã tồn tại trên hệ thống | The criteria code already exists in the systems. |
| Import – mã trùng file | Mã tiêu chí đã tồn tại trong file import | The criteria code already exists in the template import. |
| Import – tên trùng hệ thống | Tên tiêu chí đã tồn tại trên hệ thống | The criteria name already exists in the systems. |
| Import – tên trùng file | Tên tiêu chí đã tồn tại trong file import | The criteria name already exists in the template import. |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-CS-01: Tạo tiêu chí với mã trùng**
  - **Given:** Đã có tiêu chí với mã "CR001"
  - **When:** User tạo mới tiêu chí với mã "CR001"
  - **Then:** Hiển thị lỗi "Mã tiêu chí đã tồn tại." và không lưu

- **AC-CS-02: Mã tiêu chí không cho sửa**
  - **Given:** User vào cập nhật tiêu chí đã tạo
  - **When:** User cố gắng chỉnh sửa trường Mã tiêu chí
  - **Then:** Trường Mã tiêu chí bị disabled, không cho nhập

- **AC-CS-03: Active/Inactive cần xác nhận**
  - **Given:** Tiêu chí đang Active
  - **When:** User toggle sang Inactive
  - **Then:** Popup confirm hiển thị "Do you want to DEACTIVATE criterion [code]?"

- **AC-CS-04: Lưu và tiếp tục clear form**
  - **Given:** User đã nhập đầy đủ thông tin tiêu chí
  - **When:** User chọn "Lưu và tiếp tục"
  - **Then:** Tiêu chí được lưu VÀ form được clear để tiếp tục nhập tiêu chí mới

- **AC-CS-05: Tiêu chí 4 điểm mở màn hình thiết lập**
  - **Given:** User tạo tiêu chí với phân loại "Lỗi 4 điểm"
  - **When:** User nhấn "Tạo"
  - **Then:** Hệ thống mở thêm màn hình để thiết lập nội dung 4 điểm

- **AC-CS-06: Auto apply thiết lập tiêu chí cho SKU**
  - **Given:** Tiêu chí "Lỗi 4 điểm" đã có thiết lập nội dung từ màn hình Criteria
  - **When:** User chọn tiêu chí này khi thiết lập cho SKU
  - **Then:** Hệ thống tự lấy thiết lập sẵn, không yêu cầu người dùng thiết lập lại

- **AC-CS-07: Filter tìm kiếm từ 3 ký tự**
  - **Given:** User ở màn hình Thiết lập tiêu chí
  - **When:** User nhập 2 ký tự vào filter tìm kiếm
  - **Then:** Hệ thống không thực hiện tìm kiếm / không hiển thị gợi ý

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-CS-01 | R-CS-20~23 | Khi tiêu chí "Lỗi 4 điểm" đã được thiết lập và sau đó user chỉnh sửa thiết lập ở màn hình Criteria → các SKU đang dùng tiêu chí này có được tự cập nhật không? | BA/Dev | Open | | | |
| Q-CS-02 | R-CS-19 | "Luồng import dùng chung" — page import này có ở cùng URL/component với các import khác không? Có constraint nào đặc thù cho import tiêu chí? | Dev | Open | | | |

## 📝 Thay đổi so với version cũ
| Change ID | Loại | Nội dung | Version cũ | Version mới | R/AC ảnh hưởng | Trạng thái |
|:----------|:-----|:---------|:-----------|:------------|:---------------|:-----------|
| CHG-CS-01 | Add | Update 10-05-2026: thiết lập nội dung tiêu chí 4 điểm và từng bước từ màn hình Criteria | ver1.4 | ver1.5 | R-CS-20~23 | Draft |

## 🔎 Impact Analysis & Regression Proposal
| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:-----|
| CHG-CS-01 | quality_control_criteria_setup, quality_control_sku_setup | — | Add | Thiết lập SKU flow khi dùng tiêu chí có sẵn | Blocked by Gate 1 |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-CS-10 / AC-CS-01 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-CS-09 / AC-CS-02 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-CS-06 / AC-CS-03 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-CS-20 / AC-CS-05 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-CS-01 / AC-CS-07 | | ❌ Chưa tạo | Chờ Gate 1 |
| Q-CS-01 | | ❌ Blocked | Chờ câu trả lời |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo spec từ 07105 ver1.5, section Thiết lập tiêu chí | 07105#124-211, #1304-1321 |
