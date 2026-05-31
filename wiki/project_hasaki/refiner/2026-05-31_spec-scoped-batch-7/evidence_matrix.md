---
session: "2026-05-31"
batch: "spec-scoped-batch-7"
generated_at: "2026-05-31 16:40:00+07:00"
---

# Evidence Matrix — spec-scoped-batch-7

> Per-claim verification (raw-first cho mọi claim mapped đến section flag-critical: enum / formula / state_transition / business_rule / error_messages / validation_rule). Raw source: `07062_Receiving_PO_Docs_ver2.17.md` (v2.17).
> Sampling 1/5 cho claim UI/navigation thuần. Trọng tâm: Error Messages (verbatim), Business Rules, Enum completeness, Formula.

---

## stub_receiving_po_confirm_paste_id (07062#L1808-L2070)

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| L1813-1816 `PO [PO code] chưa được nhận hàng. / has not received yet.` | confirm_paste_id R002 / ERR-CPI-001 | SUPPORTED | Keep |
| L1817-1819 `PO [PO code] không tồn tại trên hệ thống. / does not exist in the system.` | R003 / ERR-CPI-002 | SUPPORTED | Keep |
| L1820-1823 `PO [PO code] không thuộc kho đang xử lý. / is not in the warehouse being processed.` | R004 / ERR-CPI-003 | SUPPORTED | Keep |
| L1824-1829 `PO [PO code] đã hoàn thành việc dán ID cho sản phẩm. / has completed pasting ID...` | R005 / ERR-CPI-004 | SUPPORTED | Keep |
| L1853-1858 màu phiên VAS {Xám / Xanh dương / Cam} + định nghĩa từng màu | R007 (enum 3/3) | SUPPORTED | Keep (enum đầy đủ) |
| L1861-1863 "Chỉ cho chọn 1 VAS cho 1 lần dán" + status → "Đang xử lý" (In-Propress[sic]) | R008 (state transition) | SUPPORTED | Keep (raw typo "In-Propress" → spec viết In-Progress; minor, không đổi nghĩa) |
| L1872-1876 mutex VAS user khác disable; chỉ chọn "Mới"(Open) hoặc "Đang xử lý" của chính user | R010 | SUPPORTED | Keep |
| L1877-1880 1 VAS nhiều người + API validation realtime tránh trùng | R011 | SUPPORTED | Keep (Q-001 hỏi endpoint — hợp lệ) |
| L1887-1890 VAS yêu cầu QC chưa đánh giá → "hiện thông báo" (raw không verbatim message) | R013 / MSG-CPI-005 | UNCLEAR | Move to Q (đã có Q-003 + Blocked Coverage) |
| L1894-1900 Step 3 không áp dụng category {Sức khoẻ-Làm đẹp, Thuốc, Thuốc (GPP)} + "có thể bổ sung" | R014 | SUPPORTED | Keep (Q-006 hỏi list bổ sung — hợp lệ) |
| L1927-1931 max 5 hình, 1 video 15s, có thể cả 2 | R018 (validation/media) | SUPPORTED | Keep |
| L1971-1972 Serial auto-gen pattern `[1023][YYMMDD][6 số tăng dần]` | R022 / AC-20 | SUPPORTED | Keep (verbatim formula/pattern) |
| L1952-1956 `wms_product.wms_config&131072>0` → QR; `config&8>0` → Imei | R021 / AC-19 | SUPPORTED | Keep (Q-002 hỏi bit list đầy đủ — hợp lệ) |
| L1978-1982 SKU required Imei → auto bật nhưng không bắt buộc nhập | R023 / AC-21 | SUPPORTED | Keep |
| L2002-2008 Lưu khi chưa đủ số dòng → "hiện thông báo xác nhận" (raw không verbatim) | R027 / MSG-CPI-006 | UNCLEAR | Move to Q (đã có Q-004 + Blocked Coverage) |
| L2012-2015 màu Step 4 {Xám / Xanh dương / Xanh lá} | R028 (enum 3/3) | SUPPORTED | Keep (enum đầy đủ) |
| L2023-2035 RFID Case 1 (nội bộ Long An) cho cả 2 option + tab Hợp lệ/Không hợp lệ | R030 | SUPPORTED | Keep |
| L2039-2044 RFID Case 2 (vendor ngoài) chỉ từng SKU; tab Không hợp lệ rỗng | R031 | SUPPORTED | Keep |
| L2050-2057 Hoàn thành chưa đủ SL → confirm → Yes → VAS giữ In-Progress | R033 / MSG-CPI-007 | SUPPORTED (msg verbatim missing → UNCLEAR) | Keep R033; Move msg to Q (Q-005) |
| L2058-2065 Hoàn thành đủ SL → confirm → Yes → VAS Completed | R034 / MSG-CPI-008 | SUPPORTED (msg verbatim missing → UNCLEAR) | Keep R034; Move msg to Q (Q-005) |

## stub_receiving_po_vas_manual (07062#L2071-L2181)

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| L2076-2079 Type bổ sung value "Manual" listing VAS | R001 (enum) | SUPPORTED | Keep |
| L2080-2085 VAS Manual + status {Open, In-Progress} → cho update Qty received | R002 | SUPPORTED | Keep (Q-011 audit log — hợp lệ) |
| L2088-2091 SKU config RFID + KHÔNG Cate Thời trang + KHÔNG Brand Synctive → scan giống Serial + sinh VAS RFID | R003 | SUPPORTED | Keep (Q-007 định nghĩa Thời trang/Synctive — hợp lệ) |
| L2104-2107 RFID validity: tất cả RFID phải CHƯA tồn tại = hợp lệ; đã tồn tại = không hợp lệ | R005 | SUPPORTED | Keep (Q-008 phân biệt 2 flow — hợp lệ) |
| L2111-2112 SL RFID scan > SL cần khai báo → "hiện thông báo" (raw không verbatim) | R007 / MSG-VSM-003 | UNCLEAR | Move to Q (đã có Q-006) |
| L2121-2122 Nút "Hoàn thành" chỉ hiện khi tất cả SKU đủ SL | R008 (state) | SUPPORTED | Keep |
| L2126-2130 Kho bắt buộc, default kho ngoài, load theo phân quyền | R010 | SUPPORTED | Keep |
| L2131-2137 Loại VAS {RFID, Serial} bắt buộc | R011 (enum 2/2) | SUPPORTED | Keep (Q-009 hỏi có value khác — hợp lệ) |
| L2142-2144 Mã phiếu nhập nguồn optional; nếu nhập validate `Mã [Code] không tồn tại trên hệ thống.` | R012 / ERR-VSM-001 | SUPPORTED (EN missing → UNCLEAR) | Keep VN; Move EN to Q (Q-005) |
| L2153-2156 check tồn kho UID {In-Bin, Picklisted} | R014 (enum/rule) | SUPPORTED | Keep (Q-010 lý do skip Received — hợp lệ) |
| L2159-2163 `Số lượng cần khai báo (125) không được lớn hơn số lượng tồn kho trên hệ thống (120).` | R015 / ERR-VSM-002 | SUPPORTED (EN missing → UNCLEAR) | Keep VN; Move EN to Q (Q-005) |
| L2164-2165 SKU phải config tương ứng Loại VAS → "hiện thông báo" (raw không verbatim) | R016 / MSG-VSM-004 | UNCLEAR | Move to Q (đã có Q-003) |
| L2166-2168 Xoá SKU khỏi danh sách → "hiện thông báo xác nhận" (raw không verbatim) | R017 / MSG-VSM-005 | UNCLEAR | Move to Q (đã có Q-004) |
| L2169-2171 Tạo mới → "hiện thông báo xác nhận" (raw không verbatim) | R018 / MSG-VSM-006 | UNCLEAR | Move to Q (đã có Q-004) |

## stub_receiving_po_date_rules (07062#L1070-L1496)

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| L1074-1077 `Hạn sử dụng nhỏ hơn yêu cầu... PO (HSD tối thiếu[sic] [Ngày hệ thống tính toán])` | R001 / ERR-DTR-001 | MISSING_DETAIL | Add Q-ID: raw VN typo "tối thiếu" → spec viết "tối thiểu" (silent correction, không có Q tương ứng — vi phạm PATCH-001). EN missing đã có Q-005 |
| L1078-1085 Formula HSD min `[% Allowed Shelf Life PO] * [Product's Shelf Life]` (không làm tròn, VD 20,16 tháng) + ngày nhận | R002 (formula) | SUPPORTED | Keep (verbatim formula) |
| L1086-1090 HSD trùng tháng HSD tối thiểu vẫn cho nhận (HSD tính ngày cuối tháng) | R003 | SUPPORTED | Keep |
| L1096-1102 `Hạn sử dụng lớn hơn vòng đời... (24 tháng). / Expiration date is greater... (24 months).` | R004 / ERR-DTR-002 | SUPPORTED | Keep (Q-006 hỏi 24 configurable — hợp lệ) |
| L1103-1105 PO tester → SKU nhận nếu HSD ≥ 3 tháng | R006 | SUPPORTED | Keep |
| L1106-1114 `Số lượng của SKU 100540031 lớn hơn... / The quantity of SKU 100540031 is greater...` | R007 / ERR-DTR-005 | SUPPORTED | Keep (verbatim incl. SKU number) |
| L1123-1128 `Số lô của sản phẩm đã tồn tại... / Batch code of product already exists...` | R008 / ERR-DTR-003 | SUPPORTED | Keep |
| L1143-1150 `Serial/Imei của sản phẩm đã tồn tại... / Serial/Imei of prodcut[sic] already exists...` | R009 / ERR-DTR-004 | SUPPORTED | Keep (typo `prodcut` đã có Q-002) |
| L1160-1162 CCDC Serial 1 scan = 1 qty; SL>1 → "hiện thông báo" (raw không verbatim) | R010 / MSG-DTR-006 | UNCLEAR | Move to Q (đã có Q-003) |
| L1182-1190 SKU combo HSD rules (30-05-2025): 3 case a/b/c verbatim | R014 | SUPPORTED | Keep |
| L1193-1203 Override (04-06-2025): chỉ cần con lẻ required → popup; combo required + lẻ không required → vẫn popup combo | R015 | SUPPORTED | Keep |
| L1207-1212 RFID Thời trang + Brand Synctives + required RFID → scan khi nhận, auto VAS | R016 | SUPPORTED | Keep (Q-011 spelling Synctive vs Synctives — raw L1209 "Synctives") |
| L1221-1224 EN `Do you want to delete SKU 253900004 from the receiving session?...` | R017 / MSG-DTR-008 | SUPPORTED (VN missing → UNCLEAR) | Keep EN; VN không có trong raw |
| L1231-1232 EN `Do you want to delete serial 2UA49P120 of SKU 253900004...` | R018 / MSG-DTR-009 | SUPPORTED (VN missing → UNCLEAR) | Keep EN |
| L1306-1320 enum Lý do thiếu {Giao thiếu hàng (+NCC giao bù Y/N), Sản phẩm không phù hợp (+Tình trạng {Hư hỏng/Cận date/Hết date/Khác}, HSD YYYY-MM)} | R023 (enum 2/2 + 4/4) | SUPPORTED | Keep (enum đầy đủ; Q-012/Q-013 — hợp lệ) |
| L1349-1352 Khai báo tất cả: Lý do default "Giao thiếu hàng" disable; NCC giao bù default "Có" editable | R026 | SUPPORTED | Keep |
| L1379-1380 Kết thúc nhận hàng → mới gọi API update PO Inside "Receiving" | R029 (state/API) | SUPPORTED | Keep (Q-001 endpoint — hợp lệ) |
| L1457-1463 API `check_issue:1, issue:{note, unsuitable:{qty, media}}` | R030 (API contract) | SUPPORTED | Keep (verbatim payload) |
| L1464-1469 API `check_issue:1, issue:{note: bắt buộc}` + Inside auto compare | R031 (API contract) | SUPPORTED | Keep (verbatim payload) |
| L1386-1387 PO không "đồng kiếm"[sic] → biên bản bàn giao kiện hàng | R033 | SUPPORTED | Keep (typo `kiếm` đã có Q-004) |
| L1419-1430 Nút Hoàn thành PO vs Hoàn thành phiên — điều kiện show | R035 | SUPPORTED | Keep (Q-014 edge case — hợp lệ) |
| L1433-1434 EN `Please update the delivery document image.` (raw chỉ EN) | R036 / MSG-DTR-011 | SUPPORTED (VN missing → UNCLEAR) | Keep EN (Q-005) |
| L1439-1448 confirm `Do you want to confirm completion of PO 10012402010027?` + status PO/ASN Received + tồn kho + sync Inside | R037 / MSG-DTR-012 | SUPPORTED | Keep |
| L1449-1456 PO config: nhận thiếu → "Waiting Adj Invoice"; item không phù hợp → "Receiving Issue" | R038 (state) | SUPPORTED | Keep (Q-015 combined — hợp lệ) |
| L1473-1479 SPKPH → import stock + UID product status "Damaged"; vendor return dùng UID Damaged theo PO source | R039 (state) | SUPPORTED | Keep |
| L1480-1495 Hoàn thành phiên → confirm → ASN Received + tồn kho theo phiên | R040 (state) | SUPPORTED | Keep |

## stub_receiving_po_packing_list (07062#L2182-L2580)

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| L2185-2186 re-import trùng PO/SKU/Roll/Batch → update SL yêu cầu | R001 | SUPPORTED | Keep |
| L2188-2218 9 validation messages (PO code/SKU/Roll/Batch/SL) VN+EN | R002-R004 / ERR-PKL-001..006,009,012 | SUPPORTED | Keep (verbatim) |
| L2201-2203 `Dòng N – SKU không tồn tại tronng[sic] PO` / `...does not exist in the PO.` | R003 / ERR-PKL-005 | SUPPORTED | Keep (typo `tronng` đã có Q-003) |
| L2227-2231 edit/xoá chỉ PO status khác Received | R005 | SUPPORTED | Keep |
| L2238-2246 ±5% validate message verbatim VN+EN (VN typo "nhân hàng") | R006 / MSG-PKL-010 | SUPPORTED | Keep (typo `nhân` đã có Q-005) |
| L2253-2255 PO Receiving + import bổ sung → SKU auto approved | R007 | SUPPORTED | Keep (Q-015 scope ±5% — hợp lệ) |
| L2256-2269 Inbound table cột Packing list PO {Chờ duyệt/Waiting for Approval, Đã duyệt/Approved} + hyperlink | R008 (enum 2/2) | SUPPORTED | Keep |
| L2262-2265 Approve confirm `Bạn có chắc... duyệt cho nhận hàng theo packing list không? / Do you want to approve...` | R009 / MSG-PKL-011 | SUPPORTED | Keep |
| L2270-2276 Re-import sau Approved >±5% → Waiting; chỉ edit/xoá → giữ Approved | R010 (state) | SUPPORTED | Keep (Q-013 control UI — hợp lệ) |
| L2290-2297 App scan validate: Waiting Approve block (VN); chưa import block (VN); Approved no data → pass | R012 / ERR-PKL-007,008 | SUPPORTED (EN missing → UNCLEAR) | Keep VN; Move EN to Q (Q-004) |
| L2308-2322 SKU vải lẻ: suggest mã cuộn theo số lô; hệ số quy đổi default x1; SL thực nhận × hệ số | R013, R014 | SUPPORTED | Keep (Q-006 suggest order, Q-007 hệ số — hợp lệ) |
| L2330-2343 thông tin ghi nhận + "SL thực nhận > SL yêu cầu packing list → ghi theo packing list, ngược lại theo thực nhận" | R015 | SUPPORTED | Keep (Q-014 conflict với R028 — hợp lệ, đúng case khác nhau) |
| L2358-2367 SKU combo: nhập thập phân; không nhân hệ số combo→con lẻ; tổng UID phải số nguyên dương | R016, R017 | SUPPORTED | Keep |
| L2387-2388 sau xác nhận hệ thống tự nhân hệ số con lẻ cập nhật stock | R017 | SUPPORTED | Keep |
| L2389-2410 `Trừ lõi`: formula `[SL thực nhận] – [Trừ lõi]`; có hệ số `[SL]×[Hệ số]–[Trừ lõi]`; combo không có hệ số | R018 (formula) | SUPPORTED | Keep (verbatim formula) |
| L2420-2429 Delivery method {Partial (no ±5%, total PKL < total PO), Full PO (giữ ±5%)} — Pending 12-05-2026 | R019 (enum 2/2) | SUPPORTED | Keep (Pending; Q-008 — hợp lệ) |
| L2473-2477 Trừ lõi tự tính `= Gross Qty − Net Qty`; = nhau → 0; disable edit | R024 (formula) | SUPPORTED | Keep (verbatim) |
| L2478-2491 Formula quy đổi `Yard = [Weight×1000]/[Width×GSM×0.9144]`; `Mét = [Weight×1000]/[Width×GSM]` | R025 (formula) | SUPPORTED | Keep (formula verbatim) |
| L2493-2510 VD raw: Width=1.5, GSM=200, Weight=15 → raw tính `(15*1000)/((180*200)*0.9144)` [raw nội bộ mâu thuẫn: formula dùng Width=1.5 nhưng VD plug 180] | AC-20 spec tự tính `(15×1000)/(1.5×200×0.9144) ≈ 54.69 Yard` | MISSING_DETAIL | Add Q-ID: raw VD dùng `180` ≠ formula Width=1.5; spec resolve bằng 1.5 → 54.69 (không trace raw VD). Q-010 chỉ cover 0.9144, KHÔNG cover 180-vs-1.5 |
| L2520-2524 ASN detail: Qty received (theo PO, không gồm dư) + Qty per ADJ (số dư auto tạo phiếu) | R026 | SUPPORTED | Keep (Q-016 display scope — hợp lệ) |
| L2531-2545 Rules nhận dư: ghi theo thực nhận; total<PO → điều chỉnh HĐ; total>PO → UID gr theo PKL + số dư ADJ sinh UID mới cùng UID group | R028 | SUPPORTED | Keep |
| L2546-2555 cảnh báo >10% packing list cây vải VN+EN verbatim + action Kiểm tra lại/Xác nhận | R029 / MSG-PKL-013 | SUPPORTED | Keep (Q-011 scope cây/SKU — raw L2546 "từng cây vải") |
| L2562-2569 VD R030: SKUA PO 105m, PKL 106.15, thực nhận 106.60; cây 9-12m; cây >PKL → UID gr theo PKL + ADJ + UID mới | R030 | SUPPORTED | Keep (raw đánh dấu "xem file excel đính kèm" — VD minh hoạ, không phải rule mới) |
| L2570-2575 push Inside: total<PO → điều chỉnh HĐ; total>PO → push theo PO + tự tạo ADJ | R031 | SUPPORTED | Keep (Q-002 endpoint — hợp lệ) |

---

## Tổng kết labels

| Spec | SUPPORTED | UNCLEAR (pending-source hợp lệ) | MISSING_DETAIL | INFERRED/LOGIC/STRIPPED/NEGATION/PHANTOM/POTENTIAL |
|:-----|:---------:|:-------------------------------:|:--------------:|:-:|
| confirm_paste_id | đa số (34 R + 29 AC) | 4 (MSG-CPI-005/006/007/008 verbatim missing) | 0 | 0 |
| vas_manual | đa số (19 R + 22 AC) | 6 (MSG-VSM-003/004/005/006 + ERR EN x2) | 0 | 0 |
| date_rules | đa số (40 R + 39 AC) | 5 (MSG-DTR-006/008/009/011 + EN missing) | 1 (R001 typo "tối thiếu" silent fix) | 0 |
| packing_list | đa số (31 R + 30 AC) | 3 (ERR-PKL-007/008 EN missing) | 1 (AC-20 raw VD 180-vs-1.5 inconsistency) | 0 |

**0 INFERRED / 0 LOGIC_INFERRED / 0 STRIPPED_CONDITION / 0 NEGATION_FLIP / 0 PHANTOM_EVIDENCE / 0 POTENTIAL_OMISSION** cho cả 4 specs.
