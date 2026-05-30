---
aliases: [stub_receiving_po_date_rules]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_date_rules
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L1070-L1496
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 21:00:00"
verification_status: Pending
approved_by:
approved_at:
approval_note:
---

# REQ: stub_receiving_po_date_rules

## Tổng quan
- **Mã tính năng:** stub_receiving_po_date_rules
- **Feature:** Rules tính ngày HSD tối thiểu + combo SKU + RFID + Xem danh sách + Khai báo thiếu + Kết thúc PO
- **Mô tả ngắn:** Bao gồm 7 mảng update lớn quanh flow nhận hàng PO trên App: (1) Rules tính HSD tối thiểu cho PO (06-01-2025) — formula `[% Allowed Shelf Life PO] * [Product's Shelf Life]`; (2) Update 02-11-2024 icon ghi chú PO + (08-01-2025) PO tester HSD ≥ 3 tháng + số lô check trùng + Serial/Imei CCDC validation 1-scan-1-qty; (3) Update 05-01-2025 button "Thay đổi vị trí nhận hàng" (chỉ Shop 170 QL1A / Kho 170 QL1A + 1 PO 1 giỏ); (4) Update 30-05-2025 SKU combo HSD; (5) Update 04-06-2025 — Step 1.1 Scan RFID (Thời trang + Synctives) + 1.2 Xoá scan + 2 Xem danh sách + 2.1-2.4 Khai báo thiếu + 3 Kết thúc nhận hàng + 4 Cập nhật chứng từ + 5 Hoàn thành PO + 17-10-2024 API receiving item; (6) 24-10-2024 SPKPH product status Damaged; (7) Update status ASN + tồn kho.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Shop, Nhân viên kho (App), Quản lý.
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[test_stub_receiving_po_date_rules]]
- **API Spec liên quan:** API receiving item PO bên Inside (`check_issue`/`issue` payload) — raw L1457-L1469.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_receiving_po_app]] (Step 1-5 flow), [[stub_receiving_po_inbound_shipment]] (PO/ASN), [[stub_receiving_po_invoice]] (Thêm hoá đơn cuối flow). ↔️ liên quan [[stub_receiving_po_vas]] (SPKPH Damaged), [[stub_receiving_po_confirm_paste_id]] (post Kết thúc PO), [[stub_receiving_po_packing_list]] (returns/Vendor return flow).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07062_Receiving_PO_Docs_ver2.17.md | 2.17 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | API receiving item PO bên Inside — case có hàng không phù hợp gửi `"check_issue":1, "issue":{"note": string, "unsuitable":{"qty": int, "media": []}}` | R030 | 07062#L1457-L1463 | TBD — Q-001 |
| N/A | API receiving item PO bên Inside — case NCC không giao lại gửi `"check_issue":1, "issue":{"note": string (bắt buộc)}` (Inside tự compare số PO vs WMS để có số thiếu) | R031 | 07062#L1464-L1469 | TBD — Q-001 |
| N/A | API đồng bộ status `Received` từ WMS → Inside khi PO hoàn thành | R035 | 07062#L1447-L1448 | TBD — Q-001 |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Update 06-01-2025 — Rules tính ngày nhận hàng tối thiểu của PO cho SKU. Thông báo cập nhật: `Hạn sử dụng nhỏ hơn yêu cầu được phép nhận hàng của PO (HSD tối thiểu [Ngày hệ thống tính toán])` | Business rule + Validation | High | ✅ | 07062#L1070-L1077 |
| R002 | Rules tính HSD tối thiểu — Formula: `[% Allowed Shelf Life PO] * [Product's Shelf Life]` → tính ra số tháng tương ứng (**không làm tròn**, vd 20.16 tháng). Từ số tháng tính được **cộng với ngày nhận hàng** để ra HSD tối thiểu có thể nhận | Business rule + Formula | High | ✅ | 07062#L1078-L1085 |
| R003 | Lưu ý HSD — khi nhận hàng nếu HSD của sản phẩm **trùng với tháng trong HSD tối thiểu thì vẫn cho nhận** (do HSD của sản phẩm sẽ tính về **ngày cuối tháng**) | Business rule + Edge case | High | ✅ | 07062#L1086-L1090 |
| R004 | Validation HSD upper bound — nếu HSD nhập vào **lớn hơn vòng đời của sản phẩm** → thông báo `Hạn sử dụng lớn hơn vòng đời được thiết lập của sản phẩm (24 tháng).` / `Expiration date is greater than the product shelf life (24 months).` | Validation | High | ✅ | 07062#L1091-L1102 |
| R005 | Update 02-11-2024 — Bổ sung **icon để xem ghi chú cho PO** | UI | High | ⚠️ | 07062#L1099-L1100 |
| R006 | Update 08-01-2025 — Nếu PO là **tester** thì tất cả SKU trong PO tester được phép nhận vào nếu **HSD của sản phẩm ≥ 3 tháng** | Business rule | High | ✅ | 07062#L1103-L1105 |
| R007 | Validation SL — nếu SL của SKU vượt SL confirm trong PO → `Số lượng của SKU 100540031 lớn hơn số lượng cần nhận trong PO.` / `The quantity of SKU 100540031 is greater than the quantity required in the PO.` (recurring validation cho cả flow normal, lô+HSD, Serial/Imei) | Validation | High | ✅ | 07062#L1106-L1114 |
| R008 | Nếu SKU yêu cầu nhập **số lô + HSD** → show popup; SL prefill từ scan SKU **cho phép chỉnh sửa**. Validate HSD tương tự R001-R004. Số lô check trùng: nếu số lô của cùng SKU đã tồn tại → `Số lô của sản phẩm đã tồn tại trên hệ thống` / `Batch code of product already exists in the system` | Validation + UI | High | ✅ | 07062#L1115-L1137 |
| R009 | Nếu SKU là **công cụ dụng cụ** (CCDC) và **config có yêu cầu nhập Serial/Imei** → show popup nhập Serial/Imei. Validate: nếu Serial/Imei của SP đã tồn tại trên hệ thống (của **cùng SKU**) → `Serial/Imei của sản phẩm đã tồn tại trên hệ thống.` / `Serial/Imei of prodcut already exists in the system.` (typo `prodcut` — Q-002) | Validation | High | ✅ | 07062#L1138-L1159 |
| R010 | Lưu ý CCDC Serial/Imei — **1 lần scan chỉ nhận SL = 1**, nếu nhập SL > 1 → thông báo (verbatim Q-003) | Business rule + Validation | High | ⚠️ | 07062#L1160-L1162 |
| R011 | Lưu ý 24-10-2024 — ở phase này với SKU yêu cầu nhập Serial/Imei thì sẽ **bypass bước nhập Serial/Imei**, chỉ cần nhập SL và date (nếu có yêu cầu). Tiếp tục scan nhận hàng cho tới khi hoàn thành | Business rule + Functional | High | ✅ | 07062#L1163-L1166 |
| R012 | Update 05-01-2025 — Bổ sung button `Thay đổi vị trí nhận hàng`. Button **chỉ hiện cho Shop 170 QL1A và Kho 170 QL1A** (kho bật config location). Khi chọn → quay về bước scan vị trí/mã giỏ cần chuyển hàng vào | UI + Business rule | High | ✅ | 07062#L1168-L1175 |
| R013 | Update 05-01-2025 — Lưu ý: các SP được scan nhận sẽ được ghi nhận vào **vị trí được scan trước đó**, tới khi có thay đổi vị trí nhận hàng mới. **1 PO chỉ được nhận vào 1 giỏ duy nhất** để đi push hàng về kệ, không được nhận vào nhiều giỏ khác nhau (do 1 user/1 thời điểm chỉ giữ 1 giỏ duy nhất) | Business rule | High | ✅ | 07062#L1176-L1181 |
| R014 | Update 30-05-2025 — Khi nhận PO nếu là **SKU combo**, check: (a) Combo required date + chỉ 1 con lẻ required date → show popup user nhập theo SKU lẻ; (b) Combo không required date thì không yêu cầu nhập date (cho dù SKU lẻ có required date → **lỗi data**); (c) Combo required date + có **từ 2 con lẻ** required date → show popup user input date cho từng con lẻ (SL con lẻ lấy theo SL của combo) | Business rule + Validation | High | ✅ | 07062#L1182-L1190 |
| R015 | Update 04-06-2025 — **Không quan tâm tới con combo có required date hay không**, chỉ cần có con lẻ có required date → show popup cho user nhập date cho con lẻ. Nếu combo required date mà con lẻ không required date → vẫn show popup nhập date cho combo (vẫn thông tin SKU lẻ để check) | Business rule | High | ✅ | 07062#L1192-L1203 |
| R016 | Step 1.1 — Scan nhận SKU có RFID. Nếu PO có SKU thoả điều kiện: `Category = Thời trang` + `Brand = Synctives` + SKU có yêu cầu RFID → **scan RFID khi nhận hàng**, không khai báo ở bước VAS, khi này sẽ **auto VAS** | Business rule + Functional | High | ✅ | 07062#L1208-L1212 |
| R017 | Step 1.2 — Xoá SP vừa scan nhận hàng (case khai báo sai HSD/Batch code/Serial). SP có HSD + batch code: nếu xoá → **xoá hết tất cả SL đã scan nhận của phiên** đang nhận để scan lại. Confirm dialog `Do you want to delete SKU 253900004 from the receiving session? (This will delete all scanned quantities in the current receiving session)` | Functional + Confirm | High | ✅ | 07062#L1216-L1224 |
| R018 | Step 1.2 — SP có Serial/Imei: nếu cần xoá → chọn **xoá Serial nhận sai** để scan lại. Confirm dialog `Do you want to delete serial 2UA49P120 of SKU 253900004 from the receiving session?` | Functional + Confirm | High | ✅ | 07062#L1225-L1232 |
| R019 | Step 2 — Xem danh sách SKU đã nhận trong PO. User chọn `+` → `Danh sách sản phẩm` để xem. **Nếu chỉ có 1 PO thì không cần chọn PO cần xem**. Thông tin 2 tab: `Đã nhận đủ` + `Chưa nhận đủ`. Thông tin SP: Tên SP, SKU, Barcode, **Vị trí nhận hàng** (chỉ hiện cho Shop 170 QL1A và Kho 170 QL1A, và chỉ cho SKU đã có SL scan nhận), SL đã scan nhận/SL cần nhận. Chọn `Chi tiết` xem thông tin HSD hay Serial/Imei đã nhận | UI + Filter | High | ✅ | 07062#L1233-L1256 |
| R020 | Step 2.1 — Xem phiên nhận hàng trong PO. User chọn `+` → `Phiên nhận hàng` để xem thông tin chi tiết của phiên đang/đã nhận. User chọn phiên để xem thông tin chi tiết | UI + Functional | High | ✅ | 07062#L1257-L1264 |
| R021 | Step 2.2 — Khai báo sản phẩm thiếu & không phù hợp. Với SP đang nhận hàng **chưa đủ số lượng**, có thêm button để khai báo SL hàng thiếu hoặc không phù hợp. User cũng có thể chọn nhiều SP chưa nhận đủ → dấu `+` ở góc trái hiện lên → `Khai báo lý do thiếu hàng` để khai nhiều SP cùng lúc | UI + Functional | High | ✅ | 07062#L1268-L1287 |
| R022 | Step 2.2 — Form `Khai báo theo sản phẩm`. Field: `Tên sản phẩm`, `SKU`, `Barcode`, `Số lượng thiếu` (Qty missing — auto prefill SL chưa nhận theo PO, cho user chỉnh sửa; bắt buộc; trống → `Vui lòng nhập số lượng thiếu`), `Lý do thiếu` (Reason for missing — bắt buộc), `Ghi chú` (Note), `Hình ảnh sản phẩm` (Product Image) | Validation + UI | High | ✅ | 07062#L1268-L1300 |
| R023 | Step 2.2 — `Lý do thiếu` enum giá trị: `Giao thiếu hàng` (bổ sung `Nhà cung cấp giao bù`: Yes/No), `Sản phẩm không phù hợp` (bổ sung `Tình trạng hàng hoá`: `Hư hỏng`/`Cận date`/`Hết date`/`Khác`; `Hạn sử dụng` format `YYYY-MM`) | Enum + Validation | High | ✅ | 07062#L1306-L1320 |
| R024 | Step 2.2 — `Hình ảnh sản phẩm`: nếu là **SPKPH** thì yêu cầu chụp hình → chọn `+` mở camera. Nếu **thiếu hàng** thì không cần chụp hình. Sau khi cập nhật thành công thì button chuyển **xanh lá cây**. User chọn button để **xem lại** thông tin đã khai báo | Business rule + UI | High | ✅ | 07062#L1321-L1334 |
| R025 | Step 2.2 — Khai báo nhiều SP cùng lúc / Xoá thông tin đã khai báo. Nếu muốn xoá thông tin đã khai báo → chọn nút `Xoá` → confirm `Do you want to delete the "Declare reason for missing" of SKU 253900004?` | Functional + Confirm | High | ✅ | 07062#L1333-L1338 |
| R026 | Step 2.3 — Khai báo thiếu hàng cho tất cả sản phẩm. Tại màn hình danh sách SP, bổ sung action `Khai báo thiếu hàng cho tất cả sản phẩm` để user khai báo nhanh. Thông tin: `Số lượng SKU` (tổng SKU chưa nhận đủ), `Số lượng sản phẩm` (tổng SP chưa nhận đủ), `Lý do thiếu hàng` (default = `Giao thiếu hàng`, **disable không cho edit**), `Nhà cung cấp giao bù` (default = `Có`, cho edit) | Functional + UI + Validation | High | ✅ | 07062#L1339-L1352 |
| R027 | Step 2.3 — Chọn `Yes` → cập nhật lý do thiếu hàng cho **tất cả SP trong danh sách chưa nhận đủ** theo SL tương ứng. Nếu user chọn `Xoá tất cả` → xoá tất cả khai báo thiếu hàng cho tất cả SKU chưa nhận đủ đã khai báo trước đó | Functional | High | ✅ | 07062#L1353-L1358 |
| R028 | Step 2.4 — Xoá sản phẩm đã scan nhận. Vào `Danh sách sản phẩm` → chọn `Chi tiết` → `Xoá sản phẩm`. **Khi xác nhận Xoá hệ thống sẽ xoá tất cả SL đã scan nhận trước đó, bao gồm cả thông tin khai báo thiếu hàng (nếu có)** | Functional + Business rule | High | ✅ | 07062#L1363-L1367 |
| R029 | Step 3 — Kết thúc nhận hàng. Sau khi user nhận hết hàng từ NCC: (a) Nếu SL thực nhận **chưa đủ** theo SL PO → user phải khai báo lý thiếu hàng cho các SKU chưa nhận đủ → button `Kết thúc nhận hàng` hiện. (b) Nếu **nhận đủ** → user chọn `Kết thúc nhận hàng` → chuyển màn tiếp theo. **Lưu ý: khi này mới gọi API để update PO trên Inside thành `Receiving`** | Functional + State + API | High | ✅ | 07062#L1368-L1380 |
| R030 | Bổ sung 17-10-2024 — Khi gọi API receiving item PO bên Inside: trường hợp **có hàng không phù hợp** thì gửi thêm payload `"check_issue":1, "issue":{"note": string (nếu có), "unsuitable":{"qty": số lượng SP không phù hợp, "media": []string (nếu có)}}` | API contract | High | ✅ | 07062#L1457-L1463 |
| R031 | Bổ sung 17-10-2024 — Khi gọi API receiving item PO: trường hợp **SL item của SKU không đủ và NCC không giao lại** → gửi thêm `"check_issue":1, "issue":{"note": string (bắt buộc)}`. Inside sẽ tự compare số trên PO và số đã nhận từ WMS để có được số thiếu | API contract | High | ✅ | 07062#L1464-L1469 |
| R032 | Step 4 — Cập nhật hình ảnh chứng từ cho PO. User chọn `Thêm biên bản giao hàng` để cập nhật hình ảnh chứng từ. Field: `Hoàn thành PO`, `Thêm biên bản giao hàng`, `Kho`, `Tổng tiền`, `Không đồng kiểm / Đồng kiểm`, `Vị trí`, `Tổng SKU`, `Tổng sản phẩm`, `Ghi chú`, `Hình ảnh chứng từ` | UI + Functional | High | ✅ | 07062#L1381-L1395 |
| R033 | Step 4 — Loại biên bản: PO **có đồng kiểm** → chụp `biên bản giao nhận hàng hoá`; PO **không đồng kiểm** (raw có typo `kiếm` → Q-004) → chụp `biên bản bàn giao kiện hàng`. Cập nhật ghi chú (nếu có) → chọn `+` mở camera chụp hình. Max 2 hình. Chọn `Xoá hình` để xoá hình chụp lại. Sau khi cập nhật → chọn `Lưu` | Functional + UI | High | ✅ | 07062#L1383-L1395 |
| R034 | Step 5 — Hoàn thành PO. User chọn `Hoàn thành PO`. Button **chỉ hiện** khi: (a) SL SP đã scan nhận đủ theo PO (bao gồm case có hàng không phù hợp); (b) PO đã cập nhật hình ảnh chứng từ giao hàng; HOẶC SL nhận chưa đủ nhưng user đã khai báo tất cả SP thiếu và NCC không giao bù. Nếu PO cần thêm hoá đơn → phải thêm đầy đủ thông tin hoá đơn | Business rule + Functional | High | ✅ | 07062#L1397-L1416 |
| R035 | Step 5 — Phân biệt button `Hoàn thành PO` vs `Hoàn thành phiên nhận hàng`. Nút `Hoàn thành PO` show khi: đã add biên bản giao hàng + đã nhận đủ SL theo PO (hoặc nếu nhận thiếu thì tất cả SL thiếu đều có cùng reason `Nhà cung cấp giao bù = No`). Nút `Hoàn thành phiên nhận hàng` show khi: đã add biên bản giao hàng + điều kiện còn lại ngược lại với `Hoàn thành PO` (cho phép nhận thiếu theo PO nhưng phải nhận đủ SL của SKU trong PO) | Business rule + UI | High | ✅ | 07062#L1419-L1430 |
| R036 | Step 5 — Validation: nếu PO chưa cập nhật hình ảnh biên bản giao hàng → thông báo `Please update the delivery document image.` (raw chỉ có EN, raw có cảnh báo "Nếu chưa nhận đủ SL của 1 SKU trong PO, hiện cảnh báo" — Q-005) | Validation | High | ✅ | 07062#L1419-L1434 |
| R037 | Step 5 — Nếu chọn `Hoàn thành PO` → hiện thông báo xác nhận `Do you want to confirm completion of PO 10012402010027?`. Chọn `No` để tắt; chọn `Yes` để xác nhận → (a) Cập nhật status PO = `Received`; (b) Cập nhật status ASN tương ứng = `Received`; (c) Update tồn kho tương ứng; (d) **Gọi API đồng bộ status `Received` lên Inside** | Functional + State transition + API | High | ✅ | 07062#L1435-L1448 |
| R038 | Step 5 — Hoàn thành PO update thêm PO config: nếu **nhận thiếu số lượng** → update PO config = `Waiting Adj Invoice`; nếu **nhận có item SP không phù hợp** → update PO config = `Receiving Issue` | Business rule + State | High | ✅ | 07062#L1449-L1456 |
| R039 | Bổ sung 24-10-2024 — Khi kết thúc phiên nhận hàng hoặc Hoàn thành PO mà có khai báo SPKPH thì **vẫn import stock và update UID có product status = `Damaged`**. Nếu có tạo lệnh vendor return thì dựa vào PO source để lấy đúng UID có product status = `Damaged` để Out ra | Business rule + State transition | High | ✅ | 07062#L1473-L1479 |
| R040 | User chọn button `Hoàn thành phiên nhận hàng` — nếu chưa nhận đủ SL theo PO → thông báo xác nhận. Chọn `Đóng` để tắt; chọn `Xác nhận` để xác nhận hoàn thành phiên: (a) Update status ASN (phiên nhận hàng) tương ứng = `Received`; (b) Update tồn kho tương ứng với SL thực nhận theo phiên nhận hàng | Functional + State transition | High | ✅ | 07062#L1480-L1495 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User đã login App và scan PO valid (xem [[stub_receiving_po_app]]).
- PO config có `% Allowed Shelf Life PO` cho SKU yêu cầu HSD.

### Luồng chuẩn (Happy Path) — Nhận SKU có HSD + Validate HSD tối thiểu
1. User scan SKU `SP-A` yêu cầu HSD → popup nhập HSD mở (R008).
2. Hệ thống tính HSD tối thiểu = `[% Allowed × Product's Shelf Life]` tháng + ngày nhận (R002).
3. Ví dụ: `% Allowed = 80%`, `Product's Shelf Life = 24 tháng` → HSD tối thiểu = 19.2 tháng (không làm tròn) (R002).
4. User nhập HSD `2026-09-30` (cùng tháng HSD tối thiểu) → pass do HSD tính về ngày cuối tháng (R003).
5. User nhập HSD `2026-08-15` (< HSD tối thiểu) → ERR-DTR-001 (R001).
6. User nhập HSD `2030-12-31` (> vòng đời) → ERR-DTR-002 (R004).

### Luồng chuẩn (Happy Path) — PO tester HSD ≥ 3 tháng
1. PO type `tester`, SKU `SP-B` HSD = 4 tháng (3 ≤ 4 tháng).
2. User scan + nhập HSD → pass (R006).
3. PO không tester, cùng SKU, HSD < HSD tối thiểu → block.

### Luồng chuẩn (Happy Path) — Nhận SKU có lô + HSD
1. User scan `SP-C` yêu cầu số lô + HSD → popup mở (R008).
2. User nhập số lô `LOT-001`, HSD valid.
3. Nếu `LOT-001` đã tồn tại trên hệ thống cho cùng SKU → ERR-DTR-003 (R008).

### Luồng chuẩn (Happy Path) — Nhận SKU CCDC có Serial/Imei
1. User scan `SP-D` CCDC config Serial → popup nhập Serial (R009).
2. Validate: Serial `SR-001` chưa tồn tại cho SKU → add (R009).
3. Validate: 1 scan chỉ nhận SL = 1; nếu nhập SL = 5 → thông báo (R010).
4. Lưu ý 24-10-2024: ở phase này bypass nhập Serial/Imei, chỉ nhập SL + date (R011).

### Luồng chuẩn (Happy Path) — SKU combo HSD (Update 30-05-2025 + 04-06-2025)
1. User scan SKU combo `COMBO-A` chứa SP lẻ `SP-1` (required date) + `SP-2` (required date).
2. Update 30-05-2025: nếu combo required date + chỉ 1 con lẻ required date → popup theo SKU lẻ (R014).
3. Update 04-06-2025: bất kể combo required hay không, chỉ cần con lẻ required → popup nhập date cho con lẻ (R015).
4. Combo không required + SP lẻ required → **lỗi data** (R014).

### Luồng chuẩn (Happy Path) — Step 1.1 RFID Thời trang + Synctives
1. PO có SKU `SP-T` Category `Thời trang` + Brand `Synctives` + required RFID.
2. User scan RFID khi nhận hàng (R016).
3. Hệ thống auto VAS — không cần khai báo ở bước VAS sau (R016).

### Luồng chuẩn (Happy Path) — Step 1.2 Xoá scan
1. User scan nhập sai HSD cho `SKU 253900004` → chọn `Xoá` (R017).
2. Confirm `Do you want to delete SKU 253900004 from the receiving session?` → Yes → xoá hết SL của SKU đã scan trong phiên.
3. Trường hợp Serial: chọn xoá Serial `2UA49P120` → confirm (R018).

### Luồng chuẩn (Happy Path) — Step 2-2.4 Khai báo thiếu
1. User vào `Danh sách sản phẩm` xem 2 tab: Đã nhận đủ / Chưa nhận đủ (R019).
2. Vị trí nhận hàng chỉ hiện cho Shop/Kho 170 QL1A và chỉ SKU đã scan (R019).
3. Step 2.2: chọn SP chưa nhận đủ → form `Khai báo theo sản phẩm` (R021, R022).
4. Lý do thiếu = `Giao thiếu hàng` → `Nhà cung cấp giao bù = No`; `Sản phẩm không phù hợp` → `Tình trạng = Hư hỏng/Cận date/Hết date/Khác` + `Hạn sử dụng YYYY-MM` (R023).
5. SPKPH yêu cầu chụp hình; thiếu hàng không cần (R024).
6. Submit thành công → button xanh lá cây (R024).
7. Step 2.3: `Khai báo thiếu hàng cho tất cả sản phẩm` → mặc định `Giao thiếu hàng` disable + `Nhà cung cấp giao bù = Có` (R026, R027).

### Luồng chuẩn (Happy Path) — Step 3 Kết thúc nhận hàng
1. SL thực nhận = SL PO → button `Kết thúc nhận hàng` hiện (R029).
2. User click → API update PO trên Inside thành `Receiving` (R029).
3. Có hàng không phù hợp: API payload thêm `check_issue`/`unsuitable` (R030).
4. NCC không giao lại: API payload thêm `check_issue`/`note` (R031).

### Luồng chuẩn (Happy Path) — Step 4 Cập nhật chứng từ
1. User chọn `Thêm biên bản giao hàng` (R032).
2. PO đồng kiểm: chụp `biên bản giao nhận hàng hoá`; không đồng kiểm: `biên bản bàn giao kiện hàng` (R033).
3. Max 2 hình; có nút Xoá hình (R033).

### Luồng chuẩn (Happy Path) — Step 5 Hoàn thành PO
1. Button `Hoàn thành PO` show khi đủ điều kiện (R034, R035).
2. User click → confirm dialog `Do you want to confirm completion of PO 10012402010027?` → Yes (R037).
3. (a) PO status `Received`; (b) ASN status `Received`; (c) Update tồn kho; (d) Sync status Inside (R037).
4. Nhận thiếu → PO config `Waiting Adj Invoice`; có SP không phù hợp → `Receiving Issue` (R038).
5. SPKPH (24-10-2024): vẫn import stock + UID status `Damaged`; vendor return dùng UID Damaged (R039).

### Luồng chuẩn (Happy Path) — Hoàn thành phiên nhận hàng
1. Nhận chưa đủ + chưa khai báo `NCC giao bù = No` cho tất cả thiếu → button `Hoàn thành phiên nhận hàng` show (R035).
2. User click → confirm xác nhận → ASN status `Received` + update tồn kho theo phiên (R040).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — Update 05-01-2025 button "Thay đổi vị trí":** chỉ cho Shop/Kho 170 QL1A; 1 PO 1 giỏ duy nhất (R012, R013).
- **A2 — 1 PO 2 giỏ:** block (R013).
- **A3 — Khai báo nhiều SP cùng lúc:** dấu `+` góc trái → form nhiều SP (R021, R025).
- **A4 — Xoá khai báo thiếu hàng:** confirm dialog cho từng SKU hoặc Xoá tất cả (R025, R027).
- **A5 — Xoá SP đã scan (Step 2.4):** confirm → xoá tất cả SL + khai báo thiếu liên quan (R028).

### Luồng ngoại lệ (Exception Paths)
- **E1 — HSD < HSD tối thiểu:** ERR-DTR-001 (R001).
- **E2 — HSD > vòng đời:** ERR-DTR-002 (R004).
- **E3 — Số lô đã tồn tại:** ERR-DTR-003 (R008).
- **E4 — Serial/Imei đã tồn tại:** ERR-DTR-004 (R009).
- **E5 — CCDC Serial scan SL > 1:** thông báo block (R010).
- **E6 — SL SKU > confirm PO:** ERR-DTR-005 (R007).
- **E7 — SKU combo data lỗi (combo không required + lẻ required):** lỗi data (R014).
- **E8 — Chưa cập nhật biên bản giao hàng → cố Hoàn thành:** `Please update the delivery document image.` (R036).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| HSD tối thiểu | formula | ✅ | `% Allowed Shelf Life PO × Product's Shelf Life` (không làm tròn) + ngày nhận = HSD tối thiểu |
| HSD edge case ngày cuối tháng | rule | ✅ | HSD trùng tháng HSD tối thiểu = pass (HSD tính ngày cuối tháng) |
| HSD upper bound | rule | ✅ | HSD ≤ vòng đời SP (default 24 tháng — Q-006 configurable?) |
| Icon ghi chú PO | UI | ✅ | Bổ sung icon (Update 02-11-2024) — Q-007 |
| PO tester HSD min | rule | ✅ | PO `tester` cho phép HSD ≥ 3 tháng |
| SL vs confirm | rule | ✅ | SL ≤ SL confirm trong PO |
| Số lô check trùng | rule | ✅ | Số lô của cùng SKU không trùng trên hệ thống |
| CCDC Serial/Imei check trùng | rule | ✅ | Cùng SKU không trùng Serial/Imei |
| CCDC Serial 1 scan = 1 qty | rule | ✅ | SL > 1 → block |
| Bypass Serial/Imei nhập 24-10-2024 | rule | ✅ | Phase này bypass nhập Serial/Imei, chỉ nhập SL + date |
| Button "Thay đổi vị trí" | rule | ✅ | Chỉ Shop 170 QL1A + Kho 170 QL1A (bật config location) |
| 1 PO 1 giỏ | rule | ✅ | 1 user 1 thời điểm 1 giỏ |
| SKU combo HSD (30-05-2025) | rule | ✅ | Combo required + 1 lẻ required → popup lẻ; combo không required + lẻ required → lỗi data; combo required + ≥ 2 lẻ required → popup cho từng lẻ |
| SKU combo HSD (04-06-2025) — override | rule | ✅ | Chỉ cần con lẻ required date → popup; combo required + lẻ không required → vẫn popup combo |
| RFID Thời trang Synctives | rule | ✅ | Cate Thời trang + Brand Synctives + required RFID → scan RFID khi nhận, auto VAS |
| Xoá SP có lô/HSD | rule | ✅ | Xoá tất cả SL đã scan của SKU trong phiên |
| Xoá Serial | rule | ✅ | Chỉ xoá Serial đó để scan lại |
| Vị trí nhận hàng listing | rule | ✅ | Chỉ Shop/Kho 170 QL1A + chỉ SKU đã scan |
| Lý do thiếu enum | enum | ✅ | {`Giao thiếu hàng`, `Sản phẩm không phù hợp`} + sub-fields |
| `Tình trạng hàng hoá` enum | enum | ✅ | {`Hư hỏng`, `Cận date`, `Hết date`, `Khác`} |
| Hình ảnh SP thiếu/SPKPH | rule | ✅ | SPKPH bắt buộc chụp hình; Thiếu hàng không cần |
| Khai báo tất cả thiếu | rule | ✅ | Default `Lý do = Giao thiếu hàng` disable; `NCC giao bù = Có` editable |
| Xoá SP đã scan (Step 2.4) | rule | ✅ | Xoá tất cả SL + khai báo thiếu liên quan |
| Kết thúc nhận hàng | rule | ✅ | Chưa đủ SL → phải khai báo lý do thiếu trước khi button show; gọi API update Inside `Receiving` |
| API check_issue (17-10-2024) | rule | ✅ | unsuitable: `qty` + `media`; thiếu hàng: `note` bắt buộc (Inside auto compare) |
| Biên bản đồng kiểm | rule | ✅ | Đồng kiểm: biên bản giao nhận hàng hoá; Không đồng kiểm: biên bản bàn giao kiện hàng |
| Hoàn thành PO conditions | rule | ✅ | (a) SL đủ + biên bản; HOẶC (b) chưa đủ + khai báo tất cả thiếu NCC không giao bù; + hoá đơn nếu cần |
| Hoàn thành PO vs phiên | rule | ✅ | `PO` = đủ SL hoặc tất cả thiếu = NCC không giao bù; `Phiên` = ngược lại |
| PO config Receiving Issue | rule | ✅ | Có item không phù hợp → `Receiving Issue` |
| PO config Waiting Adj Invoice | rule | ✅ | Nhận thiếu → `Waiting Adj Invoice` |
| SPKPH 24-10-2024 | rule | ✅ | Import stock + UID `Damaged`; vendor return dùng UID Damaged |
| Hoàn thành phiên nhận hàng | rule | ✅ | Update ASN status `Received` + tồn kho theo phiên |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-DTR-001 | Validation | HSD < HSD tối thiểu của PO | `Hạn sử dụng nhỏ hơn yêu cầu được phép nhận hàng của PO (HSD tối thiểu [Ngày hệ thống tính toán])` | (raw không có EN — Q-005) | 07062#L1074-L1077 |
| ERR-DTR-002 | Validation | HSD > vòng đời SP (default 24 tháng) | `Hạn sử dụng lớn hơn vòng đời được thiết lập của sản phẩm (24 tháng).` | `Expiration date is greater than the product shelf life (24 months).` | 07062#L1096-L1102 |
| ERR-DTR-003 | Validation | Số lô của cùng SKU đã tồn tại trên hệ thống | `Số lô của sản phẩm đã tồn tại trên hệ thống` | `Batch code of product already exists in the system` | 07062#L1123-L1128 |
| ERR-DTR-004 | Validation | Serial/Imei của cùng SKU đã tồn tại | `Serial/Imei của sản phẩm đã tồn tại trên hệ thống.` | `Serial/Imei of prodcut already exists in the system.` (typo `prodcut` — Q-002) | 07062#L1143-L1150 |
| ERR-DTR-005 | Validation | SL SKU > SL confirm trong PO | `Số lượng của SKU 100540031 lớn hơn số lượng cần nhận trong PO.` | `The quantity of SKU 100540031 is greater than the quantity required in the PO.` | 07062#L1106-L1114 |
| MSG-DTR-006 | Validation | CCDC Serial scan SL > 1 | (raw không có verbatim — Q-003) | (raw không có verbatim — Q-003) | 07062#L1160-L1162 |
| MSG-DTR-007 | Validation | Số lượng thiếu trống (Step 2.2) | `Vui lòng nhập số lượng thiếu` | (raw không có EN — Q-005) | 07062#L1298-L1300 |
| MSG-DTR-008 | Confirm | Xoá SKU khỏi phiên nhận (lô/HSD) | (raw chỉ có EN) | `Do you want to delete SKU 253900004 from the receiving session? (This will delete all scanned quantities in the current receiving session)` | 07062#L1221-L1224 |
| MSG-DTR-009 | Confirm | Xoá Serial của SKU khỏi phiên nhận | (raw chỉ có EN) | `Do you want to delete serial 2UA49P120 of SKU 253900004 from the receiving session?` | 07062#L1231-L1232 |
| MSG-DTR-010 | Confirm | Xoá khai báo thiếu hàng của SKU | (raw chỉ có EN) | `Do you want to delete the "Declare reason for missing" of SKU 253900004?` | 07062#L1337-L1338 |
| MSG-DTR-011 | Validation | Chưa cập nhật biên bản giao hàng (Step 5) | (raw không có VN — Q-005) | `Please update the delivery document image.` | 07062#L1433-L1434 |
| MSG-DTR-012 | Confirm | Hoàn thành PO (Step 5) | (raw chỉ có EN) | `Do you want to confirm completion of PO 10012402010027?` | 07062#L1439-L1440 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — HSD pass khi cùng tháng HSD tối thiểu**
  - **Given:** PO có `% Allowed = 80%`, `Product's Shelf Life = 24 tháng`. Ngày nhận `2026-05-30`. HSD tối thiểu = 19.2 tháng cộng `2026-05-30` ≈ `2027-12-30`.
  - **When:** User nhập HSD = `2027-12-31` (cùng tháng).
  - **Then:** Pass (do HSD tính ngày cuối tháng) (R002, R003).
- **AC-02 — HSD fail khi < HSD tối thiểu**
  - **Given:** HSD tối thiểu = `2027-12-30`. User nhập `2027-08-15`.
  - **When:** Validate.
  - **Then:** ERR-DTR-001 (R001).
- **AC-03 — HSD fail khi > vòng đời**
  - **Given:** Vòng đời SP = 24 tháng. User nhập HSD = `2030-12-31`.
  - **When:** Validate.
  - **Then:** ERR-DTR-002 (R004).
- **AC-04 — PO tester HSD ≥ 3 tháng pass**
  - **Given:** PO type `tester`. SP HSD còn 3 tháng.
  - **When:** User nhập HSD.
  - **Then:** Pass (R006).
- **AC-05 — Số lô trùng SKU**
  - **Given:** SKU `SP-C` đã có lô `LOT-001` trên hệ thống.
  - **When:** User nhập lô `LOT-001` lần 2.
  - **Then:** ERR-DTR-003 (R008).
- **AC-06 — CCDC Serial trùng SKU**
  - **Given:** SKU CCDC `SP-D` đã có Serial `SR-001`.
  - **When:** User nhập Serial `SR-001`.
  - **Then:** ERR-DTR-004 (R009).
- **AC-07 — CCDC scan SL > 1**
  - **Given:** SKU CCDC required Serial.
  - **When:** User nhập SL = 5 cho 1 lần scan.
  - **Then:** MSG-DTR-006 block (R010).
- **AC-08 — Bypass Serial 24-10-2024**
  - **Given:** Phase này bypass Serial/Imei.
  - **When:** User scan SKU yêu cầu Serial.
  - **Then:** Chỉ cần nhập SL + date, không cần Serial (R011).
- **AC-09 — Update 05-01-2025: Button "Thay đổi vị trí" Shop 170 QL1A**
  - **Given:** User ở Shop 170 QL1A.
  - **When:** User mở flow scan.
  - **Then:** Button hiện; click → quay về scan vị trí (R012).
- **AC-10 — 1 PO 2 giỏ block**
  - **Given:** PO đã nhận vào giỏ G1.
  - **When:** User cố nhận tiếp vào giỏ G2.
  - **Then:** Block (R013).
- **AC-11 — Update 30-05-2025: Combo 1 lẻ required**
  - **Given:** Combo `COMBO-A` required date, chỉ `SP-1` lẻ required date.
  - **When:** User scan combo.
  - **Then:** Popup nhập theo `SP-1` (R014).
- **AC-12 — Update 04-06-2025: combo không required + lẻ required**
  - **Given:** Combo `COMBO-B` không required, `SP-1` lẻ required.
  - **When:** User scan combo.
  - **Then:** Popup nhập date cho `SP-1` (R015).
- **AC-13 — Update 04-06-2025: combo required + lẻ không required**
  - **Given:** Combo `COMBO-C` required, lẻ không required.
  - **When:** User scan combo.
  - **Then:** Popup nhập date cho combo (R015).
- **AC-14 — Step 1.1 RFID Thời trang Synctives auto VAS**
  - **Given:** PO có SKU Thời trang + Synctives + required RFID.
  - **When:** User scan RFID.
  - **Then:** Auto VAS, không cần khai báo VAS sau (R016).
- **AC-15 — Step 1.2 Xoá scan SKU có lô/HSD**
  - **Given:** User scan nhập sai lô `LOT-001` cho SKU `253900004`.
  - **When:** User click Xoá → confirm MSG-DTR-008 → Yes.
  - **Then:** Xoá tất cả SL của SKU `253900004` đã scan trong phiên (R017).
- **AC-16 — Step 1.2 Xoá Serial**
  - **Given:** Serial `2UA49P120` của SKU `253900004` đã scan.
  - **When:** User chọn xoá Serial → confirm MSG-DTR-009 → Yes.
  - **Then:** Xoá riêng Serial này (R018).
- **AC-17 — Step 2 Danh sách 1 PO không cần chọn**
  - **Given:** Flow chỉ có 1 PO.
  - **When:** User vào `Danh sách sản phẩm`.
  - **Then:** Hiển thị thẳng SP của PO, không yêu cầu chọn PO (R019).
- **AC-18 — Step 2.2 Số lượng thiếu auto prefill + chỉnh sửa**
  - **Given:** SKU chưa nhận đủ 3/10.
  - **When:** Form khai báo thiếu mở.
  - **Then:** Số lượng thiếu prefill = 7 (SL chưa nhận); user có thể edit (R022).
- **AC-19 — Số lượng thiếu để trống → MSG-DTR-007**
  - **Given:** Form mở.
  - **When:** User bỏ trống và submit.
  - **Then:** Block, MSG-DTR-007 (R022).
- **AC-20 — Lý do thiếu = Giao thiếu hàng + NCC giao bù**
  - **Given:** User chọn `Giao thiếu hàng`.
  - **When:** Field NCC giao bù hiện.
  - **Then:** User chọn Yes/No (R023).
- **AC-21 — Lý do thiếu = Sản phẩm không phù hợp + Tình trạng**
  - **Given:** User chọn `Sản phẩm không phù hợp`.
  - **When:** Field Tình trạng + HSD hiện.
  - **Then:** Tình trạng ∈ {`Hư hỏng`, `Cận date`, `Hết date`, `Khác`}; HSD format `YYYY-MM` (R023).
- **AC-22 — SPKPH bắt buộc chụp hình; thiếu hàng không cần**
  - **Given:** SP = SPKPH.
  - **When:** Form khai báo mở.
  - **Then:** Bắt buộc chụp hình. Khi thiếu hàng → không yêu cầu hình (R024).
- **AC-23 — Khai báo thành công → button xanh lá**
  - **Given:** User khai báo đầy đủ.
  - **When:** Submit.
  - **Then:** Button chuyển xanh lá (R024).
- **AC-24 — Step 2.3 Khai báo thiếu cho tất cả SP**
  - **Given:** PO có 5 SKU chưa đủ.
  - **When:** User chọn `Khai báo thiếu hàng cho tất cả sản phẩm` → Yes.
  - **Then:** Tất cả 5 SKU có khai báo thiếu với reason `Giao thiếu hàng` + NCC giao bù = Có (R026, R027).
- **AC-25 — Step 2.4 Xoá SP đã scan**
  - **Given:** SKU `SP-A` đã scan 5/10, có khai báo thiếu 5.
  - **When:** User vào Chi tiết → Xoá sản phẩm → confirm.
  - **Then:** Xoá hết 5 SL đã scan + xoá khai báo thiếu (R028).
- **AC-26 — Step 3 Kết thúc nhận hàng → API Inside Receiving**
  - **Given:** User nhận đủ SL theo PO.
  - **When:** User click `Kết thúc nhận hàng`.
  - **Then:** Hệ thống gọi API update PO Inside thành `Receiving` (R029).
- **AC-27 — 17-10-2024 API payload unsuitable**
  - **Given:** PO có 3 SP không phù hợp.
  - **When:** Hoàn thành.
  - **Then:** API gửi payload `check_issue:1, issue: {unsuitable: {qty: 3, media: [...]}}` (R030).
- **AC-28 — 17-10-2024 API payload missing**
  - **Given:** PO có SKU thiếu, NCC không giao lại.
  - **When:** Hoàn thành.
  - **Then:** API gửi payload `check_issue:1, issue: {note: "..."}`; Inside auto compare (R031).
- **AC-29 — Step 4 PO đồng kiểm chụp biên bản giao nhận**
  - **Given:** PO có đồng kiểm.
  - **When:** User chụp biên bản.
  - **Then:** Label `biên bản giao nhận hàng hoá` (R033).
- **AC-30 — Step 4 PO không đồng kiểm chụp biên bản bàn giao**
  - **Given:** PO không đồng kiểm.
  - **When:** User chụp.
  - **Then:** Label `biên bản bàn giao kiện hàng` (R033).
- **AC-31 — Step 4 max 2 hình**
  - **Given:** User chụp 2 hình.
  - **When:** Cố chụp thêm.
  - **Then:** Block (R033).
- **AC-32 — Step 5 Hoàn thành PO button show khi đủ điều kiện**
  - **Given:** SL đủ + biên bản đã add + hoá đơn (nếu yêu cầu) đầy đủ.
  - **When:** User xem màn hình.
  - **Then:** Button `Hoàn thành PO` show (R034, R035).
- **AC-33 — Step 5 Hoàn thành PO button không show khi chưa add biên bản**
  - **Given:** SL đủ nhưng chưa add biên bản.
  - **When:** User cố Hoàn thành.
  - **Then:** Button không show; nếu trigger error → MSG-DTR-011 (R036).
- **AC-34 — Step 5 Confirm + chuyển status**
  - **Given:** User đủ điều kiện click Hoàn thành PO.
  - **When:** Confirm MSG-DTR-012 → Yes.
  - **Then:** PO status `Received`, ASN status `Received`, tồn kho update, sync Inside (R037).
- **AC-35 — Step 5 nhận thiếu → PO config Waiting Adj Invoice**
  - **Given:** PO nhận thiếu, khai báo NCC không giao bù.
  - **When:** Hoàn thành.
  - **Then:** PO config = `Waiting Adj Invoice` (R038).
- **AC-36 — Step 5 SP không phù hợp → PO config Receiving Issue**
  - **Given:** PO có SP không phù hợp.
  - **When:** Hoàn thành.
  - **Then:** PO config = `Receiving Issue` (R038).
- **AC-37 — 24-10-2024 SPKPH Damaged UID**
  - **Given:** PO có SPKPH.
  - **When:** Hoàn thành PO/phiên.
  - **Then:** Vẫn import stock + UID product status `Damaged` (R039).
- **AC-38 — 24-10-2024 Vendor return dùng UID Damaged**
  - **Given:** Có lệnh vendor return cho PO có SPKPH.
  - **When:** Out UID.
  - **Then:** Dựa vào PO source để lấy đúng UID `Damaged` (R039).
- **AC-39 — Hoàn thành phiên nhận hàng**
  - **Given:** SL chưa đủ và có SKU có `NCC giao bù = Yes`.
  - **When:** User click `Hoàn thành phiên nhận hàng` → confirm.
  - **Then:** ASN status `Received`; tồn kho update theo phiên (R040).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R029, R030, R031, R037 | API receiving item PO bên Inside — endpoint cụ thể là gì? Schema đầy đủ request/response? Sync vs async? | Dev | Open | | | |
| Q-002 | R009, ERR-DTR-004 | Raw EN có typo `prodcut` → `product` — fix trong v2.18 hay giữ verbatim? | PO/UX | Open | | | |
| Q-003 | R010, MSG-DTR-006 | Verbatim VN+EN cho message khi CCDC scan Serial SL > 1. | PO/UX | Open | | | |
| Q-004 | R033 | Raw L1387 có typo `Không đồng kiếm` → `Không đồng kiểm`? Verify. | PO/UX | Open | | | |
| Q-005 | ERR-DTR-001, MSG-DTR-007, MSG-DTR-011 | Verbatim EN cho 3 message chỉ có VN (HSD min, SL thiếu trống, biên bản). | PO/UX | Open | | | |
| Q-006 | R004 | "24 tháng" trong ERR-DTR-002 — default vòng đời SP hay configurable per SKU? Lấy từ master data SP? | PO/Dev | Open | | | |
| Q-007 | R005 | "Icon ghi chú PO" — đặt ở màn hình nào (List PO hay Detail PO trên App)? Verbatim icon ký hiệu? | UX | Open | | | |
| Q-008 | R006 | PO `tester` — flag trên master PO (`is_tester=true`) hay là category PO? Cách detect? | PO/Dev | Open | | | |
| Q-009 | R012, R013 | "Shop 170 QL1A và Kho 170 QL1A" — feature flag rollout cho 2 kho cụ thể này (POC) hay đã rollout toàn bộ? Khi nào toàn bộ kho hỗ trợ? | PO | Open | | | |
| Q-010 | R014, R015 | "SKU combo lỗi data (combo không required + lẻ required)" — hệ thống block user nhận hay hiện cảnh báo? Verbatim? | PO/UX | Open | | | |
| Q-011 | R016 | "Brand = Synctives" — verify chính xác spelling (Synctive vs Synctives — raw có cả 2 ở L1209). Master data có brand nào exact? | PO | Open | | | |
| Q-012 | R023 | `Tình trạng hàng hoá = Khác` — user nhập text tự do hay chỉ chọn từ list? | PO/UX | Open | | | |
| Q-013 | R023 | `Hạn sử dụng YYYY-MM` trong khai báo `Sản phẩm không phù hợp` — đây là HSD của SP bị thiếu/lỗi, hay HSD đã scan? Validate vs HSD tối thiểu PO không? | PO | Open | | | |
| Q-014 | R035 | "Tất cả SL thiếu đều có cùng reason NCC giao bù = No" — vậy nếu 1 SKU `NCC giao bù = Yes` thì button "Hoàn thành PO" KHÔNG show? Edge case. | PO | Open | | | |
| Q-015 | R038 | `Waiting Adj Invoice` và `Receiving Issue` — PO config có thể có cả 2 cùng lúc (nhận thiếu + SP không phù hợp) không? | PO/Dev | Open | | | |
| Q-016 | R039 | "Product status = Damaged" — đây là UID-level status hay SKU-level? Có flow recovery để chuyển Damaged → Available không? | PO/Dev | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-21..S-27 | 2.17 (stub) | 2.17 | All R + AC | Draft |
| CHG-002 | Update | Update 06-01-2025: rules tính HSD tối thiểu theo `% Allowed Shelf Life × Product's Shelf Life` + edge case ngày cuối tháng | (trước 2.17) | 2.17 | R001-R004 | Done |
| CHG-003 | Add | Update 02-11-2024: icon ghi chú PO + 08-01-2025 PO tester HSD ≥ 3 tháng | (trước 2.17) | 2.17 | R005, R006 | Done |
| CHG-004 | Update | Update 24-10-2024: bypass nhập Serial/Imei cho CCDC | (trước 2.17) | 2.17 | R011 | Done |
| CHG-005 | Add | Update 05-01-2025: button "Thay đổi vị trí nhận hàng" + 1 PO 1 giỏ | (trước 2.17) | 2.17 | R012, R013 | Done |
| CHG-006 | Update | Update 30-05-2025 + 04-06-2025: SKU combo HSD rules (override) | (trước 2.17) | 2.17 | R014, R015 | Done |
| CHG-007 | Add | Update 04-06-2025: Step 1.1 RFID Thời trang Synctives auto VAS + Step 1.2 Xoá scan | (trước 2.17) | 2.17 | R016-R018 | Done |
| CHG-008 | Update | Update 17-10-2024: API receiving item payload `check_issue` cho unsuitable + missing | (trước 2.17) | 2.17 | R030, R031 | Done |
| CHG-009 | Add | Bổ sung 24-10-2024: SPKPH import stock + UID Damaged + vendor return logic | (trước 2.17) | 2.17 | R039 | Done |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_date_rules | test_stub_receiving_po_date_rules | Add (chờ Gate 1B) | [[stub_receiving_po_app]] (Step 1-5 flow), [[stub_receiving_po_inbound_shipment]] (PO/ASN status), [[stub_receiving_po_invoice]] (Step 5 hoá đơn), [[stub_receiving_po_vas]] (SPKPH + auto VAS RFID), [[stub_receiving_po_confirm_paste_id]] (post Hoàn thành PO), [[stub_receiving_po_packing_list]] (vendor return UID Damaged) | Q-001..Q-016 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R040, AC-01..AC-39 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-016 |

## 🚧 Blocked Coverage

- R029, R030, R031, R037 — chờ Q-001 (API Inside endpoint + schema)
- R009 — chờ Q-002 (typo `prodcut` fix)
- R010, MSG-DTR-006 — chờ Q-003 (verbatim message)
- R033 — chờ Q-004 (typo `kiếm`)
- ERR-DTR-001, MSG-DTR-007, MSG-DTR-011 — chờ Q-005 (verbatim EN)
- R004 — chờ Q-006 (vòng đời 24 tháng configurable)
- R005 — chờ Q-007 (icon ghi chú PO scope)
- R006 — chờ Q-008 (PO tester detection)
- R012, R013 — chờ Q-009 (rollout Shop 170 QL1A scope)
- R014, R015 — chờ Q-010 (lỗi data behavior)
- R016 — chờ Q-011 (Brand Synctive vs Synctives)
- R023 — chờ Q-012, Q-013 (Tình trạng Khác + HSD scope)
- R035 — chờ Q-014 (edge case mixed NCC giao bù)
- R038 — chờ Q-015 (PO config combined)
- R039 — chờ Q-016 (Damaged scope)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 21:00:00 | v1.1 | Refine stub → full spec: 40 R-ID, 39 AC, 36 BR, 12 messages (6 verbatim VN+EN, 6 missing — Q-003 Q-005), 16 questions Open. `partial_read: false`. | refine-batch-5-2026-05-30 |
