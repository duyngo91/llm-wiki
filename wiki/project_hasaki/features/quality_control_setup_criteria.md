---
tags: [qa/requirement, qa/feature-group/quality-control]
status: Draft
created: 2026-05-25
updated: 2026-05-25
feature: quality_control_setup_criteria
project: project_hasaki
source_version: v1.5
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Quality Control — Thiết lập tiêu chí (Web)

## Tổng quan
- **Mã tính năng:** quality_control_setup_criteria
- **Feature:** Quản lý tiêu chí đánh giá chất lượng — Tạo, Import, Active/Inactive tiêu chí
- **Mô tả ngắn:** Tab "Thiết lập tiêu chí" (Setup criteria) trong menu Inbound / Quality Control (kiểm soát chất lượng) — cho phép quản lý danh sách tiêu chí đánh giá, tạo mới, import hàng loạt, active/inactive.
- **Source chính:** `raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.md` — mục "Thiết lập tiêu chí", "Tạo tiêu chí", "Import tiêu chí"
- **Đối tượng sử dụng (Actors):** QC Staff (Web), Quản lý kho
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** —
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ➡️ [[wiki/project_hasaki/features/quality_control_setup_sku|Setup Criteria by SKU]] — tiêu chí sau khi tạo được dùng khi gán cho SKU

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted from PDF) | `07105_Quality_Control_Docs_ver1.5.md` | v1.5 | ✅ Hiện hành |
| 2 | Figma | `https://www.figma.com/design/CLtzJtUv6sA4rxyaBPnbz5/34.-Quality-Control` | — | ❓ Chưa đọc được |
| 3 | Workflow | `https://drive.hasaki.vn/d/d45615dafe0b441785ff/` | — | ❓ Chưa đọc được |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | — | — | Không có API explicit | N/A |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Menu: Inbound / Quality Control — Tab "Thiết lập tiêu chí" (Setup criteria) | Functional | High | ✅ | v1.5, mục Thiết lập tiêu chí |
| R2 | Filter: Mã, tên tiêu chí — tìm gần đúng, nhập từ 3 ký tự | Functional | Medium | ✅ | v1.5, Filter |
| R3 | Filter: Đang hoạt động (Active) | Functional | Low | ✅ | v1.5, Filter |
| R4 | Filter: Từ ngày…đến ngày — theo ngày tạo; đến ngày ≥ từ ngày; mặc định không chọn | Functional | Low | ✅ | v1.5, Filter |
| R5 | Listing hiển thị: TT (tăng dần), Mã tiêu chí, Tên tiêu chí, Mô tả, Hướng dẫn, Đang hoạt động, Người tạo, Người cập nhật, Thao tác | Functional | High | ✅ | v1.5, Listing |
| R6 | Tiêu chí mới tạo mặc định ở trạng thái Active | Functional | High | ✅ | v1.5, Listing |
| R7 | Active/Inactive tiêu chí → hiển thị popup xác nhận: "Do you want to DEACTIVATE criterion [code]?" hoặc "Do you want to ACTIVATE criterion [code]?" | Functional | High | ✅ | v1.5, Listing |
| R8 | Người tạo: format "email Hasaki + thời gian tạo YYYY-MM-DD HH:SS" | Functional | Medium | ✅ | v1.5, Listing |
| R9 | Người cập nhật: format "email Hasaki cuối cùng cập nhật + thời gian YYYY-MM-DD HH:SS" | Functional | Medium | ✅ | v1.5, Listing |
| R10 | Thao tác (Action): chọn để cập nhật — không cho cập nhật Mã tiêu chí; các trường còn lại được phép cập nhật | Functional | High | ✅ | v1.5, Listing |
| R11 | Tạo tiêu chí: Mã tiêu chí bắt buộc, không được trùng — lỗi VN: "Mã tiêu chí đã tồn tại." / EN: "The criteria code already exists." | Functional | High | ✅ | v1.5, Tạo tiêu chí |
| R12 | Tạo tiêu chí: Tên tiêu chí bắt buộc, không được trùng — lỗi VN: "Tên tiêu chí đã tồn tại." / EN: "The criteria name already exists." | Functional | High | ✅ | v1.5, Tạo tiêu chí |
| R13 | Tạo tiêu chí: Mô tả không bắt buộc | Functional | Low | ✅ | v1.5, Tạo tiêu chí |
| R14 | Tạo tiêu chí: Hướng dẫn (instruct) không bắt buộc | Functional | Low | ✅ | v1.5, Tạo tiêu chí |
| R15 | Tạo tiêu chí: Button "Đóng" — tắt popup | Functional | Medium | ✅ | v1.5, Tạo tiêu chí |
| R16 | Tạo tiêu chí: Button "Lưu và đóng" — lưu và tắt popup | Functional | High | ✅ | v1.5, Tạo tiêu chí |
| R17 | Tạo tiêu chí: Button "Lưu và tiếp tục" — lưu và clear form để tạo tiếp | Functional | Medium | ✅ | v1.5, Tạo tiêu chí |
| R18 | Import tiêu chí: Validate duplicate mã/tên — 4 loại lỗi: trùng trong hệ thống hoặc trùng trong file import | Functional | High | ✅ | v1.5, Import tiêu chí |
| R19 | Import tiêu chí: dùng lại page import chung của hệ thống | Functional | Medium | ✅ | v1.5, Import tiêu chí |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User đã đăng nhập WMS với quyền truy cập Inbound / Quality Control

### Luồng chuẩn — Tạo tiêu chí (Happy Path)
1. User vào Inbound / Quality Control / Tab Thiết lập tiêu chí
2. Danh sách tiêu chí hiển thị với listing và filter
3. User chọn "Tạo mới" → popup hiện ra
4. Nhập Mã tiêu chí (bắt buộc), Tên tiêu chí (bắt buộc), Mô tả (tùy chọn), Hướng dẫn (tùy chọn)
5. Chọn "Lưu và đóng" → lưu tiêu chí, trạng thái Active, đóng popup
6. Tiêu chí mới xuất hiện trong danh sách

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 — Lưu và tiếp tục:** Sau khi lưu, form clear, popup vẫn mở để tạo thêm
- **Alt-Flow 2 — Import:** User chọn Import → vào page import chung, upload file, hệ thống validate

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1 — Trùng mã:** Popup hiện lỗi "Mã tiêu chí đã tồn tại." — không lưu, user sửa mã
- **Exc-Flow 2 — Trùng tên:** Popup hiện lỗi "Tên tiêu chí đã tồn tại." — không lưu, user sửa tên
- **Exc-Flow 3 — Import lỗi:** Validate từng dòng — hiện danh sách lỗi theo 4 loại

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu

| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| Mã tiêu chí | Text | ✅ | Unique trong hệ thống; không được cập nhật sau khi tạo |
| Tên tiêu chí | Text | ✅ | Unique trong hệ thống |
| Mô tả | Text | Không | — |
| Hướng dẫn | Text | Không | — |
| Filter ngày | Date range | Không | Đến ngày ≥ Từ ngày |
| Filter tên/mã | Text | Không | Nhập tối thiểu 3 ký tự mới search |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi

| Tình huống | VN | EN |
|:-----------|:---|:---|
| Mã tiêu chí trùng (tạo mới) | Mã tiêu chí đã tồn tại. | The criteria code already exists. |
| Tên tiêu chí trùng (tạo mới) | Tên tiêu chí đã tồn tại. | The criteria name already exists. |
| Mã tiêu chí trùng trong hệ thống (import) | Mã tiêu chí đã tồn tại trên hệ thống | The criteria code already exists in the systems. |
| Mã tiêu chí trùng trong file import | Mã tiêu chí đã tồn tại trong file import | The criteria code already exists in the template import. |
| Tên tiêu chí trùng trong hệ thống (import) | Tên tiêu chí đã tồn tại trên hệ thống | The criteria name already exists in the systems. |
| Tên tiêu chí trùng trong file import | Tên tiêu chí đã tồn tại trong file import | The criteria name already exists in the template import. |
| Confirm deactivate | Do you want to DEACTIVATE criterion [code]? | — |
| Confirm activate | Do you want to ACTIVATE criterion [code]? | — |

## 🏁 Tiêu Chí Nghiệm Thu (BDD)

- **Scenario 1: Tạo tiêu chí thành công**
  - **Given:** User ở tab Thiết lập tiêu chí, chọn Tạo mới
  - **When:** Nhập Mã tiêu chí unique, Tên tiêu chí unique, chọn "Lưu và đóng"
  - **Then:** Tiêu chí được lưu, trạng thái Active, xuất hiện trong danh sách

- **Scenario 2: Tạo tiêu chí với mã trùng**
  - **Given:** Mã tiêu chí "TC001" đã tồn tại trong hệ thống
  - **When:** User tạo mới với Mã tiêu chí = "TC001"
  - **Then:** Hiện lỗi "Mã tiêu chí đã tồn tại." — không lưu

- **Scenario 3: Active/Inactive tiêu chí**
  - **Given:** Tồn tại tiêu chí đang Active
  - **When:** User click Inactive cho tiêu chí đó
  - **Then:** Popup xác nhận "Do you want to DEACTIVATE criterion [code]?" — confirm → tiêu chí chuyển Inactive

- **Scenario 4: Lưu và tiếp tục**
  - **Given:** User đang tạo tiêu chí trong popup
  - **When:** Nhập đủ thông tin và chọn "Lưu và tiếp tục"
  - **Then:** Tiêu chí được lưu, popup vẫn mở, form bị clear sẵn sàng nhập tiêu chí tiếp theo

- **Scenario 5: Filter tìm kiếm theo tên tối thiểu 3 ký tự**
  - **Given:** User ở danh sách tiêu chí
  - **When:** Nhập 1-2 ký tự vào filter Mã/Tên
  - **Then:** Không trigger search (chưa đủ 3 ký tự)

- **Scenario 6: Filter ngày — validate đến ngày ≥ từ ngày**
  - **Given:** User dùng filter Từ ngày…đến ngày
  - **When:** Chọn đến ngày < từ ngày
  - **Then:** Hệ thống không cho chọn hoặc hiện lỗi validate

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn | Ngày |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:------|:-----|
| Q-001 | R2 | Filter tên/mã: nhập < 3 ký tự thì UX như thế nào? Disable search button, không gọi API, hay giữ kết quả cũ? | PO/Dev | Open | | | |
| Q-002 | R8, R9 | Format timestamp "YYYY-MM-DD HH:SS" trong doc — có phải là YYYY-MM-DD HH:mm:SS không? Thiếu phút? | PO/BA | Open | | | |
| Q-003 | R19 | Page import chung: template import cho tiêu chí có cấu trúc cột như thế nào? | BA/Dev | Open | | | |
| Q-004 | R7 | Sau khi Inactive tiêu chí, các SKU đang dùng tiêu chí đó bị ảnh hưởng gì? (xem thêm ở feature Setup SKU) | PO/Dev | Open | | | |
| Q-005 | — | Thuật ngữ & viết tắt trong doc để trống — có danh sách định nghĩa riêng không? | BA | Open | | | |
| Q-006 | R4 | Filter "Đến ngày" > hay ≥ "Từ ngày"? Doc ghi "Đến ngày phải lớn hơn hoặc bằng đến ngày" — có vẻ typo, ý là ≥ Từ ngày | PO/BA | Open | | | |

## 📝 Thay đổi so với version cũ
| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | R/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:---------------|:-----------|
| CHG-001 | Add | Toàn bộ feature mới (QC chưa tồn tại trước doc v1.0) | — | v1.5 | All | Draft |

## 🔎 Impact Analysis & Regression Proposal
| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:----------------------|
| CHG-001 | quality_control_setup_criteria | — | Add (mới) | — | Q-004 |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R1–R19 | — | ❌ Blocked | Chờ Gate 1 |
| R2 (filter <3 ký tự) | — | ❌ Blocked | Chờ Q-001 |
| R8, R9 (timestamp format) | — | ❌ Blocked | Chờ Q-002 |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo từ 07105_Quality_Control_Docs_ver1.5.md | Raw ingest |
