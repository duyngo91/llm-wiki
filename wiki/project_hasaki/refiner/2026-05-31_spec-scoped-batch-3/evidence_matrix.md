---
session: "2026-05-31"
batch: "spec-scoped-batch-3"
generated_at: "2026-05-31 16:40:00+07:00"
---

# Evidence Matrix — spec-scoped-batch-3

> Per-claim verification. Format: Raw evidence (path#line) | Wiki claim (path#line) | Status | Action.
>
> Verify rule: 100% claims mapped đến sections có flag critical (enum / state_transition / formula / business_rule / error_messages / validation_rule); 1/5 sampling cho non-critical.
> Anti-confirmation-bias: raw đọc TRƯỚC spec, mô tả lại bằng ngôn ngữ raw rồi mới đối chiếu claim.

---

## stub_qc_evaluation_manual

> Critical flags trong scope: has_business_rule, has_validation_rule, has_error_messages, has_enum (ADJ Require VAT), has_state_transition (UID Blocked/Damaged/Normal). Verify 100% R004-R023 + 5 messages + 22 BR.

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07105#L1023-L1024` "Tạo mới đánh giá – Manual **(bỏ)** (Xem phần update mới ... ngày 12-02-2026)" | manual.md `R001` flow cũ deprecated | `SUPPORTED` | Keep |
| `07105#L1040-L1074` Step 2 cũ (chọn PO → Bắt đầu đánh giá, info SKU/PO/SL/NCC/ghi chú/tiêu chí, max 5 hình) | manual.md `R002` flow cũ deprecated | `SUPPORTED` | Keep |
| `07105#L1078-L1080` "Update 11-02-2026 / Link mockup figma 1946-1696" | manual.md `R003` section heading marker | `SUPPORTED` | Keep |
| `07105#L1175-L1187` Step 1 mới: Tạo mới → chọn kho → tìm SP (SKU/barcode/tên) + "Chọn để tìm modal tìm kiếm mở rộng" + load 10 PO gần nhất theo kho + tìm mã PO chính xác + "Chọn Tiếp tục" + "Nếu SKU chưa thiết lập tiêu chí thì hiện thông báo" | manual.md `R004` Step 1 mới | `SUPPORTED` | Keep |
| `07105#L1189-L1200` Step 2: SKU+tên, Mã PO, Ngày nhận PO, NCC của PO, Ghi chú, UID group (bắt buộc), Số lượng cần đánh giá (bắt buộc) | manual.md `R005` Step 2 khai báo | `SUPPORTED` | Keep |
| `07105#L1201-L1205` validate: UID không tồn tại → "Mã UID không tồn tại."; SL khai báo không đủ → "Số lượng trong UID group không đủ số lượng yêu cầu."; ngược lại → bước tiếp | manual.md `R006` Step 2 validation | `SUPPORTED` | Keep |
| `07105#L1209-L1222` Step 3: Nhóm UID, SL đang có, Số lô, HSD, SL cần đánh giá, Mã PO, NCC, SP, Ghi chú, Tiêu chí đạt/không đạt + danh sách tiêu chí theo SKU | manual.md `R007` Step 3 info | `SUPPORTED` | Keep |
| `07105#L1223-L1235` Thông tin tiêu chí: Thứ tự/Tên/Mô tả/Mô tả điều kiện theo SKU/Đạt-Không đạt/Hình ảnh; Fail → required chụp + ghi chú; max 5 hình/tiêu chí | manual.md `R008` Step 3 tiêu chí | `SUPPORTED` | Keep |
| `07105#L1237-L1238` "Đánh giá ... tất cả tiêu chí → chọn Hoàn thành để xác nhận đánh giá xong" | manual.md `R009` Hoàn thành | `SUPPORTED` | Keep |
| `07105#L1242` "Update 20-04-2026" heading | manual.md `R010` section heading | `SUPPORTED` | Keep |
| `07105#L1243-L1246` "Đánh giá SKU phụ liệu (SKU thường) ... Áp dụng cho các SKU KHÔNG PHẢI là cate Thời trang (NVL) và không phải là Vải" | manual.md `R011` scope SKU phụ liệu | `SUPPORTED` | Keep |
| `07105#L1247-L1249` "nếu kết quả đánh giá cuối cùng bị Failed (có ít nhất 1 kết quả bị failed) thì hiển thị thêm màn hình để user xác nhận số lượng cần trả hàng cho NCC" | manual.md `R012` Failed trigger | `SUPPORTED` | Keep |
| `07105#L1250-L1255` EN verbatim "SKU 422280022 has evaluation criteria marked as FAILED..." + "Để sau (Later)" + "Tạo phiếu điều chỉnh (Create adjustment)" | manual.md `R013` confirm dialog | `SUPPORTED` | Keep |
| `07105#L1256-L1262` "Số lượng cần xuất trả nhà cung cấp ... Nhập số lượng cần trả; Số lượng phải nhỏ hơn số lượng nhập hàng PO; Đóng/Xác nhận" | manual.md `R014` ADJ SL validation | `SUPPORTED` | Keep |
| `07105#L1263-L1284` Adjustment: Warehouse=kho phát sinh; Type=Export; Reason=Return to vendor; Vendor=source PO; Require VAT=3 option (No / Yes VAT Hasaki xuất / Yes VAT NCC xuất); Source code=Mã PO; Required picking=No; ADJ status=Waiting for approval | manual.md `R015` ADJ fields + Require VAT enum (3 values) | `SUPPORTED` | Keep — enum verified đủ 3/3 values verbatim |
| `07105#L1286-L1291` "SKU lấy theo user request; Số lượng theo user input; VAT và Price lấy theo SKU trên Inside theo rules của **Asjustment** hiện tại" (raw typo "Asjustment") | manual.md `R016` SKU info ADJ "rules của Adjustment hiện tại" | `SUPPORTED` | Keep — typo "Asjustment"→"Adjustment" là chính tả rõ ràng; "rules ADJ hiện tại" đã có Q-011 flag verbatim/doc rules |
| `07105#L1292-L1294` "Với các SKU vải, khi đánh giá có kết quả Failed thì hệ thống sẽ tự động blocked lại tất cả các UID group của SKU nhận trong cùng PO và cùng LOT" | manual.md `R017` Blocked UID group (SKU vải, cùng PO + LOT) | `SUPPORTED` | Keep — state_transition verified verbatim |
| `07105#L1295-L1297` "chuyển Product status của các UID ... thành Damaged để không cộng vào stock Available để không thể IT" | manual.md `R018` UID → Damaged, không cộng Available, không picklist | `SUPPORTED` | Keep |
| `07105#L1298-L1299` "Khi user Un-Blocked UID group ngoài việc unbock UID group về Available thì sẽ auto chuyển UID từ Product status Damaged thành Normal" | manual.md `R019` Un-Blocked → Damaged→Normal | `SUPPORTED` | Keep |
| `07105#L1305-L1308` "Thiết lập tiêu chí 4 điểm ... nếu chọn phân loại là 'Lỗi 4 điểm' (4 points error) thì khi nhấn 'Tạo' → mở thêm màn hình ... giống với khi thiết lập tiêu chí cho SKU" | manual.md `R020` thiết lập tiêu chí 4 điểm | `SUPPORTED` | Keep |
| `07105#L1309-L1311` "Khi thiết lập tiêu chí cho SKU, nếu chọn tiêu chí 4 điểm thì hệ thống tự lấy các thiết lập ... không cần thiết lập lại cho từng SKU" | manual.md `R021` auto-inherit 4 điểm | `SUPPORTED` | Keep |
| `07105#L1312-L1315` "Thiết lập đánh giá từng bước ... nếu chọn 'Theo từng bước' (Step by step) → mở thêm màn hình ... giống thiết lập tiêu chí cho SKU" | manual.md `R022` thiết lập theo từng bước | `SUPPORTED` | Keep |
| `07105#L1320-L1321` "Khi thiết lập tiêu chí cho SKU, nếu chọn tiêu chí 'Theo từng bước' thì hệ thống tự lấy các thiết lập ... không cần thiết lập lại cho từng SKU" | manual.md `R023` auto-inherit từng bước | `SUPPORTED` | Keep |
| `07105#L1202` "Mã UID không tồn tại." | manual.md `ERR-EVM-001` VN verbatim | `SUPPORTED` | Keep — EN missing đã flag Q-004 |
| `07105#L1203-L1204` "Số lượng trong UID group không đủ số lượng yêu cầu." | manual.md `ERR-EVM-002` VN verbatim | `SUPPORTED` | Keep — EN missing đã flag Q-004 |
| `07105#L1186-L1187` "Nếu SKU chưa thiết lập tiêu chí thì hiện thông báo" (raw KHÔNG có verbatim) | manual.md `MSG-EVM-003` (raw không verbatim — Q-003) | `SUPPORTED` | Keep — đã đánh dấu missing + Q-003 đúng |
| `07105#L1250-L1253` EN verbatim only; raw KHÔNG có VN | manual.md `MSG-EVM-004` (raw không VN — Q-005) | `SUPPORTED` | Keep — VN missing đã flag Q-005 |
| `07105#L1259-L1260` "Số lượng phải nhỏ hơn số lượng nhập hàng PO" (rule, raw KHÔNG có verbatim message) | manual.md `ERR-EVM-005` (raw không verbatim — Q-006) | `SUPPORTED` | Keep — verbatim missing đã flag Q-006 đúng |
| `07105#L1128-L1147` (trong range manual L1023-L1304) "Khai báo số lượng cần đánh giá cho UID group (App)": **Bắt buộc; Phải là số nguyên dương; sau xác nhận tự động trừ SL đã khai báo khỏi UID group** (VD 9500−500=9000). "Chụp hình tem QC (App)": **bắt buộc, chỉ chụp 1 hình QC Pass/Fail khi nhấn Hoàn thành** | (KHÔNG mapped tới R-ID nào trong cả manual lẫn mobile) | `POTENTIAL_OMISSION` | Review + add — App-side UID SL auto-deduct rule + QC stamp photo rule chưa có R-ID; thuộc luồng App (mobile) nhưng nằm trong line-range manual |
| `07105#L1152-L1168` (trong range manual) "Một số lưu ý luồng mới": transfer UID group vào F0-XV tự sinh yêu cầu đánh giá Xã vải; tiêu chí SKU PO chính phải map tiêu chí SKU PO sample (BOD duyệt 4/5 → PO chính dùng điều kiện PO sample) | (KHÔNG mapped — thuộc feature xã vải / PO sample) | `MISSING_DETAIL` | Note out-of-feature; ghi cross-ref sang stub xã vải / PO sample (không phải scope manual core) |

**Manual sampling AC (non-critical UI):** AC-01..AC-25 đều trace đúng R-ID tương ứng đã verify ở trên; spot-check AC-09 (R011/R012/R013), AC-16 (R015), AC-18 (R017), AC-21 (R019) → khớp raw. `SUPPORTED`.

---

## stub_qc_evaluation_mobile

> Critical flags: has_enum (R023 19 loại lỗi), has_formula (R025/R027/R029 điểm lỗi nhân hệ số), has_business_rule, has_validation_rule, has_error_messages, has_state/color enum. Verify 100% R007, R022-R033 + enum + formula + 1 message + 12 BR.

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07105#L793-L795` "App bổ sung thêm tính năng 'Quality Control' ... Menu: **Pruchase Order** / Quality Control" (raw typo Pruchase) | mobile.md `R001` menu `Pruchase Order / Quality Control` | `SUPPORTED` | Keep — typo `Pruchase` giữ verbatim + đã flag Q-011 đúng |
| `07105#L797-L799` "Chọn kho → show các VAS có type Quality control có trạng thái Open hoặc In-Progress" | mobile.md `R002` filter VAS status | `SUPPORTED` | Keep |
| `07105#L800` "Hỗ trợ tìm kiếm theo mã PO và VAS" | mobile.md `R003` search PO/VAS | `SUPPORTED` | Keep |
| `07105#L803-L808` header: Shop, VAS, Tổng SKU, Mã PO, Tổng sản phẩm | mobile.md `R004` Step 2 header | `SUPPORTED` | Keep |
| `07105#L809-L810` "Tìm kiếm sản phẩm theo SKU, Barcode hoặc tên sản phẩm (tìm gần đúng)" | mobile.md `R005` search SP | `SUPPORTED` | Keep — "tìm gần đúng" semantics flag Q-008 đúng |
| `07105#L811-L815` danh sách SP: Tên SP, SKU–Barcode, Số lượng SP | mobile.md `R006` danh sách SP | `SUPPORTED` | Keep |
| `07105#L816-L820` (general) "Xám nhạt/Xanh dương nhạt/Xanh lá nhạt"; `07105#L893-L900` (vải) bổ sung "Xanh lá nhạt = đã đánh giá và **Đạt**" + "Cam nhạt = đã đánh giá và **Không Đạt**" | mobile.md `R007` color coding + Cam nhạt | `SUPPORTED` | Keep — enum 4 màu verified; "Cam nhạt = Không Đạt" mô tả ở section vải, Q-006 flag scope general đúng |
| `07105#L823-L830` Step 3 info: SP(SKU–Tên), PO, Số lượng, NCC (từ PO), Ghi chú default trống editable, Tiêu chí đạt, Tiêu chí không đạt | mobile.md `R008` Step 3 info | `SUPPORTED` | Keep |
| `07105#L831-L840` danh sách tiêu chí theo SKU; mỗi tiêu chí: Thứ tự/Tên/Mô tả/Mô tả điều kiện theo SKU/Hình chụp mẫu/Đạt-Không đạt | mobile.md `R009` Step 3 tiêu chí | `SUPPORTED` | Keep |
| `07105#L841-L846` "Nhập kết quả đánh giá: dành cho tiêu chí theo điều kiện, nhập >0 → Enter hoặc tích xanh → so sánh với điều kiện config → Đạt/Không đạt" | mobile.md `R010` tiêu chí theo điều kiện | `SUPPORTED` | Keep |
| `07105#L847-L853` "user có thể edit lại kết quả đánh giá theo điều kiện và xác nhận lại" | mobile.md `R011` edit kết quả | `SUPPORTED` | Keep |
| `07105#L854-L861` "Hình ảnh: theo config; Fail → required chụp + ghi chú; tối đa 5 hình/tiêu chí (nếu có yêu cầu)" | mobile.md `R012` chụp hình | `SUPPORTED` | Keep |
| `07105#L862-L863` "Đánh giá tất cả tiêu chí → chọn Hoàn thành để xác nhận đánh giá xong" | mobile.md `R013` Hoàn thành SP | `SUPPORTED` | Keep |
| `07105#L864-L868` "1 VAS có nhiều hơn 1 SP → cần đánh giá tất cả SP để hoàn thành VAS → Hoàn thành đánh giá" | mobile.md `R014` Step 4 VAS multi | `SUPPORTED` | Keep |
| `07105#L888-L892` (vải Step 2) bổ sung "Số lô", "Hạn sử dụng" | mobile.md `R015` Số lô + HSD | `SUPPORTED` | Keep |
| `07105#L902-L904` "do rules đánh giá 10% số lượng cây vải của từng lô, nên nếu 1 lô cần đánh giá 3 cây vải tương ứng 3 group UID thì hiện thành 3 dòng" | mobile.md `R016` 10% group UID → 3 dòng | `SUPPORTED` | Keep |
| `07105#L909` "Yêu cầu scan nhóm UID tương ứng với cây vải cần giá" | mobile.md `R017` scan UID group | `SUPPORTED` | Keep |
| `07105#L910-L911` "Nếu nhóm UID không tồn tại hoặc không thuộc PO và số lô được yêu cầu đánh giá hiện thông báo" | mobile.md `R018` UID invalid → thông báo lỗi | `SUPPORTED` | Keep |
| `07105#L912-L913` "Hỗ trợ suggest các nhóm UID đã nhận cho sản phẩm theo lô để user chọn nhanh" | mobile.md `R019` suggest UID | `SUPPORTED` | Keep |
| `07105#L914-L915` "Sau khi scan hoặc chọn nhóm UID hợp lệ, chọn 'Xác nhận' để qua bước tiếp theo" | mobile.md `R020` Xác nhận | `SUPPORTED` | Keep |
| `07105#L918-L928` "Ở phase này có tổng cộng 3 tiêu chí ... thông tin: Tên tiêu chí (kèm hướng dẫn mở modal), Mô tả, Điều kiện (nếu có)" | mobile.md `R021` 3 tiêu chí + info | `SUPPORTED` | Keep |
| `07105#L930-L934` "1. Kiểm tra lỗi 4 điểm: Lỗi 1 điểm (0–3"), 2 điểm (3"–6"), 3 điểm (6"–9"), 4 điểm (>9")" | mobile.md `R022` 4 mức điểm | `SUPPORTED` | Keep — boundary verbatim khớp |
| `07105#L935-L960` enum 19 loại lỗi: 1.Slub ... 19.Other (chụp đối chiếu từng dòng) | mobile.md `R023` enum 19 values | `SUPPORTED` | Keep — enum đếm đủ **19/19** values, text verbatim khớp (kể cả typo raw "16.Printing erro") |
| `07105#L961-L966` "Nhập ghi chú; Chụp hình ảnh lỗi: bắt buộc, max 3 hình; Chọn 'Xác nhận' để ghi nhận lỗi" | mobile.md `R024` ghi chú + max 3 hình | `SUPPORTED` | Keep — ghi chú optional, hình bắt buộc khớp raw |
| `07105#L967-L973` "tính: Số lỗi từng loại; Tổng điểm lỗi (chưa nhân hệ số); Tổng điểm lỗi đã nhân hệ số" | mobile.md `R025` formula tổng điểm | `SUPPORTED` | Keep — formula: raw KHÔNG nêu hệ số cụ thể; Q-004 flag đúng |
| `07105#L974` "Chọn vào icon để xem thông tin lỗi đã cập nhật trước đó" | mobile.md `R026` icon xem lỗi | `SUPPORTED` | Keep |
| `07105#L975-L982` "Hoàn thành → Kết quả = Tổng điểm lỗi đã nhân hệ số → so sánh điều kiện thiết lập → Đạt/Không đạt → ghi nhận vào kết quả bên ngoài" | mobile.md `R027` kết quả vs điều kiện | `SUPPORTED` | Keep |
| `07105#L984-L1003` "2. Kiểm tra độ co rút (step-by-step): Thứ tự bước + Tên bước (+hình mẫu), Hướng dẫn, Yêu cầu chụp hình theo thiết lập, Ghi nhận kết quả (Đạt/Không đạt hoặc nhập giá trị), Ghi chú" | mobile.md `R028` độ co rút step-by-step | `SUPPORTED` | Keep |
| `07105#L1005-L1012` "cập nhật bước → Tiếp theo; bước cuối → Hoàn thành → áp công thức thiết lập (nếu có) → tính kết quả → so sánh điều kiện → Đạt/Không đạt" | mobile.md `R029` formula step-by-step | `SUPPORTED` | Keep — công thức chi tiết flag Q-005 đúng |
| `07105#L1013-L1014` "3. Kiểm tra độ đồng màu: Thực hiện tương tự như Kiểm tra độ co rút" | mobile.md `R030` độ đồng màu | `SUPPORTED` | Keep |
| `07105#L1015-L1016` "5. Ghi nhận kết quả cuối cùng cho nhóm UID ... chọn Hoàn thành để xác nhận đánh giá xong" | mobile.md `R031` Step 5 hoàn thành | `SUPPORTED` | Keep |
| `07105#L1017-L1018` "Nếu có ít nhất 1 tiêu chí không đạt thì xem như kết quả của sản phẩm được đánh giá theo nhóm UID là Không đạt" | mobile.md `R032` ≥1 fail → UID group Không đạt | `SUPPORTED` | Keep |
| `07105#L1019` "Tiếp tục thực hiện cho các nhóm UID còn lại cho tới khi hoàn thành" | mobile.md `R033` tiếp tục UID group | `SUPPORTED` | Keep |
| `07105#L910-L911` "hiện thông báo" (raw KHÔNG có verbatim message) | mobile.md `ERR-QCM-001` (chưa có verbatim — Q-007) | `SUPPORTED` | Keep — verbatim missing đã flag Q-007 đúng |
| `07105#L902-L904` "rules đánh giá 10% số lượng cây vải của từng lô" (raw KHÔNG nêu công thức `ceil(...)`) | mobile.md BR "10% group UID cho vải" = `ceil(lot_uid_count × 0.10)` | `INFERRED` | Remove formula `ceil(× 0.10)` — raw chỉ nói "10%" + VD "3 cây vải"; spec tự suy `ceil()` và biến `lot_uid_count` không có trong raw |

**Mobile sampling AC:** AC-01..AC-20 trace đúng R-ID; spot-check AC-11 (R016 10%→3 dòng "30 group ×10%=3"), AC-14 (R023 19 enum), AC-16 (R025 formula), AC-17 (R027), AC-19 (R031/R032) → khớp raw. `SUPPORTED`. **Lưu ý AC-11** "Lô L1 có 30 group UID, áp 10% = 3 dòng" — số 30/3 là ví dụ minh hoạ của spec (raw chỉ có VD "3 cây vải"); chấp nhận là illustrative example trong AC, không phải claim formula.

---

## stub_qc_evaluation_result

> Critical flags: has_enum (R006 status, R007 type, R009 yes/no, R030 N/A/No/Yes), has_state_transition (R030 No→Yes), has_validation_rule (R010 date range), has_business_rule, has_error_messages. Verify 100% R006-R010, R014-R015, R020, R023-R030 + enum + state + 1 message + 16 BR.

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07105#L570-L573` "Kết quả đánh giá / Menu: Inbound / Quality control / Tab Kết quả đánh giá (Assessment Result)" | result.md `R001` navigation | `SUPPORTED` | Keep |
| `07105#L578-L579` "SKU, barcode: Hỗ trợ tìm theo SKU, barcode; Tìm theo mã chính xác nhập vào" | result.md `R002` filter SKU/barcode exact | `SUPPORTED` | Keep — match exact rule flag Q-010 đúng |
| `07105#L580-L582` "VAS: tìm theo mã VAS; Tìm theo mã chính xác nhập vào" | result.md `R003` filter VAS exact | `SUPPORTED` | Keep |
| `07105#L583-L585` "Kho: tìm theo kho cần đánh giá; Hỗ trợ tìm theo tên kho khi nhập từ 3 ký tự" | result.md `R004` filter Kho ≥3 ký tự | `SUPPORTED` | Keep |
| `07105#L586-L588` "Mã PO: tìm theo mã PO nguồn (mã PO inside); Tìm theo mã chính xác nhập vào" | result.md `R005` filter Mã PO exact | `SUPPORTED` | Keep |
| `07105#L589-L595` "Trạng thái: Mới (New) yêu cầu vừa sinh; Đang đánh giá (Processing) đang đánh giá chưa hoàn thành; Hoàn thành (Completed) đã xác nhận hoàn thành" | result.md `R006` status enum 3 values | `SUPPORTED` | Keep — enum đủ **3/3** verbatim |
| `07105#L596-L606` "Phân loại (Type): Tự động (Automation); Thủ công (Manual); Bình thường/Normal; Nhóm UID/Group UID (SP Vải); Xã vải/Fabric Relaxing (khâu xã vải)" | result.md `R007` type enum 2 trục (nguồn gốc + flow) | `SUPPORTED` | Keep — enum đủ 5 values; raw gộp trong 1 cell `Phân loại`, spec diễn giải "2 trục" → Q-005 flag cấu trúc cột đúng (không phải INFERRED vì raw thực sự list 2 nhóm value trong 1 cột) |
| `07105#L607-L611` "Người đánh giá (Assessment by): Người thực hiện đánh giá; Format: Email của Hasaki + Thời gian hoàn thành đánh giá" | result.md `R008` filter người đánh giá format | `SUPPORTED` | Keep — layout flag Q-006 đúng |
| `07105#L612-L616` "Có tiêu chí không đạt (Have criteria fail): Có (Yes) có ít nhất 1 tiêu chí không đạt; Không (No) không có tiêu chí không đạt" | result.md `R009` filter enum Yes/No | `SUPPORTED` | Keep |
| `07105#L617-L624` "Ngày đánh giá (Assessment at): Từ ngày đến ngày" + `L624` "Từ ngày phải nhỏ hơn hoặc bằng đến ngày" | result.md `R010` date range `Từ ngày ≤ Đến ngày` | `SUPPORTED` | Keep — validation verbatim khớp |
| `07105#L629` "VAS: Chọn vào VAS để hyperlink qua trang detail của VAS tương ứng" | result.md `R011` listing VAS hyperlink | `SUPPORTED` | Keep |
| `07105#L630-L631` "Kho / Warehouse" | result.md `R012` listing Kho | `SUPPORTED` | Keep |
| `07105#L632` "Sản phẩm / Product / Format: SKU – tên sản phẩm" | result.md `R013` listing SP format | `SUPPORTED` | Keep |
| `07105#L633` "Tiêu chí đạt / Criteria passed / Tổng số tiêu chí đạt / tổng tiêu chí cần đánh giá cho SKU" | result.md `R014` listing tiêu chí đạt ratio | `SUPPORTED` | Keep |
| `07105#L634` "Tiêu chí không đạt / Criteria failed / Tổng số tiêu chí không đạt / tổng tiêu chí cần đánh giá cho SKU" | result.md `R015` listing tiêu chí không đạt ratio | `SUPPORTED` | Keep |
| `07105#L635-L636` "Phân loại / Type" (cột listing) | result.md `R016` listing phân loại | `SUPPORTED` | Keep |
| `07105#L637` "Mã PO nguồn / PO source number / Chọn vào mã PO hyperlink qua trang detail PO trên Inside" | result.md `R017` listing PO hyperlink | `SUPPORTED` | Keep |
| `07105#L638-L645` cột SP: Nhà cung cấp, Danh mục, Thương hiệu, Ghi chú, Người đánh giá (Email hasaki + Thời gian hoàn thành đánh giá), Trạng thái | result.md `R018` listing cột info SP | `SUPPORTED` | Keep |
| `07105#L645-L647` "Thao tác: Chọn [icon] để xem chi tiết kết quả đánh giá" | result.md `R019` cột Thao tác | `SUPPORTED` | Keep — icon cụ thể flag Q-007 đúng |
| `07105#L649-L658` "Dựng 1 service ghi nhận kết quả ... WMS ghi nhận kết quả cuối cùng; VAS_ID + Group UID gắn từng service; mỗi service gồm Group UID + Mã tiêu chí + Kết quả; mỗi service = 1 kết quả đánh giá của 1 group UID; tổng hợp → kết quả cho cả group UID và VAS" | result.md `R020` service ghi nhận | `SUPPORTED` | Keep — API endpoint flag Q-001 đúng |
| `07105#L659-L662` "18-09-2025: Chi tiết kết quả đánh giá / Chi tiết kết quả đánh giá chất lượng sản phẩm / Type = Bình thường" (raw chỉ heading, KHÔNG nêu fields) | result.md `R021` chi tiết Type=Bình thường (format Q-002) | `SUPPORTED` | Keep — testable ⚠️ + Q-002 flag thiếu format đúng |
| `07105#L665-L666` "Type = Nhóm UID / Chọn để xem chi tiết kết quả đánh giá theo từng nhóm UID" | result.md `R022` chi tiết Type=Nhóm UID | `SUPPORTED` | Keep |
| `07105#L667-L668` "Với tiêu chí lỗi 4 điểm / Do loại tiêu chí này hơi đặc thù nên cho lưu trữ và hiển thị riêng" | result.md `R023` lỗi 4 điểm hiển thị riêng | `SUPPORTED` | Keep |
| `07105#L672` "Mỗi 1 loại lỗi là 1 group, có thể thu gọn hoặc mở rộng" | result.md `R024` group thu gọn/mở rộng | `SUPPORTED` | Keep |
| `07105#L674-L675` "Tổng điểm lỗi = tổng số điểm của 4 loại chưa nhân hệ số; Tổng điểm lỗi đã nhân hệ số" | result.md `R025` tổng điểm 4 điểm | `SUPPORTED` | Keep — formula hệ số flag Q-003 đúng |
| `07105#L676-L684` "Trong mỗi loại lỗi hiện chi tiết từng lỗi: Loại lỗi, Hình ảnh lỗi, Ghi chú; Tương tự cho các loại lỗi 2/3/4 điểm" | result.md `R026` chi tiết lỗi 4 nhóm | `SUPPORTED` | Keep |
| `07105#L685-L689` "tiêu chí thiết lập theo từng bước: 1 bước là 1 nhóm thông tin gồm Hình ảnh, Kết quả ghi nhận, Ghi chú" | result.md `R027` tiêu chí theo bước | `SUPPORTED` | Keep |
| `07105#L1103-L1106` "Chi tiết kết quả đánh giá: bổ sung thêm 2 thông tin: Số lượng cần đánh giá; Hình ảnh tem QC" | result.md `R028` S-25 bổ sung 2 info | `SUPPORTED` | Keep |
| `07105#L1108-L1111` "Cột phân loại (Type): bổ sung giá trị Xã vải / Fabric Relaxing: luồng đánh giá cho khâu xã vải trước khi chuyển qua may thành phẩm" | result.md `R029` bổ sung enum Xã vải | `SUPPORTED` | Keep |
| `07105#L1112-L1123` "UID group (Web) Menu: Inventory / Group UID / Tab Danh sách; field 'Đánh giá đạt': N/A (SKU có khai báo UID group nhưng không thuộc Thời trang NVL và không phải SKU vải); No (SKU thuộc Thời trang NVL và là SKU vải, sau nhận PO mặc định No; sau đánh giá xã vải Đạt → No qua Yes); Yes (SKU Thời trang NVL và SKU vải, sau nhận PO và hoàn thành đánh giá xã vải kết quả Đạt)" | result.md `R030` field Đánh giá đạt N/A/No/Yes + transition No→Yes | `SUPPORTED` | Keep — enum đủ **3/3**, state_transition `No→Yes khi Đạt` verbatim khớp; edge case Không đạt / re-evaluate flag Q-008/Q-009 đúng |
| `07105#L624` "Từ ngày phải nhỏ hơn hoặc bằng đến ngày" (rule, raw KHÔNG có verbatim error message) | result.md `ERR-QCR-001` (raw không verbatim — Q-004) | `SUPPORTED` | Keep — verbatim missing đã flag Q-004 đúng |

**Result sampling AC:** AC-01..AC-20 trace đúng R-ID; spot-check AC-04 (R006), AC-05 (R007/R029 "5 giá trị enum"), AC-07 (R010), AC-15 (R025), AC-18/19/20 (R030) → khớp raw. `SUPPORTED`. **Lưu ý AC-05** "hỗ trợ 5 giá trị enum (Tự động, Thủ công, Bình thường, Nhóm UID, Xã vải)" — raw list 5 value trong cột Phân loại nhưng chia 2 nhóm ngữ nghĩa (nguồn gốc 2 + flow 3); AC gộp "5 giá trị" là cách diễn đạt hợp lệ (đếm đủ), Q-005 đã flag verify cấu trúc cột thực tế. `SUPPORTED`.

---

## Tổng kết labels

| Spec | SUPPORTED | INFERRED | POTENTIAL_OMISSION | MISSING_DETAIL | UNCLEAR | Khác |
|:-----|----------:|---------:|-------------------:|---------------:|--------:|:-----|
| stub_qc_evaluation_manual | 27 | 0 | 1 | 1 | 0 | 0 |
| stub_qc_evaluation_mobile | 33 | 1 | 0 | 0 | 0 | 0 |
| stub_qc_evaluation_result | 31 | 0 | 0 | 0 | 0 | 0 |
| **Tổng** | **91** | **1** | **1** | **1** | **0** | **0** |

Tất cả enum critical (Manual Require VAT 3/3; Mobile 19 loại lỗi 19/19, 4 màu color; Result status 3/3, type 5/5, Yes/No, Đánh giá đạt 3/3) đã verify đủ count + verbatim. State transitions (Manual Blocked/Damaged/Normal; Result No→Yes) khớp raw. Error messages đều flag verbatim-missing bằng Q-ID đúng (no false SUPPORTED).
