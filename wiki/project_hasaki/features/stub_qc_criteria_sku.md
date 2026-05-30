---
aliases: [stub_qc_criteria_sku]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_qc_criteria_sku
project: project_hasaki
source_version: 1.5
source_doc: 07105_Quality_Control_Docs_ver1.5.md
source_range: 07105#L217-L432
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 16:20:00"
verification_status: Pending
approved_by:
approved_at:
approval_note:
---

# REQ: stub_qc_criteria_sku

## Tổng quan
- **Mã tính năng:** stub_qc_criteria_sku
- **Feature:** Thiết lập tiêu chí QC cho SKU (Filter, Listing, Create)
- **Mô tả ngắn:** Màn hình `Inbound / Quality control / Tab Thiết lập SKU` cho user setup tiêu chí QC theo SKU. Bao gồm: filter (search SKU/Barcode/Tên + Category + Brand + Active + Thời điểm đánh giá + Tần suất đánh giá + Date), listing với các column thông tin SKU + action buttons, và flow `Tạo mới` (modal 2 bước: nhập thông tin SKU → continue → thiết lập từng tiêu chí với các loại đánh giá Đạt/Không đạt + Theo điều kiện + Công thức).
- **Source chính:** 07105_Quality_Control_Docs_ver1.5.md (v1.5)
- **Đối tượng sử dụng (Actors):** QC Setup user (tạo + chỉnh sửa tiêu chí), QC Manager (Duyệt/Từ chối).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** [[test_stub_qc_criteria_sku]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ➡️ feed [[stub_qc_criteria_approval]] (status `Chờ duyệt` xử lý ở đó). ⬅️ phụ thuộc [[stub_qc_criteria_setup]] (danh sách tiêu chí load).

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
| R001 | Màn hình tab `Thiết lập SKU` (Setup criteria by SKU) trong menu `Inbound / Quality control` | UI | High | ✅ | 07105#L217-L219 |
| R002 | Filter `SKU, Barcode, Tên sản phẩm` (SKU, Barcode, Product name): hỗ trợ tìm theo SKU, Barcode, tên SKU | UI filter | High | ✅ | 07105#L228-L229 |
| R003 | Filter `Danh mục` (Category): hỗ trợ tìm theo category | UI filter | High | ✅ | 07105#L231 |
| R004 | Filter `Thương hiệu` (Brand): hỗ trợ tìm theo brand | UI filter | High | ✅ | 07105#L232 |
| R005 | Filter `Đang hoạt động` (Active): mặc định không chọn; values `Đang hoạt động/Active`, `Ngưng hoạt động/Inactive` | UI filter | High | ✅ | 07105#L233-L236 |
| R006 | Filter `Thời điểm đánh giá` (Assessment time): mặc định không chọn; values `Khi nhận PO/Receiving PO`, `Sau khi nhận PO/After receive of PO` | UI filter | High | ✅ | 07105#L239-L242 |
| R007 | Filter `Tần suất đánh giá` (Assessment frequency): mặc định không chọn; values `Tất cả PO/All PO`, `Ngẫu nhiên/Random` | UI filter | High | ✅ | 07105#L243-L247 |
| R008 | Filter `Từ ngày…đến ngày` (From date…to date): tìm theo ngày tạo; `Đến ngày` phải ≥ `Từ ngày`; mặc định không chọn ngày | UI filter | High | ✅ | 07105#L248-L250 |
| R009 | Listing column `Sản phẩm` (Product): hiển thị `SKU – Tên sản phẩm` | UI | High | ✅ | 07105#L256 |
| R010 | Listing column `Đang hoạt động` (Active): mặc định Active khi SKU mới được setup; user toggle Active/Inactive → hiện confirm dialog | Functional | High | ✅ | 07105#L267-L269 |
| R011 | 1 SKU không thể cùng active 2 thiết lập; phải inactive cái cũ trước khi muốn active cái mới | Business rule | High | ✅ | 07105#L272-L273 |
| R012 | Listing column `Người tạo / Created by`: format `email Hasaki` + `thời gian tạo: YYYY-MM-DD HH:SS` | UI | High | ✅ | 07105#L274-L276 |
| R013 | Listing column `Người cập nhật / Updated by`: format `email Hasaki của người cập nhật cuối cùng` + `thời gian cập nhật cuối cùng: YYYY-MM-DD HH:SS` | UI | High | ✅ | 07105#L277-L279 |
| R014 | Listing column `Thao tác` (Action): button `Cập nhật` chỉ show khi status = `Mới (New)`; button `Xem chi tiết` (cho phép Duyệt/Từ chối); button `Xoá thiết lập` chỉ show khi status = `Mới` | UI | High | ✅ | 07105#L281-L288 |
| R015 | Tạo mới: từ màn quản lý chọn `Tạo mới` → mở modal nhập thông tin SKU | Functional | High | ✅ | 07105#L289-L290 |
| R016 | Tạo modal — field `Sản phẩm` (Product): bắt buộc; hỗ trợ tìm theo SKU, barcode, tên sản phẩm | Functional | High | ✅ | 07105#L294-L299 |
| R017 | Tạo modal — `Thời điểm đánh giá` (Assessment time): bắt buộc; values `Khi nhận PO` (chưa hỗ trợ ở phase này) / `Sau khi nhận PO` | Functional | High | ✅ | 07105#L312-L323 |
| R018 | Tạo modal — `Tần suất đánh giá` (Assessment frequency): bắt buộc; values `Tất cả PO` (Tự động sinh VAS đánh giá sau khi kết thúc phiên nhận) / `Ngẫu nhiên` (User tự tạo phiên đánh giá khi có nhu cầu — chưa hỗ trợ phase này) | Functional | High | ✅ | 07105#L324-L338 |
| R019 | Tạo modal — `Ghi chú` (Note): không bắt buộc | UI | Medium | ✅ | 07105#L339 |
| R020 | Tạo modal — button `Đóng`: tắt popup không lưu | Functional | High | ✅ | 07105#L340 |
| R021 | Tạo modal — button `Tiếp tục`: qua màn hình thiết lập tiêu chí cho SKU; nếu SKU đã được thiết lập + đang Active → báo lỗi | Functional | High | ✅ | 07105#L344-L348 |
| R022 | Màn thiết lập tiêu chí — field `Tiêu chí đánh giá` (Assessment criteria): bắt buộc; load danh sách tất cả tiêu chí trên hệ thống; hỗ trợ tìm theo mã hoặc tên tiêu chí với min 3 ký tự | Functional | High | ✅ | 07105#L365-L368 |
| R023 | Màn thiết lập tiêu chí — field `Yêu cầu chụp hình` (Required Image): bắt buộc chọn; values `Yes`/`No` | UI | High | ✅ | 07105#L369-L371 |
| R024 | Màn thiết lập tiêu chí — field `Hình chụp mẫu` (Sample image): không bắt buộc; upload tối đa 3 hình | UI | High | ✅ | 07105#L372-L374 |
| R025 | Màn thiết lập tiêu chí — field `Loại đánh giá` (Assessment type): default `Đạt/Không đạt` (Phân loại = `Bình thường`, không cho chỉnh sửa) | Functional | High | ✅ | 07105#L375-L379 |
| R026 | `Loại đánh giá = Theo điều kiện`: 6 toán tử `=`, `>`, `>=`, `<`, `<=`, `Trong khoảng (between)` | Enum | High | ✅ | 07105#L380-L406 |
| R027 | Validation cho điều kiện `=`, `>`, `>=`, `<`, `<=`: `Giá trị` bắt buộc, số > 0; `Đơn vị tính` bắt buộc, text; `Sai số cho phép` không bắt buộc, số > 0 | Validation rule | High | ✅ | 07105#L383-L396 |
| R028 | Validation cho điều kiện `Trong khoảng`: `Giá trị từ…đến` bắt buộc, số > 0; `Đơn vị tính` bắt buộc, text | Validation rule | High | ✅ | 07105#L402-L405 |
| R029 | `Loại đánh giá = Công thức`: dùng setup công thức, trả kết quả và so sánh với điều kiện thiết lập (rules chi tiết sẽ bổ sung sau khi trao đổi với Dev — pending) | Functional | Medium | ⚠️ | 07105#L407-L409 |
| R030 | 1 tiêu chí chỉ hỗ trợ 1 điều kiện duy nhất; nút `Thêm (+)` disable khi đã thêm 1 điều kiện; chỉ enable lại khi xoá điều kiện đã thêm | Business rule | High | ✅ | 07105#L411-L413 |
| R031 | Field `Phân loại` (Type) — 3 lựa chọn: `Bình thường/Normal` (quy trình đánh giá bình thường); `Lỗi 4 điểm/4 points error` (quy trình đặc thù); `Theo từng bước/Step by step` (đánh giá theo từng bước) | Enum | High | ✅ | 07105#L414-L420 |
| R032 | Field `Mô tả` (Description): không bắt buộc | UI | Medium | ✅ | 07105#L421 |
| R033 | Button `Thêm` (Add): add tiêu chí vào danh sách thiết lập cho SKU; nếu tiêu chí đã tồn tại trong danh sách → báo lỗi `Tiêu chí đã tồn tại trong danh sách. / Criteria already exists in the list.` | Functional + Error | High | ✅ | 07105#L422-L426 |
| R034 | Button `Đóng` (Close): tắt popup thêm tiêu chí cho SKU | Functional | High | ✅ | 07105#L428 |
| R035 | Button `Lưu` (Save): lưu lại thông tin để tiếp tục cho những lần sau | Functional | High | ✅ | 07105#L429-L430 |
| R036 | Button `Hoàn thành` (Request approve / `Yêu cầu duyệt`): xác nhận chuyển thiết lập cho SKU qua trạng thái `Chờ duyệt` | State transition | High | ✅ | 07105#L431-L432 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User có quyền truy cập tab `Thiết lập SKU` (Setup criteria by SKU).
- Hệ thống đã có danh sách tiêu chí được setup (`stub_qc_criteria_setup`).

### Luồng chuẩn (Happy Path) — Tạo mới tiêu chí cho SKU
1. User vào `Inbound / Quality control` → tab `Thiết lập SKU` (R001).
2. Click `Tạo mới` (R015).
3. Modal hiển thị; user nhập:
   - `Sản phẩm` = `SKU_X` (R016)
   - `Thời điểm đánh giá` = `Sau khi nhận PO` (R017)
   - `Tần suất đánh giá` = `Tất cả PO` (R018)
   - `Ghi chú` = "" (optional — R019)
4. Click `Tiếp tục` → mở màn thiết lập tiêu chí (R021).
5. Trên màn thiết lập tiêu chí, user chọn:
   - `Tiêu chí đánh giá` = `TC001` (search ≥ 3 chars) (R022)
   - `Yêu cầu chụp hình` = `Yes` (R023)
   - `Hình chụp mẫu` = upload 2 hình mẫu (R024)
   - `Loại đánh giá` = `Đạt/Không đạt` (R025) — phân loại default `Bình thường`
   - `Mô tả` = "" (R032)
6. Click `Thêm` → tiêu chí thêm vào danh sách (R033).
7. Lặp lại bước 5-6 cho các tiêu chí khác. Khi đủ, click `Hoàn thành` (R036).
8. Setup chuyển status sang `Chờ duyệt`; chờ Gate 1B của criteria approval (→ [[stub_qc_criteria_approval]]).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — Loại đánh giá `Theo điều kiện` với toán tử so sánh (`=`, `>`, `>=`, `<`, `<=`):** nhập `Giá trị` (số > 0), `Đơn vị tính` (text), optional `Sai số cho phép` (số > 0) (R026, R027).
- **A2 — Loại đánh giá `Trong khoảng`:** nhập `Giá trị từ…đến` (số > 0), `Đơn vị tính` (text) (R028).
- **A3 — Phân loại `Lỗi 4 điểm` hoặc `Theo từng bước`:** quy trình đặc thù (R031).
- **A4 — Loại đánh giá `Công thức`:** pending, chờ trao đổi với Dev (R029 — Q-005).
- **A5 — Toggle Active/Inactive trên listing:** confirm dialog hiện EN message (R010).
- **A6 — Cập nhật / Xoá thiết lập:** chỉ áp dụng cho status = `Mới (New)` (R014).

### Luồng ngoại lệ (Exception Paths)
- **E1 — Modal `Tạo mới` không chọn `Sản phẩm`:** message `Thông tin này là bắt buộc. / This information is required.` (R016).
- **E2 — Modal — SKU đã active trên hệ thống:** message `SKU {sku_code} đã tồn tại và đang hoạt động trên hệ thống.` (R016 + ERR-CSKU-002).
- **E3 — Continue khi SKU đã được thiết lập và Active:** message `SKU đã được thiết lập và đang hoạt động.` (R021 + ERR-CSKU-003).
- **E4 — Trùng tiêu chí trong danh sách thiết lập:** message `Tiêu chí đã tồn tại trong danh sách.` (R033).
- **E5 — Cố thêm điều kiện thứ 2 cho 1 tiêu chí:** nút `Thêm (+)` disable (R030).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Filter date `Từ ngày → Đến ngày` | date | ❌ | `Đến ngày ≥ Từ ngày` |
| Filter `Active` | enum | ❌ | `Đang hoạt động/Active` hoặc `Ngưng hoạt động/Inactive` |
| Filter / Modal `Thời điểm đánh giá` | enum | ❌ (filter) / ✅ (modal) | Values: `Khi nhận PO/Receiving PO` (chưa hỗ trợ phase 1), `Sau khi nhận PO/After receive of PO` |
| Filter / Modal `Tần suất đánh giá` | enum | ❌ (filter) / ✅ (modal) | Values: `Tất cả PO/All PO` (auto VAS), `Ngẫu nhiên/Random` (manual, chưa hỗ trợ phase 1) |
| 1 SKU active duy nhất 1 setup | rule | ✅ | Cùng SKU không thể có 2 setup status Active đồng thời (R011) |
| 1 tiêu chí 1 điều kiện | rule | ✅ | Nút `Thêm (+)` disable sau khi add 1 điều kiện; reset khi xoá điều kiện (R030) |
| Loại đánh giá `Đạt/Không đạt` | enum | ✅ default | Default; Phân loại = `Bình thường` không cho sửa |
| Toán tử điều kiện | enum | ✅ | `=`, `>`, `>=`, `<`, `<=`, `Trong khoảng (between)` |
| Validation `Giá trị` | numeric | ✅ | > 0 |
| Validation `Đơn vị tính` | text | ✅ | Không rỗng |
| Validation `Sai số cho phép` | numeric | ❌ | > 0 nếu có |
| Phân loại (Type) | enum | ✅ | `Bình thường/Normal`, `Lỗi 4 điểm/4 points error`, `Theo từng bước/Step by step` |
| Yêu cầu chụp hình | enum | ✅ | `Yes`/`No` |
| Hình chụp mẫu | file | ❌ | Tối đa 3 hình |
| Search tiêu chí | string | ❌ | Min 3 ký tự để trigger search (R022) |
| Người tạo / Người cập nhật | format | ✅ | Email Hasaki + thời gian `YYYY-MM-DD HH:SS` |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-CSKU-001 | Validation | Field bắt buộc trong modal Tạo mới chưa nhập | `Thông tin này là bắt buộc.` | `This information is required.` | 07105#L303-L304, L317-L318, L329-L330 |
| ERR-CSKU-002 | Validation | SKU đã được thiết lập trước và đang Active | `SKU {sku_code} đã tồn tại và đang hoạt động trên hệ thống.` | `SKU {sku_code} already exists and is active in the system.` | 07105#L308-L311 |
| ERR-CSKU-003 | Validation | Click `Tiếp tục` từ modal nhưng SKU đã active | `SKU đã được thiết lập và đang hoạt động.` | `SKU has been set up and is currently active` | 07105#L347-L348 |
| ERR-CSKU-004 | Validation | Tiêu chí trùng trong danh sách thiết lập | `Tiêu chí đã tồn tại trong danh sách.` | `Criteria already exists in the list.` | 07105#L425-L426 |
| MSG-CSKU-005 | Confirm | Toggle Active → Inactive | (chưa có VN) | `Do you want to DEACTIVATE setup by SKU {sku_code}?` | 07105#L270 |
| MSG-CSKU-006 | Confirm | Toggle Inactive → Active | (chưa có VN) | `Do you want to ACTIVATE setup by SKU {sku_code}?` | 07105#L271 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Filter date range Đến ngày ≥ Từ ngày**
  - **Given:** Filter `Từ ngày` = 2026-05-15, `Đến ngày` = 2026-05-10.
  - **When:** User apply filter.
  - **Then:** Hệ thống không cho phép (validation `Đến ngày ≥ Từ ngày` — R008).
- **AC-02 — Tạo mới — empty Sản phẩm**
  - **Given:** Modal `Tạo mới` mở.
  - **When:** User click `Tiếp tục` không nhập `Sản phẩm`.
  - **Then:** Hiển thị ERR-CSKU-001 dưới field `Sản phẩm` (R016).
- **AC-03 — Tạo mới — SKU đã active**
  - **Given:** SKU `422280022` đã có setup status Active.
  - **When:** User nhập `Sản phẩm = 422280022` trong modal Tạo mới.
  - **Then:** Hiển thị ERR-CSKU-002 (R016).
- **AC-04 — Tiếp tục — SKU đã setup + Active (lần 2)**
  - **Given:** SKU đã được setup và Active; user vẫn cố vào modal Tạo mới với SKU đó.
  - **When:** Click `Tiếp tục`.
  - **Then:** Hiển thị ERR-CSKU-003 (R021).
- **AC-05 — Search tiêu chí min 3 ký tự**
  - **Given:** Màn thiết lập tiêu chí, user gõ "AB" (2 ký tự).
  - **When:** User nhập tiếp.
  - **Then:** Search chưa trigger; gõ thêm 1 ký tự "ABC" → search trigger (R022).
- **AC-06 — Upload max 3 hình mẫu**
  - **Given:** Field `Hình chụp mẫu`.
  - **When:** User upload 4 file.
  - **Then:** Hệ thống chỉ chấp nhận 3 file đầu (R024).
- **AC-07 — Loại đánh giá `Đạt/Không đạt` default + Phân loại `Bình thường` không sửa**
  - **Given:** Tạo tiêu chí mới.
  - **When:** Mở màn thiết lập.
  - **Then:** Default `Loại đánh giá = Đạt/Không đạt`, `Phân loại = Bình thường` và không cho sửa (R025).
- **AC-08 — Validation điều kiện `=` Giá trị > 0**
  - **Given:** Loại đánh giá `Theo điều kiện`, toán tử `=`.
  - **When:** User nhập `Giá trị = -5`.
  - **Then:** Hệ thống reject (R027 — yêu cầu > 0).
- **AC-09 — Toán tử `Trong khoảng` cần Giá trị từ + đến**
  - **Given:** Loại đánh giá `Theo điều kiện`, toán tử `Trong khoảng`.
  - **When:** User nhập từ = 5, đến = "" (trống).
  - **Then:** Hệ thống yêu cầu nhập đủ (R028).
- **AC-10 — 1 tiêu chí 1 điều kiện**
  - **Given:** User đã add 1 điều kiện cho tiêu chí.
  - **When:** User cố click `Thêm (+)` để add điều kiện thứ 2.
  - **Then:** Nút `Thêm (+)` disable (R030).
- **AC-11 — Trùng tiêu chí trong danh sách**
  - **Given:** Danh sách thiết lập đã có `TC001`.
  - **When:** User cố add `TC001` lần 2.
  - **Then:** Hiển thị ERR-CSKU-004 (R033).
- **AC-12 — `Hoàn thành` → Chờ duyệt**
  - **Given:** Đã add ≥ 1 tiêu chí vào danh sách thiết lập.
  - **When:** User click `Hoàn thành`.
  - **Then:** Setup chuyển status sang `Chờ duyệt` (R036) → unlock luồng `stub_qc_criteria_approval`.
- **AC-13 — 1 SKU không 2 setup active**
  - **Given:** SKU_A có setup_1 status Active.
  - **When:** User cố Active setup_2 cho cùng SKU_A.
  - **Then:** Hệ thống chặn; yêu cầu Inactive setup_1 trước (R011).
- **AC-14 — Toggle Active confirm dialog**
  - **Given:** Setup cho SKU `422280022` status Active.
  - **When:** User toggle sang Inactive.
  - **Then:** Hiển thị MSG-CSKU-005 (R010).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | Section start | Index JSON (S-07: L192-L218, S-08: L219-L399) **không khớp** với content thật (`Thiết lập tiêu chí cho SKU` bắt đầu ở L217, `Tạo tiêu chí cho SKU` ở L289). Cần re-anchor section boundary trong index. | Internal (script `index_skeleton.py`) | Open | | | |
| Q-002 | R005, R014 | Status setup gồm những values nào ngoài `Mới (New)`, `Chờ duyệt`, `Đã duyệt`, `Từ chối`, `Open`? Raw chỉ đề cập rời rạc, không có 1 bảng tổng hợp. | PO | Open | | | |
| Q-003 | R017, R018 | `Khi nhận PO / Receiving PO` và `Ngẫu nhiên / Random` cùng được mô tả "chưa hỗ trợ phase này" — phase tiếp theo (2/3) hay không có timeline? | PO | Open | | | |
| Q-004 | R022 | Search tiêu chí min 3 ký tự — chỉ áp dụng cho mã/tên tiêu chí, hay cho mọi field search trong form thiết lập? | UX | Open | | | |
| Q-005 | R029 | Loại đánh giá `Công thức`: rules chi tiết "sẽ bổ sung sau khi trao đổi với Dev" — đã có conclusion chưa? Nếu chưa, R029 + AC liên quan phải Block. | Dev Lead | Open | | | |
| Q-006 | R023 | `Yêu cầu chụp hình = Yes` thì sau khi đánh giá QC, user có bắt buộc chụp hình mới được submit không? Hay chỉ là flag để display? | PO | Open | | | |
| Q-007 | R012, R013 | Format `YYYY-MM-DD HH:SS` — SS nghĩa là **seconds** hay đây là typo của `HH:MM` (minutes)? Format ISO chuẩn có dạng `HH:MM:SS`. | PO/Dev | Open | | | |
| Q-008 | R010, MSG-CSKU-005 | Verbatim message VN cho confirm `DEACTIVATE` và `ACTIVATE` — raw chỉ cung cấp EN. | PO | Open | | | |
| Q-009 | R031 | Khi `Phân loại = Lỗi 4 điểm` hoặc `Theo từng bước` — UI thay đổi thế nào so với `Bình thường`? Có thêm field gì không? | UX/PO | Open | | | |
| Q-010 | R030 | "1 tiêu chí 1 điều kiện" — `1 tiêu chí` ở đây nghĩa là 1 dòng `Tiêu chí đánh giá` chọn trong dropdown, hay 1 row tiêu chí trong danh sách thiết lập của SKU? | PO | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-07, S-08 (lưu ý S-07/S-08 boundary trong index không khớp content — Q-001) | 1.5 (stub) | 1.5 | All R + AC | Draft |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_qc_criteria_sku | test_stub_qc_criteria_sku | Add (chờ Gate 1B) | [[stub_qc_criteria_approval]] (status `Chờ duyệt` sink), [[stub_qc_criteria_setup]] (danh sách tiêu chí load) | Q-001..Q-010 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R036, AC-01..AC-14 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-010 |

## 🚧 Blocked Coverage

- R005, R014 — chờ Q-002 (status enum đầy đủ)
- R017, R018 — chờ Q-003 (phase support timeline)
- R022 — chờ Q-004 (search semantics phạm vi)
- R029, AC-04 — chờ Q-005 (rules `Công thức` từ Dev)
- R023 — chờ Q-006 (Yêu cầu chụp hình → bắt buộc khi submit?)
- R012, R013 — chờ Q-007 (format HH:SS vs HH:MM)
- R010, MSG-CSKU-005/006 — chờ Q-008 (verbatim VN)
- R031, A3 — chờ Q-009 (UI cho 4-point và step-by-step)
- R030 — chờ Q-010 (semantics "1 tiêu chí")

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:36:55 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 16:20:00 | v1.1 | Refine stub → full spec: 36 R-ID, 14 AC, 16 BR, 6 messages (4 verbatim VN+EN), 10 questions Open. `partial_read: false`. | refine-batch-2-2026-05-30 |
