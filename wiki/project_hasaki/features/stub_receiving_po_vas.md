---
aliases: [stub_receiving_po_vas]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_vas
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L522-L783
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-31 19:12:50"
verification_status: Verified
approved_by:
approved_at:
approval_note:
last_verified_source_version: 2.17

---

# REQ: stub_receiving_po_vas

## Tổng quan
- **Mã tính năng:** stub_receiving_po_vas
- **Feature:** VAS — Listing, Detail, Cập nhật Serial/Imei/Label/QRCode, Group UID, SPKPH (không đồng kiểm)
- **Mô tả ngắn:** Module VAS (Value-Added Service) tại `Menu: Inbound / VAS`. Cho các SKU có quản lý Serial/Imei/Label code (không phải `Sức khoẻ - Làm đẹp`), sau khi kết thúc nhận hàng user phải xác nhận dán ID cho sản phẩm vật lý. Tự sinh VAS từ ASN khi ASN chuyển Received cho category TSCĐ/CCDC/CCDC PB (status Open). SKU `Sức khoẻ - Làm đẹp` có quản lý serial/imei → auto sinh + auto Completed (chỉ update serial khi đóng đơn). VAS detail gồm Thông tin chung + Danh sách SP cần dán ID. Cập nhật Serial/Imei/Label/QRCode với rules per category (CCDC bật QRCode required theo `wms_product.wms_config&131072 > 0`, Imei theo `config&8 > 0`). Update 25-02-2025: tắt Serial dưới BE, chỉ cần QRCode (Serial tự gen `[1023][YYMMDD][6 số tăng dần]`). Update 16-09-2025: group UID 10% đánh giá. Update 05-03-2025 + 05-05-2026: SPKPH (sản phẩm khai báo phụ hàng) cho PO không đồng kiểm — ASN riêng status `Waiting for approval`, action Cancel/Reject/Approve.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Nhân viên kho (dán ID), QC (đánh giá group UID), Quản lý (action Cancel/Reject/Approve SPKPH), Shop, NCC.
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[ts_receiving_po_vas]]
- **API Spec liên quan:** N/A — raw không mô tả API explicit (chỉ mention WMS BE config flags).
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_receiving_po_asn]] (ASN status Received trigger sinh VAS), [[stub_receiving_po_inbound_shipment]] (SL thực nhận). ↔️ liên quan [[stub_qc_uid_group]] (Group UID), [[stub_qc_evaluation_result]] (VAS Quality control results), [[stub_receiving_po_confirm_paste_id]] (xác nhận dán ID), [[stub_receiving_po_vas_manual]] (Create/Update VAS manual). ➡️ feed [[stub_receiving_po_app]] (App Confirm Unsuitable Product cho SPKPH).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07062_Receiving_PO_Docs_ver2.17.md | 2.17 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | BE config flag `wms_product.wms_config & 131072 > 0` → required QR | R016 | 07062#L679-L680 | Internal config (Q-002) |
| N/A | BE config flag `wms_product.config & 8 > 0` → required Imei | R016 | 07062#L681 | Internal config (Q-002) |
| N/A | QRCode scan validate against HR system (tồn tại/không tồn tại trên hệ thống HR) | R020 | 07062#L716-L717 | External — Q-003 |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Menu VAS đặt tại `Inbound / VAS` | UI + Navigation | High | ✅ | 07062#L523 |
| R002 | Với SKU có quản lý Serial/Imei/Label code mà **không phải category `Sức khoẻ - Làm đẹp`** → sau khi kết thúc nhận hàng user phải làm thêm bước **xác nhận dán ID** cho sản phẩm vật lý. Khi nhận hàng PO user chỉ scan theo số lượng, **không cần khai báo Serial/Imei/Label code** | Business rule | High | ✅ | 07062#L524-L528 |
| R003 | Bổ sung logic ASN ↔ VAS — SKU category `Sức khoẻ - Làm đẹp` có quản lý serial/imei: khi ASN chuyển status `Received` → hệ thống **auto sinh VAS và auto completed**. Hiện tại chỉ update thông tin serial khi đóng đơn để ghi nhận đóng cho đơn hàng nào | Business rule + Auto-flow | High | ✅ | 07062#L530-L533 |
| R004 | Bổ sung logic ASN ↔ VAS — SKU category `TSCĐ` (Tài sản cố định), `CCDC` (Công cụ dụng cụ), `CCDC PB` (CCDC phân bổ) có quản lý Serial/Imei/Label code: khi ASN chuyển status `Received` → hệ thống **sinh ra 1 VAS tương ứng với ASN với status = `Open`** | Business rule + Auto-flow | High | ✅ | 07062#L534-L536 |
| R005 | State transition UID — UID sau ASN Received có status `Received`, **chưa auto chuyển In-Bin**. UID `Received` **không được picklisted** cho order/receipt/IT. Sau khi user xác nhận chụp hình hoặc dán ID cho từng UID (tuỳ category SKU) → status chuyển `Received → In-Bin` | State transition + Business rule | High | ✅ | 07062#L537-L544 |
| R006 | Filter VAS — Select filter gồm các fields: `Mã VAS` (VAS number), `Mã phiếu nhập` (Inbound shipment), `Phiếu nhập nguồn` (Inbound source mapping), `Mã phiếu xuất` (Outbound order), `Phiếu xuất nguồn` (Outbound source mapping), `Loại` (Type), `Kho` (Warehouse), `SKU, Barcode`, `Người sở hữu` (Owner), `Trạng thái` (Status), `Từ ngày…đến ngày` | Filter + UI | High | ✅ | 07062#L545-L577 |
| R007 | Filter `Trạng thái`: 4 values — `Mới / Open`, `Đang xử lý / In-Progress`, `Hoàn thành / Completed`, `Đã huỷ / Canceled`. Mặc định = `Null`. Hỗ trợ **chọn nhiều** | Filter + Enum | High | ✅ | 07062#L564-L575 |
| R008 | Listing VAS — Cột: `TT` (No), `Mã VAS`, `Kho`, `Loại`, `Mã ASN` (hyperlink ASN detail), `Mã phiếu nhập` (hyperlink Inbound shipment detail), `Phiếu nhập nguồn` (hyperlink PO detail Inside), `Mã phiếu xuất`, `Phiếu xuất nguồn`, `Vị trí`, `Người tạo`, `Người thực hiện`, `Ngày cập nhật`, `Trạng thái`, `Thao tác` | UI + Navigation | High | ✅ | 07062#L580-L621 |
| R009 | Listing `Vị trí` — vị trí nhận hàng theo ASN. Lưu ý: nếu cùng 1 phiên nhận mà 1 SKU được nhận vào **2 location khác nhau → sinh ra VAS tương ứng** (2 VAS riêng). Nếu SKU yêu cầu serial → không cần hiển thị, chỉ hiện SKU có yêu cầu serial | Business rule + UI | High | ✅ | 07062#L594-L601 |
| R010 | Listing `Trạng thái` enum — `Mới / Open`: khi ASN received và sinh ra 1 VAS cho SKU TSCĐ/CCDC/CCDC PB có quản lý Serial/Imei/Label code; `Đang xử lý / In-Progress`: khi có ít nhất 1 SKU có số lượng đã dán > 1; `Hoàn thành / Completed`; `Đã huỷ / Canceled` | State + Enum | High | ✅ | 07062#L607-L614 |
| R011 | Listing `Thao tác` — Button cập nhật thông tin Serial/Imei/Label code cho SKU (**chỉ show cho VAS status `Open` và `In-Progress`**); Button xem chi tiết VAS | UI + Functional | High | ✅ | 07062#L615-L621 |
| R012 | VAS detail — Thông tin chung dạng text gồm: `Kho`, `Loại`, `ASN`, `Mã phiếu nhập`, `Phiếu nhập nguồn`, `Mã phiếu xuất`, `Phiếu xuất nguồn`, `Vị trí`, `Ngày tạo`, `Người tạo`, `Ngày cập nhật` | UI | High | ✅ | 07062#L630-L653 |
| R013 | VAS detail — Danh sách sản phẩm **chỉ hiện SKU có quản lý serial** (cần xác nhận dán ID). Cột: `SKU`, `Barcode`, `Sản phẩm` (Product name), `SL thực nhận` (Qty received — số lượng thực nhận của SKU theo ASN tương ứng), `SL đã dán` (Qty pasted — số lượng cập nhật đã dán ID), `Hình ảnh/Video`, `Thao tác` | UI + Business rule | High | ✅ | 07062#L654-L673 |
| R014 | VAS detail `Thao tác` — Button cập nhật thông tin Serial/Imei/Label code (chỉ show cho VAS status `Open` và `In-Progress`); Button xem chi tiết Serial/Imei/Label code theo SKU | UI + Functional | High | ✅ | 07062#L664-L673 |
| R015 | Cập nhật thông tin Serial/Imei/Label code — chọn button trên từng dòng SKU → mở form cập nhật cho sản phẩm tương ứng. Hệ thống **auto chọn thông tin cần cập nhật** theo category | Functional + UI | High | ✅ | 07062#L674-L678 |
| R016 | Auto chọn thông tin cập nhật — Nếu cate = `CCDC`, `CCDC PB`, ... (cates thực hiện theo luồng VAS): bật ON cập nhật `QRCode` khi `wms_product.wms_config & 131072 > 0` (required QR); HOẶC bật ON cập nhật `Serial/Imei` khi `wms_product.config & 8 > 0` (required Imei) | Business rule + BE config | High | ⚠️ | 07062#L678-L681 |
| R017 | Cập nhật 25-02-2025 — Hiện tại luôn **tắt option Serial dưới BE**, user chỉ cần cập nhật QRCode. Sau này cần sẽ mở ra sau | Functional | High | ✅ | 07062#L682-L685 |
| R018 | Cập nhật 25-02-2025 — Serial nếu không có thông tin thì hệ thống WMS **tự gen mã** theo rule `[1023][YYMMDD][6 số tăng dần]`. Nếu sau này kiểm kê user count lại theo Serial → update Serial mới đè lên Serial auto-gen | Business rule + Auto-gen | High | ✅ | 07062#L686-L689 |
| R019 | Ngược lại 2 case ON QRCode/Serial — chỉ cần **chụp hình**, bỏ qua bước cập nhật QRCode hoặc Serial | Functional | High | ✅ | 07062#L690-L691 |
| R020 | Lưu ý QRCode — mã QRCode in ra có dạng `Object` nên khi scan hệ thống **tự cắt chuỗi** để lấy đúng thông tin. Cụ thể: lấy field `Code` trong object | Business rule + Parser | High | ✅ | 07062#L692-L694 |
| R021 | Logic scan form cập nhật — thông tin tích chọn (QRCode hoặc Serial) → ô scan của thông tin đó show lên để user scan. Nếu chỉ chọn cập nhật 1 thông tin → khi scan tự động add vào danh sách; nếu user nhập → nhấn icon `+` để add. Nếu chọn cập nhật cả 2 → khi scan QRCode hợp lệ, **auto chuyển focus** qua ô scan Serial/Imei để tiếp tục scan và add vào danh sách | Functional + UX | High | ✅ | 07062#L698-L703 |
| R022 | Validation Serial — Serial scan vào đã tồn tại trong danh sách / trên hệ thống → message lỗi tương ứng. Serial không hợp lệ phải từ **16 ký tự** trở lên | Validation | High | ✅ | 07062#L704-L711 |
| R023 | Validation QRCode — QRCode scan vào đã tồn tại trên hệ thống / trong danh sách / không tồn tại trên hệ thống HR → 3 message lỗi tương ứng | Validation | High | ✅ | 07062#L712-L717 |
| R024 | Thông tin sau khi cập nhật — hỗ trợ **search gần đúng** (nhập từ 3 ký tự) cho QRCode và Serial đã scan vào danh sách. Cần chỉnh sửa thông tin: chọn icon tương ứng để cập nhật (vẫn validation như scan mới) | Functional + UI | High | ✅ | 07062#L722-L724 |
| R025 | Form action — `Đóng` để tắt thông báo; `Lưu` để lưu thông tin cho sản phẩm. Sau khi `SL đã dán = SL thực nhận` (cần dán) **của tất cả SKU trong VAS** → button `Complete` show lên cho user complete VAS với confirm dialog `Do you want to confirm pasting ID completion?` | Functional + UI | High | ✅ | 07062#L725-L731 |
| R026 | Update 16-09-2025 — Update Group UID và Quality control results cho `type = Quality control`. **1 SKU nhận trong ASN theo group UID sẽ lấy ra 10% để đánh giá**, nếu ra số lẻ thì **làm tròn lên** | Business rule + Auto-calc | High | ✅ | 07062#L736-L739 |
| R027 | Update 16-09-2025 — Ví dụ R026: SKUA nhận trong ASN là 25 group UID → 10% = 2.5 → làm tròn lên 3 → có 3 dòng VAS cần đánh giá chất lượng cho SKUA | Business rule | High | ✅ | 07062#L740-L742 |
| R028 | Update 16-09-2025 — Trong VAS Quality control bổ sung thêm `Group UID` và `kết quả đánh giá theo group UID`. **Chỉ cần 1 kết quả Failed thì ghi nhận là Failed** | Business rule | High | ✅ | 07062#L743-L745 |
| R029 | Update 16-09-2025 — VAS sinh ra khi user **chưa thực hiện đánh giá** → `Group UID = trống`. VAS sinh ra khi user **đã thực hiện đánh giá** → `Group UID = thông tin được scan vào` | Business rule + State | High | ✅ | 07062#L746-L747 |
| R030 | Update 05-03-2025 + 05-05-2026 — Khi nhận hàng PO **không đồng kiểm và có SPKPH** (sản phẩm khai báo phụ hàng): Shop vẫn khai báo như bình thường nhưng hệ thống ghi nhận như **nhận thiếu và nhận lại ở phiên sau**. Luồng xử lý SPKPH cho luồng nhận PO **tạm Off không sử dụng** | Business rule | High | ✅ | 07062#L751-L754 |
| R031 | SPKPH luồng — Với PO không đồng kiểm có khai báo SPKPH: SKU bình thường nhận trong phiên → đưa vào 1 ASN riêng + update status = `Received` + import stock. SKU khai báo SPKPH → đưa vào 1 ASN với status `Waiting for approval`. Nhiều SKU SPKPH cùng phiên → nằm trong 1 phiên ASN riêng. **Không import stock cho SKU khai báo SPKPH** | Business rule + State transition | High | ✅ | 07062#L757-L766 |
| R032 | SPKPH action — Quản lý action `Cancel` → Xác nhận → UID của SKU này chuyển về "chưa nhận" để user scan nhận lại hoặc khai báo thiếu hàng và NCC không giao lại để Completed PO; ASN status = `Cancel` | Functional + State transition | High | ✅ | 07062#L770-L773 |
| R033 | SPKPH action — Quản lý action `Reject` → chuyển các SP khai báo SPKPH qua "SP chưa nhận"; user scan nhận lại như SP bình thường; ASN status = `Reject` | Functional + State transition | High | ✅ | 07062#L774-L777 |
| R034 | SPKPH action — Quản lý action `Approve` → ASN status = `Chờ NCC đến lấy` (Waiting for vendor to pick). Shop chỉ quản lý hàng vật lý bên ngoài chờ NCC đến lấy hoặc **quá 7 ngày NCC chưa lấy → tiêu huỷ theo quy trình**. User xác nhận việc NCC đến lấy hàng hoặc tiêu huỷ thông qua App WMS | Functional + State + Timer | High | ✅ | 07062#L778-L783 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- ASN đã chuyển status `Received` (từ flow nhận hàng PO).
- SKU có quản lý Serial/Imei/Label code.
- User có quyền truy cập `Inbound / VAS`.

### Luồng chuẩn (Happy Path) — Sinh VAS tự động từ ASN
1. ASN chuyển status `Received` (R005 trigger).
2. Hệ thống check category SKU:
   - **`Sức khoẻ - Làm đẹp`** có serial/imei → auto sinh VAS + auto Completed (R003).
   - **`TSCĐ` / `CCDC` / `CCDC PB`** có Serial/Imei/Label code → sinh VAS status `Open` (R004).
3. UID của các SP này có status `Received`, **không picklisted** cho order/receipt/IT (R005).
4. User truy cập `Inbound / VAS`, filter theo nhu cầu (R006, R007).
5. Listing hiển thị VAS với cột hyperlink ASN/Inbound shipment/PO source (R008).
6. User click `Thao tác` → mở VAS detail (R011, R014).

### Luồng chuẩn (Happy Path) — Cập nhật Serial/QRCode (CCDC bật QR)
1. User mở VAS detail, danh sách SKU có serial hiển thị (R013).
2. Click button cập nhật trên dòng SKU → form mở (R015).
3. Hệ thống auto chọn `QRCode` (vì cate CCDC + `wms_config & 131072 > 0`) (R016).
4. Update 25-02-2025 — Serial bị tắt dưới BE (R017). Nếu cần Serial → hệ thống tự gen `[1023][YYMMDD][6 số tăng dần]` (R018).
5. User scan QRCode → hệ thống cắt chuỗi lấy field `Code` từ Object (R020).
6. Validation QRCode: không trùng danh sách/hệ thống + tồn tại trên HR (R023).
7. Tự động add vào danh sách (R021).
8. Sau khi `SL đã dán = SL thực nhận` cho **tất cả SKU**, button `Complete` show lên (R025).
9. User click `Complete` → confirm `Do you want to confirm pasting ID completion?` → VAS chuyển `Completed`. UID chuyển `Received → In-Bin` (R005, R025).

### Luồng chuẩn (Happy Path) — Cập nhật cả QRCode + Serial (TSCĐ)
1. Form mở, auto chọn cả QRCode + Serial (R016).
2. User scan QRCode → validation pass (R023) → **auto chuyển focus qua ô Serial/Imei** (R021).
3. User scan Serial → validation 16 ký tự + không trùng (R022) → add vào danh sách.

### Luồng chuẩn (Happy Path) — Group UID Quality Control (Update 16-09-2025)
1. ASN có SKUA nhận theo group UID = 25.
2. Hệ thống auto sinh 10% = 2.5 → làm tròn lên 3 → 3 dòng VAS cần đánh giá cho SKUA (R026, R027).
3. VAS sinh khi user **chưa scan** → Group UID = trống (R029).
4. User scan group UID → VAS được gắn Group UID = giá trị scan (R029).
5. QC đánh giá → bổ sung Group UID + kết quả vào VAS Quality control (R028).
6. Có 1 group UID kết quả `Failed` → toàn bộ VAS ghi nhận `Failed` (R028).

### Luồng chuẩn (Happy Path) — SPKPH (PO không đồng kiểm)
1. Shop nhận PO không đồng kiểm có SPKPH (R030).
2. Hệ thống tách:
   - SKU bình thường → ASN riêng status `Received` + import stock (R031).
   - SKU SPKPH → ASN khác status `Waiting for approval`, KHÔNG import stock (R031).
3. Quản lý approve/reject/cancel:
   - **Cancel** → ASN status `Cancel`, UID về "chưa nhận", user scan lại hoặc khai báo thiếu hàng (R032).
   - **Reject** → ASN status `Reject`, SP qua "chưa nhận", user scan nhận lại như SP bình thường (R033).
   - **Approve** → ASN status `Chờ NCC đến lấy`. Shop quản lý hàng vật lý chờ NCC hoặc quá 7 ngày → tiêu huỷ. User xác nhận qua App WMS (R034).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — SKU `Sức khoẻ - Làm đẹp`:** không phải dán ID, VAS auto Completed; chỉ update serial khi đóng đơn (R002, R003).
- **A2 — Cùng SKU 2 location:** sinh 2 VAS riêng (R009).
- **A3 — Form không tích chọn QRCode/Serial:** chỉ cần chụp hình, bỏ qua scan (R019).
- **A4 — User chỉnh sửa thông tin đã scan:** click icon → modify với validation như scan mới (R024).
- **A5 — User tự gen Serial:** hệ thống tự gen theo rule `[1023][YYMMDD][6 số]`; sau này count lại theo Serial sẽ override (R018).

### Luồng ngoại lệ (Exception Paths)
- **E1 — Serial scan đã tồn tại trong danh sách:** message `Serial [code] đã tồn tại trong danh sách.` (ERR-VAS-001).
- **E2 — Serial scan đã tồn tại trên hệ thống:** message `Serial [code] đã tồn tại trên hệ thống.` (ERR-VAS-002).
- **E3 — Serial < 16 ký tự:** message `Serial [code] không hợp lệ (phải từ 16 ký tự)` (ERR-VAS-003).
- **E4 — QRCode đã tồn tại trên hệ thống:** message `QRCode [code] đã tồn tại trên hệ thống.` (ERR-VAS-004).
- **E5 — QRCode đã tồn tại trong danh sách:** message `QRCode [code] đã tồn tại trong danh sách.` (ERR-VAS-005).
- **E6 — QRCode không tồn tại trên hệ thống HR:** message `QRCode [code] không tồn tại trên hệ thống HR.` (ERR-VAS-006).
- **E7 — Cố Complete VAS khi chưa đủ SL đã dán:** button `Complete` không show (R025).
- **E8 — User cố picklist UID trạng thái `Received` (chưa In-Bin):** hệ thống block (R005).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Trigger sinh VAS | rule | ✅ | ASN chuyển Received: cate `Sức khoẻ - Làm đẹp` có serial → auto VAS + auto Completed; cate `TSCĐ/CCDC/CCDC PB` có Serial/Imei/Label → VAS status Open |
| UID state | enum | ✅ | `Received` (không picklisted) → `In-Bin` (sau khi user xác nhận chụp hình/dán ID) |
| Filter Trạng thái | multi-enum | ❌ | Default Null; chọn nhiều; values {Open, In-Progress, Completed, Canceled} |
| Vị trí | rule | ✅ | Cùng SKU 2 location → 2 VAS riêng |
| Listing — chỉ SKU có serial | rule | ✅ | Trong VAS detail, danh sách SP chỉ hiện SKU có yêu cầu serial |
| Button Cập nhật Serial/Imei/QRCode | rule | ✅ | Chỉ show cho VAS status `Open` hoặc `In-Progress` |
| Auto chọn thông tin update | rule | ✅ | Cate CCDC + `wms_config & 131072 > 0` → bật QRCode; `config & 8 > 0` → bật Imei |
| Serial auto-gen | rule | ✅ | Pattern `[1023][YYMMDD][6 số tăng dần]` khi không có Serial input |
| Serial override | rule | ✅ | Khi user count lại theo Serial sẽ override Serial auto-gen |
| QRCode parser | rule | ✅ | QRCode in dạng Object → lấy field `Code` |
| Form scan logic | rule | ✅ | 1 info: scan tự add; nhập tay nhấn `+`. 2 info: scan QR pass → auto focus Serial |
| Serial length | integer | ✅ | ≥ 16 ký tự |
| Search gần đúng | rule | ✅ | QRCode/Serial trong danh sách: nhập từ 3 ký tự |
| Trigger Complete button | rule | ✅ | SL đã dán = SL thực nhận của TẤT CẢ SKU trong VAS |
| Confirm dialog Complete | message | ✅ | `Do you want to confirm pasting ID completion?` |
| Group UID 10% | formula | ✅ | `dòng VAS đánh giá = ceil(SL group UID × 10%)` |
| Group UID Failed rule | rule | ✅ | Có 1 kết quả Failed → toàn bộ VAS = Failed |
| Group UID empty rule | rule | ✅ | VAS sinh trước scan → Group UID = trống; sau scan → Group UID = giá trị scan |
| SPKPH ASN tách | rule | ✅ | SKU thường: ASN riêng + import stock; SKU SPKPH: ASN riêng status `Waiting for approval`, không import |
| SPKPH action Approve timeout | rule | ✅ | Sau Approve, NCC quá 7 ngày chưa lấy → tiêu huỷ theo quy trình |
| Luồng SPKPH nhận PO | rule | ✅ | Tạm Off không sử dụng |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-VAS-001 | Validation | Serial scan đã tồn tại trong danh sách | `Serial 11333787241140438102 đã tồn tại trong danh sách.` | `Serial 11333787241140438102 already exists in the list.` | 07062#L706-L707 |
| ERR-VAS-002 | Validation | Serial scan đã tồn tại trên hệ thống | `Serial 11333787241140438102 đã tồn tại trên hệ thống.` | `Serial 11333787241140438102 already exists on the system.` | 07062#L708-L709 |
| ERR-VAS-003 | Validation | Serial < 16 ký tự | `Serial 1133378724121 không hợp lệ (phải từ 16 ký tự)` | `Serial 1133378724121 is invalid (must be 16 characters or more)` | 07062#L710-L711 |
| ERR-VAS-004 | Validation | QRCode scan đã tồn tại trên hệ thống | `QRCode UEA1JDJ3 đã tồn tại trên hệ thống.` | `QRCode UEA1JDJ3 already exists on the system.` | 07062#L712-L713 |
| ERR-VAS-005 | Validation | QRCode scan đã tồn tại trong danh sách | `QRCode UEA1JDJ3 đã tồn tại trong danh sách.` | `QRCode UEA1JDJ3 already exists in the list.` | 07062#L714-L715 |
| ERR-VAS-006 | Validation | QRCode không tồn tại trên hệ thống HR | `QRCode UEA1JDJ3 không tồn tại trên hệ thống HR.` | `QRCode UEA1JDJ3 does not exist on the HR system.` | 07062#L716-L717 |
| MSG-VAS-007 | Confirm | User click `Complete` khi đủ SL đã dán | (raw chỉ có EN — Q-001) | `Do you want to confirm pasting ID completion?` | 07062#L730-L731 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Auto sinh VAS auto Completed cho cate Sức khoẻ - Làm đẹp**
  - **Given:** SKU `Mỹ phẩm A` quản lý serial, category `Sức khoẻ - Làm đẹp`.
  - **When:** ASN chuyển `Received`.
  - **Then:** Hệ thống auto sinh VAS + auto chuyển `Completed`; user không cần dán ID (R002, R003).
- **AC-02 — Sinh VAS Open cho TSCĐ/CCDC/CCDC PB**
  - **Given:** SKU thuộc cate `CCDC` có Serial/Imei.
  - **When:** ASN chuyển `Received`.
  - **Then:** Hệ thống sinh 1 VAS tương ứng ASN với status `Open`; UID status `Received`, không picklisted (R004, R005).
- **AC-03 — UID không picklisted khi status Received**
  - **Given:** UID đang ở status `Received`.
  - **When:** Hệ thống try lấy UID cho picklisted order/receipt/IT.
  - **Then:** UID bị skip, không được lấy (R005).
- **AC-04 — UID chuyển In-Bin sau khi dán ID**
  - **Given:** UID `Received`, VAS `In-Progress`.
  - **When:** User xác nhận chụp hình/dán ID cho UID này.
  - **Then:** UID chuyển `Received → In-Bin` (R005).
- **AC-05 — Cùng SKU 2 location sinh 2 VAS**
  - **Given:** Phiên nhận có SKUA vào location L1 (5 cái) và L2 (3 cái).
  - **When:** ASN chuyển Received.
  - **Then:** Sinh 2 VAS riêng (1 cho L1, 1 cho L2) (R009).
- **AC-06 — Filter Trạng thái chọn nhiều**
  - **Given:** Có VAS với cả 4 status.
  - **When:** User filter Trạng thái = [`Open`, `In-Progress`].
  - **Then:** Listing hiển thị VAS với 2 status này (R007).
- **AC-07 — Hyperlink Mã ASN, Mã phiếu nhập, Phiếu nhập nguồn**
  - **Given:** Dòng VAS có Mã ASN = `ASN-001`.
  - **When:** User click cell `ASN-001`.
  - **Then:** Chuyển sang trang ASN detail (R008).
- **AC-08 — Button cập nhật chỉ show cho VAS Open/In-Progress**
  - **Given:** VAS-A status `Open`, VAS-B status `Completed`.
  - **When:** User xem listing.
  - **Then:** VAS-A có button cập nhật; VAS-B không có (R011, R014).
- **AC-09 — Danh sách SP trong VAS detail chỉ SKU có serial**
  - **Given:** VAS-A có 5 SKU, 3 SKU có yêu cầu serial.
  - **When:** User mở VAS detail.
  - **Then:** Danh sách hiển thị 3 SKU có yêu cầu serial (R013).
- **AC-10 — Auto chọn QRCode cho CCDC theo BE config**
  - **Given:** SKU `CCDC-A` có `wms_config & 131072 > 0`.
  - **When:** User click cập nhật.
  - **Then:** Form auto check QRCode (R016).
- **AC-11 — Update 25-02-2025: Serial off, chỉ QRCode**
  - **Given:** Form mở cho SKU CCDC.
  - **When:** User xem form.
  - **Then:** Option Serial bị tắt dưới BE; chỉ có QRCode để cập nhật (R017).
- **AC-12 — Serial auto-gen pattern**
  - **Given:** SKU không có Serial input từ user.
  - **When:** User submit cập nhật.
  - **Then:** Hệ thống gen Serial pattern `[1023][YYMMDD][6 số tăng dần]`, ví dụ `1023260530000001` (R018).
- **AC-13 — QRCode parser lấy field Code từ Object**
  - **Given:** QRCode in dạng `{"Code":"ABC123","Other":"xyz"}`.
  - **When:** User scan QRCode.
  - **Then:** Hệ thống lấy `ABC123` (giá trị field `Code`) để add vào danh sách (R020).
- **AC-14 — Auto focus QRCode → Serial khi cả 2 ON**
  - **Given:** Form mở với QRCode + Serial cùng ON.
  - **When:** User scan QRCode `XYZ` → validation pass.
  - **Then:** Focus tự chuyển sang ô Serial/Imei (R021).
- **AC-15 — Serial scan trùng danh sách**
  - **Given:** Serial `11333787241140438102` đã có trong danh sách.
  - **When:** User scan lại Serial này.
  - **Then:** Message ERR-VAS-001 hiện (R022).
- **AC-16 — Serial < 16 ký tự**
  - **Given:** Form mở.
  - **When:** User scan Serial `1133378724121` (13 ký tự).
  - **Then:** Message ERR-VAS-003 hiện (R022).
- **AC-17 — QRCode không tồn tại HR**
  - **Given:** QRCode `UEA1JDJ3` không tồn tại trên hệ thống HR.
  - **When:** User scan.
  - **Then:** Message ERR-VAS-006 hiện (R023).
- **AC-18 — Search gần đúng QRCode/Serial từ 3 ký tự**
  - **Given:** Danh sách có Serial `1023260530000001`, `1023260530000002`.
  - **When:** User nhập search `102` (3 ký tự).
  - **Then:** Cả 2 Serial hiển thị (R024).
- **AC-19 — Complete button khi đủ SL dán**
  - **Given:** VAS có 3 SKU, mỗi SKU SL thực nhận = 5. SKU 1 đã dán 5/5, SKU 2 đã dán 5/5, SKU 3 đã dán 4/5.
  - **When:** User xem VAS.
  - **Then:** Button `Complete` không show. Khi SKU 3 dán đủ 5/5 → button show với confirm `Do you want to confirm pasting ID completion?` (R025).
- **AC-20 — Update 16-09-2025: 10% group UID đánh giá**
  - **Given:** SKUA nhận trong ASN có 25 group UID.
  - **When:** Hệ thống tính SL VAS cần đánh giá.
  - **Then:** SL = ceil(25 × 10%) = ceil(2.5) = 3 dòng VAS (R026, R027).
- **AC-21 — Group UID Failed → toàn VAS Failed**
  - **Given:** VAS có 3 group UID đánh giá, kết quả 2 Pass + 1 Failed.
  - **When:** Hệ thống tổng hợp.
  - **Then:** VAS ghi nhận `Failed` (R028).
- **AC-22 — Group UID empty khi VAS sinh trước scan**
  - **Given:** VAS sinh từ ASN, user chưa scan group UID.
  - **When:** User xem VAS detail.
  - **Then:** Field Group UID = trống (R029).
- **AC-23 — SPKPH tách ASN**
  - **Given:** PO không đồng kiểm có 5 SKU bình thường + 2 SKU SPKPH.
  - **When:** Shop khai báo nhận.
  - **Then:** Hệ thống tạo 2 ASN: ASN-1 (5 SKU thường, status Received, import stock), ASN-2 (2 SKU SPKPH, status `Waiting for approval`, không import stock) (R031).
- **AC-24 — SPKPH action Cancel**
  - **Given:** ASN SPKPH status `Waiting for approval`.
  - **When:** Quản lý action Cancel → confirm.
  - **Then:** UID SKU SPKPH chuyển "chưa nhận"; ASN status `Cancel`; user có thể scan lại hoặc khai báo thiếu để Completed PO (R032).
- **AC-25 — SPKPH action Reject**
  - **Given:** ASN SPKPH status `Waiting for approval`.
  - **When:** Quản lý action Reject.
  - **Then:** SP qua "chưa nhận"; user scan lại như SP thường; ASN status `Reject` (R033).
- **AC-26 — SPKPH action Approve**
  - **Given:** ASN SPKPH status `Waiting for approval`.
  - **When:** Quản lý action Approve.
  - **Then:** ASN status `Chờ NCC đến lấy`; Shop quản lý hàng vật lý; user xác nhận trên App WMS (R034).
- **AC-27 — SPKPH timeout 7 ngày NCC chưa lấy**
  - **Given:** ASN SPKPH status `Chờ NCC đến lấy` từ ngày `2026-05-23`.
  - **When:** Today = `2026-05-30` (đã 7 ngày).
  - **Then:** Trigger tiêu huỷ theo quy trình; user xác nhận tiêu huỷ trên App WMS (R034).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R025, MSG-VAS-007 | Verbatim VN cho confirm dialog `Do you want to confirm pasting ID completion?` — raw chỉ có EN. | PO/UX | Open | | | |
| Q-002 | R016 | BE config flags `wms_product.wms_config & 131072` và `config & 8` — có doc kỹ thuật mô tả các bit khác không? Có thể đổi runtime hay chỉ deploy fix? | Dev | Open | | | |
| Q-003 | R023, ERR-VAS-006 | "Hệ thống HR" là service nào? API endpoint check QRCode tồn tại trên HR? Có dependency và rate limit không? | Dev | Open | | | |
| Q-004 | R018 | Serial pattern `[1023][YYMMDD][6 số tăng dần]` — `1023` là constant prefix gì? Đếm 6 số tăng dần theo scope nào (per kho/per ngày/global)? | Dev | Open | | | |
| Q-005 | R002, R003 | "Sức khoẻ - Làm đẹp" là tên category cụ thể trong master data, hay là 1 group cha gồm nhiều category con? | PO/Dev | Open | | | |
| Q-006 | R010 | Status `In-Progress` định nghĩa "có ít nhất 1 SKU có số lượng đã dán > 1" — vậy nếu chỉ 1 SP duy nhất đã dán = 1 thì có chuyển In-Progress không? Edge: dán = 0 vẫn `Open`? | PO | Open | | | |
| Q-007 | R026, R027 | Cách làm tròn 10% — luôn ceil hay theo rules khác (vd <0.5 round down)? Raw chỉ ví dụ 2.5 → 3. | PO | Open | | | |
| Q-008 | R028 | VAS Quality control — phạm vi `Failed` này cho toàn bộ VAS hay chỉ cho group UID đó? Verbatim "ghi nhận là Failed" có nghĩa VAS status = Failed, hay 1 field result riêng = Failed? | PO | Open | | | |
| Q-009 | R031 | "Phiên ASN riêng" cho nhiều SKU SPKPH — 1 phiên = 1 ASN, hay nhiều SKU SPKPH cùng phiên chỉ chung 1 ASN duy nhất? | PO | Open | | | |
| Q-010 | R030 | "Luồng xử lý SPKPH cho luồng nhận PO tạm Off không sử dụng" — flow Off này là flow nào, đối lập với SPKPH active flow? Verify trạng thái thực tế production. | PO/Dev | Open | | | |
| Q-011 | R034 | Action Approve sau 7 ngày NCC chưa lấy → tiêu huỷ "theo quy trình" — có doc quy trình tiêu huỷ riêng không? Quy trình tự động trigger hay user manual phải xác nhận? | PO | Open | | | |
| Q-012 | R029 | Khi VAS đã sinh với Group UID empty, user sau đó scan group UID — group UID được gắn vào VAS hiện hữu hay tạo VAS mới? | PO | Open | | | |
| Q-013 | R009 | Cùng SKU 2 location → 2 VAS. Vậy ngược lại: 1 SKU 1 location nhưng 2 phiên nhận khác nhau — 1 VAS hay 2 VAS? | PO | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-10..S-14 | 2.17 (stub) | 2.17 | All R + AC | Draft |
| CHG-002 | Update | Update 25-02-2025: tắt Serial dưới BE, chỉ cần QRCode; Serial tự gen `[1023][YYMMDD][6 số tăng dần]` | (trước 2.17) | 2.17 | R017, R018, AC-11, AC-12 | Done (đã trong raw v2.17) |
| CHG-003 | Add | Update 16-09-2025: VAS Quality control + Group UID 10% đánh giá + Failed rule | (trước 2.17) | 2.17 | R026-R029, AC-20, AC-21, AC-22 | Done (đã trong raw v2.17) |
| CHG-004 | Add | Update 05-03-2025 + 05-05-2026: SPKPH cho PO không đồng kiểm — ASN tách, action Cancel/Reject/Approve, timeout 7 ngày | (trước 2.17) | 2.17 | R030-R034, AC-23..AC-27 | Done (đã trong raw v2.17); flow Off mention (R030) |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_vas | test_stub_receiving_po_vas | Add (chờ Gate 1B) | [[stub_receiving_po_asn]] (ASN trigger sinh VAS), [[stub_qc_uid_group]] (Group UID 10%), [[stub_qc_evaluation_result]] (VAS QC results), [[stub_receiving_po_confirm_paste_id]] (xác nhận dán ID), [[stub_receiving_po_vas_manual]] (Create/Update VAS manual), [[stub_receiving_po_app]] (App Confirm Unsuitable cho SPKPH) | Q-001..Q-013 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R034, AC-01..AC-27 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-013 |

## 🚧 Blocked Coverage

- R025, MSG-VAS-007 — chờ Q-001 (verbatim VN confirm dialog)
- R016 — chờ Q-002 (BE config bits)
- R023, ERR-VAS-006 — chờ Q-003 (HR system endpoint)
- R018 — chờ Q-004 (Serial pattern detail)
- R002, R003 — chờ Q-005 (category Sức khoẻ - Làm đẹp scope)
- R010 — chờ Q-006 (In-Progress trigger edge case)
- R026, R027 — chờ Q-007 (rounding rule)
- R028 — chờ Q-008 (Failed scope)
- R031 — chờ Q-009 (ASN phiên scope)
- R030 — chờ Q-010 (flow Off vs SPKPH active)
- R034 — chờ Q-011 (quy trình tiêu huỷ)
- R029 — chờ Q-012 (VAS gắn Group UID retroactive)
- R009 — chờ Q-013 (cùng SKU 1 location 2 phiên)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 19:30:00 | v1.1 | Refine stub → full spec: 34 R-ID, 27 AC, 22 BR, 7 messages (6 verbatim VN+EN, 1 missing VN — Q-001), 13 questions Open. `partial_read: false`. | refine-batch-4-2026-05-30 |
