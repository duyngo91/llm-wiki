---
aliases: [stub_qc_evaluation_manual]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_qc_evaluation_manual
project: project_hasaki
source_version: 1.5
source_doc: 07105_Quality_Control_Docs_ver1.5.md
source_range: 07105#L1023-L1304
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-31 17:50:34"
verification_status: Verified
approved_by:
approved_at:
approval_note:
last_verified_source_version: 1.5

---

# REQ: stub_qc_evaluation_manual

## Tổng quan
- **Mã tính năng:** stub_qc_evaluation_manual
- **Feature:** Tạo mới đánh giá Manual + SKU phụ liệu Return + Blocked UID Damaged + Tiêu chí 4 điểm / Theo từng bước
- **Mô tả ngắn:** Module tạo đánh giá chất lượng SKU thủ công ngoài luồng auto-trigger từ ASN. Cũ (S-29 — đã `(bỏ)`): flow Step 1-2 chọn PO + đánh giá. Mới (Update 11-02-2026 + 12-02-2026, S-32-S-33): Step 1-3 — Tìm SP (SKU/barcode/tên) + load 10 PO nhận gần nhất; Step 2 Khai báo UID group + SL cần đánh giá với validation; Step 3 Đánh giá chất lượng từng tiêu chí (Fail required chụp hình + ghi chú, max 5 hình/tiêu chí). Update 20-04-2026 (S-34): Đánh giá SKU phụ liệu (SKU thường, không phải Thời trang NVL + không Vải) — nếu kết quả Failed → màn xác nhận tạo Adjustment xuất trả NCC với type Export, Reason Return to vendor, status `Waiting for approval`. S-35: Blocked UID group cho SKU Vải Failed → tự blocked tất UID group cùng PO + LOT + chuyển product status UID = `Damaged` (không cộng stock Available). Un-Blocked → auto chuyển `Normal`. Update 10-05-2026: Tiêu chí 4 điểm + Tiêu chí theo từng bước — auto inherit thiết lập tiêu chí khi assign cho SKU.
- **Source chính:** 07105_Quality_Control_Docs_ver1.5.md (v1.5)
- **Đối tượng sử dụng (Actors):** QC team, BOD (approve Adjustment), Quản lý stock.
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** [[ts_qc_evaluation_manual]]
- **API Spec liên quan:** N/A — raw không mô tả API explicit; mention "load 3 option khi tạo Adjustment" và "rules của Adjustment hiện tại".
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_qc_criteria_setup]] (thiết lập tiêu chí), [[stub_qc_criteria_sku]] (tiêu chí SKU), [[stub_qc_uid_group]] (UID group khai báo SL). ↔️ liên quan [[stub_qc_evaluation_mobile]] (Mobile evaluation flow), [[stub_qc_evaluation_result]] (kết quả tổng hợp). ➡️ feed Adjustment system (Return to vendor) + Inventory system (UID Damaged state).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07105_Quality_Control_Docs_ver1.5.md | 1.5 | ✅ Hiện hành |
| 2 | Figma mockup (Update 11-02-2026) | https://www.figma.com/design/CLtzJtUv6sA4rxyaBPnbz5/34.-Quality-Control?node-id=1946-1696 | — | Hiện hành (Q-001) |
| 3 | Figma mockup (Update 20-04-2026) | https://www.figma.com/design/CLtzJtUv6sA4rxyaBPnbz5/34.-Quality-Control?node-id=2542-554 | — | Hiện hành (Q-001) |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | Adjustment Create endpoint (Type: Export, Reason: Return to vendor) — raw không nêu endpoint | R015 | 07105#L1255-L1291 | TBD — Q-002 |
| N/A | UID Blocked + Product status change API — raw không nêu endpoint | R018, R019 | 07105#L1292-L1302 | TBD — Q-002 |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | (Bỏ — deprecated) Flow cũ `Tạo mới đánh giá – Manual` tại `Menu: Purchase Order / Quality Control` với Step 1 chọn kho + Tạo mới + tìm SP (SKU/barcode/tên SP) + load 10 PO gần nhất + tìm mã PO chính xác. **Phần này đã bỏ — xem update mới ngày 12-02-2026** | Deprecated | Low | ⚠️ | 07105#L1023-L1038 |
| R002 | (Bỏ — deprecated) Step 2 cũ: chọn PO cần đánh giá → `Bắt đầu đánh giá`. Nếu SKU chưa thiết lập tiêu chí → thông báo. Thông tin: SKU+Tên, PO, SL, NCC, Ghi chú (editable), Tiêu chí đạt/không đạt. Danh sách tiêu chí lấy theo thiết lập SKU. Mỗi tiêu chí: Thứ tự, Tên, Mô tả, Mô tả điều kiện theo SKU, Đạt/Không đạt, Hình ảnh (Fail required chụp + ghi chú, max 5 hình). `Hoàn thành` để xác nhận | Deprecated | Low | ⚠️ | 07105#L1040-L1077 |
| R003 | Update 11-02-2026 — Section heading marker dẫn vào flow mới (Tạo mới đánh giá Manual S-32+S-33 ở L1173+) | Documentation | Low | ⚠️ | 07105#L1078-L1080 |
| R004 | (Mới) Step 1 — Tạo mới đánh giá. `Menu: Purchase Order / Quality Control`. User chọn kho + chọn `Tạo mới`. Thông tin: tìm SP (hỗ trợ SKU/barcode/tên SP — chọn để mở modal tìm rộng); load 10 PO nhận gần nhất của SKU được chọn theo kho; tìm mã PO chính xác (tìm trong tất cả PO chứa SKU đã chọn). Chọn `Tiếp tục` → nếu SKU chưa thiết lập tiêu chí → thông báo (verbatim Q-003) | Functional + UI | High | ✅ | 07105#L1176-L1187 |
| R005 | (Mới) Step 2 — Khai báo UID group và số lượng cần đánh giá. Thông tin: `SKU + tên SP`, `Mã PO đã chọn`, `Ngày nhận PO`, `Nhà cung cấp của PO`, `Ghi chú`, `UID group` (bắt buộc, khai báo UID cần đánh giá), `Số lượng cần đánh giá` (bắt buộc, cập nhật SL). Chọn `Bắt đầu đánh giá` → validate | Functional + UI + Validation | High | ✅ | 07105#L1190-L1206 |
| R006 | (Mới) Step 2 validation — Nếu UID group không tồn tại → `Mã UID không tồn tại.` Nếu SL cần khai báo không đủ SL trong UID group → `Số lượng trong UID group không đủ số lượng yêu cầu.` Ngược lại → chuyển bước tiếp theo | Validation | High | ✅ | 07105#L1201-L1205 |
| R007 | (Mới) Step 3 — Đánh giá chất lượng cho SP. Thông tin: `Nhóm UID`, `Số lượng đang có của nhóm UID`, `Số lô`, `Hạn sử dụng`, `SL cần đánh giá`, `Mã PO`, `Nhà cung cấp` (từ PO), `Sản phẩm` (SKU – Tên), `Ghi chú` (editable), `Tiêu chí đạt`, `Tiêu chí không đạt`. Danh sách tiêu chí lấy theo thiết lập SKU | UI + Functional | High | ✅ | 07105#L1210-L1222 |
| R008 | (Mới) Step 3 — Thông tin từng tiêu chí: `Thứ tự`, `Tên tiêu chí`, `Mô tả`, `Mô tả điều kiện theo SKU`, `Đạt/Không đạt`, `Hình ảnh` (theo config required chụp). Nếu Fail → required chụp hình và nhập ghi chú. Max 5 hình/tiêu chí (nếu yêu cầu) | UI + Validation | High | ✅ | 07105#L1223-L1235 |
| R009 | (Mới) Step 3 — Đánh giá và cập nhật thông tin cho tất cả tiêu chí → chọn `Hoàn thành` để xác nhận đánh giá xong | Functional | High | ✅ | 07105#L1237-L1238 |
| R010 | Update 20-04-2026 — Section heading dẫn vào Đánh giá SKU phụ liệu | Documentation | Low | ⚠️ | 07105#L1242-L1242 |
| R011 | Update 20-04-2026 — Đánh giá SKU phụ liệu (SKU thường). **Áp dụng cho SKU KHÔNG PHẢI là cate `Thời trang (NVL)` và không phải là `Vải`** | Business rule + Scope | High | ✅ | 07105#L1243-L1246 |
| R012 | Đánh giá SKU phụ liệu — Sau khi đánh giá tất cả tiêu chí, nếu kết quả đánh giá cuối cùng bị **Failed** (có ≥ 1 kết quả failed) → hiển thị màn hình để user xác nhận **số lượng cần trả hàng cho NCC** | Business rule + Functional | High | ✅ | 07105#L1247-L1249 |
| R013 | Đánh giá SKU phụ liệu — Confirm dialog: `SKU 422280022 has evaluation criteria marked as FAILED. Do you want to create an adjustment voucher to export the failed quantity for return to vendor?`. Option `Để sau (Later)` để tắt dialog quay về danh sách SKU cần đánh giá; Option `Tạo phiếu điều chỉnh (Create adjustment)` để tiến hành | Confirm + UI | High | ✅ | 07105#L1250-L1255 |
| R014 | Đánh giá SKU phụ liệu — Form `Tạo phiếu điều chỉnh`: `Số lượng cần xuất trả nhà cung cấp` (Quantity to Return to vendor). Validation: nhập SL cần trả; **SL phải < SL nhập hàng PO**. Options: `Đóng` (tắt) / `Xác nhận` (tạo Adjustment) | Validation + Functional | High | ✅ | 07105#L1256-L1262 |
| R015 | Đánh giá SKU phụ liệu — Adjustment được tạo với: `Warehouse` = kho phát sinh; `Type` = `Export`; `Reason` = `Return to vendor`; `Vendor` = lấy từ source PO khi đánh giá SKU; `Require VAT` = 3 option load cho user chọn — (a) `No – Trả hàng không xuất hoá đơn`, (b) `Yes VAT - Hasaki xuất hoá đơn bán hàng cho NCC`, (c) `Yes VAT – NCC xuất hoá đơn điều chỉnh cho HASAKI`; `Source code` = Mã PO khi đánh giá; `Required picking` = `No`; `ADJ status` = `Waiting for approval` | Functional + Business rule + Enum | High | ✅ | 07105#L1263-L1284 |
| R016 | Đánh giá SKU phụ liệu — Thông tin SKU trong Adjustment: `SKU` lấy theo thông tin user request; `Số lượng` lấy theo input của user; `VAT` và `Price` lấy theo thông tin của SKU trên Inside theo **rules của Adjustment hiện tại** | Business rule + Data integration | High | ✅ | 07105#L1285-L1291 |
| R017 | S-35 — Blocked UID group và chuyển Damaged. **Áp dụng cho SKU vải**: khi đánh giá có kết quả Failed → hệ thống tự động **blocked lại tất cả UID group của SKU nhận trong cùng PO và cùng LOT** | Business rule + State transition | High | ✅ | 07105#L1292-L1294 |
| R018 | S-35 — Đồng thời chuyển **Product status của các UID** của các UID group này thành `Damaged` để **không cộng vào stock Available** (không thể IT/picklisted) | Business rule + State transition | High | ✅ | 07105#L1295-L1297 |
| R019 | S-35 — Khi user **Un-Blocked UID group**: ngoài việc unblock UID group về `Available` thì sẽ **auto chuyển UID từ Product status `Damaged` thành `Normal`** | Business rule + State transition | High | ✅ | 07105#L1298-L1300 |
| R020 | Update 10-05-2026 — Thiết lập **tiêu chí 4 điểm** khi thiết lập tiêu chí. Tại màn thiết lập tiêu chí, nếu chọn phân loại là `Lỗi 4 điểm` (4 points error) thì khi nhấn `Tạo` → hệ thống mở thêm màn để thiết lập các nội dung cho tiêu chí 4 điểm, **giống với khi thiết lập tiêu chí cho SKU** | Functional + UI | High | ✅ | 07105#L1304-L1308 |
| R021 | Update 10-05-2026 — Khi thiết lập tiêu chí cho SKU, nếu chọn tiêu chí 4 điểm thì hệ thống **tự lấy các thiết lập của tiêu chí để cập nhật cho SKU**, mà không cần phải thiết lập lại cho từng SKU | Business rule + Auto-inherit | High | ✅ | 07105#L1309-L1311 |
| R022 | Update 10-05-2026 — Thiết lập **đánh giá từng bước** khi thiết lập tiêu chí. Tại màn thiết lập, nếu chọn phân loại `Theo từng bước` (Step by step) thì khi nhấn `Tạo` → mở thêm màn thiết lập các nội dung từng bước cho tiêu chí, giống với khi thiết lập tiêu chí cho SKU | Functional + UI | High | ✅ | 07105#L1312-L1315 |
| R023 | Update 10-05-2026 — Khi thiết lập tiêu chí cho SKU, nếu chọn tiêu chí `Theo từng bước` thì hệ thống **tự lấy các thiết lập của tiêu chí để cập nhật cho SKU**, mà không cần phải thiết lập lại cho từng SKU | Business rule + Auto-inherit | High | ✅ | 07105#L1320-L1321 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User có quyền QC.
- SKU cần đánh giá đã được thiết lập tiêu chí (xem [[stub_qc_criteria_setup]]).
- (Cho Step 2 Manual) UID group của SKU đã tồn tại với SL ≥ SL cần đánh giá.

### Luồng chuẩn (Happy Path) — Tạo mới đánh giá Manual mới (Update 11-02-2026)
1. User vào `Purchase Order / Quality Control` chọn kho + `Tạo mới` (R004).
2. **Step 1:** Tìm SP theo SKU/barcode/tên (modal mở rộng nếu cần) (R004).
3. Hệ thống load 10 PO gần nhất của SKU theo kho. User có thể tìm mã PO chính xác (R004).
4. User chọn PO + click `Tiếp tục`. Nếu SKU chưa có tiêu chí → thông báo (R004).
5. **Step 2:** Form khai báo UID group mở (R005):
   - User nhập `UID group` (bắt buộc).
   - User nhập `Số lượng cần đánh giá` (bắt buộc).
6. Click `Bắt đầu đánh giá` → validate (R006):
   - UID không tồn tại → ERR-EVM-001.
   - SL > SL trong UID group → ERR-EVM-002.
   - Valid → tiếp Step 3.
7. **Step 3:** Hiển thị thông tin (Nhóm UID, SL đang có, Số lô, HSD, SL cần đánh giá, ...) + danh sách tiêu chí (R007, R008).
8. User đánh giá từng tiêu chí: Đạt / Không đạt. Fail → chụp hình + ghi chú; max 5 hình (R008).
9. User click `Hoàn thành` → đánh giá xong (R009).

### Luồng chuẩn (Happy Path) — Update 20-04-2026: SKU phụ liệu Failed → Adjustment
1. SKU `SP-A` thuộc cate phụ liệu (không Thời trang NVL, không Vải) (R011).
2. User đánh giá Manual → kết quả Failed (≥ 1 tiêu chí Fail) (R012).
3. Confirm dialog mở: `SKU 422280022 has evaluation criteria marked as FAILED. Do you want to create an adjustment voucher to export the failed quantity for return to vendor?` (R013).
4. User chọn `Tạo phiếu điều chỉnh`:
   - Form nhập `Số lượng cần xuất trả` = `Y`. Validate: `Y` < SL nhập PO (R014).
   - User chọn `Require VAT` = 1 trong 3 option (R015).
   - User click `Xác nhận`.
5. Hệ thống tạo Adjustment với:
   - Warehouse = kho phát sinh
   - Type = Export
   - Reason = Return to vendor
   - Vendor = từ source PO
   - Source code = Mã PO
   - Required picking = No
   - ADJ status = Waiting for approval (R015)
6. SKU info: SL = user input; VAT + Price lấy từ Inside theo rules ADJ hiện tại (R016).

### Luồng chuẩn (Happy Path) — S-35: SKU vải Failed → Blocked UID + Damaged
1. SKU `Vải-X` được đánh giá QC, kết quả Failed (R017).
2. Hệ thống auto blocked **tất cả UID group** của SKU `Vải-X` **trong cùng PO** và **cùng LOT** (R017).
3. Hệ thống chuyển product status của các UID trong các UID group này → `Damaged` (R018).
4. Stock Available không cộng các UID `Damaged` (không thể IT/picklisted) (R018).
5. Sau xử lý xong, user `Un-Blocked` UID group → unblock về `Available` + UID `Damaged → Normal` (R019).

### Luồng chuẩn (Happy Path) — Update 10-05-2026 Tiêu chí 4 điểm
1. User thiết lập tiêu chí với phân loại `Lỗi 4 điểm` (R020).
2. Click `Tạo` → màn thiết lập 4 điểm mở (giống flow tiêu chí cho SKU) (R020).
3. User định nghĩa các loại lỗi (1, 2, 3, 4 điểm), hệ số.
4. Lưu tiêu chí. Khi assign tiêu chí này cho SKU → hệ thống auto load thiết lập, không cần config lại (R021).

### Luồng chuẩn (Happy Path) — Update 10-05-2026 Tiêu chí từng bước
1. User thiết lập tiêu chí với phân loại `Theo từng bước` (R022).
2. Click `Tạo` → màn thiết lập từng bước mở.
3. User định nghĩa các bước (Hình ảnh + Kết quả + Ghi chú per bước).
4. Khi assign cho SKU → auto inherit (R023).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — Flow cũ (deprecated):** không dùng nữa, mọi user phải dùng flow mới Update 11-02-2026 (R001, R002).
- **A2 — SKU phụ liệu Failed nhưng user `Để sau`:** dialog đóng, user quay về danh sách. Không tạo ADJ (R013).
- **A3 — Require VAT = No:** Adjustment trả hàng không xuất hoá đơn (R015 option a).
- **A4 — Require VAT = Yes VAT (Hasaki xuất):** Hasaki xuất hoá đơn bán hàng cho NCC (R015 option b).
- **A5 — Require VAT = Yes VAT (NCC xuất):** NCC xuất hoá đơn điều chỉnh cho HASAKI (R015 option c).

### Luồng ngoại lệ (Exception Paths)
- **E1 — Step 1 SKU chưa thiết lập tiêu chí:** ERR/thông báo block (R004 — verbatim Q-003).
- **E2 — Step 2 UID không tồn tại:** ERR-EVM-001 (R006).
- **E3 — Step 2 SL > SL trong UID group:** ERR-EVM-002 (R006).
- **E4 — SKU phụ liệu ADJ — SL trả > SL nhập PO:** validation block (R014).
- **E5 — Vải Failed → tự blocked + Damaged → User cố IT:** UID không picklisted (R018).
- **E6 — User Un-Blocked sau khi đã xử lý vendor return:** UID chuyển Normal (R019); cần verify case lệnh return có chưa Out (Q-007).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Flow cũ (deprecated) | rule | ✅ | `(bỏ)` — không dùng flow Step 1-2 ở L1023-L1077 |
| Step 1 Tìm SP | rule | ✅ | Hỗ trợ SKU/barcode/tên SP; load 10 PO gần nhất + tìm chính xác mã PO |
| Step 1 SKU chưa thiết lập tiêu chí | rule | ✅ | Block, không cho `Tiếp tục` |
| `UID group` (Step 2) | string | ✅ | Phải tồn tại trên hệ thống |
| `Số lượng cần đánh giá` (Step 2) | integer | ✅ | ≤ SL trong UID group |
| Step 3 SP info | rule | ✅ | Lấy theo PO (NCC) + master SKU |
| Step 3 tiêu chí Fail | rule | ✅ | Required chụp hình + nhập ghi chú; max 5 hình/tiêu chí |
| Step 3 Hoàn thành | rule | ✅ | Tất cả tiêu chí phải có Đạt/Không đạt |
| Scope SKU phụ liệu | rule | ✅ | KHÔNG `Thời trang (NVL)` + KHÔNG `Vải` |
| Failed trigger ADJ | rule | ✅ | ≥ 1 tiêu chí Fail → hiện confirm dialog tạo ADJ |
| ADJ SL trả NCC | integer | ✅ | < SL nhập hàng PO |
| ADJ Type | enum | ✅ | `Export` |
| ADJ Reason | enum | ✅ | `Return to vendor` |
| ADJ Require VAT | enum | ✅ | ∈ {`No – Trả hàng không xuất hoá đơn`, `Yes VAT - Hasaki xuất hoá đơn bán hàng cho NCC`, `Yes VAT – NCC xuất hoá đơn điều chỉnh cho HASAKI`} |
| ADJ status | enum | ✅ | Default = `Waiting for approval` |
| ADJ Required picking | enum | ✅ | `No` |
| ADJ Source code | string | ✅ | Mã PO khi đánh giá |
| ADJ SKU VAT + Price | rule | ✅ | Lấy từ Inside theo rules Adjustment hiện tại |
| Scope Blocked UID Damaged | rule | ✅ | Chỉ áp dụng cho **SKU vải**; Failed → blocked tất UID group cùng PO + cùng LOT + UID status `Damaged` |
| UID `Damaged` impact | rule | ✅ | Không cộng vào stock Available; không picklist được |
| Un-Blocked UID | rule | ✅ | Auto chuyển product status `Damaged → Normal` |
| Tiêu chí 4 điểm auto inherit | rule | ✅ | Khi assign cho SKU, auto load thiết lập tiêu chí 4 điểm, không cần config lại từng SKU |
| Tiêu chí theo từng bước auto inherit | rule | ✅ | Khi assign cho SKU, auto load thiết lập từng bước |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-EVM-001 | Validation | UID group không tồn tại (Step 2) | `Mã UID không tồn tại.` | (raw không có EN — Q-004) | 07105#L1202-L1202 |
| ERR-EVM-002 | Validation | SL cần khai báo không đủ SL trong UID group | `Số lượng trong UID group không đủ số lượng yêu cầu.` | (raw không có EN — Q-004) | 07105#L1203-L1204 |
| MSG-EVM-003 | Validation | Step 1 SKU chưa thiết lập tiêu chí | (raw không có verbatim — Q-003) | (raw không có verbatim — Q-003) | 07105#L1186-L1187 |
| MSG-EVM-004 | Confirm | SKU phụ liệu Failed — tạo ADJ Return to vendor | (raw không có VN — Q-005) | `SKU 422280022 has evaluation criteria marked as FAILED. Do you want to create an adjustment voucher to export the failed quantity for return to vendor?` | 07105#L1250-L1253 |
| ERR-EVM-005 | Validation | ADJ SL trả > SL nhập hàng PO | (raw không có verbatim — Q-006) | (raw không có verbatim — Q-006) | 07105#L1259-L1260 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Step 1 tìm SP theo SKU/barcode/tên + load 10 PO**
  - **Given:** User vào `Purchase Order / Quality Control`, chọn kho A.
  - **When:** Click `Tạo mới` + nhập SKU `SP-A`.
  - **Then:** Hệ thống load 10 PO gần nhất của `SP-A` theo kho A (R004).
- **AC-02 — Step 1 SKU chưa thiết lập tiêu chí**
  - **Given:** SKU `SP-B` không có tiêu chí thiết lập.
  - **When:** User chọn PO + click `Tiếp tục`.
  - **Then:** MSG-EVM-003 hiện, block (R004).
- **AC-03 — Step 2 UID group bắt buộc**
  - **Given:** Form Step 2 mở.
  - **When:** User để trống UID group + click `Bắt đầu đánh giá`.
  - **Then:** Validation block (R005).
- **AC-04 — Step 2 UID không tồn tại**
  - **Given:** User nhập UID `UID-XYZ` không tồn tại.
  - **When:** Click `Bắt đầu đánh giá`.
  - **Then:** ERR-EVM-001 (R006).
- **AC-05 — Step 2 SL không đủ trong UID**
  - **Given:** UID group `UID-001` có SL = 100. User nhập SL cần đánh giá = 150.
  - **When:** Click `Bắt đầu đánh giá`.
  - **Then:** ERR-EVM-002 (R006).
- **AC-06 — Step 3 Fail required chụp hình**
  - **Given:** Tiêu chí A đánh Fail.
  - **When:** User chuyển sang tiêu chí khác.
  - **Then:** Block, yêu cầu chụp hình + ghi chú (R008).
- **AC-07 — Step 3 max 5 hình**
  - **Given:** Tiêu chí Fail.
  - **When:** User chụp 5 hình.
  - **Then:** Block thêm hình (R008).
- **AC-08 — Hoàn thành đánh giá Manual**
  - **Given:** User đánh giá tất cả tiêu chí.
  - **When:** Click `Hoàn thành`.
  - **Then:** Đánh giá lưu (R009).
- **AC-09 — Update 20-04-2026: SKU phụ liệu Failed → ADJ dialog**
  - **Given:** SKU `SP-A` cate phụ liệu (không Thời trang NVL/Vải), kết quả Failed.
  - **When:** Hoàn thành đánh giá.
  - **Then:** Confirm MSG-EVM-004 hiện (R011, R012, R013).
- **AC-10 — `Để sau` đóng dialog quay về danh sách**
  - **Given:** Dialog mở.
  - **When:** User click `Để sau`.
  - **Then:** Dialog đóng, quay về danh sách SKU đánh giá; không tạo ADJ (R013).
- **AC-11 — Tạo ADJ valid SL**
  - **Given:** PO nhập SL = 100. User nhập SL trả = 30.
  - **When:** Click `Xác nhận`.
  - **Then:** ADJ tạo với SL = 30 (R014).
- **AC-12 — Tạo ADJ SL > SL nhập PO**
  - **Given:** PO nhập SL = 100. User nhập SL trả = 150.
  - **When:** Validate.
  - **Then:** ERR-EVM-005 (R014).
- **AC-13 — ADJ Require VAT = No**
  - **Given:** Form ADJ mở.
  - **When:** User chọn Require VAT = `No`.
  - **Then:** ADJ created — Trả hàng không xuất hoá đơn (R015).
- **AC-14 — ADJ Require VAT = Yes VAT Hasaki xuất**
  - **Given:** User chọn Hasaki xuất.
  - **When:** Tạo.
  - **Then:** ADJ với rule Hasaki xuất hoá đơn bán hàng cho NCC (R015).
- **AC-15 — ADJ Require VAT = Yes VAT NCC xuất**
  - **Given:** User chọn NCC xuất.
  - **When:** Tạo.
  - **Then:** ADJ với rule NCC xuất hoá đơn điều chỉnh cho HASAKI (R015).
- **AC-16 — ADJ fields auto-fill**
  - **Given:** Source PO `PO-001` có Vendor `V1`.
  - **When:** Tạo ADJ.
  - **Then:** ADJ có Vendor = `V1`, Source code = `PO-001`, Warehouse = kho đang xử lý, Type = `Export`, Reason = `Return to vendor`, Required picking = `No`, ADJ status = `Waiting for approval` (R015).
- **AC-17 — ADJ SKU info từ Inside**
  - **Given:** SKU `422280022` có VAT 10%, Price 100k trên Inside.
  - **When:** ADJ tạo cho SL = 30.
  - **Then:** SKU info trong ADJ: SL = 30, VAT = 10%, Price = 100k theo rules ADJ hiện tại (R016).
- **AC-18 — S-35 SKU Vải Failed → blocked tất UID group cùng PO + LOT**
  - **Given:** SKU Vải `V1` nhận PO `PO-X` LOT `LOT-A`, đã sinh 5 UID groups: `UG-1` đến `UG-5`. Đánh giá `UG-1` Failed.
  - **When:** Đánh giá Failed.
  - **Then:** Hệ thống auto blocked `UG-1` đến `UG-5` (cùng PO + LOT) (R017).
- **AC-19 — S-35 UID chuyển Damaged**
  - **Given:** Sau AC-18.
  - **When:** Hệ thống xử lý.
  - **Then:** Tất cả UID trong `UG-1`..`UG-5` chuyển product status = `Damaged`; stock Available không cộng (R018).
- **AC-20 — Damaged UID không picklist**
  - **Given:** UID `U1` status `Damaged`.
  - **When:** Order/Receipt/IT try pick.
  - **Then:** UID `U1` bị skip (R018).
- **AC-21 — Un-Blocked UID Damaged → Normal**
  - **Given:** UID group `UG-1` đang blocked, UID `U1` status `Damaged`.
  - **When:** User Un-Blocked `UG-1`.
  - **Then:** `UG-1` → Available; `U1` status → `Normal` (R019).
- **AC-22 — Update 10-05-2026: Tiêu chí 4 điểm setup**
  - **Given:** User vào màn thiết lập tiêu chí.
  - **When:** Chọn phân loại `Lỗi 4 điểm` + click `Tạo`.
  - **Then:** Màn thiết lập 4 điểm mở (R020).
- **AC-23 — Auto inherit 4 điểm khi assign SKU**
  - **Given:** Tiêu chí `T4-1` (4 điểm) đã setup.
  - **When:** User assign `T4-1` cho SKU `SP-X`.
  - **Then:** Hệ thống auto load thiết lập 4 điểm cho `SP-X`, không cần config lại (R021).
- **AC-24 — Update 10-05-2026: Tiêu chí Theo từng bước setup**
  - **Given:** User vào màn thiết lập tiêu chí.
  - **When:** Chọn phân loại `Theo từng bước` + click `Tạo`.
  - **Then:** Màn thiết lập từng bước mở (R022).
- **AC-25 — Auto inherit Theo từng bước khi assign SKU**
  - **Given:** Tiêu chí `TBB-1` (theo bước) đã setup với 3 bước.
  - **When:** User assign `TBB-1` cho SKU `SP-Y`.
  - **Then:** Hệ thống auto load 3 bước cho `SP-Y` (R023).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | Nguồn | Figma mockup links — node `1946-1696` (Update 11-02-2026) và `2542-554` (Update 20-04-2026) cover hết flow Manual + SKU phụ liệu hay chỉ 1 màn? | UX | Open | | | |
| Q-002 | R015, R018 | Adjustment Create API + UID Blocked/Product status API — endpoint cụ thể? Schema? Sync vs async? | Dev | Open | | | |
| Q-003 | R004, MSG-EVM-003 | Verbatim VN+EN cho message khi SKU chưa thiết lập tiêu chí. | PO/UX | Open | | | |
| Q-004 | ERR-EVM-001, ERR-EVM-002 | Verbatim EN cho 2 message validation Step 2 (raw chỉ có VN). | PO/UX | Open | | | |
| Q-005 | R013, MSG-EVM-004 | Verbatim VN cho confirm dialog "Tạo phiếu điều chỉnh" (raw chỉ có EN). | PO/UX | Open | | | |
| Q-006 | R014, ERR-EVM-005 | Verbatim VN+EN cho message khi SL trả > SL nhập PO. | PO/UX | Open | | | |
| Q-007 | R019 | Khi vendor return đã Out UID Damaged, sau đó user Un-Blocked UID group — UID đã Out có chuyển Normal được không? Edge case. | PO/Dev | Open | | | |
| Q-008 | R001, R002 | Flow cũ (bỏ) — vẫn còn data history không? Có cần migrate evaluation đã tạo bằng flow cũ sang flow mới? | PO/Dev | Open | | | |
| Q-009 | R011 | "SKU phụ liệu (SKU thường)" — định nghĩa cụ thể master data flag? Có overlap với SKU vải không (vd phụ liệu vải)? | PO | Open | | | |
| Q-010 | R012 | "Failed = có ≥ 1 kết quả failed" — vậy 1 tiêu chí Fail trong tổng 10 → toàn bộ Failed? Có threshold % cho phép không? | PO | Open | | | |
| Q-011 | R015 | "rules của Adjustment hiện tại" cho VAT/Price — có doc ADJ rules riêng không? | PO/Dev | Open | | | |
| Q-012 | R017 | "Cùng PO và cùng LOT" — định nghĩa "LOT" cụ thể? Khác `số lô` không (vì lô là master data SKU, LOT có thể là batch nhận PO)? | PO/Dev | Open | | | |
| Q-013 | R018 | Product status enum đầy đủ — {`Normal`, `Damaged`, ...?} Có status khác nào (vd `Expired`, `Quarantine`)? | PO/Dev | Open | | | |
| Q-014 | R021, R023 | Auto inherit thiết lập tiêu chí — sau khi inherit, user có thể override per SKU không (vd 1 SKU cần điều chỉnh điều kiện đạt)? | PO | Open | | | |
| Q-015 | R007 | Step 3 thông tin `Số lô` và `HSD` lấy từ đâu (UID group hay SKU master)? Validation gì? | PO/Dev | Open | | | |
| Q-016 | R001-R002 | Phần "(Bỏ)" flow cũ — vẫn giữ trong doc cho reference, hay sẽ remove ở v2.0? | PO | Open | | | |
| Q-017 | L1128-L1147 | App-side behavior trong range source: `Khai báo SL cần đánh giá cho UID group (App)` (bắt buộc, số nguyên dương, sau xác nhận tự động trừ SL đã khai báo khỏi UID group) + `Chụp hình tem QC (App)` (bắt buộc, chỉ 1 hình QC Pass/Fail khi nhấn Hoàn thành). Các behavior này chưa có R-ID. Ownership thuộc manual flow, mobile flow hay feature riêng? | PO | Open | | | |
| Q-018 | L1152-L1168 | L1152-L1168 "Một số lưu ý luồng mới": transfer UID group vào F0-XV tự sinh yêu cầu đánh giá Xã vải; tiêu chí PO sample → PO chính (BOD duyệt 4/5 → PO chính dùng điều kiện PO sample). Nội dung này thuộc spec nào (xã vải / PO sample / manual) và có cần tạo R-ID ở spec manual không? | PO | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-29..S-33 + S-34 + S-35 | 1.5 (stub) | 1.5 | All R + AC | Draft |
| CHG-002 | Deprecate | Flow cũ Tạo mới Manual `(bỏ)` — replace bởi Update 11-02-2026 | 1.5 (cũ) | 1.5 | R001, R002 | Done (đã deprecated trong raw v1.5) |
| CHG-003 | Add | Update 11-02-2026 + 12-02-2026: flow Manual mới với Step 1-3 (Tìm SP → Khai báo UID group → Đánh giá) | 1.5 | 1.5 | R004-R009 | Done (đã trong raw v1.5) |
| CHG-004 | Add | Update 20-04-2026: SKU phụ liệu Failed → Adjustment Return to vendor với 3 option VAT | 1.5 | 1.5 | R011-R016 | Done (đã trong raw v1.5) |
| CHG-005 | Add | S-35: Blocked UID group + Damaged cho SKU vải Failed | 1.5 | 1.5 | R017-R019 | Done (đã trong raw v1.5) |
| CHG-006 | Add | Update 10-05-2026: Thiết lập tiêu chí 4 điểm + Theo từng bước với auto inherit | 1.5 | 1.5 | R020-R023 | Done (đã trong raw v1.5) |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_qc_evaluation_manual | test_stub_qc_evaluation_manual | Add (chờ Gate 1B) | [[stub_qc_criteria_setup]] (tiêu chí 4 điểm + từng bước inherit), [[stub_qc_criteria_sku]] (assign tiêu chí), [[stub_qc_uid_group]] (UID group + SL), [[stub_qc_evaluation_mobile]] (Mobile flow), [[stub_qc_evaluation_result]] (kết quả tổng hợp), Adjustment system (Return to vendor), Inventory (UID Damaged stock impact) | Q-001..Q-016 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R023, AC-01..AC-25 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-016. R001/R002 là deprecated — có thể skip TC |

## 🚧 Blocked Coverage

- R015, R018 — chờ Q-002 (API endpoints)
- R004, MSG-EVM-003 — chờ Q-003 (verbatim message)
- ERR-EVM-001, ERR-EVM-002 — chờ Q-004 (verbatim EN)
- R013, MSG-EVM-004 — chờ Q-005 (verbatim VN)
- R014, ERR-EVM-005 — chờ Q-006 (verbatim SL > PO)
- R019 — chờ Q-007 (Un-Blocked sau vendor return)
- R001, R002 — chờ Q-008, Q-016 (legacy data + remove plan)
- R011 — chờ Q-009 (định nghĩa SKU phụ liệu)
- L1128-L1147 (App-side UID SL auto-deduct + chụp tem QC) — POTENTIAL_OMISSION chưa có R-ID, chờ Q-017 xác nhận ownership
- L1152-L1168 (lưu ý xã vải + tiêu chí PO sample) — MISSING_DETAIL, xem [[stub_receiving_po_fabric]] + [[stub_receiving_po_po_sample]]; chờ Q-018
- R012 — chờ Q-010 (threshold Failed)
- R015 — chờ Q-011 (rules ADJ)
- R017 — chờ Q-012 (định nghĩa LOT)
- R018 — chờ Q-013 (product status enum)
- R021, R023 — chờ Q-014 (override per SKU)
- R007 — chờ Q-015 (Số lô + HSD source)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 21:30:00 | v1.1 | Refine stub → full spec: 23 R-ID (2 deprecated), 25 AC, 22 BR, 5 messages (3 partial verbatim, 2 missing), 16 questions Open. `partial_read: false`. | refine-batch-5-2026-05-30 |
| 2026-05-31 17:00:00 | v1.2 | FIX-005 + FIX-006 (refiner batch-3): thêm Q-017 (POTENTIAL_OMISSION L1128-L1147 App-side UID SL + tem QC) + Q-018 (MISSING_DETAIL L1152-L1168 xã vải/PO sample cross-ref) + Blocked Coverage tương ứng. | refiner-spec-scoped-batch-3 |
