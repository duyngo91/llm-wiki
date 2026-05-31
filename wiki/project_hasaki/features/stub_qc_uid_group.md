---
aliases: [stub_qc_uid_group]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_qc_uid_group
project: project_hasaki
source_version: 1.5
source_doc: 07105_Quality_Control_Docs_ver1.5.md
source_range: 07105#L1084-L1172
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-31 18:36:07"
verification_status: Verified
approved_by:
approved_at:
approval_note: "FIX-001: xóa inferred 'thấp nhất' khỏi BR + Q-006 trace; FIX-002: thêm Q-016 typo L141 + R002 ⚠️"
last_verified_source_version: 1.5

---

# REQ: stub_qc_uid_group

## Tổng quan
- **Mã tính năng:** stub_qc_uid_group
- **Feature:** UID group — Tiêu chí `QC xã vải`, Khai báo SL cần đánh giá (App), Chụp hình tem QC, Lưu ý transfer location
- **Mô tả ngắn:** Hỗ trợ luồng đánh giá Xã vải (Fabric Relaxing) trên UID group. Khi tạo/cập nhật tiêu chí bổ sung thông tin `QC xã vải`. Khi transfer UID group vào location `F0-XV` (hoặc type `Xã vải`) bằng transfer location/UID group → hệ thống tự sinh yêu cầu đánh giá xã vải cho các tiêu chí có bật `QC xã vải`. App có bước khai báo SL cần đánh giá cho UID group (bắt buộc, số nguyên dương, hệ thống trừ SL khỏi UID group) + chụp hình tem QC Pass/Fail (bắt buộc 1 hình). Lưu ý quan trọng: tiêu chí PO chính map tiêu chí PO sample (BOD approve case).
- **Source chính:** 07105_Quality_Control_Docs_ver1.5.md (v1.5)
- **Đối tượng sử dụng (Actors):** QC team, kho, BOD (approve case PO sample).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** [[ts_qc_uid_group]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_qc_criteria_setup]] (thiết lập tiêu chí + QC xã vải), [[stub_qc_criteria_sku]] (tiêu chí SKU). ↔️ liên quan [[stub_qc_evaluation_result]] (field `Đánh giá đạt`, tổng hợp kết quả), [[stub_qc_evaluation_mobile]] (App flow đánh giá), [[stub_receiving_po_fabric]] (UID group cho SKU vải).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07105_Quality_Control_Docs_ver1.5.md | 1.5 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Raw không mô tả API explicit | N/A |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Khi tạo mới hoặc cập nhật tiêu chí, hệ thống bổ sung thông tin `QC xã vải` (Fabric relaxation QC) | UI + Functional | High | ✅ | 07105#L1083-L1085 |
| R002 | Thông tin `QC xã vải` được dùng để **tạo yêu cầu đánh giá xã vải** cho UID group khi transfer vào location `F0-XV` (hoặc type location `Xã vải / Fabric Relaxing`) bằng tính năng `transfer location` hoặc `transfer UID group` → hệ thống **tự động sinh ra 1 yêu cầu đánh giá Xã vải** cho các tiêu chí có bật `QC xã vải` cho SKU | Business rule + Functional | High | ✅ | 07105#L1086-L1093 |
| R003 | Phạm vi sinh yêu cầu đánh giá xã vải — chỉ sinh cho các tiêu chí có bật `QC xã vải`. Ví dụ: SKU thiết lập 5 tiêu chí nhưng chỉ 2 tiêu chí bật `QC xã vải` → chỉ sinh yêu cầu đánh giá cho 2 tiêu chí này | Business rule | High | ✅ | 07105#L1090-L1093 |
| R004 | Lưu ý nhận hàng Vải: số vải còn lại (90%) được nhận sau khi nhận 10% và đánh giá Đạt **đều phải được đánh giá qua khâu Xã vải** trước khi đưa vào sản xuất | Business rule | High | ✅ | 07105#L1094-L1096 |
| R005 | App — `Menu: App / Purchase order / Quality control`. Ở bước scan UID group cần đánh giá, bổ sung thông tin `Khai báo số lượng cần đánh giá` cho UID group | UI + Functional | High | ✅ | 07105#L1128-L1132 |
| R006 | Validation `Số lượng cần đánh giá` (App): **bắt buộc**, phải là **số nguyên dương** | Validation | High | ✅ | 07105#L1133-L1134 |
| R007 | Sau khi user `Xác nhận` SL cần đánh giá, hệ thống **tự động trừ SL đã khai báo ra khỏi UID group**. Ví dụ: UID group có SKU A qty 9500, user khai báo SL cần đánh giá = 500 → qty của SKU A trong UID group còn 9000 | Business rule + Functional | High | ✅ | 07105#L1135-L1139 |
| R008 | Thông tin `Số lượng cần đánh giá` được bổ sung vào **phần thông tin chung** của UID group | UI | High | ✅ | 07105#L1140 |
| R009 | App — Chụp hình tem QC. `Menu: App / Purchase order / Quality control`. Sau khi hoàn thành đánh giá tất cả tiêu chí cho SKU, khi user nhấn `Hoàn thành` → hệ thống bổ sung bước **chụp hình tem QC Pass/Fail** để ghi nhận lên hệ thống | Functional + UI | High | ✅ | 07105#L1141-L1145 |
| R010 | Validation chụp hình tem QC: **bắt buộc**, chỉ cần chụp **1 hình** | Validation | High | ✅ | 07105#L1146-L1147 |
| R011 | Lưu ý — Khi transfer UID group qua location xã vải (`F0-XV`) hoặc type location là `Xã vải (Fabric Relaxing)` bằng tính năng `transfer bin`, `transfer bin cart`, `transfer vị trí trong UID group` → **validate**: nếu UID group đã sinh yêu cầu và được đánh giá xã vải `Đạt` → **bỏ qua**; nếu chưa được sinh yêu cầu → **sinh yêu cầu đánh giá** theo tiêu chí xã vải | Business rule + State transition | High | ✅ | 07105#L1153-L1158 |
| R012 | Tiêu chí đánh giá trên SKU của **PO chính phải map với tiêu chí của SKU khi đánh giá trên PO sample**. Khi SKU PO sample chỉ đạt 4/5 tiêu chí được thiết lập nhưng BOD vẫn duyệt cho nhận hàng vào theo Lot này để sản xuất → tiêu chí đánh giá cho SKU của PO chính cũng phải **dựa vào điều kiện của tiêu chí của SKU trên PO sample** | Business rule | High | ✅ | 07105#L1160-L1165 |
| R013 | Ví dụ rule R012 — điều kiện đạt của tiêu chí A của SKU thiết lập là `>6`, PO sample đánh giá chỉ 5.5 (Không đạt) nhưng BOD approve cho nhận Lot này → trên PO chính SKU này chỉ cần đạt từ **5.5** là Đạt yêu cầu (mức điều kiện điều chỉnh theo Lot sample đã được BOD duyệt) | Business rule | High | ✅ | 07105#L1166-L1168 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User có quyền QC trên App + Web.
- Có ít nhất 1 UID group được khai báo cho SKU vải / SKU thuộc category Thời trang (NVL).
- Tiêu chí đánh giá cho SKU đã được thiết lập và có ít nhất 1 tiêu chí bật `QC xã vải`.

### Luồng chuẩn (Happy Path) — Setup tiêu chí QC xã vải
1. QC vào trang thiết lập tiêu chí (xem [[stub_qc_criteria_setup]]).
2. Khi tạo mới hoặc cập nhật, user check checkbox `QC xã vải` cho các tiêu chí cần đánh giá xã vải (R001).
3. Lưu tiêu chí — tiêu chí có flag `QC xã vải = true`.

### Luồng chuẩn (Happy Path) — Auto sinh yêu cầu đánh giá xã vải khi transfer F0-XV
1. UID group X đang ở location khác (vd `F0-VAS`).
2. User transfer UID group X vào location `F0-XV` bằng `transfer location` hoặc `transfer UID group`.
3. Validate (R011):
   - Nếu UID group X đã có yêu cầu xã vải và đã Đạt → bỏ qua.
   - Nếu chưa có yêu cầu → hệ thống tự sinh yêu cầu đánh giá xã vải cho các tiêu chí có bật `QC xã vải` (R002, R003).
4. SKU thiết lập 5 tiêu chí nhưng chỉ 2 tiêu chí bật `QC xã vải` → yêu cầu chỉ chứa 2 tiêu chí này (R003).

### Luồng chuẩn (Happy Path) — Đánh giá UID group trên App
1. QC mở `App / Purchase order / Quality control`.
2. Scan UID group cần đánh giá (R005).
3. Khai báo `Số lượng cần đánh giá` (bắt buộc, số nguyên dương) (R005, R006).
4. Click `Xác nhận` → hệ thống trừ SL khai báo khỏi UID group (R007). Ví dụ: UID group 9500 → khai báo 500 → còn 9000.
5. Thông tin SL cần đánh giá bổ sung vào phần thông tin chung của UID group (R008).
6. QC tiến hành đánh giá từng tiêu chí (xem [[stub_qc_evaluation_mobile]]).
7. Sau khi đánh giá xong tất cả tiêu chí cho SKU, user nhấn `Hoàn thành`.
8. Hệ thống yêu cầu user chụp hình tem QC Pass/Fail (bắt buộc 1 hình) (R009, R010).
9. User chụp hình → ghi nhận lên hệ thống.

### Luồng chuẩn (Happy Path) — Tiêu chí PO chính theo PO sample (BOD approve)
1. PO sample của SKU A đánh giá đạt 4/5 tiêu chí. Tiêu chí A có điều kiện thiết lập `>6`, PO sample đạt 5.5 (không đạt theo điều kiện thiết lập).
2. BOD approve cho nhận Lot này vào sản xuất.
3. Khi PO chính của SKU A được nhận hàng và đánh giá:
   - Tiêu chí A trên PO chính dùng điều kiện điều chỉnh: SKU đạt 5.5 là `Đạt yêu cầu` (R012, R013).
4. Các tiêu chí khác giữ điều kiện thiết lập gốc.

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — Transfer bin / transfer bin cart / transfer vị trí UID group:** cùng validate rule (R011).
- **A2 — UID group đã Đạt xã vải:** transfer vào F0-XV → bỏ qua sinh yêu cầu (R011).
- **A3 — SKU có 100% tiêu chí bật `QC xã vải`:** yêu cầu sinh chứa toàn bộ tiêu chí (R003).
- **A4 — SKU không có tiêu chí nào bật `QC xã vải`:** transfer vào F0-XV → không sinh yêu cầu (R002 implicit).

### Luồng ngoại lệ (Exception Paths)
- **E1 — `Số lượng cần đánh giá` để trống hoặc 0:** validation block, không cho `Xác nhận` (R006 / ERR-UIG-001).
- **E2 — `Số lượng cần đánh giá` không phải số nguyên dương (vd 0.5, -10):** validation block (R006 / ERR-UIG-001).
- **E3 — `Số lượng cần đánh giá` > qty của SKU trong UID group:** hệ thống chặn (raw không nêu rõ — Q-001).
- **E4 — User skip bước chụp hình tem QC:** không cho `Hoàn thành` đánh giá (R010 / ERR-UIG-002).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Tiêu chí `QC xã vải` flag | boolean | ✅ (khi setup) | Bổ sung khi tạo mới hoặc cập nhật tiêu chí; per tiêu chí (không per SKU) |
| Trigger sinh yêu cầu đánh giá xã vải | rule | ✅ | UID group transfer vào location = `F0-XV` hoặc type = `Xã vải / Fabric Relaxing` qua các tính năng: transfer location / transfer UID group / transfer bin / transfer bin cart / transfer vị trí UID group |
| Validation transfer F0-XV | rule | ✅ | Đã đánh giá xã vải Đạt → bỏ qua; chưa có yêu cầu → sinh yêu cầu |
| Phạm vi yêu cầu đánh giá xã vải | rule | ✅ | Chỉ sinh cho các tiêu chí có flag `QC xã vải = true` |
| Số vải còn lại 90% | rule | ✅ | Phải đánh giá xã vải trước khi đưa vào sản xuất |
| `Số lượng cần đánh giá` (App) | integer | ✅ | Bắt buộc; số nguyên dương; sau Xác nhận hệ thống auto trừ SL khỏi UID group |
| Vị trí hiển thị SL cần đánh giá | UI rule | ✅ | Phần thông tin chung của UID group |
| Hình tem QC Pass/Fail | image | ✅ | Bắt buộc; chỉ chụp 1 hình; sau khi hoàn thành đánh giá tất cả tiêu chí; nhấn `Hoàn thành` trigger bước chụp |
| Tiêu chí PO chính map PO sample | rule | ✅ | Khi BOD approve PO sample không đạt 100% tiêu chí thiết lập → điều kiện đạt tiêu chí trên PO chính **dựa vào điều kiện của tiêu chí của SKU trên PO sample** (cách tổng hợp khi nhiều Lot sample khác nhau chưa rõ — Q-006) |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-UIG-001 | Validation | `Số lượng cần đánh giá` không hợp lệ (rỗng / 0 / số âm / không phải số nguyên) | (raw không có verbatim — Q-002) | (raw không có verbatim — Q-002) | 07105#L1133-L1134 |
| ERR-UIG-002 | Validation | User cố `Hoàn thành` mà chưa chụp hình tem QC | (raw không có verbatim — Q-002) | (raw không có verbatim — Q-002) | 07105#L1146-L1147 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Setup tiêu chí có flag QC xã vải**
  - **Given:** QC tạo mới tiêu chí.
  - **When:** User check `QC xã vải = true` và lưu.
  - **Then:** Tiêu chí được lưu với flag `QC xã vải = true` (R001).
- **AC-02 — Auto sinh yêu cầu đánh giá xã vải khi transfer F0-XV**
  - **Given:** UID group X có SKU A thiết lập 5 tiêu chí, 2 tiêu chí bật `QC xã vải`. UID group chưa có yêu cầu xã vải.
  - **When:** User transfer UID group X vào `F0-XV` qua `transfer location`.
  - **Then:** Hệ thống tự sinh 1 yêu cầu đánh giá xã vải chỉ chứa 2 tiêu chí có `QC xã vải = true` (R002, R003).
- **AC-03 — Bỏ qua nếu UID group đã Đạt xã vải**
  - **Given:** UID group X đã có yêu cầu xã vải và kết quả `Đạt`.
  - **When:** User transfer X vào F0-XV lần 2.
  - **Then:** Hệ thống bỏ qua, không sinh yêu cầu mới (R011).
- **AC-04 — Transfer bin/bin cart cũng trigger validate**
  - **Given:** UID group Y chưa có yêu cầu xã vải.
  - **When:** User dùng `transfer bin cart` đưa Y vào location type `Xã vải`.
  - **Then:** Hệ thống sinh yêu cầu đánh giá xã vải (R011).
- **AC-05 — Khai báo SL cần đánh giá UID group App**
  - **Given:** User mở App / Purchase order / Quality control, scan UID group có SKU A qty 9500.
  - **When:** User nhập `Số lượng cần đánh giá = 500`, click `Xác nhận`.
  - **Then:** SL được lưu; qty SKU A trong UID group còn 9000 (R005, R006, R007).
- **AC-06 — SL cần đánh giá phải nguyên dương (rỗng)**
  - **Given:** Form khai báo SL mở.
  - **When:** User bỏ trống và click `Xác nhận`.
  - **Then:** Block, hiện ERR-UIG-001 (R006).
- **AC-07 — SL cần đánh giá là 0**
  - **Given:** Form mở.
  - **When:** User nhập `0`, click `Xác nhận`.
  - **Then:** Block, hiện ERR-UIG-001 (R006).
- **AC-08 — SL cần đánh giá là số thập phân**
  - **Given:** Form mở.
  - **When:** User nhập `0.5`, click `Xác nhận`.
  - **Then:** Block, hiện ERR-UIG-001 (R006).
- **AC-09 — SL cần đánh giá là số âm**
  - **Given:** Form mở.
  - **When:** User nhập `-10`, click `Xác nhận`.
  - **Then:** Block, hiện ERR-UIG-001 (R006).
- **AC-10 — Hiển thị SL cần đánh giá ở phần thông tin chung**
  - **Given:** UID group đã khai báo SL = 500.
  - **When:** User xem UID group trong phần thông tin chung.
  - **Then:** Field `Số lượng cần đánh giá = 500` hiển thị (R008).
- **AC-11 — Chụp hình tem QC sau Hoàn thành**
  - **Given:** QC đã đánh giá xong tất cả tiêu chí của SKU.
  - **When:** User nhấn `Hoàn thành`.
  - **Then:** Hệ thống mở bước chụp hình tem QC Pass/Fail (R009).
- **AC-12 — Chụp đúng 1 hình tem QC**
  - **Given:** Bước chụp hình mở.
  - **When:** User chụp 1 hình + click `Lưu`.
  - **Then:** Hình tem QC được ghi nhận, hoàn thành đánh giá (R009, R010).
- **AC-13 — Skip chụp hình tem QC**
  - **Given:** Bước chụp hình mở.
  - **When:** User cố thoát mà chưa chụp.
  - **Then:** Block, hiện ERR-UIG-002 (R010).
- **AC-14 — Tiêu chí PO chính dùng điều kiện PO sample BOD approve**
  - **Given:** PO sample SKU A có tiêu chí A thiết lập `>6`, đánh giá PO sample đạt 5.5 (không đạt theo thiết lập gốc). BOD approve Lot.
  - **When:** PO chính SKU A nhận hàng, đánh giá tiêu chí A.
  - **Then:** Điều kiện đạt tiêu chí A trên PO chính dùng `≥5.5`; SKU đạt từ 5.5 trở lên là Đạt yêu cầu (R012, R013).
- **AC-15 — Số vải 90% còn lại phải qua xã vải trước sản xuất**
  - **Given:** PO sample SKU vải đánh giá Đạt → nhận 10%. Số 90% còn lại nhận sau.
  - **When:** 90% còn lại nhận vào kho.
  - **Then:** Phải sinh yêu cầu đánh giá xã vải và Đạt trước khi đưa vào sản xuất (R004).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R007 | Khi `Số lượng cần đánh giá > qty SKU trong UID group` — hệ thống có chặn không? Verbatim message? | PO/Dev | Open | | | |
| Q-002 | ERR-UIG-001, ERR-UIG-002 | Verbatim VN+EN cho 2 message (SL cần đánh giá không hợp lệ + bắt buộc chụp hình tem QC). | PO/UX | Open | | | |
| Q-003 | R002, R011 | Phân biệt `transfer location` vs `transfer bin` vs `transfer bin cart` vs `transfer vị trí trong UID group` — 4 tính năng riêng biệt hay alias cùng 1 flow? | PO | Open | | | |
| Q-004 | R002, R011 | Khi UID group có nhiều SKU, sinh yêu cầu xã vải là 1 yêu cầu / SKU hay 1 yêu cầu / UID group? | PO | Open | | | |
| Q-005 | R009 | Hình tem QC Pass/Fail — có 2 loại tem riêng (Pass/Fail) hay 1 tem có 2 trạng thái? User chụp hình tem nào tuỳ kết quả đánh giá? | PO/UX | Open | | | |
| Q-006 | R013 | Khi BOD approve nhiều Lot PO sample với điều kiện khác nhau cho cùng SKU → PO chính dùng điều kiện Lot nào? Hay tổng hợp min/max? | PO | Open | | | |
| Q-007 | R012, R013 | Sau khi PO chính theo điều kiện PO sample đã hoàn thành, các PO sau đó của SKU cùng pattern có dùng điều kiện cũ không, hay reset về thiết lập gốc? | PO | Open | | | |
| Q-008 | R007 | Khi user đánh giá xong và submit kết quả, SL đã trừ có được hoàn lại UID group không (rollback) nếu kết quả không hợp lệ? | PO/Dev | Open | | | |
| Q-009 | R001 | "Bổ sung khi tạo mới hay cập nhật tiêu chí" — field `QC xã vải` áp dụng cho tất cả tiêu chí mới/cập nhật, hay chỉ tiêu chí thuộc category Thời trang (NVL)? | PO | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-24, S-26, S-27, S-28 | 1.5 (stub) | 1.5 | All R + AC | Draft |
| CHG-002 | Add | Bổ sung field `QC xã vải` cho tiêu chí thiết lập + flow auto sinh yêu cầu đánh giá xã vải khi transfer F0-XV | (trước 1.5) | 1.5 | R001, R002, R003, R011, AC-01, AC-02, AC-04 | Done (đã trong raw v1.5) |
| CHG-003 | Add | App — Khai báo SL cần đánh giá + Chụp hình tem QC Pass/Fail | (trước 1.5) | 1.5 | R005-R010, AC-05..AC-13 | Done (đã trong raw v1.5) |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_qc_uid_group | test_stub_qc_uid_group | Add (chờ Gate 1B) | [[stub_qc_criteria_setup]] (flag QC xã vải khi setup), [[stub_qc_evaluation_mobile]] (App flow đánh giá), [[stub_qc_evaluation_result]] (field Đánh giá đạt), [[stub_receiving_po_fabric]] (UID group cho SKU vải), [[stub_receiving_po_po_sample]] (PO sample BOD approve) | Q-001..Q-009 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R013, AC-01..AC-15 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-009 |

## 🚧 Blocked Coverage

- R007 — chờ Q-001, Q-008 (rules SL > qty + rollback)
- ERR-UIG-001, ERR-UIG-002 — chờ Q-002 (verbatim message)
- R002, R011 — chờ Q-003, Q-004 (phân biệt transfer + scope sinh yêu cầu)
- R009 — chờ Q-005 (tem Pass vs Fail)
- R013 — chờ Q-006, Q-007 (nhiều Lot BOD approve + carryover)
- R001 — chờ Q-009 (scope flag QC xã vải)
- R012, R013, BR "Tiêu chí PO chính" — chờ Q-006 (cách tổng hợp điều kiện khi nhiều Lot sample BOD approve khác nhau)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 18:30:00 | v1.1 | Refine stub → full spec: 13 R-ID, 15 AC, 9 BR, 2 messages (verbatim missing — Q-002), 9 questions Open. `partial_read: false`. | refine-batch-3-2026-05-30 |
| 2026-05-31 17:30:00 | v1.2 | FIX-001 (refiner batch-4): xóa "thấp nhất" INFERRED khỏi BR "Tiêu chí PO chính map PO sample"; giữ verbatim raw "dựa vào điều kiện của tiêu chí của SKU trên PO sample"; thêm Q-006 trace + Blocked Coverage. | refiner-spec-scoped-batch-4 |
