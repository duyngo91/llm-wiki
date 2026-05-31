---
aliases: [stub_receiving_po_app]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_app
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L784-L1069
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-31 19:12:50"
verification_status: Verified
approved_by:
approved_at:
approval_note:
last_verified_source_version: 2.17

---

# REQ: stub_receiving_po_app

## Tổng quan
- **Mã tính năng:** stub_receiving_po_app
- **Feature:** Receiving PO trên App — App Confirm Unsuitable + Flow scan nhận PO (Step 1-5)
- **Mô tả ngắn:** Tính năng nhận hàng PO trên App WMS. Gồm 2 module: (1) `App / Confirm Unsuitable Product` — quản lý phiên SPKPH status `Chờ NCC đến lấy` (phương án Đã trả NCC / Đã tiêu huỷ). (2) `Receiving PO` (Step 1-5): scan PO (validate VAT/kho/verify/received), chọn loại nhận (đồng kiểm/không đồng kiểm), scan camera (config `Required camera`), scan vị trí/giỏ (PO zone bắt buộc bin Di động vs PO thường), scan SKU/HSD/số lô. Update 05-01-2026: rules force SKU bất thường qty < 100k. Update 18-02-2025: config `Required camera` per Warehouse. Update 27-02-2024: Bin Di động (Pallet) shared multi-stock.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Shop/Nhân viên kho (App), Quản lý (cấu hình Warehouse).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[ts_receiving_po_app]]
- **API Spec liên quan:** N/A — raw không mô tả API explicit, chỉ mention "API update status PO trên Inside" (Q-001).
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_receiving_po_vas]] (SPKPH ASN status `Chờ NCC đến lấy`), [[stub_receiving_po_inbound_shipment]] (PO/Inbound Shipment), [[stub_receiving_po_invoice]] (verify invoice). ↔️ liên quan [[stub_receiving_po_date_rules]] (HSD rules), [[stub_receiving_po_confirm_paste_id]] (post-scan flow). ➡️ feed [[stub_receiving_po_asn]] (sinh ASN), [[stub_receiving_po_fabric]] (scan Vải step).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07062_Receiving_PO_Docs_ver2.17.md | 2.17 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | API update status PO trên Inside thành `Receiving` — raw mention "Lưu ý khi này chưa gọi API" | R009 | 07062#L880-L881 | TBD — Q-001 |
| N/A | Warehouse config endpoint `Configuration / General / Required camera` | R017 | 07062#L921-L935 | Internal — Q-002 |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | App `Confirm Unsuitable Product` đặt tại `App / Purchase order / Confirm Unsuitable Product` | UI + Navigation | High | ✅ | 07062#L787 |
| R002 | User chọn kho → show danh sách ASN khai báo SPKPH có trạng thái `Chờ NCC đến lấy` của kho tương ứng. Thông tin gồm: `Mã PO`, `Thời gian tạo PO`, `Mã ASN`, `Tổng SKU` (trong ASN của SPKPH), `Tổng sản phẩm` (trong ASN của SPKPH) | UI + Functional | High | ✅ | 07062#L788-L798 |
| R003 | User chọn vào phiên SPKPH cần xác nhận → hiển thị thông tin phiên: `Mã PO`, `Mã ASN`, `SKU`, `Qty`, Danh sách sản phẩm (Tên sản phẩm, `SKU`, `Barcode`, Số lượng SPKPH, Ghi chú); `Chọn phương án xử lý` (default = `Null`, values: `Đã trả Nhà cung cấp`, `Đã tiêu huỷ`); Ghi chú; Hình ảnh và video bằng chứng | UI + Functional + Enum | High | ✅ | 07062#L799-L823 |
| R004 | Sau khi cập nhật đầy đủ thông tin và chụp hình, user chọn `Hoàn thành và xác nhận` → cập nhật status ASN theo phương án xử lý | Functional + State transition | High | ✅ | 07062#L824-L826 |
| R005 | Receiving PO trên App — user login App với tài khoản được cung cấp, vào tính năng `Receiving PO` | Functional + Auth | High | ✅ | 07062#L834-L838 |
| R006 | Step 1 — Hiện hướng dẫn ở màn hình scan PO cần nhận. Lưu ý: thông tin này **mặc định show khi user mới vào chức năng `Receiving PO`** | UI + UX | High | ✅ | 07062#L842-L843 |
| R007 | Step 2 — Scan mã PO cần nhận hàng. Validation `Scan mã PO` / `Scan PO code`: nếu PO **không yêu cầu VAT** → bỏ qua bước check verify invoice và force Invoice. Nếu PO có yêu cầu VAT mà **chưa được verify/approve hoặc không tồn tại** trên hệ thống → hiện thông báo | Validation | High | ✅ | 07062#L847-L854 |
| R008 | Step 2 — Validation thêm: nếu PO **không thuộc kho** đang xử lý → thông báo; PO **chưa được verify invoice** → thông báo; PO **đã được nhận hàng (received)** → thông báo | Validation | High | ✅ | 07062#L855-L860 |
| R009 | Step 2 — Nếu PO hợp lệ: (1) Show thông tin PO trên giao diện gồm `Mã PO chính (PO 1)`, `Nếu có add thêm PO Gift thì là PO 2`, `Tổng tiền`, `Tổng SKU` (đã scan nhận), `Tổng sản phẩm` (đã scan nhận); (2) Tạo ASN tương ứng với `ASN number` (hệ thống tự sinh), `Type = Purchase Order`, `Inbound Shipment` (mã của WMS), `Outbound Order` (mã của WMS), `Status = Receiving`. **Lưu ý:** chưa gọi API update status PO trên Inside thành `Receiving`. Chuyển qua bước tiếp theo | Functional + Auto-gen | High | ✅ | 07062#L861-L882 |
| R010 | Update 05-01-2026 — Bổ sung rules force SKU bất thường: khi scan PO nếu có 1 SKU thoả điều kiện trong PO có **qty < 100.000** → hiện thông báo và **không cho nhận** (không chuyển PO qua receiving). Các PO **không thuộc rules này** vẫn cho nhận bình thường | Business rule + Validation | High | ✅ | 07062#L883-L886 |
| R011 | Update 05-01-2026 — Bổ sung **filter** các PO thoả điều kiện này. Filter VN: `Cho phép nhận PO có SKU bất thường`; Filter EN: `Force receiving PO with abnormal SKUs` | Filter + UI | High | ✅ | 07062#L888-L889 |
| R012 | Update 05-01-2026 — Thông báo xác nhận khi force nhận PO bất thường: VN: `Bạn có muốn xác nhận cho phép nhận PO có SKU bất thường không?` / EN: `Do you want to confirm allowing receiving PO with abnormal SKUs?` | UX + Confirm dialog | High | ✅ | 07062#L890-L893 |
| R013 | Update 05-01-2026 — Bổ sung **nút force** cho các PO thoả điều kiện này để có thể force cho nhận nếu cần | UI + Functional | High | ✅ | 07062#L885-L895 |
| R014 | Step 3 — Chọn loại nhận hàng cho PO. Values: `Không đồng kiểm` (`No check of goods`) → user phải scan và nhận dưới camera → chuyển bước 4; `Có đồng kiểm` (`Check of goods`) → bỏ qua bước scan camera; nếu shop có quản lý location → chuyển bước scan vị trí; nếu shop không quản lý location → chuyển bước scan sản phẩm | Functional + Enum | High | ✅ | 07062#L904-L914 |
| R015 | Step 3 — Chọn `Đóng` để tắt popup và quay lại màn hình scan PO cần nhận (bước 2) | UI + Functional | High | ✅ | 07062#L915-L916 |
| R016 | Step 4 — Scan mã camera. User **chỉ phải scan camera nếu PO là Không đồng kiểm**. Field: `Scan mã camera` / `Scan camera code`. Hiển thị: `Tổng tiền`, `Loại nhận hàng (Receiving type)` | Functional + UI | High | ✅ | 07062#L919-L923 |
| R017 | Update 18-02-2025 — Bổ sung config `Required camera` tại `Master data / Warehouse / view Warehouse config / Tab Configuration / Group "General"`. Default = `No` (không cần scan camera cho chức năng được xét điều kiện này) | Config + UI | High | ✅ | 07062#L921-L935 |
| R018 | Update 18-02-2025 — Update Receiving PO trên App theo config: khi user scan nhận PO chọn `Không đồng kiểm` — nếu `Required camera = Yes` → phải scan camera; nếu `Required camera = No` → **bypass bước scan camera** (giống case PO `Đồng kiểm`) | Business rule | High | ✅ | 07062#L936-L940 |
| R019 | Step 4 — Validation mã camera: nếu **không thuộc kho hoặc không tồn tại** trên hệ thống → thông báo `Mã camera không hợp lệ hoặc không tồn tại trên hệ thống.` / `Camera code is invalid or does not exist on the system.` | Validation | High | ✅ | 07062#L945-L950 |
| R020 | Step 4 — Nếu mã camera hợp lệ: shop có quản lý location → scan mã vị trí cần chuyển hàng vào hoặc chọn chuyển vào giỏ; shop không quản lý location → chuyển bước scan sản phẩm | Functional | High | ✅ | 07062#L951-L956 |
| R021 | Step 5 — Scan vị trí / mã giỏ cần chuyển hàng vào. **Chỉ scan nếu shop/kho có quản lý theo location**. Hệ thống **tự động detect** thông tin user scan/nhập vào là mã `Bin` hay mã `giỏ` | Functional | High | ✅ | 07062#L958-L960 |
| R022 | Step 5 — **Rule cho PO zone:** sau khi scan camera (nếu có), hệ thống hiện thông báo lưu ý: với **PO zone chỉ được phép chuyển hàng vào location type `Di động`**, không được chuyển vào giỏ hoặc location khác | Business rule | High | ✅ | 07062#L961-L966 |
| R023 | Step 5 — PO zone validation vị trí: nếu mã vị trí không thuộc kho/không tồn tại → `Vị trí không hợp lệ hoặc không tồn tại trên hệ thống.` / `Location code is invalid or does not exist on the system.`. Nếu mã vị trí **không được thiết lập là bin Di động** → `Vị trí F2-AP-01-01-01-01 không được thiết lập để lưu trữ hàng cho PO zone.` / `Location F2-AP-01-01-01-01 is not setup to storage for PO zone.` | Validation | High | ✅ | 07062#L970-L981 |
| R024 | Step 5 — PO zone: nếu vị trí hợp lệ → chuyển bước scan sản phẩm; nếu user scan mã giỏ → hiện thông báo (raw không nêu verbatim — Q-003) | Functional + Validation | High | ⚠️ | 07062#L982-L984 |
| R025 | Step 5 — **Rule cho PO thường:** PO thường có thể nhận vào **bất kỳ location nào**. Nếu mã vị trí không thuộc kho/không tồn tại → `Vị trí không hợp lệ hoặc không tồn tại trên hệ thống.` / `Location code is invalid or does not exist on the system.` | Business rule + Validation | High | ✅ | 07062#L985-L994 |
| R026 | Step 5 — PO thường: nếu mã vị trí config là bin Di động → thông báo `Vị trí F0-A1-PL-50-01-01 là bin Di động, nên không thể lưu trữ hàng cho PO.` / `Location F2-AP-01-01-01-01 is not setup to storage for PO.` (lưu ý raw có inconsistency mã vị trí VN vs EN — Q-004). Vị trí hợp lệ → chuyển bước scan SP | Validation | High | ✅ | 07062#L997-L1004 |
| R027 | Step 5 — User scan mã giỏ: nếu mã giỏ không thuộc kho/không tồn tại → `Mã giỏ không hợp lệ hoặc không tồn tại trên hệ thống.` / `Cart code is invalid or does not exist on the system.`. Nếu mã giỏ có **trạng thái khác `Available` hoặc `Transfer Bin`** → `Mã giỏ 404005 có trạng thái không hợp lệ.` / `Cart code 404005 has invalid status.`. Mã giỏ hợp lệ → chuyển bước scan SP | Validation + Enum | High | ✅ | 07062#L1005-L1018 |
| R028 | Update 27-02-2024 — Bổ sung rules check và cập nhật thông tin location Di động (Pallet). **1 Bin location sẽ có thông tin `stock_id` và `location_id`** (bổ sung). 1 Bin location **sử dụng chung cho nhiều stock** trong cùng `location_id` (ví dụ Bin A có thể chung cho Shop 170 QL1A, WH 170 QL1A, WH 170 QL1A KT1... cùng thuộc location 170 QL1A). **Ở 1 thời điểm Bin A chỉ thuộc 1 stock duy nhất** | Data model + Business rule | High | ✅ | 07062#L1019-L1026 |
| R029 | Update 27-02-2024 — Rules khi nhận PO vào Bin di động (Pallet): trước nhận Bin A thuộc Shop 170 QL1A. Khi scan nhận PO mới vào Bin A: **(case 1)** PO thuộc Shop 170 QL1A → cho phép nhận bình thường (luồng cũ); **(case 2)** PO thuộc WH 170 QL1A → check: nếu Bin A đang có hàng (còn UID) → **báo lỗi không cho nhận**; nếu Bin A không còn hàng → cho nhận và **cập nhật stock_id của Bin A** từ Shop 170 QL1A thành WH 170 QL1A | Business rule + State transition | High | ✅ | 07062#L1027-L1035 |
| R030 | Case 1 (Chỉ nhận riêng PO thường — không có PO Gift) — Step 1: Nhập số lượng + Scan SKU cần nhận hàng. Field: `Tổng tiền` (Total Amount), `Tổng SKU` (Total SKU), `Tổng sản phẩm` (Total item). Validation: nếu SKU **không tồn tại trong PO** → thông báo `SKU 100540031 không có trong PO.` / `SKU 100540031 is not in PO.` | Functional + Validation | High | ✅ | 07062#L1038-L1044 |
| R031 | Case 1 — Validation: nếu số lượng của SKU **vượt quá số lượng confirm trong PO** → thông báo `Số lượng của SKU 100540031 lớn hơn số lượng cần nhận trong PO.` / `The quantity of SKU 100540031 is greater than the quantity required in the PO.` | Validation | High | ✅ | 07062#L1045-L1050 |
| R032 | Case 1 — SKU hợp lệ: nếu SKU **không yêu cầu nhập date** → cập nhật thông tin sản phẩm và số lượng scan lên màn hình; nếu SKU **yêu cầu nhập date** → show thông tin nhập HSD cho sản phẩm. Số lượng lấy từ thông tin nhập ở màn hình scan SKU và **cho phép chỉnh sửa** | Functional + UI | High | ✅ | 07062#L1051-L1057 |
| R033 | Case 1 — Validation HSD: nếu HSD **nhỏ hơn yêu cầu cho phép nhận hàng** → thông báo `Hạn sử dụng nhỏ hơn yêu cầu được phép nhận hàng của PO (9 tháng).` / `Expiration date is less than the PO permission request (9 months)` | Validation | High | ✅ | 07062#L1061-L1069 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User đăng nhập App WMS với tài khoản hợp lệ (R005).
- Warehouse config đã set `Required camera` (R017).
- PO tồn tại trên Inside + verify invoice (nếu yêu cầu VAT) (R007).

### Luồng chuẩn (Happy Path) — Receiving PO Step 1-5
1. **Step 1:** User vào `Receiving PO`, hiện hướng dẫn scan PO (R006).
2. **Step 2:** User scan mã PO. Validate: VAT verify, kho match, chưa received (R007, R008).
   - Pass: show info PO + tạo ASN status `Receiving` (chưa gọi API update Inside) (R009).
3. **Step 3:** User chọn loại nhận hàng (R014):
   - `Không đồng kiểm` → tiếp Step 4.
   - `Có đồng kiểm` → bypass camera → Step 5 (nếu shop quản lý location) hoặc Step nhận SP.
4. **Step 4 (nếu Không đồng kiểm):** Validate config `Required camera`:
   - `Required camera = No` → bypass (R018).
   - `Required camera = Yes` → user scan camera; validate hợp lệ → Step 5 (R016, R019).
5. **Step 5 (nếu shop quản lý location):** User scan vị trí hoặc giỏ (R021):
   - **PO zone:** bắt buộc location `Di động` (R022). Validate (R023).
   - **PO thường:** bất kỳ location nhưng không phải bin Di động (R025, R026).
   - **Mã giỏ:** validate status `Available` hoặc `Transfer Bin` (R027).
6. **Step nhận SP (Case 1 — PO thường, không Gift):** User nhập số lượng + scan SKU (R030):
   - SKU không trong PO → ERR (R030).
   - SL > confirm → ERR (R031).
   - SKU yêu cầu HSD → show form nhập HSD; validate HSD ≥ yêu cầu (R032, R033).

### Luồng chuẩn (Happy Path) — App Confirm Unsuitable Product (SPKPH)
1. User vào `App / Purchase order / Confirm Unsuitable Product` (R001).
2. Chọn kho → show danh sách ASN SPKPH status `Chờ NCC đến lấy` (R002).
3. User chọn phiên cần xác nhận → form mở với danh sách SP và `Chọn phương án xử lý` (R003).
4. User chọn `Đã trả Nhà cung cấp` hoặc `Đã tiêu huỷ`; nhập ghi chú + chụp hình/video bằng chứng (R003).
5. User click `Hoàn thành và xác nhận` → ASN status cập nhật theo phương án (R004).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — Force SKU bất thường (Update 05-01-2026):** PO có SKU qty < 100k → block default; user bật filter `Cho phép nhận PO có SKU bất thường` → nút force show → confirm dialog → cho nhận (R010, R011, R012, R013).
- **A2 — Đồng kiểm + shop quản lý location:** Step 3 chọn Đồng kiểm → bypass Step 4 → Step 5 scan vị trí.
- **A3 — Đồng kiểm + shop KHÔNG quản lý location:** Step 3 → Step nhận SP trực tiếp.
- **A4 — PO chuyển stock Bin Di động cùng location (Pallet):** PO thuộc Shop 170 QL1A nhận vào Bin A (Shop 170 QL1A) → bình thường (R029 case 1).
- **A5 — PO chuyển stock Bin Di động khác stock cùng location:** PO thuộc WH 170 QL1A scan Bin A (Shop 170 QL1A) → Bin A không UID → nhận và update `stock_id` (R029 case 2).

### Luồng ngoại lệ (Exception Paths)
- **E1 — PO không yêu cầu VAT:** bỏ qua check verify invoice (R007).
- **E2 — PO yêu cầu VAT chưa verify:** thông báo (R007).
- **E3 — PO không thuộc kho:** thông báo (R008).
- **E4 — PO đã received:** thông báo (R008).
- **E5 — Mã camera không hợp lệ:** ERR-APP-001 (R019).
- **E6 — PO zone scan vị trí không Di động:** ERR-APP-003 (R023).
- **E7 — PO thường scan vị trí Di động:** ERR-APP-004 (R026).
- **E8 — Mã giỏ trạng thái không hợp lệ:** ERR-APP-006 (R027).
- **E9 — Bin Di động đang có UID nhưng PO khác stock:** báo lỗi không cho nhận (R029).
- **E10 — SKU không trong PO:** ERR-APP-007 (R030).
- **E11 — Số lượng SKU vượt confirm:** ERR-APP-008 (R031).
- **E12 — HSD < yêu cầu:** ERR-APP-009 (R033).
- **E13 — SKU qty < 100.000 (Update 05-01-2026):** block default; cần force qua filter (R010).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Login App | rule | ✅ | Tài khoản được cung cấp |
| Filter ASN SPKPH | rule | ✅ | Chỉ ASN status `Chờ NCC đến lấy` của kho được chọn |
| Phương án xử lý SPKPH | enum | ✅ | Default `Null`; values {`Đã trả Nhà cung cấp`, `Đã tiêu huỷ`} |
| Hình ảnh/video bằng chứng SPKPH | media | ✅ | Bắt buộc trước khi `Hoàn thành và xác nhận` |
| Scan PO — VAT validation | rule | ✅ | PO không yêu cầu VAT → skip; PO yêu cầu VAT chưa verify/approve hoặc không tồn tại → block |
| Scan PO — Kho validation | rule | ✅ | PO phải thuộc kho user đang xử lý |
| Scan PO — Verify invoice | rule | ✅ | PO phải verify invoice (nếu yêu cầu VAT) trước khi nhận |
| Scan PO — Received check | rule | ✅ | PO đã received → block |
| ASN auto-gen | rule | ✅ | ASN number tự sinh; Type = `Purchase Order`; Status = `Receiving`; chưa gọi API Inside |
| SKU bất thường (05-01-2026) | rule | ✅ | Qty < 100.000 → block default; cần force qua filter `Cho phép nhận PO có SKU bất thường` |
| Force SKU bất thường | confirm | ✅ | Confirm dialog VN+EN trước khi nhận force |
| Loại nhận hàng | enum | ✅ | `Không đồng kiểm`/`Có đồng kiểm` |
| Camera scan | rule | ✅ | Chỉ `Không đồng kiểm`; bypass nếu `Required camera = No` |
| Warehouse `Required camera` config | enum | ✅ | Default `No`; values {`Yes`, `No`}; tab `Configuration / Group General` |
| Camera code validation | string | ✅ | Phải thuộc kho + tồn tại trên hệ thống |
| Vị trí (location) — PO zone | rule | ✅ | Bắt buộc bin `Di động`; không cho giỏ/location khác |
| Vị trí (location) — PO thường | rule | ✅ | Bất kỳ location nhưng KHÔNG bin Di động |
| Mã giỏ status | enum | ✅ | Phải ∈ {`Available`, `Transfer Bin`} |
| Bin Di động `stock_id` + `location_id` | data | ✅ | 1 Bin có cả 2 IDs; 1 location_id chia sẻ nhiều stock; 1 thời điểm chỉ thuộc 1 stock |
| Bin Di động — switch stock | rule | ✅ | Đang có UID + PO khác stock → block; không UID + PO khác stock → cho nhận + update `stock_id` |
| SKU validation (PO) | rule | ✅ | SKU phải trong PO; SL ≤ SL confirm |
| HSD validation | rule | ✅ | HSD ≥ yêu cầu cho phép nhận hàng của PO (default 9 tháng) |
| Số lượng nhập | rule | ✅ | Cho phép chỉnh sửa khi nhập HSD |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-APP-001 | Validation | Mã camera không thuộc kho hoặc không tồn tại | `Mã camera không hợp lệ hoặc không tồn tại trên hệ thống.` | `Camera code is invalid or does not exist on the system.` | 07062#L947-L950 |
| ERR-APP-002 | Validation | Mã vị trí không thuộc kho/không tồn tại (PO zone) | `Vị trí không hợp lệ hoặc không tồn tại trên hệ thống.` | `Location code is invalid or does not exist on the system.` | 07062#L972-L975 |
| ERR-APP-003 | Validation | PO zone scan vị trí không phải bin Di động | `Vị trí F2-AP-01-01-01-01 không được thiết lập để lưu trữ hàng cho PO zone.` | `Location F2-AP-01-01-01-01 is not setup to storage for PO zone.` | 07062#L978-L981 |
| ERR-APP-004 | Validation | PO thường scan vị trí là bin Di động | `Vị trí F0-A1-PL-50-01-01 là bin Di động, nên không thể lưu trữ hàng cho PO.` | `Location F2-AP-01-01-01-01 is not setup to storage for PO.` (lưu ý: EN có inconsistency mã — Q-004) | 07062#L999-L1002 |
| ERR-APP-005 | Validation | Mã giỏ không thuộc kho/không tồn tại | `Mã giỏ không hợp lệ hoặc không tồn tại trên hệ thống.` | `Cart code is invalid or does not exist on the system.` | 07062#L1008-L1011 |
| ERR-APP-006 | Validation | Mã giỏ có trạng thái khác `Available` / `Transfer Bin` | `Mã giỏ 404005 có trạng thái không hợp lệ.` | `Cart code 404005 has invalid status.` | 07062#L1014-L1016 |
| ERR-APP-007 | Validation | SKU không tồn tại trong PO | `SKU 100540031 không có trong PO.` | `SKU 100540031 is not in PO.` | 07062#L1042-L1044 |
| ERR-APP-008 | Validation | Số lượng SKU vượt quá SL confirm PO | `Số lượng của SKU 100540031 lớn hơn số lượng cần nhận trong PO.` | `The quantity of SKU 100540031 is greater than the quantity required in the PO.` | 07062#L1047-L1050 |
| ERR-APP-009 | Validation | HSD < yêu cầu cho phép nhận hàng | `Hạn sử dụng nhỏ hơn yêu cầu được phép nhận hàng của PO (9 tháng).` | `Expiration date is less than the PO permission request (9 months)` | 07062#L1063-L1069 |
| MSG-APP-010 | Confirm | Force nhận PO có SKU bất thường (Update 05-01-2026) | `Bạn có muốn xác nhận cho phép nhận PO có SKU bất thường không?` | `Do you want to confirm allowing receiving PO with abnormal SKUs?` | 07062#L891-L893 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Login App + vào Receiving PO**
  - **Given:** User có tài khoản hợp lệ.
  - **When:** User login App + chọn `Receiving PO`.
  - **Then:** Hệ thống mở màn hình scan PO với hướng dẫn show ngay lần đầu vào (R005, R006).
- **AC-02 — PO không yêu cầu VAT → skip verify**
  - **Given:** PO không yêu cầu VAT.
  - **When:** User scan mã PO.
  - **Then:** Bypass check verify invoice và force Invoice (R007).
- **AC-03 — PO yêu cầu VAT chưa verify**
  - **Given:** PO yêu cầu VAT, invoice chưa verify.
  - **When:** User scan mã PO.
  - **Then:** Hiện thông báo block, không cho nhận (R007).
- **AC-04 — PO không thuộc kho**
  - **Given:** User đang xử lý kho A, PO thuộc kho B.
  - **When:** User scan PO.
  - **Then:** Thông báo block (R008).
- **AC-05 — PO đã received**
  - **Given:** PO đã received trước đây.
  - **When:** User scan lại.
  - **Then:** Thông báo block (R008).
- **AC-06 — PO hợp lệ → tạo ASN status Receiving**
  - **Given:** PO hợp lệ.
  - **When:** User scan PO thành công.
  - **Then:** Hệ thống show info PO + tạo ASN với status `Receiving`, **chưa gọi API update Inside** (R009).
- **AC-07 — Update 05-01-2026: SKU qty < 100k block**
  - **Given:** PO có SKU qty = 50.000 (< 100k).
  - **When:** User scan PO.
  - **Then:** Block default, không cho nhận (R010).
- **AC-08 — Update 05-01-2026: force qua filter**
  - **Given:** PO có SKU qty < 100k. User bật filter `Cho phép nhận PO có SKU bất thường`.
  - **When:** User scan PO + click nút force.
  - **Then:** Confirm dialog MSG-APP-010 → user xác nhận → cho nhận (R011, R012, R013).
- **AC-09 — Chọn Đồng kiểm + shop quản lý location**
  - **Given:** Shop quản lý location.
  - **When:** User chọn `Có đồng kiểm` ở Step 3.
  - **Then:** Bypass Step 4 camera → chuyển Step 5 scan vị trí (R014).
- **AC-10 — Chọn Đồng kiểm + shop không quản lý location**
  - **Given:** Shop không quản lý location.
  - **When:** User chọn `Có đồng kiểm`.
  - **Then:** Bypass Step 4 + Step 5 → chuyển bước scan SP trực tiếp (R014).
- **AC-11 — Update 18-02-2025: Required camera = No bypass**
  - **Given:** Warehouse config `Required camera = No`.
  - **When:** User chọn `Không đồng kiểm`.
  - **Then:** Bypass Step 4 scan camera (R018).
- **AC-12 — Update 18-02-2025: Required camera = Yes phải scan**
  - **Given:** Warehouse config `Required camera = Yes`.
  - **When:** User chọn `Không đồng kiểm`.
  - **Then:** User phải scan camera ở Step 4 (R018).
- **AC-13 — Mã camera không hợp lệ**
  - **Given:** User scan mã camera không thuộc kho.
  - **When:** Validation.
  - **Then:** ERR-APP-001 hiện (R019).
- **AC-14 — PO zone chỉ Di động**
  - **Given:** PO zone, user scan vị trí `F2-AP-01-01-01-01` không phải bin Di động.
  - **When:** Validation.
  - **Then:** ERR-APP-003 hiện (R023).
- **AC-15 — PO thường không vào Di động**
  - **Given:** PO thường, user scan `F0-A1-PL-50-01-01` là bin Di động.
  - **When:** Validation.
  - **Then:** ERR-APP-004 hiện (R026).
- **AC-16 — Mã giỏ status không hợp lệ**
  - **Given:** Mã giỏ `404005` status `Locked` (không phải `Available` hoặc `Transfer Bin`).
  - **When:** User scan giỏ.
  - **Then:** ERR-APP-006 hiện (R027).
- **AC-17 — Update 27-02-2024: Bin Di động cùng stock OK**
  - **Given:** Bin A thuộc Shop 170 QL1A. PO thuộc Shop 170 QL1A.
  - **When:** User scan Bin A.
  - **Then:** Cho phép nhận bình thường (R029 case 1).
- **AC-18 — Update 27-02-2024: Bin Di động khác stock có UID block**
  - **Given:** Bin A thuộc Shop 170 QL1A đang có UID. PO thuộc WH 170 QL1A.
  - **When:** User scan Bin A.
  - **Then:** Báo lỗi không cho nhận (R029).
- **AC-19 — Update 27-02-2024: Bin Di động khác stock không UID switch**
  - **Given:** Bin A thuộc Shop 170 QL1A, đã hết UID. PO thuộc WH 170 QL1A.
  - **When:** User scan Bin A.
  - **Then:** Cho nhận + `stock_id` của Bin A update từ Shop 170 QL1A → WH 170 QL1A (R029).
- **AC-20 — SKU không tồn tại trong PO**
  - **Given:** User scan SKU `100540031` không có trong PO.
  - **When:** Validation.
  - **Then:** ERR-APP-007 hiện (R030).
- **AC-21 — SL SKU vượt SL confirm**
  - **Given:** PO confirm SKU `100540031` SL = 10. User scan đã 11.
  - **When:** Validation.
  - **Then:** ERR-APP-008 hiện (R031).
- **AC-22 — SKU yêu cầu HSD → form nhập date**
  - **Given:** SKU yêu cầu nhập date.
  - **When:** User scan SKU thành công.
  - **Then:** Form HSD mở với số lượng prefill từ scan SKU, cho phép chỉnh sửa (R032).
- **AC-23 — HSD < yêu cầu PO**
  - **Given:** PO yêu cầu HSD ≥ 9 tháng. User nhập HSD = 6 tháng.
  - **When:** Validation.
  - **Then:** ERR-APP-009 hiện (R033).
- **AC-24 — App Confirm Unsuitable — danh sách ASN SPKPH theo kho**
  - **Given:** User vào `Confirm Unsuitable Product`, chọn kho A.
  - **When:** Hệ thống load.
  - **Then:** Danh sách hiện các ASN SPKPH status `Chờ NCC đến lấy` của kho A (R002).
- **AC-25 — Confirm Unsuitable — chọn phương án `Đã trả NCC`**
  - **Given:** Phiên SPKPH mở.
  - **When:** User chọn `Đã trả Nhà cung cấp` + ghi chú + chụp hình → click `Hoàn thành và xác nhận`.
  - **Then:** ASN status cập nhật theo phương án (R004).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R009 | "Lưu ý khi này chưa gọi API để update status PO trên Inside thành Receiving" — vậy khi nào API được gọi? Sau scan vị trí, sau scan SP đầu tiên, hay sau Hoàn thành PO? Có endpoint cụ thể không? | Dev | Open | | | |
| Q-002 | R017 | Config `Required camera` của Warehouse — chỉ apply cho `Không đồng kiểm` hay cả `Đồng kiểm`? Group `General` còn config nào khác liên quan không? | PO/Dev | Open | | | |
| Q-003 | R024 | Khi user scan mã giỏ trong flow PO zone (không được phép giỏ), verbatim message hiển thị là gì? Raw chỉ nói "hiện thông báo" không có message. | PO/UX | Open | | | |
| Q-004 | R026, ERR-APP-004 | Raw có inconsistency: VN message `Vị trí F0-A1-PL-50-01-01 là bin Di động` nhưng EN `Location F2-AP-01-01-01-01 is not setup to storage for PO` (mã vị trí khác nhau). Đúng verbatim 2 ngôn ngữ là gì? | PO/UX | Open | | | |
| Q-005 | R010 | "Qty < 100.000" — đơn vị là gì? Tổng SL SKU (number of units), hay tổng tiền (VND)? Raw chỉ nói "qty" — Q clarify. | PO | Open | | | |
| Q-006 | R011, R013 | Filter `Cho phép nhận PO có SKU bất thường` + nút force — filter này ở màn hình nào (App list PO, hay setting riêng)? Quyền sử dụng (nhân viên kho hay manager only)? | PO | Open | | | |
| Q-007 | R022 | "PO zone" định nghĩa là gì? Khác PO thường thế nào (vd flag trên master PO, hay rule per kho)? | PO/Dev | Open | | | |
| Q-008 | R027 | Mã giỏ trạng thái `Available` và `Transfer Bin` — đây là 2 trạng thái valid duy nhất, hay còn trạng thái khác valid không (vd `Empty`)? Enum đầy đủ? | PO/Dev | Open | | | |
| Q-009 | R028, R029 | "stock_id" — đây có phải là warehouse_id (Shop vs WH) không? Hay là 1 đại lượng khác? Sao 1 location_id có thể chia sẻ nhiều stock_id? | Dev | Open | | | |
| Q-010 | R033 | "9 tháng" trong message HSD — đây là default hay configurable per PO/SKU? Có doc rules tính ngày nhận hàng tối thiểu chưa (raw mention "06-01-2025: cập nhật rules tính ngày nhận hàng tối thiếu" ở L1070 — bắt đầu section khác)? | PO | Open | | | |
| Q-011 | R032 | "Cho phép chỉnh sửa" số lượng khi nhập HSD — sau chỉnh sửa, SL nhập có validate lại vs SL confirm PO không? Có thể nhập 0 không? | PO/UX | Open | | | |
| Q-012 | R003 | "Số lượng SPKPH" và "Số lượng" trong danh sách SP phiên SPKPH — 2 field khác nhau hay alias? Raw có cả 2 mention. | PO | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-15..S-20 | 2.17 (stub) | 2.17 | All R + AC | Draft |
| CHG-002 | Add | Update 18-02-2025: bổ sung config `Required camera` per Warehouse + bypass camera khi `= No` | (trước 2.17) | 2.17 | R017, R018, AC-11, AC-12 | Done (đã trong raw v2.17) |
| CHG-003 | Add | Update 27-02-2024: rules Bin di động (Pallet) — stock_id + location_id, switch stock | (trước 2.17) | 2.17 | R028, R029, AC-17, AC-18, AC-19 | Done (đã trong raw v2.17) |
| CHG-004 | Add | Update 05-01-2026: rules force SKU bất thường (qty < 100k) + filter + nút force | (trước 2.17) | 2.17 | R010-R013, AC-07, AC-08 | Done (đã trong raw v2.17) |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_app | test_stub_receiving_po_app | Add (chờ Gate 1B) | [[stub_receiving_po_vas]] (SPKPH ASN), [[stub_receiving_po_inbound_shipment]] (ASN sinh ra), [[stub_receiving_po_invoice]] (verify VAT), [[stub_receiving_po_date_rules]] (HSD ≥ 9 tháng rules), [[stub_receiving_po_confirm_paste_id]] (post-scan flow), [[stub_receiving_po_asn]] (ASN status), [[stub_receiving_po_fabric]] (scan SP Vải) | Q-001..Q-012 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R033, AC-01..AC-25 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-012 |

## 🚧 Blocked Coverage

- R009 — chờ Q-001 (API update Inside endpoint)
- R017 — chờ Q-002 (scope config `Required camera`)
- R024 — chờ Q-003 (verbatim message PO zone scan giỏ)
- R026, ERR-APP-004 — chờ Q-004 (inconsistency mã VN vs EN)
- R010 — chờ Q-005 (đơn vị "100.000")
- R011, R013 — chờ Q-006 (filter location + quyền)
- R022 — chờ Q-007 (định nghĩa PO zone)
- R027 — chờ Q-008 (enum status mã giỏ)
- R028, R029 — chờ Q-009 (stock_id semantics)
- R033 — chờ Q-010 (9 tháng configurable)
- R032 — chờ Q-011 (re-validate SL khi chỉnh sửa)
- R003 — chờ Q-012 ("Số lượng SPKPH" vs "Số lượng" semantics)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 19:50:00 | v1.1 | Refine stub → full spec: 33 R-ID, 25 AC, 23 BR, 10 messages (9 verbatim VN+EN, 1 với typo Q-004), 12 questions Open. `partial_read: false`. | refine-batch-4-2026-05-30 |
