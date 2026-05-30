---
aliases: [stub_receiving_po_vas_manual]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_vas_manual
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L2071-L2181
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 20:30:00"
verification_status: Pending
approved_by:
approved_at:
approval_note:
---

# REQ: stub_receiving_po_vas_manual

## Tổng quan
- **Mã tính năng:** stub_receiving_po_vas_manual
- **Feature:** 01-12-2025 Create/Update VAS Manual — Web update listing/detail + Khai báo VAS RFID + Tạo thủ công
- **Mô tả ngắn:** Update 01-12-2025. Web (`Inbound / VAS`) bổ sung `Type = Manual` để phân biệt với VAS auto-gen. VAS detail cho phép update `Qty received` nếu VAS Manual + status `Open`/`In-Progress` (vì SL hàng vật lý có thể không khớp lúc khai báo RFID/Serial). App (`Purchase order / Confirm paste ID`): SKU có config RFID **không thuộc Cate Thời trang và Brand Synctive** → khi nhận PO scan theo số lượng (giống Serial) + sinh VAS yêu cầu khai báo RFID. Khai báo VAS type RFID: scan từng barcode hoặc máy scan hàng loạt; validate RFID phải chưa tồn tại; cảnh báo nếu SL RFID scan > SL cần. Tạo thủ công VAS: form với Kho (auto từ ngoài, có thể đổi), Loại VAS (RFID/Serial), Mã phiếu nhập nguồn (optional, validate tồn tại), Thêm SP (scan/SKU/tên, check tồn kho UID In-Bin + Picklisted, SL không vượt tồn kho), confirm tạo mới.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Nhân viên kho (App khai báo RFID), Quản lý (Web update Qty + tạo thủ công).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[test_stub_receiving_po_vas_manual]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_receiving_po_vas]] (VAS listing/detail base), [[stub_receiving_po_confirm_paste_id]] (Confirm paste ID flow base). ↔️ liên quan [[stub_receiving_po_fabric]] (UID group / RFID).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07062_Receiving_PO_Docs_ver2.17.md | 2.17 | ✅ Hiện hành |
| 2 | Figma mockup | https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO?node-id=1562-910 | — | Hiện hành (Q-001) |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | API check tồn kho UID có status `In-Bin` + `Picklisted` cho SKU | R013 | 07062#L2153-L2156 | Internal — Q-002 |
| N/A | API validate mã phiếu nhập nguồn tồn tại | R011 | 07062#L2142-L2144 | Internal — Q-002 |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Web update — Ở màn hình danh sách VAS (`Menu: Inbound / VAS`), thông tin `Type` **bổ sung thêm giá trị `Manual`** để phân biệt với những VAS được tạo tự động | UI + Enum | High | ✅ | 07062#L2076-L2079 |
| R002 | Web update — Ở màn hình VAS detail, với những VAS **được tạo manual** và có trạng thái là `Open` hoặc `In-Progress` thì cho user có quyền **update lại số lượng `Qty received`**. Lý do: trong quá trình khai báo RFID/Serial thì SL hàng vật lý có thể không khớp với SL đã khai báo trước đó | Functional + Business rule | High | ✅ | 07062#L2080-L2085 |
| R003 | App — Nhận hàng PO SKU có RFID của vendor ngoài đặt tại `Menu: Purchase order / Confirm paste ID`. Với SKU có config RFID và **KHÔNG thuộc Cate Thời trang và Brand Synctive**: khi nhận PO vẫn scan nhận theo **số lượng giống Serial** và sinh VAS yêu cầu khai báo RFID | Business rule + Functional | High | ✅ | 07062#L2088-L2091 |
| R004 | App — Khai báo VAS với `VAS type = RFID`. Flow: chọn VAS cần khai báo → chọn SKU cần khai báo → user có thể (a) scan **từng barcode RFID** (nếu có) hoặc (b) chọn để **scan RFID hàng loạt** bằng máy scan RFID | Functional | High | ✅ | 07062#L2092-L2103 |
| R005 | Khai báo RFID — Validation: với luồng này thì **tất cả RFID phải chưa tồn tại trên hệ thống** thì được hiểu là hợp lệ. Nếu RFID đã tồn tại trên hệ thống → **không hợp lệ** | Validation + Business rule | High | ✅ | 07062#L2104-L2107 |
| R006 | Khai báo RFID — Lưu ý khi scan bằng máy scan RFID: **phải đảm bảo chỉ có RFID của SP cần khai báo**, không để lẫn hàng khác vào để tránh hệ thống ghi nhận sai | Business rule + UX | High | ⚠️ | 07062#L2108-L2110 |
| R007 | Khai báo RFID — Nếu **SL RFID scan vào lớn hơn SL RFID cần khai báo** → hiện thông báo. User cần xoá RFID dư hoặc scan lại cho đúng SL rồi nhấn `Lưu` | Validation + Functional | High | ✅ | 07062#L2111-L2117 |
| R008 | Khai báo RFID — Nhấn `Lưu` → ghi nhận thông tin RFID cho SKU chọn khai báo. Làm tương tự cho đến khi khai báo đầy đủ SKU có trong VAS. Sau khi khai báo đầy đủ → nhấn `Hoàn thành` để kết thúc VAS. **Nút `Hoàn thành` chỉ hiện** khi tất cả các SKU đã khai báo đủ số lượng | Functional + State transition | High | ✅ | 07062#L2118-L2122 |
| R009 | Tạo thủ công VAS — đặt tại `Menu: Purchase order / Confirm paste ID`. Tại màn hình quản lý các VAS cần khai báo, chọn `Tạo mới` | UI + Navigation | High | ✅ | 07062#L2123-L2125 |
| R010 | Form `Tạo mới VAS` — Field `Kho`: lấy thông tin ở màn hình ngoài đã chọn; **bắt buộc chọn**; user có thể chọn lại theo nhu cầu; load thông tin kho theo **phân quyền user** | Functional + Auth | High | ✅ | 07062#L2126-L2130 |
| R011 | Form `Tạo mới VAS` — Field `Loại VAS`: default không chọn; **bắt buộc chọn**; values: `RFID` (tạo VAS cho SKU có config serial cần khai báo bổ sung), `Serial` (tạo VAS cho SKU có config serial cần khai báo bổ sung) | Enum + Validation | High | ✅ | 07062#L2131-L2137 |
| R012 | Form `Tạo mới VAS` — Field `Mã phiếu nhập nguồn`: thường là mã PO đã nhập hàng cho SKU cần khai báo; **không bắt buộc**. Nếu có nhập thì validate mã có tồn tại trên hệ thống không, nếu không → thông báo `Mã [Code] không tồn tại trên hệ thống.` | Validation | High | ✅ | 07062#L2138-L2144 |
| R013 | Form `Tạo mới VAS` — `Thêm sản phẩm cần khai báo`: hỗ trợ scan barcode, SKU hoặc tìm theo tên sản phẩm (chọn tìm theo tên để mở modal tìm sản phẩm theo tên có sẵn) | Functional + UI | High | ✅ | 07062#L2145-L2152 |
| R014 | Form `Tạo mới VAS` — `Số lượng tồn kho hệ thống`: sau khi scan/chọn SKU hợp lệ, hệ thống check tồn kho các UID có **trạng thái `In-Bin` và `Picklisted`** và hiện lên màn hình để user biết | Business rule + UI | High | ✅ | 07062#L2153-L2156 |
| R015 | Form `Tạo mới VAS` — `Số lượng cần khai báo VAS`: user nhập SL cần khai báo theo SL gợi ý từ hệ thống. **Chỉ cho nhập số ≤ SL tồn kho** của hệ thống; nếu nhập lớn hơn → thông báo `Số lượng cần khai báo (125) không được lớn hơn số lượng tồn kho trên hệ thống (120).` | Validation | High | ✅ | 07062#L2157-L2163 |
| R016 | Form `Tạo mới VAS` — Tuỳ vào loại VAS lựa chọn, SKU được add vào danh sách khai báo **phải được config tương ứng** (RFID config nếu Loại VAS = RFID; Serial config nếu Loại VAS = Serial); nếu không → hiện thông báo (verbatim Q-003) | Validation + Business rule | High | ⚠️ | 07062#L2164-L2165 |
| R017 | Form `Tạo mới VAS` — Có thể chọn để **xoá SKU ra khỏi danh sách** đã add trước đó; hiện thông báo xác nhận (verbatim Q-004) | Functional + Confirm | High | ⚠️ | 07062#L2166-L2168 |
| R018 | Form `Tạo mới VAS` — Sau khi add đủ SKU cần khai báo, chọn `Tạo mới` để tiến hành tạo VAS; hiện thông báo xác nhận (verbatim Q-004) | Functional + Confirm | High | ⚠️ | 07062#L2169-L2171 |
| R019 | Form `Tạo mới VAS` — Chọn `Xác nhận` để tạo VAS và chuyển qua bước khai báo cho VAS vừa tạo | Functional + Navigation | High | ✅ | 07062#L2176-L2176 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User có quyền truy cập `Inbound / VAS` (Web) hoặc `Purchase order / Confirm paste ID` (App).
- SKU có config RFID hoặc Serial.
- (App) PO có SKU thuộc luồng RFID vendor ngoài đã được nhận hàng.

### Luồng chuẩn (Happy Path) — Web update Qty received cho VAS Manual
1. Quản lý vào `Web / Inbound / VAS`.
2. Listing hiển thị VAS với cột `Type = Manual` cho VAS được tạo manual (R001).
3. Click VAS-M (Type Manual, status `Open`) → mở VAS detail.
4. Quản lý sửa `Qty received` của SKU từ 100 → 95 (do hàng vật lý khai báo thiếu) → save (R002).

### Luồng chuẩn (Happy Path) — App nhận PO RFID vendor ngoài + khai báo RFID
1. PO có SKU `SP-X` config RFID, không thuộc Thời trang, không Brand Synctive.
2. User vào `Receiving PO` (App), scan PO, scan `SP-X` theo SL (giống flow Serial).
3. Sau khi hoàn thành nhận PO → hệ thống sinh VAS type `RFID` cho `SP-X` (R003).
4. User vào `Purchase order / Confirm paste ID`, chọn VAS RFID đã sinh.
5. Chọn SKU `SP-X` cần khai báo (R004).
6. User chọn option scan từng barcode RFID hoặc scan hàng loạt bằng máy (R004).
7. Validate: tất cả RFID phải chưa tồn tại trên hệ thống (R005).
8. Nếu SL RFID scan = SL cần → nhấn `Lưu` ghi nhận (R008).
9. Khai báo lần lượt cho tất cả SKU trong VAS.
10. Khi đủ tất cả SKU → button `Hoàn thành` show → user click → VAS kết thúc (R008).

### Luồng chuẩn (Happy Path) — Tạo thủ công VAS
1. User vào `App / Purchase order / Confirm paste ID` → tại quản lý VAS chọn `Tạo mới` (R009).
2. Form mở:
   - `Kho`: prefill từ kho ngoài, user có thể đổi (R010).
   - `Loại VAS`: chọn `RFID` hoặc `Serial` (R011).
   - `Mã phiếu nhập nguồn`: nhập mã PO (optional); nếu nhập → validate tồn tại (R012).
3. `Thêm sản phẩm cần khai báo`: scan/SKU/tên SP (R013).
4. Sau scan SKU `SP-A`, hệ thống check tồn kho UID In-Bin + Picklisted = 120 → hiển thị (R014).
5. User nhập `Số lượng cần khai báo VAS = 50` (≤ 120) → valid (R015).
6. Lặp lại với SP khác.
7. User click `Tạo mới` → confirm dialog → `Xác nhận` → VAS được tạo + chuyển flow khai báo (R018, R019).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — Web update Qty received VAS auto-gen:** không được phép (chỉ áp dụng VAS Manual) (R002).
- **A2 — Web update Qty với VAS Manual status Completed/Canceled:** không cho update (R002).
- **A3 — Khai báo RFID 1 SKU 1 lần:** sau scan đủ SL của SKU đó → next SKU.
- **A4 — Tạo thủ công không nhập Mã phiếu nhập nguồn:** OK, optional (R012).
- **A5 — Tạo thủ công SKU có config khác Loại VAS:** vd Loại = RFID nhưng SKU không có config RFID → block (R016).

### Luồng ngoại lệ (Exception Paths)
- **E1 — RFID đã tồn tại trên hệ thống:** không hợp lệ (R005).
- **E2 — SL RFID scan > SL cần khai báo:** thông báo block; phải xoá hoặc scan lại (R007).
- **E3 — Mã phiếu nhập nguồn không tồn tại:** ERR-VSM-001 (R012).
- **E4 — SL cần khai báo > tồn kho:** ERR-VSM-002 (R015).
- **E5 — Hoàn thành khi chưa đủ tất cả SKU:** nút `Hoàn thành` không show (R008).
- **E6 — Lẫn RFID hàng khác khi scan hàng loạt:** hệ thống ghi nhận sai (R006); chú ý người dùng cần kiểm tra trước scan.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Type `Manual` listing VAS | enum | ✅ | Bổ sung enum value `Manual` cho cột Type trong listing (Inbound/VAS) |
| Qty received editable | rule | ✅ | Chỉ áp dụng cho VAS Type = `Manual` + status ∈ {`Open`, `In-Progress`} |
| Trigger flow RFID vendor ngoài | rule | ✅ | SKU config RFID + KHÔNG thuộc Cate Thời trang + KHÔNG Brand Synctive |
| Scan RFID — 2 option | enum | ✅ | (1) Từng barcode; (2) Hàng loạt bằng máy scan RFID |
| RFID validity | rule | ✅ | Tất cả RFID scan vào phải chưa tồn tại trên hệ thống; đã tồn tại = không hợp lệ |
| SL RFID limit | rule | ✅ | SL RFID scan ≤ SL cần khai báo; vượt → block, user xoá dư hoặc scan lại |
| Hoàn thành VAS RFID | rule | ✅ | Button `Hoàn thành` chỉ show khi tất cả SKU đã khai báo đủ SL |
| Tạo thủ công Kho | rule | ✅ | Bắt buộc; default = kho ngoài; load theo phân quyền user |
| Tạo thủ công Loại VAS | enum | ✅ | Bắt buộc; values {`RFID`, `Serial`} |
| Mã phiếu nhập nguồn | string | ❌ | Optional; nếu nhập phải validate tồn tại trên hệ thống |
| Tồn kho check | rule | ✅ | Check UID có status `In-Bin` + `Picklisted` |
| SL cần khai báo VAS | integer | ✅ | ≤ SL tồn kho hệ thống |
| SKU config consistency | rule | ✅ | Loại VAS = RFID → SKU phải có config RFID; Loại = Serial → SKU phải có config Serial |
| Confirm dialog xoá SKU | rule | ✅ | Cần confirm trước khi xoá khỏi danh sách |
| Confirm dialog tạo VAS | rule | ✅ | Cần confirm trước khi tạo VAS |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-VSM-001 | Validation | Mã phiếu nhập nguồn không tồn tại trên hệ thống | `Mã [Code] không tồn tại trên hệ thống.` | (raw không có EN — Q-005) | 07062#L2142-L2144 |
| ERR-VSM-002 | Validation | SL cần khai báo > SL tồn kho hệ thống | `Số lượng cần khai báo (125) không được lớn hơn số lượng tồn kho trên hệ thống (120).` | (raw không có EN — Q-005) | 07062#L2159-L2163 |
| MSG-VSM-003 | Warning | SL RFID scan vào > SL cần khai báo (R007) | (raw chỉ nói "hiện thông báo" — Q-006) | (raw không có EN — Q-006) | 07062#L2111-L2117 |
| MSG-VSM-004 | Validation | SKU không config tương ứng Loại VAS (R016) | (raw không có verbatim — Q-003) | (raw không có verbatim — Q-003) | 07062#L2164-L2165 |
| MSG-VSM-005 | Confirm | Xoá SKU khỏi danh sách (R017) | (raw không có verbatim — Q-004) | (raw không có verbatim — Q-004) | 07062#L2166-L2168 |
| MSG-VSM-006 | Confirm | Tạo mới VAS (R018) | (raw không có verbatim — Q-004) | (raw không có verbatim — Q-004) | 07062#L2169-L2171 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Listing VAS có Type Manual**
  - **Given:** Đã có VAS được tạo manual.
  - **When:** User mở `Inbound / VAS`.
  - **Then:** Cột `Type` hiển thị `Manual` cho VAS đó (R001).
- **AC-02 — Update Qty received cho VAS Manual Open**
  - **Given:** VAS-M Type Manual status `Open`, SKU-A `Qty received = 100`.
  - **When:** User mở VAS-M detail, sửa Qty thành 95 → save.
  - **Then:** Qty received của SKU-A cập nhật = 95 (R002).
- **AC-03 — Update Qty received cho VAS Manual In-Progress**
  - **Given:** VAS-M Type Manual status `In-Progress`, SKU-B `Qty received = 50`.
  - **When:** User sửa Qty thành 48.
  - **Then:** Lưu thành công (R002).
- **AC-04 — Không cho update Qty cho VAS auto-gen**
  - **Given:** VAS-Auto Type ≠ `Manual` status `Open`.
  - **When:** User cố mở VAS-Auto detail và sửa Qty.
  - **Then:** Field disable, không cho sửa (R002).
- **AC-05 — Không cho update Qty cho VAS Manual Completed**
  - **Given:** VAS-M Type Manual status `Completed`.
  - **When:** User cố sửa Qty.
  - **Then:** Field disable (R002).
- **AC-06 — Sinh VAS RFID khi nhận PO SKU RFID vendor ngoài**
  - **Given:** PO có SKU `SP-X` config RFID, không Thời trang, không Synctive.
  - **When:** User scan nhận SP-X theo SL.
  - **Then:** Hệ thống sinh VAS type `RFID` cho SP-X (R003).
- **AC-07 — Scan RFID từng barcode**
  - **Given:** VAS RFID mở, chọn SP-X cần khai báo SL = 10.
  - **When:** User scan 10 RFID barcode lần lượt.
  - **Then:** 10 RFID add vào danh sách; SL đủ; có thể `Lưu` (R004, R008).
- **AC-08 — Scan RFID hàng loạt bằng máy**
  - **Given:** VAS RFID, chọn SP-X SL = 10. Máy scan RFID có sẵn.
  - **When:** User chọn option scan hàng loạt → máy đọc 10 RFID.
  - **Then:** 10 RFID đọc xong, add vào danh sách (R004).
- **AC-09 — RFID đã tồn tại = không hợp lệ**
  - **Given:** RFID `RFID-001` đã tồn tại trên hệ thống.
  - **When:** User scan `RFID-001`.
  - **Then:** Hệ thống đánh dấu không hợp lệ, không add vào danh sách (R005).
- **AC-10 — SL RFID scan > SL cần khai báo**
  - **Given:** SP-X cần khai báo SL = 10.
  - **When:** Máy scan hàng loạt đọc 12 RFID.
  - **Then:** Thông báo MSG-VSM-003 hiện; user phải xoá 2 RFID dư hoặc scan lại (R007).
- **AC-11 — Hoàn thành VAS chỉ khi đủ tất cả SKU**
  - **Given:** VAS có 3 SKU, mới khai báo đủ 2 SKU.
  - **When:** User xem.
  - **Then:** Button `Hoàn thành` không show. Khi SKU 3 khai báo đủ → button show (R008).
- **AC-12 — Tạo mới VAS — Kho default từ ngoài**
  - **Given:** User đang ở kho A trong list VAS.
  - **When:** User click `Tạo mới`.
  - **Then:** Field Kho prefill = `kho A`; user có thể đổi (R010).
- **AC-13 — Tạo mới VAS — Kho phải có quyền**
  - **Given:** User chỉ có quyền kho A và B.
  - **When:** User click Kho dropdown.
  - **Then:** Dropdown chỉ hiển thị {`kho A`, `kho B`} (R010).
- **AC-14 — Loại VAS bắt buộc chọn**
  - **Given:** Form `Tạo mới VAS` mở. User để Loại VAS trống.
  - **When:** User click `Tạo mới`.
  - **Then:** Block, validation Loại VAS bắt buộc (R011).
- **AC-15 — Mã phiếu nhập nguồn optional**
  - **Given:** Form mở.
  - **When:** User để trống Mã phiếu nhập nguồn → click `Tạo mới`.
  - **Then:** Pass validation (R012).
- **AC-16 — Mã phiếu nhập nguồn không tồn tại**
  - **Given:** User nhập Mã phiếu nhập nguồn = `PO-XYZ` (không tồn tại).
  - **When:** Validate.
  - **Then:** ERR-VSM-001 hiện (R012).
- **AC-17 — Thêm SP scan barcode**
  - **Given:** Form mở.
  - **When:** User scan barcode `BC-001` của SP-A.
  - **Then:** SP-A add vào danh sách + check tồn kho (R013, R014).
- **AC-18 — Tồn kho check In-Bin + Picklisted**
  - **Given:** SKU SP-A có 80 UID In-Bin + 40 UID Picklisted + 30 UID Received.
  - **When:** User add SP-A vào danh sách.
  - **Then:** Hiển thị `Số lượng tồn kho hệ thống = 120` (80 + 40); không tính 30 UID Received (R014).
- **AC-19 — SL cần khai báo vượt tồn kho**
  - **Given:** Tồn kho SP-A = 120.
  - **When:** User nhập `Số lượng cần khai báo = 125`.
  - **Then:** ERR-VSM-002 với verbatim `(125) không được lớn hơn... (120)` (R015).
- **AC-20 — Loại VAS = RFID nhưng SKU không config RFID**
  - **Given:** Loại VAS = RFID. SP-B không có config RFID.
  - **When:** User cố add SP-B vào danh sách.
  - **Then:** MSG-VSM-004 hiện, block add (R016).
- **AC-21 — Xoá SKU khỏi danh sách**
  - **Given:** Danh sách có SP-A, SP-B.
  - **When:** User click icon xoá SP-A.
  - **Then:** Confirm MSG-VSM-005 hiện; sau xác nhận → SP-A bị xoá (R017).
- **AC-22 — Tạo VAS thành công**
  - **Given:** Form đầy đủ thông tin: Kho A, Loại RFID, 3 SKU đã add.
  - **When:** User click `Tạo mới` → confirm MSG-VSM-006 → `Xác nhận`.
  - **Then:** VAS được tạo + chuyển sang flow khai báo cho VAS vừa tạo (R018, R019).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | Nguồn | Figma mockup link `1562-910` — có version control giữa raw doc v2.17 và Figma? Mockup này cover toàn bộ flow Create/Update VAS Manual hay chỉ 1 màn? | UX | Open | | | |
| Q-002 | API | API endpoints — check tồn kho In-Bin + Picklisted + validate mã phiếu nhập nguồn — có spec rõ không? | Dev | Open | | | |
| Q-003 | R016, MSG-VSM-004 | Verbatim VN+EN cho message khi SKU không config tương ứng Loại VAS (RFID vs Serial). | PO/UX | Open | | | |
| Q-004 | R017, R018, MSG-VSM-005, MSG-VSM-006 | Verbatim VN+EN cho 2 confirm dialog (xoá SKU + tạo mới VAS). | PO/UX | Open | | | |
| Q-005 | ERR-VSM-001, ERR-VSM-002 | Raw chỉ có verbatim VN cho 2 message — verbatim EN là gì? | PO/UX | Open | | | |
| Q-006 | R007, MSG-VSM-003 | Verbatim VN+EN cho message khi SL RFID scan > SL cần khai báo. | PO/UX | Open | | | |
| Q-007 | R003 | "Cate Thời trang" và "Brand Synctive" — định nghĩa cụ thể (master data flag, category code chính xác)? Có Brand khác bị exclude tương lai không? | PO | Open | | | |
| Q-008 | R005 | RFID đã tồn tại trên hệ thống = không hợp lệ — trong luồng RFID vendor ngoài. Vậy luồng nội bộ (vd Long An chuyển về Shop từ flow `confirm_paste_id`) thì rule ngược lại (đã tồn tại = hợp lệ)? Phân biệt 2 flow thế nào? | PO/Dev | Open | | | |
| Q-009 | R011 | Loại VAS — chỉ có `RFID` và `Serial`? Có values khác (vd `Imei`, `Label`) không? | PO | Open | | | |
| Q-010 | R014 | Tồn kho check chỉ tính `In-Bin` + `Picklisted` — vì sao bỏ qua `Received`? Lý do business? | PO | Open | | | |
| Q-011 | R002 | "Quá trình khai báo RFID hoặc Serial thì SL hàng vật lý có thể không khớp với SL đã khai báo trước đó" — `Qty received` update lại có audit log không? Trị tối thiểu (vd > 0)? | PO/Dev | Open | | | |
| Q-012 | R006 | Khi scan hàng loạt mà lẫn RFID hàng khác — hệ thống có cách detect không (vd check master data RFID có thuộc PO không)? Hay chỉ là warning UX? | PO/Dev | Open | | | |
| Q-013 | R010 | Loại VAS RFID hay Serial — sau khi tạo VAS có thể đổi không? Hay là immutable? | PO | Open | | | |
| Q-014 | R013 | Modal tìm SP "theo tên có sẵn" — `có sẵn` là gì (auto-complete suggest, hay strict equal)? | UX | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-44..S-47 (Update 01-12-2025) | 2.17 (stub) | 2.17 | All R + AC | Draft |
| CHG-002 | Add | Update 01-12-2025: bổ sung `Type = Manual` cho listing VAS + cho phép update `Qty received` với VAS Manual Open/In-Progress | (trước 2.17) | 2.17 | R001, R002, AC-01..AC-05 | Done (đã trong raw v2.17) |
| CHG-003 | Add | Update 01-12-2025: SKU RFID vendor ngoài + Khai báo VAS RFID | (trước 2.17) | 2.17 | R003-R008, AC-06..AC-11 | Done (đã trong raw v2.17) |
| CHG-004 | Add | Update 01-12-2025: Tạo thủ công VAS với form đầy đủ (Kho/Loại/Mã PO/SP) + validation tồn kho In-Bin + Picklisted | (trước 2.17) | 2.17 | R009-R019, AC-12..AC-22 | Done (đã trong raw v2.17) |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_vas_manual | test_stub_receiving_po_vas_manual | Add (chờ Gate 1B) | [[stub_receiving_po_vas]] (listing/detail VAS), [[stub_receiving_po_confirm_paste_id]] (flow khai báo VAS), [[stub_receiving_po_fabric]] (UID group + RFID mapping) | Q-001..Q-014 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R019, AC-01..AC-22 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-014 |

## 🚧 Blocked Coverage

- Nguồn — chờ Q-001 (Figma mockup version)
- API — chờ Q-002 (API endpoints)
- R016, MSG-VSM-004 — chờ Q-003 (verbatim SKU mismatch Loại VAS)
- R017, R018, MSG-VSM-005, MSG-VSM-006 — chờ Q-004 (verbatim 2 confirm)
- ERR-VSM-001, ERR-VSM-002 — chờ Q-005 (verbatim EN)
- R007, MSG-VSM-003 — chờ Q-006 (verbatim SL dư)
- R003 — chờ Q-007 (định nghĩa Thời trang + Synctive)
- R005 — chờ Q-008 (phân biệt 2 flow RFID)
- R011 — chờ Q-009 (enum Loại VAS đầy đủ)
- R014 — chờ Q-010 (lý do skip Received)
- R002 — chờ Q-011 (audit log + tối thiểu)
- R006 — chờ Q-012 (detect RFID lẫn)
- R010 — chờ Q-013 (Loại VAS immutable)
- R013 — chờ Q-014 (modal tìm tên)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 20:30:00 | v1.1 | Refine stub → full spec: 19 R-ID, 22 AC, 15 BR, 6 messages (2 verbatim VN, 4 missing — Q-003/004/005/006), 14 questions Open. `partial_read: false`. | refine-batch-4-2026-05-30 |
