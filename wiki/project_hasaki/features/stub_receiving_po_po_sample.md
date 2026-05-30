---
aliases: [stub_receiving_po_po_sample]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_po_sample
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L2581-L2624
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 22:50:00"
verification_status: Verified
approved_by:
approved_at:
approval_note:
---

# REQ: stub_receiving_po_po_sample

## Tổng quan
- **Mã tính năng:** stub_receiving_po_po_sample
- **Feature:** PO Sample (PO mẫu thử) & PO chính
- **Mô tả ngắn:** Bổ sung PO type "Sample" trên Inside cho luồng quality control trước khi nhận PO gốc. PO Sample phải Completed + QC Pass thì mới được nhận PO gốc, và lần đầu chỉ cho nhận max 30% kèm tạo request QC cho 30% UID group.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Nhân viên kho (User scan nhận hàng), hệ thống Inside (master data PO), hệ thống WMS.
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[test_stub_receiving_po_po_sample]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_qc_evaluation_result]] (kết quả QC quyết định nhận PO gốc). ➡️ block luồng nhận PO gốc thông thường khi có Sample.

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07062_Receiving_PO_Docs_ver2.17.md | 2.17 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Raw không mô tả API explicit | N/A |

## Phân rã Requirement
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Inside bổ sung PO type mới `Sample` (tương tự type `Gift`), dùng để phân biệt cho luồng quality control | Functional | High | ✅ | 07062#L2582-L2584 |
| R002 | Ghi nhận liên kết 2 chiều giữa PO `Sample` và PO gốc | Functional | High | ✅ | 07062#L2585 |
| R003 | Khi NCC giao hàng có cả PO Sample và PO gốc, PO `Sample` được nhận vào trước và thực hiện QC trước; PO gốc chưa được nhận trên WMS ở giai đoạn này | Functional | High | ✅ | 07062#L2587-L2589 |
| R004 | QC SKU của PO `Sample` chạy theo luồng QC thông thường | Functional | High | ✅ | 07062#L2590 |
| R005 | Phase 1: tiêu chí QC thiết lập cho SKU của PO Sample và PO gốc giống nhau | Functional | Medium | ✅ | 07062#L2591 |
| R006 | Hệ thống chặn nhận PO gốc khi PO `Sample` chưa Completed hoặc kết quả QC không Đạt | Functional | High | ✅ | 07062#L2595-L2598 |
| R007 | Hiển thị thông báo lỗi (song ngữ VN/EN) khi user scan nhận PO gốc trong khi PO `Sample` chưa Completed hoặc QC không Đạt | Functional | High | ✅ | 07062#L2599-L2606 |
| R008 | Sau khi PO Sample đánh giá `Passed`, lần đầu nhận PO chính chỉ cho nhận tối đa **30%** packing list và hệ thống tự tạo request QC cho 30% UID group được nhận vào | Functional | High | ✅ | 07062#L2607-L2610 |
| R009 | UID mới nhận và chưa QC giữ status `Received`; sau QC chuyển status sang `Inbin` (passed hoặc failed đều chuyển) | State transition | High | ✅ | 07062#L2611-L2613 |
| R010 | UID group QC failed: không nhận phần còn lại, trả lại nhà cung cấp | Functional | High | ✅ | 07062#L2614 |
| R011 | UID group QC passed: cho nhận tiếp bình thường, đánh dấu cột `Đánh giá đạt = No` cho UID group; UID chỉ được transfer nội kho, không IT (inter-warehouse transfer) sang kho khác | Functional | High | ✅ | 07062#L2615-L2617 |
| R012 | Quy tắc làm tròn 30% packing list: làm tròn lên (ceil); nhận vượt giới hạn 30% thì báo lỗi (song ngữ VN/EN) | Validation rule | High | ✅ | 07062#L2618-L2624 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- PO gốc đã được tạo trên Inside.
- Inside đã thiết lập PO `Sample` liên kết với PO gốc tương ứng (R002).
- Tiêu chí QC đã được thiết lập cho SKU (giống cả Sample và gốc — R005).

### Luồng chuẩn (Happy Path)
1. NCC giao hàng kèm PO `Sample` và PO gốc tương ứng.
2. User scan nhận PO `Sample` vào WMS như PO Gift bình thường.
3. QC SKU của PO `Sample` chạy theo luồng QC thông thường, ghi nhận kết quả `Passed`.
4. PO `Sample` chuyển sang status `Completed`.
5. User scan nhận PO gốc lần đầu — hệ thống cho phép nhận tối đa 30% packing list (R008).
6. Hệ thống tự tạo request QC cho 30% UID group vừa nhận vào.
7. UID mới nhận giữ status `Received` (R009).
8. Sau QC: nếu `Passed` → UID chuyển `Inbin`, cột `Đánh giá đạt = No` cho UID group, chỉ transfer nội kho (R011); nếu `Failed` → UID chuyển `Inbin` (theo R009) nhưng không cho nhận phần còn lại, trả NCC (R010).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — PO Sample chưa Completed nhưng user thử nhận PO gốc:** hệ thống chặn + hiển thị message VN/EN (R006, R007).
- **A2 — QC Sample kết quả `Failed`:** hệ thống chặn + hiển thị message VN/EN; không cho mở phiên nhận PO gốc (R006, R007).

### Luồng ngoại lệ (Exception Paths)
- **E1 — User cố nhận hơn 30% packing list ở phiên đầu:** hệ thống báo lỗi (R012) với message VN/EN.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| `PO.type` | enum mở rộng | ✅ | Thêm value `Sample` (cùng tập với `Gift`, `Normal`, ... — danh sách đầy đủ chưa được liệt kê trong section này, xem Q-001) |
| Liên kết PO Sample ↔ gốc | reference 2 chiều | ✅ | Mỗi PO `Sample` phải có 1 PO gốc; cardinality phía gốc chưa rõ (Q-002) |
| Pre-condition nhận PO gốc | rule | ✅ | PO Sample tương ứng phải có status = `Completed` **AND** QC result = `Đạt`/`Passed` |
| 30% receiving rule | percentage | ✅ | Phiên nhận PO chính **lần đầu** sau Sample passed: max 30% packing list per batch; làm tròn lên (ceil) — ví dụ 18 cây × 30% = 5.4 → 6 cây |
| UID status sau QC | state transition | ✅ | `Received` → `Inbin` (sau QC, cả passed/failed) |
| UID group sau QC passed | rule | ✅ | Cột `Đánh giá đạt = No` được set; UID chỉ transfer nội kho, không IT |
| UID group sau QC failed | rule | ✅ | Block nhận phần còn lại; return vendor toàn bộ |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Trigger | Message VN | Message EN | Source |
|:-------|:--------|:-----------|:-----------|:-------|
| ERR-POS-001 | User scan PO gốc khi PO `Sample` chưa completed hoặc QC không đạt | `PO mẫu thử {sample_po_code} của PO gốc {original_po_code} chưa được nhận hàng hoặc kết quả đánh giá chất lượng KHÔNG ĐẠT nên không thể nhận hàng cho PO gốc.` | `Sample PO {sample_po_code} of original PO {original_po_code} has not been received or the quality evaluation result is FAILED, therefore the original PO cannot be received.` | 07062#L2601-L2606 |
| ERR-POS-002 | User cố nhận vượt 30% packing list trong phiên đầu | `PO chỉ cho nhận tối đa 30% cuộn vải theo từng lô cho phiên nhận đầu tiên.` | `The PO only allows receiving up to 30% of the fabric rolls per batch for the first receiving session.` | 07062#L2621-L2624 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Thêm PO type Sample trên Inside**
  - **Given:** Inside có danh sách PO type hiện hành.
  - **When:** PO Sample được tạo cho PO gốc.
  - **Then:** PO type = `Sample` và có liên kết 2 chiều với PO gốc (R001, R002).
- **AC-02 — Block nhận PO gốc khi Sample chưa Completed**
  - **Given:** PO Sample chưa Completed, hoặc đã Completed nhưng QC `Failed`.
  - **When:** User scan PO gốc để mở phiên nhận hàng.
  - **Then:** Hệ thống chặn, hiển thị message VN+EN theo ERR-POS-001 (R006, R007).
- **AC-03 — Sau Sample passed cho phép nhận PO gốc max 30%**
  - **Given:** PO Sample `Completed` và QC `Passed`.
  - **When:** User mở phiên nhận PO gốc lần đầu.
  - **Then:** Hệ thống cho nhận tối đa 30% packing list (làm tròn lên), tự tạo request QC cho 30% UID group vừa nhận (R008, R012).
- **AC-04 — Block nhận quá 30% trong phiên đầu**
  - **Given:** Đã nhận đủ 30% packing list ở phiên đầu PO gốc.
  - **When:** User cố nhận thêm.
  - **Then:** Hệ thống báo lỗi theo ERR-POS-002 (R012).
- **AC-05 — UID state transition sau QC**
  - **Given:** UID vừa được nhận vào, status = `Received`, chưa có kết quả QC.
  - **When:** QC hoàn tất (passed hoặc failed).
  - **Then:** UID chuyển status sang `Inbin` (R009).
- **AC-06 — UID group QC passed chỉ được transfer nội kho**
  - **Given:** UID group có kết quả QC `Passed`.
  - **When:** Tra cứu UID group sau QC.
  - **Then:** Cột `Đánh giá đạt = No` được set; thao tác IT (inter-warehouse transfer) bị chặn, chỉ cho transfer nội kho (R011).
- **AC-07 — UID group QC failed không cho nhận phần còn lại**
  - **Given:** UID group có kết quả QC `Failed`.
  - **When:** User cố nhận thêm phần còn lại của PO gốc.
  - **Then:** Hệ thống chặn, yêu cầu return vendor toàn bộ phần chưa nhận (R010).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R001 | Danh sách enum đầy đủ của `PO.type` sau khi thêm `Sample`? Raw chỉ đề cập tương tự `Gift` nhưng không liệt kê tất cả values. | PO/Inside team | Open | | | |
| Q-002 | R002 | Cardinality liên kết PO Sample ↔ PO gốc: 1 PO gốc có thể có nhiều PO Sample hay không? Raw không khẳng định. | PO | Open | | | |
| Q-003 | R008 | Cách xác định "lần đầu" nhận PO gốc — flag riêng trong DB, đếm số phiên đã nhận, hay logic khác? | Dev Lead | Open | | | |
| Q-004 | R012 | "30%" áp dụng theo SKU (mỗi SKU 30%) hay theo packing list (tổng số cuộn 30%)? Ví dụ "SKUA packing list có 18 cây" cho thấy theo SKU nhưng cần confirm. | PO | Open | | | |
| Q-005 | R011 | "Đánh giá đạt = No" treo trên UID group là **status display** trong khi chưa hết QC hay flag persistent? Khi nào chuyển sang `Yes`? | PO/Dev | Open | | | |
| Q-006 | R012 | Error message ERR-POS-002 chỉ đề cập "cuộn vải" — áp dụng cho mọi PO type Sample hay chỉ PO vải? | PO | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-60 | 2.17 (stub) | 2.17 | All R + AC | Draft |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_po_sample | test_stub_receiving_po_po_sample | Add (chờ Gate 1B) | [[stub_qc_evaluation_result]] (luồng QC), [[stub_receiving_po_inbound_shipment]] (rules chung) | Q-001..Q-006 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R012, AC-01..AC-07 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-006 |

## 🚧 Blocked Coverage

- R001 — chờ Q-001 (full enum PO.type)
- R002 — chờ Q-002 (cardinality)
- R008 — chờ Q-003 ("lần đầu" detection)
- R011 — chờ Q-005 (semantics "Đánh giá đạt = No")
- R012 — chờ Q-004 (scope 30% per SKU vs packing list) + Q-006 (chỉ vải hay tất cả)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:36:55 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 15:30:00 | v1.1 | Refine stub → full spec: 12 R-ID, 7 AC, 7 BR, 2 error messages, 6 questions Open. `partial_read: false`. | refine-batch-1-2026-05-30 |
