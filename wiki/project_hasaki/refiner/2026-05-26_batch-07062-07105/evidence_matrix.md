# Evidence Matrix — Batch 07062 + 07105
**Session:** 2026-05-26

---

## receiving_po_inbound_shipment.md — partial_read: false

| Raw Evidence (path#line) | Wiki Claim (path#line) | Status | Action |
|:-------------------------|:-----------------------|:-------|:-------|
| 07062#229-231: filter Check of goods = Yes/No; Eligible to receive = Yes/No | R-IS-01, R-IS-02: Yes/No values | `SUPPORTED` | — |
| 07062#233-240: WMS Status filter, 5 values: Mới/Open, Đang nhận hàng/Receiving, Đã nhận hàng/Received, Hoàn thành/Completed, Đã huỷ/Canceled; chỉ Type=PO; chọn nhiều | R-IS-03: 5 values, multi-select, Type=PO only | `SUPPORTED` | — |
| 07062#244-246: Đồng kiểm — "lấy thông tin khi user chọn khi scan nhận PO" | R-IS-04: mô tả đúng | `SUPPORTED` | — |
| 07062#247-248: Eligible = Yes: đủ điều kiện / No: không đủ | R-IS-05: Yes/No description | `SUPPORTED` | — |
| 07062#249-262: Mô tả — 4 giá trị VN/EN (PO chưa xác nhận, PO chưa được duyệt, PO chưa xác nhận hoá đơn, SKU tester chưa khai báo) | R-IS-06: 4 values đúng | `SUPPORTED` | — |
| 07062#264-271: Status mapping Inside→WMS: Verified→Open, Receiving→Receiving, Received→Received, Cancel→Canceled; chọn nhiều | R-IS-07: 4 mappings + multi-select | `SUPPORTED` | — |
| 07062#272-276: "Với Status Receiving thì bổ sung thêm thời gian đã bao lâu chưa hoàn thành nhận hàng (tính từ khi bắt đầu scan PO để nhận hàng)" | R-IS-08: hiển thị thời gian, tính từ lúc scan PO | `SUPPORTED` | — |
| 07062#277-290: WMS Status column (listing) — Mới/Open, Đang nhận hàng/Receiving, Đã nhận hàng/Received, Đã huỷ/Canceled; 4 values; chỉ Type=PO | R-IS-09: 4 values (không có Completed), Type=PO only | `SUPPORTED` | — |
| 07062#317: "Số lượng thiếu  Qty missing  Số lượng confirm – số lượng đã nhận" | R-IS-13: Qty missing = Qty confirm − Qty received | `SUPPORTED` | — |
| 07062#319-322: "Nếu PO giao trong ngày nhưng vẫn chưa chuyển 'Đã nhận hàng' thì user sẽ vào để giải trình lý do tại sao PO bị treo receiving. Sắp xếp giảm dần theo thời gian tạo" | R-IS-14: điều kiện giải trình + sort desc | `SUPPORTED` | — |

**Q-IS-01 note:** WMS Status "Hoàn thành/Completed" — raw chỉ ghi trong filter table (line 238), không có trong WMS status listing table (lines 279-290). Question Open — không sinh TC.

---

## receiving_po_asn.md — partial_read: false

| Raw Evidence (path#line) | Wiki Claim (path#line) | Status | Action |
|:-------------------------|:-----------------------|:-------|:-------|
| 07062#441-449: ReOpen — chỉ show khi status=Receiving VÀ user chưa scan item nào; reopen về Open; xoá nhân viên | R-ASN-11: conditions + result | `SUPPORTED` | — |
| 07062#448-449: "Do you want to ReOpen for ticket ASN [code]?" | R-ASN-12: exact confirm message | `SUPPORTED` | — |
| 07062#371-377: Filter Loại — Purchase order, Customer return, Internal transfer, Adjustment; chọn nhiều | R-ASN-04: 4 values, multi-select | `SUPPORTED` | — |
| 07062#378-383: Filter Owner — Hasaki Cosmetics, Hasaki WMS, Hasaki OMS; chọn nhiều | R-ASN-05: 3 values, multi-select | `SUPPORTED` | — |
| 07062#384-390: Filter Status — Mới/Open, Đang nhận/Receiving, Đã nhận/Received, Đã huỷ/Canceled; chọn nhiều | R-ASN-06: 4 values, multi-select | `SUPPORTED` | — |
| 07062#488-495: "SL thiếu = SL PO − SL nhận phiên đó; Ví dụ: SKU A PO 10, lần 1 nhận 5 → thiếu 5, lần 2 nhận 3 → thiếu 2" | R-ASN-18: formula và ví dụ | `SUPPORTED` | — |

---

## receiving_po_vas.md — partial_read: false

| Raw Evidence (path#line) | Wiki Claim (path#line) | Status | Action |
|:-------------------------|:-----------------------|:-------|:-------|
| 07062#530-531: "Sức khoẻ Làm đẹp có quản lý serial/imei → ASN Received → hệ thống tự sinh VAS và auto completed" | R-VAS-01: auto sinh VAS + auto Complete | `SUPPORTED` | — |
| 07062#534-536: "TSCĐ, CCDC, CCDC PB có quản lý Serial/Imei/Label → ASN Received → sinh VAS với status=Open" | R-VAS-02: TSCĐ/CCDC/CCDC PB → Open | `SUPPORTED` | — |
| 07062#537-540: "UID sau received → status Received, chưa auto chuyển In-Bin; không được lấy pick cho order/receipt/IT" | R-VAS-03: status Received, no pick | `SUPPORTED` | — |
| 07062#542-543: "Sau khi user xác nhận chụp hình/dán ID → trạng thái chuyển Received → In-Bin" | R-VAS-04: transition Received→In-Bin | `SUPPORTED` | — |
| 07062#564: "Trạng thái  Status  Mặc định = Null" + lines 571-574: Mới/Open, Đang xử lý/In-Progress, Hoàn thành/Completed, Đã huỷ/Canceled | R-VAS-08: default Null, 4 status values | `SUPPORTED` | — |
| **07062#607: "Mới / Open: khi ASN received và sinh ra 1 VAS cho TSCĐ/CCDC/CCDC PB"** | **R-VAS-12: Open = khi ASN received** | **`SUPPORTED`** | — |
| **07062#611-612: "Đang xử lý / In-Progress: khi có ít nhất 1 SKU có số lượng đã dán > 1"** | **R-VAS-12: In-Progress = SL đã dán > 0** | **`INFERRED`** | **Xóa "> 0", dùng "> 1". Thêm Q-VAS-03.** |
| 07062#613-614: "Hoàn thành / Completed. Đã huỷ / Canceled" | R-VAS-12: Completed và Canceled | `SUPPORTED` | — |
| 07062#704-716: Serial validation (đã tồn tại trong danh sách / trên hệ thống / không hợp lệ ≥16 ký tự); QRCode validation | R-VAS-21: validation conditions | `SUPPORTED` | — |

---

## quality_control_criteria_setup.md — partial_read: false

| Raw Evidence (path#line) | Wiki Claim (path#line) | Status | Action |
|:-------------------------|:-----------------------|:-------|:-------|
| 07105#134-135: "Mã, tên tiêu chí — tìm gần đúng, nhập tối thiểu 3 ký tự" | R-CS-01: search ≥3 chars | `SUPPORTED` | — |
| 07105#139-142: "Từ ngày…đến ngày — tìm theo ngày tạo; Đến ngày ≥ Từ ngày; mặc định không chọn ngày" | R-CS-03: date filter rules | `SUPPORTED` | — |
| 07105#153-160: Deactivate/Activate confirm messages exact EN text | R-CS-06: popup confirm messages | `SUPPORTED` | — |
| **07105#162-163: "Người tạo: email Hasaki. Thời gian tạo: YYYY-MM-DD HH:SS"** | **R-CS-07: "YYYY-MM-DD HH:SS"** | **`UNCLEAR`** | **Format thiếu MM. Raw cũng ghi HH:SS. Thêm Q-CS-03 hỏi Dev.** |
| **07105#165-166: "Người cập nhật cuối cùng: email Hasaki. Thời gian cập nhật: YYYY-MM-DD HH:SS"** | **R-CS-08: "YYYY-MM-DD HH:SS"** | **`UNCLEAR`** | **Cùng vấn đề format. Ghi nhận trong Q-CS-03.** |
| 07105#173-179: "Mã tiêu chí: bắt buộc; không được trùng → Mã tiêu chí đã tồn tại. / The criteria code already exists." | R-CS-10: unique + messages VN/EN | `SUPPORTED` | — |
| 07105#180-189: "Tên tiêu chí: bắt buộc; không được trùng → Tên tiêu chí đã tồn tại. / The criteria name already exists." | R-CS-11: unique + messages VN/EN | `SUPPORTED` | — |
| 07105#1306-1308: "Khi tạo tiêu chí có phân loại Lỗi 4 điểm → sau nhấn Tạo → mở màn hình thiết lập nội dung" | R-CS-20: Alt-Flow 4 điểm | `SUPPORTED` | — |
| 07105#1309-1311: "Khi thiết lập tiêu chí cho SKU, nếu chọn Lỗi 4 điểm → hệ thống tự lấy thiết lập của tiêu chí để cập nhật cho SKU" | R-CS-22: auto apply từ Criteria | `SUPPORTED` | — |

---

## Stubs — [STUB — section chưa đọc]

| File | Stub coverage | Action |
|:-----|:-------------|:-------|
| receiving_po_app.md | Chỉ verify R-APP-01~03 (scan PO entry). Phần còn lại chưa đọc — không verify | Đọc đủ rồi Gate 1B |
| receiving_po_confirm_paste_id.md | Chưa đọc trang 84–95 — skip verify | Đọc đủ rồi Gate 1B |
| receiving_po_vas_manual.md | Chưa đọc trang 96–101 — skip verify | Đọc đủ rồi Gate 1B |
| receiving_po_packing_list.md | Chưa đọc trang 102–115 — skip verify | Đọc đủ rồi Gate 1B |
| receiving_po_fabric_uid_group.md | Chỉ verify R-FUG-01~03 (ngữ cảnh VAS/ASN đã đọc). Trang 74–78 chưa đọc | Đọc đủ rồi Gate 1B |
