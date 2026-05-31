---
aliases: [stub_receiving_po_invoice]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_invoice
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L1497-L1674
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-31 19:00:33"
verification_status: Verified
approved_by:
approved_at:
approval_note:
last_verified_source_version: 2.17

---

# REQ: stub_receiving_po_invoice

## Tổng quan
- **Mã tính năng:** stub_receiving_po_invoice
- **Feature:** Thêm hoá đơn cho PO + Case 2 (nhận PO Gift chung với PO thường)
- **Mô tả ngắn:** Cuối flow nhận PO, nếu PO chưa được bổ sung hoá đơn → hiển thị button `Thêm hoá đơn`. Form nhập gồm Tax code/Serial/Form/Total/Ngày/Ghi chú/Hình ảnh với validation chi tiết (1-8 chars, total chênh ≤ 1000 đồng, ngày ≤ hiện tại). Cho phép thêm nhiều hoá đơn. Hỗ trợ case PO gốc + PO Gift cùng yêu cầu add invoice (user chọn PO nào cần add). Case 2 nhận PO Gift chung PO thường: scan, validate, share SL ưu tiên cho PO Gift, cập nhật chứng từ cho cả 2 PO.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Nhân viên kho (user nhận hàng và add invoice).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[ts_receiving_po_invoice]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_receiving_po_inbound_shipment]] (SL confirm), [[stub_receiving_po_gift]] (rules PO gift). ➡️ feed [[stub_receiving_po_asn]] (Taxcode trong biên bản).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07062_Receiving_PO_Docs_ver2.17.md | 2.17 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Raw không mô tả API explicit | N/A |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Sau khi kết thúc nhận hàng và SL thực nhận đủ với SL confirm của PO, nếu PO chưa được bổ sung hoá đơn → hiển thị button `Thêm hoá đơn` | Functional | High | ✅ | 07062#L1500-L1502 |
| R002 | User click `Thêm hoá đơn` → hệ thống hiển thị 2 lưu ý liên tiếp: lưu ý 1 có button `Kiểm tra lại` (tắt) + `Xác nhận` (tiếp); lưu ý 2 có `Kiểm tra lại` (tắt) + `Tôi đã hiểu` (tiếp) | Functional + UX | High | ✅ | 07062#L1503-L1512 |
| R003 | Form nhập hoá đơn — `Tax code` (Mã số thuế): bắt buộc; format 1-8 ký tự (chữ + số), không ký tự đặc biệt | Validation | High | ✅ | 07062#L1516-L1527 |
| R004 | Form nhập hoá đơn — `Serial` (Ký hiệu): bắt buộc; format 1-8 ký tự (chữ + số), không ký tự đặc biệt | Validation | High | ✅ | 07062#L1528-L1538 |
| R005 | Form nhập hoá đơn — `Form` (Mẫu số): bắt buộc | Validation | High | ✅ | 07062#L1539-L1543 |
| R006 | Form nhập hoá đơn — `Total` (Tổng tiền): phải bằng hoặc chênh lệch tổng tiền PO không quá **1.000 đồng** | Validation | High | ✅ | 07062#L1544-L1553 |
| R007 | Khi PO có nhiều hoá đơn: **tổng tiền của tất cả hoá đơn** phải bằng tổng tiền PO hoặc chênh ≤ 1.000 đồng | Validation + Business rule | High | ✅ | 07062#L1554-L1561 |
| R008 | Form nhập hoá đơn — `Ngày`: default ngày hiện tại, format `YYYY-MM-DD`; chỉ cho chọn ngày hiện tại hoặc quá khứ, không cho chọn ngày tương lai | Validation | High | ✅ | 07062#L1562-L1564 |
| R009 | Form nhập hoá đơn — button `Đóng`: tắt popup không lưu | Functional | High | ✅ | 07062#L1565 |
| R010 | Form nhập hoá đơn — button `Thêm`: cập nhật thông tin hoá đơn; nếu chưa nhập đầy đủ thông tin → cảnh báo nhập thông tin tương ứng | Functional + Validation | High | ✅ | 07062#L1566-L1568 |
| R011 | Form nhập hoá đơn — `Ghi chú`: input optional | UI | Medium | ✅ | 07062#L1569 |
| R012 | Form nhập hoá đơn — `Hình ảnh hoá đơn`: button `+` mở camera để chụp hoặc lấy từ thư viện ảnh; max 2 hình / hoá đơn | Functional | High | ✅ | 07062#L1570-L1572 |
| R013 | User có thể thêm nhiều hoá đơn cho 1 PO | Business rule | High | ✅ | 07062#L1573 |
| R014 | Khi PO gốc + PO gift cùng yêu cầu add invoice: hệ thống yêu cầu user chọn PO cần add invoice. Bước add hoá đơn và cập nhật tương tự như chỉ add cho PO gốc | Functional | High | ✅ | 07062#L1579-L1583 |
| R015 | Button `Hoàn thành PO` chỉ hiển thị khi tất cả thông tin hoá đơn đã cập nhật đầy đủ bao gồm hình ảnh | Functional + Validation | High | ✅ | 07062#L1587-L1589 |
| R016 | Case 2 nhận PO Gift chung PO thường — Step 1: nếu PO có PO gift đi kèm, sau khi scan PO thường thành công → cảnh báo user phải scan PO Gift để nhận chung | Functional | High | ✅ | 07062#L1599-L1601 |
| R017 | Case 2 — validation khi scan PO Gift: PO không thuộc PO đang nhận → thông báo; PO chưa verify invoice (trừ PO Gift 0 đồng) → thông báo; PO đã Received → thông báo | Validation | High | ✅ | 07062#L1602-L1609 |
| R018 | Case 2 — PO hợp lệ → hiển thị thông tin PO 2 lên màn hình | UI | High | ✅ | 07062#L1610-L1611 |
| R019 | Case 2 — Step 1.1 Chọn Loại nhận hàng cho PO (tham khảo mô tả luồng chung) | Functional | High | ✅ | 07062#L1613-L1613 |
| R020 | Case 2 — Step 1.2 Scan vị trí hoặc giỏ cần chuyển hàng vào — giống Case 1 | Functional | High | ✅ | 07062#L1618-L1621 |
| R021 | Case 2 — Step 2 Scan sản phẩm: tương tự PO thường. Nếu PO thường + PO Gift có cùng SKU, scan 1 lần mà SL SKU ≠ tổng SL của 2 PO → ưu tiên SL cho PO Gift trước (để PO Gift luôn phải nhận đủ hàng); phân biệt SKU PO Gift dựa vào giá nhỏ hơn | Business rule | High | ✅ | 07062#L1623-L1631 |
| R022 | Case 2 — Step 3 Xem danh sách sản phẩm: do có 2 PO nên user chọn PO nào cần xem thông tin | UI | High | ✅ | 07062#L1636-L1636 |
| R023 | Case 2 — Step 4 Cập nhật hình ảnh chứng từ cho PO gốc và PO gift: chọn `Thêm biên bản giao hàng`; PO có đồng kiểm → chụp `biên bản giao nhận hàng hoá`; PO không đồng kiểm → chụp `biên bản bàn giao kiện hàng` | Functional | High | ✅ | 07062#L1642-L1647 |
| R024 | Step 4 — form fields hiển thị: `Kho`, `Tổng tiền`, `Không đồng kiểm/Đồng kiểm`, `Vị trí`, `Tổng SKU`, `Tổng sản phẩm`, `Ghi chú`, `Hình ảnh chứng từ` | UI | High | ✅ | 07062#L1644-L1655 |
| R025 | Step 4 — icon camera mở camera chụp hình chứng từ; max 2 hình; button `Xoá hình` để chụp lại; click `Lưu` để lưu hình ảnh | Functional | High | ✅ | 07062#L1649-L1655 |
| R026 | Update 20-11-2024: bổ sung biên bản giao hàng của PO Gift; khi cập nhật đầy đủ hình ảnh PO gốc + PO gift → button `Lưu` hiển thị | Functional | High | ✅ | 07062#L1657-L1662 |
| R027 | Update 20-11-2024: với case 2 PO, button `Kết thúc nhận hàng` đổi thành `Kết thúc nhận hàng cả 2 PO`; button `Hoàn thành PO` đổi thành `Hoàn thành cả 2 PO` | UI | High | ✅ | 07062#L1663-L1666 |
| R028 | Update 20-11-2024: thông báo xác nhận đổi thành ... (raw bị cắt — verbatim không rõ — Q-010) | UX | Medium | ⚠️ | 07062#L1667-L1668 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- PO ở status `Receiving` hoặc gần `Received`.
- SL thực nhận của PO đã đủ với SL confirm.
- PO chưa có hoá đơn trên hệ thống.

### Luồng chuẩn (Happy Path) — Add invoice cho PO single
1. User kết thúc scan nhận hàng PO → button `Thêm hoá đơn` hiện (R001).
2. Click `Thêm hoá đơn` → 2 lưu ý liên tiếp: lưu ý 1 → click `Xác nhận`; lưu ý 2 → click `Tôi đã hiểu` (R002).
3. Form nhập hoá đơn mở:
   - Tax code: `0123456A` (1-8 chars valid) (R003)
   - Serial: `AA01` (R004)
   - Form: `01` (R005)
   - Total: 1.500.000 (chênh PO 1.500.000 = 0, OK) (R006)
   - Ngày: today (R008)
   - Ghi chú: optional (R011)
   - Hình ảnh: chụp 1 hình + thư viện 1 hình = 2 hình (R012)
4. Click `Thêm` → hoá đơn đầu lưu (R010).
5. Button `Hoàn thành PO` hiển thị (R015) — user click hoàn thành.

### Luồng chuẩn (Happy Path) — Case 2 (PO gốc + PO Gift)
1. User scan PO thường (PO_A) thành công.
2. Hệ thống cảnh báo user phải scan PO Gift (R016).
3. User scan PO_AG → validate (R017): hợp lệ → hiển thị PO 2 (R018).
4. Step 1.1 chọn Loại nhận hàng (R019); Step 1.2 scan vị trí/giỏ (R020).
5. Scan SKU lần lượt; nếu cùng SKU PO thường + PO Gift → ưu tiên SL cho PO Gift (R021).
6. Xem danh sách sản phẩm — user chọn PO nào để xem (R022).
7. `Thêm biên bản giao hàng` cho cả 2 PO: chụp `biên bản giao nhận` (đồng kiểm) hoặc `biên bản bàn giao kiện` (không đồng kiểm) (R023, R024).
8. Camera, max 2 hình, `Lưu` (R025).
9. Update 20-11-2024: sau khi đủ hình PO gốc + Gift → button `Lưu` hiện; click `Kết thúc nhận hàng cả 2 PO` → `Hoàn thành cả 2 PO` (R026, R027).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — Thêm nhiều hoá đơn:** tổng các hoá đơn phải bằng tổng PO hoặc chênh ≤ 1000đ (R013, R007).
- **A2 — PO gốc + PO Gift cùng yêu cầu add invoice:** hệ thống yêu cầu user chọn PO trước khi add (R014).
- **A3 — PO Gift 0 đồng:** miễn validate "chưa verify invoice" (R017 exception).

### Luồng ngoại lệ (Exception Paths)
- **E1 — Tax code không hợp lệ:** message `Mã số thuế phải từ 1 đến 8 chữ số` (R003 / ERR-INV-002).
- **E2 — Serial không hợp lệ:** message `Ký hiệu phải từ 1 đến 8 chữ số` (R004 / ERR-INV-003).
- **E3 — Total chênh > 1000đ:** message `Tổng số tiền tren hoá đơn không hợp lệ` (R006, R007 / ERR-INV-004).
- **E4 — Field bắt buộc trống:** message `Thông tin là bắt buộc` (R010 / ERR-INV-001).
- **E5 — Ngày tương lai:** UI block date picker; raw không có message verbatim — Q-002.
- **E6 — Case 2 scan PO Gift không hợp lệ:** 3 thông báo riêng cho 3 trigger (PO không thuộc, chưa verify, đã Received) (R017).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Trigger `Thêm hoá đơn` | rule | ✅ | SL thực nhận đủ SL confirm + PO chưa có hoá đơn |
| `Tax code` | string | ✅ | 1-8 chars; chữ + số; không ký tự đặc biệt |
| `Serial` | string | ✅ | 1-8 chars; chữ + số; không ký tự đặc biệt |
| `Form` | string | ✅ | (raw không nêu validation format chi tiết) |
| `Total` (single invoice) | number | ✅ | `|Total - PO_total| ≤ 1.000 VND` |
| `Total` (multi invoice) | number | ✅ | `|sum(invoices.Total) - PO_total| ≤ 1.000 VND` |
| `Ngày` | date YYYY-MM-DD | ✅ | ≤ today; default = today |
| `Hình ảnh hoá đơn` | image | ✅ | Max 2 hình / hoá đơn |
| `Hình ảnh chứng từ` (Step 4) | image | ✅ | Max 2 hình; có button `Xoá hình` |
| PO Gift 0 đồng | rule | ✅ | Miễn validate "chưa verify invoice" trong case 2 |
| Cùng SKU PO thường + Gift | rule | ✅ | Ưu tiên SL cho PO Gift; phân biệt SKU dựa giá nhỏ hơn = PO Gift |
| `Hoàn thành PO` visibility | rule | ✅ | Chỉ hiện khi tất cả hoá đơn đầy đủ thông tin + hình ảnh |
| Update 20-11-2024 — case 2 PO | UI rule | ✅ | Button "Kết thúc nhận hàng cả 2 PO" + "Hoàn thành cả 2 PO" |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-INV-001 | Validation | Field bắt buộc trống (Tax code/Serial/Form) | `Thông tin là bắt buộc` | `Information is required.` | 07062#L1519-L1520, L1531-L1532, L1542-L1543 |
| ERR-INV-002 | Validation | Tax code không đủ 1-8 ký tự hoặc có ký tự đặc biệt | `Mã số thuế phải từ 1 đến 8 chữ số` (raw rule L1516 ghi "chữ + số" nhưng message L1527 ghi "chữ số" — Q-013) | `Tax code must be from 1 to 8 digits` | 07062#L1525-L1527 |
| ERR-INV-003 | Validation | Serial không đủ 1-8 ký tự hoặc có ký tự đặc biệt | `Ký hiệu phải từ 1 đến 8 chữ số` (raw rule L1528 ghi "chữ + số" nhưng message L1538 ghi "chữ số" — Q-013) | `Serial must be from 1 to 8 digits` | 07062#L1537-L1538 |
| ERR-INV-004 | Validation | Total chênh PO > 1.000 đồng (single hoặc multi-invoice) | `Tổng số tiền tren hoá đơn không hợp lệ` (lưu ý typo `tren` — Q-004) | `Total amount on invoice is invalid` | 07062#L1551-L1553, L1559-L1561 |
| MSG-INV-005 | Warning | Sau scan PO thường có PO gift đi kèm | (chưa có verbatim — Q-009) | (chưa có verbatim — Q-009) | 07062#L1599-L1601 |
| MSG-INV-006 | Validation | Case 2 scan PO Gift không thuộc PO đang nhận | (chưa có verbatim — Q-009) | (chưa có verbatim — Q-009) | 07062#L1602 |
| MSG-INV-007 | Validation | Case 2 scan PO Gift chưa verify invoice (trừ PO Gift 0 đồng) | (chưa có verbatim — Q-009) | (chưa có verbatim — Q-009) | 07062#L1603-L1604 |
| MSG-INV-008 | Validation | Case 2 scan PO Gift đã Received | (chưa có verbatim — Q-009) | (chưa có verbatim — Q-009) | 07062#L1608-L1609 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Show button `Thêm hoá đơn`**
  - **Given:** PO_A nhận đủ SL, chưa có hoá đơn.
  - **When:** User kết thúc nhận hàng.
  - **Then:** Button `Thêm hoá đơn` hiển thị (R001).
- **AC-02 — 2 lưu ý liên tiếp**
  - **Given:** User click `Thêm hoá đơn`.
  - **When:** Click `Xác nhận` ở lưu ý 1.
  - **Then:** Lưu ý 2 hiện; click `Tôi đã hiểu` → form nhập hoá đơn mở (R002).
- **AC-03 — Tax code 1-8 chars valid**
  - **Given:** Form nhập hoá đơn.
  - **When:** User nhập `0123456A` (7 chars chữ+số).
  - **Then:** Field valid (R003).
- **AC-04 — Tax code invalid**
  - **Given:** Form mở.
  - **When:** User nhập `01234567890` (>8 chars).
  - **Then:** Message ERR-INV-002 (R003).
- **AC-05 — Tax code rỗng**
  - **Given:** Form mở.
  - **When:** User click `Thêm` không nhập Tax code.
  - **Then:** Message ERR-INV-001 dưới Tax code (R003, R010).
- **AC-06 — Total chênh ≤ 1000đ valid**
  - **Given:** PO total = 1.500.000.
  - **When:** User nhập Total = 1.499.500 (chênh 500đ).
  - **Then:** Field valid (R006).
- **AC-07 — Total chênh > 1000đ invalid**
  - **Given:** PO total = 1.500.000.
  - **When:** User nhập Total = 1.498.000 (chênh 2000đ).
  - **Then:** Message ERR-INV-004 (R006).
- **AC-08 — Multi-invoice total sum**
  - **Given:** PO total = 1.500.000. Hoá đơn 1 = 800.000.
  - **When:** User thêm hoá đơn 2 với Total = 600.000 (sum = 1.400.000, chênh 100.000đ).
  - **Then:** Message ERR-INV-004 (R007).
- **AC-09 — Ngày tương lai bị block**
  - **Given:** Today = 2026-05-30.
  - **When:** User chọn date = 2026-06-01.
  - **Then:** Date picker không cho chọn (R008).
- **AC-10 — Image upload max 2**
  - **Given:** Field Hình ảnh.
  - **When:** User chụp 2 hình.
  - **Then:** Button `+` disable / không cho upload thêm (R012).
- **AC-11 — Thêm nhiều hoá đơn**
  - **Given:** PO_A đã có 1 hoá đơn 800k; PO total = 1500k.
  - **When:** User click thêm hoá đơn 2 với Total = 700k.
  - **Then:** 2 hoá đơn cùng lưu cho PO_A; sum = 1500k = PO total (R013).
- **AC-12 — PO gốc + PO Gift cùng yêu cầu add invoice**
  - **Given:** PO_A (gốc) + PO_AG (gift) đều yêu cầu invoice.
  - **When:** User click `Thêm hoá đơn`.
  - **Then:** Hệ thống yêu cầu user chọn PO_A hoặc PO_AG (R014).
- **AC-13 — Hoàn thành PO chỉ enable khi đủ thông tin**
  - **Given:** Hoá đơn 1 chưa có hình ảnh.
  - **When:** User xem flow add invoice.
  - **Then:** Button `Hoàn thành PO` không hiện; sau khi upload hình → button hiện (R015).
- **AC-14 — Case 2 scan PO thường → cảnh báo scan PO Gift**
  - **Given:** PO_A có PO Gift PO_AG đi kèm.
  - **When:** User scan PO_A thành công.
  - **Then:** Cảnh báo MSG-INV-005 hiện (R016).
- **AC-15 — Case 2 scan PO Gift không thuộc PO đang nhận**
  - **Given:** PO_A scan đầu.
  - **When:** User scan PO_X không phải PO Gift của PO_A.
  - **Then:** Thông báo MSG-INV-006 (R017).
- **AC-16 — Case 2 PO Gift chưa verify invoice**
  - **Given:** PO_AG chưa verify invoice, không phải PO Gift 0 đồng.
  - **When:** User scan PO_AG.
  - **Then:** Thông báo MSG-INV-007 (R017).
- **AC-17 — PO Gift 0 đồng bypass**
  - **Given:** PO_AG là PO Gift 0 đồng, chưa verify invoice.
  - **When:** User scan PO_AG.
  - **Then:** Bypass validation; hiển thị PO_AG thông tin (R017 exception).
- **AC-18 — Case 2 cùng SKU phân chia SL ưu tiên PO Gift**
  - **Given:** PO_A SKU_X 5 cái, PO_AG SKU_X 2 cái (giá thấp hơn). User scan SKU_X 4 cái.
  - **When:** Phân chia.
  - **Then:** PO_AG nhận 2 cái (ưu tiên đủ), PO_A nhận 2 cái (R021).
- **AC-19 — Case 2 xem danh sách sản phẩm chọn PO**
  - **Given:** Case 2 nhận xong.
  - **When:** User chọn xem danh sách.
  - **Then:** Hệ thống yêu cầu user chọn PO_A hoặc PO_AG (R022).
- **AC-20 — Step 4 PO đồng kiểm chụp biên bản giao nhận**
  - **Given:** PO_A có đồng kiểm = Yes.
  - **When:** User chụp biên bản.
  - **Then:** Label hiển thị `biên bản giao nhận hàng hoá` (R023).
- **AC-21 — Step 4 PO không đồng kiểm chụp biên bản bàn giao kiện**
  - **Given:** PO_B không đồng kiểm.
  - **When:** User chụp biên bản.
  - **Then:** Label hiển thị `biên bản bàn giao kiện hàng` (R023).
- **AC-22 — Update 20-11-2024 — button "Kết thúc nhận hàng cả 2 PO"**
  - **Given:** Case 2 (PO gốc + Gift) đã cập nhật đủ hình ảnh.
  - **When:** User xem button.
  - **Then:** Button hiện `Kết thúc nhận hàng cả 2 PO` thay vì `Kết thúc nhận hàng` (R027).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R002 | Verbatim VN cho 2 lưu ý dialog khi click `Thêm hoá đơn` (raw chỉ mô tả buttons, không có message text). | PO/UX | Open | | | |
| Q-002 | R008, E5 | Khi user cố chọn ngày tương lai, UI block date picker hay hiển thị message? Verbatim message nếu có? | UX | Open | | | |
| Q-003 | R006, R007 | Đơn vị "1.000 đồng" = VND fix hard-coded, hay configurable? Cho PO ngoại tệ (nếu có) thì rule ra sao? | PO | Open | | | |
| Q-004 | ERR-INV-004 | Message ERR-INV-004 raw ghi `Tổng số tiền tren hoá đơn không hợp lệ` — typo `tren` (thiếu dấu) → cần fix thành `trên`. Verify trước khi implement. | PO/UX | Open | | | |
| Q-005 | R024 | Raw L1647 ghi `không đồng kiếm` — typo `kiếm` → `kiểm`? Verify. | PO/UX | Open | | | |
| Q-006 | R017 | Định nghĩa "PO Gift 0 đồng": là PO Gift có `Total` = 0, hay có flag riêng (`zero_value_gift`)? Cách detect? | PO/Dev | Open | | | |
| Q-007 | R014 | Khi PO gốc + PO gift đều yêu cầu add invoice và user chỉ chọn 1 → PO còn lại có timeout, reminder, hay phải re-trigger flow lại? | PO | Open | | | |
| Q-008 | R021 | Khi PO thường + PO Gift có cùng SKU và 2 SKU có cùng giá — rules phân biệt SKU PO Gift bằng gì (raw chỉ nói "dựa vào giá nhỏ hơn")? | PO | Open | | | |
| Q-009 | MSG-INV-005..008 | Verbatim VN+EN cho 4 thông báo trong S-29 (cảnh báo scan PO Gift, PO không thuộc, chưa verify, đã Received). | PO | Open | | | |
| Q-010 | R028 | Update 20-11-2024 thông báo xác nhận đổi thành ... (raw bị cắt). Verbatim VN+EN là gì? | PO | Open | | | |
| Q-011 | R007 | Nếu user nhập thừa 1 hoá đơn khiến sum vượt > 1.000đ — hệ thống block ngay khi nhập hoá đơn cuối hay khi user thử Hoàn thành PO? | UX | Open | | | |
| Q-012 | R005 | Field `Form` (mẫu số) — có format validation (vd length, alphanumeric) không? Raw không nêu rule. | PO/Dev | Open | | | |
| Q-013 | R003, R004, ERR-INV-002, ERR-INV-003 | Raw-internal inconsistency: rule nêu "1-8 ký tự **chữ + số**" (alphanumeric) nhưng message nêu "1 đến 8 **chữ số**" (có thể hiểu là chỉ digit). Thực tế Tax code và Serial có cho phép ký tự chữ cái không? Confirm ý định đúng. | PO/Dev | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-28, S-29, S-30 | 2.17 (stub) | 2.17 | All R + AC | Draft |
| CHG-002 | Update | Update 20-11-2024: bổ sung biên bản PO Gift + đổi button text cho case 2 PO | (trước 1.6) | 1.6 | R026-R028, AC-22 | Done (đã trong raw v2.17) |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_invoice | test_stub_receiving_po_invoice | Add (chờ Gate 1B) | [[stub_receiving_po_gift]] (case 2 PO Gift), [[stub_receiving_po_inbound_shipment]] (SL confirm + Mô tả `PO chưa được xác nhận hoá đơn`), [[stub_receiving_po_asn]] (Taxcode mapping) | Q-001..Q-012 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R028, AC-01..AC-22 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-012 |

## 🚧 Blocked Coverage

- R002, AC-02 — chờ Q-001 (verbatim 2 lưu ý)
- R008, E5 — chờ Q-002 (date picker behavior + message)
- R006, R007 — chờ Q-003 (đơn vị tiền + currency rules)
- ERR-INV-004 — chờ Q-004 (typo `tren`)
- R024 — chờ Q-005 (typo `kiếm`)
- R017, AC-17 — chờ Q-006 (định nghĩa PO Gift 0 đồng)
- R014 — chờ Q-007 (timeout/reminder PO còn lại)
- R021, AC-18 — chờ Q-008 (cùng SKU cùng giá)
- MSG-INV-005..008 — chờ Q-009 (verbatim 4 thông báo)
- R028 — chờ Q-010 (verbatim confirmation message)
- R007 — chờ Q-011 (timing block validation)
- R005 — chờ Q-012 (Form format)
- R003, R004, ERR-INV-002, ERR-INV-003 — chờ Q-013 (raw-internal inconsistency: "chữ + số" vs "chữ số")

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:36:55 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 17:15:00 | v1.1 | Refine stub → full spec: 28 R-ID, 22 AC, 13 BR, 8 messages (4 verbatim VN+EN, 4 missing), 12 questions Open. `partial_read: false`. | refine-batch-2-2026-05-30 |
| 2026-05-31 18:50:00 | v1.2 | FIX-003 (refiner batch-5): thêm Q-013 raw-internal inconsistency "chữ + số" vs "chữ số" cho ERR-INV-002/003 + R003/R004; cập nhật Error Messages Map + Blocked Coverage. | refiner-spec-scoped-batch-5 |
