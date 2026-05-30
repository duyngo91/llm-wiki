---
aliases: [stub_receiving_po_fabric]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_fabric
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L1676-L1737
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 18:00:00"
verification_status: Pending
approved_by:
approved_at:
approval_note:
---

# REQ: stub_receiving_po_fabric

## Tổng quan
- **Mã tính năng:** stub_receiving_po_fabric
- **Feature:** Nhận hàng Vải khai báo Group UID + Scan RFID mapping
- **Mô tả ngắn:** Áp dụng cho các SKU Vải không quản lý theo UID (Thời trang BTP/Phụ liệu/NVL, tên có "Vải"). Form scan nhận có 2 input chính: `Nhóm UID` (optional, status `New`) và `Số lượng` (Kg/Mét quy đổi). Update 10-11-2025: có thể chuyển sang scan RFID mapping. Update 10-12-2025: với SKU quản lý UID group, scan nhận bằng RFID mapping có 2 case — RFID chưa tồn tại (gen UID group mới) hoặc RFID/UID group đã tồn tại từ Transfer company (suggest SL, gen UID group mới mapping vào). Rule khoá: 1 SKU chỉ nhận hoặc theo RFID/UID Group hoặc theo SL, không cùng lúc 2 loại.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Nhân viên kho (user scan nhận hàng Vải).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[test_stub_receiving_po_fabric]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_receiving_po_app]] (flow scan nhận trên App), [[stub_receiving_po_inbound_shipment]] (SL confirm PO). ↔️ liên quan [[stub_receiving_po_vas]] (UID group, Serial/Imei concepts).

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
| R001 | Áp dụng nhận hàng Vải khai báo Group UID cho các SKU **không quản lý theo UID**, thuộc category `Thời trang (bán thành phẩm)` / `Thời trang (Phụ liệu)` / `Thời trang (NVL)`, và **tên sản phẩm có chứa từ "Vải"** | Functional | High | ✅ | 07062#L1679-L1686 |
| R002 | Nếu SKU **không quản lý số lô và hạn sử dụng** → hệ thống hiện form scan nhận với 2 input chính (`Nhóm UID` + `Số lượng`) để user cập nhật thông tin | Functional + UI | High | ✅ | 07062#L1688-L1705 |
| R003 | Field `Nhóm UID`: scan nhóm UID đại diện cho cây/tấm vải; **không bắt buộc**. Nếu không khai báo Nhóm UID → chỉ cần nhập `Số lượng` và xác nhận như nhận SKU theo số lượng bình thường | Validation + Functional | High | ✅ | 07062#L1692-L1695 |
| R004 | Validation `Nhóm UID`: nhóm UID scan vào **phải có trạng thái `New`**; nếu không đúng → báo lỗi | Validation | High | ✅ | 07062#L1696-L1697 |
| R005 | Update 10-11-2025: ở bước scan `Nhóm UID`, user **có thể chuyển qua scan RFID mapping** thay vì scan UID group | Functional | High | ✅ | 07062#L1698 |
| R006 | Business rule khoá: **1 SKU chỉ có thể nhận theo 1 trong 2 loại** — hoặc theo RFID mapping/UID Group, hoặc theo số lượng, **không cùng lúc cả 2 loại**. Khi user đã khai báo `Số lượng` + chọn `+` để thêm vào danh sách → input `Nhóm UID` và `Số lượng` sẽ **ẩn đi**, không cho thêm mới | Business rule | High | ✅ | 07062#L1699-L1701 |
| R007 | Field `Số lượng`: là **số Kg hoặc Mét** của cây/tấm vải được quy đổi ra số lượng khi nhận hàng. Tổng `Số lượng` được cộng lại cho tất cả cây/tấm vải để ra **tổng SL của SKU cần nhận cho PO** | Validation + Business rule | High | ✅ | 07062#L1702-L1705 |
| R008 | Sau khi scan nhận `Nhóm UID` + `Số lượng`, user chọn `Xác nhận` để **ghi nhận vào danh sách** | Functional | High | ✅ | 07062#L1705 |
| R009 | Nếu SKU **có quản lý số lô và hạn sử dụng** → hệ thống hiện form scan nhận với các input: `Nhóm UID`, `Số lượng`, **thông tin số lô và hạn sử dụng** | Functional + UI | High | ✅ | 07062#L1709-L1717 |
| R010 | Update màn hình chi tiết sản phẩm của các sản phẩm đã nhận đủ số lượng (S-32 — raw chỉ có heading, không có content chi tiết — Q-005) | Functional | Medium | ⚠️ | 07062#L1722 |
| R011 | Update 10-12-2025: với SKU **có quản lý UID group**, user có thể **scan nhận bằng RFID mapping** | Functional | High | ✅ | 07062#L1726-L1727 |
| R012 | Case 1 (Update 10-12-2025) — Nếu **RFID mapping chưa tồn tại** trên hệ thống: hành xử giống như khai báo 1 UID group mới theo luồng ban đầu. Khi user submit → hệ thống **tự gen 1 UID group mới** và **mapping với RFID** được scan vào | Business rule + Functional | High | ✅ | 07062#L1728-L1730 |
| R013 | Case 2 (Update 10-12-2025) — Nếu **RFID mapping hoặc UID group scan vào đã tồn tại** (chạy cho luồng Transfer company, khi RFID/UID group ở công ty xuất đã được `out`): hệ thống **suggest số lượng** sản phẩm của UID group và **cho phép user edit số lượng theo UID group**. Khi user submit → hệ thống tự gen 1 UID group mới và mapping với RFID scan vào | Business rule + Functional | High | ✅ | 07062#L1731-L1734 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- PO có SKU thuộc category `Thời trang (BTP)`, `Thời trang (Phụ liệu)`, `Thời trang (NVL)` và tên sản phẩm có chứa "Vải" (R001).
- User đang ở flow Receiving PO trên App, bước scan SKU (xem [[stub_receiving_po_app]]).

### Luồng chuẩn (Happy Path) — SKU không quản lý số lô + HSD, scan UID group
1. User scan SKU Vải thoả R001 → hệ thống mở form scan nhận (R002).
2. User scan `Nhóm UID` của cây/tấm vải đầu tiên (R003).
   - Validation: nhóm UID có status `New` (R004) — nếu OK thì pass.
3. User nhập `Số lượng` Kg hoặc Mét (R007).
4. User click `Xác nhận` → record được ghi vào danh sách (R008).
5. Lặp lại bước 2-4 cho từng cây/tấm vải khác trong PO.
6. Tổng `Số lượng` các record cộng lại → tổng SL SKU đã nhận (R007).

### Luồng chuẩn (Happy Path) — SKU không quản lý lô/HSD, scan theo số lượng (skip UID group)
1. User scan SKU Vải thoả R001 → form mở (R002).
2. User bỏ qua field `Nhóm UID`, chỉ nhập `Số lượng` (R003).
3. User click `+` thêm vào danh sách → input `Nhóm UID` + `Số lượng` ẩn đi, không cho thêm record mới cho SKU này (R006).
4. SKU này được khoá flow "theo số lượng" — không thể switch sang RFID/UID Group nữa cho đến khi reset.

### Luồng chuẩn (Happy Path) — SKU không quản lý lô/HSD, scan RFID mapping (Update 10-11-2025)
1. User scan SKU Vải thoả R001 → form mở (R002).
2. User chuyển sang scan RFID mapping thay cho `Nhóm UID` (R005).
3. User nhập `Số lượng`, click `Xác nhận` → record ghi vào danh sách (R008).

### Luồng chuẩn (Happy Path) — SKU có quản lý số lô + HSD
1. User scan SKU Vải có quản lý số lô/HSD → form mở với thêm input số lô + HSD (R009).
2. User scan `Nhóm UID`, nhập `Số lượng`, cập nhật số lô + HSD.
3. User click `Xác nhận` → record ghi vào danh sách (R008).

### Luồng chuẩn (Happy Path) — Update 10-12-2025: scan RFID mapping (SKU có UID group)
1. User scan SKU có quản lý UID group, chọn scan RFID mapping (R011).
2. **Case 1 — RFID chưa tồn tại:** flow giống khai báo UID group mới. User nhập SL, submit → hệ thống gen UID group mới + mapping RFID (R012).
3. **Case 2 — RFID/UID group đã tồn tại (Transfer company):** hệ thống suggest SL của UID group; user có thể edit. Submit → hệ thống gen UID group mới + mapping RFID (R013).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — Skip UID group:** user nhập `Số lượng` mà không scan `Nhóm UID` → flow nhận theo số lượng (R003).
- **A2 — Chuyển RFID mapping:** thay vì scan UID group, scan RFID mapping (R005, R011).
- **A3 — SKU có lô + HSD:** form thêm input số lô + HSD (R009).
- **A4 — Transfer company (RFID đã out):** suggest SL, cho edit (R013).

### Luồng ngoại lệ (Exception Paths)
- **E1 — UID group không có status `New`:** hệ thống báo lỗi, không cho ghi nhận (R004 / ERR-FAB-001).
- **E2 — Cố scan thêm UID group sau khi đã nhận theo SL:** input `Nhóm UID` và `Số lượng` đã ẩn, không cho thêm record mới (R006).
- **E3 — Cố nhận cùng lúc cả 2 loại (UID Group + Số lượng) cho 1 SKU:** business rule chặn (R006).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Trigger flow Vải khai báo Group UID | rule | ✅ | SKU không quản lý theo UID + category ∈ {Thời trang BTP, Phụ liệu, NVL} + tên sản phẩm chứa "Vải" |
| `Nhóm UID` | string (scan barcode/RFID) | ❌ Optional | Nếu khai báo: phải có status `New`; nếu không khai báo: chuyển flow nhận theo số lượng |
| `Số lượng` (cây/tấm vải) | number (Kg hoặc Mét) | ✅ | Quy đổi ra SL khi nhận hàng; tổng SL = sum tất cả cây/tấm vải = tổng SL SKU cho PO |
| Mutex receive mode | rule | ✅ | 1 SKU chỉ nhận hoặc theo `RFID/UID Group` hoặc theo `Số lượng`, **không cùng lúc cả 2**. Sau khi chọn 1 mode → mode còn lại bị ẩn / không cho thêm mới |
| Số lô | string | ✅ (nếu SKU quản lý lô) | Bắt buộc khi SKU có quản lý số lô và hạn sử dụng |
| Hạn sử dụng (HSD) | date | ✅ (nếu SKU quản lý HSD) | Bắt buộc khi SKU có quản lý số lô và hạn sử dụng |
| Update 10-12-2025 — Case 1 RFID chưa tồn tại | rule | ✅ | Hệ thống tự gen 1 UID group mới + mapping với RFID khi user submit |
| Update 10-12-2025 — Case 2 RFID đã tồn tại (Transfer company) | rule | ✅ | Hệ thống suggest SL của UID group + cho user edit; submit → gen UID group mới + mapping RFID |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-FAB-001 | Validation | UID group scan vào không có status `New` | (raw không có verbatim — Q-001) | (raw không có verbatim — Q-001) | 07062#L1696-L1697 |
| ERR-FAB-002 | Business rule | User cố nhận cùng lúc 2 loại (UID Group + Số lượng) cho 1 SKU | (raw không có verbatim — Q-002) | (raw không có verbatim — Q-002) | 07062#L1699-L1701 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Trigger flow Vải khai báo Group UID**
  - **Given:** SKU thuộc category `Thời trang (NVL)`, tên có "Vải", không quản lý theo UID.
  - **When:** User scan SKU trong flow Receiving PO.
  - **Then:** Hệ thống mở form scan nhận Vải khai báo Group UID (R001, R002).
- **AC-02 — SKU không trong scope thì không mở form Vải**
  - **Given:** SKU thuộc category `Mỹ phẩm`, tên không chứa "Vải".
  - **When:** User scan SKU.
  - **Then:** Hệ thống mở form scan nhận thường (không phải form Vải) (R001).
- **AC-03 — Nhóm UID không bắt buộc**
  - **Given:** Form scan nhận Vải mở, SKU không quản lý lô/HSD.
  - **When:** User bỏ trống `Nhóm UID`, nhập `Số lượng = 5 Kg`, click `Xác nhận`.
  - **Then:** Record được ghi vào danh sách như SKU nhận theo SL bình thường (R003, R008).
- **AC-04 — UID group status New valid**
  - **Given:** Form mở; nhóm UID `UID-001` có status `New`.
  - **When:** User scan `UID-001`, nhập `Số lượng = 10 Mét`, click `Xác nhận`.
  - **Then:** Record được ghi vào danh sách (R003, R004, R008).
- **AC-05 — UID group status không phải New**
  - **Given:** Nhóm UID `UID-002` đang ở status `Received` (không phải `New`).
  - **When:** User scan `UID-002`.
  - **Then:** Hệ thống báo lỗi (ERR-FAB-001), không cho ghi nhận (R004).
- **AC-06 — Số lượng tổng cộng = sum tất cả cây/tấm vải**
  - **Given:** PO cần SKU `Vải-X` tổng SL = 100 Mét.
  - **When:** User scan cây 1 (40 Mét), cây 2 (35 Mét), cây 3 (25 Mét).
  - **Then:** Tổng SL nhận = 40 + 35 + 25 = 100 Mét, khớp tổng SL SKU cho PO (R007).
- **AC-07 — Mutex receive mode (chọn SL trước → khoá UID/RFID)**
  - **Given:** Form mở. User nhập `Số lượng = 5 Kg`, click `+` để thêm vào danh sách (không khai báo Nhóm UID).
  - **When:** User cố scan thêm `Nhóm UID` cho SKU này.
  - **Then:** Input `Nhóm UID` và `Số lượng` đã ẩn đi, không cho thêm record mới (R006).
- **AC-08 — Switch sang RFID mapping (Update 10-11-2025)**
  - **Given:** Form mở, SKU không quản lý lô/HSD.
  - **When:** User chọn chuyển sang scan RFID mapping thay vì UID group.
  - **Then:** Hệ thống chấp nhận, user scan RFID, nhập SL → record ghi vào danh sách (R005, R008).
- **AC-09 — SKU có quản lý số lô + HSD**
  - **Given:** SKU `Vải-Y` có quản lý số lô và HSD.
  - **When:** User scan SKU → form mở.
  - **Then:** Form bao gồm input `Nhóm UID`, `Số lượng`, **số lô** và **HSD**; user cập nhật đủ rồi `Xác nhận` (R009).
- **AC-10 — Case 1 Update 10-12-2025: RFID chưa tồn tại**
  - **Given:** SKU `Vải-Z` quản lý UID group. User chọn scan RFID mapping.
  - **When:** User scan RFID `RFID-NEW-001` (chưa tồn tại trên hệ thống), nhập SL, submit.
  - **Then:** Hệ thống gen 1 UID group mới và mapping với `RFID-NEW-001` (R011, R012).
- **AC-11 — Case 2 Update 10-12-2025: RFID đã tồn tại (Transfer company)**
  - **Given:** SKU `Vải-Z`. RFID `RFID-OLD-002` đã tồn tại từ luồng Transfer company (đã `out` ở công ty xuất).
  - **When:** User scan `RFID-OLD-002`.
  - **Then:** Hệ thống suggest SL của UID group cũ; user có thể edit SL; submit → gen UID group mới + mapping với `RFID-OLD-002` (R013).
- **AC-12 — Update 10-12-2025 không áp dụng cho SKU không quản lý UID group**
  - **Given:** SKU `Vải-NoUID` (không quản lý UID group).
  - **When:** User cố scan RFID mapping theo flow Update 10-12-2025.
  - **Then:** Flow Update 10-12-2025 không apply — chỉ apply Update 10-11-2025 (scan RFID thay UID group cho SKU không quản lý UID, không tự gen mới) (R011, Q-003).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R004, ERR-FAB-001, AC-05 | Verbatim VN+EN cho message lỗi khi UID group scan vào không có status `New`. | PO/UX | Open | | | |
| Q-002 | R006, ERR-FAB-002, AC-07 | Verbatim VN+EN cho message khi user cố nhận cùng lúc 2 loại (UID Group + Số lượng) cho 1 SKU. Hệ thống có hiện message hay chỉ ẩn UI ngầm? | PO/UX | Open | | | |
| Q-003 | R005, R011 | Phân biệt rõ Update 10-11-2025 (scan RFID thay cho `Nhóm UID` cho SKU **không quản lý UID**) vs Update 10-12-2025 (scan RFID cho SKU **có quản lý UID group**, tự gen UID mới) — đúng diễn giải? Hay là cùng 1 flow chỉ là cập nhật mới? | PO | Open | | | |
| Q-004 | R007 | Quy đổi `Kg → SL` và `Mét → SL` dùng công thức gì? Per SKU có conversion factor riêng hay hệ thống lấy từ master data SKU? Verbatim formula? | PO/Dev | Open | | | |
| Q-005 | R010 | S-32 ("Update màn hình chi tiết sản phẩm của các sản phẩm đã nhận đủ số lượng") raw chỉ có heading, không có content. Update này thay đổi gì cụ thể trên màn hình chi tiết? Verbatim. | PO | Open | | | |
| Q-006 | R013 | "Transfer company" — định nghĩa cụ thể flow Transfer company là gì? Khi nào RFID/UID group "đã out ra" ở công ty xuất? Source raw không nêu chi tiết — có doc Transfer riêng không? | PO | Open | | | |
| Q-007 | R013 | Khi hệ thống suggest SL của UID group cũ và user edit khác đi, SL final ghi nhận theo SL user edit hay theo SL suggest? Có validation min/max so với SL suggest không? | PO | Open | | | |
| Q-008 | R002, R009 | Khi nào hệ thống phân biệt SKU "có/không quản lý số lô + HSD"? Là flag trên master SKU (`is_lot_managed`, `is_expiry_managed`) hay rule khác? | PO/Dev | Open | | | |
| Q-009 | R001 | Tên sản phẩm có "Vải" — match exact substring (case-sensitive) hay normalize (lowercase, không dấu)? Vd "vải", "VẢI", "Vai" có trigger flow không? | PO/Dev | Open | | | |
| Q-010 | R012, R013 | Sau khi gen UID group mới + mapping RFID, UID group mới có status gì (`New`?)? Có thể dùng lại UID group này cho lần nhận sau không? | PO/Dev | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-31, S-32, S-33 | 2.17 (stub) | 2.17 | All R + AC | Draft |
| CHG-002 | Update | Update 10-11-2025: cho phép chuyển scan `Nhóm UID` sang scan RFID mapping cho SKU không quản lý UID | (trước 2.17) | 2.17 | R005, AC-08 | Done (đã trong raw v2.17) |
| CHG-003 | Update | Update 10-12-2025: bổ sung flow scan RFID mapping cho SKU **có quản lý UID group** với 2 case (RFID chưa tồn tại / đã tồn tại Transfer company) | (trước 2.17) | 2.17 | R011-R013, AC-10, AC-11 | Done (đã trong raw v2.17) |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_fabric | test_stub_receiving_po_fabric | Add (chờ Gate 1B) | [[stub_receiving_po_app]] (flow scan nhận App), [[stub_receiving_po_vas]] (UID group khác feature), [[stub_receiving_po_packing_list]] (case nhận PO Vải) | Q-001..Q-010 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R013, AC-01..AC-12 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-010 |

## 🚧 Blocked Coverage

- R004, ERR-FAB-001, AC-05 — chờ Q-001 (verbatim message lỗi UID group status)
- R006, ERR-FAB-002, AC-07 — chờ Q-002 (verbatim message + behavior mutex mode)
- R005 vs R011 — chờ Q-003 (phân biệt 2 Update RFID mapping)
- R007 — chờ Q-004 (formula quy đổi Kg/Mét → SL)
- R010 — chờ Q-005 (verbatim Update S-32)
- R013 — chờ Q-006, Q-007 (định nghĩa Transfer company + rules edit SL suggest)
- R002, R009 — chờ Q-008 (flag lô/HSD trên SKU)
- R001 — chờ Q-009 (match rule tên sản phẩm "Vải")
- R012, R013 — chờ Q-010 (status UID group mới gen)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 18:00:00 | v1.1 | Refine stub → full spec: 13 R-ID, 12 AC, 8 BR, 2 messages (verbatim missing — Q-001, Q-002), 10 questions Open. `partial_read: false`. | refine-batch-3-2026-05-30 |
