---
spec: stub_receiving_po_gift
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [Functional, UI]
---

# Test Suite — Rules nhận PO Gift (1 gốc - 1 gift và 1 gốc - nhiều gift)

## Phạm vi
- Source spec: [[stub_receiving_po_gift]]
- Active requirements: 3 (R001, R003, R004, R006 — phần clear; R002, R005 phần bị block)
- Blocked: 5 R/AC chờ open questions (R002/Q-004, R005+AC-05/Q-001+Q-002+Q-007, R003+R004/Q-005, R006+AC-07/Q-003)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-GIFT-001 | Case A nhận chung: scan PO gốc trước khi có 1 PO gift → mở phiên nhận chung | R001 / AC-01 | Functional | PO_A có 1 PO gift PO_AG; User scan PO_A trước | Hệ thống mở phiên nhận chung cho PO_A và PO_AG; user có thể nhận hàng cho cả 2 trong cùng phiên | High |
| TC-GIFT-002 | Case C nhiều gift — scan PO gốc → hiển thị thông báo yêu cầu hoàn thành tất cả gift trước | R003 / AC-03 | UI + Functional | PO_X có 2 PO gift PO_XG1 và PO_XG2 đều đủ điều kiện; User scan PO_X | Hệ thống hiển thị ERR-GIFT-001 liệt kê PO_XG1, PO_XG2; chặn nhận PO_X | High |
| TC-GIFT-003 | ERR-GIFT-001 message VN — nhiều gift chưa hoàn thành | R003 | UI | PO gốc có nhiều PO gift đủ điều kiện chưa completed; User scan PO gốc | Message VN: `PO [{po_goc}] có nhiều hơn 1 PO gift ({po_gift_codes}), vui lòng hoàn thành tất cả PO gift trước khi nhận PO gốc.` | High |
| TC-GIFT-004 | ERR-GIFT-001 message EN — nhiều gift chưa hoàn thành | R003 | UI | Như TC-GIFT-003 | Message EN: `PO [{po_goc}] has more than 1 gift PO ({po_gift_codes}), please complete all gift PO before receiving original PO.` | High |
| TC-GIFT-005 | Case C — sau khi hoàn thành tất cả PO gift → cho nhận PO gốc | R004 / AC-04 | Functional | PO_X; User đã completed PO_XG1 và PO_XG2 | User scan PO_X → hệ thống mở phiên nhận PO_X, không hiển thị ERR-GIFT-001 | High |
| TC-GIFT-006 | PO gift thiếu hàng lần đầu — cho nhận chung với PO gốc | R006 / AC-06 | Functional | PO gốc + PO gift; PO gift thiếu hàng so với SL kỳ vọng; Nhận chung lần đầu | Phiên nhận hoàn thành thành công; ghi nhận PO gift thiếu hàng | High |
| TC-GIFT-007 | Decision Table — 1 gốc + 1 gift + gifts đủ điều kiện → không block | R001, R003 | Functional | 1 PO gốc + đúng 1 PO gift; user scan PO gốc | Không hiển thị ERR-GIFT-001 (chỉ báo khi > 1 gift); mở phiên nhận chung | High |
| TC-GIFT-008 | State Transition — PO gift status Completed → cho nhận PO gốc | R004 | Functional | PO gift đạt status Completed | PO gốc có thể được scan nhận | High |

## 🚧 Blocked Coverage

- **R002 (AC-02, Q-004)** — chờ xác nhận UI confirm khi user "nhận riêng PO gift" (hỏi confirm hay mở phiên trực tiếp). Không thể test UI confirm dialog.
- **R005 (AC-05, Q-001)** — chờ danh sách đầy đủ các điều kiện để PO gift "đủ điều kiện nhận" (raw chỉ ví dụ `invoice chưa verify`). Không thể test hết các override condition.
- **R005 (AC-05, Q-002)** — chờ xác nhận audit/log và notification khi PO gift pending. Không thể test audit trail.
- **R005 (AC-05, Q-007)** — chờ confirm raw typo "gift → gốc" ở L1755-L1756. Không thể thiết kế TC cho R005 khi chưa xác nhận behavior đúng.
- **R003, R004 (Q-005)** — chờ xác nhận định nghĩa "hoàn thành" PO gift (status Completed hay có % tối thiểu). Không thể test boundary điều kiện "hoàn thành".
- **R006, AC-07 (Q-003)** — chờ cách detect "lần sau" khi NCC giao lại (flag DB hay đếm session). Không thể test enforcement bắt buộc nhận riêng.

## Regression Impact
- [[stub_receiving_po_invoice]] — điều kiện verify invoice cho PO gift
- [[stub_receiving_po_inbound_shipment]] — status Completed PO gift, luồng chung

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.2. 8 TC active, 6 blocked coverage item.
