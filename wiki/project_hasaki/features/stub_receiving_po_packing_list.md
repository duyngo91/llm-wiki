---
aliases: [stub_receiving_po_packing_list]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_packing_list
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L2182-L2580
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 22:30:00"
verification_status: Pending
approved_by:
approved_at:
approval_note:
---

# REQ: stub_receiving_po_packing_list

## Tổng quan
- **Mã tính năng:** stub_receiving_po_packing_list
- **Feature:** Import Packing list PO + Nhận hàng theo Packing list (SKU vải lẻ/combo) + Trừ lõi + Quy đổi Yard/Mét + Update rules nhận dư
- **Mô tả ngắn:** Import packing list cho PO vải với 9 validations (PO code, SKU, Roll code, Batch code, Số lượng yêu cầu, trùng dòng). Listing quản lý import cho phép edit SL/xoá nếu PO chưa Received. Update 29-01-2026: validate ±5% Qty confirm + Inbound table thêm cột Packing list PO (Waiting for Approval / Approved); App receiving validate Packing list status. Nhận hàng SKU vải lẻ (suggest mã cuộn từ packing list, quy đổi pcs với hệ số) và combo (input thập phân, không nhân hệ số). Update 02-04-2026: bổ sung `Trừ lõi`. Update 16-04-2026 (Pending 12-05-2026): Delivery method (Partial/Full PO), Width, GSM, Gross qty, Net qty + công thức quy đổi Kg → Yard/Mét. Update 20-04-2026: `Qty per ADJ` cho số dư + cảnh báo > 10% packing list. Update 17-05-2026 mark phần sau cho PO sample & PO chính.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Operations (import packing list), Nhân viên kho (scan nhận PO vải), BOD (approve packing list > ±5%).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[test_stub_receiving_po_packing_list]]
- **API Spec liên quan:** N/A — raw không nêu endpoint cụ thể; mention "push lên Inside" cho số dư ADJ.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_receiving_po_fabric]] (nhận hàng Vải khai báo Group UID), [[stub_receiving_po_inbound_shipment]] (Inbound listing), [[stub_receiving_po_app]] (Receiving PO App). ↔️ liên quan [[stub_receiving_po_date_rules]] (HSD validation), [[stub_receiving_po_po_sample]] (PO sample). ➡️ feed Adjustment system (ADJ cho số dư), Inside (sync stock).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07062_Receiving_PO_Docs_ver2.17.md | 2.17 | ✅ Hiện hành |
| 2 | Figma mockup UID group | https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO?node-id=2302-771 | — | Hiện hành (Q-001) |
| 3 | Figma mockup ASN detail (20-04-2026) | https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO?node-id=2328-217 | — | Hiện hành (Q-001) |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | Sync Inside: push số PO (nếu nhận thiếu yêu cầu điều chỉnh hoá đơn); push theo PO + tự tạo ADJ cho số dư (nếu > PO) | R031 | 07062#L2570-L2575 | TBD — Q-002 |
| N/A | Adjustment Auto-Create cho số dư packing list (sinh UID mới cùng UID group) | R028, R031 | 07062#L2543-L2545 | TBD — Q-002 |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Import packing list với template import. **Lưu ý:** nếu import lại nhưng các thông tin `PO code`, `SKU`, `Roll code`, `Batch code` **trùng với data đã có trên hệ thống** thì sẽ **cho update lại số lượng yêu cầu** | Functional + Business rule | High | ✅ | 07062#L2182-L2186 |
| R002 | Validation Import — `PO code` để trống → `Dòng N – Mã PO không được để trống.` / `Line N – PO code cannot be empty.`; `PO code` không tồn tại hệ thống → `Dòng N – Mã PO không tồn tại trên hệ thống.` / `Line N – PO code does not exist in the system.` | Validation | High | ✅ | 07062#L2188-L2195 |
| R003 | Validation Import — `SKU` để trống → `Dòng N – SKU không được để trống.` / `Line N – SKU cannot be empty.`; `SKU` không tồn tại hệ thống → `Dòng N – SKU không tồn tại trên hệ thống.` / `Line N – SKU does not exist in the system.`; `SKU` không tồn tại trong PO → `Dòng N – SKU không tồn tại tronng PO` (typo `tronng` — Q-003) / `Line N – SKU does not exist in the PO.` | Validation | High | ✅ | 07062#L2196-L2203 |
| R004 | Validation Import — `Roll code` để trống → `Dòng N – Mã cuộn không được để trống.` / `Line N – Roll code cannot be empty.`; `Batch code` để trống → `Dòng N – Mã lô không được để trống.` / `Line N – Batch code cannot be empty.`; `Số lượng yêu cầu` để trống → `Dòng N – Số lượng yêu cầu không được để trống.` / `Line N – Requested quantity cannot be empty.`; `Số lượng yêu cầu` âm/ký tự → `Dòng N – Số lượng yêu cầu không hợp lệ` / `Line N – Requested quantity is invalid.`; Thông tin trùng dòng (2 dòng giống hệt nhưng khác qty request) → `Dòng N – Dữ liệu đã tồn tại trên file import` / `Line N – Data already exists in the import file.` | Validation | High | ✅ | 07062#L2204-L2218 |
| R005 | Màn hình quản lý thông tin packing list được import — với những PO có trạng thái **khác `Received`**, hỗ trợ cho user: (a) chọn nhiều dòng để **xoá và import lại**; (b) chọn **edit số lượng yêu cầu** | Functional + UI | High | ✅ | 07062#L2220-L2231 |
| R006 | Update 29-01-2026 — Import Packing list PO: sau khi validate data file hợp lệ → bước Save data, **bổ sung validate**: nếu tổng `Qty request` của SKU > **± 5%** Qty confirm của SKU trong PO → **hiện cảnh báo** `PO 10012601001737, SKU 422504712 có tổng số lượng trong packing list lớn hơn ± 5% so với số lượng yêu cầu trên PO. Nếu xác nhận import thì liên hệ BOD để được duyệt trước khi nhân hàng.` / `PO 10012601001737, SKU 422504712: The total quantity in the packing list exceeds ±5% of the PO quantity. If confirming the import, please contact BOD for approval before receiving.`. Action: `Kiểm tra lại` (tắt → không lưu data), `Xác nhận Import` (xác nhận import) | Validation + Confirm | High | ✅ | 07062#L2233-L2252 |
| R007 | Update 29-01-2026 — Nếu PO đã chuyển **`Receiving`** thì khi import packing list bổ sung thì **mặc định các SKU sẽ auto approved** | Business rule | High | ✅ | 07062#L2253-L2255 |
| R008 | Update 29-01-2026 — **Inbound Data table**: bổ sung cột `Packing list PO` với 2 values: `Chờ duyệt / Waiting for Approval` (khi PO vải vừa rớt xuống WMS), `Đã duyệt / Approved` (nếu Packing list import vào vẫn trong khoảng ±5% thì **auto approved**). Hyperlink: nhấp vào để link sang trang Packing list theo filter của PO | UI + Enum + Navigation | High | ✅ | 07062#L2256-L2269 |
| R009 | Update 29-01-2026 — Inbound table — Approve button: nếu Packing list `Waiting for Approval`, hiển thị button `Approve` dưới trạng thái với confirm dialog `Bạn có chắc chắn muốn duyệt cho nhận hàng theo packing list không?` / `Do you want to approve receiving based on the packing list?` | Confirm + Functional | High | ✅ | 07062#L2262-L2266 |
| R010 | Update 03-02-2026 — Rules khi status packing list PO đang là `Approved`: (a) Nếu có **import lại** Packing list mà validate tổng Qty request SKU > ±5% Qty confirm PO → vẫn sẽ chuyển về `Waiting for Approval`; (b) Nếu có **update lại số lượng hay xoá bớt** đi thì trạng thái sẽ **không thay đổi** (do chưa thể tính toán lại nên tạm thời chưa control trên UI) | Business rule + State transition | High | ✅ | 07062#L2270-L2276 |
| R011 | Update 29-01-2026 — Inbound `More filter`: `Packing list PO` 2 values {`Chờ duyệt / Waiting Approve`, `Đã duyệt / Approved`}. Detail page: hiện thông tin Packing list PO và button Approve cho trạng thái `Waiting Approve` | Filter + UI | High | ✅ | 07062#L2277-L2289 |
| R012 | Update 29-01-2026 — Receiving PO App — bổ sung validate khi scan nhận PO. Nếu Packing list status `Waiting Approve` → **không cho nhận**, hiện thông báo `PO chưa được duyệt Packing list nên không thể nhận hàng.` (raw chỉ có VN — Q-004). Nếu Packing list của PO **chưa được import** → không cho nhận, `PO chưa import Packing list nên không thể nhận hàng.` Nếu Packing list PO đã `Approved` nhưng **không có data import** → vẫn pass cho nhận PO | Validation + Business rule | High | ✅ | 07062#L2290-L2300 |
| R013 | Nhận hàng PO cho SKU vải **theo packing list (SKU vải là con lẻ)**: khi scan nhận SKU lẻ vải — nếu PO chưa import packing list → vẫn cho nhận theo UID group bình thường. Nếu PO đã import: khi user nhập số lô, **hệ thống suggest danh sách mã theo packing list** để user chọn (user vẫn có thể nhập mã cuộn khác suggest) | Functional + UX | High | ✅ | 07062#L2305-L2313 |
| R014 | SKU vải lẻ (tiếp) — Sau khi có đầy đủ thông tin số lô + mã cuộn → show thông tin `Số lượng yêu cầu từ packing list`. User nhập `Số lượng thực nhận` sau khi cân. **Chọn hệ số cần quy đổi ra đơn vị cần nhận (pcs)** — mặc định `x1`. Khai báo nhóm UID và HSD cho SP. Nhấn `+` để thêm vào danh sách đã nhận. **Lưu ý: SL thực nhận sẽ được nhân với hệ số khi cập nhật vào danh sách**. Chụp hình cho SP đang khai báo nhận | Functional + UI | High | ✅ | 07062#L2314-L2327 |
| R015 | SKU vải lẻ — Thông tin ghi nhận sau khi nhấn thêm: `Mã cuộn` (user nhập), `Nhóm UID` (user nhập), `Hình ảnh` (chụp), `Số lô` (user nhập), `SL yêu cầu` (lấy từ packing list nếu có), `SL thực nhận` (user nhập × hệ số quy đổi), `Nhận lệch = SL thực nhận – SL yêu cầu`, `HSD` (user nhập). **Lưu ý:** nếu `SL thực nhận > SL yêu cầu từ packing list` → **ghi nhận theo packing list**. Ngược lại → ghi nhận theo số thực nhận | Business rule + UI | High | ✅ | 07062#L2329-L2346 |
| R016 | SKU vải combo — Khi scan nhận SKU combo vải: nếu PO chưa import packing list → nhận theo UID group bình thường. Nếu đã import: user nhập số lô → suggest mã cuộn; user nhập `Số lượng thực nhận` (**cho nhập số thập phân**); khai báo nhóm UID + HSD; nhấn `+` để thêm. **Lưu ý: SL thực nhận là số thực theo combo trong packing list (không nhân hệ số quy đổi từ combo qua con lẻ)** | Functional + Business rule | High | ✅ | 07062#L2348-L2363 |
| R017 | SKU vải combo (tiếp) — Tổng SL thực nhận khai báo nhóm UID cho SKU combo **phải là số nguyên dương** (raw L2366-L2367). Cùng format thông tin ghi nhận như SKU lẻ (R015). Sau khi xác nhận → hệ thống tự động **nhân với hệ số của con lẻ** để cập nhật đúng stock cho con lẻ | Business rule + Validation | High | ✅ | 07062#L2366-L2388 |
| R018 | Update 02-04-2026 — Bổ sung thông tin `Trừ lõi` (Tare weight) tại màn khai báo UID group cho SKU vải. Cho phép user nhập **số thập phân**. **Với SKU normal:** giá trị mặc định = 0. Khi user thay đổi → lưu lại cho lần thao tác sau. Sau khi user nhập đầy đủ + submit → công thức: `[Số lượng thực nhận] – [Trừ lõi]` và so sánh với SL yêu cầu Packing list để ghi nhận SL thực nhận. **Lưu ý:** khi SL thực nhận có nhân hệ số: `[SL thực nhận] × [Hệ số] – [Trừ lõi]`. **Với SKU combo:** tương tự normal, chỉ khác **không có chỗ nhân hệ số quy đổi** | Business rule + Formula | High | ✅ | 07062#L2389-L2412 |
| R019 | Update 16-04-2026 (**Pending 12-05-2026 không làm tiếp do vận hành PO gặp khó khăn**) — Import Packing list update template bổ sung cột `Delivery method` 2 lựa chọn: (a) `Giao 1 phần (Partial)` — nếu chọn thì khi import sẽ **không validate chỗ lệch ±5%**, chỉ cần total SL trong Packing list < total SL trong PO là cho import. Nếu PO đã chọn option này thì những lần import sau cũng dùng option này; (b) `Giao full PO (Full PO)` — giữ nguyên validate cũ (±5%) | Enum + Business rule + Pending | Medium | ⚠️ | 07062#L2415-L2429 |
| R020 | Update 16-04-2026 — Cột `Khổ vải (Width)(m)`: thông tin khổ vải do NCC cung cấp. Sử dụng khi SKU đặt hàng bằng đơn vị tính là `Yard` hoặc `Mét`, dùng để **quy đổi từ cân nặng (Kg) qua Yard và Mét** | Business rule + Data | Medium | ⚠️ | 07062#L2430-L2434 |
| R021 | Update 16-04-2026 — Cột `Định lượng vải (GSM)(g/m2)`: thông tin định lượng vải do NCC cung cấp. Sử dụng khi SKU đặt hàng bằng Yard/Mét để **quy đổi từ Kg sang Yard/Mét** | Business rule + Data | Medium | ⚠️ | 07062#L2435-L2439 |
| R022 | Update 16-04-2026 — Cột `Gross quantity(Kg)` (thay thế cột `Quantity request` cũ) — cân nặng bao gồm lõi và bao bì (nếu có). Cột `Net quantity (Kg)` — cân nặng thực không bao gồm lõi và bao bì. **Lưu ý:** nếu sản phẩm không có bao bì, lõi thì `Gross quantity = Net quantity` | Business rule + Data | Medium | ⚠️ | 07062#L2440-L2451 |
| R023 | Update 16-04-2026 — Page quản lý Packing list tại `Menu: Inbound / Packing list PO`. Bổ sung các cột tương ứng file Excel import. **Tạm thời ẩn tính năng edit SL trên UI của packing list** để hạn chế các case phát sinh — người dùng cần thì import lại để update | UI + Functional | Medium | ⚠️ | 07062#L2456-L2462 |
| R024 | Update 16-04-2026 — Update UI nhận SKU có UID group. Màn scan nhận SKU vải yêu cầu khai báo UID group hiển thị 2 thông tin `Gross Qty` và `Net Qty` trên file Packing list theo số lô và số cuộn tương ứng đã chọn. Thông tin `Trừ lõi` hệ thống **tự tính**: `Trừ lõi = Gross Qty − Net Qty`. Nếu 2 số bằng nhau → Trừ lõi = 0. **Disable không cho edit** | Business rule + Formula + UI | Medium | ⚠️ | 07062#L2465-L2477 |
| R025 | Update 16-04-2026 — Công thức quy đổi từ Kg thành: `Yard = [Weight(Kg) × 1000] / [Width(m) × GSM(g/m²) × 0.9144]`; `Mét = [Weight(Kg) × 1000] / [Width(m) × GSM(g/m²)]`. Áp dụng khi nhận PO cho SKU có **đơn vị tính (lấy từ Inside) là Yard hoặc Mét**. Các đơn vị tính khác vẫn ghi nhận theo số lượng (Kg) lấy từ cân. `Weight` = cân nặng từ cân; `Width` + `GSM` từ Packing list theo mã lô + mã cuộn | Formula + Business rule | Medium | ⚠️ | 07062#L2478-L2491 |
| R026 | Update 20-04-2026 — Update rules nhận dư cho PO vải. Màn `ASN detail`: `Qty received` vẫn là SL thực nhận theo PO như hiện tại (không bao gồm SL dư); `Qty per ADJ` (Số lượng theo ADJ): **số lượng dư mà hệ thống tự động tạo phiếu điều chỉnh** để import vào hệ thống để ghi nhận stock theo đúng SL thực nhận | UI + Business rule + Auto-create ADJ | High | ✅ | 07062#L2517-L2524 |
| R027 | Update 20-04-2026 — Màn chi tiết UID group theo SKU: bổ sung 2 cột `Số lượng theo PO (Qty per PO)` (SL hệ thống ghi nhận theo PO) và `Số lượng theo ADJ (Qty per ADJ)` | UI | High | ✅ | 07062#L2525-L2530 |
| R028 | Update 20-04-2026 — Rules: khi khai báo nhận cho từng cuộn vải (UID group), ghi nhận hết theo SL thực nhận, **không quan tâm SL thực nhận nhỏ hay lớn hơn Packing list**. Nếu `total SKU thực nhận < SL trên PO` → ghi nhận theo SL thực nhận + yêu cầu NCC điều chỉnh hoá đơn. Nếu `total SKU > SL trên PO` → (a) ghi nhận Qty cho UID group theo số của Packing list; (b) số dư sẽ được ADJ vào và sinh ra UID mới vẫn là UID group được khai báo khi nhận | Business rule + Auto-create | High | ✅ | 07062#L2531-L2545 |
| R029 | Update 20-04-2026 — Khi khai báo UID group cho từng cây vải, nếu SL thực nhận > **10% SL trên Packing list** → hiện thông báo cảnh báo để user check lại trước khi xác nhận: VN `Số lượng thực nhận lớn hơn 10% so với Packing list, bạn có muốn xác nhận nhận hàng không?` / EN `The actual received quantity exceeds the packing list by more than 10%. Do you want to confirm the receipt?`. Action: `Kiểm tra lại` (tắt thông báo + giữ nguyên màn hình khai báo), `Xác nhận` (ghi nhận vào danh sách nhận hàng) | Validation + Confirm | High | ✅ | 07062#L2546-L2555 |
| R030 | Update 20-04-2026 — Ví dụ minh hoạ R028 + R029: SKUA PO order 105 mét, PKL = 106.15 mét, Thực nhận 106.60 mét. Packing list NCC giao tổng 10 cây, mỗi cây 9-12m. Với cây có qty thực nhận ≤ qty packing list → ghi nhận UID + UID group theo qty thực nhận như cũ. Với cây có qty thực nhận > qty packing list → ghi nhận UID gr có qty = qty Packing list + tổng số dư tạo ADJ + phần chênh lệch của 1 cuộn sinh ra 1 UID mới có cùng UID group với cây đã khai báo | Business rule + Example | High | ⚠️ | 07062#L2557-L2569 |
| R031 | Update 20-04-2026 — Push lên Inside sau khi nhận xong: nếu `total SKU < SL trên PO` → yêu cầu điều chỉnh hoá đơn; nếu `total SKU > SL trên PO` → chỉ push theo số của PO, số còn lại WMS sẽ tự tạo ADJ để import vào | Business rule + API integration | High | ✅ | 07062#L2570-L2575 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User Operations có quyền import packing list.
- PO vải tồn tại trên Inside + đã rớt xuống WMS.
- BOD có quyền approve packing list > ±5%.
- SKU vải có config category Thời trang (NVL) và tên có "Vải" (xem [[stub_receiving_po_fabric]]).

### Luồng chuẩn (Happy Path) — Import packing list valid + auto Approved
1. Operations vào màn import packing list, upload file Excel với template (R001).
2. Hệ thống validate 9 rule (R002-R004): pass.
3. Validate ±5% (R006): total Qty request ≤ ±5% Qty confirm → pass.
4. Save data. Inbound table cột `Packing list PO` = `Approved` auto (R008).

### Luồng chuẩn (Happy Path) — Import > ±5% → Waiting for Approval + BOD approve
1. Import file valid 9 rule.
2. ±5% validate: total Qty > ±5% → MSG-PKL-010 hiện (R006).
3. Operations click `Xác nhận Import` → data save với status `Waiting for Approval` (R006, R008).
4. BOD vào Inbound table, click `Approve` → confirm MSG-PKL-011 → Yes (R009).
5. Status chuyển `Approved`.

### Luồng chuẩn (Happy Path) — Update 03-02-2026: re-import sau Approved
1. Packing list status `Approved`.
2. Operations import lại packing list.
3. Validate ±5%: nếu > ±5% → chuyển về `Waiting for Approval` (R010).
4. Nếu chỉ update SL hoặc xoá bớt → status giữ nguyên `Approved` (R010).

### Luồng chuẩn (Happy Path) — App scan nhận PO với validate Packing list
1. User App scan PO `PO-A` (xem [[stub_receiving_po_app]] flow).
2. Validate Packing list (R012):
   - `Waiting Approve` → ERR-PKL-007 block.
   - Chưa import → ERR-PKL-008 block.
   - `Approved` không có data → pass.
   - `Approved` có data → tiếp flow nhận packing list.

### Luồng chuẩn (Happy Path) — Nhận hàng SKU vải lẻ theo packing list
1. PO đã import packing list. User scan SKU lẻ vải `SP-X` (R013).
2. Nhập số lô `LOT-001` → hệ thống suggest danh sách mã cuộn từ packing list (R013).
3. User chọn `Roll-A1`. Hệ thống show `SL yêu cầu = 50 kg` từ packing list (R014).
4. User cân SP và nhập `SL thực nhận = 48 kg`. Chọn hệ số quy đổi `x2` (1 cuộn = 2 pcs).
5. Khai báo nhóm UID + HSD + chụp hình (R014).
6. Nhấn `+`: SL ghi nhận = 48 × 2 = 96 pcs (R014).
7. `Nhận lệch = 48 − 50 = −2 kg` (R015).
8. Lặp tới đủ SL PO. Nếu SL thực nhận > SL packing list → ghi nhận theo packing list (R015).

### Luồng chuẩn (Happy Path) — Nhận SKU vải combo theo packing list
1. SKU combo vải `COMBO-Y` (R016).
2. Nhập số lô → suggest mã cuộn từ packing list.
3. Nhập `SL thực nhận` (số thập phân OK).
4. Khai báo UID + HSD + chụp hình.
5. Nhấn `+`: ghi nhận theo combo, **không nhân hệ số quy đổi** (R016).
6. Tổng SL khai báo nhóm UID cho combo phải là **số nguyên dương** (R017).
7. Submit → hệ thống tự nhân hệ số con lẻ để cập nhật stock con lẻ (R017).

### Luồng chuẩn (Happy Path) — Update 02-04-2026 Trừ lõi
1. SKU normal: nhập `Trừ lõi = 0.5 kg` (R018).
2. SL thực nhận sau khi cân = 50 kg.
3. Công thức: `50 − 0.5 = 49.5 kg` ghi nhận (R018).
4. Nếu có hệ số x2: `(50 × 2) − 0.5 = 99.5 pcs` (R018).
5. Lần thao tác sau cho SKU này: hệ thống nhớ Trừ lõi đã set (R018).

### Luồng chuẩn (Happy Path) — Update 16-04-2026 Quy đổi Kg → Yard
1. Packing list có Width = 1.5m, GSM = 200 g/m², Gross qty = 15.3 kg, Net qty = 15 kg (R022).
2. Trừ lõi tự tính = 15.3 − 15 = 0.3 (R024).
3. Cân thực = 15 kg. Đơn vị SKU = `Yard`.
4. Yard cần nhận = `(15 × 1000) / (1.5 × 200 × 0.9144) = 54.69` Yard (R025).
5. Ghi nhận số này vào SL thực nhận.
6. Do đơn vị Yard/Mét, packing list không có info SL yêu cầu nên SL yêu cầu + Nhận lệch để trống (R025).

### Luồng chuẩn (Happy Path) — Update 20-04-2026 nhận dư + ADJ
1. PO order 105 mét, packing list 106.15 mét, thực nhận 106.60 mét (R030).
2. Mỗi cây vải 9-12m. User khai báo UID group cho từng cây.
3. Cây có qty thực nhận ≤ qty packing list → ghi nhận UID + UID gr theo qty thực nhận (R030).
4. Cây có qty thực nhận > qty packing list → ghi nhận UID gr = qty packing list. Số dư + chênh lệch 1 cuộn tạo ADJ + sinh UID mới cùng UID group (R028, R030).
5. Cảnh báo > 10%: nếu user khai báo UID 1 cây vải thực nhận > 10% packing list → MSG-PKL-013 confirm (R029).
6. ASN detail: `Qty received` (thực nhận theo PO) + `Qty per ADJ` (số dư) (R026).
7. Push Inside: nếu total < PO → yêu cầu điều chỉnh hoá đơn; nếu total > PO → push theo PO + tự tạo ADJ (R031).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — PO chưa import packing list:** vẫn cho nhận theo UID group bình thường (R013, R016).
- **A2 — Approved không có data import:** vẫn pass cho nhận PO (R012).
- **A3 — Update 03-02-2026: edit SL hoặc xoá bớt packing list Approved:** status giữ nguyên (R010).
- **A4 — Update 16-04-2026 (Pending): Delivery method `Partial`:** không validate ±5%, chỉ cần total Packing list < total PO (R019).
- **A5 — SKU đơn vị Kg (không Yard/Mét):** không apply quy đổi (R025).
- **A6 — Trừ lõi = 0:** không trừ gì (R018, R024).

### Luồng ngoại lệ (Exception Paths)
- **E1-E9 Import 9 validation:** R002-R004 messages.
- **E10 — > ±5% Qty confirm:** MSG-PKL-010 cần BOD approve (R006).
- **E11 — App scan PO Waiting Approve:** ERR-PKL-007 (R012).
- **E12 — App scan PO chưa import packing list:** ERR-PKL-008 (R012).
- **E13 — > 10% packing list cây vải:** MSG-PKL-013 confirm (R029).
- **E14 — SKU combo total UID không phải số nguyên dương:** block (R017).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Re-import packing list | rule | ✅ | PO+SKU+Roll+Batch trùng → update lại SL yêu cầu |
| Import 9 validations | rule | ✅ | PO code/SKU/Roll/Batch không trống + tồn tại + SL hợp lệ + không trùng dòng |
| ±5% validation (29-01-2026) | rule | ✅ | Tổng Qty request SKU > ±5% Qty confirm PO → cảnh báo + cần BOD approve |
| Auto Approved | rule | ✅ | Packing list trong khoảng ±5% → auto Approved khi import |
| PO Receiving + import bổ sung | rule | ✅ | SKU bổ sung auto approved |
| Edit/Xoá packing list | rule | ✅ | Chỉ cho PO status khác `Received` |
| Re-import sau Approved (03-02-2026) | rule | ✅ | > ±5% → chuyển về `Waiting for Approval`; chỉ edit/xoá → giữ Approved |
| App scan validate Packing list | rule | ✅ | `Waiting Approve` block; chưa import block; Approved không data → pass |
| Suggest mã cuộn | rule | ✅ | Hệ thống suggest theo packing list khi nhập số lô |
| Hệ số quy đổi SKU lẻ | rule | ✅ | Default x1; SL thực nhận × hệ số khi ghi vào danh sách |
| SL thực nhận vs Packing list | rule | ✅ | Thực nhận > Packing list → ghi theo Packing list; Thực nhận ≤ Packing list → ghi theo thực nhận |
| SKU combo SL thập phân | rule | ✅ | Cho nhập thập phân khi nhập SL thực nhận |
| SKU combo không nhân hệ số | rule | ✅ | Ghi nhận theo số thực combo, không quy đổi con lẻ |
| SKU combo total UID | integer | ✅ | Tổng SL nhóm UID combo phải là số nguyên dương |
| Auto nhân hệ số combo → con lẻ | rule | ✅ | Sau xác nhận, hệ thống tự nhân hệ số để cập nhật stock con lẻ |
| `Trừ lõi` (02-04-2026) | decimal | ❌ | Default 0 cho SKU normal; user thay đổi → lưu lại cho lần sau |
| Công thức Trừ lõi normal | formula | ✅ | `SL thực nhận − Trừ lõi` (hoặc `SL × Hệ số − Trừ lõi`) |
| Công thức Trừ lõi combo | formula | ✅ | Như normal nhưng không có hệ số quy đổi |
| Delivery method (16-04-2026 Pending) | enum | ❌ | {Partial (no ±5% validate, total PKL < total PO), Full PO (giữ ±5%)} |
| Width + GSM + Gross + Net (16-04-2026) | rule | ⚠️ | Pending 12-05-2026; dùng cho quy đổi Kg → Yard/Mét |
| Edit SL UI packing list | rule | ⚠️ | Tạm thời ẩn (16-04-2026); user import lại để update |
| Trừ lõi tự tính (16-04-2026) | rule | ⚠️ | `Trừ lõi = Gross Qty − Net Qty`; nếu = nhau → 0; disable edit |
| Công thức quy đổi Yard | formula | ⚠️ | `Yard = [Weight × 1000] / [Width × GSM × 0.9144]` |
| Công thức quy đổi Mét | formula | ⚠️ | `Mét = [Weight × 1000] / [Width × GSM]` |
| Quy đổi áp dụng | rule | ⚠️ | Chỉ SKU đơn vị Inside = Yard/Mét; khác đơn vị → Kg từ cân |
| `Qty per ADJ` (20-04-2026) | rule | ✅ | SL dư > PO → auto tạo phiếu ADJ |
| Rule nhận dư cây vải | rule | ✅ | Mỗi cây qty thực nhận > packing list → UID gr theo packing list + ADJ + sinh UID mới cùng UID group |
| Cảnh báo > 10% cây vải | rule | ✅ | SL thực nhận > 10% packing list → confirm dialog trước xác nhận |
| Push Inside sync | rule | ✅ | Total < PO → yêu cầu điều chỉnh hoá đơn; Total > PO → push theo PO + ADJ |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-PKL-001 | Validation | Import — PO code để trống | `Dòng N – Mã PO không được để trống.` | `Line N – PO code cannot be empty.` | 07062#L2190-L2192 |
| ERR-PKL-002 | Validation | Import — PO code không tồn tại | `Dòng N – Mã PO không tồn tại trên hệ thống.` | `Line N – PO code does not exist in the system.` | 07062#L2193-L2195 |
| ERR-PKL-003 | Validation | Import — SKU để trống | `Dòng N – SKU không được để trống.` | `Line N – SKU cannot be empty.` | 07062#L2196-L2197 |
| ERR-PKL-004 | Validation | Import — SKU không tồn tại hệ thống | `Dòng N – SKU không tồn tại trên hệ thống.` | `Line N – SKU does not exist in the system.` | 07062#L2198-L2200 |
| ERR-PKL-005 | Validation | Import — SKU không tồn tại trong PO | `Dòng N – SKU không tồn tại tronng PO` (typo `tronng` — Q-003) | `Line N – SKU does not exist in the PO.` | 07062#L2201-L2203 |
| ERR-PKL-006 | Validation | Import — Roll code để trống | `Dòng N – Mã cuộn không được để trống.` | `Line N – Roll code cannot be empty.` | 07062#L2204-L2206 |
| ERR-PKL-007 | Validation | App scan PO Packing list Waiting Approve | `PO chưa được duyệt Packing list nên không thể nhận hàng.` | (raw chỉ có VN — Q-004) | 07062#L2292-L2294 |
| ERR-PKL-008 | Validation | App scan PO chưa import packing list | `PO chưa import Packing list nên không thể nhận hàng.` | (raw chỉ có VN — Q-004) | 07062#L2295-L2297 |
| ERR-PKL-009 | Validation | Import — Batch code để trống | `Dòng N – Mã lô không được để trống.` | `Line N – Batch code cannot be empty.` | 07062#L2207-L2208 |
| MSG-PKL-010 | Confirm | Import — Tổng Qty SKU > ±5% Qty confirm PO | `PO 10012601001737, SKU 422504712 có tổng số lượng trong packing list lớn hơn ± 5% so với số lượng yêu cầu trên PO. Nếu xác nhận import thì liên hệ BOD để được duyệt trước khi nhân hàng.` (typo `nhân` → `nhận` — Q-005) | `PO 10012601001737, SKU 422504712: The total quantity in the packing list exceeds ±5% of the PO quantity. If confirming the import, please contact BOD for approval before receiving.` | 07062#L2241-L2246 |
| MSG-PKL-011 | Confirm | Inbound Approve button Waiting Approve | `Bạn có chắc chắn muốn duyệt cho nhận hàng theo packing list không?` | `Do you want to approve receiving based on the packing list?` | 07062#L2263-L2265 |
| ERR-PKL-012 | Validation | Import — Số lượng yêu cầu trống / không hợp lệ / trùng dòng | `Dòng N – Số lượng yêu cầu không được để trống.` / `Dòng N – Số lượng yêu cầu không hợp lệ` / `Dòng N – Dữ liệu đã tồn tại trên file import` | `Line N – Requested quantity cannot be empty.` / `Line N – Requested quantity is invalid.` / `Line N – Data already exists in the import file.` | 07062#L2210-L2218 |
| MSG-PKL-013 | Confirm | UID group cây vải > 10% packing list | `Số lượng thực nhận lớn hơn 10% so với Packing list, bạn có muốn xác nhận nhận hàng không?` | `The actual received quantity exceeds the packing list by more than 10%. Do you want to confirm the receipt?` | 07062#L2549-L2552 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Import valid file → auto Approved**
  - **Given:** PO `PO-A` cần nhận. Import file valid 9 rules + ±5% pass.
  - **When:** Save data.
  - **Then:** Inbound table cột Packing list PO của `PO-A` = `Approved` (R008).
- **AC-02 — Import > ±5% → Waiting for Approval**
  - **Given:** Qty packing list > ±5% Qty PO.
  - **When:** Operations click `Xác nhận Import` ở MSG-PKL-010.
  - **Then:** Save với status `Waiting for Approval` (R006).
- **AC-03 — Re-import update SL**
  - **Given:** Packing list đã có dòng `PO-A | SKU-X | Roll-1 | Batch-1 | Qty 50`.
  - **When:** Import file có cùng PO/SKU/Roll/Batch nhưng Qty = 60.
  - **Then:** Update Qty = 60 cho dòng đó (R001).
- **AC-04 — Validation rule — PO code rỗng**
  - **Given:** File có dòng 5 PO code rỗng.
  - **When:** Validate.
  - **Then:** ERR-PKL-001 với `Dòng 5` (R002).
- **AC-05 — Edit/Xoá chỉ cho PO khác Received**
  - **Given:** PO-B status `Received` đã có packing list.
  - **When:** User cố edit Qty hoặc xoá dòng.
  - **Then:** UI disable / không cho thao tác (R005).
- **AC-06 — Inbound BOD approve packing list**
  - **Given:** PO-C packing list `Waiting for Approval`.
  - **When:** BOD click Approve → confirm MSG-PKL-011 → Yes.
  - **Then:** Status chuyển `Approved` (R009).
- **AC-07 — Re-import sau Approved > ±5% → quay lại Waiting**
  - **Given:** PO-D packing list `Approved`.
  - **When:** Operations import lại file mà > ±5%.
  - **Then:** Status chuyển về `Waiting for Approval` (R010).
- **AC-08 — Update SL/Xoá sau Approved → giữ Approved**
  - **Given:** PO-D `Approved`.
  - **When:** User edit Qty hoặc xoá dòng.
  - **Then:** Status giữ `Approved` (R010).
- **AC-09 — App scan PO Waiting Approve → block**
  - **Given:** PO-E packing list `Waiting Approve`.
  - **When:** User App scan PO-E.
  - **Then:** ERR-PKL-007 block (R012).
- **AC-10 — App scan PO chưa import packing list → block**
  - **Given:** PO-F là PO vải nhưng chưa import packing list.
  - **When:** User App scan.
  - **Then:** ERR-PKL-008 block (R012).
- **AC-11 — App scan PO Approved không data → pass**
  - **Given:** PO-G packing list `Approved` không data import.
  - **When:** User App scan.
  - **Then:** Pass cho nhận (R012).
- **AC-12 — SKU vải lẻ suggest mã cuộn**
  - **Given:** Packing list có Roll-A1, Roll-A2 cho lô LOT-001.
  - **When:** User nhập số lô `LOT-001`.
  - **Then:** Hệ thống suggest danh sách {Roll-A1, Roll-A2} (R013).
- **AC-13 — SKU vải lẻ hệ số quy đổi**
  - **Given:** Hệ số x2.
  - **When:** User nhập SL thực nhận = 48 kg, nhấn `+`.
  - **Then:** SL ghi nhận = 96 pcs (R014).
- **AC-14 — SKU vải combo nhập thập phân**
  - **Given:** SKU combo vải.
  - **When:** User nhập SL thực nhận = 4.5.
  - **Then:** Pass (R016).
- **AC-15 — SKU combo total UID phải nguyên dương**
  - **Given:** Tổng SL khai báo UID = 4.5.
  - **When:** Submit.
  - **Then:** Block validate (R017).
- **AC-16 — Update 02-04-2026 Trừ lõi normal**
  - **Given:** SL thực nhận = 50, Trừ lõi = 0.5.
  - **When:** Submit.
  - **Then:** SL ghi nhận = 49.5 (R018).
- **AC-17 — Update 02-04-2026 Trừ lõi có hệ số**
  - **Given:** SL thực nhận = 50, hệ số = 2, Trừ lõi = 0.5.
  - **When:** Submit.
  - **Then:** SL ghi nhận = `50 × 2 − 0.5 = 99.5` (R018).
- **AC-18 — Update 16-04-2026 Trừ lõi tự tính**
  - **Given:** Gross qty = 15.3, Net qty = 15.
  - **When:** User mở màn khai báo UID.
  - **Then:** Trừ lõi auto = 0.3, disable edit (R024).
- **AC-19 — Update 16-04-2026 Gross = Net → Trừ lõi = 0**
  - **Given:** Gross = Net = 50.
  - **When:** User xem.
  - **Then:** Trừ lõi = 0, disable edit (R024).
- **AC-20 — Update 16-04-2026 quy đổi Yard**
  - **Given:** Width = 1.5m, GSM = 200, Weight cân = 15kg, SKU đơn vị Inside = Yard.
  - **When:** Tính SL.
  - **Then:** Yard = `(15 × 1000) / (1.5 × 200 × 0.9144)` ≈ 54.69 Yard (R025).
- **AC-21 — Update 16-04-2026 quy đổi không apply cho Kg**
  - **Given:** SKU đơn vị Inside = Kg.
  - **When:** User cân + submit.
  - **Then:** Ghi nhận theo Kg, không apply quy đổi (R025).
- **AC-22 — Update 20-04-2026 nhận dư → ADJ**
  - **Given:** PO order 105 mét, packing list 106.15, thực nhận 106.60.
  - **When:** User nhận xong.
  - **Then:** UID group ghi theo Packing list (106.15), số dư (0.45) tạo ADJ + sinh UID mới (R028, R030).
- **AC-23 — Update 20-04-2026 cảnh báo > 10% cây vải**
  - **Given:** Cây vải packing list = 10m, user nhập thực nhận = 12m (> 10%).
  - **When:** User xác nhận.
  - **Then:** MSG-PKL-013 confirm hiện (R029).
- **AC-24 — MSG-PKL-013 Kiểm tra lại tắt và giữ màn hình**
  - **Given:** MSG-PKL-013 đang hiện.
  - **When:** User click `Kiểm tra lại`.
  - **Then:** Dialog tắt, giữ nguyên màn hình khai báo (R029).
- **AC-25 — MSG-PKL-013 Xác nhận → ghi nhận**
  - **Given:** MSG-PKL-013 hiện.
  - **When:** User click `Xác nhận`.
  - **Then:** Ghi nhận vào danh sách nhận (R029).
- **AC-26 — Push Inside total < PO**
  - **Given:** PO 105 mét, total thực nhận push 100 mét.
  - **When:** Hoàn thành PO.
  - **Then:** Push 100 mét + yêu cầu điều chỉnh hoá đơn (R031).
- **AC-27 — Push Inside total > PO**
  - **Given:** PO 105 mét, total thực nhận 106.5 mét.
  - **When:** Hoàn thành.
  - **Then:** Push 105 mét theo PO + tạo ADJ cho 1.5 mét dư (R031).
- **AC-28 — ASN detail Qty received + Qty per ADJ**
  - **Given:** ASN-X có nhận dư.
  - **When:** User xem ASN detail.
  - **Then:** Cột `Qty received` = SL theo PO; `Qty per ADJ` = SL dư (R026).
- **AC-29 — Pending 12-05-2026 (Update 16-04-2026)**
  - **Given:** Update 16-04-2026 đã pending.
  - **When:** Verify production hiện tại.
  - **Then:** Delivery method/Width/GSM/Gross/Net columns chưa được dùng (R019-R023 — Q-008).
- **AC-30 — Update 29-01-2026: SKU bổ sung sau Receiving auto approved**
  - **Given:** PO đã chuyển Receiving.
  - **When:** Operations import packing list bổ sung.
  - **Then:** SKU bổ sung auto Approved (R007).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | Nguồn | Figma mockup links — node `2302-771` (UID group) + `2328-217` (ASN detail) cover hết flow nhận packing list hay chỉ 1 phần? | UX | Open | | | |
| Q-002 | R028, R031 | API push Inside + Auto-create ADJ endpoints — spec? Async? Có audit log không? | Dev | Open | | | |
| Q-003 | ERR-PKL-005 | Raw VN có typo `tronng PO` — fix thành `trong PO` ở v2.18? | PO/UX | Open | | | |
| Q-004 | ERR-PKL-007, ERR-PKL-008 | Verbatim EN cho 2 message validation App scan (raw chỉ có VN). | PO/UX | Open | | | |
| Q-005 | MSG-PKL-010 | Raw VN có typo `nhân hàng` → `nhận hàng`? Fix? | PO/UX | Open | | | |
| Q-006 | R013, R016 | "Hệ thống suggest danh sách mã cuộn" — suggest order theo gì (alphabetical / số lô / qty đầu tiên)? | UX | Open | | | |
| Q-007 | R014 | Hệ số quy đổi — default x1 vẫn là hệ số tính nhân 1, hay là "không nhân"? Khi nào hệ số khác x1 (master data SKU, hay user nhập)? | PO | Open | | | |
| Q-008 | R019-R023, AC-29 | Update 16-04-2026 Pending 12-05-2026 — bao giờ sẽ resume? Cần test scope hiện tại không bao gồm phần này? | PO | Open | | | |
| Q-009 | R024, AC-18 | Update 16-04-2026 Trừ lõi tự tính từ Gross-Net (16-04-2026) vs Trừ lõi user nhập (02-04-2026) — sau khi 16-04-2026 active, 02-04-2026 còn dùng không? | PO | Open | | | |
| Q-010 | R025 | Công thức quy đổi: `× 0.9144` cho Yard — đây là conversion constant cố định (1 yard = 0.9144 mét)? Có thể configurable? | Dev | Open | | | |
| Q-011 | R029, AC-23 | > 10% cảnh báo — tính per cây vải (1 UID) hay tổng SKU? Raw L2546-L2552 nói "từng cây vải" → confirm. | PO | Open | | | |
| Q-012 | R028 | "Số dư của 1 cuộn sinh ra 1 UID mới cùng UID group" — UID mới có status gì (Available, New)? Khi nào IT/picklist được? | PO/Dev | Open | | | |
| Q-013 | R010 | "Edit lại số lượng hay xoá bớt → status không thay đổi (do chưa thể tính toán lại, tạm thời chưa control UI)" — bao giờ control UI sẽ được fix? | PO/Dev | Open | | | |
| Q-014 | R015 | "Nếu SL thực nhận > SL packing list → ghi nhận theo packing list" (R015) vs Update 20-04-2026 ghi nhận dư + ADJ (R028) — conflict? 2 rule cho 2 case khác nhau? | PO | Open | | | |
| Q-015 | R007 | "PO Receiving + import bổ sung → SKU bổ sung auto approved" — auto approved bất kể ±5% hay vẫn validate? | PO | Open | | | |
| Q-016 | R026, R027 | `Qty per ADJ` ở ASN detail và UID group detail — số ADJ này hiển thị theo cái nào (cuộn / UID / SKU)? | PO | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-48..S-59 | 2.17 (stub) | 2.17 | All R + AC | Draft |
| CHG-002 | Add | Import packing list base + Validation 9 messages + listing edit/xoá nếu PO khác Received | (trước 2.17) | 2.17 | R001-R005 | Done |
| CHG-003 | Add | Update 29-01-2026: ±5% validate + Waiting/Approved status + Inbound listing + App scan validate | (trước 2.17) | 2.17 | R006-R012 | Done |
| CHG-004 | Add | Update 03-02-2026: rules re-import sau Approved | (trước 2.17) | 2.17 | R010 | Done |
| CHG-005 | Add | Flow nhận hàng SKU vải lẻ + combo theo packing list (suggest mã cuộn, hệ số quy đổi, format SL ghi nhận) | (trước 2.17) | 2.17 | R013-R017 | Done |
| CHG-006 | Add | Update 02-04-2026: bổ sung `Trừ lõi` | (trước 2.17) | 2.17 | R018 | Done |
| CHG-007 | Pending | Update 16-04-2026 (Pending 12-05-2026): Delivery method + Width + GSM + Gross + Net + công thức quy đổi Yard/Mét + ẩn edit SL UI | (trước 2.17) | 2.17 | R019-R025 | Pending |
| CHG-008 | Add | Update 20-04-2026: rules nhận dư + Qty per ADJ + cảnh báo > 10% + sync Inside | (trước 2.17) | 2.17 | R026-R031 | Done |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_packing_list | test_stub_receiving_po_packing_list | Add (chờ Gate 1B) | [[stub_receiving_po_fabric]] (nhận Vải UID group), [[stub_receiving_po_app]] (validate App scan), [[stub_receiving_po_inbound_shipment]] (Inbound listing), [[stub_receiving_po_date_rules]] (HSD validation), [[stub_receiving_po_po_sample]] (PO sample), Adjustment system, Inside sync | Q-001..Q-016 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R031, AC-01..AC-30 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-016. R019-R025 (16-04-2026) là Pending → cân nhắc scope test |

## 🚧 Blocked Coverage

- R028, R031 — chờ Q-002 (API endpoints)
- ERR-PKL-005 — chờ Q-003 (typo `tronng`)
- ERR-PKL-007, ERR-PKL-008 — chờ Q-004 (verbatim EN)
- MSG-PKL-010 — chờ Q-005 (typo `nhân`)
- R013, R016 — chờ Q-006 (suggest order)
- R014 — chờ Q-007 (hệ số default)
- R019-R025 — chờ Q-008, Q-009 (Pending status + reconcile với 02-04-2026)
- R025 — chờ Q-010 (constant 0.9144 configurable)
- R029 — chờ Q-011 (>10% scope cây hay SKU)
- R028 — chờ Q-012 (UID mới status)
- R010 — chờ Q-013 (control UI edit fix)
- R015 vs R028 — chờ Q-014 (conflict rule)
- R007 — chờ Q-015 (auto approved scope)
- R026, R027 — chờ Q-016 (Qty per ADJ display scope)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 22:30:00 | v1.1 | Refine stub → full spec: 31 R-ID, 30 AC, 30 BR, 13 messages (10 verbatim VN+EN, 3 missing EN — Q-004), 16 questions Open. R019-R025 marked Pending từ 12-05-2026. `partial_read: false`. | refine-batch-5-2026-05-30 |
