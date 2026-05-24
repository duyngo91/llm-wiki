---
aliases: [Packing List Hasaki, Import Packing List, hasaki-receiving-packing-list]
tags: [qa/requirement, qa/feature-group/receiving-po]
status: Draft
created: 2026-05-23
updated: 2026-05-23
feature: hasaki_receiving_packing_list
project: project_hasaki
source_version: v2.17
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Import Packing List PO (Hasaki WMS)

## Tổng quan
- **Mã tính năng:** hasaki_receiving_packing_list
- **Feature:** Import và quản lý Packing List cho PO vải — bao gồm import file Excel, validate, phê duyệt, quản lý trang Packing list, và tích hợp với luồng nhận hàng SKU vải (Group UID, Trừ lõi, quy đổi đơn vị Yard/Mét).
- **Mô tả ngắn:** Tính năng cho phép import Packing list từ NCC để kiểm soát số lượng khi nhận hàng PO cho SKU vải, bao gồm validate dữ liệu, phê duyệt (Waiting Approval/Approved), trang quản lý Packing list, quy đổi từ Kg sang Yard/Mét, quy tắc nhận dư và Trừ lõi (Tare weight).
- **Source chính:** `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.pdf` — v2.17
- **Đối tượng sử dụng (Actors):** Quản lý kho, Kế toán kho, BOD (phê duyệt khi chênh lệch >5%)
- **Test Suite tương ứng:** [[wiki/project_hasaki/test_suites/test_hasaki_receiving_packing_list|test_hasaki_receiving_packing_list]]
- **Mối quan hệ:**
  - ➡️ [[wiki/project_hasaki/features/hasaki_receiving_po_app|#2 App PO Receiving]] — Packing List Approved là điều kiện để App gợi ý Roll code khi nhận SKU vải; validate ±5% tolerance khi nhận
  - ➡️ [[wiki/project_hasaki/features/hasaki_qc_evaluation|#6 QC Evaluation]] — Group UID tạo ra từ luồng nhận vải (Packing List) là đơn vị đánh giá QC (10% sampling)
  - ⬅️ [[wiki/project_hasaki/features/hasaki_receiving_inbound_shipment|#1 Inbound Shipment]] — PO vải trên web cần có Packing List trước khi cho phép nhận

---

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | PDF | `07062_Receiving_PO_Docs_ver2.17.pdf` | v2.17 | ✅ Hiện hành |

---

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Import file Packing list theo template: cột PO code, SKU, Roll code, Batch code, Qty request, Delivery method, Khổ vải (Width)(m), Định lượng vải (GSM)(g/m2), Gross quantity (Kg), Net quantity (Kg) | Functional | High | ✅ | PDF v2.17, update 16-04-2026 |
| R2 | Validate import: PO code/SKU không được trống, phải tồn tại hệ thống, SKU phải có trong PO; Roll code/Batch code không trống; Qty request không trống và phải số dương; không trùng dữ liệu giữa các dòng | Functional | High | ✅ | PDF v2.17, mục Validate |
| R3 | Import lại: nếu PO code + SKU + Roll code + Batch code trùng với data đã có thì update lại Qty request (không tạo mới) | Functional | Medium | ✅ | PDF v2.17 |
| R4 | Validate sau khi check file hợp lệ: nếu tổng Qty request của SKU > ±5% Qty confirm trong PO → cảnh báo yêu cầu liên hệ BOD; action "Kiểm tra lại" (không lưu) hoặc "Xác nhận Import" (lưu) | Functional | High | ✅ | PDF v2.17, update 29-01-2026 |
| R5 | Delivery method = "Giao 1 phần (Partial)": không validate chênh lệch ±5%; chỉ cần tổng Qty trong packing list ≤ tổng Qty PO | Functional | Medium | ✅ | PDF v2.17, update 16-04-2026 |
| R6 | Delivery method = "Giao full PO": giữ nguyên validate ±5% như cũ | Functional | Medium | ✅ | PDF v2.17 |
| R7 | Packing list status sau import: nếu ±5% hợp lệ → Approved (tự động); nếu vượt ±5% → Waiting for Approval (chờ BOD duyệt) | Functional | High | ✅ | PDF v2.17, mục Inbound |
| R8 | PO đã chuyển Receiving khi import thêm packing list: các SKU auto Approved | Functional | Medium | ✅ | PDF v2.17 |
| R9 | Cột Packing list PO trong Inbound Listing: giá trị Waiting for Approval (có button Approve) / Approved (có link hyperlink đến trang Packing list theo PO) | Functional | High | ✅ | PDF v2.17, update 29-01-2026 |
| R10 | More filter trong Inbound: bổ sung filter Packing list PO (Waiting Approve / Approved) | Functional | Medium | ✅ | PDF v2.17 |
| R11 | Inbound Detail: hiện thêm thông tin Packing list PO và button Approve cho trạng thái Waiting Approve; xác nhận "Bạn có chắc chắn muốn duyệt cho nhận hàng theo packing list không?" | Functional | High | ✅ | PDF v2.17 |
| R12 | Re-import khi status Approved mà chênh lệch >±5% → status chuyển về Waiting for Approval | Functional | Medium | ✅ | PDF v2.17, 03-02-2026 |
| R13 | Trang quản lý Packing list — Menu: Inbound / Packing list PO: hiển thị các cột tương ứng file import; hỗ trợ chọn nhiều dòng để xoá và import lại (PO chưa Received) | Functional | Medium | ✅ | PDF v2.17, update 16-04-2026 |
| R14 | App nhận hàng SKU vải con lẻ (với Packing list Approved): nhập số lô → suggest Roll code từ packing list; nhập số lượng thực nhận + hệ số quy đổi; khai báo Group UID; chụp hình | Functional | High | ✅ | PDF v2.17, mục SKU vải con lẻ |
| R15 | App nhận hàng SKU vải combo (với Packing list Approved): tương tự con lẻ nhưng SL thực nhận theo combo (không nhân hệ số con lẻ); tổng SL thực nhận UID group phải là số nguyên dương | Functional | High | ✅ | PDF v2.17, mục SKU vải combo |
| R16 | Trừ lõi (Tare weight): tự động tính từ Gross Qty - Net Qty trong packing list; hiển thị trên màn hình khai báo UID group; disable không cho edit | Functional | Medium | ✅ | PDF v2.17, update 02-04-2026 |
| R17 | Công thức quy đổi Kg → Yard/Mét: Yard = [Kg*1000] / [Width(m) * GSM(g/m²) * 0.9144]; Mét = [Kg*1000] / [Width(m) * GSM(g/m²)]; chỉ áp dụng khi đơn vị tính SKU là Yard hoặc Mét | Functional | High | ✅ | PDF v2.17, update 16-04-2026 |
| R18 | Rules nhận dư cho PO vải: SL thực nhận > SL packing list → ghi nhận theo packing list; phần dư ADJ vào và sinh UID mới cùng UID group; nếu total > SL PO → chỉ push theo SL PO lên Inside | Functional | High | ✅ | PDF v2.17, update 20-04-2026 |
| R19 | Cảnh báo nhận dư >10% so với packing list: "Số lượng thực nhận lớn hơn 10% so với Packing list"; action Kiểm tra lại / Xác nhận | Functional | Medium | ✅ | PDF v2.17 |
| R20 | Ghi nhận thông tin sau khi nhận từng cuộn vải: Mã cuộn, Nhóm UID, Hình ảnh, Số lô, SL yêu cầu (từ packing list), SL thực nhận, Nhận lệch = SL thực - SL yêu cầu, HSD | Functional | High | ✅ | PDF v2.17 |

---

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- PO vải đã được tạo trên Inside và đồng bộ WMS.
- SKU trong PO thuộc category Thời trang (NVL) hoặc có từ "Vải" trong tên.

---

### Luồng chuẩn (Happy Path) — Import Packing List, auto Approved

1. User vào Inbound / Packing list PO (hoặc từ Inbound Listing), chọn "Import".
2. Upload file Excel theo template; hệ thống validate từng dòng.
3. Nếu tổng Qty request ≤ ±5% Qty confirm PO → tự động Approved.
4. Cột "Packing list PO" trong Inbound Listing hiển thị "Approved" kèm link đến trang Packing list.
5. User vào App nhận hàng PO → scan PO → nhập số lô → hệ thống suggest Roll code từ packing list → nhập SL thực nhận → khai báo Group UID → chụp hình → xác nhận.
6. Hệ thống ghi nhận: SL thực nhận theo cuộn, so sánh với packing list, tính Nhận lệch.

### Luồng rẽ nhánh (Alternative Paths)

- **Alt-Flow 1 — Tổng Qty >±5%:** Hệ thống cảnh báo, user liên hệ BOD; BOD approve trên Web → status = Approved → mới cho nhận hàng.
- **Alt-Flow 2 — Delivery method = Partial:** Không validate ±5%; chỉ cần tổng ≤ SL PO là cho import.
- **Alt-Flow 3 — SL thực nhận < SL packing list:** Ghi nhận theo SL thực nhận.
- **Alt-Flow 4 — SL thực nhận > SL packing list:** Ghi nhận theo SL packing list; phần dư → ADJ tự động.
- **Alt-Flow 5 — Đơn vị tính Yard/Mét:** Hệ thống tự quy đổi Kg → Yard hoặc Mét theo công thức; không hiển thị SL yêu cầu và Nhận lệch.

---

### Luồng ngoại lệ (Exception Paths)

- **Exc-Flow 1 — PO code không tồn tại:** "Dòng N – Mã PO không tồn tại trên hệ thống."
- **Exc-Flow 2 — SKU không có trong PO:** "Dòng N – SKU không tồn tại trong PO."
- **Exc-Flow 3 — Roll code trống:** "Dòng N – Mã cuộn không được để trống."
- **Exc-Flow 4 — Qty âm hoặc ký tự:** "Dòng N – Số lượng yêu cầu không hợp lệ."
- **Exc-Flow 5 — Dữ liệu trùng giữa các dòng:** "Dòng N – Dữ liệu đã tồn tại trên file import."
- **Exc-Flow 6 — Packing list Waiting Approval → không cho nhận App:** "PO chưa được duyệt Packing list nên không thể nhận hàng."
- **Exc-Flow 7 — SL thực nhận > 10% packing list:** Cảnh báo cho user check lại; action Kiểm tra lại / Xác nhận.

---

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu

| Tên trường | Định dạng | Bắt buộc? | Ràng buộc |
|:-----------|:---------|:----------|:----------|
| PO code | String | ✅ | Tồn tại trên hệ thống |
| SKU | String | ✅ | Tồn tại hệ thống và trong PO |
| Roll code | String | ✅ | Không trống |
| Batch code | String | ✅ | Không trống |
| Qty request | Số dương | ✅ | > 0; tổng ≤ ±5% Qty PO (hoặc ≤ SL PO nếu Partial) |
| Delivery method | Partial / Full PO | ✅ | Một khi chọn Partial thì các lần import sau cũng dùng Partial |
| Width (m) | Số thập phân | Theo SKU | Dùng để quy đổi Yard/Mét |
| GSM (g/m²) | Số thập phân | Theo SKU | Dùng để quy đổi Yard/Mét |
| Gross quantity (Kg) | Số thập phân | Theo SKU | ≥ Net quantity |
| Net quantity (Kg) | Số thập phân | Theo SKU | ≤ Gross quantity |
| Trừ lõi | Gross Qty - Net Qty | Auto | Disable, không cho edit |

**Công thức quy đổi:**
- Yard = [Weight(Kg) × 1000] / [Width(m) × GSM(g/m²) × 0.9144]
- Mét = [Weight(Kg) × 1000] / [Width(m) × GSM(g/m²)]

**Ghi nhận SL thực nhận:**
- SL thực nhận ≤ SL packing list → ghi nhận theo SL thực nhận
- SL thực nhận > SL packing list → ghi nhận theo SL packing list + ADJ cho phần dư

---

## 🚨 Đặc Tả Thông Điệp Báo Lỗi

| Ngữ cảnh | Thông báo (VN) | Thông báo (EN) |
|:---------|:--------------|:---------------|
| PO code trống | Dòng N – Mã PO không được để trống | Line N – PO code cannot be empty |
| PO code không tồn tại | Dòng N – Mã PO không tồn tại trên hệ thống | Line N – PO code does not exist in the system |
| SKU trống | Dòng N – SKU không được để trống | Line N – SKU cannot be empty |
| SKU không tồn tại hệ thống | Dòng N – SKU không tồn tại trên hệ thống | Line N – SKU does not exist in the system |
| SKU không có trong PO | Dòng N – SKU không tồn tại trong PO | Line N – SKU does not exist in the PO |
| Roll code trống | Dòng N – Mã cuộn không được để trống | Line N – Roll code cannot be empty |
| Batch code trống | Dòng N – Mã lô không được để trống | Line N – Batch code cannot be empty |
| Qty request trống | Dòng N – Số lượng yêu cầu không được để trống | Line N – Requested quantity cannot be empty |
| Qty request âm/ký tự | Dòng N – Số lượng yêu cầu không hợp lệ | Line N – Requested quantity is invalid |
| Trùng dữ liệu file | Dòng N – Dữ liệu đã tồn tại trên file import | Line N – Data already exists in the import file |
| Qty >±5% PO | PO [X], SKU [Y] có tổng số lượng trong packing list lớn hơn ±5% so với số lượng yêu cầu trên PO. Nếu xác nhận import thì liên hệ BOD để được duyệt trước khi nhận hàng | PO [X], SKU [Y]: The total quantity in the packing list exceeds ±5% of the PO quantity. If confirming the import, please contact BOD for approval before receiving |
| Packing list Waiting Approve | PO chưa được duyệt Packing list nên không thể nhận hàng | — |
| SL thực nhận >10% packing list | Số lượng thực nhận lớn hơn 10% so với Packing list, bạn có muốn xác nhận nhận hàng không? | The actual received quantity exceeds the packing list by more than 10%. Do you want to confirm the receipt? |
| Approve packing list | Bạn có chắc chắn muốn duyệt cho nhận hàng theo packing list không? | Do you want to approve receiving based on the packing list? |

---

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01: Import thành công, auto Approved**
  - **Given:** File import hợp lệ, tổng Qty ≤ ±5% Qty PO
  - **When:** User import
  - **Then:** Status = Approved; cột Packing list PO trong Inbound = "Approved" kèm link

- **AC-02: Import vượt ±5%, yêu cầu BOD duyệt**
  - **Given:** Tổng Qty import SKU A = 110, Qty PO = 100 (chênh 10%)
  - **When:** User xác nhận import
  - **Then:** Status = Waiting for Approval; cột Inbound hiện "Waiting for Approval" + button Approve

- **AC-03: App không cho nhận khi Packing list Waiting Approval**
  - **Given:** PO vải có Packing list status = Waiting Approval
  - **When:** User scan PO trên App
  - **Then:** Thông báo "PO chưa được duyệt Packing list nên không thể nhận hàng"

- **AC-04: Quy đổi Kg → Yard**
  - **Given:** SKU đặt theo Yard; Width = 1.5m, GSM = 200g/m², Weight nhập = 15Kg
  - **When:** User submit khai báo cuộn vải
  - **Then:** Hệ thống tự tính Yard = [15*1000] / [1.5*200*0.9144] ≈ 54.68 Yard

- **AC-05: Trừ lõi tự động từ Packing list**
  - **Given:** Gross Qty = 15.3 Kg, Net Qty = 15 Kg
  - **When:** User xem màn hình khai báo UID group
  - **Then:** Trừ lõi = 0.3 Kg, hiển thị disabled không cho chỉnh sửa

- **AC-06: Nhận dư >10% packing list**
  - **Given:** Packing list Roll code A Batch code 01 = 10 Yard; user nhập thực nhận 12 Yard (vượt 20%)
  - **When:** User submit
  - **Then:** Hiện cảnh báo "Số lượng thực nhận lớn hơn 10% so với Packing list"

- **AC-07: Import lại khi đã Approved → chênh >±5% → về Waiting**
  - **Given:** Packing list PO đang Approved; user import lại với Qty chênh >±5%
  - **When:** Import
  - **Then:** Status chuyển về Waiting for Approval

---

## ❓ Câu hỏi chưa rõ

- [ ] ❓ **R16 — Update 16-04-2026 Pending:** Spec ghi "(12-05-2026: Pending lại không làm tiếp do vận hành Purchase order gặp khó khăn khi làm việc với Vendor)" — vậy các cột Delivery method / Width / GSM / Gross Qty / Net Qty có trong scope test không? Cần xác nhận trạng thái triển khai.
- [ ] ❓ **R18 — ADJ tự động khi nhận dư:** Dev xác nhận flow ADJ được tạo tự động hay thủ công? Khi nào ADJ được tạo?
- [ ] ❓ **R13 — Edit số lượng tạm ẩn:** "Tạm thời ẩn tính năng edit số lượng trên giao diện" — đây có phải là tính năng đã build nhưng ẩn, hay chưa build? Ảnh hưởng test case UI.
- [ ] ❓ **R4 vs R5 — Delivery method Partial:** Khi PO đã chọn Partial rồi import lại theo Full PO thì có báo lỗi không, hay cứ theo lần import mới nhất?
- [ ] ❓ **R17 — Đơn vị tính lấy từ đâu:** "Đơn vị tính của SKU lấy từ Attributes của Inside". Màn hình App có hiển thị đơn vị tính để user biết không?
- [ ] ❓ **R2 — Boundary Qty request:** Rule chưa nêu rõ Qty request = 0 có luôn bị từ chối hay không. Cần thông báo lỗi chính thức nếu có validate này.
- [ ] ❓ **R19 — Threshold cảnh báo 10% khi nhận dư:** Trường hợp SL thực nhận lệch đúng 10% so với packing list thì có cảnh báo không? Cần xác nhận toán tử `>` hay `>=`.

---

## 📝 Thay đổi so với version cũ

| # | Nội dung thay đổi | Version cũ | Version mới | Ảnh hưởng TC |
|:--|:------------------|:----------|:-----------|:-------------|
| 1 | Validate Qty >±5% khi import | v2.13 | v2.17 | TC validate |
| 2 | Cột Delivery method (Partial/Full PO) trong template | v2.16 | v2.17 | TC import |
| 3 | Cột Width, GSM, Gross Qty, Net Qty trong template | v2.16 | v2.17 | TC import (pending) |
| 4 | Rules nhận dư + ADJ | v2.16 | v2.17 | TC nhận dư |

---

## Test Coverage
| Requirement | Test Case(s) | Status |
|:-----------|:------------|:-------|
| R1–R20 | _(chờ thiết kế)_ | ⏳ |

---

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 21:49:34 | v1.1 | Bổ sung câu hỏi boundary R2/R19 sau khi loại test case suy diễn khỏi Test Suite | [[wiki/project_hasaki/test_suites/test_hasaki_receiving_packing_list\|test_hasaki_receiving_packing_list]] |
| 2026-05-23 00:00:00 | v1.0 | Khởi tạo Feature Spec từ PDF v2.17 — Import Packing List | `07062_Receiving_PO_Docs_ver2.17.pdf` |

## ?? Impact Analysis & Regression Proposal

| Th?nh ph?n b? ?nh h??ng | M?c ?? | H?nh ??ng ?? xu?t |
|:------------------------|:-------|:------------------|
| Test Suites li?n quan | High | Khi requirement/answer thay ??i, c?p nh?t traceability tr??c r?i sinh/ch?y l?i test cases li?n quan |
| KANBAN TC count | Medium | ??ng b? l?i s? TC active sau m?i l?n th?m/x?a test case |
| Test Plan | Medium | R? l?i scope regression n?u c? thay ??i AC/lu?ng nghi?p v? |
