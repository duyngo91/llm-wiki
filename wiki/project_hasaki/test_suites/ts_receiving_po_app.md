---
spec: stub_receiving_po_app
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [Functional, UI]
---

# Test Suite — Receiving PO trên App — App Confirm Unsuitable + Flow scan PO (Step 1-5)

## Phạm vi
- Source spec: [[stub_receiving_po_app]]
- Active requirements: 21 (R001-R022, R025-R033 — phần không bị block)
- Blocked: 12 R-ID chờ open questions (R009/Q-001, R017/Q-002, R024/Q-003, R026+ERR-APP-004/Q-004, R010/Q-005, R011+R013/Q-006, R022/Q-007, R027/Q-008, R028+R029/Q-009, R033/Q-010, R032/Q-011, R003/Q-012)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-APP-001 | Login App + vào Receiving PO | R005 / AC-01 | Functional | User login App hợp lệ; chọn Receiving PO | Màn hình scan PO mở; hướng dẫn hiển thị lần đầu | High |
| TC-APP-002 | Hướng dẫn mặc định show khi vào lần đầu | R006 | UI | Vào Receiving PO lần đầu | Hướng dẫn hiển thị | High |
| TC-APP-003 | PO không yêu cầu VAT → bypass check verify invoice | R007 / AC-02 | Functional | Scan PO không yêu cầu VAT | Bypass check verify invoice; cho nhận | High |
| TC-APP-004 | PO yêu cầu VAT chưa verify → block | R007 / AC-03 | Functional | Scan PO VAT yêu cầu, invoice chưa verify | Thông báo block | High |
| TC-APP-005 | PO không thuộc kho → block | R008 / AC-04 | Functional | User kho A; scan PO kho B | Thông báo block | High |
| TC-APP-006 | PO đã received → block | R008 / AC-05 | Functional | Scan PO đã received | Thông báo block | High |
| TC-APP-007 | PO hợp lệ → tạo ASN status Receiving (chưa gọi API Inside) | R009 / AC-06 | Functional | Scan PO hợp lệ | Show info PO; tạo ASN Receiving; chưa gọi API update Inside | High |
| TC-APP-008 | Update 05-01-2026: SKU qty < 100k → block default | R010 / AC-07 | Functional | PO có SKU qty = 50.000 | Block default, không cho nhận | High |
| TC-APP-009 | Update 05-01-2026: force qua filter + nút force | R010, R011, R012, R013 / AC-08 | Functional | PO SKU qty < 100k; bật filter; click force | Confirm dialog MSG-APP-010 VN+EN → xác nhận → cho nhận | High |
| TC-APP-010 | Chọn "Đồng kiểm" + shop quản lý location → Step 5 | R014 / AC-09 | Functional | Shop quản lý location; chọn Đồng kiểm | Bypass Step 4 camera → chuyển Step 5 scan vị trí | High |
| TC-APP-011 | Chọn "Đồng kiểm" + shop không quản lý location → bước scan SP | R014 / AC-10 | Functional | Shop không quản lý location; chọn Đồng kiểm | Bypass Step 4 + 5 → bước scan SP trực tiếp | High |
| TC-APP-012 | Button "Đóng" Step 3 → quay về scan PO | R015 | Functional | Click "Đóng" tại popup chọn loại nhận | Đóng popup; quay về màn hình scan PO | High |
| TC-APP-013 | Update 18-02-2025: Required camera = No → bypass camera | R018 / AC-11 | Functional | Config Required camera = No; chọn Không đồng kiểm | Bypass Step 4 scan camera | High |
| TC-APP-014 | Update 18-02-2025: Required camera = Yes → phải scan | R018 / AC-12 | Functional | Config Required camera = Yes; chọn Không đồng kiểm | User phải scan camera ở Step 4 | High |
| TC-APP-015 | Mã camera không hợp lệ → ERR-APP-001 | R019 / AC-13 | Functional | Scan mã camera không thuộc kho | ERR-APP-001 VN+EN | High |
| TC-APP-016 | PO zone: bắt buộc location Di động; vị trí không phải Di động → ERR-APP-003 | R023 / AC-14 | Functional | PO zone; scan vị trí F2-AP-01-01-01-01 không Di động | ERR-APP-003 VN+EN | High |
| TC-APP-017 | PO thường: không vào bin Di động → ERR-APP-004 (behavior) | R026 / AC-15 | Functional | PO thường; scan vị trí Di động F0-A1-PL-50-01-01 | ERR-APP-004 hiển thị (message text chờ Q-004 clarify) | High |
| TC-APP-018 | Mã giỏ trạng thái không hợp lệ → ERR-APP-006 | R027 / AC-16 | Functional | Giỏ 404005 status Locked | ERR-APP-006 VN+EN | High |
| TC-APP-019 | Update 27-02-2024: Bin Di động cùng stock → bình thường | R029 / AC-17 | Functional | Bin A thuộc Shop 170 QL1A; PO Shop 170 QL1A | Cho nhận bình thường | High |
| TC-APP-020 | Update 27-02-2024: Bin Di động khác stock có UID → block | R029 / AC-18 | Functional | Bin A Shop 170 QL1A đang có UID; PO WH 170 QL1A | Báo lỗi, không cho nhận | High |
| TC-APP-021 | Update 27-02-2024: Bin Di động khác stock không UID → switch stock_id | R029 / AC-19 | Functional | Bin A Shop 170 QL1A hết UID; PO WH 170 QL1A | Cho nhận; stock_id Bin A update → WH 170 QL1A | High |
| TC-APP-022 | SKU không tồn tại trong PO → ERR-APP-007 | R030 / AC-20 | Functional | Scan SKU 100540031 không có trong PO | ERR-APP-007 VN+EN | High |
| TC-APP-023 | SL SKU vượt SL confirm → ERR-APP-008 | R031 / AC-21 | Functional | PO confirm SKU SL=10; scan thứ 11 | ERR-APP-008 VN+EN | High |
| TC-APP-024 | SKU yêu cầu HSD → form nhập date với SL prefill | R032 / AC-22 | UI + Functional | Scan SKU required date | Form HSD mở; SL prefill từ scan; cho chỉnh sửa | High |
| TC-APP-025 | HSD < yêu cầu PO → ERR-APP-009 | R033 / AC-23 | Functional | PO yêu cầu HSD ≥ 9 tháng; nhập 6 tháng | ERR-APP-009 VN+EN | High |
| TC-APP-026 | App Confirm Unsuitable — danh sách ASN SPKPH theo kho | R002 / AC-24 | Functional | User vào Confirm Unsuitable; chọn kho A | Danh sách ASN SPKPH status "Chờ NCC đến lấy" của kho A | High |
| TC-APP-027 | Confirm Unsuitable — form với Mã PO, Mã ASN, SKU, Qty | R003 | UI | Chọn phiên SPKPH | Form hiển thị Mã PO, Mã ASN, SKU, Qty, danh sách SP, Chọn phương án, Ghi chú, Hình/video | High |
| TC-APP-028 | Confirm Unsuitable — chọn "Đã trả NCC" → Hoàn thành | R004 / AC-25 | Functional | Chọn phương án + ghi chú + hình/video; click "Hoàn thành và xác nhận" | ASN status cập nhật theo phương án | High |
| TC-APP-029 | Decision Table: Không đồng kiểm + Required camera=Yes + shop quản lý location → Step 4 → Step 5 | R014, R018, R021 | Functional | Không đồng kiểm; Required camera Yes; shop quản lý location | Phải scan camera Step 4; sau đó scan vị trí Step 5 | High |
| TC-APP-030 | BVA: SL = SL confirm (boundary) → pass | R031 | Functional | PO confirm SKU SL=10; scan thứ 10 | Pass | High |
| TC-APP-031 | Vị trí không thuộc kho/không tồn tại (PO zone) → ERR-APP-002 | R023 | Functional | PO zone; scan vị trí không thuộc kho | ERR-APP-002 VN+EN | High |
| TC-APP-032 | Mã giỏ không thuộc kho/không tồn tại → ERR-APP-005 | R027 | Functional | Mã giỏ không thuộc kho | ERR-APP-005 VN+EN | High |

## 🚧 Blocked Coverage

- **R009 (Q-001)** — chờ xác nhận khi nào API update Inside Receiving được gọi. TC-APP-007 test "chưa gọi" nhưng không test thời điểm gọi.
- **R017 (Q-002)** — chờ xác nhận scope Required camera config (chỉ Không đồng kiểm hay cả Đồng kiểm). TC-APP-013/014 test Không đồng kiểm chỉ.
- **R024 (Q-003)** — chờ verbatim message khi PO zone scan mã giỏ. Không thể test message text.
- **R026, ERR-APP-004 (Q-004)** — chờ xác nhận VN vs EN message inconsistency (mã vị trí khác nhau). TC-APP-017 test behavior nhưng không verify message text chính xác.
- **R010 (Q-005)** — chờ xác nhận đơn vị "100.000" (units hay VND). TC-APP-008/009 giả định là số lượng đơn vị.
- **R011, R013 (Q-006)** — chờ xác nhận filter location và quyền sử dụng. Không thể test role-based access.
- **R022 (Q-007)** — chờ định nghĩa PO zone (flag hay rule per kho). Không thể test PO zone detect.
- **R027 (Q-008)** — chờ enum status mã giỏ đầy đủ ngoài Available và Transfer Bin. Không thể test trạng thái khác.
- **R028, R029 (Q-009)** — chờ xác nhận semantics stock_id. TC-APP-019/020/021 test behavior.
- **R033 (Q-010)** — chờ xác nhận "9 tháng" configurable per PO/SKU hay default. TC-APP-025 giả định default 9 tháng.
- **R032 (Q-011)** — chờ xác nhận re-validate SL khi chỉnh sửa. Không thể test SL=0 boundary.
- **R003 (Q-012)** — chờ xác nhận "Số lượng SPKPH" vs "Số lượng" là 2 field khác hay alias. Không thể test field disambiguation.

## Regression Impact
- [[stub_receiving_po_vas]] — SPKPH ASN status "Chờ NCC đến lấy"
- [[stub_receiving_po_asn]] — ASN sinh ra từ scan PO
- [[stub_receiving_po_date_rules]] — HSD rules liên quan

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.1. 32 TC active, 12 blocked coverage item.
