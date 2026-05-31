---
aliases: [stub_receiving_po_gift]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_gift
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L1738-L1758
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 23:00:00"
verification_status: Verified
approval_note: "PASS. FIX-001 applied 2026-05-30 — Q-007 captures UNCLEAR R005 (raw typo gift→gốc). Awaits PO Gate 1B answer."
approved_by:
approved_at:
approval_note:
---

# REQ: stub_receiving_po_gift

## Tổng quan
- **Mã tính năng:** stub_receiving_po_gift
- **Feature:** Bổ sung rules nhận PO Gift riêng (case 1 gốc - 1 gift và 1 gốc - nhiều gift)
- **Mô tả ngắn:** Quy định luồng nhận PO Gift trong 2 case: 1 PO gốc có 1 PO gift (cho nhận chung hoặc nhận riêng) và 1 PO gốc có nhiều PO gift (bắt buộc hoàn thành hết gift trước khi nhận gốc). Có override: nếu gift chưa đủ điều kiện (vd chưa verify invoice) thì cho nhận gốc trước; nếu gift thiếu hàng thì lần sau bắt buộc nhận riêng.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Nhân viên kho (User scan nhận hàng).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[ts_receiving_po_gift]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_receiving_po_invoice]] (điều kiện verify invoice cho PO gift). ℹ️ Liên quan [[stub_receiving_po_inbound_shipment]] (status `Completed` PO gift).

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
| R001 | Case 1 PO gốc có 1 PO gift: cho phép nhận chung PO gốc và PO gift nếu scan PO gốc trước | Functional | High | ✅ | 07062#L1740-L1742 |
| R002 | Case 1 PO gốc có 1 PO gift: cho phép nhận riêng PO gift (không qua PO gốc) | Functional | High | ✅ | 07062#L1743-L1744 |
| R003 | Case 1 PO gốc có nhiều PO gift: hiển thị thông báo song ngữ VN/EN yêu cầu hoàn thành tất cả PO gift trước khi nhận PO gốc | Functional | High | ✅ | 07062#L1745-L1751 |
| R004 | Case 1 PO gốc có nhiều PO gift: user scan nhận từng PO gift đến khi hoàn thành, sau đó mới scan PO gốc để nhận | Functional | High | ✅ | 07062#L1752-L1753 |
| R005 | Override (Update 22-01-2025): nếu tại thời điểm scan nhận PO gốc mà PO gift chưa đủ điều kiện nhận (vd chưa verify invoice), hệ thống không hiện thông báo R003 và cho nhận PO gốc; PO gift sẽ scan nhận sau khi đủ điều kiện. **Lưu ý:** raw L1755-L1756 ghi "cho nhận PO gift" — spec interpret là "cho nhận PO gốc" do context (trigger = scan PO gốc; PO gift chưa đủ điều kiện thì không thể "cho nhận PO gift"); cần PO confirm raw typo gift→gốc — xem Q-007 | Business rule | High | ⚠️ | 07062#L1755-L1756 |
| R006 | Update 22-01-2025: nếu PO gift thiếu hàng → lần đầu được nhận chung với PO gốc (cả PO có thể nhận thiếu hoặc không); **lần sau** khi NCC giao lại thì phải nhận riêng cho cả Gift và gốc | Business rule | High | ✅ | 07062#L1757-L1758 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- PO gốc và (các) PO gift đã được tạo trên Inside và liên kết với nhau.
- Hàng vật lý đã giao tới kho.

### Luồng chuẩn (Happy Path)

**Case A — 1 PO gốc + 1 PO gift, nhận chung:**
1. User scan PO gốc trước (R001).
2. Hệ thống mở phiên nhận cho cả PO gốc và PO gift chung.
3. User nhận hàng cho cả 2 PO trong cùng phiên.

**Case B — 1 PO gốc + 1 PO gift, nhận riêng:**
1. User scan PO gift trước (không scan PO gốc) (R002).
2. Hệ thống mở phiên nhận chỉ cho PO gift.
3. User hoàn thành PO gift.
4. Sau đó user scan PO gốc, mở phiên nhận PO gốc riêng.

**Case C — 1 PO gốc + nhiều PO gift:**
1. User scan PO gốc trước.
2. Hệ thống hiển thị thông báo ERR-GIFT-001 (R003) liệt kê danh sách PO gift, yêu cầu hoàn thành tất cả trước.
3. User scan từng PO gift, hoàn thành lần lượt (R004).
4. Sau khi tất cả PO gift `Completed`, user scan PO gốc → mở phiên nhận PO gốc.

### Luồng rẽ nhánh (Alternative Paths)

- **A1 — Override khi PO gift chưa đủ điều kiện (R005):** trong case C, nếu một hoặc nhiều PO gift chưa đủ điều kiện nhận (vd `invoice chưa verify`), hệ thống KHÔNG hiển thị ERR-GIFT-001 và cho phép user nhận PO gốc; các PO gift sẽ scan nhận sau khi đủ điều kiện.
- **A2 — PO gift thiếu hàng, lần đầu nhận chung (R006):** nếu PO gift bị thiếu hàng, lần đầu nhận chung với PO gốc, cho phép PO nhận thiếu (hoặc không thiếu) như bình thường.

### Luồng ngoại lệ (Exception Paths)

- **E1 — PO gift thiếu hàng, lần sau NCC giao lại (R006):** lần nhận tiếp theo bắt buộc phải nhận riêng cho cả Gift và gốc (không cho phép nhận chung).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Cardinality PO gốc - PO gift | reference | ✅ | 1 PO gốc có 0..n PO gift; mỗi PO gift link với 1 PO gốc |
| Case A (1 gốc - 1 gift) | rule | ✅ | Cho phép nhận chung (scan PO gốc trước) hoặc nhận riêng (scan PO gift) |
| Case C (1 gốc - nhiều gift) | rule | ✅ | Phải hoàn thành tất cả PO gift (`Completed`) trước khi nhận PO gốc; nếu user scan PO gốc trước → ERR-GIFT-001 |
| Override "PO gift chưa đủ điều kiện" | rule | ✅ | Khi nhận PO gốc (R003 nếu trigger), check PO gift `đủ điều kiện` (vd `invoice đã verify`): nếu có ≥1 gift chưa đủ → bỏ qua thông báo R003, cho nhận PO gốc. Danh sách đầy đủ điều kiện — xem Q-001. |
| PO gift thiếu hàng → ràng buộc lần sau | rule | ✅ | Lần đầu nhận chung được phép thiếu; lần sau (giao lại) bắt buộc nhận riêng cho cả Gift và gốc |
| "Lần sau" detection | rule | ⚠️ | Cách detect chưa rõ — flag DB, session count, hay query lịch sử ASN? Xem Q-003 |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Trigger | Message VN | Message EN | Source |
|:-------|:--------|:-----------|:-----------|:-------|
| ERR-GIFT-001 | User scan PO gốc khi PO gốc có nhiều hơn 1 PO gift chưa hoàn thành (và tất cả PO gift đều đủ điều kiện) | `PO [{po_goc}] có nhiều hơn 1 PO gift ({po_gift_codes}), vui lòng hoàn thành tất cả PO gift trước khi nhận PO gốc.` | `PO [{po_goc}] has more than 1 gift PO ({po_gift_codes}), please complete all gift PO before receiving original PO.` | 07062#L1748-L1751 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Case A nhận chung (1 gốc + 1 gift, scan gốc trước)**
  - **Given:** PO gốc `PO_A` có 1 PO gift `PO_AG`.
  - **When:** User scan `PO_A` trước.
  - **Then:** Hệ thống mở phiên nhận chung cho `PO_A` và `PO_AG`; user có thể nhận hàng cho cả 2 trong cùng phiên (R001).
- **AC-02 — Case A nhận riêng PO gift**
  - **Given:** PO gốc `PO_A` có 1 PO gift `PO_AG`.
  - **When:** User scan `PO_AG` trước (không qua `PO_A`).
  - **Then:** Hệ thống mở phiên nhận chỉ cho `PO_AG`; user hoàn thành riêng (R002).
- **AC-03 — Case C scan PO gốc khi có nhiều PO gift**
  - **Given:** PO gốc `PO_X` có 2 PO gift `PO_XG1`, `PO_XG2`, cả 2 đều đủ điều kiện nhận.
  - **When:** User scan `PO_X`.
  - **Then:** Hệ thống hiển thị ERR-GIFT-001 với danh sách `PO_XG1`, `PO_XG2`; chặn nhận `PO_X` (R003).
- **AC-04 — Case C hoàn thành PO gift trước**
  - **Given:** Như AC-03, sau khi user scan và `Completed` cả `PO_XG1` lẫn `PO_XG2`.
  - **When:** User scan `PO_X`.
  - **Then:** Hệ thống mở phiên nhận `PO_X`; không hiện ERR-GIFT-001 (R004).
- **AC-05 — Override khi PO gift chưa verify invoice**
  - **Given:** PO gốc `PO_Y` có 2 PO gift; `PO_YG1` chưa verify invoice (chưa đủ điều kiện); `PO_YG2` đủ điều kiện.
  - **When:** User scan `PO_Y`.
  - **Then:** Hệ thống KHÔNG hiển thị ERR-GIFT-001; cho phép user nhận `PO_Y`; `PO_YG1` và `PO_YG2` sẽ scan nhận sau khi đủ điều kiện (R005).
- **AC-06 — PO gift thiếu hàng lần đầu nhận chung**
  - **Given:** PO gốc `PO_Z` + PO gift `PO_ZG`, scan chung; PO gift thiếu hàng so với SL kỳ vọng.
  - **When:** User submit phiên nhận.
  - **Then:** Phiên completed thành công, ghi nhận PO gift thiếu hàng (R006).
- **AC-07 — PO gift thiếu hàng lần sau bắt buộc nhận riêng**
  - **Given:** PO gift `PO_ZG` đã nhận thiếu lần đầu; NCC giao lại phần còn lại.
  - **When:** User scan `PO_ZG` lần 2.
  - **Then:** Hệ thống chỉ cho phép nhận riêng PO gift; không cho nhận chung với PO gốc (R006).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R005 | Danh sách đầy đủ "điều kiện đủ để nhận" PO gift? Raw chỉ ví dụ `invoice chưa verify` — còn các điều kiện khác (vd status PO gift, tồn kho, hạn nhận, ...) không được liệt kê. | PO | Open | | | |
| Q-002 | R005 | Khi PO gift chưa đủ điều kiện và đã cho nhận PO gốc trước, có audit / log riêng để track PO gift `pending` không? Hệ thống có notification khi gift đủ điều kiện không? | PO/Dev | Open | | | |
| Q-003 | R006 | "Lần sau" được detect thế nào? Flag riêng, đếm số session nhận đã có, hay logic timeline khác? | Dev Lead | Open | | | |
| Q-004 | R001-R002 | Khi user chọn "nhận riêng PO gift" (R002), hệ thống có hỏi confirm hay mở phiên trực tiếp? Raw không mô tả UI confirm. | UX | Open | | | |
| Q-005 | R003, R004 | "Hoàn thành" PO gift là status `Completed` hay khái niệm khác? Có ràng buộc PO gift phải có ≥ X% hàng nhận mới được tính `Completed` không? | PO | Open | | | |
| Q-007 | R005, AC-05 | Raw 07062#L1755-L1756 ghi "thì sẽ không hiện thông báo và cho nhận PO gift" — trong context "scan nhận PO gốc" + "PO gift chưa đủ điều kiện", spec interpret là "cho nhận PO gốc". Đây là typo của raw (gift → gốc) đúng không? Refiner UNCLEAR finding pilot-batch-1 FIX-001. | PO | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-34, S-35 | 2.17 (stub) | 2.17 | All R + AC | Draft |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_gift | test_stub_receiving_po_gift | Add (chờ Gate 1B) | [[stub_receiving_po_invoice]] (điều kiện verify invoice), [[stub_receiving_po_inbound_shipment]] (PO complete flow) | Q-001..Q-005 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R006, AC-01..AC-07 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-005 |

## 🚧 Blocked Coverage

- R005, AC-05 — chờ Q-001 (danh sách đầy đủ điều kiện đủ), Q-002 (audit + notification)
- R006, AC-07 — chờ Q-003 (cách detect "lần sau")
- R002 — chờ Q-004 (UI confirm khi nhận riêng PO gift)
- R003, R004 — chờ Q-005 (định nghĩa "hoàn thành" PO gift)
- R005, AC-05 — chờ Q-007 (raw typo gift → gốc — refiner UNCLEAR FIX-001)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:36:55 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 15:45:00 | v1.1 | Refine stub → full spec: 6 R-ID, 7 AC, 6 BR, 1 error message verbatim VN/EN, 5 questions Open. `partial_read: false`. | refine-batch-1-2026-05-30 |
| 2026-05-30 23:00:00 | v1.2 | Apply refiner FIX-001 — thêm Q-007 cho UNCLEAR R005 (raw typo gift→gốc), inline note trong R005 claim text, link Blocked Coverage. | refiner-pilot-batch-1 |
