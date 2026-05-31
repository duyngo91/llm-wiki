---
aliases: [stub_receiving_po_confirm_paste_id]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_confirm_paste_id
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L1808-L2070
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-31 19:34:33"
verification_status: Verified
approved_by:
approved_at:
approval_note:
last_verified_source_version: 2.17

---

# REQ: stub_receiving_po_confirm_paste_id

## Tổng quan
- **Mã tính năng:** stub_receiving_po_confirm_paste_id
- **Feature:** Confirm paste ID (App) — Flow 5 step xác nhận dán ID Serial/Imei/Label/QRCode/RFID cho VAS
- **Mô tả ngắn:** App / Purchase order / Confirm paste ID. Flow 5 step: (1) Scan PO validate (chưa nhận / không tồn tại / khác kho / VAS đã Completed); (2) Chọn phiên dán (VAS) — danh sách ASN status Received chưa xác nhận dán; phân biệt màu Xám/Xanh dương/Cam theo trạng thái + đánh giá; mutex 1 VAS / 1 user; (3) Chụp hình/video (max 5 hình + 1 video 15s, áp dụng theo category — không gồm Sức khoẻ - Làm đẹp/Thuốc); (4) Cập nhật Serial/Imei/Label/QRCode theo BE config; phân biệt màu Xám/Xanh dương/Xanh lá; (5) Hoàn thành — VAS chuyển In-Progress (chưa đủ) hoặc Completed (đủ). Bao gồm Scan RFID 2 option (cho nhiều SKU vs từng SKU) với 2 case (RFID đã define vs từ vendor ngoài). Update 24-12-2024: rules hiển thị phiên dán + cho phép nhiều người 1 VAS + crash recovery. Update 09-07-2025: cảnh báo VAS chưa đánh giá QC. Update 23-04-2025: scope chụp hình theo Serial/Imei. Update 22-05-2025: SKU required Imei auto bật nhưng không bắt buộc.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Nhân viên kho (Confirm Paste ID trên App).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[ts_receiving_po_confirm_paste_id]]
- **API Spec liên quan:** N/A — raw không mô tả API explicit, mention "khi cập nhật 1 thông tin hệ thống sẽ gọi API để validation" (R013).
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_receiving_po_app]] (Receiving PO flow), [[stub_receiving_po_vas]] (VAS sinh ra từ ASN), [[stub_qc_evaluation_result]] (Đánh giá chất lượng required). ↔️ liên quan [[stub_receiving_po_vas_manual]] (Create/Update VAS manual).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07062_Receiving_PO_Docs_ver2.17.md | 2.17 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | API validation realtime khi nhiều người dán cùng 1 VAS (mô tả khái niệm) | R013 | 07062#L1877-L1880 | TBD — Q-001 |
| N/A | BE config flag `wms_product.wms_config & 131072 > 0` → required QR; `config & 8 > 0` → required Imei | R016 | 07062#L1952-L1956 | Internal — Q-002 |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Confirm paste ID (App) đặt tại `App / Purchase order / Confirm paste ID`. User login App + chọn tính năng | UI + Navigation + Auth | High | ✅ | 07062#L1809-L1810 |
| R002 | Step 1 — Scan mã PO cần xác nhận dán ID. Validation: nếu **PO chưa nhận hàng** (status chưa `Receiving`/`Received`) → thông báo `PO [PO code] chưa được nhận hàng.` / `PO [PO code] has not received yet.` | Validation | High | ✅ | 07062#L1813-L1816 |
| R003 | Step 1 — Validation: nếu **PO không tồn tại** trên hệ thống → thông báo `PO [PO code] không tồn tại trên hệ thống.` / `PO [PO code] does not exist in the system.` | Validation | High | ✅ | 07062#L1817-L1819 |
| R004 | Step 1 — Validation: nếu **PO không thuộc kho** đang xử lý → thông báo `PO [PO code] không thuộc kho đang xử lý.` / `PO [PO code] is not in the warehouse being processed.` | Validation | High | ✅ | 07062#L1820-L1823 |
| R005 | Step 1 — Validation: nếu **PO đã hoàn thành dán ID** (VAS Completed) → thông báo `PO [PO code] đã hoàn thành việc dán ID cho sản phẩm.` / `PO [PO code] has completed pasting ID for the products.` | Validation | High | ✅ | 07062#L1824-L1830 |
| R006 | Step 2 — Khi PO hợp lệ, show **danh sách các phiên nhận hàng (ASN)** có status `Received` nhưng chưa xác nhận dán ID tương ứng PO. Thông tin gồm: `Mã VAS`, `Trạng thái VAS`, `Loại VAS`, `Đánh giá chất lượng`, `Người dán` (nếu phiên có nhiều người dán thì hiện người đầu tiên), `Phiên nhận (ASN)`, `Người nhận theo phiên ASN`, `Ngày nhận` (lấy theo ngày received), `Tổng SKU` (đã nhận trong ASN), `Tổng sản phẩm` (đã nhận trong ASN), `Vị trí` (lưu trữ của ASN), `Tìm SKU/barcode/tên sản phẩm`, `Ghi chú PO` | UI + Filter + Functional | High | ✅ | 07062#L1836-L1852 |
| R007 | Step 2 — **Phân biệt màu phiên VAS:** `Xám` = Mới, chưa đánh giá và có thể xác nhận dán; `Xanh dương` = đang thực hiện xác nhận dán ID; `Cam` = Mới, chưa đánh giá và **chưa thể xác nhận dán** do chưa đánh giá chất lượng | UI + Enum + State | High | ✅ | 07062#L1853-L1858 |
| R008 | Step 2 — User chọn phiên cần dán. Rule: **chỉ cho chọn 1 VAS / 1 lần dán**. Khi chọn → update status VAS = `Đang xử lý` (`In-Progress`) | Functional + State transition | High | ✅ | 07062#L1859-L1864 |
| R009 | Update 24-12-2024 — Rules hiển thị phiên VAS: nếu VAS chuyển sang `Đang xử lý` (In-Progress) → màu Xanh dương | UI + State | High | ✅ | 07062#L1866-L1868 |
| R010 | Update 24-12-2024 — Mutex user: nếu VAS `Đang xử lý` của 1 user khác → user chỉ thấy và **không được chọn để dán** (disable không cho chọn); chỉ được chọn phiên có trạng thái `Mới (Open)` hoặc `Đang xử lý` mà của user đó đang làm trước đó | Business rule + Mutex | High | ✅ | 07062#L1872-L1876 |
| R011 | Update 24-12-2024 — Cho phép **1 VAS có nhiều người thực hiện cùng lúc**. Khi cập nhật 1 thông tin, hệ thống gọi API validation realtime → đảm bảo data không bị trùng | Business rule + Concurrency | High | ✅ | 07062#L1877-L1880 |
| R012 | Update 24-12-2024 — Crash recovery: nếu user đang dán **chưa lưu thông tin** và **chưa xác nhận Hoàn thành 1 phần** mà bị crash app hoặc thoát app → khi vào scan lại mã PO thì **vào lại màn hình dán của phiên đã chọn trước đó**, không cần chọn lại phiên | Resilience + Functional | High | ✅ | 07062#L1881-L1886 |
| R013 | Update 09-07-2025 — Nếu VAS có **yêu cầu đánh giá chất lượng sản phẩm nhưng chưa được đánh giá** mà chọn vào xác nhận dán → hiện thông báo (raw chỉ nói "hiện thông báo" — verbatim Q-003) | Validation + Business rule | High | ⚠️ | 07062#L1887-L1891 |
| R014 | Step 3 — Chụp hình/quay video cho sản phẩm. **Áp dụng cho các Category, không bao gồm:** `Sức khoẻ - Làm đẹp` (quản lý/không quản lý date, quản lý Imei); `Thuốc`, `Thuốc (GPP)`. **Có thể bổ sung thêm category sau — sẽ update sau** | Business rule + Scope | High | ⚠️ | 07062#L1895-L1900 |
| R015 | Update 23-04-2025 — Bước chụp hình áp dụng cho **các sản phẩm required Serial/Imei và không thuộc category `Sức khoẻ - Làm đẹp`** | Business rule + Scope | High | ✅ | 07062#L1901-L1904 |
| R016 | Step 3 — Khi user chọn phiên cần dán, hiện thông tin: `Tổng SKU cần dán` (tổng SKU đã dán/SKU cần dán), `Tổng item cần dán` (tổng item đã dán/item cần dán), `Vị trí lưu trữ của ASN tương ứng`. Danh sách SP: `Tên sản phẩm`, `SKU`, `Barcode`, `Số lượng đã cập nhật/Số lượng cần dán` | UI + Functional | High | ✅ | 07062#L1905-L1916 |
| R017 | Step 3 — User chọn SP cần cập nhật → show thông tin gồm: `Tên sản phẩm`, `SKU Barcode`, `Số lượng cần chụp hình` | UI | High | ✅ | 07062#L1917-L1922 |
| R018 | Step 3 — User chọn `+` để chụp hình/quay video. Giới hạn: **max 5 hình; chỉ 1 video; video giới hạn 15 giây** (đảm bảo dung lượng up lên hệ thống). User có thể chụp hình hoặc quay video hoặc **cả 2** | Validation + Media + UI | High | ✅ | 07062#L1925-L1931 |
| R019 | Step 3 — Nhấn `Lưu` để qua bước tiếp theo. **Lưu ý:** SP **không có quản lý Imei** thì sau khi chụp hình/quay video → nhấn `Lưu` xem như **hoàn thành VAS cho SKU đó**. UID chuyển `Received → In-Bin`; SKU mới có thể sử dụng cho đơn hàng hoặc IT | Business rule + State transition | High | ✅ | 07062#L1932-L1938 |
| R020 | Step 4 — Cập nhật thông tin Serial/Imei/Label code. Thông tin SP cần dán: `Tên sản phẩm`, `SKU Barcode`, `Số lượng đã cập nhật/Số lượng cần cập nhật`, **Tuỳ chọn thông tin cần cập nhật** — hệ thống auto chọn theo category | Functional + UI | High | ✅ | 07062#L1940-L1947 |
| R021 | Step 4 — Auto chọn thông tin theo category: nếu cate `CCDC`, `CCDC PB`... (cates VAS): `wms_product.wms_config & 131072 > 0` → bật QRCode required; `wms_product.config & 8 > 0` → bật Imei required | Business rule + BE config | High | ⚠️ | 07062#L1948-L1956 |
| R022 | Update 25-02-2025 — **Tắt option Serial dưới BE**, user chỉ cần cập nhật QRCode. Sau này cần sẽ mở ra sau. Serial nếu không có thông tin → hệ thống WMS tự gen mã `[1023][YYMMDD][6 số tăng dần]`. Nếu kiểm kê count theo Serial → update Serial mới đè lên Serial gen | Functional + Auto-gen | High | ✅ | 07062#L1959-L1977 |
| R023 | Update 22-05-2025 — Nếu SKU có config required Imei → **auto bật option Imei**, nhưng **không bắt buộc nhập**. Nếu nhập → lưu vào; không nhập → để trống | Business rule | High | ✅ | 07062#L1978-L1982 |
| R024 | Step 4 — Ngược lại 2 case ON QRCode/Imei → chỉ cần **chụp hình**, bỏ qua bước cập nhật QRCode/Serial | Functional | High | ✅ | 07062#L1983-L1984 |
| R025 | Step 4 — Lưu ý QRCode in dạng Object → khi scan hệ thống **tự cắt chuỗi** để lấy thông tin field `Code` | Business rule + Parser | High | ✅ | 07062#L1985-L1988 |
| R026 | Step 4 — Logic scan form: thông tin tích chọn → ô scan show lên để user scan. Nếu chỉ 1 thông tin → scan tự add (nhập tay nhấn `+`). Nếu 2 thông tin (QRCode + Serial) → scan QRCode hợp lệ → **auto chuyển focus** qua ô scan Serial/Imei | Functional + UX | High | ✅ | 07062#L1992-L2000 |
| R027 | Step 4 — Sau cập nhật user có thể chỉnh sửa: chọn icon → modify thông tin và lưu lại; validation giống lúc scan mới. Nhấn `Lưu`: nếu **chưa đủ số dòng thông tin** → hiện thông báo xác nhận với option `Đóng` (tắt thông báo) hoặc `Xác nhận` (lưu thông tin đã cập nhật) (verbatim Q-004) | Functional + UI | High | ⚠️ | 07062#L1957-L2009 |
| R028 | Step 4 — Update SL đã cập nhật thông tin tương ứng ở danh sách bên ngoài. **Phân biệt màu:** Xám = chưa cập nhật; Xanh dương = cập nhật 1 phần; Xanh lá = đã cập nhật đủ SL yêu cầu | UI + Enum | High | ✅ | 07062#L2010-L2015 |
| R029 | Step 4.1 — Scan RFID cho SP. 2 option: (1) **Scan RFID cho nhiều SKU cùng lúc** — xác nhận dán nhanh cho nhiều SP trong VAS; (2) **Scan RFID cho từng SKU** — xác nhận dán từng ID. Lưu ý: SKU required RFID **không cần qua bước chụp hình SP khi VAS** | Functional + Business rule | High | ✅ | 07062#L2017-L2020 |
| R030 | Step 4.1 — Hệ thống đọc RFID từ đầu đọc và trả thông tin lên màn hình App. **Case 1 — RFID đã define trên hệ thống** (hàng từ nhà máy Long An chuyển về Shop, cùng hệ thống Hasaki): có thể scan cả 2 option (cho nhiều SKU hoặc từng SKU). Có Tab `Hợp lệ` + Tab `không hợp lệ`. Xem chi tiết RFID từng SKU hợp lệ | Business rule + Functional | High | ✅ | 07062#L2021-L2035 |
| R031 | Step 4.1 — **Case 2 — RFID từ vendor bên ngoài** (chưa có sẵn trên hệ thống, mới dán lên SP): **chỉ cho scan khai báo RFID cho từng SKU**, không cho scan nhiều SKU cùng lúc. Tab `không hợp lệ` không có data; tab `Hợp lệ` load RFID đã scan | Business rule + Functional | High | ✅ | 07062#L2039-L2044 |
| R032 | Step 4.1 — Sau scan RFID xong → nhấn `Xác nhận` để submit thông tin cho từng SP | Functional | High | ✅ | 07062#L2045-L2046 |
| R033 | Step 5 — Xác nhận `Hoàn thành`. **Case A:** chưa cập nhật đủ SL yêu cầu → hiện thông báo xác nhận với option `No` (tắt) hoặc `Yes` (xác nhận hoàn thành). Khi Yes: VAS **giữ status `In-Progress`**, đồng thời update QRCode/Serial/Imei cho các UID tương ứng | Functional + State transition | High | ✅ | 07062#L2051-L2057 |
| R034 | Step 5 — **Case B:** đã cập nhật đủ SL yêu cầu → hiện thông báo xác nhận với `No`/`Yes`. Khi Yes: VAS **update status `Completed`**, đồng thời update QRCode/Serial/Imei cho UID tương ứng | Functional + State transition | High | ✅ | 07062#L2058-L2065 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User login App WMS với tài khoản hợp lệ.
- PO đã được nhận hàng (status `Receiving` hoặc `Received`) với VAS sinh ra (xem [[stub_receiving_po_vas]]).
- ASN status `Received` đã có UID chưa dán ID.

### Luồng chuẩn (Happy Path) — Confirm Paste ID full 5 steps (SP CCDC bật QRCode)
1. User vào `App / Purchase order / Confirm paste ID` (R001).
2. **Step 1:** Scan mã PO `PO-001`. Validate pass (R002-R005).
3. **Step 2:** Danh sách phiên VAS hiển thị, phiên VAS-A màu Xám (R006, R007).
4. User chọn VAS-A → status VAS-A chuyển `In-Progress`, màu Xanh dương (R008, R009).
5. **Step 3:** Hiển thị `Tổng SKU cần dán` + `Tổng item cần dán` + Danh sách SP (R016).
6. User chọn SP `SKU-001` → form mở (R017).
7. User chụp 3 hình + 1 video 10s (R018).
8. Nhấn `Lưu` → nếu SP không có Imei → hoàn thành VAS cho SKU-001, UID chuyển `Received → In-Bin` (R019). Nếu có Imei → tiếp Step 4.
9. **Step 4:** Form cập nhật QRCode mở (auto chọn QRCode vì CCDC + `wms_config & 131072 > 0`) (R020, R021).
10. Serial bị tắt dưới BE; nếu cần sẽ tự gen (R022).
11. User scan QRCode → tự cắt chuỗi lấy field `Code` (R025).
12. Validation pass → add vào danh sách. Cả 2 thông tin ON → auto focus Serial/Imei (R026).
13. SL đã cập nhật của SP-001 = 5/5 → màu Xanh lá (R028).
14. **Step 5:** User click `Hoàn thành` (R033, R034):
    - Đủ SL → confirm dialog → Yes → VAS `Completed`, update QRCode/Serial/Imei cho UID (R034).
    - Chưa đủ → confirm dialog → Yes → VAS giữ `In-Progress` (R033).

### Luồng chuẩn (Happy Path) — Scan RFID Case 1 (nội bộ Hasaki)
1. Bước 4.1 Scan RFID kích hoạt cho SKU required RFID (R029).
2. SP từ nhà máy Long An chuyển về Shop → RFID đã define trên hệ thống (R030 case 1).
3. User chọn option 1 (Scan RFID cho nhiều SKU cùng lúc) hoặc option 2 (từng SKU).
4. Hệ thống đọc RFID → trả tab `Hợp lệ` (xem chi tiết) + tab `không hợp lệ` (R030).
5. User nhấn `Xác nhận` → submit thông tin (R032).

### Luồng chuẩn (Happy Path) — Scan RFID Case 2 (vendor ngoài)
1. SP từ vendor ngoài, RFID mới dán → chưa có trên hệ thống (R031).
2. **Chỉ cho** option 2 (Scan RFID cho từng SKU); không cho nhiều SKU cùng lúc (R031).
3. Tab `không hợp lệ` rỗng; tab `Hợp lệ` load RFID đã scan.
4. User nhấn `Xác nhận` → submit từng SP (R032).

### Luồng chuẩn (Happy Path) — Update 22-05-2025 SKU required Imei optional
1. Step 4 form mở cho SKU CCDC + required Imei.
2. Option Imei **auto bật nhưng không bắt buộc** (R023).
3. User nhập Imei → lưu vào; không nhập → để trống (R023).

### Luồng chuẩn (Happy Path) — Update 24-12-2024 mutex VAS + multi-user
1. VAS-A đang `In-Progress` bởi user1.
2. User2 vào danh sách phiên → thấy VAS-A màu Xanh dương nhưng **disable, không chọn được** (R010).
3. VAS-B (status `Mới` Xám) → user2 có thể chọn.
4. 2 user khác cùng dán VAS-C: khi update thông tin, API validate realtime → tránh data trùng (R011).

### Luồng chuẩn (Happy Path) — Crash recovery
1. User1 đang dán VAS-A, chụp 2 hình chưa lưu → app crash.
2. User1 re-launch App, scan lại PO → vào lại màn hình dán VAS-A (không cần chọn lại phiên) (R012).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — VAS chưa đánh giá chất lượng (Update 09-07-2025):** chọn VAS đỏ Cam → thông báo block (R013).
- **A2 — Category Sức khoẻ - Làm đẹp / Thuốc:** không qua bước chụp hình (R014, R015).
- **A3 — Sau Update 23-04-2025:** chỉ áp dụng chụp hình cho SP required Serial/Imei + không thuộc Sức khoẻ - Làm đẹp (R015).
- **A4 — SP không có Imei:** chụp hình + Lưu → hoàn thành VAS cho SKU đó luôn (R019).
- **A5 — SP có Imei nhưng không bắt buộc nhập (22-05-2025):** option Imei bật default nhưng skip cũng được (R023).
- **A6 — Scan 1 thông tin only (QRCode hoặc Serial):** scan tự add vào danh sách (R026).
- **A7 — Step 4 chỉnh sửa thông tin:** click icon → modify + validation lại (R027).

### Luồng ngoại lệ (Exception Paths)
- **E1 — PO chưa nhận hàng:** ERR-CPI-001 (R002).
- **E2 — PO không tồn tại:** ERR-CPI-002 (R003).
- **E3 — PO khác kho:** ERR-CPI-003 (R004).
- **E4 — PO VAS Completed:** ERR-CPI-004 (R005).
- **E5 — Chọn VAS đỏ Cam (chưa đánh giá):** block + thông báo (R013, Q-003).
- **E6 — Quá 5 hình:** không cho chụp thêm (R018).
- **E7 — Video > 15s:** không cho lưu (R018).
- **E8 — Quá 1 video:** không cho thêm video (R018).
- **E9 — Hoàn thành chưa đủ SL:** confirm dialog xác nhận → giữ In-Progress (R033).
- **E10 — VAS đang In-Progress của user khác:** disable không cho chọn (R010).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Scan PO — Receiving/Received check | rule | ✅ | PO phải có status `Receiving` hoặc `Received` |
| Scan PO — Existence check | rule | ✅ | PO phải tồn tại trên hệ thống |
| Scan PO — Warehouse check | rule | ✅ | PO phải thuộc kho user đang xử lý |
| Scan PO — VAS Completed check | rule | ✅ | VAS đã Completed → block, không cho dán lại |
| Phiên VAS màu | enum | ✅ | Xám (Mới chưa đánh giá có thể dán) / Xanh dương (In-Progress) / Cam (Mới chưa đánh giá chưa thể dán do thiếu QC) |
| Mutex 1 VAS / 1 user | rule | ✅ | 1 user/1 VAS/1 lần dán; VAS In-Progress của user khác → disable; user chỉ chọn được VAS `Mới` hoặc VAS đang làm |
| Multi-user concurrency | rule | ✅ | 1 VAS cho phép nhiều user dán cùng; mỗi update gọi API validate realtime đảm bảo không trùng |
| Crash recovery | rule | ✅ | Khi chưa lưu + chưa Hoàn thành 1 phần mà crash → vào lại màn hình dán phiên đã chọn |
| VAS QC requirement (Update 09-07-2025) | rule | ✅ | VAS yêu cầu QC chưa được đánh giá → block xác nhận dán |
| Category scope Step 3 (chụp hình) | rule | ✅ | KHÔNG áp dụng cho `Sức khoẻ - Làm đẹp` (Imei/date), `Thuốc`, `Thuốc (GPP)`; có thể bổ sung |
| Scope chụp hình (Update 23-04-2025) | rule | ✅ | Áp dụng cho SP required Serial/Imei và không thuộc `Sức khoẻ - Làm đẹp` |
| Hình ảnh | media | ❌ | Max 5 hình |
| Video | media | ❌ | Max 1 video; ≤ 15 giây |
| Lưu Step 3 (SP không Imei) | rule | ✅ | Lưu xem như hoàn thành VAS cho SKU đó; UID `Received → In-Bin` |
| Auto chọn QRCode (Step 4) | rule | ✅ | Cate CCDC + `wms_product.wms_config & 131072 > 0` → bật QRCode |
| Auto chọn Imei (Step 4) | rule | ✅ | `wms_product.config & 8 > 0` → bật Imei |
| Update 25-02-2025 Serial OFF + auto-gen | rule | ✅ | Serial luôn OFF dưới BE; nếu cần auto-gen pattern `[1023][YYMMDD][6 số tăng dần]` |
| Update 22-05-2025 Imei optional | rule | ✅ | SKU required Imei → auto bật nhưng không bắt buộc; nhập thì lưu, không nhập để trống |
| QRCode parser | rule | ✅ | QRCode in dạng Object → cắt chuỗi lấy field `Code` |
| Form scan logic | rule | ✅ | 1 info: scan tự add (nhập `+`); 2 info: QRCode pass → auto focus Serial |
| Phân biệt màu Step 4 | enum | ✅ | Xám chưa cập nhật / Xanh dương cập nhật 1 phần / Xanh lá đã đủ SL |
| Scan RFID — 2 option | enum | ✅ | (1) Nhiều SKU cùng lúc; (2) Từng SKU |
| RFID Case 1 (nội bộ) | rule | ✅ | RFID đã define hệ thống → cho cả 2 option, có tab Hợp lệ + Không hợp lệ |
| RFID Case 2 (vendor ngoài) | rule | ✅ | RFID chưa define → chỉ option từng SKU; tab Không hợp lệ rỗng |
| Hoàn thành VAS — chưa đủ SL | rule | ✅ | Confirm Yes → VAS `In-Progress`, update QRCode/Serial/Imei cho UID đã làm |
| Hoàn thành VAS — đủ SL | rule | ✅ | Confirm Yes → VAS `Completed`, update QRCode/Serial/Imei cho UID đã làm |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-CPI-001 | Validation | PO chưa được nhận hàng (chưa Receiving/Received) | `PO [PO code] chưa được nhận hàng.` | `PO [PO code] has not received yet.` | 07062#L1813-L1816 |
| ERR-CPI-002 | Validation | PO không tồn tại trên hệ thống | `PO [PO code] không tồn tại trên hệ thống.` | `PO [PO code] does not exist in the system.` | 07062#L1817-L1819 |
| ERR-CPI-003 | Validation | PO không thuộc kho đang xử lý | `PO [PO code] không thuộc kho đang xử lý.` | `PO [PO code] is not in the warehouse being processed.` | 07062#L1820-L1823 |
| ERR-CPI-004 | Validation | PO đã hoàn thành dán ID (VAS Completed) | `PO [PO code] đã hoàn thành việc dán ID cho sản phẩm.` | `PO [PO code] has completed pasting ID for the products.` | 07062#L1824-L1830 |
| MSG-CPI-005 | Warning | VAS yêu cầu QC chưa được đánh giá (Update 09-07-2025) | (raw không có verbatim — Q-003) | (raw không có verbatim — Q-003) | 07062#L1887-L1891 |
| MSG-CPI-006 | Confirm | Step 4 Lưu khi chưa đủ số dòng thông tin | (raw không có verbatim — Q-004) | (raw không có verbatim — Q-004) | 07062#L2002-L2009 |
| MSG-CPI-007 | Confirm | Step 5 Hoàn thành khi chưa đủ SL | (raw chỉ nêu "thông báo xác nhận" — Q-005) | (raw chỉ nêu "thông báo xác nhận" — Q-005) | 07062#L2050-L2053 |
| MSG-CPI-008 | Confirm | Step 5 Hoàn thành khi đủ SL | (raw chỉ nêu "thông báo xác nhận" — Q-005) | (raw chỉ nêu "thông báo xác nhận" — Q-005) | 07062#L2058-L2061 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Login App + vào Confirm paste ID**
  - **Given:** User có tài khoản hợp lệ.
  - **When:** User login + vào `Purchase order / Confirm paste ID`.
  - **Then:** Màn hình scan PO mở (R001).
- **AC-02 — PO chưa nhận hàng → ERR**
  - **Given:** PO `PO-001` status `New` (chưa Receiving/Received).
  - **When:** User scan `PO-001`.
  - **Then:** ERR-CPI-001 (R002).
- **AC-03 — PO không tồn tại → ERR**
  - **Given:** Hệ thống không có PO `PO-XYZ`.
  - **When:** User scan `PO-XYZ`.
  - **Then:** ERR-CPI-002 (R003).
- **AC-04 — PO khác kho → ERR**
  - **Given:** User xử lý kho A, PO `PO-002` thuộc kho B.
  - **When:** User scan `PO-002`.
  - **Then:** ERR-CPI-003 (R004).
- **AC-05 — PO VAS Completed → ERR**
  - **Given:** PO `PO-003` đã hoàn thành dán ID (VAS Completed).
  - **When:** User scan `PO-003`.
  - **Then:** ERR-CPI-004 (R005).
- **AC-06 — Danh sách phiên VAS theo PO**
  - **Given:** PO `PO-001` có 2 ASN status `Received`, mỗi ASN có 1 VAS chưa dán.
  - **When:** User scan `PO-001` thành công.
  - **Then:** Danh sách hiển thị 2 phiên VAS với info VAS + ASN + Người dán/nhận + Tổng SKU/item + Vị trí (R006).
- **AC-07 — Phân biệt màu phiên VAS (Xám/Xanh dương/Cam)**
  - **Given:** Danh sách có 3 VAS: VAS-A (Mới, đã đánh giá), VAS-B (In-Progress), VAS-C (Mới, chưa đánh giá QC required).
  - **When:** User xem danh sách.
  - **Then:** VAS-A màu Xám, VAS-B Xanh dương, VAS-C Cam (R007, R009).
- **AC-08 — Chọn VAS → chuyển In-Progress**
  - **Given:** VAS-A status `Mới` Xám.
  - **When:** User chọn VAS-A.
  - **Then:** VAS-A chuyển `In-Progress`, màu Xanh dương; user vào flow dán (R008, R009).
- **AC-09 — Mutex user khác (Update 24-12-2024)**
  - **Given:** VAS-A đang `In-Progress` bởi user1. User2 vào.
  - **When:** User2 xem danh sách.
  - **Then:** VAS-A disable, không cho chọn; user2 chỉ chọn được VAS `Mới` (R010).
- **AC-10 — Multi-user 1 VAS (Update 24-12-2024)**
  - **Given:** VAS-C đang `In-Progress` bởi user3 và user4.
  - **When:** User3 và user4 cùng cập nhật QRCode cho 1 SKU.
  - **Then:** API validate realtime → tránh trùng data; 1 update fail nếu QRCode đã được user kia add (R011).
- **AC-11 — Crash recovery (Update 24-12-2024)**
  - **Given:** User5 đang dán VAS-D, chụp 2 hình chưa lưu, chưa xác nhận. App crash.
  - **When:** User5 re-launch App, scan lại PO của VAS-D.
  - **Then:** Vào trực tiếp màn hình dán VAS-D (không cần chọn lại phiên) (R012).
- **AC-12 — VAS chưa đánh giá QC (Update 09-07-2025)**
  - **Given:** VAS-E required đánh giá chất lượng nhưng chưa được đánh giá.
  - **When:** User chọn VAS-E.
  - **Then:** Thông báo MSG-CPI-005 hiện; không cho vào flow dán (R013).
- **AC-13 — Step 3 không áp dụng cho Sức khoẻ - Làm đẹp**
  - **Given:** SP cate `Sức khoẻ - Làm đẹp` quản lý Imei.
  - **When:** User dán VAS.
  - **Then:** Bỏ qua bước chụp hình → vào Step 4 trực tiếp (R014).
- **AC-14 — Step 3 áp dụng SP required Serial/Imei (Update 23-04-2025)**
  - **Given:** SP cate `CCDC` required Serial.
  - **When:** User dán VAS.
  - **Then:** Step 3 chụp hình áp dụng (R015).
- **AC-15 — Chụp tối đa 5 hình**
  - **Given:** Form chụp hình mở.
  - **When:** User chụp 5 hình.
  - **Then:** Button `+` disable, không cho chụp thêm (R018).
- **AC-16 — Video tối đa 15s**
  - **Given:** Form quay video mở.
  - **When:** User quay 16s.
  - **Then:** Hệ thống stop tại 15s; chỉ lưu 15s đầu (R018).
- **AC-17 — Cả hình + video cùng SP**
  - **Given:** Form mở.
  - **When:** User chụp 3 hình + 1 video.
  - **Then:** Cả 2 media được lưu (R018).
- **AC-18 — SP không Imei → Lưu = hoàn thành SKU**
  - **Given:** SP `SKU-X` không quản lý Imei.
  - **When:** User chụp hình + click `Lưu`.
  - **Then:** VAS cho SKU-X hoàn thành; UID `Received → In-Bin` (R019).
- **AC-19 — Step 4 auto chọn QRCode cho CCDC**
  - **Given:** SP cate `CCDC` có `wms_config & 131072 > 0`.
  - **When:** User vào Step 4.
  - **Then:** Option QRCode tự bật (R021).
- **AC-20 — Update 25-02-2025 Serial OFF + auto-gen**
  - **Given:** SP CCDC không có Serial input.
  - **When:** User submit cập nhật.
  - **Then:** Hệ thống gen Serial pattern `[1023][YYMMDD][6 số]` (R022).
- **AC-21 — Update 22-05-2025 Imei optional**
  - **Given:** SKU required Imei.
  - **When:** Form Step 4 mở.
  - **Then:** Option Imei auto bật nhưng không bắt buộc; user skip cũng pass (R023).
- **AC-22 — QRCode parser Object → Code**
  - **Given:** QRCode in `{"Code":"ABC123","Other":"xyz"}`.
  - **When:** User scan.
  - **Then:** Hệ thống add `ABC123` vào danh sách (R025).
- **AC-23 — Auto focus QRCode → Serial khi 2 ON**
  - **Given:** Cả 2 QRCode + Serial ON.
  - **When:** User scan QRCode hợp lệ.
  - **Then:** Focus tự chuyển sang ô scan Serial/Imei (R026).
- **AC-24 — Phân biệt màu Step 4**
  - **Given:** SP-1 chưa cập nhật, SP-2 cập nhật 3/5, SP-3 cập nhật đủ 5/5.
  - **When:** User xem danh sách Step 4.
  - **Then:** SP-1 Xám, SP-2 Xanh dương, SP-3 Xanh lá (R028).
- **AC-25 — Scan RFID Case 1 cho nhiều SKU**
  - **Given:** SP từ nhà máy Long An (RFID đã define).
  - **When:** User chọn option scan nhiều SKU cùng lúc → đầu đọc đọc RFID.
  - **Then:** Tab `Hợp lệ` hiển thị RFID nhận; tab `không hợp lệ` rỗng (R030).
- **AC-26 — Scan RFID Case 2 chỉ từng SKU**
  - **Given:** SP từ vendor ngoài (RFID chưa define).
  - **When:** User cố scan nhiều SKU cùng lúc.
  - **Then:** Hệ thống chặn — chỉ cho scan từng SKU (R031).
- **AC-27 — Hoàn thành chưa đủ → VAS giữ In-Progress**
  - **Given:** VAS có 10 SP cần dán, user cập nhật 6 SP.
  - **When:** User click `Hoàn thành` → confirm Yes.
  - **Then:** VAS giữ status `In-Progress`; 6 UID đã update có QRCode/Serial/Imei (R033).
- **AC-28 — Hoàn thành đủ → VAS Completed**
  - **Given:** VAS có 10 SP, user cập nhật đủ 10.
  - **When:** User click `Hoàn thành` → confirm Yes.
  - **Then:** VAS `Completed`; 10 UID update đầy đủ (R034).
- **AC-29 — SKU required RFID skip chụp hình**
  - **Given:** SKU-Y required RFID.
  - **When:** User dán VAS cho SKU-Y.
  - **Then:** Step 3 chụp hình bị skip (R029).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R011 | API validation realtime cho multi-user — endpoint nào? Schema request/response? Có rate limit không? | Dev | Open | | | |
| Q-002 | R021 | BE config flags `wms_product.wms_config & 131072` và `config & 8` — bit list đầy đủ cho category nào dùng QRCode/Imei/Label code/RFID? | Dev | Open | | | |
| Q-003 | R013, MSG-CPI-005 | Verbatim VN+EN cho message khi VAS chưa được đánh giá QC mà chọn xác nhận dán. | PO/UX | Open | | | |
| Q-004 | R027, MSG-CPI-006 | Verbatim VN+EN cho confirm dialog Step 4 khi user cố Lưu mà chưa đủ số dòng thông tin. | PO/UX | Open | | | |
| Q-005 | R033, R034, MSG-CPI-007, MSG-CPI-008 | Verbatim VN+EN cho 2 confirm dialog Step 5 (chưa đủ SL vs đủ SL). 2 message có khác nhau không? | PO/UX | Open | | | |
| Q-006 | R014 | "Có thể bổ sung thêm 1 số category khác" — list dự kiến cập nhật là gì? Khi nào update? | PO | Open | | | |
| Q-007 | R007 | Định nghĩa "đã đánh giá chất lượng" — đánh giá đầy đủ tất cả tiêu chí hay 1 phần? VAS có nhiều SKU thì 1 SKU chưa đánh giá có khoá toàn VAS Cam không? | PO | Open | | | |
| Q-008 | R029, R030 | SKU required RFID — flag trên master SKU là gì (`is_rfid_required`)? Trùng với `required Imei` không? | Dev | Open | | | |
| Q-009 | R030, R031 | Case 1 vs Case 2 — hệ thống tự detect (theo origin SP / vendor flag) hay user phải chọn manual? | PO/Dev | Open | | | |
| Q-010 | R032 | "Xác nhận để submit thông tin cho từng sản phẩm" — submit từng SP hay submit batch all RFID đã scan? | Dev | Open | | | |
| Q-011 | R012 | Crash recovery state — lưu local hay server-side? User1 crash bao lâu thì state expire? | Dev | Open | | | |
| Q-012 | R018 | "Cả 2" hình + video — bắt buộc cả 2 hay là optional (có thể chỉ 1 loại)? | PO | Open | | | |
| Q-013 | R023 | Update 22-05-2025 — Imei "auto bật nhưng không bắt buộc" áp dụng cho SKU CCDC/CCDC PB hay tất cả cate có config Imei? | PO | Open | | | |
| Q-014 | R006 | "Người dán không có để trống, nếu phiên có nhiều người dán thì hiện người đầu tiên" — "đầu tiên" theo timestamp dán đầu hay alphabet email? | PO | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-38..S-43 | 2.17 (stub) | 2.17 | All R + AC | Draft |
| CHG-002 | Add | Update 24-12-2024: rules hiển thị phiên VAS theo màu + mutex user + multi-user concurrency + crash recovery | (trước 2.17) | 2.17 | R009-R012, AC-07, AC-08, AC-09, AC-10, AC-11 | Done (đã trong raw v2.17) |
| CHG-003 | Add | Update 09-07-2025: cảnh báo VAS yêu cầu QC chưa đánh giá khi xác nhận dán | (trước 2.17) | 2.17 | R013, AC-12 | Done (đã trong raw v2.17) |
| CHG-004 | Update | Update 23-04-2025: scope chụp hình áp dụng cho SP required Serial/Imei và không thuộc Sức khoẻ - Làm đẹp | (trước 2.17) | 2.17 | R015, AC-14 | Done (đã trong raw v2.17) |
| CHG-005 | Update | Update 25-02-2025: tắt Serial dưới BE, chỉ QRCode, Serial auto-gen pattern | (trước 2.17) | 2.17 | R022, AC-20 | Done (đã trong raw v2.17) |
| CHG-006 | Update | Update 22-05-2025: SKU required Imei → auto bật nhưng không bắt buộc | (trước 2.17) | 2.17 | R023, AC-21 | Done (đã trong raw v2.17) |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_confirm_paste_id | test_stub_receiving_po_confirm_paste_id | Add (chờ Gate 1B) | [[stub_receiving_po_vas]] (VAS sinh từ ASN + Serial/QRCode validation tương tự), [[stub_receiving_po_app]] (Receiving PO flow upstream), [[stub_qc_evaluation_result]] (QC required check), [[stub_receiving_po_vas_manual]] (Create/Update VAS Manual feature kế tiếp) | Q-001..Q-014 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R034, AC-01..AC-29 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-014 |

## 🚧 Blocked Coverage

- R011 — chờ Q-001 (API validation realtime endpoint)
- R021 — chờ Q-002 (BE config bits)
- R013, MSG-CPI-005 — chờ Q-003 (verbatim message QC chưa đánh giá)
- R027, MSG-CPI-006 — chờ Q-004 (verbatim Step 4 confirm)
- R033, R034, MSG-CPI-007, MSG-CPI-008 — chờ Q-005 (verbatim 2 confirm Step 5)
- R014 — chờ Q-006 (list cate bổ sung)
- R007 — chờ Q-007 (định nghĩa đã đánh giá QC)
- R029, R030 — chờ Q-008 (flag required RFID)
- R030, R031 — chờ Q-009 (detect Case 1 vs Case 2)
- R032 — chờ Q-010 (submit từng SP vs batch)
- R012 — chờ Q-011 (crash recovery state location + expire)
- R018 — chờ Q-012 (hình + video bắt buộc cả 2 hay optional)
- R023 — chờ Q-013 (scope cate Update 22-05-2025)
- R006 — chờ Q-014 (rules "Người đầu tiên")

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 20:15:00 | v1.1 | Refine stub → full spec: 34 R-ID, 29 AC, 25 BR, 8 messages (4 verbatim VN+EN, 4 missing — Q-003 Q-004 Q-005), 14 questions Open. `partial_read: false`. | refine-batch-4-2026-05-30 |
