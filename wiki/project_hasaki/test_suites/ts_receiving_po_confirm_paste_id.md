---
spec: stub_receiving_po_confirm_paste_id
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [Functional, UI]
---

# Test Suite — Confirm paste ID (App) — Flow 5 step xác nhận dán ID

## Phạm vi
- Source spec: [[stub_receiving_po_confirm_paste_id]]
- Active requirements: 20 (R001-R012, R015-R020, R022-R026, R028-R034 — phần không bị block)
- Blocked: 14 R-ID chờ open questions (R011/Q-001, R021/Q-002, R013+MSG-CPI-005/Q-003, R027+MSG-CPI-006/Q-004, R033+R034+MSG-CPI-007+MSG-CPI-008/Q-005, R014/Q-006, R007/Q-007, R029+R030/Q-008, R030+R031/Q-009, R032/Q-010, R012/Q-011, R018/Q-012, R023/Q-013, R006/Q-014)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-CPI-001 | Login App + vào Confirm paste ID | R001 / AC-01 | UI + Functional | User login App hợp lệ; chọn "Purchase order / Confirm paste ID" | Màn hình scan PO mở | High |
| TC-CPI-002 | Step 1: PO chưa nhận hàng → ERR-CPI-001 | R002 / AC-02 | Functional | Scan PO status "New" (chưa Receiving/Received) | ERR-CPI-001 VN: `PO [PO code] chưa được nhận hàng.` / EN tương ứng | High |
| TC-CPI-003 | Step 1: PO không tồn tại → ERR-CPI-002 | R003 / AC-03 | Functional | Scan PO không tồn tại | ERR-CPI-002 VN+EN | High |
| TC-CPI-004 | Step 1: PO khác kho → ERR-CPI-003 | R004 / AC-04 | Functional | User kho A; scan PO thuộc kho B | ERR-CPI-003 VN+EN | High |
| TC-CPI-005 | Step 1: PO VAS Completed → ERR-CPI-004 | R005 / AC-05 | Functional | Scan PO đã hoàn thành dán ID | ERR-CPI-004 VN+EN | High |
| TC-CPI-006 | Step 1: PO hợp lệ → hiển thị danh sách phiên VAS | R006 / AC-06 | Functional | Scan PO hợp lệ | Danh sách phiên VAS với Mã VAS, Trạng thái, Loại VAS, Đánh giá, Người dán, Phiên ASN, Ngày nhận, Tổng SKU/item, Vị trí | High |
| TC-CPI-007 | Step 2: Phân biệt màu Xám/Xanh dương/Cam | R007 / AC-07 | UI | VAS-A Mới đã đánh giá; VAS-B In-Progress; VAS-C Mới chưa đánh giá QC | VAS-A Xám; VAS-B Xanh dương; VAS-C Cam | High |
| TC-CPI-008 | Step 2: Chọn VAS → chuyển In-Progress + màu Xanh dương | R008 / AC-08 | Functional | Chọn VAS-A status Mới Xám | VAS-A chuyển In-Progress; màu Xanh dương | High |
| TC-CPI-009 | Mutex user: VAS In-Progress của user khác → disable | R010 / AC-09 | Functional | VAS-A đang In-Progress bởi user1; user2 xem danh sách | VAS-A hiển thị disable, không cho user2 chọn | High |
| TC-CPI-010 | Multi-user 1 VAS: 2 user cùng dán VAS | R011-partial / AC-10 | Functional | user3 và user4 cùng vào VAS-C | Cả 2 có thể vào; API validate realtime (behavior: không trùng QRCode) | High |
| TC-CPI-011 | Crash recovery: scan lại PO → vào lại màn hình dán | R012 / AC-11 | Functional | user5 dán VAS-D chưa lưu; app crash; scan lại PO | Vào trực tiếp màn hình dán VAS-D (không cần chọn lại phiên) | High |
| TC-CPI-012 | Step 3: max 5 hình | R018 / AC-15 | Functional | Form chụp hình; chụp 5 hình | Button "+" disable, không cho chụp thêm | High |
| TC-CPI-013 | BVA Step 3: chụp 4 hình vẫn được (max-1) | R018 | Functional | Chụp 4 hình | Thành công; vẫn cho chụp thêm 1 | Medium |
| TC-CPI-014 | Step 3: video tối đa 15s | R018 / AC-16 | Functional | Quay video 16s | Hệ thống stop tại 15s; chỉ lưu 15s đầu | High |
| TC-CPI-015 | Step 3: hình + video cùng 1 SP | R018 / AC-17 | Functional | Chụp 3 hình + 1 video | Cả 2 media lưu thành công | High |
| TC-CPI-016 | SP không Imei: Lưu = hoàn thành VAS cho SKU đó | R019 / AC-18 | Functional | SKU không quản lý Imei; chụp hình; click "Lưu" | VAS cho SKU hoàn thành; UID Received → In-Bin | High |
| TC-CPI-017 | Step 4: auto chọn QRCode cho CCDC (wms_config & 131072 > 0) | R021 / AC-19 | Functional | SP CCDC có wms_config & 131072 > 0; vào Step 4 | Option QRCode auto bật | High |
| TC-CPI-018 | Update 25-02-2025: Serial OFF, chỉ QRCode | R022 / AC-20 | Functional | SP CCDC; vào Step 4 | Serial không có; tự gen `[1023][YYMMDD][6 số]` | High |
| TC-CPI-019 | Update 22-05-2025: Imei auto bật nhưng không bắt buộc | R023 / AC-21 | Functional | SKU required Imei; form Step 4 mở | Option Imei auto bật; user có thể skip → vẫn pass | High |
| TC-CPI-020 | QRCode parser Object → lấy field "Code" | R025 / AC-22 | Functional | QRCode in `{"Code":"ABC123","Other":"xyz"}` | Hệ thống add "ABC123" vào danh sách | High |
| TC-CPI-021 | Auto focus: QRCode scan pass → focus qua ô Serial | R026 / AC-23 | UI | Cả 2 QRCode + Serial ON; scan QRCode hợp lệ | Focus tự chuyển sang ô scan Serial/Imei | High |
| TC-CPI-022 | Phân biệt màu Step 4: Xám/Xanh dương/Xanh lá | R028 / AC-24 | UI | SP-1 chưa cập nhật, SP-2 cập nhật 3/5, SP-3 cập nhật đủ 5/5 | SP-1 Xám; SP-2 Xanh dương; SP-3 Xanh lá | High |
| TC-CPI-023 | RFID Case 1 (nội bộ Hasaki): cho cả 2 option scan | R030 / AC-25 | Functional | SP từ nhà máy Long An (RFID đã define); chọn scan nhiều SKU cùng lúc | Tab Hợp lệ hiển thị RFID; tab không hợp lệ rỗng | High |
| TC-CPI-024 | RFID Case 2 (vendor ngoài): chỉ scan từng SKU | R031 / AC-26 | Functional | SP từ vendor ngoài; cố scan nhiều SKU cùng lúc | Hệ thống chặn; chỉ cho scan từng SKU | High |
| TC-CPI-025 | Hoàn thành chưa đủ → VAS giữ In-Progress | R033 / AC-27 | Functional | VAS có 10 SP; cập nhật 6 SP; click "Hoàn thành" → confirm Yes | VAS giữ In-Progress; 6 UID đã update QRCode/Serial/Imei | High |
| TC-CPI-026 | Hoàn thành đủ → VAS Completed | R034 / AC-28 | Functional | VAS 10 SP; cập nhật đủ 10; click "Hoàn thành" → Yes | VAS Completed; 10 UID update đầy đủ | High |
| TC-CPI-027 | SKU required RFID: skip bước chụp hình | R029 / AC-29 | Functional | SKU required RFID | Step 3 bị skip; chuyển thẳng sang RFID | High |
| TC-CPI-028 | Step 3: SP không áp dụng chụp hình cho cate "Sức khoẻ - Làm đẹp" | R015 / AC-13 | Functional | SP cate "Sức khoẻ - Làm đẹp" required Imei | Bỏ qua Step 3 chụp hình → vào Step 4 trực tiếp | High |
| TC-CPI-029 | Step 3: áp dụng cho SP required Serial/Imei (Update 23-04-2025) | R015 / AC-14 | Functional | SP cate "CCDC" required Serial | Step 3 chụp hình áp dụng | High |
| TC-CPI-030 | Step 3: không áp dụng cho cate Thuốc | R014-partial | Functional | SP cate "Thuốc" | Bỏ qua bước chụp hình (R014: không áp dụng cho Thuốc) | High |

## 🚧 Blocked Coverage

- **R011 (Q-001)** — chờ API endpoint và schema cho multi-user realtime validation. Không thể test API contract.
- **R021 (Q-002)** — chờ bit list đầy đủ cho category/config. Không thể test toàn bộ bit flags.
- **R013, MSG-CPI-005 (Q-003)** — chờ verbatim message khi VAS chưa đánh giá QC. Không thể test message text.
- **R027, MSG-CPI-006 (Q-004)** — chờ verbatim confirm dialog Step 4 khi Lưu chưa đủ. Không thể test message text.
- **R033, R034, MSG-CPI-007, MSG-CPI-008 (Q-005)** — chờ verbatim 2 confirm dialog Step 5. TC-CPI-025/026 test behavior nhưng không verify message text.
- **R014 (Q-006)** — chờ danh sách category bổ sung thêm ngoài Sức khoẻ - Làm đẹp và Thuốc. Không thể test cho category chưa xác định.
- **R007 (Q-007)** — chờ định nghĩa "đã đánh giá chất lượng" (đầy đủ hay 1 phần, 1 SKU chưa đánh giá có khoá toàn VAS Cam không). Không thể test edge case Cam.
- **R029, R030 (Q-008)** — chờ flag required RFID trên master SKU. Không thể test SKU required RFID qua flag.
- **R030, R031 (Q-009)** — chờ xác nhận hệ thống tự detect Case 1 vs Case 2 hay user chọn manual. Không thể test detect mechanism.
- **R032 (Q-010)** — chờ xác nhận submit từng SP hay batch. Không thể test submit granularity.
- **R012 (Q-011)** — chờ xác nhận crash recovery state lưu local hay server-side, expire time. TC-CPI-011 test behavior nhưng không verify storage.
- **R018 (Q-012)** — chờ xác nhận hình + video bắt buộc cả 2 hay optional. Không thể test mandatory combination.
- **R023 (Q-013)** — chờ xác nhận Update 22-05-2025 Imei optional áp dụng cho cate nào. Không thể test scope cate.
- **R006 (Q-014)** — chờ xác nhận "Người dán đầu tiên" theo timestamp hay alphabet. Không thể test display rule.

## Regression Impact
- [[stub_receiving_po_vas]] — VAS sinh từ ASN, Serial/QRCode validation
- [[stub_receiving_po_app]] — Receiving PO flow upstream
- [[stub_qc_evaluation_result]] — QC required check cho VAS

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.1. 30 TC active, 14 blocked coverage item.
