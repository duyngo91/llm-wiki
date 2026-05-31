---
spec: stub_receiving_po_date_rules
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [Functional, UI]
---

# Test Suite — Rules HSD tối thiểu + combo SKU + RFID + Khai báo thiếu + Kết thúc PO

## Phạm vi
- Source spec: [[stub_receiving_po_date_rules]]
- Active requirements: 24 (R002, R003, R004, R006, R007, R008, R009, R011, R012, R013, R014, R015, R016, R017, R018, R019, R020, R021, R022, R023, R024, R025, R026, R027, R028, R029, R032, R033, R034, R035, R036, R037, R038, R039, R040 — phần không bị block)
- Blocked: 16 R-ID chờ open questions

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-DTR-001 | HSD tối thiểu: tính đúng theo % × Shelf Life (không làm tròn) | R002 / AC-01 | Functional | % Allowed=80%; Shelf Life=24 tháng; Ngày nhận 2026-05-30 | HSD tối thiểu = 19.2 tháng cộng 2026-05-30 ≈ 2027-12-30 (không làm tròn 19.2) | High |
| TC-DTR-002 | HSD edge case: trùng tháng HSD tối thiểu → pass | R003 / AC-01 | Functional | HSD tối thiểu tháng 2027-12; nhập HSD = 2027-12-31 (cùng tháng) | Pass — HSD tính ngày cuối tháng | High |
| TC-DTR-003 | HSD < HSD tối thiểu → ERR-DTR-001 | R002 / AC-02 | Functional | HSD tối thiểu = 2027-12-30; nhập 2027-08-15 | ERR-DTR-001 VN: `Hạn sử dụng nhỏ hơn yêu cầu được phép nhận hàng của PO (HSD tối thiểu [Ngày hệ thống tính toán])` | High |
| TC-DTR-004 | HSD > vòng đời SP (24 tháng) → ERR-DTR-002 | R004 / AC-03 | Functional | Vòng đời = 24 tháng; nhập HSD = 2030-12-31 | ERR-DTR-002 VN+EN | High |
| TC-DTR-005 | PO tester HSD ≥ 3 tháng → pass | R006 / AC-04 | Functional | PO type tester; SKU HSD còn 3 tháng | Pass | High |
| TC-DTR-006 | BVA PO tester: HSD đúng 3 tháng (boundary) | R006 | Functional | PO tester; HSD = 3 tháng | Pass | High |
| TC-DTR-007 | SL SKU > SL confirm PO → ERR-DTR-005 | R007 / AC-07-ref | Functional | SKU confirm=10; scan SL=11 | ERR-DTR-005 VN+EN | High |
| TC-DTR-008 | SKU có số lô: popup nhập HSD + lô; prefill SL từ scan | R008 | UI + Functional | Scan SKU yêu cầu số lô + HSD | Popup mở; SL prefill từ scan nhưng cho sửa; field số lô + HSD | High |
| TC-DTR-009 | Số lô trùng cùng SKU → ERR-DTR-003 | R008 / AC-05 | Functional | SKU đã có lô LOT-001; nhập LOT-001 lần 2 | ERR-DTR-003 VN+EN | High |
| TC-DTR-010 | CCDC Serial trùng cùng SKU → ERR-DTR-004 | R009 / AC-06 | Functional | CCDC đã có Serial SR-001; nhập SR-001 | ERR-DTR-004 VN (typo EN `prodcut` chờ Q-002) | High |
| TC-DTR-011 | Bypass nhập Serial/Imei CCDC (24-10-2024) | R011 / AC-08 | Functional | SKU CCDC yêu cầu Serial; phase bypass | Chỉ nhập SL + date; không yêu cầu Serial | High |
| TC-DTR-012 | Button "Thay đổi vị trí nhận hàng" chỉ hiện Shop 170 QL1A | R012 / AC-09 | UI | User ở Shop 170 QL1A | Button hiện; click → quay về scan vị trí | High |
| TC-DTR-013 | 1 PO chỉ nhận vào 1 giỏ duy nhất | R013 / AC-10 | Functional | PO đã nhận vào giỏ G1; cố nhận tiếp vào G2 | Block | High |
| TC-DTR-014 | Update 30-05-2025: combo 1 lẻ required date → popup theo SKU lẻ | R014 / AC-11 | Functional | Combo required date; chỉ SP-1 lẻ required date | Popup nhập theo SP-1 | High |
| TC-DTR-015 | Update 04-06-2025: combo không required + lẻ required → popup nhập lẻ | R015 / AC-12 | Functional | Combo không required; SP-1 lẻ required | Popup nhập date cho SP-1 | High |
| TC-DTR-016 | Update 04-06-2025: combo required + lẻ không required → popup nhập combo | R015 / AC-13 | Functional | Combo required; lẻ không required | Popup nhập date cho combo | High |
| TC-DTR-017 | Step 1.1: RFID Thời trang + Synctives → scan RFID khi nhận, auto VAS | R016 / AC-14 | Functional | SKU Thời trang + Brand Synctives + required RFID | Scan RFID khi nhận; auto VAS sinh ra | High |
| TC-DTR-018 | Step 1.2: Xóa scan SKU có lô/HSD → xóa hết SL phiên | R017 / AC-15 | Functional | User nhập sai lô LOT-001; click Xóa → confirm EN → Yes | Xóa tất cả SL của SKU đã scan trong phiên hiện tại | High |
| TC-DTR-019 | Step 1.2: Xóa Serial riêng lẻ | R018 / AC-16 | Functional | Serial 2UA49P120 đã scan; user chọn xóa Serial | Xóa Serial đó; SL SKU khác không bị ảnh hưởng | High |
| TC-DTR-020 | Step 2: Danh sách 1 PO không cần chọn PO | R019 / AC-17 | UI | Flow chỉ có 1 PO | Hiển thị thẳng SP của PO, không yêu cầu chọn PO | High |
| TC-DTR-021 | Step 2: 2 tab Đã nhận đủ và Chưa nhận đủ | R019 | UI | PO có SKU nhận đủ và chưa đủ | Hiển thị 2 tab riêng biệt | High |
| TC-DTR-022 | Step 2.2: Số lượng thiếu auto prefill SL chưa nhận | R022 / AC-18 | UI | SKU nhận 3/10 | Form khai báo: Số lượng thiếu prefill = 7 | High |
| TC-DTR-023 | Step 2.2: Số lượng thiếu trống → MSG-DTR-007 | R022 / AC-19 | Functional | Bỏ trống Số lượng thiếu; submit | MSG-DTR-007 VN: `Vui lòng nhập số lượng thiếu` | High |
| TC-DTR-024 | Step 2.2: Lý do = "Giao thiếu hàng" → hiện "NCC giao bù" | R023 / AC-20 | UI + Functional | Chọn "Giao thiếu hàng" | Field "NCC giao bù" Yes/No hiện ra | High |
| TC-DTR-025 | Step 2.2: Lý do = "Sản phẩm không phù hợp" → Tình trạng + HSD | R023 / AC-21 | UI + Functional | Chọn "Sản phẩm không phù hợp" | Field Tình trạng ∈ {Hư hỏng, Cận date, Hết date, Khác} và HSD YYYY-MM hiện ra | High |
| TC-DTR-026 | SPKPH bắt buộc chụp hình; thiếu hàng không cần | R024 / AC-22 | Functional | Case SPKPH và case thiếu hàng | SPKPH: bắt buộc hình. Thiếu hàng: không yêu cầu | High |
| TC-DTR-027 | Khai báo thành công → button xanh lá | R024 / AC-23 | UI | User khai báo đầy đủ; submit | Button khai báo chuyển màu xanh lá | High |
| TC-DTR-028 | Step 2.3: Khai báo tất cả SP thiếu cùng lúc | R026 / AC-24 | Functional | PO 5 SKU chưa đủ; click "Khai báo thiếu cho tất cả" → Yes | Tất cả 5 SKU có khai báo reason=Giao thiếu + NCC giao bù=Có | High |
| TC-DTR-029 | Step 2.4: Xóa SP đã scan → xóa tất cả SL + khai báo thiếu | R028 / AC-25 | Functional | SKU đã scan 5/10 và có khai báo thiếu; xóa SP | Xóa hết 5 SL + khai báo thiếu liên quan | High |
| TC-DTR-030 | Step 3: API update PO Inside → Receiving khi kết thúc nhận | R029 / AC-26 | Functional | Nhận đủ SL; click "Kết thúc nhận hàng" | Hệ thống gọi API update PO Inside thành Receiving | High |
| TC-DTR-031 | API payload check_issue: hàng không phù hợp | R030 / AC-27 | Functional | PO có 3 SP không phù hợp; hoàn thành | API gửi payload với `check_issue:1, issue:{unsuitable:{qty:3, media:[]}}` | High |
| TC-DTR-032 | API payload check_issue: NCC không giao lại | R031 / AC-28 | Functional | Thiếu hàng NCC không giao lại; hoàn thành | API gửi payload với `check_issue:1, issue:{note:"..."}` | High |
| TC-DTR-033 | Step 4: PO đồng kiểm → biên bản giao nhận hàng hoá | R033 / AC-29 | UI | PO đồng kiểm | Label "biên bản giao nhận hàng hoá" | High |
| TC-DTR-034 | Step 4: PO không đồng kiểm → biên bản bàn giao kiện hàng | R033 / AC-30 | UI | PO không đồng kiểm | Label "biên bản bàn giao kiện hàng" | High |
| TC-DTR-035 | Step 4: max 2 hình chứng từ | R033 / AC-31 | Functional | Chụp 2 hình; cố chụp thêm | Block | High |
| TC-DTR-036 | Step 5: Button "Hoàn thành PO" show khi đủ điều kiện | R034 / AC-32 | Functional | SL đủ + biên bản đã add + hoá đơn đầy đủ | Button "Hoàn thành PO" show | High |
| TC-DTR-037 | Step 5: chưa add biên bản → không show button hoặc block | R036 / AC-33 | Functional | SL đủ nhưng chưa add biên bản; cố hoàn thành | Button không show; nếu trigger → MSG-DTR-011 EN: `Please update the delivery document image.` | High |
| TC-DTR-038 | Step 5: Confirm "Hoàn thành PO" → 4 action | R037 / AC-34 | Functional | Confirm Yes cho `Do you want to confirm completion of PO...?` | (a) PO status Received; (b) ASN Received; (c) tồn kho update; (d) sync Inside | High |
| TC-DTR-039 | Step 5: nhận thiếu → PO config Waiting Adj Invoice | R038 / AC-35 | Functional | Nhận thiếu; NCC không giao bù; Hoàn thành | PO config = Waiting Adj Invoice | High |
| TC-DTR-040 | Step 5: SP không phù hợp → PO config Receiving Issue | R038 / AC-36 | Functional | Có SP không phù hợp; Hoàn thành | PO config = Receiving Issue | High |
| TC-DTR-041 | 24-10-2024: SPKPH import stock + UID Damaged | R039 / AC-37 | Functional | PO có SPKPH; Hoàn thành PO | Vẫn import stock; UID product status = Damaged | High |
| TC-DTR-042 | Hoàn thành phiên nhận hàng (không phải Hoàn thành PO) | R040 / AC-39 | Functional | SL chưa đủ + SKU có NCC giao bù=Yes; click "Hoàn thành phiên" → confirm | ASN status Received; tồn kho update theo phiên | High |

## 🚧 Blocked Coverage

- **R001, ERR-DTR-001 (Q-017)** — chờ confirm raw typo "tối thiếu" → "tối thiểu". Không thể test message text chính xác.
- **R029, R030, R031, R037 (Q-001)** — chờ API endpoint cụ thể và schema. TC-DTR-030/031/032/038 test behavior nhưng không verify endpoint/schema.
- **R009, ERR-DTR-004 (Q-002)** — chờ xác nhận typo EN "prodcut" → "product". Không thể test message EN.
- **R010, MSG-DTR-006 (Q-003)** — chờ verbatim VN+EN message CCDC scan SL > 1. Không thể test message text.
- **R033 (Q-004)** — chờ xác nhận typo "kiếm" → "kiểm". Không thể test label chính xác.
- **ERR-DTR-001, MSG-DTR-007, MSG-DTR-011 (Q-005)** — chờ verbatim EN cho 3 message. TC chỉ test VN.
- **R004 (Q-006)** — chờ xác nhận 24 tháng là default hay configurable per SKU. Không thể test các SKU có vòng đời khác 24.
- **R005 (Q-007)** — chờ xác nhận icon ghi chú PO đặt ở màn hình nào. Không thể test placement icon.
- **R006 (Q-008)** — chờ xác nhận flag PO tester. Không thể test detect tester.
- **R012, R013 (Q-009)** — chờ xác nhận rollout Shop 170 QL1A scope. TC-DTR-012/013 dựa trên 2 kho cụ thể.
- **R014, R015 (Q-010)** — chờ behavior khi combo lỗi data (block hay cảnh báo). Không thể test edge case lỗi data.
- **R016 (Q-011)** — chờ verify spelling chính xác "Synctive" vs "Synctives". TC-DTR-017 test behavior.
- **R023 (Q-012, Q-013)** — chờ xác nhận "Tình trạng Khác" là text tự do hay list, và HSD YYYY-MM scope. Không thể test "Khác" input.
- **R035 (Q-014)** — chờ xác nhận edge case 1 SKU NCC giao bù=Yes trong group. Không thể test mixed NCC giao bù.
- **R038 (Q-015)** — chờ xác nhận PO config có thể combine cả 2 values. Không thể test combined case.
- **R039 (Q-016)** — chờ xác nhận Damaged là UID-level status hay SKU-level. Không thể test recovery flow.

## Regression Impact
- [[stub_receiving_po_app]] — Step 1-5 flow upstream
- [[stub_receiving_po_inbound_shipment]] — PO/ASN status changes
- [[stub_receiving_po_invoice]] — Step 5 hoá đơn condition

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.2. 42 TC active, 16 blocked coverage item.
