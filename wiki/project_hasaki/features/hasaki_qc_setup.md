---
aliases: [QC Setup, Thiết lập tiêu chí chất lượng, hasaki_qc_setup]
tags: [qa/requirement, qa/feature-group/receiving-po]
status: Draft
created: 2026-05-23
updated: 2026-05-23
feature: hasaki_qc_setup
project: project_hasaki
source_version: v1.5
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Thiết lập Tiêu chí Kiểm soát Chất lượng (QC Setup)

## Tổng quan
- **Mã tính năng:** hasaki_qc_setup
- **Feature:** QC Setup — Thiết lập tiêu chí và thiết lập tiêu chí cho SKU
- **Mô tả ngắn:** Quản lý danh mục tiêu chí đánh giá chất lượng (Web) và cấu hình tiêu chí theo từng SKU với workflow duyệt/từ chối. Bao gồm 3 loại phân loại tiêu chí: Bình thường, Lỗi 4 điểm, Theo từng bước. Tích hợp VAS type mới và cột QC xã vải.
- **Source chính:** `raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.pdf`
- **Đối tượng sử dụng (Actors):** QC Staff (Web), QC Lead / Approver (duyệt SKU), Admin (import tiêu chí)
- **Test Suite tương ứng:** [[wiki/project_hasaki/test_suites/test_hasaki_qc_setup]]
- **Mối quan hệ:**
  - ➡️ [[wiki/project_hasaki/features/hasaki_qc_evaluation|#6 QC Evaluation]] — Tiêu chí thiết lập ở đây được dùng trực tiếp khi đánh giá chất lượng; SKU thiết lập "Tất cả PO" → tự sinh VAS QC sau phiên nhận
  - ➡️ [[wiki/project_hasaki/features/hasaki_receiving_vas|#3 VAS]] — QC Setup cập nhật VAS type mới (IMEI/RFID/Quality Control/Other) và các trạng thái VAS bổ sung; cột "QC xã vải" trong tiêu chí điều khiển sinh yêu cầu đánh giá Xã vải
  - ℹ️ [[wiki/project_hasaki/features/hasaki_receiving_po_app|#2 App PO Receiving]] — Tần suất đánh giá "Tất cả PO" kích hoạt sinh VAS sau khi kết thúc phiên nhận trên App

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | PDF | 07105_Quality_Control_Docs_ver1.5.pdf | v1.5 | ✅ Hiện hành |
| 2 | Link | Figma: CLtzJtUv6sA4rxyaBPnbz5 / node 366-229 | — | ✅ Hiện hành |
| 3 | Link | Figma: node 1946-1696 (Update 11-02-2026) | — | ✅ Hiện hành |

## Phân rã Requirement
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Màn hình Tab Thiết lập tiêu chí hỗ trợ filter theo Mã/Tên (≥3 ký tự, tìm gần đúng), trạng thái Active, và khoảng ngày tạo | Functional | High | ✅ | PDF v1.5, mục Thiết lập tiêu chí |
| R2 | Listing tiêu chí hiển thị: TT, Mã, Tên, Mô tả, Hướng dẫn, Đang hoạt động, Người tạo, Người cập nhật, Thao tác | Functional | High | ✅ | PDF v1.5, mục Thiết lập tiêu chí |
| R3 | Toggle Active/Inactive tiêu chí phải hiện popup xác nhận; mặc định tiêu chí mới là Active | Functional | High | ✅ | PDF v1.5, listing |
| R4 | Tạo tiêu chí: Mã tiêu chí và Tên tiêu chí là bắt buộc, không được trùng; có 3 nút Đóng / Lưu và đóng / Lưu và tiếp tục | Functional | High | ✅ | PDF v1.5, mục Tạo tiêu chí |
| R5 | Import tiêu chí validate trùng mã/tên trên hệ thống và trong file; reuse page import dùng chung | Functional | Medium | ✅ | PDF v1.5, mục Import tiêu chí |
| R6 | Tab Thiết lập SKU hỗ trợ filter theo SKU/Barcode/Tên sản phẩm, Category, Brand, Active/Inactive, Assessment time, Assessment frequency, khoảng ngày tạo | Functional | High | ✅ | PDF v1.5, mục Thiết lập tiêu chí cho SKU |
| R7 | Listing Thiết lập SKU hiển thị: TT, Sản phẩm, Danh mục, Thương hiệu, Thời điểm đánh giá, Tần suất đánh giá, Số lượng tiêu chí, Đang hoạt động, Người tạo, Người cập nhật, Trạng thái, Thao tác | Functional | High | ✅ | PDF v1.5, listing SKU |
| R8 | 1 SKU không thể cùng lúc có 2 thiết lập Active; phải Inactive cái cũ trước khi Active cái mới | Functional | High | ✅ | PDF v1.5, mục Thiết lập SKU |
| R9 | Tạo thiết lập SKU: Sản phẩm, Thời điểm đánh giá (bắt buộc chọn "Sau khi nhận PO"), Tần suất đánh giá (bắt buộc chọn "Tất cả PO" hoặc "Ngẫu nhiên") là bắt buộc | Functional | High | ✅ | PDF v1.5, mục Tạo tiêu chí cho SKU |
| R10 | Mỗi tiêu chí thêm vào SKU cần chọn: tiêu chí (search ≥3 ký tự), Yêu cầu chụp hình (Yes/No), Hình chụp mẫu (≤3 hình, không bắt buộc), Loại đánh giá, Phân loại, Mô tả | Functional | High | ✅ | PDF v1.5, mục thiết lập tiêu chí cho SKU |
| R11 | Loại đánh giá "Đạt/Không đạt" → Phân loại mặc định = Bình thường, không cho sửa | Functional | High | ✅ | PDF v1.5 |
| R12 | Loại đánh giá "Theo điều kiện" cho phép cấu hình: phép so sánh (=, >, >=, <, <=, between), Giá trị (số > 0), Đơn vị tính (text), Sai số cho phép; mỗi tiêu chí chỉ hỗ trợ 1 điều kiện | Functional | High | ✅ | PDF v1.5 |
| R13 | Phân loại "Bình thường": đánh giá theo quy trình chuẩn | Functional | High | ✅ | PDF v1.5 |
| R14 | Phân loại "Lỗi 4 điểm": khi thêm vào SKU, tự động mở modal thiết lập nội dung (Content, Yêu cầu chụp hình, Ghi nhận kết quả, Từ khoá, Hướng dẫn, Công thức) | Functional | High | ✅ | PDF v1.5, update 27-09-2025 |
| R15 | Phân loại "Theo từng bước": khi thêm vào SKU, tự động mở modal thiết lập các bước (Bước 1–10, Nội dung, Yêu cầu chụp hình, Hình ảnh mẫu, Ghi nhận kết quả, Từ khoá, Hướng dẫn, Công thức); nút Lưu chỉ enable khi có ≥1 bước và công thức hợp lệ | Functional | High | ✅ | PDF v1.5, update 17-09-2025 |
| R16 | Công thức (Formula) có nút Kiểm tra định dạng: hợp lệ = chữ xanh lá, không hợp lệ = chữ đỏ; khi nhấn Lưu mà chưa kiểm tra thì tự động validate lại | Functional | Medium | ✅ | PDF v1.5 |
| R17 | Nếu tiêu chí bị Inactive trong khi SKU đang Open/Waiting for Approval → xóa tiêu chí khỏi danh sách; nếu SKU đang Approved → tiêu chí không hiển thị | Functional | High | ✅ | PDF v1.5, update 05-08-2025 |
| R18 | Workflow duyệt SKU: Chọn "Hoàn thành" → trạng thái chuyển "Chờ duyệt"; Approver có thể Duyệt (→ Đã duyệt) / Từ chối (→ Từ chối) / Mở lại (→ Open); hỗ trợ duyệt/từ chối nhiều dòng cùng lúc | Functional | High | ✅ | PDF v1.5, mục Duyệt/Từ chối |
| R19 | Button Edit và Delete chỉ hiện với status Mới (New/Open); button Xem chi tiết/Duyệt dùng cho Chờ duyệt | Functional | Medium | ✅ | PDF v1.5 |
| R20 | VAS bổ sung VAS type mới: IMEI, RFID, Quality Control, Other; filter và cột listing hiển thị; nếu VAS vừa có Quality Control vừa có RFID/IMEI thì hiển thị cả 2 cách nhau bởi dấu phẩy | Functional | High | ✅ | PDF v1.5, VAS updated |
| R21 | VAS bổ sung trạng thái mới: Chờ duyệt (Waiting for approval), Chờ dán ID (Waiting for paste ID), Chờ đánh giá (Waiting quality control), Chờ NCC đến lấy (Waiting vendor to pick), Đã trả NCC (Returned to vendor) | Functional | High | ✅ | PDF v1.5, VAS updated |
| R22 | VAS status "Chờ duyệt": cho phép Nhận hàng (→ Chờ dán ID nếu có IMEI/RFID, hoặc Completed), Trả NCC (→ Chờ NCC đến lấy), Mở lại (→ Open/New) | Functional | High | ✅ | PDF v1.5, VAS updated |
| R23 | Cột "QC xã vải" (Fabric relaxation QC) bổ sung vào thiết lập tiêu chí; tiêu chí có bật QC xã vải sẽ tự động sinh yêu cầu đánh giá khi UID group được TF vào location F0-XV hoặc type "Xã vải" | Functional | High | ✅ | PDF v1.5, update 11-02-2026 |
| R24 | Update 10-05-2026: Khi tạo tiêu chí với Phân loại "Lỗi 4 điểm" hoặc "Theo từng bước", hệ thống mở màn hình thiết lập nội dung ngay tại màn hình thiết lập tiêu chí (không chỉ ở màn hình thiết lập cho SKU); khi add tiêu chí cho SKU sẽ tự kế thừa thiết lập đó | Functional | Medium | ✅ | PDF v1.5, update 10-05-2026 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User đã login hệ thống WMS với quyền truy cập Menu: Inbound / Quality control
- Đối với Duyệt SKU: user phải có quyền Approver

### Luồng chuẩn (Happy Path) — Tạo tiêu chí và cấu hình cho SKU

**A. Quản lý Tiêu chí (Tab Thiết lập tiêu chí)**
1. Vào Menu Inbound → Quality control → Tab Thiết lập tiêu chí
2. Nhấn "Tạo mới" → popup hiện ra
3. Nhập Mã tiêu chí (bắt buộc, unique), Tên tiêu chí (bắt buộc, unique), Mô tả (optional), Hướng dẫn (optional)
4. Nếu phân loại là "Lỗi 4 điểm" hoặc "Theo từng bước" (update 10-05-2026): hệ thống mở màn hình thiết lập nội dung chi tiết
5. Nhấn "Lưu và đóng" → tiêu chí được tạo với trạng thái Active
6. Hiển thị trong danh sách

**B. Cấu hình Tiêu chí cho SKU (Tab Thiết lập SKU)**
1. Chọn Tab Thiết lập SKU → Tạo mới
2. Tìm và chọn SKU (theo SKU/barcode/tên)
3. Chọn Thời điểm đánh giá = "Sau khi nhận PO", Tần suất = "Tất cả PO"
4. Nhấn Tiếp tục → màn hình cấu hình tiêu chí
5. Thêm từng tiêu chí: chọn tiêu chí, cấu hình Yêu cầu chụp hình, Hình mẫu, Loại đánh giá, Phân loại, Mô tả
   - Nếu Phân loại = "Theo từng bước" → tự động mở modal thiết lập bước
   - Nếu Phân loại = "Lỗi 4 điểm" → tự động mở modal thiết lập nội dung lỗi (hoặc kế thừa từ tiêu chí nếu đã cấu hình sẵn)
6. Nhấn Thêm → tiêu chí vào danh sách
7. Nhấn "Lưu" để lưu nháp hoặc "Yêu cầu duyệt" → trạng thái chuyển "Chờ duyệt"

**C. Workflow Duyệt SKU**
1. Approver vào Tab Thiết lập SKU → filter trạng thái "Chờ duyệt"
2. Chọn 1 hoặc nhiều dòng → nhấn Duyệt → popup xác nhận → Yes → trạng thái = "Đã duyệt"
3. Hoặc nhấn Từ chối → trạng thái = "Từ chối" → QC Staff có thể Mở lại (Reopen → Open)

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 — Import tiêu chí hàng loạt:** Tại Tab Thiết lập tiêu chí → Import → upload file template → hệ thống validate trùng mã/tên (trong file và trên hệ thống) → import thành công các dòng hợp lệ
- **Alt-Flow 2 — Cập nhật tiêu chí đã tồn tại:** Chọn icon Edit trên dòng tiêu chí → sửa (không được đổi Mã) → Lưu → cập nhật Người cập nhật và thời gian
- **Alt-Flow 3 — Tần suất "Ngẫu nhiên":** SKU thiết lập Ngẫu nhiên → không tự động sinh VAS; user tự tạo phiên đánh giá thủ công (chưa hỗ trợ ở phase này)
- **Alt-Flow 4 — VAS Chờ duyệt → Nhận hàng (pass QC):** Approver vào chi tiết VAS → Nhận hàng → nếu SKU có IMEI/RFID → VAS chuyển "Chờ dán ID"; nếu không → "Completed"
- **Alt-Flow 5 — VAS Chờ duyệt → Trả NCC:** Nhập số lượng (mặc định = số lượng nhận, disabled ở phase này) → Xác nhận → VAS = "Chờ NCC đến lấy" → khi NCC đến lấy thì update = "Đã trả NCC"; sinh Outbound type Return vendor + ADJ type Vendor Return (Dev xác nhận chưa hỗ trợ ở phase này)
- **Alt-Flow 6 — QC xã vải:** UID group được TF vào location F0-XV hoặc location type "Xã vải" → hệ thống tự động sinh yêu cầu đánh giá cho các tiêu chí có bật "QC xã vải"

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1 — Mã/Tên tiêu chí trùng khi Tạo mới:** Hiện thông báo "Mã tiêu chí đã tồn tại." / "Tên tiêu chí đã tồn tại."
- **Exc-Flow 2 — SKU đã Active thiết lập:** Khi cố tạo mới cho SKU đang Active → "SKU 422280022 đã tồn tại và đang hoạt động trên hệ thống."
- **Exc-Flow 3 — Tiêu chí đã có trong danh sách SKU:** "Tiêu chí đã tồn tại trong danh sách."
- **Exc-Flow 4 — Công thức không hợp lệ:** Khi nhấn Lưu trong thiết lập bước → hệ thống validate công thức; nếu không hợp lệ → không cho lưu
- **Exc-Flow 5 — Tiêu chí bị Inactive trong khi SKU đang Open/Waiting:** Tiêu chí tự động bị xóa khỏi danh sách của SKU đó

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------|:---------|:----------|:-------------------------------|
| Mã tiêu chí | Text | ✅ | Unique trên hệ thống; không được sửa sau khi tạo |
| Tên tiêu chí | Text | ✅ | Unique trên hệ thống |
| Mô tả | Text | ❌ | — |
| Hướng dẫn | Text | ❌ | — |
| QC xã vải | Toggle Yes/No | ❌ | Nếu bật → tự sinh đánh giá xã vải khi UID TF vào F0-XV |
| Sản phẩm (SKU Setup) | Search | ✅ | Tìm theo SKU/barcode/tên; SKU đang Active không thể tạo thêm |
| Thời điểm đánh giá | Enum | ✅ | Sau khi nhận PO (Khi nhận PO chưa hỗ trợ) |
| Tần suất đánh giá | Enum | ✅ | Tất cả PO: tự sinh VAS; Ngẫu nhiên: user tự tạo (chưa hỗ trợ) |
| Yêu cầu chụp hình | Yes/No | ✅ | Per tiêu chí |
| Hình chụp mẫu | Image | ❌ | Upload ≤3 hình |
| Loại đánh giá | Enum | ✅ | Đạt/Không đạt (default Bình thường) hoặc Theo điều kiện |
| Phân loại | Enum | ✅ | Bình thường / Lỗi 4 điểm / Theo từng bước |
| Điều kiện (Theo điều kiện) | Số > 0 | ✅ | Phép so sánh: =, >, >=, <, <=, between; chỉ 1 điều kiện/tiêu chí |
| Đơn vị tính (Theo điều kiện) | Text | ✅ | — |
| Sai số cho phép | Số > 0 | ❌ | — |
| Số bước (Theo từng bước) | Integer 1–10 | ✅ | Số bước đã chọn → disable không cho chọn lại |
| Từ khoá (step/4-point) | Text | Conditional | Chỉ show khi Ghi nhận kết quả ≠ Không; tự động IN HOA, không khoảng trắng; cho phép `_`, `-`, `.` |
| Công thức | Text | ❌ | Phải pass "Kiểm tra định dạng" trước khi Lưu |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Trigger | Thông báo VN | Thông báo EN |
|:-------|:--------|:-------------|:-------------|
| ERR-QCS-01 | Mã tiêu chí trùng hệ thống | Mã tiêu chí đã tồn tại. | The criteria code already exists in the systems. |
| ERR-QCS-02 | Tên tiêu chí trùng hệ thống | Tên tiêu chí đã tồn tại. | The criteria name already exists in the systems. |
| ERR-QCS-03 | Mã tiêu chí trùng trong file import | Mã tiêu chí đã tồn tại trong file import. | The criteria code already exists in the template import. |
| ERR-QCS-04 | Tên tiêu chí trùng trong file import | Tên tiêu chí đã tồn tại trong file import. | The criteria name already exists in the template import. |
| ERR-QCS-05 | Thiếu trường bắt buộc (chung) | Thông tin này là bắt buộc. | This information is required. |
| ERR-QCS-06 | SKU đang Active đã tồn tại | SKU 422280022 đã tồn tại và đang hoạt động trên hệ thống. | SKU 422280022 already exists and is active in the system. |
| ERR-QCS-07 | Tiêu chí đã có trong danh sách SKU | Tiêu chí đã tồn tại trong danh sách. | Criteria already exists in the list. |
| ERR-QCS-08 | SKU đang Active khi Lưu | SKU đã được thiết lập và đang hoạt động. | SKU has been set up and is currently active. |
| ERR-QCS-09 | Công thức không hợp lệ | Công thức không hợp lệ (chữ đỏ) | (invalid formula — shown in red) |
| ERR-QCS-10 | Deactivate criterion confirm | — | Do you want to DEACTIVATE criterion 1001? |
| ERR-QCS-11 | Activate criterion confirm | — | Do you want to ACTIVATE criterion 1001? |
| ERR-QCS-12 | Approve SKU setup | — | Do you want to confirm APPROVE criteria setup for SKU 297500046? |
| ERR-QCS-13 | Reject SKU setup | — | Do you want to confirm REJECT criteria setup for SKU 297500046? |
| ERR-QCS-14 | Reopen SKU setup | — | Do you want to confirm RE-OPEN criteria setup for SKU 297500046? |
| ERR-QCS-15 | Approve multiple | — | Do you want to confirm APPROVE setting criteria for SKUs of all selected lines? |
| ERR-QCS-16 | VAS Receive confirm | — | Do you want to confirm RECEIVE for the quality control of VAS 1003241119000039? |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01: Tạo tiêu chí mới hợp lệ**
  - **Given:** User ở Tab Thiết lập tiêu chí, nhấn Tạo mới
  - **When:** Nhập Mã và Tên tiêu chí unique, nhấn "Lưu và đóng"
  - **Then:** Tiêu chí được tạo với trạng thái Active, hiện trong danh sách

- **AC-02: Tạo tiêu chí trùng mã**
  - **Given:** Đã có tiêu chí mã "TC001"
  - **When:** Tạo mới với mã "TC001"
  - **Then:** Hiện thông báo "Mã tiêu chí đã tồn tại." Không tạo mới

- **AC-03: Toggle Inactive tiêu chí có xác nhận**
  - **Given:** Tiêu chí đang Active trong danh sách
  - **When:** Nhấn toggle Inactive
  - **Then:** Hiện popup "Do you want to DEACTIVATE criterion ...?" → Yes → trạng thái = Inactive; No → giữ nguyên

- **AC-04: Tạo thiết lập SKU và yêu cầu duyệt**
  - **Given:** SKU chưa có thiết lập Active
  - **When:** Tạo mới, chọn SKU, điền đầy đủ trường bắt buộc, thêm ≥1 tiêu chí, nhấn "Yêu cầu duyệt"
  - **Then:** Trạng thái thiết lập chuyển "Chờ duyệt", không thể edit/delete

- **AC-05: Approve thiết lập SKU**
  - **Given:** Thiết lập SKU đang ở trạng thái "Chờ duyệt"
  - **When:** Approver nhấn Duyệt → xác nhận Yes
  - **Then:** Trạng thái chuyển "Đã duyệt"; hệ thống sẽ tự sinh VAS sau khi kết thúc phiên nhận PO

- **AC-06: Reject và Reopen thiết lập SKU**
  - **Given:** Thiết lập SKU đang "Chờ duyệt"
  - **When:** Approver nhấn Từ chối → Yes
  - **Then:** Trạng thái = "Từ chối"; QC Staff có thể nhấn Mở lại → trạng thái về "Open" để chỉnh sửa

- **AC-07: Thiết lập tiêu chí Theo từng bước**
  - **Given:** Khi thêm tiêu chí Phân loại = "Theo từng bước" vào SKU
  - **When:** Hệ thống tự mở modal thiết lập bước; user thiết lập ≥1 bước với nội dung, ghi nhận kết quả, hướng dẫn; nhấn Lưu
  - **Then:** Thiết lập bước được lưu; tiêu chí hiện trong danh sách SKU

- **AC-08: Cột QC xã vải tự sinh yêu cầu đánh giá**
  - **Given:** Tiêu chí có bật "QC xã vải" và SKU đã có thiết lập Approved
  - **When:** UID group được transfer vào location F0-XV hoặc location type "Xã vải"
  - **Then:** Hệ thống tự động sinh yêu cầu đánh giá Xã vải cho tiêu chí đó

- **AC-09: VAS type mới hiển thị đúng**
  - **Given:** VAS có type Quality Control + RFID
  - **When:** Xem danh sách VAS
  - **Then:** Cột VAS type hiển thị "Quality Control, RFID"

- **AC-10: Tiêu chí Inactive tự xóa khỏi SKU Open**
  - **Given:** Thiết lập SKU đang Open, có tiêu chí TC-X trong danh sách
  - **When:** TC-X bị Inactive
  - **Then:** TC-X bị xóa tự động khỏi danh sách tiêu chí của SKU đó

## ❓ Câu hỏi chưa rõ

- [ ] ❓ **R12 — Loại "Theo điều kiện" và "Công thức":** Spec ghi "Công thức: dùng để thiết lập công thức, trả kết quả và so sánh với điều kiện được thiết lập (sẽ bổ sung rules sau khi trao đổi với Dev)". Hiện tại rules công thức đã được chốt chưa? Cú pháp công thức là gì? Có ví dụ mẫu không? *(Hỏi Dev Lead)*

- [ ] ❓ **R9/Alt-Flow 3 — Tần suất "Ngẫu nhiên":** Spec ghi "chưa hỗ trợ ở phase này". Phase này là phase mấy? Dự kiến phát triển ở sprint nào? *(Hỏi PO)*

- [ ] ❓ **R22/Alt-Flow 5 — Trả NCC (Return to vendor):** Spec ghi "Tạo Adjustment type Vendor Return để trả nhà cung cấp — Dev xác nhận chưa thể tạo được". Tình trạng hiện tại ra sao? Khi nào sẽ hỗ trợ? Luồng tạm thời là gì? *(Hỏi Dev Lead)*

- [ ] ❓ **R18 — Bulk Approve/Reject:** Spec ghi hỗ trợ chọn nhiều dòng "Chờ duyệt". Số lượng dòng tối đa có thể chọn là bao nhiêu? Có phân trang không? *(Hỏi Dev Lead)*

- [ ] ❓ **R24 — Update 10-05-2026 kế thừa thiết lập:** Khi tiêu chí "Lỗi 4 điểm" / "Theo từng bước" đã cấu hình nội dung tại màn hình Tiêu chí, nhưng khi add vào SKU thì nội dung được kế thừa hoàn toàn hay QC Staff vẫn có thể chỉnh sửa thêm? *(Hỏi Dev Lead)*
- [ ] ❓ **R12 — Boundary giá trị điều kiện:** Với loại "Theo điều kiện", hệ thống có chặn giá trị 0 hoặc âm không? Nếu chặn, thông báo lỗi chính xác là gì?

## 📝 Thay đổi so với version cũ

| # | Nội dung thay đổi | Version cũ | Version mới | Ảnh hưởng TC |
|:--|:------------------|:----------|:-----------|:-------------|
| 1 | Bổ sung "Thiết lập đánh giá từng bước" cho tiêu chí | v1.1 | v1.2 (17-09-2025) | Cần TC mới cho Step-by-step |
| 2 | Bổ sung nội dung đánh giá cho tiêu chí lỗi 4 điểm | v1.2 | v1.3 (27-09-2025) | Cần TC mới cho 4-point error |
| 3 | Cột "QC xã vải" trong thiết lập tiêu chí; chụp hình tem pass/fail | v1.3 | v1.4 (11-02-2026) | TC mới cho QC xã vải |
| 4 | VAS bổ sung type mới và trạng thái mới; luồng Nhận hàng/Trả NCC | v1.3 | v1.4 (11-02-2026) | TC mới cho VAS flow |
| 5 | Thiết lập 4 điểm/từng bước ngay tại màn hình Tiêu chí (kế thừa cho SKU) | v1.4 | v1.5 (10-05-2026) | Update TC cho criteria setup |

## Test Coverage

| Requirement | Test Case(s) | Status |
|:-----------|:------------|:-------|
| R1–R3 | Chờ thiết kế | ❌ Chưa có |
| R4–R5 | Chờ thiết kế | ❌ Chưa có |
| R6–R9 | Chờ thiết kế | ❌ Chưa có |
| R10–R17 | Chờ thiết kế | ❌ Chưa có |
| R18–R19 | Chờ thiết kế | ❌ Chưa có |
| R20–R22 | Chờ thiết kế | ❌ Chưa có |
| R23–R24 | Chờ thiết kế | ❌ Chưa có |

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 21:49:34 | v1.1 | Bổ sung câu hỏi boundary R12 sau khi loại test case suy diễn khỏi Test Suite | [[wiki/project_hasaki/test_suites/test_hasaki_qc_setup\|test_hasaki_qc_setup]] |
| 2026-05-23 00:05:00 | v1.0 | Khởi tạo Feature Spec từ PDF v1.5 | [[raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.pdf\|PDF QC v1.5]] |

## ?? Impact Analysis & Regression Proposal

| Th?nh ph?n b? ?nh h??ng | M?c ?? | H?nh ??ng ?? xu?t |
|:------------------------|:-------|:------------------|
| Test Suites li?n quan | High | Khi requirement/answer thay ??i, c?p nh?t traceability tr??c r?i sinh/ch?y l?i test cases li?n quan |
| KANBAN TC count | Medium | ??ng b? l?i s? TC active sau m?i l?n th?m/x?a test case |
| Test Plan | Medium | R? l?i scope regression n?u c? thay ??i AC/lu?ng nghi?p v? |
