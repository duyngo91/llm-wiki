---
aliases: [QC SKU Setup, Thiết lập tiêu chí cho SKU]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: quality_control_sku_setup
project: project_hasaki
source_version: "07105 ver1.5"
partial_read: false
partial_read_note: ""
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Thiết lập tiêu chí cho SKU (Setup Criteria by SKU) — Web

## Tổng quan
- **Mã tính năng:** quality_control_sku_setup
- **Feature:** Setup Criteria by SKU (Web)
- **Mô tả ngắn:** Thiết lập tiêu chí đánh giá chất lượng cho từng SKU — bao gồm thời điểm đánh giá, tần suất, loại tiêu chí (Bình thường/Lỗi 4 điểm/Theo từng bước), yêu cầu chụp hình và thiết lập đánh giá theo điều kiện. Update 11-02-2026 bổ sung cột "QC xã vải".
- **Source chính:** `07105_Quality_Control_Docs_ver1.5.md` – section "Thiết lập tiêu chí cho SKU", "17-09-2025", "27-09-2025", "Update 11-02-2026 – Thêm cột khi thiết lập tiêu chí"
- **Đối tượng sử dụng (Actors):** QC Manager, Warehouse Manager
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[quality_control_criteria_setup]] — Tiêu chí được chọn từ danh sách đã thiết lập
  - ➡️ [[quality_control_approval]] — Sau khi thiết lập cần duyệt
  - ➡️ [[quality_control_mobile]] — App dùng thiết lập này để đánh giá

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07105_Quality_Control_Docs_ver1.5.md | ver1.5 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Không có API explicit | N/A |

## Phân rã Requirement

### Filter – Thiết lập SKU
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-SS-01 | Filter SKU, Barcode, Tên sản phẩm — tìm theo SKU, Barcode, tên sản phẩm | Functional | High | ✅ | 07105#228-229 |
| R-SS-02 | Filter Danh mục, Thương hiệu | Functional | Medium | ✅ | 07105#231-232 |
| R-SS-03 | Filter "Đang hoạt động / Active" — giá trị: Đang hoạt động/Active, Ngưng hoạt động/Inactive; mặc định không chọn | Functional | Medium | ✅ | 07105#233-236 |
| R-SS-04 | Filter "Thời điểm đánh giá / Assessment time" — giá trị: Khi nhận PO/Receiving PO, Sau khi nhận PO/After receive of PO; mặc định không chọn | Functional | Medium | ✅ | 07105#239-242 |
| R-SS-05 | Filter "Tần suất đánh giá / Assessment frequency" — giá trị: Tất cả PO/All PO, Ngẫu nhiên/Random; mặc định không chọn | Functional | Medium | ✅ | 07105#243-247 |
| R-SS-06 | Filter Từ ngày…đến ngày — Đến ngày ≥ Từ ngày; mặc định không chọn | Functional | Low | ✅ | 07105#248-250 |

### Listing – Thiết lập SKU
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-SS-07 | Listing gồm: TT, Sản phẩm (SKU – Tên), Danh mục, Thương hiệu, Thời điểm đánh giá, Tần suất đánh giá, Số lượng tiêu chí, Đang hoạt động, Người tạo, Người cập nhật, Trạng thái, Thao tác | Functional | High | ✅ | 07105#252-280 |
| R-SS-08 | Active/Inactive thiết lập SKU: confirm message — "Do you want to DEACTIVATE setup by SKU [code]?" / "Do you want to ACTIVATE setup by SKU [code]?" | Functional | High | ✅ | 07105#268-271 |
| R-SS-09 | Business rule: tại 1 thời điểm 1 SKU không thể cùng active 2 thiết lập; phải inactive cái cũ trước khi active cái mới | Functional | High | ✅ | 07105#272-273 |
| R-SS-10 | Action Edit — chỉ show cho status Mới (New) | Functional | Medium | ✅ | 07105#284 |
| R-SS-11 | Action View/Duyệt — xem chi tiết hoặc duyệt/từ chối | Functional | High | ✅ | 07105#285-286 |
| R-SS-12 | Action Xoá — chỉ show cho status Mới (New) | Functional | Medium | ✅ | 07105#287-288 |

### Tạo thiết lập cho SKU – Bước 1
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-SS-13 | Sản phẩm: bắt buộc; tìm bằng SKU, barcode, tên; validation: chưa chọn → "Thông tin này là bắt buộc." / "This information is required." | Functional | High | ✅ | 07105#295-303 |
| R-SS-14 | SKU đã có thiết lập Active: báo lỗi "SKU [code] đã tồn tại và đang hoạt động trên hệ thống." / "SKU [code] already exists and is active in the system." | Functional | High | ✅ | 07105#305-311 |
| R-SS-15 | Thời điểm đánh giá: bắt buộc; giá trị: "Khi nhận PO" (chưa hỗ trợ ở phase này) và "Sau khi nhận PO" | Functional | High | ✅ | 07105#312-323 |
| R-SS-16 | Tần suất đánh giá: bắt buộc; giá trị: "Tất cả PO" (tự sinh VAS sau khi kết thúc phiên nhận) và "Ngẫu nhiên" (user tự tạo phiên — chưa hỗ trợ ở phase này) | Functional | High | ✅ | 07105#324-338 |
| R-SS-17 | Ghi chú: không bắt buộc | Functional | Low | ✅ | 07105#339 |
| R-SS-18 | Button "Tiếp tục" → qua màn hình thiết lập tiêu chí; nếu SKU đã thiết lập và đang active → báo lỗi "SKU đã được thiết lập và đang hoạt động." / "SKU has been set up and is currently active" | Functional | High | ✅ | 07105#344-348 |

### Tạo thiết lập cho SKU – Bước 2: Thêm tiêu chí
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-SS-19 | Tiêu chí đánh giá: bắt buộc; load tất cả tiêu chí trên hệ thống; hỗ trợ tìm theo mã hoặc tên từ 3 ký tự | Functional | High | ✅ | 07105#365-368 |
| R-SS-20 | Yêu cầu chụp hình: bắt buộc chọn; giá trị: Yes/No | Functional | High | ✅ | 07105#369-371 |
| R-SS-21 | Hình chụp mẫu: không bắt buộc; upload tối đa 3 hình | Functional | Low | ✅ | 07105#372-374 |
| R-SS-22 | Loại đánh giá: Đạt/Không đạt (mặc định; phân loại = Bình thường, không cho chỉnh sửa) hoặc Theo điều kiện (=, >, >=, <, <=, Trong khoảng, Công thức) | Functional | High | ✅ | 07105#375-409 |
| R-SS-23 | Loại đánh giá "=" và ">", ">=", "<", "<=": giá trị bắt buộc (số > 0), đơn vị tính bắt buộc (text), sai số cho phép (không bắt buộc, số > 0) | Functional | High | ✅ | 07105#383-400 |
| R-SS-24 | Loại đánh giá "Trong khoảng (between)": Giá trị từ…đến (bắt buộc, số > 0), đơn vị tính (bắt buộc, text) | Functional | High | ✅ | 07105#402-405 |
| R-SS-25 | Loại đánh giá "Công thức": rules chưa đầy đủ ("sẽ bổ sung sau khi trao đổi với Dev") | Functional | Medium | ⚠️ UNCLEAR | 07105#407-409 |
| R-SS-26 | Lưu ý: 1 tiêu chí chỉ hỗ trợ 1 điều kiện; sau khi thêm 1 điều kiện thì nút Thêm (+) disable | Functional | High | ✅ | 07105#411-413 |
| R-SS-27 | Phân loại (Type): Bình thường/Normal, Lỗi 4 điểm/4 points error, Theo từng bước/Step by step | Functional | High | ✅ | 07105#414-420 |
| R-SS-28 | Mô tả tiêu chí: không bắt buộc | Functional | Low | ✅ | 07105#421 |
| R-SS-29 | Button "Thêm": add tiêu chí vào danh sách; nếu tiêu chí đã tồn tại → "Tiêu chí đã tồn tại trong danh sách." / "Criteria already exists in the list." | Functional | High | ✅ | 07105#422-427 |
| R-SS-30 | Button "Lưu" — lưu tạm để tiếp tục sau | Functional | Medium | ✅ | 07105#429-430 |
| R-SS-31 | Button "Yêu cầu duyệt" — chuyển status sang "Chờ duyệt" (Waiting for Approval) | Functional | High | ✅ | 07105#431-432 |
| R-SS-32 | Update 05-08-2025: nếu status SKU = Open/Waiting for Approval mà tiêu chí bị inactive → xoá tiêu chí khỏi danh sách SKU | Functional | High | ✅ | 07105#434-436 |
| R-SS-33 | Update 05-08-2025: nếu status SKU = Approved mà tiêu chí bị inactive → không hiển thị tiêu chí cho SKU | Functional | High | ✅ | 07105#436-437 |

### Thiết lập đánh giá từng bước (17-09-2025)
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-SS-34 | Tiêu chí type "Theo từng bước": chọn Edit → mở modal thiết lập các bước; khi add tiêu chí "Theo từng bước" → tự chuyển qua màn hình thiết lập | Functional | High | ✅ | 07105#444-449 |
| R-SS-35 | Thiết lập bước: Bước (số 1-10, số đã chọn disable), Nội dung (tên bước), Yêu cầu chụp hình, Hình ảnh mẫu | Functional | High | ✅ | 07105#451-461 |
| R-SS-36 | Ghi nhận kết quả cho từng bước: Không/No, Nhập giá trị/Fill value, Đạt/Không đạt – Passed/Failed | Functional | High | ✅ | 07105#462-467 |
| R-SS-37 | Từ khoá (Keywords): chỉ show khi Ghi nhận kết quả ≠ Không; tự động bật in hoa, không cho nhập khoảng trắng; cho phép "_", "-", "." | Functional | High | ✅ | 07105#468-471 |
| R-SS-38 | Hướng dẫn, Công thức, Kiểm tra định dạng (hợp lệ: xanh lá / không hợp lệ: đỏ) | Functional | High | ✅ | 07105#473-479 |
| R-SS-39 | Button Lưu chỉ hiện khi có ≥1 bước được thiết lập VÀ công thức (nếu có) hợp lệ; nếu cập nhật công thức chưa kiểm tra → validate lại khi nhấn Lưu | Functional | High | ✅ | 07105#482-488 |

### Thiết lập nội dung tiêu chí Lỗi 4 điểm (27-09-2025)
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-SS-40 | Tiêu chí type "Lỗi 4 điểm": chọn Edit → mở modal; khi add tiêu chí "Lỗi 4 điểm" → tự chuyển qua màn hình thiết lập | Functional | High | ✅ | 07105#494-499 |
| R-SS-41 | Fields thiết lập Lỗi 4 điểm: Nội dung, Yêu cầu chụp hình, Ghi nhận kết quả (Không/Nhập giá trị/Đạt-Không đạt), Từ khoá, Hướng dẫn, Công thức, Kiểm tra định dạng | Functional | High | ✅ | 07105#500-525 |
| R-SS-42 | Button Lưu: điều kiện giống như thiết lập từng bước (≥1 nội dung + công thức hợp lệ nếu có) | Functional | High | ✅ | 07105#522-525 |

### Update 11-02-2026: Cột QC xã vải
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-SS-43 | Khi tạo/cập nhật tiêu chí: bổ sung thêm thông tin "QC xã vải / Fabric relaxation QC" | Functional | High | ✅ | 07105#1083-1086 |
| R-SS-44 | "QC xã vải" dùng để tạo yêu cầu đánh giá xã vải khi UID group được TF vào location "F0-XV" | Functional | High | ✅ | 07105#1087-1089 |
| R-SS-45 | Ví dụ: SKU có 5 tiêu chí nhưng chỉ 2 tiêu chí bật "QC xã vải" → chỉ sinh yêu cầu đánh giá cho 2 tiêu chí đó | Functional | High | ✅ | 07105#1091-1093 |
| R-SS-46 | 90% vải còn lại sau khi nhận 10% và đánh giá Đạt đều phải qua khâu Xã vải trước khi đưa vào sản xuất | Functional | High | ✅ | 07105#1094-1096 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User có quyền QC management.
- Đã có tiêu chí trong hệ thống.

### Luồng chuẩn (Happy Path)
1. User vào Menu: Inbound / Quality control → Tab "Thiết lập SKU".
2. User chọn "Tạo mới".
3. Bước 1: Chọn sản phẩm, thời điểm đánh giá, tần suất, ghi chú → "Tiếp tục".
4. Bước 2: Chọn tiêu chí, cấu hình loại đánh giá, yêu cầu chụp hình, phân loại.
5. Nếu phân loại = "Theo từng bước" hoặc "Lỗi 4 điểm" → mở modal thiết lập chi tiết.
6. Sau khi thêm đủ tiêu chí → "Yêu cầu duyệt" → status chuyển "Chờ duyệt".

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 – Lưu tạm:** User chọn "Lưu" để lưu giữ chỗ, chưa yêu cầu duyệt.
- **Alt-Flow 2 – Tiêu chí bị inactive:** Tiêu chí trong SKU bị inactive → tự xoá khỏi danh sách (nếu status = Open/Waiting) hoặc ẩn đi (nếu status = Approved).

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1:** SKU đã có thiết lập Active → thông báo lỗi khi chọn SKU.
- **Exc-Flow 2:** Công thức không hợp lệ → button Lưu disabled.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| Sản phẩm | SKU/Barcode/tên | Có | Unique active: 1 SKU chỉ có 1 thiết lập active |
| Thời điểm đánh giá | Enum | Có | Phase này chỉ hỗ trợ "Sau khi nhận PO" |
| Tần suất đánh giá | Enum | Có | Phase này chỉ hỗ trợ "Tất cả PO" |
| Loại đánh giá = | Số | Có | > 0; bắt buộc đơn vị tính |
| Loại đánh giá Trong khoảng | Số từ/đến | Có | > 0; bắt buộc đơn vị tính |
| Số bước (Theo từng bước) | Số 1–10 | Có | Số đã chọn bị disable |
| Từ khoá | Text | Có (nếu ghi nhận kết quả ≠ Không) | In hoa tự động; không khoảng trắng; cho phép "_", "-", "." |
| 1 tiêu chí = 1 điều kiện | — | — | Nút Thêm (+) disable sau khi đã thêm 1 điều kiện |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
| Tình huống | VN | EN |
|:-----------|:---|:---|
| Chưa chọn sản phẩm | Thông tin này là bắt buộc. | This information is required. |
| SKU đã có thiết lập Active | SKU [code] đã tồn tại và đang hoạt động trên hệ thống. | SKU [code] already exists and is active in the system. |
| Chưa chọn thời điểm đánh giá | Thông tin này là bắt buộc. | This information is required. |
| Chưa chọn tần suất đánh giá | Thông tin này là bắt buộc. | This information is required. |
| SKU đã active khi nhấn Tiếp tục | SKU đã được thiết lập và đang hoạt động. | SKU has been set up and is currently active |
| Tiêu chí đã tồn tại trong danh sách | Tiêu chí đã tồn tại trong danh sách. | Criteria already exists in the list. |
| DEACTIVATE setup | — | Do you want to DEACTIVATE setup by SKU [code]? |
| ACTIVATE setup | — | Do you want to ACTIVATE setup by SKU [code]? |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-SS-01: 1 SKU không thể có 2 thiết lập Active**
  - **Given:** SKU A đã có thiết lập Active
  - **When:** User tạo thiết lập mới cho SKU A và nhấn "Tiếp tục"
  - **Then:** Hệ thống hiển thị lỗi "SKU đã được thiết lập và đang hoạt động."

- **AC-SS-02: Tiêu chí Theo từng bước tự chuyển modal**
  - **Given:** User đang ở màn hình thiết lập tiêu chí cho SKU
  - **When:** User thêm tiêu chí có phân loại = "Theo từng bước"
  - **Then:** Hệ thống tự động mở modal thiết lập các bước

- **AC-SS-03: Nút Thêm (+) disable sau khi thêm 1 điều kiện**
  - **Given:** Tiêu chí với loại đánh giá = "Theo điều kiện"
  - **When:** User đã thêm 1 điều kiện
  - **Then:** Nút Thêm (+) bị disable

- **AC-SS-04: Tiêu chí inactive tự xoá khỏi danh sách Open**
  - **Given:** Thiết lập SKU có status = Open, chứa tiêu chí A
  - **When:** Tiêu chí A bị Inactive
  - **Then:** Tiêu chí A bị xoá khỏi danh sách tiêu chí của SKU đó

- **AC-SS-05: Tiêu chí inactive ẩn với Approved**
  - **Given:** Thiết lập SKU có status = Approved, chứa tiêu chí A
  - **When:** Tiêu chí A bị Inactive
  - **Then:** Tiêu chí A không hiển thị trong thiết lập SKU (không xoá, chỉ ẩn)

- **AC-SS-06: QC xã vải chỉ sinh cho tiêu chí được bật**
  - **Given:** SKU có 5 tiêu chí, chỉ 2 tiêu chí bật "QC xã vải"
  - **When:** UID group của SKU được TF vào location F0-XV
  - **Then:** Hệ thống chỉ sinh 2 yêu cầu đánh giá xã vải (không phải 5)

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-SS-01 | R-SS-25 | Loại đánh giá "Công thức" — rules cụ thể là gì? Source ghi "sẽ bổ sung sau khi trao đổi với Dev" | BA/Dev | Open | | | |
| Q-SS-02 | R-SS-15 | "Khi nhận PO" hiện chưa hỗ trợ — có timeline dự kiến không? Có cần viết test case blocked cho value này không? | BA | Open | | | |

## 📝 Thay đổi so với version cũ
| Change ID | Loại | Nội dung | Version cũ | Version mới | R/AC ảnh hưởng | Trạng thái |
|:----------|:-----|:---------|:-----------|:------------|:---------------|:-----------|
| CHG-SS-01 | Add | 17-09-2025: Thiết lập đánh giá từng bước | ver1.0 | ver1.1 | R-SS-34~39 | Draft |
| CHG-SS-02 | Add | 27-09-2025: Thiết lập nội dung Lỗi 4 điểm | ver1.1 | ver1.2 | R-SS-40~42 | Draft |
| CHG-SS-03 | Update | Update 05-08-2025: tiêu chí inactive → xoá/ẩn trong SKU setup | — | ver1.2 | R-SS-32~33 | Draft |
| CHG-SS-04 | Add | Update 11-02-2026: cột QC xã vải | ver1.3 | ver1.4 | R-SS-43~46 | Draft |

## 🔎 Impact Analysis & Regression Proposal
| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:-----|
| CHG-SS-04 | quality_control_sku_setup, quality_control_fabric_mobile | — | Add | QC xã vải trigger | Blocked by Gate 1 |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-SS-09 / AC-SS-01 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-SS-34 / AC-SS-02 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-SS-26 / AC-SS-03 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-SS-32 / AC-SS-04 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-SS-33 / AC-SS-05 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-SS-45 / AC-SS-06 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-SS-25 (Công thức) | | ❌ Blocked | Chờ Q-SS-01 |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo spec từ 07105 ver1.5, section Thiết lập tiêu chí cho SKU | 07105#217-526, #1081-1096 |
