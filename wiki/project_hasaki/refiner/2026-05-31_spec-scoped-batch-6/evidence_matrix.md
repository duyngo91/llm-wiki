---
session: "2026-05-31"
batch: "spec-scoped-batch-6"
generated_at: "2026-05-31 21:10:00+07:00"
---

# Evidence Matrix — spec-scoped-batch-6

> Per-claim verification (raw-first). Format: Raw evidence (path#line) | Wiki claim (path#line) | Status | Action.
>
> Verify rule: 100% claims mapped đến sections có flag critical (enum / state_transition / formula / business_rule / error_messages / validation_rule); 1/5 sampling cho non-critical UI/nav.
> Raw source: `07062_Receiving_PO_Docs_ver2.17.md` (đọc raw range TRƯỚC spec — chống confirmation bias).
> PATCH-001 active: mọi deviation interpretive thiếu Q-ID → INFERRED/UNCLEAR.

---

## stub_receiving_po_vas (raw L522-L783)

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07062#L523` "Menu: Inbound / VAS" | `stub_receiving_po_vas#L50` R001 | `SUPPORTED` | Keep |
| `07062#L524-L528` SKU có Serial/Imei/Label không phải "Sức khoẻ - Làm đẹp" → xác nhận dán ID; nhận PO chỉ scan SL, không khai báo Serial/Imei/Label | `#L51` R002 | `SUPPORTED` | Keep |
| `07062#L530-L532` "Sức khoẻ - Làm đẹp" có serial/imei → ASN Received → auto sinh VAS + auto completed; chỉ update serial khi đóng đơn | `#L52` R003 | `SUPPORTED` | Keep |
| `07062#L534-L536` TSCĐ/CCDC/CCDC PB có Serial/Imei/Label → ASN Received → sinh 1 VAS tương ứng ASN status = Open | `#L53` R004 | `SUPPORTED` | Keep |
| `07062#L537-L543` UID sau received status "Received", chưa auto In-Bin, không picklisted cho order/receipt/IT; sau xác nhận chụp hình/dán ID → Received → In-Bin | `#L54` R005 | `SUPPORTED` | Keep |
| `07062#L547-L577` Select filter fields (Mã VAS, Mã phiếu nhập, Phiếu nhập nguồn, Mã phiếu xuất, Phiếu xuất nguồn, Loại, Kho, SKU/Barcode, Người sở hữu, Trạng thái, Từ ngày…đến ngày) | `#L55` R006 | `SUPPORTED` | Keep |
| `07062#L564,L571-L575` Trạng thái default Null; 4 values (Mới/Open, Đang xử lý/In-Progress, Hoàn thành/Completed, Đã huỷ/Canceled); "Hỗ trợ chọn nhiều" | `#L56` R007 (enum 4/4) | `SUPPORTED` | Keep — enum completeness 4/4 khớp |
| `07062#L580-L621` Listing columns (TT, Mã VAS, Kho, Loại, Mã ASN hyperlink, Mã phiếu nhập hyperlink, Phiếu nhập nguồn hyperlink PO Inside, Mã phiếu xuất, Phiếu xuất nguồn, Vị trí, Người tạo, Người thực hiện, Ngày cập nhật, Trạng thái, Thao tác) | `#L57` R008 | `SUPPORTED` | Keep |
| `07062#L594-L601` Vị trí nhận theo ASN; cùng phiên 1 SKU vào 2 location → sinh VAS tương ứng; SKU yêu cầu serial chỉ hiện SKU có yêu cầu serial | `#L58` R009 | `SUPPORTED` | Keep |
| `07062#L607-L614` Trạng thái enum: Open (ASN received sinh VAS cho TSCĐ/CCDC/CCDC PB có Serial/Imei/Label); In-Progress ("có ít nhất 1 SKU có số lượng đã dán > 1"); Completed; Canceled | `#L59` R010 | `SUPPORTED` | Keep — "đã dán > 1" khớp verbatim raw (xem Q-006 đã flag edge) |
| `07062#L615-L621` Button cập nhật Serial/Imei/Label (chỉ show VAS status Open và In-Progress); Button xem chi tiết VAS | `#L60` R011 | `SUPPORTED` | Keep |
| `07062#L630-L653` VAS detail Thông tin chung dạng text (Kho, Loại, ASN, Mã phiếu nhập, Phiếu nhập nguồn, Mã phiếu xuất, Phiếu xuất nguồn, Vị trí, Ngày tạo, Người tạo, Ngày cập nhật) | `#L61` R012 | `SUPPORTED` | Keep |
| `07062#L654-L664` Danh sách SP chỉ hiện SKU có quản lý serial; cột SKU, Barcode, Sản phẩm, SL thực nhận, SL đã dán, Hình ảnh/Video, Thao tác | `#L62` R013 | `SUPPORTED` | Keep |
| `07062#L665-L673` Button cập nhật (chỉ Open/In-Progress); Button xem chi tiết Serial/Imei/Label theo SKU | `#L63` R014 | `SUPPORTED` | Keep |
| `07062#L674-L677` Chọn button trên dòng SKU → cập nhật; hệ thống auto chọn thông tin cần cập nhật | `#L64` R015 | `SUPPORTED` | Keep |
| `07062#L678-L681` Cate CCDC/CCDC PB: `wms_config&131072 > 0` → required QR (ON QRCode); `config&8 > 0` → required Imei (ON Serial/Imei) | `#L65` R016 | `SUPPORTED` | Keep — config flags verbatim (Q-002 pending dev) |
| `07062#L682-L685` Cập nhật 25-02-2025: luôn tắt option Serial dưới BE, user chỉ cần QRCode, sau này mở | `#L66` R017 | `SUPPORTED` | Keep |
| `07062#L686-L689` Serial không có info → WMS tự gen `[1023][YYMMDD][6 số tăng dần]`; count lại theo Serial → update đè | `#L67` R018 | `SUPPORTED` | Keep — pattern verbatim (Q-004 pending semantic) |
| `07062#L690-L691` "Ngược lại với 2 case trên thì chỉ cần chụp hình, bỏ qua bước cập nhật QRCode hoặc Serial" | `#L68` R019 | `SUPPORTED` | Keep |
| `07062#L692-L694` QRCode in dạng Object → tự cắt chuỗi; "Lấy thông tin Code trong object" | `#L69` R020 | `SUPPORTED` | Keep |
| `07062#L698-L703` Thông tin tích chọn → ô scan show; 1 info: scan tự add / nhập nhấn `+`; 2 info: scan QR hợp lệ → auto chuyển focus qua ô Serial/Imei | `#L70` R021 | `SUPPORTED` | Keep |
| `07062#L704-L711` Validation Serial (trùng danh sách / trùng hệ thống / "phải từ 16 ký tự") | `#L71` R022 | `SUPPORTED` | Keep |
| `07062#L712-L717` Validation QRCode (trùng hệ thống / trùng danh sách / "không tồn tại trên hệ thống HR") | `#L72` R023 | `SUPPORTED` | Keep |
| `07062#L722-L724` Search gần đúng (nhập từ 3 ký tự) cho QRCode/Serial; chỉnh sửa chọn icon → validation giống scan mới | `#L73` R024 | `SUPPORTED` | Keep |
| `07062#L725-L731` "Đóng" tắt thông báo; "Lưu" lưu thông tin; SL xác nhận dán = SL đã nhận (cần dán) của TẤT CẢ SKU trong VAS → button Complete show → EN "Do you want to confirm pasting ID completion?" | `#L74` R025 | `SUPPORTED` | Keep |
| `07062#L736-L742` Update 16-09-2025: Group UID + QC results cho type Quality control; "1 SKU nhận trong ASN theo group UID sẽ lấy ra 10% để thực hiện đánh giá, nếu ra số lẻ thì làm tròn lên" | `#L75` R026 | `SUPPORTED` | Keep |
| `07062#L740-L742` "VD: SKUA nhận trong ASN là 25 group UID thì 10% là 2,5 làm tròn thành 3, tức sẽ có 3 dòng VAS cần đánh giá chất lượng cho SKUA" | `#L76` R027 | `SUPPORTED` | Keep — ví dụ verbatim |
| `07062#L743-L745` "Trong VAS Quality control bổ sung thêm Group UID và kết quả đánh giá theo group UID; Chỉ cần có 1 kết quả Failed thì ghi nhận là Failed" | `#L77` R028 | `SUPPORTED` | Keep (scope Failed → Q-008 đã flag) |
| `07062#L746-L747` VAS sinh khi user chưa đánh giá → Group UID = trống; đã đánh giá → Group UID = thông tin scan vào | `#L78` R029 | `SUPPORTED` | Keep |
| `07062#L751-L754` Update 05-03-2025 + 05-05-2026: PO không đồng kiểm có SPKPH — Shop khai báo bình thường, hệ thống ghi nhận như nhận thiếu + nhận lại phiên sau; "Luồng xử lý SPKPH cho luồng nhận PO tạm Off không sử dụng" | `#L79` R030 | `SUPPORTED` | Keep (flow Off → Q-010 đã flag) |
| `07062#L757-L766` SKU bình thường → 1 ASN riêng + Received + import stock; SKU SPKPH → 1 ASN status Waiting for approval; nhiều SKU SPKPH cùng phiên → 1 phiên ASN riêng; không import stock cho SKU SPKPH | `#L80` R031 | `SUPPORTED` | Keep |
| `07062#L770-L773` Action Cancel → Xác nhận → UID chuyển "chưa nhận" để scan lại / khai báo thiếu + NCC không giao lại để Completed PO; ASN = Cancel | `#L81` R032 | `SUPPORTED` | Keep |
| `07062#L774-L777` Action Reject → SP khai báo SPKPH qua "sản phẩm chưa nhận"; user scan nhận lại như SP bình thường; ASN = Reject | `#L82` R033 | `SUPPORTED` | Keep |
| `07062#L778-L785` Action Approve → ASN = Chờ NCC đến lấy (Waiting for vender to pick); shop quản lý hàng vật lý chờ NCC; quá 7 ngày NCC chưa lấy → tiêu huỷ theo quy trình; user xác nhận NCC lấy hàng / tiêu huỷ qua App WMS | `#L83` R034 | `SUPPORTED` | Keep |
| `07062#L706-L707` "Serial 11333787241140438102 đã tồn tại trong danh sách." / "...already exists in the list." | `#L183` ERR-VAS-001 | `SUPPORTED` | Keep — verbatim VN+EN khớp |
| `07062#L708-L709` "Serial 11333787241140438102 đã tồn tại trên hệ thống." / "...already exists on the system." | `#L184` ERR-VAS-002 | `SUPPORTED` | Keep |
| `07062#L710-L711` "Serial 1133378724121 không hợp lệ (phải từ 16 ký tự)" / "...is invalid (must be 16 characters or more)" | `#L185` ERR-VAS-003 | `SUPPORTED` | Keep |
| `07062#L712-L713` "QRCode UEA1JDJ3 đã tồn tại trên hệ thống." / "...already exists on the system." | `#L186` ERR-VAS-004 | `SUPPORTED` | Keep |
| `07062#L714-L715` "QRCode UEA1JDJ3 đã tồn tại trong danh sách." / "...already exists in the list." | `#L187` ERR-VAS-005 | `SUPPORTED` | Keep |
| `07062#L716-L717` "QRCode UEA1JDJ3 không tồn tại trên hệ thống HR." / "...does not exist on the HR system." | `#L188` ERR-VAS-006 | `SUPPORTED` | Keep |
| `07062#L730-L731` Raw chỉ có "EN: Do you want to confirm pasting ID completion?" — không có VN verbatim | `#L189` MSG-VAS-007 | `UNCLEAR` (pending-source) | Keep — đã flag Q-001 + Blocked Coverage. Raw thực sự thiếu VN. Đúng cách xử lý |

**VAS — Sampling non-critical (1/5 UI/flow claims):** AC-01..AC-27 derive trực tiếp từ R001-R034 đã verify; spot-check AC-12 (Serial gen ví dụ `1023260530000001`), AC-20 (ceil(25×10%)=3) — đều là worked-example từ raw verbatim VD, không generalize beyond raw. `SUPPORTED`.

---

## stub_receiving_po_fabric (raw L1676-L1737)

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07062#L1676-L1686` "Nhận hàng Vải khai báo Group UID"; áp dụng SKU không quản lý theo UID, category Thời trang (BTP)/(Phụ liệu)/(NVL); "Trong tên sản phẩm có từ 'Vải'" | `stub_receiving_po_fabric#L48` R001 | `SUPPORTED` | Keep |
| `07062#L1688` "Nếu SKU không quản lý số lô và hạn sử dụng, hiện thông tin cho user cập nhật" + L1692/L1702 form 2 input (Nhóm UID + Số lượng) | `#L49` R002 | `SUPPORTED` | Keep |
| `07062#L1692-L1695` "Nhóm UID: scan nhóm UID đại diện cho cây/tấm vải; Không bắt buộc; nếu không khai báo UID group thì chỉ cần nhập số lượng và xác nhận như nhận SKU số lượng bình thường" | `#L50` R003 | `SUPPORTED` | Keep |
| `07062#L1696-L1697` "Nhóm UID scan vào phải có trạng thái New, không đúng thì báo lỗi" | `#L51` R004 | `SUPPORTED` | Keep |
| `07062#L1698` "10-11-2025: có thể chuyển qua scan RFID mapping" | `#L52` R005 | `SUPPORTED` | Keep |
| `07062#L1699-L1701` "nếu chỉ khai báo số lượng và chọn + để thêm vào danh sách thì input Nhóm UID và số lượng sẽ ẩn đi và không cho thêm mới... 1 SKU chỉ có thể nhận hoặc theo RFID mapping/UID Group hoặc là theo số lượng, không thể nhận cùng lúc 2 loại cho 1 SKU" | `#L53` R006 | `SUPPORTED` | Keep — mutex rule verbatim |
| `07062#L1702-L1704` "Số lượng: là số Kg hoặc Mét của cây/tấm vải được quy đổi ra số lượng; sẽ cộng lại cho tất cả cây/tấm vải để ra tổng SL của SKU cần nhận cho PO" | `#L54` R007 | `SUPPORTED` | Keep (conversion factor → Q-004 đã flag) |
| `07062#L1705` "Sau khi scan nhận, chọn xác nhận để ghi nhận vào danh sách" | `#L55` R008 | `SUPPORTED` | Keep |
| `07062#L1709-L1717` "Nếu SKU có quản lý số lô và hạn sử dụng, hiện thông tin..." form gồm Nhóm UID, Số lượng, + cập nhật số lô và HSD | `#L56` R009 | `SUPPORTED` | Keep |
| `07062#L1722` Heading-only "Update màn hình chi tiết sản phẩm của các sản phẩm đã nhận đủ số lượng" — KHÔNG có content chi tiết dưới | `#L57` R010 | `UNCLEAR` (pending-source) | Keep — đã flag Q-005 + Blocked. Raw thật sự chỉ có heading. Đúng cách xử lý |
| `07062#L1726-L1727` "Update 10-12-2025: Với những SKU có quản lý UID group, user có thể scan nhận bằng RFID mapping" | `#L58` R011 | `SUPPORTED` | Keep |
| `07062#L1728-L1730` Case 1: "Nếu RFID mapping chưa tồn tại trên hệ thống thì giống khai báo 1 UID group mới như luồng ban đầu, khi user submit hệ thống tự gen 1 UID group mới và mapping với RFID scan vào" | `#L59` R012 | `SUPPORTED` | Keep |
| `07062#L1731-L1734` Case 2: "Nếu RFID mapping hoặc UID group đã tồn tại (chạy cho luồng Transfer company, khi RFID/UID group ở công ty xuất đã được out ra) hệ thống suggest số lượng SP của UID group và cho phép user edit số lượng theo UID group; submit → gen 1 UID group mới + mapping RFID" | `#L60` R013 | `SUPPORTED` | Keep (Transfer company def → Q-006 đã flag) |
| `07062#L1696-L1697` Raw chỉ nói "không đúng thì báo lỗi" — KHÔNG có verbatim VN/EN message | `#L126` ERR-FAB-001 | `UNCLEAR` (pending-source) | Keep — đã flag Q-001 + Blocked. Raw thật sự thiếu verbatim. KHÔNG bịa message. Đúng cách xử lý |
| `07062#L1699-L1701` Raw mô tả behavior "input ẩn đi, không cho thêm mới" — KHÔNG có verbatim message text; chưa rõ có hiện message hay chỉ ẩn UI ngầm | `#L127` ERR-FAB-002 | `UNCLEAR` (pending-source) | Keep — đã flag Q-002 (kèm câu hỏi "hệ thống có hiện message hay chỉ ẩn UI ngầm?") + Blocked. KHÔNG bịa. Đúng cách xử lý |

**FABRIC — Sampling non-critical:** AC-01..AC-12 derive từ R001-R013. Spot-check AC-12 (`#L175-L178`): "Flow Update 10-12-2025 không apply cho SKU không quản lý UID group" + "chỉ apply Update 10-11-2025" → flag Q-003 (xem dưới — interpretive deviation, đã có Q-ID). AC-06 (40+35+25=100 Mét) là worked-example trung thành với R007. `SUPPORTED` (trừ AC-12 xem dòng riêng).
| `07062#L1698 vs L1726-L1727` Raw nêu 2 update riêng (10-11-2025 RFID cho SKU không quản lý UID; 10-12-2025 RFID cho SKU CÓ quản lý UID group), nhưng raw KHÔNG mô tả explicit hành vi khi SKU không quản lý UID group cố dùng flow 10-12-2025 (tự gen UID mới) | `#L175-L178` AC-12 (kết luận "flow 10-12-2025 không apply... không tự gen mới") | `MISSING_DETAIL` (đã trace Q-003) | Keep — AC-12 đã đính Q-003 ("đúng diễn giải? hay cùng 1 flow?"). Deviation interpretive có Q-ID → tuân PATCH-001, không phạt. Đề xuất FIX-002 soft (đánh dấu AC-12 là provisional tới khi Q-003 answered) |

---

## stub_receiving_po_app (raw L784-L1069)

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `07062#L786-L787` "App – Confirm Unsuitable Product"; "Vào mục Purchase order / Confirm Unsuitable Product" | `stub_receiving_po_app#L49` R001 | `SUPPORTED` | Keep |
| `07062#L788-L798` Chọn kho → danh sách ASN SPKPH status "Chờ NCC đến lấy" của kho; info: Mã PO, Thời gian tạo PO, Mã ASN, Tổng SKU, Tổng sản phẩm | `#L50` R002 | `SUPPORTED` | Keep (raw L793 typo "Mã ANS" → spec sửa "Mã ASN", trivial OCR typo) |
| `07062#L799-L823` Chọn phiên → Mã PO, Mã ASN, SKU, Qty, Danh sách SP (Tên SP, SKU/Barcode, Số lượng SPKPH, Ghi chú); Chọn phương án xử lý (default Null, values: Đã trả Nhà cung cấp, Đã tiêu huỷ); Ghi chú; Hình ảnh và video bằng chứng | `#L51` R003 | `SUPPORTED` | Keep — enum phương án 2/2 (Số lượng SPKPH vs Số lượng → Q-012 đã flag) |
| `07062#L824-L826` "Sau khi cập nhật đầy đủ + chụp hình → Chọn Hoàn thành và xác nhận → Cập nhật status của ASN theo phương án xử lý" | `#L52` R004 | `SUPPORTED` | Keep |
| `07062#L834-L838` User login App với tài khoản được cung cấp; vào tính năng "Receiving PO" | `#L53` R005 | `SUPPORTED` | Keep |
| `07062#L841-L843` Step 1: Hiện hướng dẫn ở màn hình scan PO; "thông tin này sẽ mặc định show khi user mới vào chức năng Receiving PO" | `#L54` R006 | `SUPPORTED` | Keep |
| `07062#L847-L854` Step 2: PO không yêu cầu VAT → bỏ qua check verify invoice và force Invoice; PO có yêu cầu VAT chưa verify/approve hoặc không tồn tại → thông báo | `#L55` R007 | `SUPPORTED` | Keep |
| `07062#L855-L860` PO không thuộc kho đang xử lý → thông báo; PO chưa verify invoice → thông báo; PO đã received → thông báo | `#L56` R008 | `SUPPORTED` | Keep |
| `07062#L861-L882` PO hợp lệ → show info (Mã PO chính PO 1, PO Gift PO 2, Tổng tiền, Tổng SKU, Tổng sản phẩm); tạo ASN (ASN number tự sinh, Type=Purchase Order, Inbound Shipment, Outbound Order, Status=Receiving); "Lưu ý khi này chưa gọi API để update status PO trên Inside thành Receiving" | `#L57` R009 | `SUPPORTED` | Keep (API timing → Q-001 đã flag) |
| `07062#L883-L886` Update 05-01-2026: "khi scan PO nếu có 1 SKU thoả điều kiện trong PO có qty < 100.000 thì hiện thông báo và không cho nhận (không chuyển PO qua receiving); các PO thuộc rules này vẫn cho nhận bình thường" | `#L58` R010 | `SUPPORTED` | Keep — "qty < 100.000" verbatim (đơn vị → Q-005 đã flag) |
| `07062#L887-L889` "Bổ sung filter các PO thoả điều kiện này; Filter VN: Cho phép nhận PO có SKU bất thường; Filter EN: Force receiving PO with abnormal SKUs" | `#L59` R011 | `SUPPORTED` | Keep — verbatim VN+EN |
| `07062#L890-L893` "Thông báo xác nhận VN: Bạn có muốn xác nhận cho phép nhận PO có SKU bất thường không? EN: Do you want to confirm allowing receiving PO with abnormal SKUs?" | `#L60` R012 | `SUPPORTED` | Keep — verbatim VN+EN |
| `07062#L895` "Bổ sung nút force cho các PO thoả điều kiện này để có thể force cho nhận nếu cần" | `#L61` R013 | `SUPPORTED` | Keep (raw L895; spec source ghi L885-L895 — range bao trùm đúng) |
| `07062#L903-L916` Step 3: chọn loại nhận hàng; Không đồng kiểm (No check of goods) → scan dưới camera → bước 4; Có đồng kiểm (check of goods) → bỏ qua scan camera; shop quản lý location → scan vị trí; shop không quản lý → scan SP | `#L62` R014 | `SUPPORTED` | Keep — enum 2/2 (raw EN "check of goods", spec "Check of goods" — capitalize trivial) |
| `07062#L915-L916` "Chọn đóng để tắt popup và quay lại màn hình scan PO cần nhận (bước 2)" | `#L63` R015 | `SUPPORTED` | Keep |
| `07062#L918-L923` Step 4: Scan mã camera; "User chỉ phải scan camera nếu PO đó là Không đồng kiểm"; Field Scan mã camera / Scan camera code; hiển thị Tổng tiền, Loại nhận hàng (Receiving type) | `#L64` R016 | `SUPPORTED` | Keep (raw EN "Total amount" → spec "Tổng tiền" hiển thị) |
| `07062#L921-L935` Update 18-02-2025: config "Required camera" tại Master data/Warehouse/view Warehouse config/Tab Configuration/Group "General"; "Mặc định = No: không cần scan camera cho chức năng được xét điều kiện này" | `#L65` R017 | `SUPPORTED` | Keep |
| `07062#L936-L940` Update 18-02-2025: chọn "Không đồng kiểm" — Required camera = Yes → phải scan camera; = No → bypass bước scan camera (giống case PO "Đồng kiểm") | `#L66` R018 | `SUPPORTED` | Keep |
| `07062#L945-L950` Validation mã camera không thuộc kho/không tồn tại → VN "Mã camera không hợp lệ hoặc không tồn tại trên hệ thống." / EN "Camera code is invalid or does not exist on the system." | `#L67` R019 / `#L170` ERR-APP-001 | `SUPPORTED` | Keep — verbatim VN+EN |
| `07062#L951-L956` Mã camera hợp lệ → shop quản lý location → scan mã vị trí / chọn chuyển vào giỏ; shop không quản lý → scan SP | `#L68` R020 | `SUPPORTED` | Keep |
| `07062#L957-L960` Step 5: scan vị trí/mã giỏ chỉ nếu shop/kho quản lý location; "Hệ thống tự động detect... là mã Bin hay mã giỏ" | `#L69` R021 | `SUPPORTED` | Keep |
| `07062#L961-L966` PO zone: sau scan camera (nếu có) → thông báo lưu ý; "với PO zone chỉ được phép chuyển hàng vào các location có type Di động, không được chuyển vào giỏ hoặc location khác" | `#L70` R022 | `SUPPORTED` | Keep (def PO zone → Q-007 đã flag) |
| `07062#L970-L981` PO zone: vị trí không thuộc kho/không tồn tại → "Vị trí không hợp lệ hoặc không tồn tại trên hệ thống." / "Location code is invalid..."; không bin Di động → "Vị trí F2-AP-01-01-01-01 không được thiết lập để lưu trữ hàng cho PO zone." / "Location F2-AP-01-01-01-01 is not setup to storage for PO zone." | `#L71` R023 / `#L171` ERR-APP-002 / `#L172` ERR-APP-003 | `SUPPORTED` | Keep — verbatim VN+EN khớp (ERR-APP-003 mã VN==EN==F2-AP-01-01-01-01, consistent) |
| `07062#L982-L984` PO zone: vị trí hợp lệ → scan SP; "Nếu user scan mã giỏ, hiện thông báo" — KHÔNG verbatim message | `#L72` R024 | `UNCLEAR` (pending-source) | Keep — đã flag Q-003 + Blocked. Raw thật sự chỉ nói "hiện thông báo". Đúng cách xử lý |
| `07062#L985-L994` PO thường: nhận vào bất kỳ location; vị trí không thuộc kho/không tồn tại → "Vị trí không hợp lệ hoặc không tồn tại trên hệ thống." / "Location code is invalid or does not exist on the system." | `#L73` R025 | `SUPPORTED` | Keep — verbatim VN+EN |
| `07062#L997-L1002` PO thường: vị trí config bin Di động → VN "Vị trí F0-A1-PL-50-01-01 là bin Di động, nên không thể lưu trữ hàng cho PO." / EN "Location F2-AP-01-01-01-01 is not setup to storage for PO." — **raw có inconsistency**: mã VN (F0-A1-PL-50-01-01) ≠ mã EN (F2-AP-01-01-01-01) VÀ nội dung VN ("là bin Di động") ≠ EN ("is not setup to storage") | `#L74` R026 / `#L173` ERR-APP-004 | `UNCLEAR` (raw self-contradiction, đã trace Q-004) | Keep — spec quote CẢ 2 verbatim đúng + đính Q-004 ("Raw có inconsistency... Đúng verbatim 2 ngôn ngữ là gì?") + Blocked. KHÔNG bịa/normalize. Đây là raw tự mâu thuẫn, spec xử lý đúng (xem L_root_cause watch-item) |
| `07062#L1005-L1018` Mã giỏ không thuộc kho/không tồn tại → "Mã giỏ không hợp lệ hoặc không tồn tại trên hệ thống." / "Cart code is invalid or does not exist on the system."; status khác Available hoặc Transfer Bin → "Mã giỏ 404005 có trạng thái không hợp lệ." / "Cart code 404005 has invalid status." | `#L75` R027 / `#L174` ERR-APP-005 / `#L175` ERR-APP-006 | `SUPPORTED` | Keep — enum status giỏ {Available, Transfer Bin} 2/2 verbatim (đầy đủ enum → Q-008 đã flag) |
| `07062#L1019-L1026` Update 27-02-2024: "1 Bin location sẽ có thông tin stock_id và location_id (bổ sung); 1 Bin location sử dụng chung cho nhiều stock trong cùng location_id (VD Bin A: Shop 170 QL1A, WH 170 QL1A, WH 170 QL1A KT1... cùng location 170 QL1A); Ở 1 thời điểm Bin A chỉ thuộc 1 stock duy nhất" | `#L76` R028 | `SUPPORTED` | Keep (stock_id semantics → Q-009 đã flag) |
| `07062#L1027-L1035` Update 27-02-2024: trước nhận Bin A thuộc Shop 170 QL1A; PO thuộc Shop 170 QL1A → nhận bình thường; PO thuộc WH 170 QL1A → check: Bin A còn UID → báo lỗi không cho nhận; Bin A không còn hàng → cho nhận + cập nhật stock_id từ Shop 170QL1A thành WH 170QL1A | `#L77` R029 | `SUPPORTED` | Keep |
| `07062#L1038-L1044` Case 1 (PO thường không Gift): nhập SL + scan SKU; Field Tổng tiền/Total Amount, Tổng SKU/Total SKU, Tổng sản phẩm/Total item; SKU không trong PO → "SKU 100540031 không có trong PO." / "SKU 100540031 is not in PO." | `#L78` R030 / `#L176` ERR-APP-007 | `SUPPORTED` | Keep — verbatim VN+EN |
| `07062#L1045-L1050` SL vượt quá SL confirm → "Số lượng của SKU 100540031 lớn hơn số lượng cần nhận trong PO." / "The quantity of SKU 100540031 is greater than the quantity required in the PO." | `#L79` R031 / `#L177` ERR-APP-008 | `SUPPORTED` | Keep — verbatim VN+EN |
| `07062#L1051-L1057` SKU hợp lệ: không yêu cầu date → cập nhật info + SL lên màn hình; yêu cầu date → show form nhập HSD; "Số lượng: lấy từ thông tin nhập ở màn hình scan SKU và cho phép chỉnh sửa" | `#L80` R032 | `SUPPORTED` | Keep (re-validate SL → Q-011 đã flag) |
| `07062#L1061-L1069` HSD nhỏ hơn yêu cầu → "Hạn sử dụng nhỏ hơn yêu cầu được phép nhận hàng của PO (9 tháng)." / "Expiration date is less than the PO permission request (9 months)" | `#L81` R033 / `#L178` ERR-APP-009 | `SUPPORTED` | Keep — verbatim VN+EN ("9 tháng" configurable → Q-010 đã flag) |
| `07062#L890-L893` MSG confirm force | `#L179` MSG-APP-010 | `SUPPORTED` | Keep — verbatim VN+EN khớp R012 |

**APP — Sampling non-critical:** AC-01..AC-25 derive trực tiếp từ R001-R033. Spot-check AC-14/AC-15 (PO zone vs PO thường location), AC-17..AC-19 (Bin Di động switch stock) — đều khớp R022-R029 verbatim, không generalize. `SUPPORTED`.

---

## Tổng kết labels

| Spec | SUPPORTED | UNCLEAR (pending-source) | MISSING_DETAIL | INFERRED | LOGIC_INFERRED | STRIPPED | NEGATION | PHANTOM | POTENTIAL_OMISSION |
|:-----|:---------:|:------------------------:|:--------------:|:--------:|:--------------:|:--------:|:--------:|:-------:|:------------------:|
| VAS | 39 | 1 (MSG-VAS-007 Q-001) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| FABRIC | 24 | 3 (ERR-FAB-001 Q-001, ERR-FAB-002 Q-002, R010 Q-005) | 1 (AC-12, trace Q-003) | 0 | 0 | 0 | 0 | 0 | 0 |
| APP | 35 | 2 (R024 Q-003, ERR-APP-004 Q-004) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **98** | **6** | **1** | **0** | **0** | **0** | **0** | **0** | **0** |

> Toàn bộ deviation interpretive đều có Q-ID (PATCH-001 tuân thủ 100%). 0 violation severity ≥ INFERRED. 6 UNCLEAR đều là pending-source hợp lệ (raw thật sự thiếu verbatim / heading-only / raw tự mâu thuẫn) — KHÔNG phạt điểm theo scoring rule. 1 MISSING_DETAIL low-severity (AC-12 interpretive đã trace Q-003).
