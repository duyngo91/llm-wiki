---
spec: stub_receiving_po_fabric
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [Functional, UI]
---

# Test Suite — Nhận hàng Vải khai báo Group UID + Scan RFID mapping

## Phạm vi
- Source spec: [[stub_receiving_po_fabric]]
- Active requirements: 7 (R001, R002, R003, R005, R006, R007, R008, R009, R011, R012, R013 — phần không bị block)
- Blocked: 10 R-ID chờ open questions (R004+ERR-FAB-001/Q-001, R006+ERR-FAB-002/Q-002, R005+R011/Q-003, R007/Q-004, R010/Q-005, R013/Q-006+Q-007, R002+R009/Q-008, R001/Q-009, R012+R013/Q-010)

**Ghi chú:** R010 có Testable = ⚠️ (raw chỉ có heading S-32 không có content) → blocked.

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-FAB-001 | Trigger flow Vải khai báo Group UID — SKU đúng scope | R001 / AC-01 | Functional | SKU cate "Thời trang (NVL)", tên có "Vải", không quản lý UID; scan SKU | Hệ thống mở form scan nhận Vải Group UID | High |
| TC-FAB-002 | Không trigger flow Vải cho SKU ngoài scope | R001 / AC-02 | Functional | SKU cate "Mỹ phẩm", tên không có "Vải"; scan SKU | Form scan nhận bình thường (không phải form Vải) | High |
| TC-FAB-003 | SKU không quản lý lô/HSD — form 2 input Nhóm UID + Số lượng | R002 | UI | Scan SKU Vải không lô/HSD | Form hiện 2 field: Nhóm UID (optional) + Số lượng | High |
| TC-FAB-004 | Nhóm UID không bắt buộc — skip để nhận theo SL | R003 / AC-03 | Functional | Bỏ trống Nhóm UID; nhập SL = 5 Kg; click Xác nhận | Record ghi vào danh sách như SL bình thường | High |
| TC-FAB-005 | Nhóm UID có status New → valid, ghi nhận | R003 / AC-04 | Functional | Nhóm UID status New; nhập SL=10 Mét; Xác nhận | Record ghi vào danh sách | High |
| TC-FAB-006 | Số lượng tổng = sum tất cả cây/tấm vải | R007 / AC-06 | Functional | 3 lần scan: 40+35+25 Mét | Tổng SL nhận = 100 Mét | High |
| TC-FAB-007 | Mutex receive mode: chọn SL trước → khoá UID/RFID mode | R006 / AC-07 | Functional | Nhập SL=5; click "+"; sau đó cố scan Nhóm UID | Input Nhóm UID và SL ẩn đi; không cho thêm record mới | High |
| TC-FAB-008 | Không cho 1 SKU nhận cùng lúc 2 loại (UID + SL) | R006 | Functional | Đã nhận theo UID; cố nhập thêm theo SL | Block (behavior; message verbatim chờ Q-002) | High |
| TC-FAB-009 | Switch sang scan RFID mapping (Update 10-11-2025) | R005 / AC-08 | Functional | SKU không lô/HSD; user chuyển sang RFID mapping | Hệ thống chấp nhận RFID; nhập SL → record ghi | High |
| TC-FAB-010 | SKU có quản lý số lô + HSD — form có thêm input lô + HSD | R009 / AC-09 | UI | Scan SKU Vải có lô + HSD | Form bao gồm: Nhóm UID, Số lượng, số lô, HSD | High |
| TC-FAB-011 | Case 1 RFID chưa tồn tại: gen UID group mới + mapping | R012 / AC-10 | Functional | SKU quản lý UID group; scan RFID-NEW-001 (chưa tồn tại); submit | Hệ thống gen 1 UID group mới + mapping RFID-NEW-001 | High |
| TC-FAB-012 | Case 2 RFID đã tồn tại (Transfer company): suggest SL + gen UID mới | R013 / AC-11 | Functional | RFID-OLD-002 đã tồn tại từ Transfer company; scan | Suggest SL UID group cũ; user có thể edit; submit → gen UID group mới + mapping | High |

## 🚧 Blocked Coverage

- **R004, ERR-FAB-001, AC-05 (Q-001)** — chờ verbatim VN+EN message khi UID group status ≠ New. Không thể test message text; behavior blocked (TC-FAB-005 test pass case, failure case blocked).
- **R006, ERR-FAB-002, AC-07 (Q-002)** — chờ verbatim VN+EN message và hệ thống có hiện message hay chỉ ẩn UI ngầm. TC-FAB-007/008 test behavior nhưng không verify message.
- **R005 vs R011 (Q-003)** — chờ xác nhận phân biệt Update 10-11-2025 vs 10-12-2025 (cùng flow hay khác). TC-FAB-009/011/012 giả định 2 flow riêng.
- **R007 (Q-004)** — chờ công thức quy đổi Kg/Mét → SL và conversion factor. Không thể test formula chuyển đổi.
- **R010 (Q-005)** — raw S-32 chỉ có heading không có content. Không thể thiết kế TC.
- **R013 (Q-006)** — chờ định nghĩa Transfer company flow. Không thể test full Transfer company context.
- **R013 (Q-007)** — chờ xác nhận SL final khi edit khác SL suggest (theo edit hay suggest). Không thể test validation min/max.
- **R002, R009 (Q-008)** — chờ xác nhận flag quản lý lô/HSD trên master SKU. Không thể test flag detection.
- **R001 (Q-009)** — chờ xác nhận match "Vải": exact substring case-sensitive hay normalize. TC-FAB-001 giả định tên chứa "Vải" exact.
- **R012, R013 (Q-010)** — chờ xác nhận status UID group mới gen và reuse rules. Không thể test lifecycle UID mới.

## Regression Impact
- [[stub_receiving_po_app]] — flow scan nhận trên App là parent
- [[stub_receiving_po_packing_list]] — case nhận PO Vải theo packing list

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.1. 12 TC active, 10 blocked coverage item.
