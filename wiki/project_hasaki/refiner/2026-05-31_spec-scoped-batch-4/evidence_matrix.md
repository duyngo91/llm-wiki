---
session: "2026-05-31"
batch: spec-scoped-batch-4
generated_at: "2026-05-31 23:10:00+07:00"
---

# Evidence Matrix — spec-scoped-batch-4

> Per-claim verification (L_inference). Format: Raw evidence (path#line) | Wiki claim (path#line) | Status | Action.
>
> Verify rule: 100% claims mapped đến sections có flag critical (enum / state_transition / formula / business_rule / error_messages / validation_rule); 1/5 sampling cho non-critical.
> Raw-first: đã đọc raw `07105_Quality_Control_Docs_ver1.5.md` L102-124, L131-220, L226-348, L357-437, L443-525, L1078-1172, L1304-1321 TRƯỚC khi đối chiếu spec.
> PATCH-001 applied: mọi spec text khác raw verbatim PHẢI có Q-ID + raw quote.

---

## stub_qc_overview

Tất cả claim là metadata/reference-link — không có flag critical business. Verify 100% (spec nhỏ, 4R).

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07105#L102-L110` — heading `Thuật ngữ & viết tắt`; table header `# Code \| Name \| \| Desciption`; 5 dòng (1.-5.) đều rỗng | `stub_qc_overview.md` R001 | `SUPPORTED` | Keep. Typo raw `Desciption` (L104) đã flag Q-003; bảng rỗng đã flag Q-004 |
| `07105#L112-L113` — `Quy trình (Workflow)` - Link: `https://drive.hasaki.vn/d/d45615dafe0b441785ff/` | `stub_qc_overview.md` R002 | `SUPPORTED` | Keep — URL khớp verbatim |
| `07105#L115-L118` — `Giao diện (Wireframe)` - Link figma `...34.-Quality-Control?node-id=366-229&t=dvLSI74zHLKyyM0v-1` | `stub_qc_overview.md` R003 | `SUPPORTED` | Keep — URL + node-id khớp verbatim |
| `07105#L124` — heading `Yêu cầu chức năng` dẫn vào `Thiết lập tiêu chí` (L125) | `stub_qc_overview.md` R004 | `SUPPORTED` | Keep — heading + vị trí khớp |
| `07105#L102-L110` | `stub_qc_overview.md` AC-01 (bảng terms 5 row rỗng, header `# Code\|Name\|Desciption`) | `SUPPORTED` | Keep — 5 row rỗng khớp raw L106-110 |
| `07105#L112-L113` | `stub_qc_overview.md` AC-02 (link Drive) | `SUPPORTED` | Keep |
| `07105#L115-L118` | `stub_qc_overview.md` AC-03 (link Figma node 366-229) | `SUPPORTED` | Keep |
| `07105#L124` | `stub_qc_overview.md` AC-04 (heading Yêu cầu chức năng) | `SUPPORTED` | Keep |
| `07105#L102-L110` | `stub_qc_overview.md` BR `Bảng thuật ngữ` (trống, cần bổ sung Q-004) | `SUPPORTED` | Keep |
| `07105#L112-L113` | `stub_qc_overview.md` BR `Workflow link` (URL Drive Hasaki) | `SUPPORTED` | Keep |
| `07105#L115-L118` | `stub_qc_overview.md` BR `Wireframe link` (Figma `34. Quality Control`) | `SUPPORTED` | Keep |

**Kết quả spec:** 11/11 SUPPORTED. 0 violation.

---

## stub_qc_criteria_setup

Verify 100% critical sections: enum (R011/R016/R017/R022/R026/R031), state_transition (R028/R029), formula (R024/R032/R033), error_messages (R006/R007/R009/R015/R016/R019/R027 → ERR-CRS-001..010, MSG-CRS-011..014), business_rule (R004/R005/R013/R014/R022/R025/R037/R038). Sampling 1/5 cho UI/navigation thuần.

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07105#L126-L128` — `Menu: Inbound / Quality control` o `Tab Thiết lập tiêu chí (Setup criteria)` | R001 | `SUPPORTED` | Keep |
| `07105#L131-L143` — Filter: `Mã, tên tiêu chí` tìm gần đúng nhập từ 3 ký tự; `Đang hoạt động`; `Từ ngày…đến ngày` tìm theo ngày tạo; "Đến ngày phải lớn hơn hoặc bằng **đến ngày**" (L141 — typo self-reference); mặc định không chọn ngày | R002 (spec ghi `Đến ngày ≥ Từ ngày`) | `UNCLEAR` | Raw L141 typo "đến ngày ≥ đến ngày"; spec interpret thành "Đến ngày ≥ Từ ngày" (reading hợp lý) nhưng **chưa có Q-ID** trace theo PATCH-001 → FIX-002 thêm Q vào `Câu hỏi chưa rõ` + Blocked Coverage |
| `07105#L144-L170` — Listing cột: `TT`(tăng dần), `Mã tiêu chí`(theo user nhập), `Tên tiêu chí`, `Mô tả`, `Hướng dẫn`, `Đang hoạt động`(default Active), `Người tạo`(email + `YYYY-MM-DD HH:SS`), `Người cập nhật`, `Thao tác` | R003 | `SUPPORTED` | Keep — đủ cột + format thời gian khớp |
| `07105#L158-L160` — `Do you want to DEACTIVATE criterion 1001?` / `Do you want to ACTIVATE criterion 1001?` (xác nhận khi Active/Inactive) | R004 + MSG-CRS-011/012 | `SUPPORTED` | Keep — verbatim EN khớp; raw chỉ có EN (spec ghi đúng) |
| `07105#L167-L170` — Thao tác: cập nhật info, "Không cho cập nhật mã tiêu chí", còn lại được phép cập nhật | R005 | `SUPPORTED` | Keep |
| `07105#L171-L179` — Tạo: `Mã tiêu chí` Bắt buộc, không trùng → VN `Mã tiêu chí đã tồn tại.` EN `The criteria code already exists.` | R006 + ERR-CRS-001 | `SUPPORTED` | Keep — verbatim VN+EN khớp L178-179 |
| `07105#L180-L189` — `Tên tiêu chí` Bắt buộc, không trùng → VN `Tên tiêu chí đã tồn tại.` EN `The criteria name already exists.` | R007 + ERR-CRS-002 | `SUPPORTED` | Keep — verbatim khớp L185-189 |
| `07105#L190-L198` — `Mô tả` không bắt buộc; `Hướng dẫn` không bắt buộc; buttons `Đóng`/`Lưu và đóng`/`Lưu và tiếp tục` (clear để tạo tiếp) | R008 | `SUPPORTED` | Keep |
| `07105#L199-L211` — Import: Template + Validate, 4 message. Raw L203-204 `...trên hệ thống thống` (typo lặp); L205-206 `...trong file import`; L207-208 `...trên hệ thống thống`; L209-210 `...trong file import`. Page import dùng chung | R009 + ERR-CRS-006..009 | `SUPPORTED` | Keep — verbatim khớp gồm typo `thống thống` (đã flag Q-003); EN `the systems.` / `the template import.` khớp |
| `07105#L217-L220` — `Menu: Inbound / Quality control` o `Tab Thiết lập SKU` | R010 | `SUPPORTED` | Keep |
| `07105#L226-L250` — Filter SKU: `SKU/Barcode/Tên SP`, `Danh mục`, `Thương hiệu`, `Đang hoạt động`(default không chọn; `Đang hoạt động`/`Ngưng hoạt động`), `Trạng thái`, `Thời điểm đánh giá`(`Khi nhận PO`/`Sau khi nhận PO`), `Tần suất đánh giá`(`Tất cả PO`/`Ngẫu nhiên`), `Từ ngày…đến ngày` | R011 | `SUPPORTED` | Keep — enum values khớp đủ |
| `07105#L253-L283` — Listing SKU cột: `TT`, `Sản phẩm`(`SKU – Tên sản phẩm`), `Danh mục`, `Thương hiệu`, `Thời điểm đánh giá`, `Tần suất đánh giá`, `Số lượng tiêu chí`, `Đang hoạt động`, `Người tạo`, `Người cập nhật`, `Trạng thái`, `Thao tác` | R012 | `SUPPORTED` | Keep — đủ cột |
| `07105#L267-L274` — `Do you want to DEACTIVATE setup by SKU 422280022?` / `Do you want to ACTIVATE...`; "tại 1 thời điểm 1 SKU không thể cùng active 2 thiết lập, phải inactive cái cũ trước" | R013 + MSG-CRS-013/014 | `SUPPORTED` | Keep — verbatim khớp; mutex rule khớp L272-273 |
| `07105#L281-L288` — Thao tác 3 button: cập nhật (chỉ status `Mới (New)`), xem chi tiết/Duyệt-Từ chối, xoá (chỉ status `Mới (New)`) | R014 | `SUPPORTED` | Keep — điều kiện "chỉ show cho status New" khớp |
| `07105#L289-L311` — `Sản phẩm` Bắt buộc, tìm SKU/barcode/tên; chưa chọn → VN `Thông tin này là bắt buộc.`; SKU Active → VN `SKU 422280022 đã tồn tại và đang hoạt động trên hệ thống.` EN `SKU 422280022 already exists and is active in the system.` | R015 + ERR-CRS-003/010 | `SUPPORTED` | Keep — verbatim khớp L300-311 |
| `07105#L312-L323` — `Thời điểm đánh giá` Bắt buộc; values `Khi nhận PO / Receiving PO (chưa hỗ trợ ở phase này)`, `Sau khi nhận PO / After receive of PO` | R016 | `SUPPORTED` | Keep — modifier "(chưa hỗ trợ ở phase này)" giữ nguyên L321-322 |
| `07105#L324-L338` — `Tần suất đánh giá` Bắt buộc; `Tất cả PO`(tự động sinh VAS sau khi kết thúc phiên nhận), `Ngẫu nhiên`(user tự tạo phiên khi có nhu cầu, chưa hỗ trợ phase này) | R017 | `SUPPORTED` | Keep — modifier + behavior VAS giữ nguyên L334-338 |
| `07105#L339-L344` — `Ghi chú` không bắt buộc; `Đóng`; `Tiếp tục` qua màn thiết lập tiêu chí cho SKU | R018 | `SUPPORTED` | Keep |
| `07105#L345-L348` — `Tiếp tục`: SKU đã thiết lập + active → VN `SKU đã được thiết lập và đang hoạt động.` EN `SKU has been set up and is currently active` | R019 + ERR-CRS-004 | `SUPPORTED` | Keep — verbatim khớp |
| `07105#L357-L368` — Form fields đọc Step 1 + `Tiêu chí đánh giá` Bắt buộc, load tất cả tiêu chí, tìm theo mã/tên nhập từ 3 ký tự | R020 | `SUPPORTED` | Keep |
| `07105#L369-L374` — `Yêu cầu chụp hình` Bắt buộc chọn, `Yes/No`; `Hình chụp mẫu` không bắt buộc, upload tối đa **3 hình** | R021 | `SUPPORTED` | Keep — "max 3 hình" khớp L374 |
| `07105#L375-L380` — `Loại đánh giá`: `Đạt/Không đạt`(mặc định; phân loại = `Bình thường` và **không cho chỉnh sửa**); `Theo điều kiện` | R022 | `SUPPORTED` | Keep — default + lock Bình thường khớp L377-379 |
| `07105#L380-L406` — operators `=`,`>`,`>=`,`<`,`<=`: `Giá trị` bắt buộc số >0, `Đơn vị tính` text bắt buộc; `=` thêm `Sai số cho phép`(không bắt buộc, số >0); `Trong khoảng`: `Giá trị từ…đến` bắt buộc số >0 + `Đơn vị tính` bắt buộc | R023 + AC-13/AC-14 | `SUPPORTED` | Keep — đủ operator + field rules |
| `07105#L407-L409` — `Công thức`: thiết lập công thức, trả kết quả, so sánh điều kiện; "sẽ bổ sung rules sau khi trao đổi với Dev" | R024 | `SUPPORTED` | Keep — pending đã flag Q-001 đúng; không suy diễn rule |
| `07105#L410-L413` — "1 tiêu chí chỉ hỗ trợ 1 điều kiện duy nhất"; thêm 1 → nút `Thêm (+)` disable; xoá → hiện lại | R025 | `SUPPORTED` | Keep — verbatim logic khớp |
| `07105#L414-L420` — `Phân loại`: `Bình thường / Normal`, `Lỗi 4 điểm / 4 points error`, `Theo từng bước / Step by step` | R026 | `SUPPORTED` | Keep — 3 enum values đủ |
| `07105#L421-L427` — `Mô tả` không bắt buộc; `Thêm` add tiêu chí; trùng → VN `Tiêu chí đã tồn tại trong danh sách.` EN `Criteria already exists in the list.` | R027 + ERR-CRS-005 | `SUPPORTED` | Keep — verbatim khớp L425-426 |
| `07105#L428-L432` — `Đóng`; `Lưu` (lưu để tiếp tục lần sau); `Yêu cầu duyệt` chọn `Hoàn thành` → chuyển `Chờ duyệt (Waiting for Approval)` | R028 + AC-17 | `SUPPORTED` | Keep — state transition khớp |
| `07105#L433-L437` — SKU `Open`/`Waiting for Approval` + tiêu chí inactive → xoá khỏi danh sách; SKU `Approved` + tiêu chí inactive → không hiển thị (vẫn lưu) | R029 + AC-18/AC-19 | `SUPPORTED` | Keep — state transition + 2 nhánh khớp |
| `07105#L443-L450` — edit tiêu chí `type = Theo từng bước` → mở modal thiết lập bước; "khi add tiêu chí... `Theo từng bước` → tự động chuyển qua màn thiết lập các bước" | R030 + AC-20 | `SUPPORTED` | Keep |
| `07105#L451-L467` — `Bước` số `1 đến 10` (đã chọn disable); `Nội dung`; `Yêu cầu chụp hình`; `Hình ảnh mẫu`; `Ghi nhận kết quả`: `Không/No`, `Nhập giá trị/Fill value`, `Đạt/Không đạt – Passed/Failed` | R031 + AC-21/AC-22 | `SUPPORTED` | Keep — range 1-10 + enum 3 values khớp |
| `07105#L468-L475` — `Từ khoá` chỉ show nếu Ghi nhận ≠ `Không`; tự động in hoa + không cho space; cho phép `_`, `-`, `.`; `Hướng dẫn` text; `Công thức` | R032 + AC-23 | `SUPPORTED` | Keep — special chars `_-.` khớp L471-472 |
| `07105#L476-L488` — `Kiểm tra định dạng`: Hợp lệ chữ xanh lá / Không hợp lệ chữ đỏ; `Đóng`; `Lưu` chỉ hiện khi ≥1 bước + công thức (nếu nhập) hợp lệ; chưa check format → khi Lưu validate thêm 1 lần | R033 + AC-24/AC-25/AC-26 | `SUPPORTED` | Keep — toàn bộ logic khớp (raw có typo `vaidate`/`định đạng` L488 nhưng không ảnh hưởng claim) |
| `07105#L493-L499` — edit tiêu chí `type = Lỗi 4 điểm` → mở modal thiết lập nội dung; "khi thiết lập... `Lỗi 4 điểm` → tự động chuyển qua màn thiết lập các bước" | R034 | `SUPPORTED` | Keep |
| `07105#L500-L525` — Form Lỗi 4 điểm: `Tiêu chí`, `Nội dung`, `Yêu cầu chụp hình`, `Ghi nhận kết quả`, `Từ khoá`, `Hướng dẫn`, `Công thức`, `Kiểm tra định dạng`, `Đóng`, `Lưu` — **không có field Step** | R035 + AC-27 | `SUPPORTED` | Keep — "không có Step" khớp (form 4 điểm raw không có dòng `Bước`) |
| `07105#L1081-L1097` — "Bổ sung thêm thông tin `QC xã vải` (Fabric relaxation QC)... Khi tạo hay cập nhật tiêu chí" → dùng tạo yêu cầu đánh giá xã vải khi UID group TF vào `F0-XV` | R036 + AC-28 | `SUPPORTED` | Keep — khớp; cross-ref [[stub_qc_uid_group]] hợp lệ |
| `07105#L1304-L1311` — "Thiết lập tiêu chí 4 điểm khi thiết lập tiêu chí... chọn `Lỗi 4 điểm` → nhấn `Tạo` → mở màn thiết lập nội dung 4 điểm, giống setup SKU; khi assign cho SKU → hệ thống tự lấy thiết lập, không cần thiết lập lại từng SKU" | R037 + AC-29 | `SUPPORTED` | Keep — auto-inherit khớp |
| `07105#L1312-L1321` — "Thiết lập đánh giá từng bước khi thiết lập tiêu chí... `Theo từng bước` → `Tạo` → mở màn thiết lập từng bước; assign SKU → tự lấy thiết lập, không cần thiết lập lại" | R038 + AC-30 | `SUPPORTED` | Keep — auto-inherit khớp |
| (BR table — sampling) `07105#L141/L272/L375/L410/L414/L433` | BR rows (Filter Đến ngày, Mutex, Loại đánh giá, 1 điều kiện, Phân loại, inactive impact) | `SUPPORTED` | Keep — trừ BR `Filter Đến ngày` mang cùng typo issue như R002 (xem UNCLEAR ở trên, cùng FIX-002) |

**Kết quả spec:** 37/38 critical claim SUPPORTED, 1 UNCLEAR (R002 date filter typo, thiếu Q-ID theo PATCH-001). 0 INFERRED/PHANTOM/NEGATION. Error messages 14/14 verbatim khớp raw (gồm typo `thống thống` đã trace Q-003).

---

## stub_qc_uid_group

Verify 100% critical: state_transition (R002/R011), business_rule (R002/R003/R004/R007/R012/R013), validation (R006/R010), error_messages (ERR-UIG-001/002), enum/flag (R001).

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07105#L1083-L1085` — "Bổ sung thêm thông tin `QC xã vải` (Fabric relaxation QC)... Khi tạo hay cập nhật tiêu chí sẽ bổ sung thêm thông tin này" | R001 + AC-01 | `SUPPORTED` | Keep — flag QC xã vải khi tạo/cập nhật khớp. Scope (toàn bộ tiêu chí vs category Thời trang) đã flag Q-009 đúng |
| `07105#L1086-L1093` — "Thông tin này được dùng để tạo yêu cầu đánh giá xã vải... Khi UID group được TF vào location `F0-XV` bằng tính năng transfer location hoặc transfer UID group thì hệ thống tự động sinh ra 1 yêu cầu đánh giá Xã vải cho các tiêu chí có bật `QC xã vải` cho SKU" | R002 + AC-02 | `SUPPORTED` | Keep — trigger + auto-sinh khớp verbatim |
| `07105#L1090-L1093` — "VD: SKU có thiết lập 5 tiêu chí nhưng chỉ có 2 tiêu chí được bật `QC xã vải` thì chỉ sinh yêu cầu đánh giá cho 2 tiêu chí này thôi" | R003 + AC-02 | `SUPPORTED` | Keep — ví dụ 5/2 khớp verbatim |
| `07105#L1094-L1096` — "Lưu ý: Số vải (90%) còn lại được nhận vào sau khi nhận 10% và đánh giá Đạt đều phải được đánh giá qua khâu Xã vải trước khi đưa và[o] sản xuất" | R004 + AC-15 | `SUPPORTED` | Keep — 90%/10% + "đánh giá xã vải trước khi sản xuất" khớp |
| `07105#L1128-L1132` — "Khai báo số lượng cần đánh giá cho UID group (App). Menu: App / Purchase order / Quality control. Ở bước scan UID group cần đánh giá, bổ sung thông tin cập nhật số lượng cần đánh giá" | R005 + AC-05 | `SUPPORTED` | Keep — menu + bước scan khớp |
| `07105#L1133-L1134` — "Bắt buộc / Phải là số nguyên dương" | R006 | `SUPPORTED` | Keep — bắt buộc + số nguyên dương khớp |
| `07105#L1135-L1139` — "Sau khi xác nhận, hệ thống tự động trừ số lượng đã khai báo ra khỏi UID group. VD: UID group có SKU A qty 9500... khai báo 500 thì qty SKU A còn 9000" | R007 + AC-05 | `SUPPORTED` | Keep — auto trừ + ví dụ 9500/500/9000 khớp verbatim. (Rule SL > qty + rollback đã flag Q-001/Q-008 đúng) |
| `07105#L1140` — "Bổ sung thông tin này vào phần thông tin chung" | R008 + AC-10 | `SUPPORTED` | Keep — "phần thông tin chung" khớp |
| `07105#L1141-L1145` — "Chụp hình tem QC. Menu: App / Purchase order / Quality control. Sau khi hoàn thành đánh giá tất cả tiêu chí cho SKU, khi nhấn `Hoàn thành` bổ sung thêm bước chụp hình tem QC Pass/Fail để ghi nhận lên hệ thống" | R009 + AC-11 | `SUPPORTED` | Keep — trigger `Hoàn thành` + tem Pass/Fail khớp. (Pass vs Fail 1 tem hay 2 đã flag Q-005 đúng) |
| `07105#L1146-L1147` — "Bắt buộc / Chỉ cần chụp 1 hình" | R010 + AC-12 | `SUPPORTED` | Keep — bắt buộc + 1 hình khớp |
| `07105#L1153-L1158` — "Khi transfer UID group qua location xã vải (F0-XV) hoặc type location là `Xã vải` (Fabric Relaxing) bằng tính năng transfer bin, transfer bin cart, transfer vị trí trong UID group, validate: Nếu UID group đã sinh yêu cầu và được đánh giá xã vải Đạt thì bỏ qua / Nếu chưa được sinh yêu cầu thì sinh yêu cầu đánh giá theo tiêu chí xã vải" | R011 + AC-03/AC-04 | `SUPPORTED` | Keep — state transition + 3 tính năng transfer khớp verbatim (phân biệt 4 transfer đã flag Q-003 đúng) |
| `07105#L1160-L1165` — "Tiêu chí đánh giá trên SKU của PO chính phải map với tiêu chí của SKU khi đánh giá trên PO sample. SKU PO sample đánh giá chỉ đạt 4/5 tiêu chí được thiết lập nhưng BOD vẫn duyệt cho nhận hàng vào theo Lot này... thì tiêu chí đánh giá cho SKU của PO chính cũng phải dựa vào điều kiện của tiêu chí của SKU trên PO sample" | R012 + AC-14 | `SUPPORTED` | Keep — map PO chính ↔ PO sample + 4/5 + BOD duyệt khớp verbatim |
| `07105#L1166-L1168` — "VD: điều kiện đạt của tiêu chí A của SKU được thiết lập là >6, PO sample đánh giá chỉ 5.5 (Không đạt) nhưng BOD approve cho nhận Lot này, thì trên PO chính SKU này cũng chỉ cần đạt từ 5.5 là Đạt yêu cầu" | R013 + AC-14 | `SUPPORTED` | Keep — ví dụ >6 / 5.5 / "đạt từ 5.5" khớp verbatim |
| `07105#L1160-L1168` — raw chỉ nói PO chính "dựa vào điều kiện của tiêu chí trên PO sample" + 1 ví dụ (5.5). **KHÔNG** có khái niệm aggregation "thấp nhất" | BR table row `Tiêu chí PO chính map PO sample` (`stub_qc_uid_group.md#L124`): "...dùng **giá trị PO sample đạt thấp nhất** đã được approve" | `INFERRED` | Remove "thấp nhất" — raw không nêu min-aggregation. Spec đã tự generalize từ 1 ví dụ thành rule "thấp nhất". Chính Q-006 của spec đang hỏi "tổng hợp min/max?" → mâu thuẫn nội bộ. FIX-001 |
| `07105#L1133-L1134` — chỉ có "Bắt buộc / Phải là số nguyên dương", **không có text message lỗi** | ERR-UIG-001 (Message VN/EN = "raw không có verbatim — Q-002") | `UNCLEAR` | Keep row + Q-002. Spec **đúng** khi không bịa verbatim; validation tồn tại nhưng message text không có trong raw → pending source. Không phải PHANTOM (validation requirement có thật) |
| `07105#L1146-L1147` — chỉ có "Bắt buộc / Chỉ cần chụp 1 hình", **không có text message lỗi** | ERR-UIG-002 (Message VN/EN = "raw không có verbatim — Q-002") | `UNCLEAR` | Keep row + Q-002. Spec đúng khi không bịa verbatim; pending source. Không phải PHANTOM |
| `07105#L1083-L1097` (flag), `L1153-L1158` (trigger), `L1133-L1147` (validation), `L1160-L1168` (PO map) | BR rows (QC xã vải flag, Trigger sinh yêu cầu, Validation transfer, Phạm vi, 90% vải, SL cần đánh giá, Hình tem QC) | `SUPPORTED` | Keep — 7/8 BR row khớp raw; row 8 (PO chính map) là INFERRED ở trên |

**Kết quả spec:** 13 R SUPPORTED, 15 AC SUPPORTED, 7/8 BR SUPPORTED, 1 BR INFERRED ("thấp nhất"), 2 error message UNCLEAR (pending verbatim, xử lý đúng). Điểm L_structural CONDITIONAL (ERR-UIG verbatim) → resolved: spec xử lý đúng, là UNCLEAR/pending hợp lệ, KHÔNG block.

---

## Tổng hợp violation

| Spec | SUPPORTED | UNCLEAR | INFERRED | LOGIC_INFERRED | NEGATION_FLIP | PHANTOM | POTENTIAL_OMISSION | MISSING_DETAIL |
|:-----|:---------:|:-------:|:--------:|:--------------:|:-------------:|:-------:|:------------------:|:--------------:|
| stub_qc_overview | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| stub_qc_criteria_setup | 37 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| stub_qc_uid_group | 35 | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| **Tổng** | **83** | **3** | **1** | **0** | **0** | **0** | **0** | **0** |

> Note: bảng đếm theo unique claim/row critical. Nhiều AC share cùng raw evidence với R nên gộp.

