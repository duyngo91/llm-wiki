---
session: 2026-05-30
batch: spec-scoped-batch-2
generated_at: "2026-05-30 21:15:00+07:00"
---

# Evidence Matrix — spec-scoped-batch-2

> Per-claim verification. Format: Raw evidence (path#line) | Wiki claim (path#line) | Status | Action.

Verify rule: 100% claims mapped đến sections có flag critical (enum / state_transition / formula / business_rule / error_messages / validation_rule); 1/5 sampling cho non-critical. Vì index flags=[] (observation), AI manually treat enum/BR/formula/error/state-transition claims là critical.

---

## stub_receiving_po_inbound_shipment

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07062#L227-L231` (Đồng kiểm filter Yes/No, move qua ASN) | `stub_receiving_po_inbound_shipment.md#L48` R001 | `SUPPORTED` | Keep |
| `07062#L232` (Đủ điều kiện nhận filter Yes/No) | `stub_receiving_po_inbound_shipment.md#L49` R002 | `SUPPORTED` | Keep |
| `07062#L233-L240` (Trạng thái WMS filter, Type=PO, multi, 5 values: Mới/Đang nhận hàng/Đã nhận hàng/Hoàn thành/Đã huỷ) | `stub_receiving_po_inbound_shipment.md#L50` R003 | `SUPPORTED` | Keep — 5 values verbatim, multi-select confirmed |
| `07062#L244-L246` (Listing Đồng kiểm lấy thông tin khi user scan PO) | `stub_receiving_po_inbound_shipment.md#L51` R004 | `SUPPORTED` | Keep |
| `07062#L247-L248` (Listing Đủ điều kiện nhận Yes/No) | `stub_receiving_po_inbound_shipment.md#L52` R005 | `SUPPORTED` | Keep |
| `07062#L249-L250` (Mô tả lý do PO không đủ điều kiện, song ngữ VN/EN) | `stub_receiving_po_inbound_shipment.md#L53` R006 | `SUPPORTED` | Keep |
| `07062#L255-L262` (4 sample messages, raw có literal `422225215`) | `stub_receiving_po_inbound_shipment.md#L54` R007 + L120 DESC-INS-004 | `UNCLEAR (đã captured)` | Spec dùng `{sku_code}` placeholder; Q-003 đã capture. Acceptable interpretation. |
| `07062#L264-L272` (Listing Trạng thái + mapping Inside↔WMS + multi-select) | `stub_receiving_po_inbound_shipment.md#L55` R008 | `SUPPORTED` | Keep |
| `07062#L266-L271` (Mapping table Inside↔WMS: Verified>>Open, Receiving<<Receiving, Received<<Received, Cancel>>Canceled) | `stub_receiving_po_inbound_shipment.md#L56` R009 | `SUPPORTED` | Keep — verbatim |
| `07062#L273-L276, L291-L295` (Receiving: bổ sung thời gian từ khi bắt đầu scan PO, giải trình cuối ngày) | `stub_receiving_po_inbound_shipment.md#L57` R010 | `SUPPORTED` | Keep |
| `07062#L277-L278` (Trạng thái WMS riêng, Type=PO only) | `stub_receiving_po_inbound_shipment.md#L58` R011 | `SUPPORTED` | Keep |
| `07062#L279-L290` (Định nghĩa 4 WMS status: Mới, Đang nhận hàng, Đã nhận hàng, Đã huỷ) | `stub_receiving_po_inbound_shipment.md#L59` R012 | `SUPPORTED` | Keep — 4 values. Confirms inconsistency với R003 (filter có 5 values). Q-001 capture. |
| `07062#L303-L307` (Detail: bổ sung Đủ điều kiện nhận + Mô tả) | `stub_receiving_po_inbound_shipment.md#L60` R013 | `SUPPORTED` | Keep |
| `07062#L310-L315` (Đổi Số lượng → Số lượng xác nhận / Qty confirm) | `stub_receiving_po_inbound_shipment.md#L61` R014 | `SUPPORTED` | Keep |
| `07062#L316` (Số lượng đã nhận = tổng SL scan theo ASN) | `stub_receiving_po_inbound_shipment.md#L62` R015 | `SUPPORTED` | Keep |
| `07062#L317` (Formula: Số lượng confirm – số lượng đã nhận) | `stub_receiving_po_inbound_shipment.md#L63` R016 + AC-08 + BR | `SUPPORTED` | Keep — raw uses "Số lượng confirm", spec consistently uses renamed "Số lượng xác nhận" (per R014) |
| `07062#L320-L321` (Giải trình lý do treo PO trigger) | `stub_receiving_po_inbound_shipment.md#L64` R017 | `SUPPORTED` | Keep |
| `07062#L322` (Sắp xếp giảm dần theo thời gian tạo) | `stub_receiving_po_inbound_shipment.md#L65` R018 | `SUPPORTED` | Keep |
| `07062#L326-L329` (Bình luận, button Thêm hiện ở mọi status) | `stub_receiving_po_inbound_shipment.md#L66` R019 | `SUPPORTED` | Keep |
| `07062#L330-L339` (Columns: TT/Nội dung/Người tạo/Ngày tạo) | `stub_receiving_po_inbound_shipment.md#L67` R020 | `SUPPORTED` | Keep |
| Section flag check `has_enum=true` (R003, R007, R012) | spec có đủ enum tables | `SUPPORTED` | Keep — note index `flags=[]` advisory |
| BR "Hiển thị thời gian Receiving — tính từ scan PO đầu tiên" | `stub_receiving_po_inbound_shipment.md#L106` | `UNCLEAR (minor)` | Raw `07062#L274` says "tính từ khi bắt đầu scan PO" — spec thêm "đầu tiên". Implicit qualifier; Q-004 (format thời gian) đã capture liên quan. Acceptable. |
| AC-01..AC-11 (11 ACs) | spec lines 124-167 | `SUPPORTED` | All ACs derivable từ corresponding R-IDs |

---

## stub_qc_criteria_sku

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07105#L217-L219` (Menu + Tab Thiết lập SKU) | `stub_qc_criteria_sku.md#L48` R001 | `SUPPORTED` | Keep |
| `07105#L228-L229` (Filter SKU/Barcode/Tên sản phẩm) | `stub_qc_criteria_sku.md#L49` R002 | `SUPPORTED` | Keep |
| `07105#L231` (Filter Danh mục) | `stub_qc_criteria_sku.md#L50` R003 | `SUPPORTED` | Keep |
| `07105#L232` (Filter Thương hiệu) | `stub_qc_criteria_sku.md#L51` R004 | `SUPPORTED` | Keep |
| `07105#L233-L236` (Filter Active default không chọn, 2 values) | `stub_qc_criteria_sku.md#L52` R005 | `SUPPORTED` | Keep |
| `07105#L239-L242` (Filter Thời điểm đánh giá: Khi nhận PO / Sau khi nhận PO) | `stub_qc_criteria_sku.md#L53` R006 | `SUPPORTED` | Keep |
| `07105#L243-L247` (Filter Tần suất: Tất cả PO / Ngẫu nhiên) | `stub_qc_criteria_sku.md#L54` R007 | `SUPPORTED` | Keep |
| `07105#L248-L250` (Filter date range — **raw L249 có typo "Đến ngày phải lớn hơn hoặc bằng đến ngày"**) | `stub_qc_criteria_sku.md#L55` R008 + BR L129 | **`POTENTIAL_OMISSION`** | Spec silently correct thành `Đến ngày ≥ Từ ngày`. Cần FIX-002 — thêm Q-011 |
| `07105#L256` (Listing Sản phẩm = SKU – Tên sản phẩm) | `stub_qc_criteria_sku.md#L56` R009 | `SUPPORTED` | Keep |
| `07105#L267-L269` (Active default; toggle hiện confirm dialog) | `stub_qc_criteria_sku.md#L57` R010 | `SUPPORTED` | Keep — note: raw "SKU mới được tạo" interpret contextually = setup mới |
| `07105#L272-L273` (1 SKU không thể cùng active 2 thiết lập) | `stub_qc_criteria_sku.md#L58` R011 | `SUPPORTED` | Keep — verbatim |
| `07105#L274-L276` (Người tạo: email Hasaki + YYYY-MM-DD HH:SS) | `stub_qc_criteria_sku.md#L59` R012 | `SUPPORTED` | Keep — HH:SS verbatim, Q-007 đã capture format question |
| `07105#L277-L279` (Người cập nhật format) | `stub_qc_criteria_sku.md#L60` R013 | `SUPPORTED` | Keep |
| `07105#L281-L288` (Thao tác: Cập nhật + Xem chi tiết + Xoá thiết lập, status Mới only) | `stub_qc_criteria_sku.md#L61` R014 | `SUPPORTED` | Keep |
| `07105#L289-L290` (Tạo mới → modal) | `stub_qc_criteria_sku.md#L62` R015 | `SUPPORTED` | Keep |
| `07105#L294-L299` (Modal Sản phẩm bắt buộc, search) | `stub_qc_criteria_sku.md#L63` R016 | `SUPPORTED` | Keep |
| `07105#L312-L323` (Modal Thời điểm đánh giá bắt buộc; Khi nhận PO chưa hỗ trợ phase) | `stub_qc_criteria_sku.md#L64` R017 | `SUPPORTED` | Keep |
| `07105#L324-L338` (Modal Tần suất bắt buộc; Random chưa hỗ trợ phase) | `stub_qc_criteria_sku.md#L65` R018 | `SUPPORTED` | Keep — minor drop của "sản phẩm" trong VAS description, không thay đổi meaning |
| `07105#L339` (Modal Ghi chú không bắt buộc) | `stub_qc_criteria_sku.md#L66` R019 | `SUPPORTED` | Keep |
| `07105#L340` (Modal Đóng tắt popup) | `stub_qc_criteria_sku.md#L67` R020 | `SUPPORTED` | Keep — spec thêm "không lưu" là implicit từ context (separate Lưu button) |
| `07105#L344-L348` (Tiếp tục; SKU đã active báo lỗi, VN+EN) | `stub_qc_criteria_sku.md#L68` R021 + ERR-CSKU-003 | `SUPPORTED` | Keep — message verbatim |
| `07105#L365-L368` (Tiêu chí đánh giá bắt buộc, min 3 ký tự search) | `stub_qc_criteria_sku.md#L69` R022 | `SUPPORTED` | Keep |
| `07105#L369-L371` (Yêu cầu chụp hình Yes/No) | `stub_qc_criteria_sku.md#L70` R023 | `SUPPORTED` | Keep |
| `07105#L372-L374` (Hình chụp mẫu max 3) | `stub_qc_criteria_sku.md#L71` R024 | `SUPPORTED` | Keep |
| `07105#L375-L379` (Loại đánh giá default Đạt/Không đạt; Phân loại = Bình thường không sửa) | `stub_qc_criteria_sku.md#L72` R025 | `SUPPORTED` | Keep |
| `07105#L380-L406` (6 toán tử: =, >, >=, <, <=, Trong khoảng) | `stub_qc_criteria_sku.md#L73` R026 | `SUPPORTED` | Keep — 6 verbatim |
| `07105#L383-L396` (Validation cho `=`: Giá trị/Đơn vị tính/Sai số. Raw cho `>`, `>=`, `<`, `<=` (L395-L401) **chỉ list Giá trị + Đơn vị tính, KHÔNG nhắc Sai số**) | `stub_qc_criteria_sku.md#L74` R027 | **`POTENTIAL_OMISSION`** | Spec apply Sai số cho 5 toán tử nhưng raw chỉ explicit `=`. Cần FIX-003 — thêm Q-012 |
| `07105#L402-L405` (Trong khoảng: Giá trị từ-đến + Đơn vị tính) | `stub_qc_criteria_sku.md#L75` R028 | `SUPPORTED` | Keep |
| `07105#L407-L409` (Công thức: chờ Dev) | `stub_qc_criteria_sku.md#L76` R029 | `SUPPORTED` | Keep — Q-005 capture |
| `07105#L411-L413` (1 tiêu chí 1 điều kiện; Thêm (+) disable) | `stub_qc_criteria_sku.md#L77` R030 | `SUPPORTED` | Keep |
| `07105#L414-L420` (Phân loại 3 values) | `stub_qc_criteria_sku.md#L78` R031 | `SUPPORTED` | Keep — 3 verbatim |
| `07105#L421` (Mô tả không bắt buộc) | `stub_qc_criteria_sku.md#L79` R032 | `SUPPORTED` | Keep |
| `07105#L422-L426` (Thêm; trùng tiêu chí → message verbatim) | `stub_qc_criteria_sku.md#L80` R033 + ERR-CSKU-004 | `SUPPORTED` | Keep — message verbatim |
| `07105#L428` (Đóng) | `stub_qc_criteria_sku.md#L81` R034 | `SUPPORTED` | Keep |
| `07105#L429-L430` (Lưu) | `stub_qc_criteria_sku.md#L82` R035 | `SUPPORTED` | Keep |
| `07105#L431-L432` (Hoàn thành → Chờ duyệt) | `stub_qc_criteria_sku.md#L83` R036 | `SUPPORTED` | Keep |
| `07105#L303-L304, L317-L318, L329-L330` (ERR-CSKU-001 verbatim VN+EN) | `stub_qc_criteria_sku.md#L150` ERR-CSKU-001 | `SUPPORTED` | Keep — verbatim |
| `07105#L308-L311` (ERR-CSKU-002 — raw literal SKU `422280022`) | `stub_qc_criteria_sku.md#L151` ERR-CSKU-002 | `UNCLEAR (placeholder)` | Spec dùng `{sku_code}`. Pattern lặp với DESC-INS-004 của inbound_shipment. Q-008 partially capture (VN missing aspect). Acceptable interpretation. |
| `07105#L347-L348` (ERR-CSKU-003 verbatim) | `stub_qc_criteria_sku.md#L152` ERR-CSKU-003 | `SUPPORTED` | Keep — verbatim |
| `07105#L425-L426` (ERR-CSKU-004 verbatim) | `stub_qc_criteria_sku.md#L153` ERR-CSKU-004 | `SUPPORTED` | Keep — verbatim |
| `07105#L270` (MSG-CSKU-005 EN: `Do you want to DEACTIVATE setup by SKU 422280022?`) | `stub_qc_criteria_sku.md#L154` MSG-CSKU-005 | `UNCLEAR (placeholder + VN missing)` | Spec dùng `{sku_code}` (placeholder); raw chỉ EN; VN missing. Q-008 capture verbatim VN issue. |
| `07105#L271` (MSG-CSKU-006 EN: ACTIVATE) | `stub_qc_criteria_sku.md#L155` MSG-CSKU-006 | `UNCLEAR (placeholder + VN missing)` | Same as MSG-CSKU-005. |
| AC-01..AC-14 (14 ACs) | spec lines 159-214 | `SUPPORTED` | All ACs derivable từ corresponding R-IDs |

---

## stub_qc_vas

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07105#L697-L706` (VAS type 4 values: IMEI/RFID/Quality Control/Other) | `stub_qc_vas.md#L48` R001 | `SUPPORTED` | Keep — 4 values verbatim |
| `07105#L700-L707` (Filter VAS type multi-select) | `stub_qc_vas.md#L49` R002 | `SUPPORTED` | Keep |
| `07105#L708-L710` (Data table bổ sung VAS type column) | `stub_qc_vas.md#L50` R003 | `SUPPORTED` | Keep |
| `07105#L711-L712` (Multi VAS type display, ngăn bởi dấu phẩy) | `stub_qc_vas.md#L51` R004 | `SUPPORTED` | Keep |
| `07105#L713-L728` (VAS status enum 9 values verbatim, bao gồm typo `Wating for paste ID`) | `stub_qc_vas.md#L52` R005 | `SUPPORTED` | Keep — 9 values + typo preserved verbatim; Q-008 capture typo |
| `07105#L719` (Đang xử lý semantics) | `stub_qc_vas.md#L53` R006 | `SUPPORTED` | Keep |
| `07105#L722-L723` (Chờ duyệt semantics) | `stub_qc_vas.md#L54` R007 | `SUPPORTED` | Keep |
| `07105#L724-L725` (Chờ dán ID semantics: SKU required IMEI, RFID) | `stub_qc_vas.md#L55` R008 | `SUPPORTED` | Keep — raw comma interpreted as "hoặc" consistent với L752 |
| `07105#L727` (Chờ NCC đến lấy: "Khi VAS được chọn") | `stub_qc_vas.md#L56` R009 | `SUPPORTED` | Keep — spec thêm "(action Trả nhà cung cấp)" derivable từ R015 flow L762. Q-005 capture ambiguity. |
| `07105#L734-L755` (VAS Chờ duyệt: 3 actions Mở lại/Nhận hàng/Trả NCC) | `stub_qc_vas.md#L57` R010 | `SUPPORTED` | Keep |
| `07105#L737-L742` (Mở lại dialog + revert về Mới) | `stub_qc_vas.md#L58` R011 | `SUPPORTED` | Keep — Q-001 capture RECEIVE typo |
| `07105#L743-L751` (Nhận hàng: xác nhận tiêu chí Đạt; cho phép confirm dù có tiêu chí không đạt) | `stub_qc_vas.md#L59` R012 | `SUPPORTED` | Keep |
| `07105#L752-L754` (Branch sau Nhận hàng: IMEI/RFID required → Chờ dán ID; ko required → Completed) | `stub_qc_vas.md#L60` R013 | `SUPPORTED` | Keep |
| `07105#L755-L759` (Trả NCC dialog: SL default = SL đã nhận, disable input) | `stub_qc_vas.md#L61` R014 | `SUPPORTED` | Keep |
| `07105#L760-L762` (Sau Xác nhận Trả NCC: ghi nhận SL + → Chờ NCC đến lấy) | `stub_qc_vas.md#L62` R015 | `SUPPORTED` | Keep |
| `07105#L763-L767` (Sau NCC lấy: → Đã trả NCC + Outbound Return vendor) | `stub_qc_vas.md#L63` R016 | `SUPPORTED` | Keep |
| `07105#L768-L771` (Adjustment Vendor Return chưa tạo được) | `stub_qc_vas.md#L64` R017 | `SUPPORTED` | Keep |
| `07105#L775-L780` (Update 18-09-2025: 10% group UID cho SKU vải; ceil; VD 25→3) | `stub_qc_vas.md#L65` R018 | `SUPPORTED` | Keep — formula `ceil(group_uid_count × 0.10)` verbatim, VD 25→3 confirmed |
| `07105#L739-L740` (MSG-VAS-001 EN với raw literal `1003241119000039`) | `stub_qc_vas.md#L111` MSG-VAS-001 | `UNCLEAR (placeholder)` | Spec dùng `{vas_code}`. Pattern lặp với DESC-INS-004 / ERR-CSKU-002. Q-001 capture indirectly. |
| `07105#L743-L744` (MSG-VAS-002 — raw nói "hiện thông báo" nhưng không quote text) | `stub_qc_vas.md#L112` MSG-VAS-002 | `SUPPORTED` | Keep — spec correctly ghi "chưa có" cho cả VN+EN; Q-007 capture |
| `07105#L755-L756` (MSG-VAS-003 — raw không quote text) | `stub_qc_vas.md#L113` MSG-VAS-003 | `SUPPORTED` | Keep — Q-007 capture |
| AC-01..AC-12 (12 ACs) | spec lines 117-165 | `SUPPORTED` | All ACs derivable; AC-12 boundary case capture Q-004 |
