---
aliases: [stub_qc_evaluation_mobile]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_qc_evaluation_mobile
project: project_hasaki
source_version: 1.5
source_doc: 07105_Quality_Control_Docs_ver1.5.md
source_range: 07105#L790-L1021
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-31 17:50:34"
verification_status: Verified
approved_by:
approved_at:
approval_note:
last_verified_source_version: 1.5

---

# REQ: stub_qc_evaluation_mobile

## Tổng quan
- **Mã tính năng:** stub_qc_evaluation_mobile
- **Feature:** Đánh giá chất lượng sản phẩm trên Mobile (general + Update 18-09-2025 cho vải)
- **Mô tả ngắn:** App bổ sung tính năng `Quality Control` cho user đánh giá CL sản phẩm theo VAS đã được tạo. General flow (Step 1-4): chọn kho → chọn VAS → đánh giá từng sản phẩm theo tiêu chí thiết lập cho SKU → ghi nhận kết quả. Update 18-09-2025 cho vải bổ sung scan UID group + 3 tiêu chí đặc thù (`Lỗi 4 điểm` 19 enum, `Độ co rút` step-by-step, `Độ đồng màu` step-by-step), kết quả tính theo công thức + ngưỡng config.
- **Source chính:** 07105_Quality_Control_Docs_ver1.5.md (v1.5)
- **Đối tượng sử dụng (Actors):** QC user trên App.
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** [[ts_qc_evaluation_mobile]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_qc_criteria_sku]] (tiêu chí thiết lập cho SKU), [[stub_qc_vas]] (VAS source). ➡️ feed [[stub_qc_evaluation_result]] (kết quả lưu trữ).

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
| R001 | App bổ sung tính năng `Quality Control` truy cập qua menu `Pruchase Order / Quality Control` | UI | High | ✅ | 07105#L790-L795 |
| R002 | Step 1: User chọn kho → hiển thị các VAS type `Quality Control` có status `Open` hoặc `In-Progress` | Functional | High | ✅ | 07105#L797-L799 |
| R003 | Step 1: hỗ trợ tìm kiếm theo mã PO và VAS | Functional | High | ✅ | 07105#L800 |
| R004 | Step 2: chọn VAS → hiển thị header: Shop, VAS, Tổng SKU, Mã PO, Tổng sản phẩm | UI | High | ✅ | 07105#L803-L808 |
| R005 | Step 2: search sản phẩm trong VAS theo SKU, Barcode hoặc tên sản phẩm (tìm gần đúng) | Functional | High | ✅ | 07105#L809-L810 |
| R006 | Step 2: danh sách sản phẩm hiển thị: Tên sản phẩm, SKU – Barcode, Số lượng sản phẩm | UI | High | ✅ | 07105#L811-L815 |
| R007 | Step 2: color coding sản phẩm — `Xám nhạt` (chưa đánh giá), `Xanh dương nhạt` (đang đánh giá chưa hoàn thành), `Xanh lá nhạt` (đã đánh giá). Cho vải (S-20) bổ sung `Cam nhạt` = đã đánh giá Không Đạt | UI | High | ✅ | 07105#L816-L820, 07105#L893-L900 |
| R008 | Step 3 (general): click sản phẩm → hiển thị Sản phẩm (SKU–Tên), PO, Số lượng, Nhà cung cấp (từ PO), Ghi chú (default trống, user edit được), Tổng tiêu chí đạt, Tổng tiêu chí không đạt | UI | High | ✅ | 07105#L824-L830 |
| R009 | Step 3 (general): danh sách tiêu chí lấy theo thiết lập cho SKU; mỗi tiêu chí hiển thị Thứ tự, Tên, Mô tả, Mô tả điều kiện theo SKU, Hình chụp mẫu, Đạt/Không đạt | UI | High | ✅ | 07105#L831-L840 |
| R010 | Step 3 (general): tiêu chí thiết lập "Theo điều kiện" cho phép user nhập kết quả > 0 → nhấn Enter hoặc tích xanh để hệ thống so sánh với điều kiện và xác định Đạt/Không đạt | Functional + Validation | High | ✅ | 07105#L841-L846 |
| R011 | Step 3 (general): user có thể edit lại kết quả đánh giá theo điều kiện và xác nhận lại | Functional | High | ✅ | 07105#L847-L853 |
| R012 | Step 3 (general): tiêu chí thiết lập yêu cầu chụp hình → user chụp. Tiêu chí Fail → bắt buộc chụp hình + nhập ghi chú; hỗ trợ chụp tối đa 5 hình / tiêu chí | Validation + Business rule | High | ✅ | 07105#L854-L861 |
| R013 | Step 3 (general): đánh giá hết tiêu chí → click `Hoàn thành` để xác nhận đánh giá xong cho sản phẩm | Functional | High | ✅ | 07105#L862-L863 |
| R014 | Step 4 (general): VAS có nhiều hơn 1 sản phẩm → cần đánh giá tất cả sản phẩm để hoàn thành VAS; click `Hoàn thành đánh giá` sau khi xong tất cả | Functional | High | ✅ | 07105#L865-L868 |
| R015 | Update 18-09-2025 — Step 2 (vải): danh sách sản phẩm bổ sung Số lô và Hạn sử dụng (so với general flow) | UI | High | ✅ | 07105#L888-L892 |
| R016 | Update 18-09-2025 — Step 2 (vải): do rules đánh giá 10% group UID, 1 lô cần đánh giá 3 cây vải → hiển thị 3 dòng UID group tương ứng | UI + Business rule | High | ✅ | 07105#L902-L904 |
| R017 | Update 18-09-2025 — Step 3 (vải): click sản phẩm → yêu cầu scan UID group tương ứng với cây vải cần đánh giá | Functional | High | ✅ | 07105#L909-L909 |
| R018 | Update 18-09-2025 — Step 3 (vải): UID group không tồn tại hoặc không thuộc PO/số lô được yêu cầu → hiển thị thông báo lỗi | Validation | High | ✅ | 07105#L910-L911 |
| R019 | Update 18-09-2025 — Step 3 (vải): hỗ trợ suggest các UID group đã nhận cho sản phẩm theo lô để user chọn nhanh | Functional | High | ✅ | 07105#L912-L913 |
| R020 | Update 18-09-2025 — Step 3 (vải): sau khi scan/chọn UID group hợp lệ → click `Xác nhận` để qua bước tiếp theo | Functional | High | ✅ | 07105#L914-L915 |
| R021 | Update 18-09-2025 — Step 4 (vải): phase này có 3 tiêu chí đánh giá; thông tin hiển thị cho mỗi tiêu chí gồm Tên (kèm hướng dẫn mở modal), Mô tả, Điều kiện (nếu có) | UI | High | ✅ | 07105#L918-L928 |
| R022 | Tiêu chí 1 — `Kiểm tra lỗi 4 điểm`: hiển thị 4 mức điểm — Lỗi 1 điểm (lỗi 0–3"), 2 điểm (3–6"), 3 điểm (6–9"), 4 điểm (>9") | Enum + Business rule | High | ✅ | 07105#L930-L934 |
| R023 | Lỗi 4 điểm — user click `+` thêm thông tin lỗi; chọn loại lỗi (bắt buộc) từ enum 19 values: `1.Slub (sợi thô cục)`, `2.Foreign yarn (sợi tạp,sợi màu)`, `3.Thin yarn, rough yarn (sợi rách,sợi thô)`, `4.Yarn knot (gút sợi)`, `5.Missing yarn (mất sợi)`, `6.Break yarn (đứt sợi)`, `7.Needle line (lỗi kim)`, `8.Dark line (sọc đậm màu)`, `9.Scratch (dập tuyết, trầy xước)`, `10.Staining (loang màu)`, `11.Fade of color (bạc màu)`, `12.Dyeing block (vết dơ trong nhuộm)`, `13.Color spot (chấm màu)`, `14.Dirty (dơ)`, `15.Hole (lỗi rách)`, `16.Printing erro (lỗi in)`, `17.Fold,crease (nếp nhăn)`, `18.Dead fold (nếp gấp chết)`, `19.Other (lỗi khác)` | Enum | High | ✅ | 07105#L935-L960 |
| R024 | Lỗi 4 điểm — nhập ghi chú (optional); chụp hình lỗi bắt buộc max 3 hình; click `Xác nhận` để ghi nhận lỗi | Functional + Validation | High | ✅ | 07105#L961-L966 |
| R025 | Lỗi 4 điểm — sau khi ghi nhận lỗi, tính: Số lỗi từng loại, Tổng điểm lỗi (chưa nhân hệ số), Tổng điểm lỗi đã nhân hệ số | Formula | High | ✅ | 07105#L967-L973 |
| R026 | Lỗi 4 điểm — icon xem thông tin lỗi đã cập nhật trước đó | UI | Medium | ✅ | 07105#L974 |
| R027 | Lỗi 4 điểm — click `Hoàn thành` → kết quả = Tổng điểm lỗi đã nhân hệ số → so sánh với điều kiện thiết lập của tiêu chí → xác định Đạt/Không đạt → ghi nhận vào kết quả bên ngoài | Formula + Business rule | High | ✅ | 07105#L975-L982 |
| R028 | Tiêu chí 2 — `Kiểm tra độ co rút` (thiết lập step-by-step): hiển thị thông tin từng bước theo thiết lập gồm Thứ tự bước + Tên bước (+ hình mẫu), Hướng dẫn, Yêu cầu chụp hình (theo thiết lập), Ghi nhận kết quả (Đạt/Không đạt hoặc nhập giá trị), Ghi chú | Functional | High | ✅ | 07105#L985-L1003 |
| R029 | Tiêu chí 2 — sau khi cập nhật bước → click `Tiếp theo`; bước cuối → click `Hoàn thành` → áp công thức thiết lập (nếu có) → tính kết quả → so sánh với điều kiện → Đạt/Không đạt | Functional + Formula | High | ✅ | 07105#L1005-L1012 |
| R030 | Tiêu chí 3 — `Kiểm tra độ đồng màu`: thực hiện tương tự `Kiểm tra độ co rút` (step-by-step + công thức) | Functional | High | ✅ | 07105#L1014-L1014 |
| R031 | Step 5 (vải) — sau khi đánh giá xong tất cả tiêu chí cho 1 UID group → click `Hoàn thành` → ghi nhận kết quả cuối cùng | Functional | High | ✅ | 07105#L1016-L1016 |
| R032 | Step 5 (vải) — nếu có ít nhất 1 tiêu chí Không Đạt → kết quả sản phẩm theo UID group được tính là **Không đạt** | Business rule | High | ✅ | 07105#L1017-L1018 |
| R033 | Step 5 (vải) — tiếp tục đánh giá cho các UID group còn lại cho tới khi hoàn thành | Functional | High | ✅ | 07105#L1019 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User đã login App với account QC được cấp.
- VAS type `Quality Control` đã được tạo cho phiên nhận (xem [[stub_qc_vas]]).
- Tiêu chí QC đã được thiết lập + approved cho SKU (xem [[stub_qc_criteria_sku]] + [[stub_qc_criteria_approval]]).

### Luồng chuẩn (Happy Path) — General (non-vải)
1. User mở App → menu `Pruchase Order / Quality Control` (R001).
2. Chọn kho → App show danh sách VAS type QC status `Open`/`In-Progress` (R002). Search PO/VAS (R003).
3. Click VAS → header hiển thị Shop, VAS, Tổng SKU, Mã PO, Tổng sản phẩm (R004); danh sách sản phẩm color-coded `Xám nhạt` (R005-R007).
4. Click sản phẩm → hiển thị thông tin và danh sách tiêu chí (R008, R009).
5. Per tiêu chí: chọn `Đạt`/`Không đạt` hoặc nhập giá trị (cho tiêu chí Theo điều kiện) → Enter/tích xanh (R010). User có thể edit (R011).
6. Chụp hình theo config; Fail bắt buộc chụp + ghi chú; max 5 hình (R012).
7. Đánh giá xong tất cả tiêu chí → click `Hoàn thành` (R013); sản phẩm chuyển sang `Xanh lá nhạt`.
8. VAS có nhiều sản phẩm → quay lại bước 4 cho sản phẩm tiếp; xong tất cả → `Hoàn thành đánh giá` (R014).

### Luồng chuẩn (Happy Path) — Vải (Update 18-09-2025)
1-3. Như general bước 1-3, nhưng Step 2 bổ sung Số lô + Hạn sử dụng (R015), color coding có thêm `Cam nhạt` (R007). Mỗi lô cần đánh giá 10% group UID → hiển thị nhiều dòng tương ứng (R016).
4. Click sản phẩm → App yêu cầu scan UID group (R017). Nếu invalid → thông báo lỗi (R018); App suggest UID đã nhận theo lô (R019). Click `Xác nhận` (R020).
5. App hiển thị 3 tiêu chí (R021):
   - **Tiêu chí 1 — Kiểm tra lỗi 4 điểm:** thêm lỗi qua `+`, chọn loại từ 19 enum (R023), nhập ghi chú, chụp ≤ 3 hình bắt buộc, `Xác nhận` (R024). Tổng tự động (R025). `Hoàn thành` → so sánh với điều kiện (R027).
   - **Tiêu chí 2 — Độ co rút (step-by-step):** từng bước theo thiết lập với chụp hình + kết quả (R028); `Tiếp theo` per bước; bước cuối `Hoàn thành` → áp công thức (R029).
   - **Tiêu chí 3 — Độ đồng màu:** giống Tiêu chí 2 (R030).
6. Step 5: click `Hoàn thành` → tổng kết kết quả cho UID group (R031). ≥ 1 tiêu chí Không Đạt → UID group Không Đạt (R032).
7. Tiếp tục các UID group còn lại (R033).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — Edit kết quả đánh giá:** user edit giá trị nhập → xác nhận lại → hệ thống tính lại Đạt/Không đạt (R011).
- **A2 — Tiêu chí Fail trong general flow:** bắt buộc chụp ảnh + ghi chú (R012).
- **A3 — Tiêu chí step-by-step:** đi qua từng bước, không skip; mỗi bước có config chụp hình riêng.

### Luồng ngoại lệ (Exception Paths)
- **E1 — UID group invalid (vải):** App hiển thị thông báo lỗi (R018 + ERR-QCM-001 nếu có verbatim).
- **E2 — User cố submit chưa đánh giá hết tiêu chí:** raw không mô tả block; assume `Hoàn thành` chỉ enable khi đủ — Q-010.

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Filter VAS theo status (Step 1) | rule | ✅ | Chỉ show `Open` hoặc `In-Progress` |
| Search PO/VAS/sản phẩm | rule | ❌ | "Tìm gần đúng" — semantics chưa rõ — Q-008 |
| Color coding sản phẩm | enum | ✅ | `Xám nhạt`/`Xanh dương nhạt`/`Xanh lá nhạt` (general); + `Cam nhạt` (vải) |
| Nhập kết quả (tiêu chí theo điều kiện) | numeric | ✅ | > 0 |
| Chụp hình (general — config OFF) | rule | ❌ | Optional theo config |
| Chụp hình (general — config ON) | rule | ✅ | Max 5 hình/tiêu chí; Fail bắt buộc chụp + ghi chú |
| Chụp hình (Lỗi 4 điểm — Update vải) | rule | ✅ | Bắt buộc, max 3 hình |
| Lỗi 4 điểm — phân loại lỗi | enum | ✅ | 19 values (R023) |
| Lỗi 4 điểm — formula | rule | ✅ | Tổng điểm đã nhân hệ số; hệ số / weight chưa rõ — Q-004 |
| 10% group UID cho vải | rule | ✅ | Đánh giá 10% số lượng cây vải của từng lô; công thức tính số dòng UID group (làm tròn lên/xuống/thường) chưa rõ — Q-012 |
| Kết quả UID group (vải) | rule | ✅ | ≥ 1 tiêu chí Không Đạt → UID group Không Đạt |
| Edit kết quả audit | rule | ⚠️ | Có audit log không — Q-009 |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

> Raw chỉ mô tả "hiện thông báo" cho lỗi UID không hợp lệ mà không cung cấp verbatim.

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-QCM-001 | Validation | Scan UID group không tồn tại / không thuộc PO / không thuộc số lô được yêu cầu (vải) | (chưa có — Q-007) | (chưa có — Q-007) | 07105#L910-L911 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Filter VAS theo status Open/In-Progress**
  - **Given:** VAS_A `Open`, VAS_B `Completed`, VAS_C `In-Progress` cùng kho.
  - **When:** User chọn kho.
  - **Then:** App show VAS_A, VAS_C; VAS_B bị filter (R002).
- **AC-02 — Search PO/VAS Step 1**
  - **Given:** Danh sách VAS với mã VAS_X, VAS_Y, PO_P1.
  - **When:** User search "P1".
  - **Then:** Chỉ VAS có PO_P1 xuất hiện (R003).
- **AC-03 — Hiển thị thông tin VAS + sản phẩm Step 2**
  - **Given:** VAS_X có 5 SKU.
  - **When:** User click VAS_X.
  - **Then:** Header hiển thị Shop, VAS, Tổng SKU=5, Mã PO, Tổng sản phẩm; danh sách 5 SKU với Tên/SKU-Barcode/SL/color (R004-R006).
- **AC-04 — Color coding chưa/đang/đã đánh giá**
  - **Given:** 3 SKU trong VAS: SKU_A chưa, SKU_B đang đánh giá, SKU_C đã xong.
  - **When:** User mở VAS.
  - **Then:** SKU_A `Xám nhạt`, SKU_B `Xanh dương nhạt`, SKU_C `Xanh lá nhạt` (R007).
- **AC-05 — Nhập kết quả tiêu chí theo điều kiện**
  - **Given:** Tiêu chí TC `>` 50; user nhập 60 → Enter.
  - **When:** App so sánh.
  - **Then:** Tiêu chí Đạt (R010).
- **AC-06 — Edit kết quả đánh giá**
  - **Given:** TC đã có kết quả Đạt với input 60.
  - **When:** User edit input → 30 → xác nhận.
  - **Then:** Hệ thống tính lại → Không Đạt (R011).
- **AC-07 — Fail bắt buộc chụp + ghi chú (general)**
  - **Given:** Tiêu chí TC config require image.
  - **When:** User chọn Fail → click `Hoàn thành` chưa chụp.
  - **Then:** App block, yêu cầu chụp + ghi chú trước khi submit (R012).
- **AC-08 — Đánh giá hết tiêu chí → sản phẩm xanh lá**
  - **Given:** SKU_A có 3 tiêu chí.
  - **When:** User đánh giá xong 3 → `Hoàn thành`.
  - **Then:** Sản phẩm color → `Xanh lá nhạt` (R013).
- **AC-09 — VAS multi-sản phẩm hoàn thành**
  - **Given:** VAS_X có 5 sản phẩm, đã xong 4.
  - **When:** User cố click `Hoàn thành đánh giá` cho VAS.
  - **Then:** App yêu cầu hoàn thành sản phẩm thứ 5 trước (R014).
- **AC-10 — Step 2 vải có Số lô + HSD**
  - **Given:** SKU vải SKU_V trong VAS.
  - **When:** User mở VAS.
  - **Then:** Danh sách sản phẩm hiển thị Số lô và Hạn sử dụng (R015).
- **AC-11 — 10% group UID hiển thị nhiều dòng**
  - **Given:** Lô L1 có 30 group UID, áp 10% = 3 dòng.
  - **When:** User mở danh sách sản phẩm.
  - **Then:** Lô L1 hiển thị 3 dòng UID group cần đánh giá (R016).
- **AC-12 — Scan UID group invalid**
  - **Given:** SKU vải, lô L1; UID `UID_FOREIGN` không thuộc PO.
  - **When:** User scan `UID_FOREIGN`.
  - **Then:** App hiển thị thông báo lỗi ERR-QCM-001 (R018).
- **AC-13 — Suggest UID đã nhận**
  - **Given:** Lô L1 có 3 UID đã nhận: UID_1, UID_2, UID_3.
  - **When:** User vào màn scan UID.
  - **Then:** App suggest 3 UID này để chọn nhanh (R019).
- **AC-14 — Lỗi 4 điểm — chọn lỗi từ 19 enum**
  - **Given:** Tiêu chí `Lỗi 4 điểm`, mục `Lỗi 2 điểm`.
  - **When:** User click `+` → dropdown chọn lỗi.
  - **Then:** Hiển thị 19 lựa chọn (R023); user phải chọn 1 (bắt buộc).
- **AC-15 — Lỗi 4 điểm — chụp hình bắt buộc**
  - **Given:** User chọn lỗi `9.Scratch`, chưa chụp hình.
  - **When:** Click `Xác nhận`.
  - **Then:** App block, yêu cầu chụp ≥ 1 hình (max 3) (R024).
- **AC-16 — Lỗi 4 điểm — tính tổng điểm**
  - **Given:** User ghi nhận 2 lỗi `Lỗi 2 điểm` + 1 lỗi `Lỗi 3 điểm`.
  - **When:** App tính.
  - **Then:** Số lỗi từng loại + Tổng điểm chưa nhân + Tổng đã nhân theo hệ số được tính (R025).
- **AC-17 — Lỗi 4 điểm — kết quả vs điều kiện**
  - **Given:** Tổng điểm đã nhân = 5; điều kiện thiết lập là ≤ 4.
  - **When:** User click `Hoàn thành` cho tiêu chí.
  - **Then:** Kết quả Không Đạt (R027).
- **AC-18 — Độ co rút step-by-step**
  - **Given:** Tiêu chí `Độ co rút` setup 3 bước.
  - **When:** User đi qua bước 1 → `Tiếp theo` → bước 2 → `Tiếp theo` → bước 3 → `Hoàn thành`.
  - **Then:** App áp công thức tính kết quả → Đạt/Không đạt theo điều kiện (R028, R029).
- **AC-19 — Step 5 — Hoàn thành UID group**
  - **Given:** Đã đánh giá 3 tiêu chí cho UID_1 của lô L1, 1 tiêu chí Không Đạt.
  - **When:** Click `Hoàn thành`.
  - **Then:** UID_1 màu `Cam nhạt` = Không Đạt (R007, R031, R032).
- **AC-20 — Tiếp tục các UID group còn lại**
  - **Given:** Lô L1 có 3 UID cần đánh giá, vừa xong UID_1.
  - **When:** User quay lại danh sách.
  - **Then:** UID_2, UID_3 còn lại để đánh giá tiếp (R033).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R012 | Tiêu chí config require chụp hình OFF — user có thể optional chụp không hay UI hide upload? | UX | Open | | | |
| Q-002 | R024 | Sau khi ghi nhận 1 lỗi (Lỗi 4 điểm), user có thể xoá / sửa lỗi đó không? | UX | Open | | | |
| Q-003 | R023 | Lỗi enum `19.Other` — có cho nhập tên custom không, hay chỉ là 1 category "Khác" generic? | PO | Open | | | |
| Q-004 | R025, R027 | Hệ số nhân cho từng mức Lỗi 4 điểm (1/2/3/4 điểm) — raw không nêu công thức. Default mặc nhiên là 1/2/3/4 hay configurable? | PO | Open | | | |
| Q-005 | R028, R029, R030 | Công thức cho `Độ co rút` và `Độ đồng màu` step-by-step — input/output unit, tolerance — chi tiết chưa được mô tả. Có document riêng không? | PO/Dev | Open | | | |
| Q-006 | R007 | Color coding `Cam nhạt` (Không Đạt) chỉ áp dụng cho luồng vải hay cho general flow non-vải cũng có (chỉ raw mô tả ở section vải)? | UX | Open | | | |
| Q-007 | R018, ERR-QCM-001 | Verbatim message VN+EN khi UID group invalid (không tồn tại / không thuộc PO / không thuộc số lô)? Có phân biệt 3 case không? | PO/UX | Open | | | |
| Q-008 | R005 | "Tìm gần đúng" — semantics: fuzzy (Levenshtein), partial substring, normalized (diacritic-insensitive)? | UX/Dev | Open | | | |
| Q-009 | R011 | Khi user edit kết quả đánh giá, có audit log lưu lịch sử input cũ + người edit + thời gian không? | PO/Compliance | Open | | | |
| Q-010 | R013, R014, E2 | User cố click `Hoàn thành` khi chưa đánh giá hết tiêu chí — App block hay nhắc nhở rồi cho phép submit Pending? | UX | Open | | | |
| Q-011 | R002 | Spelling `Pruchase Order` (raw) — typo của `Purchase Order` ảnh hưởng tới UI key không? | PO/Dev | Open | | | |
| Q-012 | R016, BR | Công thức tính số dòng UID group từ "10% số lượng cây vải của từng lô" — raw nêu "10%" và ví dụ "3 cây vải = 3 dòng" nhưng không đặc tả cách làm tròn (`ceil`/`floor`/`round`) khi kết quả lẻ. | PO/Dev | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-19, S-20 | 1.5 (stub) | 1.5 | All R + AC | Draft |
| CHG-002 | Update | Update 18-09-2025: Đánh giá CL vải bổ sung scan UID group + 3 tiêu chí đặc thù (Lỗi 4 điểm 19 enum, Độ co rút, Độ đồng màu) | (trước 1.5) | 1.5 | R015-R033, AC-10..AC-20 | Done (đã trong raw v1.5) |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_qc_evaluation_mobile | test_stub_qc_evaluation_mobile | Add (chờ Gate 1B) | [[stub_qc_vas]] (VAS source + status Chờ duyệt), [[stub_qc_criteria_sku]] (tiêu chí thiết lập), [[stub_qc_evaluation_result]] (lưu kết quả) | Q-001..Q-011 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R033, AC-01..AC-20 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-011 |

## 🚧 Blocked Coverage

- R012, AC-07 — chờ Q-001 (config OFF behavior)
- R024 — chờ Q-002 (xoá lỗi đã ghi)
- R023, AC-14 — chờ Q-003 (`Other` custom)
- R025, R027, AC-16, AC-17 — chờ Q-004 (hệ số nhân)
- R028-R030, AC-18 — chờ Q-005 (công thức step-by-step)
- R007 — chờ Q-006 (Cam nhạt cho non-vải)
- R018, ERR-QCM-001, AC-12 — chờ Q-007 (verbatim message)
- R005 — chờ Q-008 (search semantics)
- R011, AC-06 — chờ Q-009 (audit log edit)
- R013, R014 — chờ Q-010 (Hoàn thành validation)
- R002 — chờ Q-011 (`Pruchase` typo)
- R016, BR "10% group UID" — chờ Q-012 (công thức làm tròn số dòng UID group)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:36:55 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 16:50:00 | v1.1 | Refine stub → full spec: 33 R-ID, 20 AC, 12 BR, 1 placeholder error message, 11 questions Open. `partial_read: false`. | refine-batch-2-2026-05-30 |
| 2026-05-31 17:00:00 | v1.2 | FIX-004 (refiner batch-3): xóa formula INFERRED `ceil(lot_uid_count × 0.10)` khỏi BR "10% group UID"; giữ verbatim "10%"; thêm Q-012 + Blocked Coverage. | refiner-spec-scoped-batch-3 |
