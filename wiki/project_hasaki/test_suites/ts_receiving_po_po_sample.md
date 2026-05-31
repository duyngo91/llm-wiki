---
spec: stub_receiving_po_po_sample
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [Functional, UI]
---

# Test Suite — PO Sample (PO mẫu thử) & PO chính

## Phạm vi
- Source spec: [[stub_receiving_po_po_sample]]
- Active requirements: 7 (R003, R004, R005, R006, R007, R008, R009 — phần không bị block)
- Blocked: 5 R/AC chờ open questions (R001/Q-001, R002/Q-002, R008/Q-003, R011/Q-005, R012/Q-004 + Q-006)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-POS-001 | QC Sample chạy theo luồng QC thông thường | R004 / AC-01 | Functional | PO Sample có SKU cần QC | QC SKU chạy theo luồng QC thông thường, ghi nhận kết quả | High |
| TC-POS-002 | Tiêu chí QC giống nhau cho PO Sample và PO gốc (Phase 1) | R005 | Functional | SKU tồn tại trong cả PO Sample và PO gốc | Tiêu chí QC được thiết lập giống nhau cho cả 2 PO | Medium |
| TC-POS-003 | Block nhận PO gốc khi PO Sample chưa Completed | R006 / AC-02 | Functional | Scan PO gốc khi PO Sample status ≠ Completed | Hệ thống chặn, không mở phiên nhận PO gốc | High |
| TC-POS-004 | Block nhận PO gốc khi QC Sample = Failed | R006 / AC-02 | Functional | Scan PO gốc khi PO Sample Completed + QC = Failed | Hệ thống chặn, không mở phiên nhận PO gốc | High |
| TC-POS-005 | Thông báo song ngữ VN/EN khi block nhận PO gốc — Sample chưa Completed | R007 / AC-02 | UI | Scan PO gốc khi PO Sample chưa Completed | Message VN: `PO mẫu thử {sample_po_code} của PO gốc {original_po_code} chưa được nhận hàng hoặc kết quả đánh giá chất lượng KHÔNG ĐẠT nên không thể nhận hàng cho PO gốc.` / EN tương ứng (ERR-POS-001) | High |
| TC-POS-006 | Thông báo song ngữ VN/EN khi block nhận PO gốc — QC Failed | R007 / AC-02 | UI | Scan PO gốc khi QC Sample = Failed | Message ERR-POS-001 hiện song ngữ VN+EN | High |
| TC-POS-007 | Sau Sample Passed: cho nhận PO gốc lần đầu tối đa 30% packing list (ceil) | R008 / AC-03 | Functional | PO Sample Completed + QC Passed; packing list = 18 cây | Hệ thống cho nhận tối đa ceil(18 × 30%) = 6 cây; auto tạo request QC cho 6 UID group | High |
| TC-POS-008 | Tạo request QC tự động cho 30% UID group vừa nhận | R008 / AC-03 | Functional | Nhận 30% packing list thành công | Hệ thống tự tạo request QC cho 30% UID group vừa nhận | High |
| TC-POS-009 | UID mới nhận giữ status Received (chưa QC) | R009 / AC-05 | Functional | UID vừa được nhận vào | UID status = Received trước khi có kết quả QC | High |
| TC-POS-010 | UID chuyển Inbin sau khi QC hoàn tất (Passed) | R009 / AC-05 | Functional | QC hoàn tất, kết quả Passed | UID chuyển status Received → Inbin | High |
| TC-POS-011 | UID chuyển Inbin sau khi QC hoàn tất (Failed) | R009 / AC-05 | Functional | QC hoàn tất, kết quả Failed | UID chuyển status Received → Inbin (cả 2 trường hợp Passed và Failed đều chuyển) | High |
| TC-POS-012 | UID group QC Failed — không cho nhận phần còn lại, yêu cầu return vendor | R010 / AC-07 | Functional | UID group QC Failed | Hệ thống chặn nhận phần còn lại của PO gốc; yêu cầu return vendor toàn bộ phần chưa nhận | High |
| TC-POS-013 | Block nhận quá 30% trong phiên đầu PO gốc | R012 / AC-04 | Functional | User cố nhận thêm sau khi đã nhận đủ 30% | Hệ thống báo lỗi ERR-POS-002 | High |
| TC-POS-014 | Thông báo song ngữ khi nhận vượt 30% | R012 / AC-04 | UI | User cố nhận vượt giới hạn 30% packing list | Message VN: `PO chỉ cho nhận tối đa 30% cuộn vải theo từng lô cho phiên nhận đầu tiên.` / EN tương ứng (ERR-POS-002) | High |
| TC-POS-015 | BVA — Nhận đúng bằng 30% packing list (ceil) | R008 | Functional | Packing list 18 cây; nhận đúng 6 cây (= ceil(18×30%)) | Cho nhận thành công, không lỗi | High |
| TC-POS-016 | BVA — Nhận vượt 1 đơn vị trên giới hạn 30% | R012 | Functional | Packing list 18 cây; cố nhận 7 cây (> 6 cây giới hạn) | Hệ thống từ chối, báo ERR-POS-002 | High |

## 🚧 Blocked Coverage

- **R001 (AC-01)** — chờ Q-001: danh sách enum đầy đủ của `PO.type` sau khi thêm `Sample`. Không thể test mọi transition enum cho đến khi có danh sách đầy đủ.
- **R002** — chờ Q-002: cardinality 1 PO gốc ↔ n PO Sample. Không thể test case 1 gốc nhiều sample.
- **R008 (Q-003)** — chờ xác nhận cách detect "lần đầu" nhận PO gốc (flag DB, đếm phiên, hay logic khác). TC-POS-007 test behavior nhưng không thể verify cơ chế detect.
- **R011 (AC-06)** — chờ Q-005: semantics "Đánh giá đạt = No" — display hay flag persistent, khi nào chuyển sang Yes. Không thể test trạng thái sau QC Passed đầy đủ.
- **R011 (AC-06)** — chờ Q-005: UID group QC Passed chỉ transfer nội kho, chặn IT. Không thể test chặn IT khi chưa rõ semantics.
- **R012 (Q-004)** — chờ xác nhận "30%" theo SKU (mỗi SKU 30%) hay theo packing list tổng. TC-POS-007/015/016 dựa trên assumption tổng packing list.
- **R012 (Q-006)** — chờ xác nhận ERR-POS-002 "cuộn vải" áp dụng cho mọi PO type Sample hay chỉ PO vải.

## Regression Impact
- [[stub_qc_evaluation_result]] — flow QC quyết định việc nhận PO gốc (R006/R007)
- [[stub_receiving_po_inbound_shipment]] — rules chung inbound, ASN status

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.1. 16 TC active, 7 blocked coverage item.
