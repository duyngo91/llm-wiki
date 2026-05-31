---
aliases: [stub_qc_criteria_setup]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_qc_criteria_setup
project: project_hasaki
source_version: 1.5
source_doc: 07105_Quality_Control_Docs_ver1.5.md
source_range: 07105#L125-L1323
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-31 18:36:07"
verification_status: Verified
approved_by:
approved_at:
approval_note: "FIX-001: xóa inferred 'thấp nhất' khỏi BR + Q-006 trace; FIX-002: thêm Q-016 typo L141 + R002 ⚠️"
last_verified_source_version: 1.5

---

# REQ: stub_qc_criteria_setup

## Tổng quan
- **Mã tính năng:** stub_qc_criteria_setup
- **Feature:** Thiết lập tiêu chí QC — Master criteria + Per-SKU + Đánh giá điều kiện + Phân loại 4 điểm/Theo từng bước + QC xã vải
- **Mô tả ngắn:** Bao gồm 4 mảng chính: (1) **Thiết lập tiêu chí** (`Tab Thiết lập tiêu chí`) — Listing với filter (Mã/tên + Active + Ngày), Listing fields, Tạo tiêu chí (Mã + Tên unique, Mô tả/Hướng dẫn optional), Import tiêu chí với 4 validation message. (2) **Thiết lập tiêu chí cho SKU** (`Tab Thiết lập SKU`) — Listing với filter (SKU/Brand/Cate/Active/Thời điểm/Tần suất/Ngày), Tạo tiêu chí cho SKU với form (Sản phẩm + Thời điểm `Khi nhận PO`/`Sau khi nhận PO` + Tần suất `Tất cả PO`/`Ngẫu nhiên`), Mutex 1 SKU 1 thiết lập active, Add tiêu chí với `Yêu cầu chụp hình`+`Hình mẫu`+`Loại đánh giá`+`Phân loại`. (3) **Đánh giá theo điều kiện** — `=`, `>`, `>=`, `<`, `<=`, `Trong khoảng`, `Công thức`; 1 tiêu chí 1 điều kiện mutex. (4) **Phân loại tiêu chí** — `Bình thường`/`Lỗi 4 điểm`/`Theo từng bước` với modal thiết lập riêng cho mỗi loại. Update 05-08-2025: tiêu chí inactive impact theo state SKU setup. Update 17-09-2025: setup từng bước (10 step max). Update 27-09-2025: setup lỗi 4 điểm. Update 11-02-2026: bổ sung `QC xã vải`. Update 10-05-2026: auto inherit tiêu chí khi assign SKU.
- **Source chính:** 07105_Quality_Control_Docs_ver1.5.md (v1.5)
- **Đối tượng sử dụng (Actors):** QC team, BOD (duyệt SKU setup).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** [[test_stub_qc_criteria_setup]]
- **API Spec liên quan:** N/A — raw không nêu API; mention "công thức (sẽ bổ sung rules sau khi trao đổi với Dev)".
- **Mối quan hệ:** ⬅️ phụ thuộc master data SKU + Category + Brand. ↔️ liên quan [[stub_qc_criteria_sku]] (Setup SKU detail), [[stub_qc_criteria_approval]] (Duyệt thiết lập). ➡️ feed [[stub_qc_evaluation_mobile]] / [[stub_qc_evaluation_manual]] (tiêu chí dùng đánh giá), [[stub_qc_uid_group]] (QC xã vải).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07105_Quality_Control_Docs_ver1.5.md | 1.5 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | Công thức validation API — raw mention "sẽ bổ sung rules sau khi trao đổi với Dev" | R023, R029 | 07105#L407-L409 | TBD — Q-001 |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Thiết lập tiêu chí — `Menu: Inbound / Quality control / Tab Thiết lập tiêu chí (Setup criteria)` | UI + Navigation | High | ✅ | 07105#L126-L128 |
| R002 | Filter listing tiêu chí — `Mã, tên tiêu chí` (Code, Criteria name): tìm gần đúng, nhập từ 3 ký tự; `Đang hoạt động` (Active); `Từ ngày…đến ngày` (From date…to date): tìm theo ngày tạo, `Đến ngày` ≥ `Từ ngày` (raw L141 có typo — Q-016), default không chọn | Filter + Validation | High | ⚠️ | 07105#L131-L143 |
| R003 | Listing tiêu chí — cột: `TT` (tăng dần), `Mã tiêu chí` (theo user nhập), `Tên tiêu chí`, `Mô tả`, `Hướng dẫn`, `Đang hoạt động` (default `Active` khi tạo mới), `Người tạo` (email + thời gian `YYYY-MM-DD HH:SS`), `Người cập nhật`, `Thao tác` | UI + Functional | High | ✅ | 07105#L144-L170 |
| R004 | Active/Inactive tiêu chí — khi muốn Active/Inactive thiết lập cho SKU thì **hiện thông báo xác nhận**: `Do you want to DEACTIVATE criterion 1001?` / `Do you want to ACTIVATE criterion 1001?` | Confirm + State transition | High | ✅ | 07105#L152-L160 |
| R005 | Thao tác — chọn để cập nhật thông tin cho tiêu chí. **Không cho cập nhật mã tiêu chí**, các thông tin còn lại được phép cập nhật | Functional + Validation | High | ✅ | 07105#L167-L170 |
| R006 | Tạo tiêu chí — Tại màn quản lý tiêu chí, chọn `Tạo mới`. Field: `Mã tiêu chí` (Criteria code) **bắt buộc**; không được trùng → `Mã tiêu chí đã tồn tại.` / `The criteria code already exists.` | Validation | High | ✅ | 07105#L171-L179 |
| R007 | Tạo tiêu chí — Field `Tên tiêu chí` (Criteria name) **bắt buộc**; không được trùng → `Tên tiêu chí đã tồn tại.` / `The criteria name already exists.` | Validation | High | ✅ | 07105#L180-L189 |
| R008 | Tạo tiêu chí — Field `Mô tả` (Description) **không bắt buộc**; `Hướng dẫn` (instruct) **không bắt buộc**. Buttons: `Đóng` tắt popup; `Lưu và đóng` lưu + tắt; `Lưu và tiếp tục` lưu + clear thông tin để tiếp tục tạo | UI + Functional | High | ✅ | 07105#L190-L198 |
| R009 | Import tiêu chí — Template import + Validate. 4 messages: `Mã tiêu chí đã tồn tại trên hệ thống thống` / `The criteria code already exists in the systems.`; `Mã tiêu chí đã tồn tại trong file import` / `The criteria code already exists in the template import.`; `Tên tiêu chí đã tồn tại trên hệ thống thống` / `The criteria name already exists in the systems.`; `Tên tiêu chí đã tồn tại trong file import` / `The criteria name already exists in the template import.`. Luồng import sử dụng lại page import dùng chung cho các tính năng đã làm trước | Validation + Import | High | ✅ | 07105#L199-L211 |
| R010 | Thiết lập tiêu chí cho SKU — `Menu: Inbound / Quality control / Tab Thiết lập SKU (Setup criteria by SKU)` | UI + Navigation | High | ✅ | 07105#L217-L220 |
| R011 | Filter SKU setup — `SKU, Barcode, Tên sản phẩm` (Product name); `Danh mục` (Category); `Thương hiệu` (Brand); `Đang hoạt động` (Active) default không chọn — values `Đang hoạt động`/`Ngưng hoạt động`; `Trạng thái` (Status); `Thời điểm đánh giá` (Assessment time) — values `Khi nhận PO` (Receiving PO) / `Sau khi nhận PO` (After receive of PO); `Tần suất đánh giá` (Assessment frequency) — values `Tất cả PO` / `Ngẫu nhiên`; `Từ ngày…đến ngày` (default không chọn) | Filter + Enum | High | ✅ | 07105#L226-L250 |
| R012 | Listing SKU setup — cột: `TT`, `Sản phẩm` (`SKU – Tên sản phẩm`), `Danh mục`, `Thương hiệu`, `Thời điểm đánh giá`, `Tần suất đánh giá`, `Số lượng tiêu chí`, `Đang hoạt động` (default Active khi tạo mới), `Người tạo`, `Người cập nhật`, `Trạng thái`, `Thao tác` | UI + Functional | High | ✅ | 07105#L253-L283 |
| R013 | SKU setup — Active/Inactive: `Do you want to DEACTIVATE setup by SKU 422280022?` / `Do you want to ACTIVATE setup by SKU 422280022?`. **Lưu ý: tại 1 thời điểm 1 SKU không thể cùng active 2 thiết lập** — phải inactive cái cũ trước khi muốn active cái mới | Confirm + Business rule | High | ✅ | 07105#L267-L274 |
| R014 | SKU setup `Thao tác` — 3 buttons: (a) Cập nhật thông tin tiêu chí (vào trang cập nhật), **chỉ show cho status `Mới (New)`**; (b) Xem chi tiết thiết lập / Duyệt-Từ chối; (c) Xoá thiết lập, **chỉ show cho status `Mới (New)`** | UI + Functional + Business rule | High | ✅ | 07105#L281-L288 |
| R015 | Tạo tiêu chí cho SKU — `Tạo mới`. Field `Sản phẩm` (Product) **bắt buộc**; hỗ trợ tìm bằng SKU/barcode/tên SP. Nếu chưa chọn → `Thông tin này là bắt buộc.` / `This information is required.`. Nếu SKU đã được thiết lập **trạng thái Active** → `SKU 422280022 đã tồn tại và đang hoạt động trên hệ thống.` / `SKU 422280022 already exists and is active in the system.` | Validation + UI | High | ✅ | 07105#L289-L311 |
| R016 | Tạo tiêu chí cho SKU — Field `Thời điểm đánh giá` (Assessment time) **bắt buộc**; chưa chọn → `Thông tin này là bắt buộc.`. Values: `Khi nhận PO / Receiving PO` (**chưa hỗ trợ ở phase này**); `Sau khi nhận PO / After receive of PO` | Validation + Enum | High | ✅ | 07105#L312-L323 |
| R017 | Tạo tiêu chí cho SKU — Field `Tần suất đánh giá` (Assessment frequency) **bắt buộc**. Values: `Tất cả PO` (tự động sinh VAS đánh giá SP sau khi kết thúc phiên nhận); `Ngẫu nhiên` (user tự tạo phiên đánh giá khi có nhu cầu, **chưa hỗ trợ ở phase này**) | Validation + Enum | High | ✅ | 07105#L324-L338 |
| R018 | Tạo tiêu chí cho SKU — Field `Ghi chú` (Note) **không bắt buộc**. Buttons: `Đóng` tắt popup; `Tiếp tục` qua màn thiết lập tiêu chí cho SKU | Functional + UI | High | ✅ | 07105#L339-L344 |
| R019 | Tạo tiêu chí cho SKU — Validation `Tiếp tục`: nếu SKU đã được thiết lập tiêu chí và đang Active → `SKU đã được thiết lập và đang hoạt động.` / `SKU has been set up and is currently active` | Validation | High | ✅ | 07105#L345-L348 |
| R020 | Màn thiết lập tiêu chí cho SKU — Form fields: `Sản phẩm`, `Danh mục`, `Thương hiệu`, `Thời điểm đánh giá`, `Tần suất đánh giá`, `Ghi chú` (đọc từ Step 1) + `Tiêu chí đánh giá` (Assessment criteria) **bắt buộc** — load danh sách tất cả tiêu chí trên hệ thống, hỗ trợ tìm theo mã hoặc tên (nhập từ 3 ký tự) | UI + Filter | High | ✅ | 07105#L357-L368 |
| R021 | Tiêu chí đánh giá Setup — Field `Yêu cầu chụp hình` (Required Image) **bắt buộc chọn**, values `Yes/No`; `Hình chụp mẫu` (Sample image) **không bắt buộc**, upload tối đa **3 hình** | Validation + UI | High | ✅ | 07105#L369-L374 |
| R022 | Tiêu chí — Field `Loại đánh giá` (Assessment type) — 2 lựa chọn: `Đạt/Không đạt` (default; mặc định phân loại = `Bình thường` và **không cho chỉnh sửa**); `Theo điều kiện` | Enum + Business rule | High | ✅ | 07105#L375-L380 |
| R023 | Loại đánh giá `Theo điều kiện` — operators: `=`, `>`, `>=`, `<`, `<=`. Mỗi operator có field: `Giá trị` **bắt buộc**, số > 0; `Đơn vị tính` (text) **bắt buộc**; **operator `=` thêm field** `Sai số cho phép` (không bắt buộc, số > 0). Operator `Trong khoảng (between)`: `Giá trị từ…đến` **bắt buộc**, số > 0; `Đơn vị tính` bắt buộc | Validation + Enum | High | ✅ | 07105#L380-L406 |
| R024 | Loại đánh giá — Operator `Công thức`: thiết lập công thức, trả kết quả và so sánh với điều kiện đã thiết lập. **Sẽ bổ sung rules sau khi trao đổi với Dev** (raw L408-L409 mark — Q-001) | Functional + Pending | Medium | ⚠️ | 07105#L407-L409 |
| R025 | Tiêu chí — Lưu ý: **1 tiêu chí chỉ hỗ trợ 1 điều kiện duy nhất**. Khi đã thêm 1 điều kiện → nút `Thêm (+)` disable. Chỉ khi xoá điều kiện đã thêm → nút `Thêm (+)` hiện lên | Business rule + UI | High | ✅ | 07105#L410-L413 |
| R026 | Tiêu chí — Field `Phân loại` (Type) 3 values: `Bình thường / Normal` (quy trình bình thường); `Lỗi 4 điểm / 4 points error` (quy trình đặc thù); `Theo từng bước / Step by step` (thiết lập từng bước) | Enum | High | ✅ | 07105#L414-L420 |
| R027 | Tiêu chí — Field `Mô tả` (Description) **không bắt buộc**. Button `Thêm` (Add): sau khi chọn xong thông tin → add tiêu chí vào danh sách thiết lập cho SKU. Nếu tiêu chí đã tồn tại trong danh sách → `Tiêu chí đã tồn tại trong danh sách.` / `Criteria already exists in the list.` | Functional + Validation | High | ✅ | 07105#L421-L427 |
| R028 | Buttons Setup SKU — `Đóng` tắt popup; `Lưu` (Save) lưu thông tin để tiếp tục lần sau; `Yêu cầu duyệt` (Request approve) — chọn `Hoàn thành` để xác nhận chuyển thiết lập SKU sang status `Chờ duyệt` (Waiting for Approval) | Functional + State transition | High | ✅ | 07105#L428-L432 |
| R029 | Update 05-08-2025 — Tiêu chí inactive impact: (a) Nếu thiết lập SKU đang status `Open` hoặc `Waiting for Approval` mà tiêu chí trong SKU **bị inactive** → tiêu chí đó sẽ **xoá khỏi danh sách tiêu chí cho SKU**; (b) Nếu thiết lập SKU đang status `Approved` mà tiêu chí **bị inactive** → tiêu chí đó sẽ **không hiển thị cho SKU** (nhưng còn lưu) | Business rule + State transition | High | ✅ | 07105#L433-L437 |
| R030 | Update 17-09-2025 — Thiết lập đánh giá từng bước cho tiêu chí. Tại màn thiết lập tiêu chí cho SKU, chọn edit cho tiêu chí với `type = Theo từng bước` → mở modal thiết lập các bước cần đánh giá. **Lưu ý: khi add tiêu chí có phân loại `Theo từng bước` → tự động chuyển qua màn thiết lập các bước** để user thao tác ngay | Functional + UX | High | ✅ | 07105#L443-L450 |
| R031 | Update 17-09-2025 — Form bước đánh giá: `Tiêu chí` (theo tiêu chí được chọn); `Bước` (Step) số thứ tự `1 đến 10` — số đã chọn disable không cho chọn lại; `Nội dung` (tên bước); `Yêu cầu chụp hình` (bước có chụp hình trên App hay không); `Hình ảnh mẫu` (Reference image); `Ghi nhận kết quả` (Record results) — values: `Không / No`, `Nhập giá trị / Fill value`, `Đạt / Không đạt – Passed / Failed` | Enum + UI | High | ✅ | 07105#L451-L467 |
| R032 | Update 17-09-2025 — Field `Từ khoá` (Keywords) — chỉ show nếu Ghi nhận kết quả ≠ `Không`. **Tự động bật in hoa và không cho nhập khoảng trắng**. Cho phép ký tự đặc biệt: `_`, `-`, `.`. Field `Hướng dẫn` (Intruction) cho nhập text. Field `Công thức` (Formula) thiết lập công thức | Validation + UI | High | ✅ | 07105#L468-L475 |
| R033 | Update 17-09-2025 — Button `Kiểm tra định dạng` (Check format) — check cấu trúc công thức có hợp lệ và đúng format hay chưa: `Hợp lệ` chữ xanh lá; `Không hợp lệ` chữ đỏ. Button `Đóng` tắt popup. Button `Lưu` (Save) — chỉ hiện khi có ít nhất 1 bước được thiết lập + công thức nếu nhập phải hợp lệ. Nếu user cập nhật công thức nhưng chưa chọn `Kiểm tra định dạng` → khi nhấn Lưu sẽ validate thêm 1 lần | Functional + Validation | High | ✅ | 07105#L476-L488 |
| R034 | Update 27-09-2025 — Thiết lập nội dung đánh giá cho tiêu chí **Lỗi 4 điểm**. Tại màn thiết lập tiêu chí cho SKU, chọn edit cho tiêu chí với `type = Lỗi 4 điểm` → mở modal thiết lập nội dung. **Lưu ý: khi thiết lập tiêu chí có phân loại `Lỗi 4 điểm` → tự động chuyển qua màn thiết lập các bước** để user thao tác ngay | Functional + UX | High | ✅ | 07105#L493-L499 |
| R035 | Update 27-09-2025 — Form fields cho Lỗi 4 điểm (giống Theo từng bước nhưng không có Step number): `Tiêu chí`, `Nội dung`, `Yêu cầu chụp hình`, `Ghi nhận kết quả` (Không/Nhập giá trị/Đạt-Không đạt), `Từ khoá`, `Hướng dẫn`, `Công thức`, `Kiểm tra định dạng`, `Đóng`, `Lưu` | UI + Validation | High | ✅ | 07105#L500-L525 |
| R036 | Update 11-02-2026 — Bổ sung thông tin `QC xã vải` (Fabric relaxation QC) khi tạo hay cập nhật tiêu chí. Thông tin này dùng để tạo yêu cầu đánh giá xã vải khi UID group được TF vào location `F0-XV` (xem [[stub_qc_uid_group]]) | Functional + Business rule | High | ✅ | 07105#L1081-L1097 |
| R037 | Update 10-05-2026 — **Thiết lập tiêu chí 4 điểm** khi setup tiêu chí. Nếu chọn phân loại = `Lỗi 4 điểm` thì khi nhấn `Tạo` → hệ thống mở thêm màn thiết lập nội dung cho tiêu chí 4 điểm (giống setup tiêu chí cho SKU). Khi assign tiêu chí cho SKU → hệ thống **tự lấy các thiết lập của tiêu chí để cập nhật cho SKU**, không cần thiết lập lại từng SKU | Functional + Auto-inherit | High | ✅ | 07105#L1304-L1311 |
| R038 | Update 10-05-2026 — **Thiết lập đánh giá từng bước** khi setup tiêu chí. Nếu chọn phân loại = `Theo từng bước` thì khi nhấn `Tạo` → hệ thống mở thêm màn thiết lập từng bước (giống setup tiêu chí cho SKU). Khi assign cho SKU → auto inherit | Functional + Auto-inherit | High | ✅ | 07105#L1312-L1321 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User có quyền QC + truy cập `Inbound / Quality control`.
- Master data SKU, Category, Brand đã có.

### Luồng chuẩn (Happy Path) — Tạo master tiêu chí
1. QC vào `Tab Thiết lập tiêu chí`, click `Tạo mới` (R001, R006).
2. Form mở:
   - Nhập `Mã tiêu chí = T-001` (R006). Nếu trùng → ERR-CRS-001.
   - Nhập `Tên tiêu chí = Kiểm tra ngoại quan` (R007). Nếu trùng → ERR-CRS-002.
   - Nhập `Mô tả` + `Hướng dẫn` (R008).
3. Click `Lưu và đóng` → tiêu chí lưu, status default `Active` (R008).
4. Listing hiển thị tiêu chí mới với Người tạo + thời gian (R003).

### Luồng chuẩn (Happy Path) — Import tiêu chí
1. QC chọn `Import tiêu chí` (R009).
2. Upload file template.
3. Hệ thống validate — báo nếu mã/tên trùng hệ thống / trùng file import (R009).

### Luồng chuẩn (Happy Path) — Tạo tiêu chí cho SKU
1. QC vào `Tab Thiết lập SKU`, click `Tạo mới` (R010, R015).
2. Form Step 1 mở:
   - Tìm SP (SKU/barcode/tên). Nếu SKU đã Active → ERR-CRS-003.
   - Chọn `Thời điểm = Sau khi nhận PO` (R016).
   - Chọn `Tần suất = Tất cả PO` (R017).
   - Nhập `Ghi chú` (optional) (R018).
   - Click `Tiếp tục`. Validate: nếu SKU đã Active → ERR-CRS-004 (R019).
3. Form Step 2 mở (thiết lập tiêu chí cho SKU) (R020):
   - Field `Tiêu chí đánh giá` — load list tiêu chí + search 3+ ký tự (R020).
   - Chọn tiêu chí + cập nhật `Yêu cầu chụp hình = Yes`, upload 2 hình mẫu (max 3) (R021).
   - `Loại đánh giá = Đạt/Không đạt` → `Phân loại = Bình thường` không sửa (R022).
   - HOẶC `Loại đánh giá = Theo điều kiện` → chọn operator (R023):
     - `=` 100 đơn vị `kg` + `Sai số = 5` (optional).
     - `Trong khoảng` 80 đến 120 đơn vị `kg`.
     - `Công thức` → chờ rules Dev (R024).
   - 1 tiêu chí 1 điều kiện; thêm 1 → nút `+` disable (R025).
   - Chọn `Phân loại = Bình thường` / `Lỗi 4 điểm` / `Theo từng bước` (R026).
   - Click `Thêm` → add vào danh sách (R027). Nếu tiêu chí đã có → ERR-CRS-005.
4. Khi đủ tiêu chí, click `Lưu` để tiếp tục, hoặc `Yêu cầu duyệt` → chuyển status `Chờ duyệt` (R028).

### Luồng chuẩn (Happy Path) — Update 17-09-2025 thiết lập từng bước
1. Add tiêu chí với `Phân loại = Theo từng bước` → auto mở màn thiết lập bước (R030).
2. Form bước: chọn `Step 1`, nhập `Nội dung = Kiểm tra màu`, `Yêu cầu chụp hình = Yes`, upload mẫu, `Ghi nhận kết quả = Đạt/Không đạt` (R031).
3. Nếu Ghi nhận khác `Không`: nhập `Từ khoá` (auto in hoa, không space, được `_-.`) (R032).
4. Nhập `Hướng dẫn`, `Công thức`. Click `Kiểm tra định dạng` → xanh = OK (R033).
5. Click `Lưu` — chỉ hiện khi ≥ 1 bước + công thức hợp lệ; nếu công thức chưa check → auto validate khi Lưu (R033).
6. Lặp tới max Step 10 (R031).

### Luồng chuẩn (Happy Path) — Update 27-09-2025 thiết lập lỗi 4 điểm
1. Add tiêu chí với `Phân loại = Lỗi 4 điểm` → auto mở màn thiết lập (R034).
2. Form: `Tiêu chí`, `Nội dung`, `Yêu cầu chụp hình`, `Ghi nhận kết quả`, `Từ khoá`, `Hướng dẫn`, `Công thức`, `Kiểm tra định dạng` (R035).
3. Click `Lưu` (R035).

### Luồng chuẩn (Happy Path) — Update 11-02-2026 bổ sung QC xã vải
1. Tạo/cập nhật tiêu chí.
2. Bổ sung field `QC xã vải` (R036).
3. Dùng để trigger sinh yêu cầu đánh giá xã vải khi UID group transfer F0-XV (xem [[stub_qc_uid_group]] R002).

### Luồng chuẩn (Happy Path) — Update 10-05-2026 auto inherit
1. User thiết lập tiêu chí với `Phân loại = Lỗi 4 điểm` → nhấn `Tạo` → màn thiết lập nội dung 4 điểm mở (R037).
2. User cấu hình 4 loại lỗi + hệ số.
3. Lưu tiêu chí.
4. Khi assign tiêu chí cho SKU `SP-X` → hệ thống auto load thiết lập 4 điểm cho `SP-X`, không cần config lại (R037).
5. Tương tự cho `Theo từng bước` (R038).

### Luồng chuẩn (Happy Path) — Update 05-08-2025 inactive tiêu chí impact
1. Tiêu chí `T-001` đang active được dùng trong setup SKU `SP-A` (status `Open`).
2. QC inactive `T-001` (confirm dialog DEACTIVATE).
3. Hệ thống xử lý (R029):
   - SKU `SP-A` status `Open` → `T-001` **xoá khỏi danh sách** tiêu chí cho `SP-A`.
   - Setup SKU `SP-B` status `Approved` → `T-001` **không hiển thị** cho `SP-B` (vẫn lưu).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — Update master tiêu chí:** chọn `Thao tác` cho 1 tiêu chí → cập nhật info (Mã không sửa được) (R005).
- **A2 — Active/Inactive:** confirm dialog yêu cầu xác nhận (R004).
- **A3 — SKU active + cố tạo lại setup:** ERR-CRS-003 (R015).
- **A4 — SKU setup status = New → cho update + xoá button:** chỉ status New mới cho thao tác đầy đủ (R014).
- **A5 — Tiêu chí Loại đánh giá = Theo điều kiện + Phân loại = Bình thường:** disable Phân loại edit khi Loại = Đạt/Không đạt (R022).

### Luồng ngoại lệ (Exception Paths)
- **E1 — Mã tiêu chí trùng:** ERR-CRS-001 (R006).
- **E2 — Tên tiêu chí trùng:** ERR-CRS-002 (R007).
- **E3 — Field bắt buộc trống:** `Thông tin này là bắt buộc.` (R015-R017).
- **E4 — SKU đã setup Active:** ERR-CRS-003 (R015).
- **E5 — SKU đã setup khi nhấn Tiếp tục:** ERR-CRS-004 (R019).
- **E6 — Tiêu chí đã có trong danh sách SKU:** ERR-CRS-005 (R027).
- **E7 — Import file: 4 messages tương ứng:** ERR-CRS-006..009 (R009).
- **E8 — Phase này không hỗ trợ Khi nhận PO + Ngẫu nhiên:** UI block (R016, R017).
- **E9 — Operator Trong khoảng giá trị từ ≥ đến:** validation chưa nêu — Q-002.
- **E10 — Công thức không hợp lệ → chữ đỏ:** không cho Lưu (R033).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Filter `Đến ngày` | date | ❌ | ≥ `Từ ngày` (raw L141 typo "đến ngày ≥ đến ngày" → spec interpret là "đến ngày ≥ từ ngày" — Q-016) |
| `Mã tiêu chí` | string | ✅ | Unique trên hệ thống; không sửa được sau khi tạo |
| `Tên tiêu chí` | string | ✅ | Unique trên hệ thống |
| Active default | rule | ✅ | Tiêu chí mới tạo / SKU setup mới → status `Active` |
| Active/Inactive confirm | rule | ✅ | Bắt buộc confirm dialog VN+EN |
| Import 4 validations | rule | ✅ | Trùng hệ thống / Trùng file import × Mã/Tên |
| Mutex 1 SKU 1 setup active | rule | ✅ | Phải inactive cái cũ trước khi active cái mới |
| `Thời điểm đánh giá` enum | enum | ✅ | {`Khi nhận PO` (chưa hỗ trợ phase này), `Sau khi nhận PO`} |
| `Tần suất đánh giá` enum | enum | ✅ | {`Tất cả PO` (auto VAS), `Ngẫu nhiên` (chưa hỗ trợ phase này)} |
| Mutex SKU setup status New | rule | ✅ | Update/Xoá thao tác chỉ cho status New |
| `Yêu cầu chụp hình` | enum | ✅ | {Yes, No} |
| `Hình chụp mẫu` | image | ❌ | Max 3 hình |
| `Loại đánh giá` = Đạt/Không đạt → Phân loại = Bình thường | rule | ✅ | Mặc định Bình thường, không cho edit |
| Operator `=`, `>`, `>=`, `<`, `<=` | rule | ✅ | `Giá trị` số > 0 + `Đơn vị tính` text bắt buộc; `=` có `Sai số cho phép` optional > 0 |
| Operator `Trong khoảng` | rule | ✅ | `Giá trị từ…đến` số > 0 + `Đơn vị tính` bắt buộc |
| Operator `Công thức` | rule | ⚠️ | Pending rules Dev (Q-001) |
| 1 tiêu chí 1 điều kiện | rule | ✅ | Add 1 → nút `+` disable; xoá → hiện lại |
| `Phân loại` enum | enum | ✅ | {`Bình thường`, `Lỗi 4 điểm`, `Theo từng bước`} |
| `Bước` (Step by step) | integer | ✅ | 1-10; chọn 1 → disable cho Step khác |
| `Ghi nhận kết quả` enum | enum | ✅ | {`Không`, `Nhập giá trị`, `Đạt/Không đạt`} |
| `Từ khoá` | string | ⚠️ | Show nếu Ghi nhận ≠ `Không`; auto in hoa; no space; allow `_-.` |
| `Công thức` validity | rule | ✅ | Kiểm tra định dạng: xanh OK; đỏ không cho Lưu |
| Lưu (Step by step + 4 points) | rule | ✅ | Chỉ hiện khi ≥ 1 bước/nội dung + công thức nếu nhập phải hợp lệ |
| Tiêu chí inactive impact (05-08-2025) | rule | ✅ | SKU setup `Open/Waiting for Approval` → xoá tiêu chí inactive; `Approved` → ẩn (lưu) |
| QC xã vải flag (11-02-2026) | boolean | ✅ | Bổ sung field khi tạo/cập nhật tiêu chí |
| Auto inherit (10-05-2026) | rule | ✅ | 4 điểm + Theo từng bước auto load thiết lập khi assign SKU |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-CRS-001 | Validation | Mã tiêu chí đã tồn tại khi tạo | `Mã tiêu chí đã tồn tại.` | `The criteria code already exists.` | 07105#L178-L179 |
| ERR-CRS-002 | Validation | Tên tiêu chí đã tồn tại khi tạo | `Tên tiêu chí đã tồn tại.` | `The criteria name already exists.` | 07105#L185-L189 |
| ERR-CRS-003 | Validation | SKU đã setup Active khi chọn SP | `SKU 422280022 đã tồn tại và đang hoạt động trên hệ thống.` | `SKU 422280022 already exists and is active in the system.` | 07105#L305-L311 |
| ERR-CRS-004 | Validation | SKU đã setup Active khi click Tiếp tục | `SKU đã được thiết lập và đang hoạt động.` | `SKU has been set up and is currently active` | 07105#L345-L348 |
| ERR-CRS-005 | Validation | Tiêu chí đã có trong danh sách khi Add | `Tiêu chí đã tồn tại trong danh sách.` | `Criteria already exists in the list.` | 07105#L425-L426 |
| ERR-CRS-006 | Validation | Import — Mã tiêu chí đã tồn tại trên hệ thống | `Mã tiêu chí đã tồn tại trên hệ thống thống` (typo lặp `thống thống` — Q-003) | `The criteria code already exists in the systems.` | 07105#L203-L204 |
| ERR-CRS-007 | Validation | Import — Mã tiêu chí đã tồn tại trong file import | `Mã tiêu chí đã tồn tại trong file import` | `The criteria code already exists in the template import.` | 07105#L205-L206 |
| ERR-CRS-008 | Validation | Import — Tên tiêu chí đã tồn tại trên hệ thống | `Tên tiêu chí đã tồn tại trên hệ thống thống` (typo Q-003) | `The criteria name already exists in the systems.` | 07105#L207-L208 |
| ERR-CRS-009 | Validation | Import — Tên tiêu chí đã tồn tại trong file import | `Tên tiêu chí đã tồn tại trong file import` | `The criteria name already exists in the template import.` | 07105#L209-L210 |
| ERR-CRS-010 | Validation | Field bắt buộc trống (SP, Thời điểm, Tần suất) | `Thông tin này là bắt buộc.` | `This information is required.` | 07105#L300-L330 |
| MSG-CRS-011 | Confirm | Deactivate tiêu chí | (raw chỉ có EN) | `Do you want to DEACTIVATE criterion 1001?` | 07105#L158-L159 |
| MSG-CRS-012 | Confirm | Activate tiêu chí | (raw chỉ có EN) | `Do you want to ACTIVATE criterion 1001?` | 07105#L159-L160 |
| MSG-CRS-013 | Confirm | Deactivate setup by SKU | (raw chỉ có EN) | `Do you want to DEACTIVATE setup by SKU 422280022?` | 07105#L270 |
| MSG-CRS-014 | Confirm | Activate setup by SKU | (raw chỉ có EN) | `Do you want to ACTIVATE setup by SKU 422280022?` | 07105#L271 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Tạo tiêu chí valid**
  - **Given:** Master tiêu chí trống.
  - **When:** User tạo `T-001 / Kiểm tra ngoại quan / Optional desc`.
  - **Then:** Lưu thành công, status `Active` (R006-R008).
- **AC-02 — Mã trùng**
  - **Given:** `T-001` đã tồn tại.
  - **When:** User tạo `T-001` lần 2.
  - **Then:** ERR-CRS-001 (R006).
- **AC-03 — Tên trùng**
  - **Given:** Tên `Kiểm tra ngoại quan` đã có.
  - **When:** User tạo cùng tên.
  - **Then:** ERR-CRS-002 (R007).
- **AC-04 — Active/Inactive confirm dialog**
  - **Given:** Tiêu chí `T-001` Active.
  - **When:** User click Inactive.
  - **Then:** MSG-CRS-011 confirm dialog (R004).
- **AC-05 — Filter tên 3 ký tự**
  - **Given:** Filter nhập 2 ký tự.
  - **When:** Search.
  - **Then:** Không trigger; nhập 3+ ký tự → trigger (R002).
- **AC-06 — Filter ngày Đến < Từ**
  - **Given:** User chọn Từ `2026-05-30`.
  - **When:** Chọn Đến `2026-05-29`.
  - **Then:** Validation block (R002).
- **AC-07 — Import — mã trùng hệ thống**
  - **Given:** File import có mã trùng hệ thống.
  - **When:** Upload + validate.
  - **Then:** ERR-CRS-006 (R009).
- **AC-08 — Setup SKU 1 active mutex**
  - **Given:** SKU `SP-A` có setup Active.
  - **When:** User cố tạo setup mới cho `SP-A`.
  - **Then:** ERR-CRS-003 (R013, R015).
- **AC-09 — Phase này không hỗ trợ Khi nhận PO**
  - **Given:** Step 1 form mở.
  - **When:** User chọn `Thời điểm = Khi nhận PO`.
  - **Then:** UI block / disabled (R016).
- **AC-10 — Phase này không hỗ trợ Ngẫu nhiên**
  - **Given:** Step 1 form mở.
  - **When:** User chọn `Tần suất = Ngẫu nhiên`.
  - **Then:** UI block / disabled (R017).
- **AC-11 — Hình mẫu max 3**
  - **Given:** Step 2 form mở.
  - **When:** User upload 3 hình mẫu.
  - **Then:** Block thêm; UI disable button upload (R021).
- **AC-12 — Loại = Đạt/Không đạt → Phân loại = Bình thường disable**
  - **Given:** Loại = `Đạt/Không đạt`.
  - **When:** User xem Phân loại.
  - **Then:** Value = `Bình thường`, không cho edit (R022).
- **AC-13 — Operator `=` thêm field `Sai số cho phép`**
  - **Given:** Loại = Theo điều kiện, Operator = `=`.
  - **When:** Form mở.
  - **Then:** Hiện field `Sai số cho phép` (số > 0, optional) (R023).
- **AC-14 — Operator `Trong khoảng` 2 giá trị**
  - **Given:** Operator = `Trong khoảng`.
  - **When:** User nhập từ 80, đến 120 đơn vị kg.
  - **Then:** Pass (R023).
- **AC-15 — 1 tiêu chí 1 điều kiện — nút + disable**
  - **Given:** User đã add 1 điều kiện.
  - **When:** Xem nút `+`.
  - **Then:** Disable; chỉ khi xoá điều kiện → enable lại (R025).
- **AC-16 — Tiêu chí duplicate trong danh sách SKU**
  - **Given:** SKU `SP-A` đã có tiêu chí `T-001`.
  - **When:** User add `T-001` lần 2.
  - **Then:** ERR-CRS-005 (R027).
- **AC-17 — Yêu cầu duyệt → status Chờ duyệt**
  - **Given:** Setup SKU đầy đủ.
  - **When:** User click `Yêu cầu duyệt` / `Hoàn thành`.
  - **Then:** Status setup SKU = `Chờ duyệt (Waiting for Approval)` (R028).
- **AC-18 — Update 05-08-2025 SKU Open inactive tiêu chí**
  - **Given:** SKU `SP-A` setup status `Open`, có tiêu chí `T-001` active.
  - **When:** QC inactive `T-001`.
  - **Then:** `T-001` xoá khỏi danh sách tiêu chí của `SP-A` (R029).
- **AC-19 — Update 05-08-2025 SKU Approved inactive tiêu chí**
  - **Given:** SKU `SP-B` setup status `Approved`, có `T-001` active.
  - **When:** QC inactive `T-001`.
  - **Then:** `T-001` không hiển thị cho `SP-B` (nhưng vẫn lưu) (R029).
- **AC-20 — Update 17-09-2025: auto chuyển màn step setup**
  - **Given:** User add tiêu chí với phân loại `Theo từng bước`.
  - **When:** Sau khi add.
  - **Then:** Tự động chuyển sang màn thiết lập các bước (R030).
- **AC-21 — Step number max 10**
  - **Given:** Step setup mở.
  - **When:** User cố nhập Step = 11.
  - **Then:** Block; chỉ cho 1-10 (R031).
- **AC-22 — Step số đã chọn disable**
  - **Given:** Step 1 đã chọn.
  - **When:** User mở dropdown cho Step 2.
  - **Then:** Số 1 disable không cho chọn lại (R031).
- **AC-23 — Từ khoá auto in hoa + no space**
  - **Given:** User nhập `abc def`.
  - **When:** Hệ thống xử lý.
  - **Then:** Field hiển thị `ABCDEF` (in hoa + bỏ space) (R032).
- **AC-24 — Công thức hợp lệ chữ xanh**
  - **Given:** User nhập công thức.
  - **When:** Click `Kiểm tra định dạng`.
  - **Then:** Nếu hợp lệ → text chuyển xanh lá; không hợp lệ → đỏ (R033).
- **AC-25 — Lưu không show khi chưa setup bước**
  - **Given:** Step setup mở, chưa nhập bước nào.
  - **When:** User xem nút Lưu.
  - **Then:** Lưu không show (R033).
- **AC-26 — Lưu validate công thức 1 lần nữa**
  - **Given:** User nhập công thức, chưa click Kiểm tra định dạng.
  - **When:** User click Lưu.
  - **Then:** Hệ thống auto validate công thức trước khi lưu (R033).
- **AC-27 — Update 27-09-2025: Lỗi 4 điểm form không có Step number**
  - **Given:** User add tiêu chí phân loại `Lỗi 4 điểm`.
  - **When:** Form mở.
  - **Then:** Form giống Theo từng bước nhưng không có field `Step` (R035).
- **AC-28 — Update 11-02-2026 QC xã vải khi tạo tiêu chí**
  - **Given:** User tạo mới tiêu chí.
  - **When:** Form mở.
  - **Then:** Field `QC xã vải` hiện thêm (R036).
- **AC-29 — Update 10-05-2026: auto inherit 4 điểm khi assign SKU**
  - **Given:** Tiêu chí `T-4P` (4 điểm) đã setup nội dung.
  - **When:** Assign `T-4P` cho SKU `SP-X`.
  - **Then:** Hệ thống auto load thiết lập 4 điểm cho `SP-X`, không cần config lại (R037).
- **AC-30 — Update 10-05-2026: auto inherit Theo từng bước khi assign SKU**
  - **Given:** Tiêu chí `T-Step` (theo bước, 3 bước) đã setup.
  - **When:** Assign cho SKU `SP-Y`.
  - **Then:** Auto load 3 bước cho `SP-Y` (R038).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R024 | Công thức rules — raw chỉ nói "sẽ bổ sung rules sau khi trao đổi với Dev". Hiện đã có rules chưa? Cú pháp công thức (operators, functions, variables)? | Dev | Open | | | |
| Q-002 | R023 | Operator `Trong khoảng` — validation `Giá trị từ ≥ đến` chưa được nêu rõ. Có block không? Verbatim message? | PO/UX | Open | | | |
| Q-003 | ERR-CRS-006, ERR-CRS-008 | Raw VN có typo `trên hệ thống thống` (lặp `thống thống`). Fix trong v2.0 hay giữ verbatim? | PO/UX | Open | | | |
| Q-004 | R016 | "Khi nhận PO chưa hỗ trợ ở phase này" — khi nào hỗ trợ? Phase 2 timeline? | PO | Open | | | |
| Q-005 | R017 | "Ngẫu nhiên chưa hỗ trợ ở phase này" — tương tự Q-004. | PO | Open | | | |
| Q-006 | R026 | Phân loại 3 values (Bình thường/Lỗi 4 điểm/Theo từng bước) — có thể thêm phân loại khác trong tương lai? Configurable hay hard-coded? | PO | Open | | | |
| Q-007 | R029 | "SKU Approved status" — khi tiêu chí bị inactive thì ẩn nhưng vẫn lưu — có UI nào để xem lại tiêu chí đã ẩn (vd audit log)? | PO/UX | Open | | | |
| Q-008 | R031 | Step number 1-10 hard limit — vì sao 10? Có thể configurable? | PO | Open | | | |
| Q-009 | R032 | Từ khoá ký tự đặc biệt allow `_-.` — có ký tự nào khác allow không (vd `+`, `/`)? Vì sao restrict 3 cái này? | PO/Dev | Open | | | |
| Q-010 | R033 | "Lưu chỉ hiện khi có 1 bước + công thức hợp lệ" — nếu tiêu chí chỉ có 1 bước + không nhập công thức → button Lưu hiện không? | PO | Open | | | |
| Q-011 | R035, R031 | Form Lỗi 4 điểm giống Theo từng bước nhưng không có Step. Vậy hệ số 4 điểm (cho lỗi 1/2/3/4 điểm) setup ở đâu? Raw không nêu rõ. | PO | Open | | | |
| Q-012 | R037 | Update 10-05-2026 — auto inherit. Nếu user muốn override per SKU (vd tiêu chí 4 điểm có hệ số khác cho 1 SKU đặc biệt) → cho phép không? | PO | Open | | | |
| Q-013 | R029 | Khi tiêu chí inactive → tự xoá khỏi SKU `Open/Waiting for Approval`. Sau khi user reactivate tiêu chí → có tự thêm lại vào SKU không, hay user phải add manual? | PO | Open | | | |
| Q-014 | R013 | "1 thời điểm 1 SKU không thể cùng active 2 thiết lập" — có ngoại lệ nào không (vd 2 thiết lập cho 2 phase khác nhau)? | PO | Open | | | |
| Q-015 | R028 | Sau khi `Yêu cầu duyệt` → status Chờ duyệt, ai có quyền approve/reject? (xem [[stub_qc_criteria_approval]]). | PO | Open | | | |
| Q-016 | R002, BR | Raw L141 có typo `"Đến ngày phải lớn hơn hoặc bằng đến ngày"` (lặp "đến ngày"). Spec interpret là `Đến ngày ≥ Từ ngày` (hợp lý về nghiệp vụ), nhưng cần PO confirm ý định đúng là `Đến ngày ≥ Từ ngày` hay logic khác? | PO/UX | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-04..S-06, S-09..S-12, S-23, S-34, S-35 (multi-range) | 1.5 (stub) | 1.5 | All R + AC | Draft |
| CHG-002 | Add | Update 05-08-2025: tiêu chí inactive impact theo state SKU setup | (trước 1.5) | 1.5 | R029 | Done |
| CHG-003 | Add | Update 17-09-2025: thiết lập đánh giá từng bước với 10 step max + Từ khoá + Công thức | (trước 1.5) | 1.5 | R030-R033 | Done |
| CHG-004 | Add | Update 27-09-2025: thiết lập nội dung đánh giá cho tiêu chí Lỗi 4 điểm | (trước 1.5) | 1.5 | R034, R035 | Done |
| CHG-005 | Add | Update 11-02-2026: bổ sung `QC xã vải` khi tạo/cập nhật tiêu chí | (trước 1.5) | 1.5 | R036 | Done |
| CHG-006 | Add | Update 10-05-2026: auto inherit thiết lập tiêu chí 4 điểm + Theo từng bước khi assign SKU | (trước 1.5) | 1.5 | R037, R038 | Done |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_qc_criteria_setup | test_stub_qc_criteria_setup | Add (chờ Gate 1B) | [[stub_qc_criteria_sku]] (chi tiết Setup SKU + form add tiêu chí), [[stub_qc_criteria_approval]] (Duyệt/Từ chối setup), [[stub_qc_evaluation_mobile]] / [[stub_qc_evaluation_manual]] (tiêu chí dùng đánh giá), [[stub_qc_uid_group]] (QC xã vải) | Q-001..Q-015 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R038, AC-01..AC-30 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-015 |

## 🚧 Blocked Coverage

- R024 — chờ Q-001 (Công thức rules Dev)
- R023 — chờ Q-002 (Trong khoảng validation)
- ERR-CRS-006, ERR-CRS-008 — chờ Q-003 (typo `thống thống` fix)
- R016 — chờ Q-004 (Khi nhận PO phase 2)
- R017 — chờ Q-005 (Ngẫu nhiên phase 2)
- R026 — chờ Q-006 (Phân loại configurable)
- R029 — chờ Q-007, Q-013 (UI ẩn tiêu chí + reactivate behavior)
- R031 — chờ Q-008 (Step max 10 configurable)
- R032 — chờ Q-009 (Từ khoá special chars)
- R033 — chờ Q-010 (Lưu rule edge)
- R035 — chờ Q-011 (hệ số 4 điểm setup)
- R037 — chờ Q-012 (override per SKU)
- R013 — chờ Q-014 (mutex active 2 setup edge)
- R028 — chờ Q-015 (approval flow scope)
- R002, BR `Filter Đến ngày` — chờ Q-016 (raw typo L141 interpretation: `Đến ngày ≥ Từ ngày` hay logic khác)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 22:00:00 | v1.1 | Refine stub → full spec: 38 R-ID, 30 AC, 26 BR, 14 messages (10 verbatim VN+EN, 4 verbatim EN only), 15 questions Open. `partial_read: false`. | refine-batch-5-2026-05-30 |
| 2026-05-31 17:30:00 | v1.2 | FIX-002 (refiner batch-4): R002 Testable ✅→⚠️; thêm Q-016 trace raw typo L141 `Đến ngày ≥ Từ ngày`; cập nhật BR Filter + Blocked Coverage. | refiner-spec-scoped-batch-4 |
