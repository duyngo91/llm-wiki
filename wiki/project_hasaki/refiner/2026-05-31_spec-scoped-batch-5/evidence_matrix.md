---
session: "2026-05-31"
batch: "spec-scoped-batch-5"
generated_at: "2026-05-31 19:30:00+07:00"
---

# Evidence Matrix — spec-scoped-batch-5

> Per-claim verification. Format: Raw evidence (path#line) | Wiki claim (path#line) | Status | Action.
>
> Verify rule: 100% claims mapped đến sections có flag critical (enum / state_transition / formula / business_rule / error_messages / validation_rule); 1/5 sampling cho non-critical.
> Raw source: `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.md` (v2.17).
> Phương pháp raw-first: đọc raw range TRƯỚC, mô tả lại bằng ngôn ngữ raw, rồi đối chiếu spec.

---

## stub_receiving_po_overview (raw L188-L224)

> Section metadata/header — không có flag critical (enum/formula/state). Verify full vì spec mới refine.

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07062#L189-L190` "Hiện tại việc nhận hàng PO đang được thực hiện trên App HSK Work, việc sử dụng đang có nhiều hạn chế cũng như cải tiến cũng gặp nhiều khó khăn" | `stub_receiving_po_overview#L51` R001 | `SUPPORTED` | Keep |
| `07062#L191-L192` "Tính năng này đang thuộc phạm vị của Kho nên sẽ move tính năng này qua WMS để đồng bộ và tiện cho việc quản lý và hỗ trợ sau này" | `stub_receiving_po_overview#L52` R002 | `SUPPORTED` | Keep |
| `07062#L198-L207` Section "Thuật ngữ & viết tắt", header `#  Code / Name / Desciption` (typo verbatim), 5 dòng (1.-5.) đều rỗng | `stub_receiving_po_overview#L53` R003 (5 dòng rỗng, header có typo `Desciption`) | `SUPPORTED` | Keep — typo `Desciption` đã flag Q-005 |
| `07062#L208-L209` "Quy trình (Workflow) - Link: https://drive.hasaki.vn/f/6fecf6ac99424782b12a/" | `stub_receiving_po_overview#L54` R004 | `SUPPORTED` | Keep — nội dung Drive flag Q-001 |
| `07062#L211-L216` "Giao diện (Wireframe) - Link figma update: .../04.-Receiving-PO_Update?node-id=0-1&t=... ; Link visily (old): .../boards/739286" | `stub_receiving_po_overview#L55` R005 (2 link Figma update + Visily old) | `SUPPORTED` | Keep — ưu tiên Figma vs Visily flag Q-002 |
| `07062#L223-L224` heading "Yêu cầu chức năng" + "Inbound Shipment – Updated" | `stub_receiving_po_overview#L56` R006 | `SUPPORTED` | Keep |
| `07062#L188-L192` migration App HSK Work → WMS | `stub_receiving_po_overview#L92-L95` AC-01 | `SUPPORTED` | Keep |
| `07062#L200-L206` bảng terms header + 5 row rỗng | `stub_receiving_po_overview#L96-L99` AC-02 (header `# Code\|Name\|Desciption`, 5 row rỗng) | `SUPPORTED` | Keep — giữ typo verbatim đúng |
| `07062#L208-L209` Drive link | `stub_receiving_po_overview#L100-L103` AC-03 | `SUPPORTED` | Keep |
| `07062#L211-L216` Figma + Visily | `stub_receiving_po_overview#L104-L107` AC-04 | `SUPPORTED` | Keep |
| `07062#L223-L224` heading trước Inbound Shipment | `stub_receiving_po_overview#L108-L111` AC-05 | `SUPPORTED` | Keep |
| BR `Mục tiêu migration` / `Bảng thuật ngữ` / `Workflow link` / `Wireframe link` | `stub_receiving_po_overview#L81-L84` (4 BR) | `SUPPORTED` | Keep — tổng hợp đúng từ R001-R005 |

**Overview: 12 claims chính SUPPORTED, 0 issue. 7 Q-ID hợp lệ (Q-001..Q-007 — pending-source/scope, không phải deviation).**

---

## stub_receiving_po_asn (raw L349-L520)

> Flag critical: enum (R006/R007/R008/R009/R012 filter values), state_transition (R015 ReOpen), formula (R023 SL thiếu), business_rule (R011/R013/R018/R021/R022/R024). Verify 100%.

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07062#L349-L351` "ASN – Updated, Menu: Inbound / ASN, Giao diện" | `stub_receiving_po_asn#L48` R001 | `SUPPORTED` | Keep |
| `07062#L358` "Mã ASN / ASN number / Tìm chính xác theo mã nhập vào" | `stub_receiving_po_asn#L49` R002 | `SUPPORTED` | Keep |
| `07062#L359-L365` "Mã phiếu nhập / Inbound shipment; Phiếu nhập nguồn / Inbound source mapping; Mã phiếu xuất / Outbound oder; Phiếu xuất nguồn / Outbound source mapping" | `stub_receiving_po_asn#L50` R003 | `SUPPORTED` | Keep — raw typo "oder" (Outbound order); spec sửa đúng nghĩa |
| `07062#L366-L368` "Kho / Warehouse — Load danh sách kho theo location và phân quyền; Hỗ trợ chọn nhiều; Hỗ trợ gợi ý khi user nhập từ 3 ký tự" | `stub_receiving_po_asn#L51` R004 | `SUPPORTED` | Keep |
| `07062#L369-L370` "SKU, Barcode — Hỗ trợ tìm theo SKU hoặc Barcode của SKU trong chi tiết của ASN" | `stub_receiving_po_asn#L52` R005 | `SUPPORTED` | Keep |
| `07062#L371-L377` "Loại / Type — Giá trị: Purchase order, Customer return, Internal transfer, Adjustment; Hỗ trợ chọn nhiều" (4 values) | `stub_receiving_po_asn#L53` R006 (4 values, multi-select) | `SUPPORTED` | Keep — enum đủ 4/4 |
| `07062#L378-L383` "Người sở hữu / Owner — Giá trị: Hasaki Cosmetics, Hasaki WMS, Hasaki OMS; Hỗ trợ chọn nhiều" (3 values) | `stub_receiving_po_asn#L54` R007 (3 values) | `SUPPORTED` | Keep — enum đủ 3/3; completeness flag Q-003 |
| `07062#L384-L395` "Trạng thái / Status — Mới/Open, Đang nhận hàng/Receiving, Đã nhận hàng/Received, Đã huỷ/Canceled" (4 values) | `stub_receiving_po_asn#L55` R008 (4 values) | `SUPPORTED` | Keep — enum đủ 4/4 |
| `07062#L396` "Đồng kiểm / Check of goods / Giá trị: Yes/No" | `stub_receiving_po_asn#L56` R009 (Yes/No, move từ inbound_shipment) | `SUPPORTED` | Keep — "move sang ASN" có dẫn chiếu chéo inbound_shipment R001 (cross-ref hợp lệ) |
| `07062#L398` "Từ ngày…Đến ngày / Form date…To date" | `stub_receiving_po_asn#L57` R010 | `SUPPORTED` | Keep — raw typo "Form date" (From date); spec sửa đúng |
| `07062#L402-L406` "In tất cả sản phẩm (Print all product) — Mặc định: chỉ in sản phẩm có khai báo thiếu hoặc SPKPH; Nếu tích chọn thì in hết tất cả sản phẩm đã nhận trong ASN" | `stub_receiving_po_asn#L58` R011 | `SUPPORTED` | Keep |
| `07062#L407-L414` "Thiết lập khổ giấy (Set paper size) — A5: template A5; In Bill: template in Bill; Mặc định: A5" | `stub_receiving_po_asn#L59` R012 (A5 + In Bill; default A5) | `SUPPORTED` | Keep — enum đủ 2/2 + default đúng |
| `07062#L415-L416` "Lưu ý: thông tin này sẽ được lưu theo máy tính local, chỉ cần chọn 1 lần sẽ apply cho sau đó, cho tới khi thay đổi" | `stub_receiving_po_asn#L60` R013 | `SUPPORTED` | Keep — storage mechanism flag Q-004 |
| `07062#L417-L443` Listing columns: Mã ASN, Kho, Loại, Mã phiếu nhập, Phiếu nhập nguồn, Mã phiếu xuất, Phiếu xuất nguồn, Người sở hữu, Đồng kiểm, Mã camera, Mã vị trí, Mã giỏ, Ngày tạo (YYYY-MM-DD HH:MM; người tạo email Hasaki), Ngày cập nhật, Trạng thái, Thao tác (16 cột) | `stub_receiving_po_asn#L61` R014 (16 columns) | `SUPPORTED` | Keep — đủ 16/16 cột |
| `07062#L441-L449` "để reopen ASN về lại trạng thái Open, và xoá nhân viên ra khỏi ASN. Button này chỉ show lên khi trạng thái ASN = 'Receiving' và user chưa scan nhận item nào. EN: Do you want to ReOpen for ticket ASN 1002240906000004?" | `stub_receiving_po_asn#L62` R015 (ReOpen; condition Receiving AND chưa scan; dialog `...ASN {asn_code}?`) | `MISSING_DETAIL` | Add detail — raw confirm dialog dùng giá trị mẫu `1002240906000004`; spec template-hoá thành `{asn_code}`. Templatization hợp lý nhưng nên ghi note giá trị mẫu gốc. Xem FIX-001 |
| `07062#L450-L452` "để in biên bản xác nhận nhận hàng với nhà cung cấp. Button này chỉ show lên khi trạng thái của ASN = 'Receiving' hoặc 'Received'" | `stub_receiving_po_asn#L63` R016 | `SUPPORTED` | Keep |
| `07062#L453-L454` "để xem biên bản giao hàng mà user upload lên khi nhận hàng cho PO" | `stub_receiving_po_asn#L64` R017 | `SUPPORTED` | Keep |
| `07062#L455-L465` "Biên bản nhận hàng PO theo ASN – template A5 / template in Bill. Lưu ý: thông tin Số hoá đơn sẽ lấy cột 'Taxcode' trên Inside - Thông tin Taxcode có thể trùng nếu là PO gift và PO gốc" | `stub_receiving_po_asn#L65` R018 | `SUPPORTED` | Keep — Taxcode duplicate handling flag Q-002 |
| `07062#L468-L476` "ASN detail – Updated, Thông tin chung - Bổ sung: Đồng kiểm/Check of goods, Camera, Mã vị trí/Location code" | `stub_receiving_po_asn#L66` R019 (3 field) | `SUPPORTED` | Keep — semantics `Camera` flag Q-006 |
| `07062#L477-L510` Danh sách sản phẩm columns: SKU, Barcode, Sản phẩm/Product name, SL xác nhận/Qty confirm, SL thực nhận/Qty received, SL thiếu/Qty missing, Vị trí/Location, Mô tả/Description, Trạng thái/Status (9 cột) | `stub_receiving_po_asn#L67` R020 (9 columns) | `SUPPORTED` | Keep — đủ 9/9 |
| `07062#L482-L484` "SL xác nhận / Qty confirm — Số lượng của SKU theo PO. Lưu ý: nếu 1 PO có nhiều phiên nhận thì vẫn ghi nhận theo số lượng trên PO" | `stub_receiving_po_asn#L68` R021 (= SL PO, không decrement theo phiên) | `SUPPORTED` | Keep |
| `07062#L485-L487` "SL thực nhận / Qty received — Số lượng thực nhận theo phiên nhận hàng. Lưu ý: nếu 1 PO có nhiều phiên nhận thì chỉ ghi nhận theo từng phiên nhận hàng" | `stub_receiving_po_asn#L69` R022 (per-session, không cumulative) | `SUPPORTED` | Keep |
| `07062#L488-L495` "SL thiếu / Qty missing — Số lượng còn thiếu so với PO. Lưu ý: nếu 1 PO có nhiều phiên nhận thì chỉ ghi nhận số lượng thiếu còn lại theo phiên nhận. VD: SKU A SL PO 10 — Lần 1 giao 5 → thiếu 5; Lần 2 giao 3 → thiếu 2" | `stub_receiving_po_asn#L70` R023 (Formula + Business rule; VD verbatim) | `SUPPORTED` | Keep — R023 prose + VD khớp raw verbatim |
| `07062#L488-L495` (VD trên — raw KHÔNG có công thức ký hiệu, chỉ có VD số) | `stub_receiving_po_asn#L113` BR row `SL thiếu (per phiên) = (SL PO - sum(SL thực nhận đã có)) — decremental` | `MISSING_DETAIL` | Add detail — công thức ký hiệu là derive từ VD, raw chỉ cho VD số. Faithful nhưng nên trích VD verbatim cạnh công thức. Xem FIX-002 |
| `07062#L496-L498` "Vị trí / Location — Mã bin mà user scan để nhận hàng vào với Shop 170 và Kho 170. Với Shop thì mặc định chuyển vào location mặc định" | `stub_receiving_po_asn#L71` R024 | `SUPPORTED` | Keep — scope Shop/Kho 170 flag Q-008 |
| `07062#L499-L508` "Mô tả / Description — Hiện các thông tin khi user khai báo lý do thiếu trên App: Lý do thiếu, Tình trạng hàng hoá (nếu có), Nhà cung cấp giao bù, Ghi chú" | `stub_receiving_po_asn#L72` R025 (4 thông tin) | `SUPPORTED` | Keep — placeholder khi không khai báo flag Q-010 |
| `07062#L512-L513` "16-09-2025: update xem chi tiết sản phẩm trong ASN - Bổ sung thông tin Group UID đã nhận cho ASN" | `stub_receiving_po_asn#L73` R026 | `SUPPORTED` | Keep — filter/search Group UID flag Q-009 |
| `07062#L448-L449` "EN: Do you want to ReOpen for ticket ASN 1002240906000004?" | `stub_receiving_po_asn#L120` MSG-ASN-001 (EN verbatim `...ASN {asn_code}?`, VN flag Q-005) | `SUPPORTED` | Keep — EN verbatim giữ template; VN missing đã flag Q-005 (pending-source hợp lệ) |
| AC-01..AC-18 (`stub_receiving_po_asn#L124-L195`) — map về R002-R026, ví dụ dùng giá trị mẫu hợp lệ | `stub_receiving_po_asn` AC block | `SUPPORTED` | Keep — 18 AC khớp R tương ứng; AC-15 dùng VD raw verbatim `10-5-3=2` |

**ASN: 28 critical claim SUPPORTED, 2 MISSING_DETAIL (R015 dialog placeholder, BR SL thiếu formula derive). 10 Q-ID hợp lệ (pending-source/scope/verbatim).**

---

## stub_receiving_po_invoice (raw L1497-L1674)

> Flag critical: validation_rule (R003-R008/R010/R015), error_messages (8 MSG/ERR), business_rule (R007/R013/R014/R017/R021), formula (R006/R007 total tolerance). Verify 100%.

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07062#L1499-L1502` "Sau khi kết thúc nhận hàng mà số lượng thực nhận đã đủ với số lượng confirm của PO, nếu PO chưa được bổ sung hoá đơn trên hệ thống, hiện button 'Thêm hoá đơn'" | `stub_receiving_po_invoice#L48` R001 | `SUPPORTED` | Keep |
| `07062#L1503-L1512` "User chọn 'Thêm hoá đơn', Show 2 lưu ý: lưu ý 1 — 'Kiểm tra lại' (tắt) / 'Xác nhận' (tiếp); lưu ý 2 — 'Kiểm tra lại' (tắt) / 'Tôi đã hiểu' (tiếp)" | `stub_receiving_po_invoice#L49` R002 | `SUPPORTED` | Keep — verbatim text 2 lưu ý flag Q-001 |
| `07062#L1516-L1527` "Tax code (mã số thuế) — Bắt buộc → 'Thông tin là bắt buộc'; MST phải từ 1 đến 8 ký tự bao gồm chữ và số, không bao gồm ký tự đặc biệt → 'Mã số thuế phải từ 1 đến 8 chữ số'" | `stub_receiving_po_invoice#L50` R003 (1-8 ký tự chữ+số, không đặc biệt) | `SUPPORTED` | Keep |
| `07062#L1528-L1538` "Serial (ký hiệu) — Bắt buộc; phải từ 1 đến 8 ký tự bao gồm chữ và số, không bao gồm ký tự đặc biệt → 'Ký hiệu phải từ 1 đến 8 chữ số'" | `stub_receiving_po_invoice#L51` R004 | `SUPPORTED` | Keep |
| `07062#L1539-L1543` "Form (mẫu số) — Bắt buộc, nếu không nhập hiện 'Thông tin là bắt buộc'" (KHÔNG nêu format) | `stub_receiving_po_invoice#L52` R005 (bắt buộc) | `SUPPORTED` | Keep — Form format flag Q-012 đúng (raw không nêu) |
| `07062#L1544-L1553` "Total (Tổng tiền) — Phải bằng hoặc chênh lệch với tổng tiền trên PO không quá 1.000 đồng, nếu không hiện 'Tổng số tiền tren hoá đơn không hợp lệ'" | `stub_receiving_po_invoice#L53` R006 (chênh ≤ 1.000 đồng) | `SUPPORTED` | Keep — đơn vị tiền flag Q-003 |
| `07062#L1554-L1561` "Lưu ý: nếu PO được add nhiều hoá đơn thì tổng tiền của các hoá đơn phải bằng tổng tiền trên PO hoặc không lệch quá 1.000 đồng" | `stub_receiving_po_invoice#L54` R007 (multi-invoice sum ≤ 1.000 đồng) | `SUPPORTED` | Keep — timing block flag Q-011 |
| `07062#L1562-L1564` "Ngày (mặc định ngày hiện tại, format YYYY-MM-DD), chỉ cho chọn ngày hiện tại hoặc quá khứ, không cho chọn ngày của tương lai" | `stub_receiving_po_invoice#L55` R008 | `SUPPORTED` | Keep — date picker behavior flag Q-002 |
| `07062#L1565` "Chọn 'Đóng' để tắt popup" | `stub_receiving_po_invoice#L56` R009 | `SUPPORTED` | Keep |
| `07062#L1566-L1568` "Chọn 'Thêm' để cập nhật thông tin hoá đơn (nếu chưa nhập đầy đủ thông tin thì cảnh báo nhập thông tin tương ứng)" | `stub_receiving_po_invoice#L57` R010 | `SUPPORTED` | Keep |
| `07062#L1569` "Nhập ghi chú" | `stub_receiving_po_invoice#L58` R011 (optional) | `SUPPORTED` | Keep — raw không nói required/optional; "optional" suy từ vị trí list (không có chữ "Bắt buộc"); chấp nhận được |
| `07062#L1570-L1572` "Hình ảnh hoá đơn: Chọn '+' để mở camera để chụp hình hoá đơn hoặc lấy hình từ thư viện ảnh (chụp tối đa 2 hình cho 1 hoá đơn)" | `stub_receiving_po_invoice#L59` R012 (max 2 hình) | `SUPPORTED` | Keep |
| `07062#L1573` "Lưu ý: user có thể thêm nhiều hoá đơn" | `stub_receiving_po_invoice#L60` R013 | `SUPPORTED` | Keep |
| `07062#L1578-L1583` "Khi nhận PO gốc và PO gift cùng lúc, nhưng cả 2 PO cùng yêu cầu add invoice thì khi user chọn add invoice hệ thống yêu cầu user chọn PO cần add invoice. Bước add và cập nhật tương tự chỉ add cho PO gốc" | `stub_receiving_po_invoice#L61` R014 | `SUPPORTED` | Keep — timeout/reminder PO còn lại flag Q-007 |
| `07062#L1586-L1589` "Button 'Hoàn thành PO' chỉ hiện lên khi tất cả thông tin của hoá đơn đã cập nhật đầy đủ thông tin bao gồm hình ảnh" | `stub_receiving_po_invoice#L62` R015 | `SUPPORTED` | Keep |
| `07062#L1598-L1601` "Nếu PO có PO gift đi kèm, sau khi scan PO thường thành công thì hiện cảnh báo. User phải scan PO Gift để nhận chung với PO thường" | `stub_receiving_po_invoice#L63` R016 | `SUPPORTED` | Keep — verbatim cảnh báo flag Q-009 |
| `07062#L1602-L1609` "Nếu PO không thuộc PO đang nhận → thông báo; Nếu PO chưa verify invoice (trừ PO Gift 0 đồng) → thông báo; Nếu PO đã Received → thông báo" | `stub_receiving_po_invoice#L64` R017 (3 validation) | `SUPPORTED` | Keep — định nghĩa PO Gift 0 đồng flag Q-006 |
| `07062#L1610-L1611` "Nếu PO hợp lệ thì hiện thông tin PO lên màn hình (PO 2)" | `stub_receiving_po_invoice#L65` R018 | `SUPPORTED` | Keep |
| `07062#L1612-L1613` "1.1 Chọn Loại nhận hàng cho PO — Tham khảo mô tả" | `stub_receiving_po_invoice#L66` R019 | `SUPPORTED` | Keep |
| `07062#L1617-L1621` "1.2 Scan vị trí hoặc giỏ cần chuyển hàng vào giống như ở case 1" | `stub_receiving_po_invoice#L67` R020 | `SUPPORTED` | Keep |
| `07062#L1622-L1631` "Scan sản phẩm tương tự PO thường. Lưu ý: nếu PO thường và PO Gift có cùng SKU — nếu scan 1 lần mà SL SKU không bằng tổng SL của 2 PO thì SL nhận sẽ ưu tiên cho PO Gift trước sau đó mới tới PO thường (để PO Gift luôn nhận đủ — dựa vào giá sản phẩm nhỏ hơn để phân biệt SKU PO Gift)" | `stub_receiving_po_invoice#L68` R021 | `SUPPORTED` | Keep — cùng giá flag Q-008 |
| `07062#L1635-L1636` "Khi chọn xem danh sách sản phẩm, do có 2 PO nên user sẽ chọn PO nào cần xem thông tin" | `stub_receiving_po_invoice#L69` R022 | `SUPPORTED` | Keep |
| `07062#L1641-L1647` "User chọn 'Thêm biên bản giao hàng' để cập nhật hình ảnh chứng từ. Nếu PO có đồng kiểm → chụp biên bản giao nhận hàng hoá; Nếu PO không đồng kiếm → chụp biên bản bàn giao kiện hàng" | `stub_receiving_po_invoice#L70` R023 | `SUPPORTED` | Keep — typo raw `kiếm` flag Q-005; spec dùng `kiểm` |
| `07062#L1644-L1655` Step 4 form fields: Kho, Tổng tiền, Không đồng kiểm/Đồng kiểm, Vị trí, Tổng SKU, Tổng sản phẩm, Ghi chú, Hình ảnh chứng từ (8 field) | `stub_receiving_po_invoice#L71` R024 (8 field) | `SUPPORTED` | Keep — đủ 8/8 |
| `07062#L1649-L1655` "Chọn icon camera để mở camera và chụp hình ảnh chứng từ; Hỗ trợ chụp tối đa 2 hình; Chọn 'Xoá hình' để xoá hình vừa chụp để chụp lại; user chọn 'Lưu' để lưu lại hình ảnh" | `stub_receiving_po_invoice#L72` R025 | `SUPPORTED` | Keep |
| `07062#L1657-L1662` "Update 20-11-2024: Bổ sung thêm biên bản giao hàng của PO Gift; Cập nhật đầy đủ hình ảnh của PO gốc và PO gift thì button 'Lưu' sẽ hiện lên" | `stub_receiving_po_invoice#L73` R026 | `SUPPORTED` | Keep |
| `07062#L1663-L1666` "Button 'Kết thúc nhận hàng' với case 2 PO đổi thành 'Kết thúc nhận hàng cả 2 PO'; Button 'Hoàn thành PO' với case 2 PO đổi thành 'Hoàn thành cả 2 PO'" | `stub_receiving_po_invoice#L74` R027 | `SUPPORTED` | Keep |
| `07062#L1667-L1668` "Thông báo xác nhận đổi thành" — raw bị cắt, không có nội dung tiếp theo | `stub_receiving_po_invoice#L75` R028 (verbatim không rõ — Q-010) | `UNCLEAR` | Move to Q — raw truncated; spec đã flag Q-010 đúng. Giữ R028 ở Blocked Coverage |
| `07062#L1519-L1520, L1531-L1532, L1542-L1543` "Thông tin là bắt buộc (Information is required.)" | `stub_receiving_po_invoice#L144` ERR-INV-001 | `SUPPORTED` | Keep — VN+EN verbatim |
| `07062#L1525-L1527` "Mã số thuế phải từ 1 đến 8 chữ số (Tax code must be from 1 to 8 digits)" | `stub_receiving_po_invoice#L145` ERR-INV-002 | `SUPPORTED` | Keep — verbatim. Lưu ý: message ghi "chữ số" trong khi rule R003 ghi "chữ và số" — mâu thuẫn nội tại của raw, chưa có Q-ID. Xem FIX-003 |
| `07062#L1537-L1538` "Ký hiệu phải từ 1 đến 8 chữ số (Serial must be from 1 to 8 digits)" | `stub_receiving_po_invoice#L146` ERR-INV-003 | `SUPPORTED` | Keep — verbatim; cùng mâu thuẫn "chữ số" vs "chữ và số" như ERR-INV-002 (FIX-003) |
| `07062#L1551-L1553, L1559-L1561` "Tổng số tiền tren hoá đơn không hợp lệ (Total amount on invoice is invalid)" (typo `tren`) | `stub_receiving_po_invoice#L147` ERR-INV-004 (typo `tren` flag Q-004) | `SUPPORTED` | Keep — verbatim giữ typo; Q-004 đúng |
| `07062#L1599-L1601` cảnh báo scan PO Gift (raw không có verbatim message text) | `stub_receiving_po_invoice#L148` MSG-INV-005 (verbatim missing — Q-009) | `UNCLEAR` | Keep — pending-source hợp lệ; Q-009 flag verbatim |
| `07062#L1602` "Nếu PO không thuộc PO đang nhận, hiện thông báo" (raw không có verbatim) | `stub_receiving_po_invoice#L149` MSG-INV-006 (Q-009) | `UNCLEAR` | Keep — pending-source; Q-009 |
| `07062#L1603-L1604` "Nếu PO chưa được verify invoice (trừ PO Gift 0 đồng), hiện thông báo" (raw không verbatim) | `stub_receiving_po_invoice#L150` MSG-INV-007 (Q-009) | `UNCLEAR` | Keep — pending-source; Q-009 |
| `07062#L1608-L1609` "Nếu PO đã được nhận hàng (status = Received), hiện thông báo" (raw không verbatim) | `stub_receiving_po_invoice#L151` MSG-INV-008 (Q-009) | `UNCLEAR` | Keep — pending-source; Q-009 |
| AC-01..AC-22 (`stub_receiving_po_invoice#L155-L242`) — map về R001-R027 | invoice AC block | `SUPPORTED` | Keep — 22 AC khớp R/ERR tương ứng; ví dụ số (1.499.500 chênh 500, 1.498.000 chênh 2000) đúng theo rule ≤1.000đ |

**Invoice: 31 critical claim SUPPORTED, 5 UNCLEAR hợp lệ (R028 truncated Q-010; MSG-INV-005..008 verbatim missing Q-009), 1 MISSING_DETAIL (mâu thuẫn nội tại raw "chữ số" vs "chữ và số", chưa có Q-ID → FIX-003).**

---

## Tổng kết batch-5

| Spec | Critical claims verified | SUPPORTED | UNCLEAR (hợp lệ) | MISSING_DETAIL | INFERRED/LOGIC/NEG/STRIP | PHANTOM | Verdict đề xuất |
|:-----|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| stub_receiving_po_overview | 12 | 12 | 0 | 0 | 0 | 0 | **PASS** |
| stub_receiving_po_asn | 30 | 28 | 0 | 2 | 0 | 0 | **PASS** |
| stub_receiving_po_invoice | 37 | 31 | 5 | 1 | 0 | 0 | **PASS** |

> **0 INFERRED / LOGIC_INFERRED / STRIPPED_CONDITION / NEGATION_FLIP / PHANTOM_EVIDENCE.** Tất cả deviation khỏi raw verbatim đã có Q-ID tương ứng (PATCH-001 compliant), trừ 1 raw-internal inconsistency (ERR "chữ số" vs rule "chữ và số") chưa có Q-ID → FIX-003 đề xuất thêm Q.
> 3 MISSING_DETAIL đều low-severity (templatization placeholder + formula derive faithful + raw inconsistency) — không block gate, có FIX suggestion.
