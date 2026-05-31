---
spec: stub_receiving_po_vas
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [Functional, UI]
---

# Test Suite — VAS Listing, Detail, Cập nhật Serial/Imei/QRCode, Group UID, SPKPH

## Phạm vi
- Source spec: [[stub_receiving_po_vas]]
- Active requirements: 21 (R001-R012, R013-R015, R017-R022, R024-R027, R029-R034 — phần không bị block)
- Blocked: 13 R-ID chờ open questions (R025+MSG-VAS-007/Q-001, R016/Q-002, R023+ERR-VAS-006/Q-003, R018/Q-004, R002+R003/Q-005, R010/Q-006, R026+R027/Q-007, R028/Q-008, R031/Q-009, R030/Q-010, R034/Q-011, R029/Q-012, R009/Q-013)

**Ghi chú:** Luồng SPKPH nhận PO (R030) hiện tạm Off không sử dụng. TC cho SPKPH vẫn thiết kế dựa trên spec R031-R034 (action Cancel/Reject/Approve vẫn clear).

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-VAS-001 | VAS menu đặt tại Inbound / VAS | R001 | UI | User điều hướng | Menu Inbound / VAS hiển thị | High |
| TC-VAS-002 | Auto sinh VAS + auto Completed cho cate "Sức khoẻ - Làm đẹp" | R003 / AC-01 | Functional | SKU "Sức khoẻ - Làm đẹp" có serial; ASN chuyển Received | Hệ thống auto sinh VAS + auto Completed; UID không cần dán ID | High |
| TC-VAS-003 | Sinh VAS Open cho TSCĐ/CCDC/CCDC PB | R004 / AC-02 | Functional | SKU CCDC có Serial; ASN chuyển Received | Sinh 1 VAS status Open tương ứng ASN | High |
| TC-VAS-004 | UID status Received: không được picklisted | R005 / AC-03 | Functional | UID status Received | Hệ thống skip UID khi picklisted cho order/receipt/IT | High |
| TC-VAS-005 | UID chuyển Received → In-Bin sau khi dán ID | R005 / AC-04 | Functional | User xác nhận chụp hình/dán ID cho UID | UID chuyển Received → In-Bin | High |
| TC-VAS-006 | Cùng SKU 2 location → sinh 2 VAS riêng | R009 / AC-05 | Functional | SKUA nhận vào L1 (5 cái) và L2 (3 cái); ASN Received | Sinh 2 VAS riêng: 1 cho L1, 1 cho L2 | High |
| TC-VAS-007 | Filter Trạng thái multi-select, 4 values | R007 / AC-06 | UI | Filter Trạng thái = [Open, In-Progress] | Listing hiển thị VAS thuộc 2 status này | High |
| TC-VAS-008 | Hyperlink Mã ASN → ASN detail | R008 / AC-07 | UI | Click cell Mã ASN trong listing | Chuyển sang ASN detail | High |
| TC-VAS-009 | Button cập nhật chỉ show cho VAS Open/In-Progress | R011 / AC-08 | UI | VAS-A Open, VAS-B Completed | VAS-A có button; VAS-B không có | High |
| TC-VAS-010 | VAS detail: chỉ hiện SKU có yêu cầu serial | R013 / AC-09 | UI | VAS có 5 SKU; 3 SKU có serial | Danh sách hiển thị 3 SKU có serial | High |
| TC-VAS-011 | Auto chọn QRCode cho CCDC (wms_config & 131072 > 0) | R016-partial / AC-10 | Functional | CCDC có config flag; click cập nhật | Form auto check QRCode | High |
| TC-VAS-012 | Update 25-02-2025: Serial OFF — chỉ QRCode | R017 / AC-11 | Functional | Form mở cho CCDC | Serial bị tắt; chỉ QRCode available | High |
| TC-VAS-013 | Serial auto-gen pattern [1023][YYMMDD][6 số] | R018 / AC-12 | Functional | SKU không có Serial input | Hệ thống gen Serial vd `1023260531000001` (theo ngày 2026-05-31) | High |
| TC-VAS-014 | QRCode parser Object → lấy field Code | R020 / AC-13 | Functional | QRCode in `{"Code":"ABC123","Other":"xyz"}` | Lấy "ABC123" add vào danh sách | High |
| TC-VAS-015 | Auto focus QRCode → Serial khi cả 2 ON | R021 / AC-14 | UI | Cả 2 ON; scan QRCode pass | Focus chuyển sang ô Serial/Imei | High |
| TC-VAS-016 | Serial scan trùng danh sách → ERR-VAS-001 | R022 / AC-15 | Functional | Serial đã có trong danh sách | ERR-VAS-001 VN+EN | High |
| TC-VAS-017 | Serial scan trùng hệ thống → ERR-VAS-002 | R022 | Functional | Serial đã tồn tại hệ thống | ERR-VAS-002 VN+EN | High |
| TC-VAS-018 | BVA Serial: < 16 ký tự → ERR-VAS-003 | R022 / AC-16 | Functional | Serial 13 ký tự `1133378724121` | ERR-VAS-003 VN+EN | High |
| TC-VAS-019 | BVA Serial: đúng 16 ký tự (boundary) | R022 | Functional | Serial đúng 16 ký tự | Valid | High |
| TC-VAS-020 | QRCode không tồn tại HR → ERR-VAS-006 | R023 / AC-17 | Functional | QRCode không tồn tại hệ thống HR | ERR-VAS-006 VN+EN | High |
| TC-VAS-021 | QRCode trùng hệ thống → ERR-VAS-004 | R023 | Functional | QRCode đã tồn tại hệ thống | ERR-VAS-004 VN+EN | High |
| TC-VAS-022 | QRCode trùng danh sách → ERR-VAS-005 | R023 | Functional | QRCode đã có trong danh sách | ERR-VAS-005 VN+EN | High |
| TC-VAS-023 | Search gần đúng QRCode/Serial từ 3 ký tự | R024 / AC-18 | UI | Nhập search "102" | Cả 2 Serial có prefix "102" hiển thị | High |
| TC-VAS-024 | BVA search: nhập 2 ký tự chưa search | R024 | UI | Nhập 2 ký tự | Không suggest hoặc chưa filter | Medium |
| TC-VAS-025 | Complete button show khi đủ SL dán tất cả SKU | R025 / AC-19 | Functional | VAS 3 SKU; SKU 3 chưa đủ | Button không show. Khi SKU 3 đủ → button show | High |
| TC-VAS-026 | Update 16-09-2025: 10% group UID ceil | R026 / AC-20 | Functional | SKUA nhận 25 group UID | SL VAS cần đánh giá = ceil(25 × 10%) = 3 | High |
| TC-VAS-027 | BVA 10% ceil: 20 group UID → ceil(2) = 2 | R026, R027 | Functional | 20 group UID | SL đánh giá = 2 | Medium |
| TC-VAS-028 | Group UID 1 Failed → toàn VAS Failed | R028 / AC-21 | Functional | VAS 3 group UID; 2 Pass + 1 Failed | VAS ghi nhận Failed | High |
| TC-VAS-029 | VAS sinh trước scan → Group UID = trống | R029 / AC-22 | Functional | VAS mới sinh; user chưa scan group UID | Group UID = trống | High |
| TC-VAS-030 | SPKPH tách ASN | R031 / AC-23 | Functional | PO không đồng kiểm; 5 SKU thường + 2 SKU SPKPH | 2 ASN: ASN-1 (5 SKU Received + import stock); ASN-2 (2 SKU SPKPH Waiting approval, không import) | High |
| TC-VAS-031 | SPKPH action Cancel → UID về chưa nhận | R032 / AC-24 | Functional | ASN SPKPH Waiting approval; Quản lý Cancel | UID về chưa nhận; ASN Cancel | High |
| TC-VAS-032 | SPKPH action Reject → SP qua chưa nhận | R033 / AC-25 | Functional | Quản lý Reject | SP qua chưa nhận; user scan lại; ASN Reject | High |
| TC-VAS-033 | SPKPH action Approve → ASN Chờ NCC đến lấy | R034 / AC-26 | Functional | Quản lý Approve | ASN status Chờ NCC đến lấy | High |
| TC-VAS-034 | SPKPH timeout 7 ngày NCC chưa lấy → tiêu hủy | R034 / AC-27 | Functional | ASN Chờ NCC đến lấy từ 7 ngày trước | Trigger tiêu hủy theo quy trình | High |
| TC-VAS-035 | SP không cần serial → only chụp hình, skip QRCode/Serial | R019 | Functional | Category không ON QRCode/Serial | Chỉ cần chụp hình; bỏ qua scan QRCode/Serial | High |

## 🚧 Blocked Coverage

- **R025, MSG-VAS-007 (Q-001)** — chờ verbatim VN cho confirm dialog Complete. TC-VAS-025 test trigger nhưng không verify message VN.
- **R016 (Q-002)** — chờ bit list đầy đủ cho category. Không thể test toàn bộ bit flags.
- **R023, ERR-VAS-006 (Q-003)** — chờ xác nhận hệ thống HR (API endpoint, dependency). Không thể test error khi HR service down.
- **R018 (Q-004)** — chờ xác nhận prefix "1023" và scope đếm 6 số. Không thể test pattern đầy đủ.
- **R002, R003 (Q-005)** — chờ xác nhận scope "Sức khoẻ - Làm đẹp" (category đơn hay group). Không thể test sub-categories.
- **R010 (Q-006)** — chờ xác nhận edge case In-Progress: dán = 1 trên 1 SKU có chuyển In-Progress không. Không thể test edge case đầu tiên.
- **R026, R027 (Q-007)** — chờ xác nhận rounding rule (ceil vs khác). TC-VAS-026/027 giả định ceil theo ví dụ spec.
- **R028 (Q-008)** — chờ xác nhận "Failed" là VAS status hay field result riêng. Không thể test VAS status transition.
- **R031 (Q-009)** — chờ xác nhận nhiều SKU SPKPH cùng phiên là 1 ASN hay nhiều ASN. TC-VAS-030 giả định 1 ASN SPKPH.
- **R030 (Q-010)** — chờ xác nhận flow SPKPH Off (tạm Off theo spec). TC-VAS-030..034 test actions vẫn active theo spec.
- **R034 (Q-011)** — chờ doc quy trình tiêu hủy chi tiết và auto trigger hay manual. TC-VAS-034 test trigger behavior.
- **R029 (Q-012)** — chờ xác nhận Group UID được gắn vào VAS hiện hữu hay tạo VAS mới. Không thể test retroactive assignment.
- **R009 (Q-013)** — chờ xác nhận 1 SKU 1 location 2 phiên → 1 hay 2 VAS. Không thể test edge case phiên.

## Regression Impact
- [[stub_receiving_po_asn]] — ASN trigger sinh VAS
- [[stub_qc_uid_group]] — Group UID 10% quality control
- [[stub_receiving_po_confirm_paste_id]] — xác nhận dán ID

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.1. 35 TC active, 13 blocked coverage item.
