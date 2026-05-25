---
tags: [qa/requirement, qa/feature-group/quality-control]
status: Draft
created: 2026-05-25
updated: 2026-05-25
feature: quality_control_setup_sku
project: project_hasaki
source_version: v1.5
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Quality Control — Thiết lập tiêu chí cho SKU (Web)

## Tổng quan
- **Mã tính năng:** quality_control_setup_sku
- **Feature:** Gán tiêu chí đánh giá chất lượng cho từng SKU, thiết lập thời điểm và tần suất đánh giá
- **Mô tả ngắn:** Tab "Thiết lập SKU" (Setup criteria by SKU) trong menu Inbound / Quality Control — cho phép tạo thiết lập gán tiêu chí QC cho SKU, xác định thời điểm đánh giá, tần suất, loại đánh giá. Sau khi hoàn thành thiết lập, gửi yêu cầu duyệt.
- **Source chính:** `raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.md` — mục "Thiết lập tiêu chí cho SKU", "Tạo tiêu chí cho SKU", "17-09-2025: thiết lập đánh giá từng bước"
- **Đối tượng sử dụng (Actors):** QC Staff (Web), Quản lý kho
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** —
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[wiki/project_hasaki/features/quality_control_setup_criteria|Setup Criteria]] — tiêu chí phải tồn tại trước khi gán cho SKU
  - ➡️ [[wiki/project_hasaki/features/quality_control_approve|Duyệt/Từ chối]] — sau khi hoàn thành thiết lập SKU, gửi yêu cầu duyệt

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted from PDF) | `07105_Quality_Control_Docs_ver1.5.md` | v1.5 | ✅ Hiện hành |
| 2 | Figma | `https://www.figma.com/design/CLtzJtUv6sA4rxyaBPnbz5/34.-Quality-Control` | — | ❓ Chưa đọc được |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | — | — | Không có API explicit | N/A |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Menu: Inbound / Quality Control — Tab "Thiết lập SKU" (Setup criteria by SKU) | Functional | High | ✅ | v1.5, mục Thiết lập tiêu chí cho SKU |
| R2 | Filter: SKU/Barcode/Tên sản phẩm | Functional | Medium | ✅ | v1.5, Filter |
| R3 | Filter: Category, Brand, Active, Status, Thời điểm đánh giá, Tần suất đánh giá, Date range | Functional | Low | ✅ | v1.5, Filter |
| R4 | Listing: TT, Sản phẩm (SKU–Tên), Category, Brand, Thời điểm đánh giá, Tần suất đánh giá, Số lượng tiêu chí, Active, Status, Người tạo, Người cập nhật, Thao tác | Functional | High | ✅ | v1.5, Listing |
| R5 | Active/Inactive thiết lập SKU → popup xác nhận "Do you want to DEACTIVATE setup by SKU [mã]?" / "Do you want to ACTIVATE setup by SKU [mã]?" | Functional | High | ✅ | v1.5, Listing |
| R6 | Tại 1 thời điểm, 1 SKU không thể cùng active 2 thiết lập — phải inactive cái cũ trước khi active cái mới | Business Rule | High | ✅ | v1.5, Listing note |
| R7 | Tạo tiêu chí cho SKU — Trường Sản phẩm: bắt buộc, tìm theo SKU/barcode/tên, nếu chưa chọn → lỗi "Thông tin này là bắt buộc." / "This information is required." | Functional | High | ✅ | v1.5, Tạo tiêu chí |
| R8 | Tạo: Nếu SKU đã được thiết lập và đang Active → lỗi "SKU [mã] đã tồn tại và đang hoạt động trên hệ thống." / "SKU [mã] already exists and is active in the system." | Functional | High | ✅ | v1.5, Tạo tiêu chí |
| R9 | Tạo: Thời điểm đánh giá — bắt buộc; Phase này chỉ hỗ trợ "Sau khi nhận PO / After receive of PO" | Functional | High | ✅ | v1.5, Tạo tiêu chí |
| R10 | Tạo: Tần suất đánh giá — bắt buộc; Giá trị: "Tất cả PO / All PO" (auto sinh VAS sau nhận) hoặc "Ngẫu nhiên / Random" (chưa hỗ trợ phase này) | Functional | High | ✅ | v1.5, Tạo tiêu chí |
| R11 | Thêm tiêu chí vào danh sách: chọn tiêu chí (required, tìm từ 3 ký tự), Yêu cầu chụp hình (Yes/No, required), Hình chụp mẫu (tối đa 3 hình, không bắt buộc) | Functional | High | ✅ | v1.5, Tạo tiêu chí cho SKU |
| R12 | Loại đánh giá: "Đạt/Không đạt" (mặc định, phân loại = Bình thường, không cho chỉnh sửa phân loại) hoặc "Theo điều kiện" (=, >, >=, <, <=, between, công thức) | Functional | High | ✅ | v1.5, Loại đánh giá |
| R13 | Loại đánh giá "Theo điều kiện" — điều kiện =: Giá trị (số >0, bắt buộc), Đơn vị tính (text, bắt buộc), Sai số (số >0, không bắt buộc) | Functional | High | ✅ | v1.5, Loại đánh giá |
| R14 | Loại đánh giá "Theo điều kiện" — điều kiện >, >=, <, <=: Giá trị (số >0, bắt buộc), Đơn vị tính (text, bắt buộc) | Functional | High | ✅ | v1.5, Loại đánh giá |
| R15 | Loại đánh giá "Theo điều kiện" — điều kiện between: Giá trị từ…đến (số >0, bắt buộc), Đơn vị tính (text, bắt buộc) | Functional | High | ✅ | v1.5, Loại đánh giá |
| R16 | Hiện tại 1 tiêu chí chỉ hỗ trợ 1 điều kiện duy nhất — sau khi thêm 1 điều kiện, nút Thêm (+) bị disable; xóa điều kiện thì nút Thêm (+) hiện lại | Business Rule | High | ✅ | v1.5, Loại đánh giá note |
| R17 | Phân loại (Type): Bình thường / Lỗi 4 điểm / Theo từng bước | Functional | High | ✅ | v1.5, Phân loại |
| R18 | Nếu tiêu chí đã tồn tại trong danh sách khi thêm → lỗi "Tiêu chí đã tồn tại trong danh sách." / "Criteria already exists in the list." | Functional | High | ✅ | v1.5, Tạo tiêu chí |
| R19 | Button "Lưu" — lưu tạm để tiếp tục sau | Functional | Medium | ✅ | v1.5, Tạo tiêu chí |
| R20 | Button "Yêu cầu duyệt" (Hoàn thành) — chuyển trạng thái thiết lập SKU sang "Chờ duyệt" | Functional | High | ✅ | v1.5, Tạo tiêu chí |
| R21 | Thiết lập theo từng bước (Type = "Theo từng bước"): modal thiết lập các bước; Bước 1–10 (số đã chọn disabled); Nội dung (tên bước); Yêu cầu chụp hình; Hình ảnh mẫu; Ghi nhận kết quả (Không/Nhập giá trị/Đạt-Không đạt) | Functional | High | ✅ | v1.5, 17-09-2025 |
| R22 | Từ khoá (Keywords): chỉ hiện khi Ghi nhận kết quả ≠ Không | Functional | Medium | ✅ | v1.5, 17-09-2025 |
| R23 | Nếu tiêu chí có type = "Theo từng bước" thì khi add vào SKU tự động mở màn hình thiết lập bước | Functional | Medium | ✅ | v1.5, 17-09-2025 |
| R24 | Nếu trạng thái SKU = Open/Waiting for Approval và tiêu chí bị inactive → tiêu chí tự xóa khỏi danh sách thiết lập | Business Rule | High | ✅ | v1.5, Update 05-08-2025 |
| R25 | Nếu trạng thái SKU = Approved và tiêu chí bị inactive → tiêu chí không hiển thị cho SKU (không xóa) | Business Rule | High | ✅ | v1.5, Update 05-08-2025 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- Tồn tại ít nhất 1 tiêu chí Active trong hệ thống
- User có quyền Inbound / Quality Control

### Luồng chuẩn (Happy Path)
1. User vào Inbound / Quality Control / Tab Thiết lập SKU
2. Chọn "Tạo mới"
3. Chọn SKU (tìm theo SKU/barcode/tên)
4. Chọn Thời điểm đánh giá = "Sau khi nhận PO"
5. Chọn Tần suất = "Tất cả PO"
6. Thêm tiêu chí: chọn tiêu chí, cài Yêu cầu chụp hình, Loại đánh giá, Phân loại
7. Nếu type = "Theo từng bước" → thiết lập bước trong modal
8. Chọn "Yêu cầu duyệt" → trạng thái chuyển sang "Chờ duyệt"

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 — Lưu tạm:** User chọn "Lưu" để lưu draft, tiếp tục sau
- **Alt-Flow 2 — Thêm nhiều tiêu chí:** Lặp bước 6 nhiều lần cho cùng 1 SKU

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1 — SKU đang Active:** Lỗi "SKU đã tồn tại và đang hoạt động." — không cho tạo thiết lập mới
- **Exc-Flow 2 — Tiêu chí trùng:** Lỗi "Tiêu chí đã tồn tại trong danh sách." — không thêm
- **Exc-Flow 3 — Tiêu chí bị inactive khi đang Open/Waiting:** Auto xóa khỏi danh sách

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu

| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| Sản phẩm (SKU) | SKU/Barcode/Tên | ✅ | Unique active — không tồn tại active cùng lúc 2 thiết lập |
| Thời điểm đánh giá | Select | ✅ | Phase này: chỉ "Sau khi nhận PO" |
| Tần suất đánh giá | Select | ✅ | "Tất cả PO" hoặc "Ngẫu nhiên" (chưa hỗ trợ) |
| Tiêu chí (trong list) | Select | ✅ | Phải là tiêu chí Active; tìm từ 3 ký tự |
| Yêu cầu chụp hình | Yes/No | ✅ | — |
| Hình chụp mẫu | Image | Không | Tối đa 3 hình |
| Giá trị điều kiện | Số | Theo loại | > 0 |
| Đơn vị tính | Text | Theo loại | Bắt buộc khi có điều kiện số |
| Số bước | 1–10 | — | Số đã chọn không cho chọn lại |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi

| Tình huống | VN | EN |
|:-----------|:---|:---|
| Trường bắt buộc chưa chọn | Thông tin này là bắt buộc. | This information is required. |
| SKU đang Active | SKU [mã] đã tồn tại và đang hoạt động trên hệ thống. | SKU [mã] already exists and is active in the system. |
| SKU has been set up and active | SKU đã được thiết lập và đang hoạt động. | SKU has been set up and is currently active. |
| Tiêu chí trùng trong danh sách | Tiêu chí đã tồn tại trong danh sách. | Criteria already exists in the list. |
| Deactivate SKU setup | Do you want to DEACTIVATE setup by SKU [mã]? | — |
| Activate SKU setup | Do you want to ACTIVATE setup by SKU [mã]? | — |

## 🏁 Tiêu Chí Nghiệm Thu (BDD)

- **Scenario 1: Tạo thiết lập cho SKU chưa có thiết lập Active**
  - **Given:** SKU chưa có thiết lập QC Active
  - **When:** User tạo mới, chọn SKU, điền đủ thông tin, chọn "Yêu cầu duyệt"
  - **Then:** Thiết lập chuyển sang "Chờ duyệt"

- **Scenario 2: Không cho tạo khi SKU đang Active**
  - **Given:** SKU có thiết lập QC đang Active
  - **When:** User tạo mới và chọn SKU đó
  - **Then:** Hiện lỗi "SKU đã tồn tại và đang hoạt động trên hệ thống."

- **Scenario 3: Tiêu chí bị inactive khi SKU ở trạng thái Open**
  - **Given:** Thiết lập SKU status = Open, có tiêu chí TC001 trong danh sách
  - **When:** TC001 bị Inactive ở màn hình tiêu chí
  - **Then:** TC001 tự động bị xóa khỏi danh sách tiêu chí của SKU

- **Scenario 4: Thêm tiêu chí type "Theo từng bước"**
  - **Given:** User thêm tiêu chí có phân loại = "Theo từng bước"
  - **When:** Tiêu chí được thêm vào danh sách
  - **Then:** Tự động mở modal thiết lập các bước

- **Scenario 5: Giới hạn 1 điều kiện cho tiêu chí**
  - **Given:** User đã thêm 1 điều kiện cho tiêu chí
  - **When:** Nhìn vào nút Thêm (+)
  - **Then:** Nút Thêm (+) bị disable

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn | Ngày |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:------|:-----|
| Q-001 | R9 | "Khi nhận PO" chưa hỗ trợ — UI hiển thị option này ở trạng thái disabled hay ẩn hoàn toàn? | PO | Open | | | |
| Q-002 | R10 | "Ngẫu nhiên" chưa hỗ trợ — UI hiển thị disabled hay ẩn hoàn toàn? | PO | Open | | | |
| Q-003 | R12 | "Công thức" trong Loại đánh giá — doc ghi "sẽ bổ sung rules sau khi trao đổi với Dev". Phase này có hay không? | PO/Dev | Open | | | |
| Q-004 | R17 | "Lỗi 4 điểm" — quy trình đặc thù là gì? Spec phần 27-09-2025 chưa được đọc đầy đủ | BA | Open | | | |
| Q-005 | R20 | Status flow đầy đủ của thiết lập SKU: Open → Waiting for Approval → Approved → ? Còn Rejected không? | PO | Open | | | |
| Q-006 | R21 | Tối đa bao nhiêu bước trong "Thiết lập theo từng bước"? Doc đề cập số 1–10 nhưng cần xác nhận giới hạn trên | BA/Dev | Open | | | |

## 📝 Thay đổi so với version cũ
| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | R/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:---------------|:-----------|
| CHG-001 | Add | Feature mới | — | v1.0 | All | Done |
| CHG-002 | Add | Yêu cầu chụp hình + Hình chụp mẫu + Đánh giá theo điều kiện | v1.0 | v1.1 | R11, R12 | Done |
| CHG-003 | Add | Thiết lập đánh giá từng bước | v1.1 | v1.2 17-09-2025 | R21, R22, R23 | Done |
| CHG-004 | Add | Rules khi tiêu chí bị inactive | v1.2 | v1.5 05-08-2025 | R24, R25 | Done |

## 🔎 Impact Analysis & Regression Proposal
| Change ID | Affected Feature(s) | Affected Test Suite(s) | TC action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:----------|:----------------------|:----------------------|
| All | quality_control_setup_sku | — | Add (mới) | — | Q-001, Q-002, Q-003, Q-005 |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R1–R25 | — | ❌ Blocked | Chờ Gate 1 |
| R9 (Khi nhận PO) | — | ❌ Blocked | Chờ Q-001 |
| R10 (Ngẫu nhiên) | — | ❌ Blocked | Chờ Q-002 |
| R12 (Công thức) | — | ❌ Blocked | Chờ Q-003 |
| R17 (Lỗi 4 điểm) | — | ❌ Blocked | Chờ Q-004 |
| R20 (Status flow) | — | ❌ Blocked | Chờ Q-005 |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-25 00:00:00 | v1.0 | Khởi tạo từ 07105_Quality_Control_Docs_ver1.5.md | Raw ingest |
