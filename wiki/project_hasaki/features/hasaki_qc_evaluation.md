---
aliases: [QC Evaluation, Kết quả đánh giá chất lượng, hasaki_qc_evaluation]
tags: [qa/requirement, qa/feature-group/receiving-po]
status: Draft
created: 2026-05-23
updated: 2026-05-23
feature: hasaki_qc_evaluation
project: project_hasaki
source_version: v1.5
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Đánh giá Chất lượng Sản phẩm (QC Evaluation)

## Tổng quan
- **Mã tính năng:** hasaki_qc_evaluation
- **Feature:** QC Evaluation — Thực hiện đánh giá chất lượng trên App và xem kết quả trên Web
- **Mô tả ngắn:** Luồng thực hiện đánh giá chất lượng sản phẩm trên Mobile App (sản phẩm thường + vải) bao gồm 3 tiêu chí vải (lỗi 4 điểm, độ co rút, độ đồng màu), tạo đánh giá thủ công, chụp hình tem QC, tạo ADJ trả hàng khi Failed, block UID group khi vải Failed. Kết quả đánh giá được tra cứu và phân tích trên Web.
- **Source chính:** `raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.pdf`
- **Đối tượng sử dụng (Actors):** QC Staff (App + Web), QC Lead / Approver (Web), Warehouse Staff (App)
- **Test Suite tương ứng:** [[wiki/project_hasaki/test_suites/test_hasaki_qc_evaluation]]
- **Mối quan hệ:**
  - ⬅️ [[wiki/project_hasaki/features/hasaki_qc_setup|#5 QC Setup]] — Tiêu chí đánh giá, loại đánh giá (Bình thường/Lỗi 4 điểm/Theo từng bước) và cấu hình "QC xã vải" đều đến từ QC Setup
  - ⬅️ [[wiki/project_hasaki/features/hasaki_receiving_vas|#3 VAS]] — VAS type Quality Control là đơn vị kích hoạt và chứa kết quả đánh giá; trạng thái VAS thay đổi theo kết quả (Chờ đánh giá → Chờ duyệt → Completed/Trả NCC)
  - ⬅️ [[wiki/project_hasaki/features/hasaki_receiving_packing_list|#4 Packing List]] — Group UID tạo ra từ luồng nhận vải là đơn vị đánh giá QC vải (10% sampling per lô)
  - ⬅️ [[wiki/project_hasaki/features/hasaki_receiving_po_app|#2 App PO Receiving]] — PO Sample: QC phải Đạt trước khi cho phép nhận PO Gốc; ngưỡng tiêu chí PO Gốc map theo điều kiện thực tế của PO Sample

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | PDF | 07105_Quality_Control_Docs_ver1.5.pdf | v1.5 | ✅ Hiện hành |
| 2 | Link | Figma: node 366-229 (Base) | — | ✅ Hiện hành |
| 3 | Link | Figma: node 1946-1696 (Update 11-02-2026) | — | ✅ Hiện hành |
| 4 | Link | Figma: node 2542-554 (Update 20-04-2026) | — | ✅ Hiện hành |

## Phân rã Requirement
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | Tab Kết quả đánh giá (Web) hỗ trợ filter: SKU/barcode, VAS (mã chính xác), Kho (≥3 ký tự), Mã PO (mã chính xác), Trạng thái (New/Processing/Completed), Phân loại (Tự động/Thủ công/Bình thường/Nhóm UID/Xã vải), Người đánh giá, Có tiêu chí không đạt (Yes/No), Ngày đánh giá | Functional | High | ✅ | PDF v1.5, mục Kết quả đánh giá |
| R2 | Listing kết quả đánh giá hiển thị: VAS (hyperlink), Kho, Sản phẩm (SKU–tên), Tiêu chí đạt, Tiêu chí không đạt, Phân loại, Mã PO nguồn (hyperlink), Nhà cung cấp, Danh mục, Thương hiệu, Ghi chú, Người đánh giá, Thời gian hoàn thành, Trạng thái, Thao tác xem chi tiết | Functional | High | ✅ | PDF v1.5, listing |
| R3 | Chi tiết kết quả đánh giá Type=Bình thường: hiển thị thông tin sản phẩm, danh sách tiêu chí với kết quả đạt/không đạt, hình ảnh | Functional | High | ✅ | PDF v1.5, update 18-09-2025 |
| R4 | Chi tiết kết quả đánh giá Type=Nhóm UID: hiển thị theo từng nhóm UID; cho phép xem chi tiết theo từng nhóm | Functional | High | ✅ | PDF v1.5, update 18-09-2025 |
| R5 | Chi tiết tiêu chí Lỗi 4 điểm: hiển thị từng loại lỗi (1/2/3/4 điểm) dưới dạng group thu gọn/mở rộng; mỗi lỗi gồm Loại lỗi, Hình ảnh, Ghi chú; Tổng điểm lỗi chưa nhân hệ số, Tổng điểm đã nhân hệ số | Functional | High | ✅ | PDF v1.5, update 18-09-2025 |
| R6 | Chi tiết tiêu chí Theo từng bước: mỗi bước là 1 nhóm gồm Hình ảnh, Kết quả ghi nhận, Ghi chú | Functional | High | ✅ | PDF v1.5, update 18-09-2025 |
| R7 | Update 11-02-2026: Chi tiết kết quả đánh giá bổ sung "Số lượng cần đánh giá" và "Hình ảnh tem QC" | Functional | Medium | ✅ | PDF v1.5, update 11-02-2026 |
| R8 | Update 11-02-2026: Cột Phân loại bổ sung giá trị "Xã vải / Fabric Relaxing" | Functional | Medium | ✅ | PDF v1.5, update 11-02-2026 |
| R9 | App QC — Vào tính năng Quality Control: Menu Purchase Order / Quality Control → chọn kho → hiện danh sách VAS type Quality Control có trạng thái Open hoặc In-Progress; hỗ trợ tìm theo mã PO và VAS | Functional | High | ✅ | PDF v1.5, mục Đánh giá chất lượng sản phẩm - Mobile |
| R10 | App QC — Chọn VAS cần đánh giá: hiển thị Shop, VAS, Tổng SKU, Mã PO, Tổng sản phẩm, tìm kiếm sản phẩm (SKU/Barcode/tên gần đúng); danh sách màu sắc trạng thái: xám nhạt (chưa đánh giá), xanh dương nhạt (đang đánh giá), xanh lá nhạt (đã đánh giá) | Functional | High | ✅ | PDF v1.5 |
| R11 | App QC sản phẩm thường — Đánh giá từng tiêu chí: thứ tự, tên, mô tả, điều kiện, hình chụp mẫu, Đạt/Không đạt; nhập kết quả số (nếu Theo điều kiện) → Enter/dấu tích → hệ thống so sánh với config → trả kết quả; tiêu chí Fail yêu cầu chụp hình (≤5 hình) và nhập ghi chú | Functional | High | ✅ | PDF v1.5 |
| R12 | App QC — Hoàn thành đánh giá: sau khi đánh giá tất cả tiêu chí → nhấn "Hoàn thành"; nếu VAS có nhiều sản phẩm phải đánh giá tất cả → "Hoàn thành đánh giá" cho toàn VAS | Functional | High | ✅ | PDF v1.5 |
| R13 | App QC — Chụp hình tem QC (update 11-02-2026): sau khi nhấn "Hoàn thành" bắt buộc chụp 1 hình tem QC Pass/Fail trước khi ghi nhận lên hệ thống | Functional | High | ✅ | PDF v1.5, update 11-02-2026 |
| R14 | App QC vải — Hiển thị danh sách sản phẩm vải: thêm cột Số lô, Hạn sử dụng; màu sắc gồm thêm màu cam nhạt (đã đánh giá Không Đạt); 10% sampling → mỗi lô N cây vải thì ceil(N×10%) dòng VAS | Functional | High | ✅ | PDF v1.5, update 18-09-2025 |
| R15 | App QC vải — Scan UID group: bắt buộc scan UID group tương ứng với cây vải cần đánh giá; nếu UID không tồn tại hoặc không thuộc PO/lô → hiện thông báo; hỗ trợ suggest UID đã nhận theo lô | Functional | High | ✅ | PDF v1.5 |
| R16 | App QC vải — Khai báo số lượng cần đánh giá (update 11-02-2026): ở bước scan UID group bổ sung nhập số lượng cần đánh giá (bắt buộc, số nguyên dương); sau xác nhận hệ thống tự trừ số lượng đó ra khỏi UID group | Functional | High | ✅ | PDF v1.5, update 11-02-2026 |
| R17 | App QC vải — 3 tiêu chí đánh giá vải: (1) Kiểm tra lỗi 4 điểm (19 loại lỗi), (2) Kiểm tra độ co rút (Theo từng bước), (3) Kiểm tra độ đồng màu (Theo từng bước) | Functional | High | ✅ | PDF v1.5, update 18-09-2025 |
| R18 | App QC vải — Lỗi 4 điểm: nhấn dấu + để ghi nhận lỗi (chọn loại lỗi bắt buộc từ 19 loại, nhập ghi chú, chụp ≤3 hình bắt buộc); tính Số lỗi từng loại, Tổng điểm lỗi (chưa nhân hệ số), Tổng điểm đã nhân hệ số; so sánh với điều kiện để xác định Đạt/Không đạt | Functional | High | ✅ | PDF v1.5 |
| R19 | App QC vải — Kết quả UID group: nếu ≥1 tiêu chí Không đạt → kết quả nhóm UID = Không đạt; phải hoàn thành tất cả nhóm UID trong VAS | Functional | High | ✅ | PDF v1.5 |
| R20 | Tạo mới đánh giá thủ công (App, update 11-02-2026): Menu PO / Quality Control → Tạo mới → tìm sản phẩm → load 10 PO nhận gần nhất → chọn PO → khai báo UID group và số lượng cần đánh giá → Bắt đầu đánh giá | Functional | High | ✅ | PDF v1.5, update 11-02-2026 |
| R21 | Validate thủ công: UID group không tồn tại → "Mã UID không tồn tại."; số lượng không đủ trong UID group → "Số lượng trong UID group không đủ số lượng yêu cầu."; SKU chưa thiết lập tiêu chí → hiện thông báo | Functional | High | ✅ | PDF v1.5, update 11-02-2026 |
| R22 | Update 20-04-2026 — Failed SKU thường → tạo ADJ: sau khi đánh giá xong (≥1 tiêu chí Fail) hiện màn hình xác nhận số lượng trả NCC; user chọn "Tạo phiếu điều chỉnh" → nhập số lượng (< số lượng nhận PO) → Xác nhận → tạo Adjustment (Export, Reason: Return to vendor, Vendor từ PO, Require VAT: 3 options, Source code: Mã PO, Required picking: No, Status: Waiting for approval) | Functional | High | ✅ | PDF v1.5, update 20-04-2026 |
| R23 | Update 20-04-2026 — Blocked UID group khi vải Failed: khi vải đánh giá Failed → tự động block tất cả UID group cùng PO cùng LOT + chuyển Product status = Damaged (không cộng vào Available, không thể IT); khi Unblock → Product status tự chuyển về Normal | Functional | High | ✅ | PDF v1.5, update 20-04-2026 |
| R24 | Update 11-02-2026 — UID group cột "Đánh giá đạt": N/A (SKU không phải vải NVL), No (SKU vải sau khi nhận PO mặc định), Yes (sau khi đánh giá xã vải Đạt); block IT nếu chưa đánh giá (No) | Functional | Medium | ✅ | PDF v1.5, update 11-02-2026 |
| R25 | Tiêu chí PO Sample map với PO Gốc: nếu PO Sample đánh giá SKU chỉ đạt X/Y tiêu chí nhưng BOD vẫn duyệt nhận → PO Gốc của SKU đó cũng áp dụng ngưỡng theo điều kiện thực tế của PO Sample | Functional | Medium | ✅ | PDF v1.5, lưu ý luồng xã vải |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- VAS đã được sinh với type Quality Control và trạng thái Open/In-Progress (tự động sau khi kết thúc phiên nhận PO với SKU có thiết lập "Tất cả PO")
- SKU đã có thiết lập tiêu chí ở trạng thái "Đã duyệt"
- QC Staff đã login App, chọn đúng kho

### Luồng chuẩn (Happy Path) — Đánh giá sản phẩm thường

1. Vào App → Menu Purchase Order / Quality Control → chọn kho
2. Chọn VAS cần đánh giá (trạng thái Open hoặc In-Progress)
3. Xem danh sách sản phẩm trong VAS → chọn sản phẩm (xám nhạt = chưa đánh giá)
4. Xem thông tin sản phẩm: SKU, PO, Số lượng, Nhà cung cấp, Ghi chú
5. Đánh giá từng tiêu chí (theo cấu hình Bình thường):
   - Chọn Đạt hoặc Không đạt cho từng tiêu chí
   - Nếu Theo điều kiện: nhập giá trị số → Enter → hệ thống tự so sánh trả kết quả
   - Nếu tiêu chí Fail: chụp ≤5 hình (bắt buộc) + nhập ghi chú
6. Sau khi hoàn thành tất cả tiêu chí → nhấn "Hoàn thành"
7. Bước chụp hình tem QC Pass/Fail (bắt buộc 1 hình) → Xác nhận
8. Nếu VAS có nhiều sản phẩm → lặp bước 3–7 cho tất cả sản phẩm
9. Nhấn "Hoàn thành đánh giá" cho toàn VAS → trạng thái VAS cập nhật theo kết quả

### Luồng chuẩn (Happy Path) — Đánh giá vải (Fabric QC)

1. Vào App → Quality Control → chọn kho → chọn VAS vải
2. Chọn sản phẩm vải (có màu phân biệt trạng thái theo lô)
3. Scan UID group của cây vải cần đánh giá (bắt buộc) hoặc chọn từ suggest
4. Khai báo số lượng cần đánh giá (bắt buộc, số nguyên dương) → Xác nhận → hệ thống trừ số lượng khỏi UID group
5. Đánh giá 3 tiêu chí vải:
   - **Tiêu chí 1 — Lỗi 4 điểm:** nhấn + để thêm lỗi (chọn 1 trong 19 loại lỗi, chụp ≤3 hình bắt buộc, ghi chú) → tính tổng điểm lỗi (chưa/đã nhân hệ số) → so sánh với điều kiện → Đạt/Không đạt
   - **Tiêu chí 2 — Kiểm tra độ co rút (Theo từng bước):** thực hiện lần lượt từng bước theo cấu hình (nhập kết quả, chụp hình nếu yêu cầu) → Tiếp theo → Hoàn thành bước cuối → hệ thống tính công thức → Đạt/Không đạt
   - **Tiêu chí 3 — Kiểm tra độ đồng màu (Theo từng bước):** thực hiện tương tự Tiêu chí 2
6. Nhấn "Hoàn thành" cho nhóm UID → ghi nhận kết quả
7. Chụp hình tem QC (bắt buộc 1 hình)
8. Nếu ≥1 tiêu chí Không đạt → kết quả nhóm UID = Không đạt
9. Lặp cho tất cả nhóm UID cần đánh giá trong lô (10% sampling)

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 — Tạo đánh giá thủ công (Manual):** App → Tạo mới → tìm SKU → chọn PO gần nhất (top 10) → khai báo UID group + số lượng → Bắt đầu đánh giá → thực hiện đánh giá tương tự luồng chuẩn
- **Alt-Flow 2 — SKU thường Failed → tạo ADJ trả NCC:** Sau khi Hoàn thành đánh giá có ≥1 tiêu chí Fail → popup xác nhận → Tạo phiếu điều chỉnh → nhập số lượng trả → chọn Require VAT (3 options) → Xác nhận → ADJ tạo với status "Waiting for approval"; hoặc chọn "Để sau" để bỏ qua
- **Alt-Flow 3 — Vải Failed → Block UID group:** Khi đánh giá vải có kết quả Failed → tự động block toàn bộ UID group của SKU trong cùng PO, cùng LOT → Product status = Damaged → không cộng vào stock Available; khi Unblock → Product status về Normal
- **Alt-Flow 4 — Đánh giá Xã vải:** Khi UID group TF vào F0-XV → sinh yêu cầu đánh giá Xã vải tự động → QC thực hiện trên App tương tự luồng thường với tiêu chí "QC xã vải"; sau khi Đạt → cột "Đánh giá đạt" trong UID group = Yes
- **Alt-Flow 5 — Xem kết quả trên Web:** Web → Inbound / Quality control → Tab Kết quả đánh giá → filter → listing → chọn icon xem chi tiết từng assessment

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1 — UID group không hợp lệ khi đánh giá vải:** Scan UID không tồn tại hoặc không thuộc PO/lô được yêu cầu → hiện thông báo lỗi; user phải scan lại
- **Exc-Flow 2 — Số lượng khai báo vượt quá UID group:** "Số lượng trong UID group không đủ số lượng yêu cầu."
- **Exc-Flow 3 — SKU chưa thiết lập tiêu chí:** Khi chọn PO để đánh giá thủ công → hiện thông báo SKU chưa được thiết lập tiêu chí
- **Exc-Flow 4 — Tiêu chí Theo điều kiện nhập giá trị sai:** Giá trị ≤0 → không chấp nhận
- **Exc-Flow 5 — Số lượng ADJ trả vượt số lượng nhận:** Số lượng cần trả phải < số lượng nhập hàng PO → validate

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------|:---------|:----------|:-------------------------------|
| Mã PO (filter Web) | Text | ❌ | Tìm theo mã chính xác |
| Mã VAS (filter Web) | Text | ❌ | Tìm theo mã chính xác |
| Phân loại | Enum | ❌ | Tự động / Thủ công / Bình thường / Nhóm UID / Xã vải |
| Số lượng 10% sampling (vải) | Integer | — | ceil(N × 10%); VD: 25 cây → ceil(2.5) = 3 |
| Khai báo SL cần đánh giá | Integer > 0 | ✅ | Hệ thống tự trừ khỏi UID group sau xác nhận |
| Hình chụp tiêu chí Fail | Image | ✅ (Fail) | ≤5 hình/tiêu chí; Fail bắt buộc chụp + ghi chú |
| Hình chụp lỗi 4 điểm | Image | ✅ | ≤3 hình/lỗi; bắt buộc |
| Hình tem QC | Image | ✅ | Bắt buộc 1 hình sau khi Hoàn thành đánh giá |
| Kết quả UID group | Enum | — | Đạt nếu tất cả tiêu chí Đạt; Không đạt nếu ≥1 Fail |
| Số lượng ADJ trả NCC | Integer | ✅ | < Số lượng nhập hàng PO; nhập bởi user |
| Require VAT (ADJ) | Enum | ✅ | No / Yes VAT (Hasaki xuất HĐ bán) / Yes VAT (NCC xuất HĐ điều chỉnh) |
| Product status (Block) | Enum | — | Damaged = không cộng stock Available, không thể IT |
| Đánh giá đạt (UID group) | Enum | — | N/A (không phải vải NVL) / No (mặc định sau nhận PO) / Yes (sau xã vải Đạt) |
| Ngưỡng PO Gốc theo PO Sample | Logic | — | Nếu PO Sample failed nhưng BOD approve → PO Gốc áp ngưỡng thực tế từ PO Sample |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Trigger | Thông báo VN | Thông báo EN |
|:-------|:--------|:-------------|:-------------|
| ERR-QCE-01 | UID group không tồn tại (App scan) | Mã UID không tồn tại. | — |
| ERR-QCE-02 | UID group không thuộc PO/lô | Nhóm UID không tồn tại hoặc không thuộc PO và số lô được yêu cầu đánh giá | — |
| ERR-QCE-03 | Số lượng khai báo > UID group qty | Số lượng trong UID group không đủ số lượng yêu cầu. | — |
| ERR-QCE-04 | SKU chưa thiết lập tiêu chí | (hiện thông báo — cần xác nhận nội dung chính xác) | — |
| ERR-QCE-05 | SKU Failed → xác nhận tạo ADJ | SKU 422280022 has evaluation criteria marked as FAILED. Do you want to create an adjustment voucher to export the failed quantity for return to vendor? | (EN như VN) |
| ERR-QCE-06 | Số lượng ADJ > số lượng nhận PO | (cần xác nhận nội dung — chưa rõ trong spec) | — |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01: Đánh giá sản phẩm thường — tất cả Đạt**
  - **Given:** VAS type Quality Control ở trạng thái Open, SKU có thiết lập Approved
  - **When:** QC Staff đánh giá tất cả tiêu chí = Đạt, chụp tem QC, nhấn Hoàn thành
  - **Then:** Kết quả = Đạt, VAS chuyển trạng thái phù hợp (Hoàn thành hoặc theo flow IMEI/RFID)

- **AC-02: Đánh giá sản phẩm thường — có tiêu chí Fail, chụp hình bắt buộc**
  - **Given:** QC Staff đánh giá tiêu chí = Không đạt
  - **When:** Chưa chụp hình hoặc chưa nhập ghi chú
  - **Then:** Không cho phép nhấn Hoàn thành cho tiêu chí đó; phải chụp hình (≤5) và nhập ghi chú

- **AC-03: Tem QC bắt buộc sau Hoàn thành**
  - **Given:** QC Staff hoàn thành đánh giá tất cả tiêu chí cho SKU
  - **When:** Nhấn "Hoàn thành"
  - **Then:** App yêu cầu chụp 1 hình tem QC Pass/Fail; không thể skip bước này

- **AC-04: Đánh giá vải — 10% sampling**
  - **Given:** SKU vải nhận 25 group UID trong ASN
  - **When:** Hệ thống sinh VAS Quality Control
  - **Then:** Sinh 3 dòng VAS (ceil(25×10%) = 3) tương ứng 3 group UID cần đánh giá

- **AC-05: Đánh giá vải — UID group Không đạt → Block + Damaged**
  - **Given:** QC Staff hoàn thành đánh giá vải với kết quả Failed cho 1 group UID
  - **When:** Nhấn Hoàn thành
  - **Then:** Toàn bộ UID group của SKU trong cùng PO + LOT bị Block; Product status = Damaged; không cộng vào Available; không thể IT

- **AC-06: Unblock UID group → Product status về Normal**
  - **Given:** UID group đang ở trạng thái Blocked + Damaged
  - **When:** User Unblock UID group
  - **Then:** Product status tự động chuyển về Normal

- **AC-07: SKU thường Failed → Tạo ADJ trả NCC**
  - **Given:** Đánh giá SKU thường có ≥1 tiêu chí Fail
  - **When:** User chọn "Tạo phiếu điều chỉnh", nhập số lượng hợp lệ, chọn Require VAT, Xác nhận
  - **Then:** ADJ được tạo (Export, Reason: Return to vendor, Source code: Mã PO, Required picking: No, Status: Waiting for approval)

- **AC-08: Tạo đánh giá thủ công**
  - **Given:** QC Staff chọn Tạo mới trong App Quality Control
  - **When:** Tìm SKU → chọn PO → khai báo UID group + số lượng hợp lệ → Bắt đầu đánh giá
  - **Then:** Màn hình đánh giá hiển thị tiêu chí theo cấu hình của SKU; sau hoàn thành ghi nhận vào Tab Kết quả đánh giá (Web) với Type = Thủ công

- **AC-09: Web — Xem chi tiết Lỗi 4 điểm**
  - **Given:** Kết quả đánh giá vải đã hoàn thành với tiêu chí Lỗi 4 điểm
  - **When:** QC Lead xem chi tiết trên Web
  - **Then:** Hiển thị từng loại lỗi dạng group (1/2/3/4 điểm) có thể thu gọn/mở rộng; mỗi lỗi hiện Loại lỗi, Hình ảnh, Ghi chú; Tổng điểm chưa/đã nhân hệ số

- **AC-10: Cột "Đánh giá đạt" của UID group**
  - **Given:** SKU vải vừa nhận PO xong
  - **When:** Xem Tab UID group trên Web
  - **Then:** Cột "Đánh giá đạt" = No; sau khi đánh giá Xã vải Đạt → chuyển Yes; các SKU không phải vải NVL hiển thị N/A

## ❓ Câu hỏi chưa rõ

- [ ] ❓ **R22/ERR-QCE-06 — Validate số lượng ADJ:** Spec chỉ ghi "Số lượng phải nhỏ hơn số lượng nhập hàng PO" nhưng không rõ thông báo lỗi cụ thể khi nhập quá. Thông báo lỗi là gì? *(Hỏi Dev Lead)*

- [ ] ❓ **ERR-QCE-04 — SKU chưa thiết lập tiêu chí:** Thông báo chính xác khi user tạo đánh giá thủ công cho SKU chưa có thiết lập là gì? Có hyperlink đến màn hình thiết lập không? *(Hỏi Dev Lead)*

- [ ] ❓ **R25 — Tiêu chí PO Sample map với PO Gốc:** Spec ghi "tiêu chí đánh giá cho SKU của PO chính cũng phải dựa vào điều kiện của tiêu chí của SKU trên PO Sample". Cơ chế kỹ thuật để map ngưỡng này là gì? Hệ thống tự động thay ngưỡng hay QC Lead phải cập nhật thủ công? *(Hỏi Dev Lead + PO)*

- [ ] ❓ **R13 — Tem QC:** Tem QC Pass/Fail là tem vật lý được in ra và dán lên sản phẩm, sau đó chụp lại? Hay là chụp màn hình kết quả App? Và hình này được lưu ở đâu trong hệ thống? *(Hỏi PO + Vận hành)*

- [ ] ❓ **R23 — Scope Blocked UID group:** Khi vải Failed, spec ghi "block tất cả UID group của SKU nhận trong cùng PO và cùng LOT". Nếu cùng PO nhưng khác LOT thì có bị block không? Nếu block 1 group thì các group còn lại của VAS chưa đánh giá có cần đánh giá tiếp không? *(Hỏi Dev Lead + QA Lead)*
- [ ] ❓ **R14 — Boundary sampling 10%:** Với N=10 (hoặc các giá trị biên khác), quy tắc làm tròn lên `ceil(N x 10%)` có được áp dụng chính thức không?
- [ ] ❓ **R2 — VAS hyperlink trên listing:** Cột VAS ở listing có click sang chi tiết không, và sang màn hình nào?

## 📝 Thay đổi so với version cũ

| # | Nội dung thay đổi | Version cũ | Version mới | Ảnh hưởng TC |
|:--|:------------------|:----------|:-----------|:-------------|
| 1 | Bổ sung đánh giá chất lượng vải (3 tiêu chí, 10% sampling, UID group) | v1.1 | v1.2 (18-09-2025) | TC mới cho luồng vải |
| 2 | Khai báo số lượng cần đánh giá khi scan UID group (App) | v1.3 | v1.4 (11-02-2026) | TC mới cho khai báo SL |
| 3 | Chụp hình tem QC bắt buộc sau Hoàn thành | v1.3 | v1.4 (11-02-2026) | TC mới bước chụp tem |
| 4 | Cột "Số lượng cần đánh giá" và "Hình ảnh tem QC" trong chi tiết Web | v1.3 | v1.4 (11-02-2026) | Update TC Web |
| 5 | Phân loại "Xã vải" trong Tab Kết quả đánh giá | v1.3 | v1.4 (11-02-2026) | TC mới filter Xã vải |
| 6 | Cột "Đánh giá đạt" trong UID group (N/A/No/Yes) | v1.3 | v1.4 (11-02-2026) | TC mới cho UID group |
| 7 | Failed SKU thường → tạo ADJ trả NCC | v1.4 | v1.5 (20-04-2026) | TC mới cho ADJ flow |
| 8 | Block UID group + Damaged khi vải Failed | v1.4 | v1.5 (20-04-2026) | TC mới cho Block/Unblock |

## Test Coverage

| Requirement | Test Case(s) | Status |
|:-----------|:------------|:-------|
| R1–R2 | Chờ thiết kế | ❌ Chưa có |
| R3–R6 | Chờ thiết kế | ❌ Chưa có |
| R7–R8 | Chờ thiết kế | ❌ Chưa có |
| R9–R13 | Chờ thiết kế | ❌ Chưa có |
| R14–R19 | Chờ thiết kế | ❌ Chưa có |
| R20–R21 | Chờ thiết kế | ❌ Chưa có |
| R22–R23 | Chờ thiết kế | ❌ Chưa có |
| R24–R25 | Chờ thiết kế | ❌ Chưa có |

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-23 21:49:34 | v1.1 | Bổ sung câu hỏi R14/R2 sau khi loại test case suy diễn khỏi Test Suite | [[wiki/project_hasaki/test_suites/test_hasaki_qc_evaluation\|test_hasaki_qc_evaluation]] |
| 2026-05-23 00:06:00 | v1.0 | Khởi tạo Feature Spec từ PDF v1.5 | [[raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.pdf\|PDF QC v1.5]] |

## ?? Impact Analysis & Regression Proposal

| Th?nh ph?n b? ?nh h??ng | M?c ?? | H?nh ??ng ?? xu?t |
|:------------------------|:-------|:------------------|
| Test Suites li?n quan | High | Khi requirement/answer thay ??i, c?p nh?t traceability tr??c r?i sinh/ch?y l?i test cases li?n quan |
| KANBAN TC count | Medium | ??ng b? l?i s? TC active sau m?i l?n th?m/x?a test case |
| Test Plan | Medium | R? l?i scope regression n?u c? thay ??i AC/lu?ng nghi?p v? |
