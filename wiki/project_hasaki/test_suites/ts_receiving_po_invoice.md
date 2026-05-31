---
spec: stub_receiving_po_invoice
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI, Functional]
---

# Test Suite — Thêm hoá đơn cho PO + Case 2 nhận PO Gift chung PO thường

## Phạm vi
- Source spec: [[stub_receiving_po_invoice]]
- Active requirements: 18 (R001, R003-R005, R006-R009, R010-R016, R018-R027 — phần không bị block)
- Blocked: 13 R-ID/Q chờ open questions (R002/Q-001, R008/Q-002, R006+R007/Q-003, ERR-INV-004/Q-004, R024/Q-005, R017+AC-17/Q-006, R014/Q-007, R021+AC-18/Q-008, MSG-INV-005..008/Q-009, R028/Q-010, R007/Q-011, R005/Q-012, R003+R004/Q-013)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-INV-001 | Hiển thị button "Thêm hoá đơn" sau khi nhận đủ SL | R001 / AC-01 | UI + Functional | PO nhận đủ SL; PO chưa có hoá đơn | Button "Thêm hoá đơn" hiển thị | High |
| TC-INV-002 | Tax code valid — 1-8 ký tự chữ+số | R003 / AC-03 | Functional | Nhập `0123456A` (7 ký tự) | Field valid, không báo lỗi | High |
| TC-INV-003 | Tax code invalid — vượt 8 ký tự | R003 / AC-04 | Functional | Nhập `01234567890` (>8 ký tự) | ERR-INV-002 hiển thị | High |
| TC-INV-004 | Tax code rỗng → bắt buộc | R003 / AC-05 | Functional | Không nhập Tax code; click "Thêm" | ERR-INV-001 dưới field Tax code | High |
| TC-INV-005 | BVA Tax code — min 1 ký tự valid | R003 | Functional | Nhập 1 ký tự "A" | Field valid | High |
| TC-INV-006 | BVA Tax code — max 8 ký tự valid | R003 | Functional | Nhập 8 ký tự "ABCD1234" | Field valid | High |
| TC-INV-007 | Serial valid — 1-8 ký tự chữ+số | R004 / AC-03 | Functional | Nhập `AA01` (4 ký tự) | Field valid | High |
| TC-INV-008 | Serial rỗng → bắt buộc | R004 / AC-05 | Functional | Không nhập Serial; click "Thêm" | ERR-INV-001 dưới field Serial | High |
| TC-INV-009 | Form → bắt buộc | R005 / AC-05 | Functional | Không nhập Form; click "Thêm" | ERR-INV-001 dưới field Form | High |
| TC-INV-010 | Total chênh ≤ 1000đ → valid | R006 / AC-06 | Functional | PO total = 1.500.000; nhập Total = 1.499.500 (chênh 500đ) | Field valid | High |
| TC-INV-011 | Total chênh > 1000đ → invalid | R006 / AC-07 | Functional | PO total = 1.500.000; nhập Total = 1.498.000 (chênh 2000đ) | ERR-INV-004 hiển thị | High |
| TC-INV-012 | BVA Total — chênh đúng 1000đ (boundary) | R006 | Functional | Chênh = 1000đ | Valid (chênh ≤ 1000đ) | High |
| TC-INV-013 | BVA Total — chênh 1001đ (boundary+1) | R006 | Functional | Chênh = 1001đ | Invalid — ERR-INV-004 | High |
| TC-INV-014 | Multi-invoice: tổng chênh > 1000đ → invalid | R007 / AC-08 | Functional | PO total = 1.500.000; HĐ1 = 800.000; HĐ2 = 600.000 (tổng = 1.400.000, chênh 100.000đ) | ERR-INV-004 | High |
| TC-INV-015 | Ngày default = ngày hiện tại | R008 | UI | Form mở lần đầu | Field Ngày prefill = today | High |
| TC-INV-016 | Ngày tương lai bị block | R008 / AC-09 | Functional | Chọn ngày tương lai (today+1) | Date picker không cho chọn hoặc báo lỗi | High |
| TC-INV-017 | Button "Đóng" → đóng popup không lưu | R009 | Functional | Click "Đóng" trong form | Popup đóng; không lưu dữ liệu đã nhập | High |
| TC-INV-018 | Hình ảnh — max 2 hình/hoá đơn | R012 / AC-10 | Functional | Upload 2 hình | Button "+" disable/không cho upload thêm | High |
| TC-INV-019 | BVA Hình ảnh — upload 1 hình | R012 | Functional | Upload 1 hình | Thành công; vẫn cho upload thêm 1 | Medium |
| TC-INV-020 | Thêm nhiều hoá đơn cho 1 PO | R013 / AC-11 | Functional | PO total 1500k; HĐ1 = 800k, HĐ2 = 700k (tổng = 1500k) | Cả 2 hoá đơn lưu cho PO; tổng = PO total; không lỗi | High |
| TC-INV-021 | PO gốc + PO Gift cùng yêu cầu invoice → chọn PO | R014 / AC-12 | Functional | PO_A và PO_AG đều yêu cầu invoice | Hệ thống yêu cầu user chọn PO nào trước khi add invoice | High |
| TC-INV-022 | Button "Hoàn thành PO" chỉ hiện khi đủ thông tin + hình | R015 / AC-13 | Functional | HĐ chưa có hình; Xem flow | Button "Hoàn thành PO" không hiện; sau upload hình → button hiện | High |
| TC-INV-023 | Case 2 nhận PO Gift chung — PO Gift 0 đồng bypass verify | R017 / AC-17 | Functional | PO_AG là Gift 0 đồng, chưa verify invoice | Bypass validation "chưa verify invoice"; hiển thị PO_AG thông tin | High |
| TC-INV-024 | Case 2 — cùng SKU ưu tiên SL cho PO Gift | R021 / AC-18 | Functional | PO_A SKU_X 5 cái; PO_AG SKU_X 2 cái (giá thấp hơn); scan 4 cái | PO_AG nhận 2 (đủ), PO_A nhận 2 | High |
| TC-INV-025 | Case 2 xem danh sách sản phẩm — chọn PO | R022 / AC-19 | UI + Functional | Case 2 nhận xong; User xem danh sách | Hệ thống yêu cầu user chọn PO_A hoặc PO_AG | High |
| TC-INV-026 | Step 4 PO đồng kiểm — label biên bản giao nhận | R023 / AC-20 | UI | PO có đồng kiểm = Yes | Label hiển thị "biên bản giao nhận hàng hoá" | High |
| TC-INV-027 | Step 4 PO không đồng kiểm — label biên bản bàn giao kiện | R023 / AC-21 | UI | PO không đồng kiểm | Label hiển thị "biên bản bàn giao kiện hàng" | High |
| TC-INV-028 | Update 20-11-2024: button "Kết thúc nhận hàng cả 2 PO" | R027 / AC-22 | UI | Case 2 (PO gốc + Gift) đủ hình ảnh | Button "Kết thúc nhận hàng cả 2 PO" hiển thị (không phải "Kết thúc nhận hàng") | High |
| TC-INV-029 | Hình chứng từ Step 4 — max 2 hình | R025 | Functional | Chụp 2 hình chứng từ | Không cho chụp thêm; button "Xoá hình" hiện để chụp lại | High |

## 🚧 Blocked Coverage

- **R002, AC-02 (Q-001)** — chờ verbatim VN cho 2 lưu ý dialog khi click "Thêm hoá đơn". Không thể test nội dung text của 2 dialog lưu ý.
- **R008, E5 (Q-002)** — chờ xác nhận UI block date picker hay hiển thị message khi chọn ngày tương lai. TC-INV-016 test behavior nhưng không verify message nếu có.
- **R006, R007 (Q-003)** — chờ xác nhận đơn vị "1.000 đồng" là VND fix hay configurable, và quy tắc cho PO ngoại tệ. Không thể test PO ngoại tệ.
- **ERR-INV-004 (Q-004)** — chờ xác nhận typo `tren` → `trên` trong message. TC-INV-011/013/014 test trigger nhưng không verify message text với typo.
- **R024 (Q-005)** — chờ xác nhận typo `kiếm` → `kiểm` ở raw L1647. Không thể test label chính xác.
- **R017, AC-17 (Q-006)** — chờ định nghĩa "PO Gift 0 đồng" (Total=0 hay flag riêng). TC-INV-023 giả định Total=0.
- **R014 (Q-007)** — chờ xác nhận timeout/reminder cho PO còn lại sau khi user chỉ add invoice 1 PO. Không thể test timeout behavior.
- **R021, AC-18 (Q-008)** — chờ xác nhận khi 2 SKU cùng giá (không phân biệt được PO Gift). Không thể test edge case cùng giá.
- **MSG-INV-005..008 (Q-009)** — chờ verbatim VN+EN cho 4 thông báo Case 2 scan PO Gift. Không thể test message text.
- **R028 (Q-010)** — chờ verbatim message xác nhận Update 20-11-2024 (raw bị cắt). Không thể test confirmation message này.
- **R007 (Q-011)** — chờ xác nhận timing block khi nhập thừa hoá đơn (khi nhập HĐ cuối hay khi Hoàn thành PO). Không thể test timing validation.
- **R005 (Q-012)** — chờ xác nhận format validation cho field Form (mẫu số). Không thể test Form validation.
- **R003, R004, ERR-INV-002, ERR-INV-003 (Q-013)** — chờ xác nhận "chữ + số" hay "chỉ chữ số" cho Tax code/Serial (raw-internal inconsistency). TC-INV-002/005/006/007 giả định alphanumeric nhưng không verify message khi nhập chữ cái.

## Regression Impact
- [[stub_receiving_po_gift]] — Case 2 nhận PO Gift chung PO thường
- [[stub_receiving_po_inbound_shipment]] — SL confirm, "PO chưa xác nhận hoá đơn"
- [[stub_receiving_po_asn]] — Taxcode mapping cho biên bản

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.2. 29 TC active, 13 blocked coverage item.
