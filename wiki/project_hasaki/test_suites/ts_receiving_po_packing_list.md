---
spec: stub_receiving_po_packing_list
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [Functional, UI]
---

# Test Suite — Import Packing list PO + Nhận hàng theo Packing list

## Phạm vi
- Source spec: [[stub_receiving_po_packing_list]]
- Active requirements: 18 (R001-R012, R013-R018, R026-R031 — phần không bị block; R019-R025 Pending 12-05-2026)
- Blocked: 17 R-ID chờ open questions + R019-R025 Pending

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-PKL-001 | Import packing list valid 9 rules → auto Approved | R001, R006 / AC-01 | Functional | File valid 9 rules; ±5% pass | Inbound table Packing list PO = Approved | High |
| TC-PKL-002 | Re-import trùng PO+SKU+Roll+Batch → update SL | R001 / AC-03 | Functional | File có dòng trùng key nhưng Qty khác | Qty update theo file mới | High |
| TC-PKL-003 | Validation PO code rỗng → ERR-PKL-001 | R002 / AC-04 | Functional | Dòng 5 PO code trống | ERR-PKL-001 VN+EN với "Dòng 5" | High |
| TC-PKL-004 | Validation PO code không tồn tại → ERR-PKL-002 | R002 | Functional | PO code nhập không tồn tại hệ thống | ERR-PKL-002 VN+EN | High |
| TC-PKL-005 | Validation SKU rỗng → ERR-PKL-003 | R003 | Functional | SKU để trống | ERR-PKL-003 VN+EN | High |
| TC-PKL-006 | Validation SKU không tồn tại hệ thống → ERR-PKL-004 | R003 | Functional | SKU không tồn tại | ERR-PKL-004 VN+EN | High |
| TC-PKL-007 | Validation Roll code rỗng → ERR-PKL-006 | R004 | Functional | Roll code trống | ERR-PKL-006 VN+EN | High |
| TC-PKL-008 | Validation Batch code rỗng → ERR-PKL-009 | R004 | Functional | Batch code trống | ERR-PKL-009 VN+EN | High |
| TC-PKL-009 | Validation SL yêu cầu trống → ERR-PKL-012 | R004 | Functional | Số lượng yêu cầu trống | ERR-PKL-012 (cannot be empty) VN+EN | High |
| TC-PKL-010 | Validation SL yêu cầu âm → ERR-PKL-012 | R004 | Functional | SL = -5 | ERR-PKL-012 (invalid) VN+EN | High |
| TC-PKL-011 | Validation dữ liệu trùng dòng trong file → ERR-PKL-012 | R004 | Functional | 2 dòng giống hệt trong file | ERR-PKL-012 (already exists) VN+EN | High |
| TC-PKL-012 | Edit/Xóa packing list chỉ cho PO khác Received | R005 / AC-05 | Functional | PO-B status Received; cố edit Qty | UI disable/không cho | High |
| TC-PKL-013 | Import > ±5% → MSG-PKL-010 confirm + status Waiting Approval | R006 / AC-02 | Functional | Qty packing list > ±5% Qty PO | MSG-PKL-010 hiện; Operations click "Xác nhận Import" → Waiting for Approval | High |
| TC-PKL-014 | BOD approve packing list → Approved | R009 / AC-06 | Functional | PO Waiting Approval; BOD click Approve → confirm MSG-PKL-011 → Yes | Status Approved | High |
| TC-PKL-015 | MSG-PKL-011 message VN+EN | R009 | UI | Click Approve | VN: `Bạn có chắc chắn muốn duyệt...?` / EN: `Do you want to approve...?` | High |
| TC-PKL-016 | Re-import sau Approved + > ±5% → Waiting Approval | R010 / AC-07 | Functional | Status Approved; re-import file > ±5% | Status chuyển về Waiting for Approval | High |
| TC-PKL-017 | Update SL sau Approved → giữ Approved | R010 / AC-08 | Functional | Status Approved; user edit Qty | Status giữ Approved | High |
| TC-PKL-018 | App scan PO Waiting Approve → ERR-PKL-007 block | R012 / AC-09 | Functional | PO packing list Waiting Approve; scan trên App | ERR-PKL-007 VN: `PO chưa được duyệt Packing list...` | High |
| TC-PKL-019 | App scan PO chưa import packing list → ERR-PKL-008 block | R012 / AC-10 | Functional | PO vải chưa import packing list; scan | ERR-PKL-008 VN: `PO chưa import Packing list...` | High |
| TC-PKL-020 | App scan PO Approved không data → pass | R012 / AC-11 | Functional | PO Approved không data; scan | Pass cho nhận | High |
| TC-PKL-021 | SKU vải lẻ: suggest mã cuộn khi nhập số lô | R013 / AC-12 | UI + Functional | Nhập số lô LOT-001 khi packing list đã có Roll-A1, Roll-A2 | Danh sách suggest {Roll-A1, Roll-A2} hiện ra | High |
| TC-PKL-022 | SKU vải lẻ: SL ghi nhận = SL thực nhận × hệ số | R014 / AC-13 | Functional | SL thực nhận = 48 kg; hệ số x2 | SL ghi nhận = 96 pcs | High |
| TC-PKL-023 | SKU vải lẻ: SL thực nhận > SL packing list → ghi theo packing list | R015 | Functional | SL thực nhận = 55 kg; SL packing list = 50 kg | Ghi nhận = 50 kg (theo packing list); "Nhận lệch" = +5 | High |
| TC-PKL-024 | SKU vải lẻ: SL thực nhận ≤ SL packing list → ghi theo thực nhận | R015 | Functional | Thực nhận = 48 kg; packing list = 50 kg | Ghi nhận = 48 kg; Nhận lệch = -2 | High |
| TC-PKL-025 | SKU vải combo: nhập SL thập phân | R016 / AC-14 | Functional | Nhập SL = 4.5 | Pass | High |
| TC-PKL-026 | SKU vải combo: total UID phải là số nguyên dương | R017 / AC-15 | Functional | Tổng SL khai báo UID = 4.5 | Block | High |
| TC-PKL-027 | SKU vải combo: không nhân hệ số quy đổi | R016 | Functional | Nhận combo; SL = 4 | Ghi nhận đúng 4 (không nhân hệ số) | High |
| TC-PKL-028 | Update 02-04-2026: Trừ lõi normal = SL − Trừ lõi | R018 / AC-16 | Functional | SL = 50; Trừ lõi = 0.5 | Ghi nhận = 49.5 | High |
| TC-PKL-029 | Update 02-04-2026: Trừ lõi có hệ số = SL × hệ số − Trừ lõi | R018 / AC-17 | Functional | SL=50; hệ số=2; Trừ lõi=0.5 | Ghi nhận = 50×2−0.5 = 99.5 | High |
| TC-PKL-030 | Update 20-04-2026: nhận dư → Qty per ADJ + sinh UID mới | R028 / AC-22 | Functional | PO 105 mét; packing list 106.15; thực nhận 106.60 | UID group ghi 106.15; dư 0.45 → ADJ + UID mới cùng UID group | High |
| TC-PKL-031 | Update 20-04-2026: cảnh báo > 10% cây vải | R029 / AC-23 | Functional | Cây vải packing list = 10m; thực nhận = 12m (>10%) | MSG-PKL-013 hiện confirm | High |
| TC-PKL-032 | MSG-PKL-013 "Kiểm tra lại" → tắt, giữ màn hình | R029 / AC-24 | Functional | Click "Kiểm tra lại" | Dialog tắt; màn hình khai báo giữ nguyên | High |
| TC-PKL-033 | MSG-PKL-013 "Xác nhận" → ghi nhận | R029 / AC-25 | Functional | Click "Xác nhận" | Ghi nhận vào danh sách | High |
| TC-PKL-034 | Push Inside: total < PO → yêu cầu điều chỉnh hoá đơn | R031 / AC-26 | Functional | Total thực nhận 100 mét; PO 105 mét | Push 100 mét + yêu cầu điều chỉnh hoá đơn | High |
| TC-PKL-035 | Push Inside: total > PO → push theo PO + ADJ | R031 / AC-27 | Functional | Total 106.5 mét; PO 105 mét | Push 105 mét theo PO; ADJ cho 1.5 mét dư | High |
| TC-PKL-036 | ASN detail: Qty received + Qty per ADJ | R026 / AC-28 | UI | ASN có nhận dư | Qty received = SL theo PO; Qty per ADJ = SL dư | High |
| TC-PKL-037 | Update 29-01-2026: SKU bổ sung sau PO Receiving → auto Approved | R007 / AC-30 | Functional | PO đã chuyển Receiving; import bổ sung | SKU bổ sung auto Approved | High |
| TC-PKL-038 | Inbound filter "Packing list PO" có 2 values | R011 | UI | More filter; chọn Packing list PO | 2 values: Chờ duyệt/Waiting Approve và Đã duyệt/Approved | High |
| TC-PKL-039 | BVA ±5%: tổng = đúng ±5% boundary | R006 | Functional | Tổng Qty packing list = Qty PO × 1.05 (boundary) | Pass không cần BOD (vẫn trong khoảng ±5%) | Medium |
| TC-PKL-040 | BVA ±5%: tổng vượt 1 đơn vị trên ±5% | R006 | Functional | Tổng vượt ±5% + 1 đơn vị | MSG-PKL-010 cảnh báo | Medium |

## 🚧 Blocked Coverage

- **R025, AC-20 (Q-017)** — chờ xác nhận formula Yard (raw L2479 vs L2506 inconsistency). Không thể test quy đổi Yard.
- **R028, R031 (Q-002)** — chờ API endpoints push Inside + ADJ. TC-PKL-030/034/035 test behavior nhưng không verify API.
- **ERR-PKL-005 (Q-003)** — chờ xác nhận typo "tronng PO". Không thể test message text.
- **ERR-PKL-007, ERR-PKL-008 (Q-004)** — chờ verbatim EN. TC-PKL-018/019 test VN chỉ.
- **MSG-PKL-010 (Q-005)** — chờ xác nhận typo "nhân" → "nhận". Không thể test VN message text.
- **R013, R016 (Q-006)** — chờ suggest order (alphabetical/số lô/qty). Không thể test sort order suggest.
- **R014 (Q-007)** — chờ xác nhận hệ số nguồn (master data hay user nhập). Không thể test source hệ số.
- **R019-R025 (Q-008, Q-009)** — Pending 12-05-2026. Toàn bộ Update 16-04-2026 (Delivery method, Width, GSM, Gross, Net, công thức Yard/Mét, ẩn edit SL) chờ resume.
- **R025 (Q-010)** — chờ xác nhận 0.9144 configurable. Không thể test constant configurable.
- **R029 (Q-011)** — chờ xác nhận > 10% per cây hay tổng SKU. TC-PKL-031 giả định per cây theo raw "từng cây".
- **R028 (Q-012)** — chờ xác nhận status UID mới sinh. Không thể test UID mới status.
- **R010 (Q-013)** — chờ xác nhận khi nào control UI edit sẽ fix. Không thể test behavior edit UI.
- **R015 vs R028 (Q-014)** — chờ xác nhận conflict rule (ghi theo packing list vs ghi dư + ADJ). TC-PKL-023/024 vs TC-PKL-030 có thể conflict nếu không được clarify.
- **R007 (Q-015)** — chờ xác nhận auto Approved bổ sung có bao gồm ±5% không. TC-PKL-037 giả định auto Approved bất kể.
- **R026, R027 (Q-016)** — chờ xác nhận Qty per ADJ display scope (cuộn/UID/SKU). Không thể test granularity.

## Regression Impact
- [[stub_receiving_po_fabric]] — nhận Vải UID group
- [[stub_receiving_po_app]] — validate App scan khi có packing list
- [[stub_receiving_po_inbound_shipment]] — Inbound listing Packing list PO column

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.2. 40 TC active, 16 blocked coverage item. R019-R025 bị Pending 12-05-2026 nên không có TC.
