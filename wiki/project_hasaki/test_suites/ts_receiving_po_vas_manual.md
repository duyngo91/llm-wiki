---
spec: stub_receiving_po_vas_manual
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [Functional, UI]
---

# Test Suite — Create/Update VAS Manual (Web + App)

## Phạm vi
- Source spec: [[stub_receiving_po_vas_manual]]
- Active requirements: 9 (R001, R002, R003, R004, R005, R008, R009, R010, R012, R013, R014, R015, R019 — phần không bị block)
- Blocked: 14 R-ID chờ open questions (R016/Q-003, R017+R018/Q-004, ERR-VSM-001+ERR-VSM-002/Q-005, R007+MSG-VSM-003/Q-006, R003/Q-007, R005/Q-008, R011/Q-009, R014/Q-010, R002/Q-011, R006/Q-012, R010/Q-013, R013/Q-014)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-VSM-001 | Listing VAS — cột Type hiển thị "Manual" cho VAS tạo thủ công | R001 / AC-01 | UI | VAS Manual đã được tạo; Mở Inbound/VAS | Cột Type = "Manual" cho VAS đó | High |
| TC-VSM-002 | Update Qty received cho VAS Manual status Open | R002 / AC-02 | Functional | VAS-M Manual status Open; Qty=100; Sửa thành 95 | Qty received cập nhật = 95 | High |
| TC-VSM-003 | Update Qty received cho VAS Manual status In-Progress | R002 / AC-03 | Functional | VAS-M Manual status In-Progress; Qty=50; Sửa thành 48 | Lưu thành công Qty=48 | High |
| TC-VSM-004 | Không cho update Qty VAS auto-gen | R002 / AC-04 | Functional | VAS-Auto Type ≠ Manual; cố sửa Qty | Field disable, không cho sửa | High |
| TC-VSM-005 | Không cho update Qty VAS Manual Completed | R002 / AC-05 | Functional | VAS-M Manual Completed; cố sửa Qty | Field disable | High |
| TC-VSM-006 | Sinh VAS RFID khi nhận PO SKU RFID vendor ngoài (không Thời trang, không Synctive) | R003 / AC-06 | Functional | PO có SKU config RFID, không Thời trang, không Synctive; nhận SP theo SL | Hệ thống sinh VAS type RFID cho SP | High |
| TC-VSM-007 | Khai báo RFID — scan từng barcode | R004 / AC-07 | Functional | VAS RFID; SP cần khai báo SL=10; scan 10 RFID lần lượt | 10 RFID add vào danh sách; có thể Lưu | High |
| TC-VSM-008 | Khai báo RFID — scan hàng loạt bằng máy | R004 / AC-08 | Functional | VAS RFID; máy scan đọc 10 RFID | 10 RFID add vào danh sách | High |
| TC-VSM-009 | RFID đã tồn tại trên hệ thống = không hợp lệ | R005 / AC-09 | Functional | RFID-001 đã tồn tại; scan RFID-001 | Không hợp lệ; không add vào danh sách | High |
| TC-VSM-010 | Button "Hoàn thành" chỉ hiện khi tất cả SKU khai báo đủ SL | R008 / AC-11 | UI + Functional | VAS 3 SKU; khai báo đủ 2 SKU | Button "Hoàn thành" không show. Khi SKU 3 đủ → button show | High |
| TC-VSM-011 | Tạo mới VAS — Kho default từ kho ngoài | R010 / AC-12 | UI + Functional | User ở kho A trong list VAS; click "Tạo mới" | Field Kho prefill = kho A; user có thể đổi | High |
| TC-VSM-012 | Tạo mới VAS — Kho load theo phân quyền user | R010 / AC-13 | Functional | User có quyền kho A và B; click Kho dropdown | Dropdown chỉ hiển thị {kho A, kho B} | High |
| TC-VSM-013 | Loại VAS bắt buộc chọn | R011-partial / AC-14 | Functional | Form mở; để trống Loại VAS; click "Tạo mới" | Block; validation Loại VAS bắt buộc | High |
| TC-VSM-014 | Mã phiếu nhập nguồn optional | R012 / AC-15 | Functional | Để trống Mã phiếu nhập nguồn; click "Tạo mới" | Pass validation (optional) | High |
| TC-VSM-015 | Mã phiếu nhập nguồn không tồn tại → ERR-VSM-001 | R012 / AC-16 | Functional | Nhập Mã phiếu nhập nguồn = "PO-XYZ" không tồn tại | ERR-VSM-001 VN: `Mã [Code] không tồn tại trên hệ thống.` | High |
| TC-VSM-016 | Thêm SP bằng scan barcode | R013 / AC-17 | Functional | Scan barcode "BC-001" của SP-A | SP-A add vào danh sách + check tồn kho | High |
| TC-VSM-017 | Tồn kho check In-Bin + Picklisted (không tính Received) | R014 / AC-18 | Functional | SKU SP-A: 80 UID In-Bin + 40 Picklisted + 30 Received | Hiển thị "Số lượng tồn kho = 120" (80+40; không tính 30 Received) | High |
| TC-VSM-018 | SL cần khai báo > tồn kho → ERR-VSM-002 | R015 / AC-19 | Functional | Tồn kho SP-A = 120; nhập SL cần khai báo = 125 | ERR-VSM-002 VN: `Số lượng cần khai báo (125) không được lớn hơn số lượng tồn kho trên hệ thống (120).` | High |
| TC-VSM-019 | BVA — SL cần khai báo = tồn kho (boundary) | R015 | Functional | Tồn kho = 120; nhập 120 | Pass validation | High |
| TC-VSM-020 | BVA — SL cần khai báo = tồn kho + 1 (boundary+1) | R015 | Functional | Tồn kho = 120; nhập 121 | ERR-VSM-002 | High |
| TC-VSM-021 | Tạo VAS thành công → chuyển sang flow khai báo | R019 / AC-22 | Functional | Form đủ thông tin; click "Tạo mới" → confirm → Xác nhận | VAS được tạo; chuyển sang flow khai báo cho VAS vừa tạo | High |
| TC-VSM-022 | SL RFID scan > SL cần khai báo → thông báo (behavior) | R007-partial / AC-10 | Functional | SP cần 10 RFID; scan 12 RFID | Thông báo MSG-VSM-003 hiển thị (behavior block được xác nhận dù verbatim chờ Q-006) | High |
| TC-VSM-023 | Sau cảnh báo SL dư — user xóa RFID dư | R007 | Functional | Sau thông báo SL dư; user xóa 2 RFID dư | SL còn đúng 10; không còn thông báo | High |
| TC-VSM-024 | Loại VAS RFID + SKU config RFID — add thành công | R016-behavior-only | Functional | Loại VAS = RFID; SKU SP-C có config RFID | SP-C add thành công vào danh sách | High |

## 🚧 Blocked Coverage

- **R016, MSG-VSM-004 (Q-003)** — chờ verbatim VN+EN khi SKU không config tương ứng Loại VAS. Không thể test message text.
- **R017, R018, MSG-VSM-005, MSG-VSM-006 (Q-004)** — chờ verbatim VN+EN cho 2 confirm dialog (xóa SKU + tạo mới VAS). Không thể test message text.
- **ERR-VSM-001, ERR-VSM-002 (Q-005)** — chờ verbatim EN. TC-VSM-015/018 chỉ test VN message.
- **R007, MSG-VSM-003 (Q-006)** — chờ verbatim VN+EN message SL RFID dư. TC-VSM-022 test behavior nhưng không verify message text.
- **R003 (Q-007)** — chờ định nghĩa chính xác "Thời trang" và "Synctive" (master data flag, category code). Không thể test boundary category.
- **R005 (Q-008)** — chờ xác nhận phân biệt 2 flow RFID (vendor ngoài vs nội bộ Long An). Không thể test isolation 2 flow.
- **R011 (Q-009)** — chờ xác nhận enum Loại VAS đầy đủ (chỉ RFID + Serial hay có thêm Imei, Label). Không thể test các values tiềm năng.
- **R014 (Q-010)** — chờ xác nhận lý do business skip Received trong tồn kho check. Không thể test edge case UID Received.
- **R002 (Q-011)** — chờ xác nhận audit log + validation tối thiểu cho Qty received update. Không thể test audit.
- **R006 (Q-012)** — chờ xác nhận detect RFID lẫn khi scan hàng loạt. Không thể test mix detection.
- **R010 (Q-013)** — chờ xác nhận Loại VAS có thể đổi sau khi tạo (immutable hay không). Không thể test change Loại VAS.
- **R013 (Q-014)** — chờ xác nhận modal tìm tên (auto-complete suggest hay strict equal). Không thể test search modal.

## Regression Impact
- [[stub_receiving_po_vas]] — VAS listing/detail base
- [[stub_receiving_po_confirm_paste_id]] — flow khai báo VAS

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.1. 24 TC active, 14 blocked coverage item.
