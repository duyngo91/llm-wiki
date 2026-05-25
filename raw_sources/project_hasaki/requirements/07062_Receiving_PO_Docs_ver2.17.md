|     |     |     |     | 1   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
 Warehouse Management System
Nhận hàng PO
I.  Document Approva
| Baseline Version  |     | Approved Date  |     | Reviewer  |     | Approver  |
| ----------------- | --- | -------------- | --- | --------- | --- | --------- |
| 1.0               |     |                |     |           |     |           |
II.  Document Revision History
| Version  | Date        |     | Author       |           | Change Description  |     |
| -------- | ----------- | --- | ------------ | --------- | ------------------- | --- |
| 1.0      | 13-08-2024  |     | Phù Minh Tú  | Creation  |                     |     |
| 1.0      | 20.08-2024  |     | Phù Minh Tú  | Updated   |                     |     |
-  Update lại UI luồng thêm biên bản giao hàng và thêm
hoá đơn
| 1.1  | 06-09-2024  |     | Phù Minh Tú  | Update giao diện 1 số màn hình  |     |     |
| ---- | ----------- | --- | ------------ | ------------------------------- | --- | --- |
1.2  07-10-2024  Phù Minh Tú  Update giao diện 1 số màn hình trên Web
-  Inbound shipment:
•  Bỏ thông tin “Đồng kiểm” => chuyển qua màn
hình ASN
•  Bỏ thông tin “WMS status”
•
Detail: bổ sung thêm thông tin: SL đã nhận, SL
thiếu
-  ASN:
•  Bổ sung thông tin “Đồng kiểm” ở filter, data
table và detail
1.3  15-10-2024  Phù Minh Tú  Update 1 số màn hình phát sinh trên App
-  Xoá SKU có HSDK hoặc Serial đã scan nhận
-  Xoá thông tin khai báo lý do thiếu hàng

2
1.3 16-10-2024 Phù Minh Tú Đổi lại bước gọi Inside update PO Receiving
- Hiện tại: khi scan PO thành công
- Update: Khi kết thúc nhận hàng
Update lại luồng gọi update Inside khi complete PO phát sinh
item thiếu hoặc sản phẩm không phù hợp
1.4 24-10-2024 Phù Minh Tú Khai báo sản phẩm không phù hợp bổ sung thêm cập nhật hạn
sử dụng cho sản phẩm
1.5 02-11-2024 Phù Minh Tú Bổ sung xem ghi chú của PO
Bỏ qua scan location nếu nhận PO zone ở kho 170
1.6 20-11-2024 Phù Minh Tú Update
- Hỗ trợ cho khai báo thiếu hàng cho tất cả SKU chưa
nhận đủ SL theo PO
- Bổ sung biên bản nhận hàng cho PO Gift kèm PO gốc
- Bổ sung tính năng xác nhận dán ID cho SKU là Tài sản
cố định có quản lý Serial/Imei
- Update VAS và cho cập nhật serial/imei/label code cho
sản phẩm
1.7 25-11-2024 Phù Minh Tú Update
- Bổ sung cho phép nhận riêng PO gift, với case PO gốc
có nhiều PO gift thì hiện thông báo yêu cầu nhận hết
PO gift (nhận riêng) sau đó mới nhận PO gốc
- Bổ sung add invoice cho PO gift nếu có yêu cầu
• Bổ sung thêm thông tin PO cho invoice
1.8 06-12-2024 Phù Minh Tú Bổ sung tiện ích xoá sản phẩm đã scan nhận trước đó
1.9 24-12-2024 Phù Minh Tú Bổ sung thêm thông tin VAS khi xác nhận dán ID
Bổ sung rules khi user dán VAS trên App
2.0 02-01-2025 Phù Minh Tú Update rules scan location hoặc giỏ cho PO thường và PO Zone
cho Shop 170 QL1A và Kho 170 QL1A
2.1 05-01-2025 Phù Minh Tú Shop 170 QL1A và Kho 170 QL1A: trong 1 phiên nhận hàng cho
PO user có thể scan để nhận hàng vào bin Di động
2.2 07-01-2025 Phù Minh Tú Bổ sung rules date cho phép nhận của PO tester
2.3 05-02-2025 Phù Minh Tú Bổ sung
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 2

3
- VAS bổ sung thêm thông tin location theo phiên nhận
- Tách VAS nếu 1 ASN, 1 SKU nhưng nhận vào 2 location
khác nhau
- App: khi dán cũng sẽ tách theo location
2.3 10-02-2025 Phù Minh Tú Update lại UI cho luồng VAS trên App và Web
2.4 18-02-2025 Phù Minh Tú Update rules nhận PO không đồng kiểm bỏ qua bước scan
camera nếu kho có bật config “Required camrera” trong
Warehouse config
Bổ sung bước chụp hình, quay video sản phẩm trong VAS cho 1
số category yêu cầu
2.4 21-02-2025 Phù Minh Tú Update lại rules lựa chọn thông tin cần cập nhật khi xác nhận
dán UID
2.5 25-02-2025 Phù Minh Tú Update lại rule cập nhật QRCode và Serial cho sản phẩm
2.5 28-02-2025 Phù Minh Tú Bổ sung rules cho luồng nhận PO không đồng kiểm có khai báo
SPKPH => sinh return vendor
2.6 05-03-2025 Phù Minh Tú Cập nhật lại rules và luồng nhận PO không đồng kiểm có khai
báo SPKPH
2.7 23-04-2025 Phù Minh Tú Cập nhật rule chụp hình/quay video cho sản phẩm có required
Serial/Imei và không thuộc Sức khoẻ làm đẹp
2.8 22-05-2025 Phù Minh Tú Cập nhật luồng VAS: với SKU có required Imei thì bật cho user
nhập nhưng không bắt buộc
Bổ sung luồng nhận hàng các SKU không có barcode
2.9 30-05-2025 Phù Minh Tú Update luồng nhận SKU combo và con lẻ có required date
2.9 04-06-2025 Phù Minh Tú Bổ sung rules cập nhật date khi nhận SKU combo có required
date
2.10 09-07-2025 Phù Minh Tú Bổ sung luồng xác nhận dán ID (VAS) cho SKU có quản lý RFID
Bổ sung Nếu PO có SKU thoả điều kiện
2.10 28-07-2025 Phù Minh Tú
- Category: Thời trang
- Brand: Synctives
- SKU có yêu cầu RFID
Thì cho scan nhận RFID khi nhận PO, bỏ qua bước VAS  auto
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 3

4
VAS
Update lại UI và rules nhận hàng SKU ko barcode
2.10 31-07-2025 Phù Minh Tú
Bổ sung luồng nhận hàng khai báo Group UID cho các sản
2.11 16-09-2025 Phù Minh Tú
phẩm Vải nguyên vật liệu – Category Thời trang NVL
Update ASN detail khi xem số lượng nhận: thêm Group UID
Update VAS detail, thêm group UID
Bổ sung luồng cho user tạo VAS manual cho các SKU có RFID
2.12 02-12-2025 Phù Minh Tú
và Serial để khai báo cho những SKU khi nhận hàng chưa được
config và những SKU đã có trong kho nhưng còn thiếu thông
tin RFID và Serial
Bổ sung cho user cập nhật thông tin VAS cho SKU có required
2.12 23-12-2025 Phù Minh Tú
Serial/Imei
Validate Import packing list
2.13 15-01-2026 Phù Minh Tú
Nhận hàng PO với các SKU vải cho con lẻ và combo: update UI
và rules
Update thông tin và bổ sung validate khi scan nhận PO liên
2.14 29-01-2026 Phù Minh Tú
quan đến Packing list PO
Bổ sung thông tin “Trừ lõi” khi khai báo UID group khi nhận PO
2.15 02-04-2026 Phù Minh Tú
vải
- Packing list PO: Update template import (bổ sung 3 cột) và
2.16 16-04-2026 Phù Minh Tú
rules validate khi import Packing list nhận 1 phần hay cả PO
- Update UI nhận SKU có UID group và rules submit số lượng
khi nhận PO
-
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 4

5
CONTENT
TỔNG QUAN ............................................................................................................................................... 7
THUẬT NGỮ & VIẾT TẮT ...................................................................................................................... 8
QUY TRÌNH (WORKFLOW) ................................................................................................................... 8
GIAO DIỆN (WIREFRAME) .................................................................................................................... 8
YÊU CẦU CHỨC NĂNG ............................................................................................................................. 9
Inbound Shipment – Updated ................................................................................................................................ 9
Inbound shipment detail – Update ........................................................................................................................ 11
ASN – Updated ...................................................................................................................................................... 13
ASN detail – Updated ............................................................................................................................................ 18
16-09-2025: update xem chi tiết sản phẩm trong ASN ............................................................................................ 19
VAS – Updated ...................................................................................................................................................... 20
VAS detail – Updated............................................................................................................................................. 23
Cập nhật thông tin Serial/Imei/Label code cho SKU ................................................................................................ 24
16-09-2025: update rules VAS và bổ sung group UID .............................................................................................. 27
05-03.2025- Luồng nhận PO khồng đồng kiểm có khai báo SPKPH ......................................................................... 28
App – Confirm Unsuitable Product .......................................................................................................................... 29
Receiving PO (App) ................................................................................................................................................ 32
Case 1 : Chỉ nhận riêng PO thường (không có PO Gift đi kèm) ................................................................................ 41
Thêm hoá đơn cho PO ............................................................................................................................................. 62
Case 2 : Nhận PO Gift chung với PO thường ............................................................................................................ 68
Nhận hàng Vải khai báo Group UID ......................................................................................................................... 74
Bổ sung rules nhận PO gift riêng ............................................................................................................................ 79
Nhận hàng SKU không barcode (update 22-05-2025) ............................................................................................. 80
Confirm paste ID (App) .......................................................................................................................................... 84
01-12-2025: Create/Update VAS manual ............................................................................................................... 96
Web: Update màn hình quản lý VAS ........................................................................................................................ 96
Nhận hàng PO SKU có RFID của vendor ngoài ......................................................................................................... 97
Tạo thủ công VAS ..................................................................................................................................................... 99
Import packing list ............................................................................................................................................... 102
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 5

6
Update 29-01-2026 ................................................................................................................................................ 103
Nhận hàng PO cho SKU vải theo packing list ........................................................................................................ 106
SKU vải là con lẻ ..................................................................................................................................................... 106
SKU vải là combo .................................................................................................................................................... 108
02-04-2026: Bổ sung thông tin “Trừ lõi” ........................................................................................................... 109
Update 16-04-2026 .............................................................................................................................................. 111
Import Packing list ................................................................................................................................................. 111
Page quản lý Packing list ........................................................................................................................................ 112
Update UI nhận SKU có UID group ......................................................................................................................... 113
Update rules nhận dư cho PO vải (20-04-2026) ................................................................................................... 115
Update 17-05-2026 .............................................................................................................................................. 118
PO sample & PO chính ........................................................................................................................................... 118
Cho nhiều user cùng nhận cùng lúc ....................................................................................................................... 119
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 6

7
TỔNG QUAN
- Hiện tại việc nhận hàng PO đang được thực hiện trên App HSK Work, việc sử dụng đang có nhiều
hạn chế cũng như cải tiến cũng gặp nhiều khó khăn
- Tính năng này đang thuộc phạm vị của Kho nên sẽ move tính năng này qua WMS để đồng bộ và
tiện cho việc quản lý và hỗ trợ sau này.
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 7

|     |     | 8   |     |
| --- | --- | --- | --- |

Thuật ngữ & viết tắt

| #  Code  | Name  |     | Desciption  |
| -------- | ----- | --- | ----------- |
| 1.       |       |     |             |
| 2.       |       |     |             |
| 3.       |       |     |             |
| 4.       |       |     |             |
| 5.       |       |     |             |

Quy trình (Workflow)
-  Link  : https://drive.hasaki.vn/f/6fecf6ac99424782b12a/

Giao diện (Wireframe)
-  Link figma update: https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-
PO_Update?node-id=0-1&t=DjHSg0g4aPYPxsTM-1
-
Link visily (old): https://app.visily.ai/projects/760aa71b-3404-49db-a5ec-
bde3412ccdc6/boards/739286

|     |     |     |     |
| --- | --- | --- | --- |
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….  8

9
Yêu cầu chức năng
Inbound Shipment – Updated
- Menu: Inbound / Inound Shipment
Filter
- Bổ sung các filter sau (trong more filter)
Tiếng Việt Tiếng Anh Description
More filter
Đồng kiểm Check of goods Giá trị: Yes/No
 Move qua trang ASN
Đủ điều kiện nhận Eligible to receive Giá trị : Yes/No
Trạng thái WMS WMS status Status này chỉ sử dụng cho Type = PO
Giá trị:
- Mới / Open
- Đang nhận hàng / Receiving
- Đã nhận hàng / Received
- Hoàn thành / Completed
- Đã huỷ / Canceled
Hỗ trợ chọn nhiều
Lưu ý: status này là status riêng của WMS, khác với cột
status hiện tạo
Listing
Tiếng Việt Tiếng Anh Description
Đồng kiểm Check of goods PO có đồng kiểm hay không
- Lấy thông tin khi user chọn khi scan nhận PO
Đủ điều kiện nhận Eligible to receive Yes: PO đủ điều kiện để nhận
No: PO không đủ điều kiện để nhận
Mô tả Description Mô tả cho những case không đủ điều kiện nhận hàng
Tiếng việt Tiếng Anh
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 9

  10

| PO chưa được xác nhận      | PO not verifed               |     |
| -------------------------- | ---------------------------- | --- |
| PO chưa được duyệt         | PO not approved              |     |
| PO chưa được xác nhận hoá  | PO not yet verified invoice  |     |
đơn
| SKU tester 422225215 chưa  | SKU Tester 422225215 does  |     |
| -------------------------- | -------------------------- | --- |
| khai báo SKU gốc           | not have original SKU      |     |

Trạng thái  Status  Bổ sung đầy đủ các status của PO trên Inside, gồm
Mapping status PO giữa Inside và WMS
| Inside     |                                 | WMS  |
| ---------- | ------------------------------- | ---- |
| Verified   | >>  Mới / Open                  |      |
| Receiving  | <<  Đang nhận hàng / Receiving  |      |
| Received   | <<  Đã nhận hàng / Received     |      |
| Cancel     | >>  Đã huỷ / Canceled           |      |
Hỗ trợ chọn nhiều
Với Status Receiving thì bổ sung thêm thời gian đã bao lâu
chưa hoàn thành nhận hàng (tính từ khi bắt đầu scan PO để
nhận hàng)  mục đích để quản lý thời gian nhận hàng của
PO để cuối ngày user phải vào giải trình
Trạng thái WMS  WMS status  Trạng thái này chỉ sử dụng cho type PO và là status riêng của
WMS
|   WMS status  |                           | Mô tả  |
| ------------- | ------------------------- | ------ |
| Mới / Open    | Khi PO được tạo mới trên  |        |
WMS
| Đang nhận hàng / Receiving  | Khi user scan PO để nhận  |     |
| --------------------------- | ------------------------- | --- |
hàng trên App
| Đã nhận hàng / Received  | Khi PO hoàn thành nhận  |     |
| ------------------------ | ----------------------- | --- |
hàng trên App
| Đã huỷ / Canceled  | Khi PO bị huỷ trên Inside  |     |
| ------------------ | -------------------------- | --- |
-  Với Status Receiving thì bổ sung thêm thời gian đã
bao lâu chưa hoàn thành nhận hàng (tính từ khi bắt
đầu scan PO để nhận hàng)  mục đích để quản lý
thời gian nhận hàng của PO để cuối ngày user phải
vào giải trình

Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 10

|     |     | 11  |
| --- | --- | --- |

Inbound shipment detail – Update
Thông tin chung

-  Bổ sung thêm thông tin
o   Đủ điều kiện nhận / Eligible to receive
o   Mô tả / Description
Danh sách sản phẩm

| Tiếng Việt  | Tiếng Anh  | Description  |
| ----------- | ---------- | ------------ |
Số lượng  đổi  Quantity  đổi thành  Số lượng confirm theo inbound
| thành “Số lượng  | “Qty confirm”  |     |
| ---------------- | -------------- | --- |
xác nhận”
Số lượng đã nhận  Qty received  Tổng số lượng đã scan nhận theo ASN
Số lượng thiếu  Qty missing  Số lượng confirm – số lượng đã nhận

Giải trình lý do treo PO
-  Nếu PO giao trong ngày nhưng vẫn chưa chuyển “Đã nhận hàng” thì user sẽ vào để giải trình lý
do tại sao PO bị treo receiving
-  Sắp xếp giảm dần theo thời gian tạo

| Tiếng Việt  | Tiếng Anh  | Description  |
| ----------- | ---------- | ------------ |
Bình luận  Comment  User nhập nội dung cần giải trình và nhấn Thêm để cập nhật
thông tin
-  Button “Thêm” sẽ hiện ở bất kỳ status nào để user
có thể nhập comment cho PO
| TT         | No          | STT tăng dần                       |
| ---------- | ----------- | ---------------------------------- |
| Nội dung   | Content     | Hiện thị nội dung mà user đã thêm  |
| Người tạo  | Created by  | Email HSK của người tạo            |
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 11

|     |     | 12  |
| --- | --- | --- |

| Ngày tạo  | Created date  | Thời gian thêm  |
| --------- | ------------- | --------------- |

|     |     |     |
| --- | --- | --- |
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 12

|     |     | 13  |
| --- | --- | --- |

ASN – Updated
-  Menu: Inbound / ASN
Giao diện

Filter

-  Thay đổi lại thứ tự và bổ sung thêm thông tin
| Tiếng Việt        | Tiếng Anh         | Description                     |
| ----------------- | ----------------- | ------------------------------- |
| Mã ASN            | ASN number        | Tìm chính xác theo mã nhập vào  |
| Mã phiếu nhập     | Inbound shipment  |                                 |
| Phiếu nhập nguồn  | Inbound source    |                                 |
mapping
| Mã phiếu xuất     | Outbound oder    |     |
| ----------------- | ---------------- | --- |
| Phiếu xuất nguồn  | Outbound source  |     |
mapping
Kho  Warehouse  Load danh sách kho theo location và phân quyền của user
Hỗ trợ chọn nhiều
Hỗ trợ gợi ý khi user nhập từ 3 ký tự
SKU, Barcode  SKU, Barcode  Hỗ trợ tìm theo SKU hoặc Barcode của SKU trong chi tiết
của ASN
| Loại  | Type  | Giá trị:  |
| ----- | ----- | --------- |
-  Purchase order
-  Customer return
-  Internal transfer
-  Adjustment
Hỗ trợ chọn nhiều
| Người sở hữu  | Owner  | Giá trị  |
| ------------- | ------ | -------- |
-  Hasaki Cosmetics
-  Hasaki WMS
-  Hasaki OMS
Hỗ trợ chọn nhiều
| Trạng thái  | Status  | Giá trị  |
| ----------- | ------- | -------- |
-  Mới / Open
-  Đang nhận hàng / Receiving
-  Đã nhận hàng / Received
-  Đã huỷ / Canceled
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 13

|     |     | 14  |
| --- | --- | --- |

Hỗ trợ chọn nhiều
| Đồng kiểm         | Check of goods     | Giá trị: Yes/No  |
| ----------------- | ------------------ | ---------------- |
| Từ ngày…Đến ngày  | Form date…To date  |                  |

Listing

-  Bổ sung thêm 2 tuỳ chọn:
  In tất cả sản phẩm (Print all product)
o
  Mặc định: chỉ in những sản phẩm có khai báo thiếu hoặc SPKPH
  Nếu tích chọn thì in hết tất cả sản phẩm đã nhận trong ASN
  Thiết lập khổ giấy (Set paper size)
o
  Value
•
A5: in biên bản theo template A5
•  In Bill: In biên bản theo template in Bill
  Mặc định: theo template khổ giấy A5
  Nếu user chọn lại theo khổ giấy in Bill thì in theo template của in Bill
Lưu ý: thông tin này sẽ được lưu theo máy tính local, chỉ cần chọn 1 lần sẽ apply
cho sau đó, cho tới khi thay đổi
| Tiếng Việt        | Tiếng Anh         | Description  |
| ----------------- | ----------------- | ------------ |
| Mã ASN            | ASN number        |              |
| Kho               | Warehouse         |              |
| Loại              | Type              |              |
| Mã phiếu nhập     | Inbound shipment  |              |
| Phiếu nhập nguồn  | Inbound source    |              |
mapping
| Mã phiếu xuất     | Outbound oder    |     |
| ----------------- | ---------------- | --- |
| Phiếu xuất nguồn  | Outbound source  |     |
mapping
| Người sở hữu  | Owner           |                             |
| ------------- | --------------- | --------------------------- |
| Đồng kiểm     | Check of goods  |                             |
| Mã camera     | Camera code     |                             |
| Mã vị trí     | Location code   |                             |
| Mã giỏ        | Cart code       |                             |
| Ngày tạo      | Created date    | Ngày tạo: YYYY-MM-DD HH:MM  |
Người tạo: email Hasaki người thực hiện
| Ngày cập nhật  | Updated date  |     |
| -------------- | ------------- | --- |
| Trạng thái     | Status        |     |
| Thao tác       | Action        |     |
 để reopen ASN về lại trạng thái Open, và xoá nhân
viên ra khỏi ASN
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 14

15
- Button này chỉ show lên khi trạng thái ASN =
“Receiving” và user chưa scan nhận item nào
- EN: Do you want to ReOpen for ticket ASN
1002240906000004?
để in biên bản xác nhận nhận hàng với nhà cung cấp
- Button này chỉ show lên khi trạng thái của ASN =
“Receiving” hoặc “Received”
để xem biên bản giao hàng mà user upload lên khi nhận
hàng cho PO
Biên bản nhận hàng PO theo ASN – template A5
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 15

16
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 16

17
Biên bản nhận hàng PO theo ASN – template in Bill
Lưu ý: thông tin Số hoá đơn sẽ lấy cột “Taxcode” trên Inside
- Thông tin Taxcode có thể trùng nếu là PO gift và PO gốc
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 17

18
ASN detail – Updated
Thông tin chung
- Bổ sung thêm thông tin
Đồng kiểm / Check of goods
o
Camera
o
Mã vị trí / Location code
o
Danh sách sản phẩm
Tiếng Việt Tiếng Anh Description
SKU SKU
Barcode Barcode
Sản phẩm Product name
SL xác nhận Qty confirm Số lượng của SKU theo PO
Lưu ý: nếu 1 PO có nhiều phiên nhận thì vẫn ghi nhận theo
số lượng trên PO
SL thực nhận Qty received Số lượng thực nhận theo phiên nhận hàng
Lưu ý: nếu 1 PO có nhiều phiên nhận thì chỉ ghi nhận theo
từng phiên nhận hàng
SL thiếu Qty missing Số lượng còn thiếu so với PO
Lưu ý: nếu 1 PO có nhiều phiên nhận thì chỉ ghi nhận số
lượng thiếu còn lại theo phiên nhận
VD: SKU A số lượng trên PO là 10
- Lần 1 giao 5 thì ở phiên nhận hàng đầu tiên ghi nhận
số lượng thiếu là 5
- Lần 2 giao 3 thì ở phiên nhận hàng thứ 2 ghi nhận số
lượng thiếu là 2
Vị trí Location Mã bin mà user scan để nhận hàng vào với Shop 170 và Kho
170
Với Shop thì mặc định chuyển vào location mặc định
Mô tả Description Hiện các thông tin khi user khai báo lý do thiếu trên App
- Lý do thiếu
- Tình trạng hàng hoá (nếu có)
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 18

|     |     | 19  |
| --- | --- | --- |

-  Nhà cung cấp giao bù
-  Ghi chú
| Trạng thái  | Status  |     |
| ----------- | ------- | --- |

16-09-2025: update xem chi tiết sản phẩm trong ASN
-  Bổ sung thông tin Group UID đã nhận cho ASN

|     |     |     |
| --- | --- | --- |
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 19

|     |     |     |     | 20  |
| --- | --- | --- | --- | --- |

VAS – Updated
-  Menu: Inbound / VAS
-  Với các SKU có quản lý Serial/Imei/Label code mà không phải category “Sức khoẻ - Làm đẹp” thì
sau khi kết thúc nhận hàng user phải làm thêm 1 bước nữa là xác nhận dán ID cho sản phẩm vật
lý
o   Khi này khi nhận hàng PO thì user chỉ cần scan nhận theo số lượng, không cần khai báo
Serial/Imei/Label code cho sản phẩm
Bổ sung logic giữa ASN và VAS
-  Với các SKU có category là “Sức khoẻ - Làm đẹp”  có quản lý serial/imei thì khi ASN chuyển status
Received thì hệ thống sẽ tự động sinh VAS và auto completed
  Hiện tại chỉ update thông tin serial khi đóng đơn để ghi nhận đóng cho đơn hàng nào
o
-  Với các SKU có category là: Tài sản cố định (TSCĐ), Công cụ dụng cụ (CCDC) , Công cụ dụng cụ
phân bổ (CCDC PB) có quản lý theo Serial/Imei/Label code thì khi ASN chuyển status Received thì
hệ thống sẽ sinh ra 1 VAS tương ứng với ASN với status = Open
  Lưu ý: với các UID này sau khi received thì status sẽ update thành “Received” chứ chưa
o
auto chuyển qua In-Bin, khi này các UID này sẽ không được lấy picklisted cho
order/receipt/IT

Sau khi user xác nhận chụp hình hoặc dán ID cho từng UID (tuỳ vào category của
SKU) thì trạng thái mới được chuyển từ Received qua In-Bin

Filter
-  Cập nhật 1 số thông tin và thứ tự trên Filter
| Tiếng Việt  |     | Tiếng Anh  |     | Description  |
| ----------- | --- | ---------- | --- | ------------ |
Select filter
|     | Mã VAS            |     | VAS number       | Xem chi tiết ASN  |
| --- | ----------------- | --- | ---------------- | ----------------- |
|     | Mã phiếu nhập     |     | Inbound shipmet  |                   |
|     | Phiếu nhập nguồn  |     | Inbound source   |                   |
mapping
|     | Mã phiếu xuất     |     | Outbound order   |     |
| --- | ----------------- | --- | ---------------- | --- |
|     | Phiếu xuất nguồn  |     | Outbound source  |     |
mapping
| Loại          |     | Type          |     |                  |
| ------------- | --- | ------------- | --- | ---------------- |
| Kho           |     | Warehouse     |     |                  |
| SKU, Barcode  |     | SKU, Barcode  |     |                  |
| Người sở hữu  |     | Owner         |     |                  |
| Trạng thái    |     | Status        |     | Mặc định = Null  |
Value
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 20

|     |     | 21  |
| --- | --- | --- |

-  Mới / Open
-  Đang xử lý / In-Progress
-  Hoàn thành / Completed
-  Đã huỷ / Canceled
Hỗ trợ chọn nhiều
| Từ ngày…đến ngày  | From date…To date  |     |
| ----------------- | ------------------ | --- |

Listing
| Tiếng Việt  | Tiếng Anh   | Description                     |
| ----------- | ----------- | ------------------------------- |
| TT          | No          |                                 |
| Mã VAS      | VAS number  |                                 |
| Kho         | Warehouse   |                                 |
| Loại        | Type        |                                 |
| Mã ASN      | ASN number  | Hyperlink tới trang ASN detail  |
Mã phiếu nhập  Inbound shipmet  Hyperlink tới trang Inbound shipment detail
Phiếu nhập nguồn  Inbound source  Hyperlink tới trang PO detail của Inside
mapping
| Mã phiếu xuất     | Outbound order   |     |
| ----------------- | ---------------- | --- |
| Phiếu xuất nguồn  | Outbound source  |     |
mapping
| Vị trí  | Location  | Vị trí nhận hàng theo ASN  |
| ------- | --------- | -------------------------- |
Lưu ý:
-  Nếu cùng 1 phiên nhận mà 1 SKU được nhận vào 2
location khác nhau thì sẽ sinh ra VAS tương ứng
-  Nếu SKU có yêu cầu serial thì không cần hiển thị
trong chi tiết của VAS, chỉ hiện các SKU có yêu cầu
serial
| Người tạo  | Created by  | Email người tạo + thời gian tạo  |
| ---------- | ----------- | -------------------------------- |
Người thực hiện  Implemented by  Email người thực hiện + thời gian thực hiện
| Ngày cập nhật  | Updated date  | Thời gian thực hiện  |
| -------------- | ------------- | -------------------- |
Trạng thái  Status  -  Mới / Open: khi ASN received và sinh ra 1 VAS cho
các SKU có category là: Tài sản cố định (TSCĐ), Công
cụ dụng cụ (CCDC) , Công cụ dụng cụ phân bổ (CCDC
PB) có quản lý theo Serial/Imei/Label code
-  Đang xử lý / In-Progress: khi có ít nhất 1 SKU có số
lượng đã dán > 1
-  Hoàn thành / Completed
-  Đã huỷ / Canceled
| Thao tác  | Action  |     |
| --------- | ------- | --- |
Button   để cập nhật thông tin Serial/Imei/Label code cho
SKU
-  Button này chỉ show cho VAS cho status Open và In-
Progress
Button   để xem chi tiết của VAS

Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 21

22
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 22

23
VAS detail – Updated
Thông tin chung
- Đổi thông tin sang dạng text, gồm các thông tin
Kho / Warehouse
o
Loại / Type
o
ASN
o
Mã phiếu nhập / Inbound shipment
o
Phiếu nhập nguồn / Inbound source mapping
o
Mã phiếu xuất / Outbound order
o
Phiếu xuất nguồn / Outbound source mapping
o
Vị trí / Location
o
Ngày tạo / Created date
o
Người tạo / Created by
o
Ngày cập nhật / Updated date
o
Danh sách sản phẩm
- Chỉ hiện các sản phẩm có quản lý serial (cần xác nhận dán ID) các sản phẩm không quản
lý serial thì không cần hiện trong danh sách này
Tiếng Việt Tiếng Anh Description
SKU SKU
Barcode Barcode
Sản phẩm Product name
SL thực nhận Qty received Số lượng thực nhận của SKU theo ASN tương ứng
SL đã dán Qty pasted Số lượng cập nhật đã dán ID
Hình ảnh/Video Image/Video
Thao tác Action
Button để cập nhật thông tin Serial/Imei/Label code cho
SKU
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 23

24
- Button này chỉ show cho VAS cho status Open và In-
Progress
Button để xem chi tiết của Serial/Imei/Label code theo
SKU
Cập nhật thông tin Serial/Imei/Label code cho SKU
- Chọn vào button trên từng dòng của SKU để cập nhật thông tin cho sản phẩm tương ứng
Tuỳ chọn thông tin cần cập nhật cho SKU: hệ thống auto chọn thông tin cần cập nhật
o
Nếu là cate: CCDC, CCDC PB...là những cate sẽ thực hiện theo luồng VAS
• Và wms_product.wms_config&131072 > 0 => required QR, tức bật ON cập nhật
QRCode
• Hoặc wms_product.config&8 > 0 => required Imei, tức bật ON cập nhật Serial/Imei
Cập nhật 25-02-2025
o
 Hiện tại sẽ luôn tắt option Serial dưới BE, user chỉ cần cập nhật
QRCode, sau này cần sẽ mở ra sau
 Serial nếu không có thông tin thì hệ thống WMS sẽ tự gen mã theo
rules sau: [1023][YYMMDD][6 số tăng dần]
• Nếu sau này có kiểm kê mà user count lại theo Serial thì sẽ
update Serial mới đè lên Serial mà hệ thống gen ra trước đó
• Ngược lại với 2 case trên thì chỉ cần chụp hình, bỏ qua bước cập nhật QRCode hoặc
Serial
Lưu ý: do mã QRCode in ra có dạng Object nên khi scan hệ thống sẽ tự động cắt chuỗi để lấy đúng
thông tin cần lấy
 Lấy thông tin “Code” trong object
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 24

25
Thông tin nào được tích chọn thì ô scan của thông tin đó sẽ được show lên để user scan
o
 Nếu chỉ cập nhật 1 thông tin thì khi user scan thì tự động add vào danh sách. Nếu
user nhập thì nhấn icon dấu + để add vào danh sách
 Nếu chọn cập nhật cả 2 thông tin thì khi scan Qrcode hợp lệ, sẽ tự động chuyển
focus qua ô scan Serial/Imei để tiếp tục scan và add vào danh sách
Validatiton
Nội dung Thông báo tiếng Việt Thông báo tiếng Anh
Serial scan vào đã tồn tại trong Serial 11333787241140438102 Serial 11333787241140438102
danh sách. đã tồn tại trong danh sách. already exists in the list.
Serial scan vào đã tồn tại trên Serial 11333787241140438102 Serial 11333787241140438102
hệ thống. đã tồn tại trên hệ thống. already exists on the system.
Serial không hợp lệ (phải từ 16 Serial 1133378724121 không Serial 1133378724121 is invalid
ký tự) hợp lệ (phải từ 16 ký tự) (must be 16 characters or more)
QRCode scan vào đã tồn tại trên QRCode UEA1JDJ3 đã tồn tại QRCode UEA1JDJ3 already exists
hệ thống. trên hệ thống. on the system.
QRCode scan vào đã tồn tại QRCode UEA1JDJ3 đã tồn tại QRCode UEA1JDJ3 already exists
trong danh sách. trong danh sách. in the list.
QRCode scan vào không tồn tại QRCode UEA1JDJ3 không tồn tại QRCode UEA1JDJ3 does not
trên hệ thống HR trên hệ thống HR. exist on the HR system.
- Thông tin sau khi cập nhật
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 25

26
- Hỗ trợ search gần đúng (nhập từ 3 ký tự) cho QRCode và Serial đã scan vào danh sách
- Nếu cần chỉnh sửa 1 thông tin thì chọn icon tương ứng để cập nhật (vẫn validation giống như
lúc scan mới)
Chọn “Đóng” để tắt thông báo
o
Chọn “Lưu” để lưu lại thông tin cho sản phẩm
o
 Sau khi số lượng xác nhận dán bằng số lượng đã nhận (cần dán) của tất cả SKU có
trong VAS thì button “Complete” show lên để user complete VAS, hiện thông báo
• EN: Do you want to confirm pasting ID completion?
- Chọn button để xem chi tiết thông tin cho sản phẩm
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 26

27
16-09-2025: update rules VAS và bổ sung group UID
- Update Group UID và Quality control results cho type Quality control
- 1 SKU nhận trong ASN theo group UID sẽ lấy ra 10% để thực hiện đánh giá, nếu ra số lẻ thì làm
tròn lên
VD: SKUA nhận trong ASN là 25 group UID thì 10% là 2,5 làm tròn thành 3, tức sẽ có 3
o
dòng VAS cần đánh giá chất lượng cho SKUA
- Trong VAS Quality control bổ sung thêm Group UID và kết quả đánh giá theo group UID
Chỉ cần có 1 kết qua Failed thì ghi nhận là Failed
o
VAS sinh ra khi user chưa thực hiện đánh giá => Group UID = trống
VAS sinh ra khi user đã thực hiện đánh giá => Group UID = thông tin được scan vào
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 27

28
05-03.2025- Luồng nhận PO khồng đồng kiểm có khai báo SPKPH
05-05-2026: Khi nhận hàng PO không đồng kiểm và có SPKPH thì Shop vẫn khai báo như bình
thường nhưng khi này hệ thống sẽ ghi nhận như nhận thiếu và nhận lại ở phiên sau
Luồng xử lý SPKPH cho luồng nhận PO tạm Off không sử dụng
o
Quy trình
Mô tả:
- Đối với PO không đồng kiểm và có khai báo SPKPH
Với những SKU bình thường nhận trong phiên thì đưa vào 1 ASN riêng và update status =
o
Received và import stock
Với những SKU khai báo SPKPH thì đưa vào 1 ASN với status Waiting for approval
o
 Nếu có nhiều SKU khai báo SPKPH trong cũng 1 phiên thì sẽ nằm trong 1 phiên
ASN riêng
 Lưu ý: không tiến hành import stock cho những SKU khai bao SPKPH
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 28

29
 Nếu quản lý thực hiện action Cancel => Xác nhận thì các UID của SKU này được
chuyển về chưa nhận để user vào scan nhận lại hoặc khai báo thiếu hàng và NCC
không giao lại để Completed PO
• Cập nhật trạng thái của ASN = Cancel
 Nếu quản lý thực hiện action Reject => chuyển các sản phẩm khai báo SPKPH qua
sản phẩm chưa nhận
• User thực hiện scan nhận lại như sản phẩm bình thường
• Cập nhật trạng thái của ASN = Reject
 Nếu quản lý thực hiện action Approve
• Cập nhật trạng thái của ASN = Chờ NCC đến lấy (Waiting for vender to
pick)
• Khi này shop chỉ quản lý hàng vật lý bên ngoài để chờ NCC đến lấy hoặc
quá 7 ngày mà NCC chưa đến lấy thì thực hiện tiêu huỷ theo quy trình
User thực hiện xác nhận việc NCC đến lấy hàng hoăc tiêu huỷ
o
thông qua App WMS
App – Confirm Unsuitable Product
- Vào mục Purchase order / Confirm Unsuitable Product
- Chọn kho  show danh sách ASN khai báo SPKPH có trạng thái “Chờ NCC đến lấy” của kho tương
ứng
Thông tin gồm
o
 Mã PO | Thời gian tạo PO
 Mã ANS
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 29

30
 Tổng SKU: có trong ASN của SPKPH
 Tổng sản phẩm: có trong ASN của SPKPH
User chọn vào phiên của SPKPH cần xác nhận
o
 Thông tin hiện thị trong phiên
• Mã PO
• Mã ASN
• SKU
• Qty
• Danh sách sản phẩm
Tên sản phẩm
o
SKU | Barcode
o
Số lượng SPKPH
o
Ghi chú
o
• Chọn phương án xử lý
Mặc định = Null
o
Giá trị:
o
 Đã trả Nhà cung cấp
 Đã tiêu huỷ
• Ghi chú
• Hình ảnh và video bằng chứng
 Sau khi cập nhật đầy đủ thông tin và chụp hình  Chọn Hoàn thành và xác nhận
để hoàn thành
• Cập nhật status của ASN theo phương án xử lý
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 30

31
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 31

|     |     | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Receiving PO (App)
•
User login vào app với tài khoản được cung cấp
•
Vào tính năng “Receiving PO”
| Step  | Action  |  UI  | Field (VN)  | Field (EN)  |     | Description  |
| ----- | ------- | ---- | ----------- | ----------- | --- | ------------ |
1  Hiện hướng dẫn ở  Nhận hàng PO  Receiving PO  Lưu ý : thông tin này sẽ mặc đinh show khi user mới
màn hình scan PO  Scan mã PO  Scan PO code  vào chức năng “Receiving PO”
| cần nhận  |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- |

2  Scan mã PO cần  Nhận hàng PO  Receiving PO  User scan PO cần nhận hàng
| nhận hàng  |     |     | Scan mã PO  | Scan PO code  | Validation                                        |     |
| ---------- | --- | --- | ----------- | ------------- | ------------------------------------------------- | --- |
|            |     |     |             |               | - Nếu PO không yêu cầu VAT thì bỏ qua bước check  |     |
verify invoice và force Invoice
- Ngược lại, Nếu PO có yêu cầu VAT mà chưa được
verify/approve hoặc không tồn tại trên hệ thống, hiện
thông báo

- Nếu PO không thuộc kho đang xử lý, hiện thông báo

33
- Nếu PO chưa được verify invoice, hiện thông báo
- Nếu PO đã được nhận hàng (received), hiện thông
báo
- Nếu PO hợp lệ,
1. Show thông tin PO lên giao diện, gồm :
• Mã PO chính (PO 1)
• Nếu có add thêm PO Gift thì là PO 2
• Tổng tiền
• Tổng SKU : số lượng SKU đã scan nhận
• Tổng sản phẩm : số lượng sản phẩm đã scan
nhận
2. Tạo ASN tương ứng, với các thông tin gồm
• ASN number : hệ thống tự sinh
• Type : Purchase Order
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 33

34
• Inbound Shipment : Mã Inbound Shipment
của WMS
• Outbound Order : Mã Outbound Order của
WMS
• Status = Receiving
Lưu ý khi này chưa gọi API để update status
PO trên Inside thành Receiving
 chuyển qua bước tiếp theo
05-01-2026: update rules scan nhận PO
1. Bổ sung rules như trong hình, khi scan PO nếu có 1 SKU thoả điều kiện trong PO có qty < 100.000 thì hiện thông báo và không cho nhận (không chuyển PO qua
receiving)
Lưu ý: các PO thuộc rules này thì vẫn cho nhận bình thường như trước giờ
2. Bổ sung filter các PO thoả điều kiện này
• Filter VN: Cho phép nhận PO có SKU bất thường
• Filter EN: Force receiving PO with abnormal SKUs
• Thông báo xác nhận
VN: Bạn có muốn xác nhận cho phép nhận PO có SKU bất thường không?
o
EN: Do you want to confirm allowing receiving PO with abnormal SKUs?
o
3. Bổ sung nút force cho các PO thoả điều kiện này để có thể force cho nhận nếu cần)
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 34

35
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 35

  36

3  Chọn loại nhận hàng  Chọn loại nhận  Select the  User chọn loại nhận hàng cho PO
- Không đồng kiểm  user phải scan và nhận dưới
| cho PO  | hàng cho PO      | receiving type for  |                                              |
| ------- | ---------------- | ------------------- | -------------------------------------------- |
|         | 10012402010027   | PO                  | camera  chuyển qua bước 4                   |
|         |                  | 10012402010027      | - Có đồng kiểm  bỏ qua bước scan camera     |
|         | Không đồng kiểm  | No check of         | •  Nếu shop có quản lý location: chuyển qua  |
|         |                  | goods               |                                              |
bước scan vị trí cần chuyển hàng vào
|     | Có đồng kiểm  | check of goods  | •  Nếu shop không có quản lý location: chuyển  |
| --- | ------------- | --------------- | ---------------------------------------------- |
|     |               |                 | qua bước scan sản phẩm cần nhận                |
- Chọn đóng để tắt popup và quay lại màn hình scan
PO cần nhận (bước 2)

4  Scan mã camera  Scan mã camera  Scan camera  User chỉ phải scan camera nếu PO đó là Không đồng
|     |                 | code            | kiểm                                           |
| --- | --------------- | --------------- | ---------------------------------------------- |
|     | Tổng tiền       | Total amount    | Update 18-02-2025                              |
|     | Loại nhận hàng  | Receiving type  | Bổ sung config "Required camera" trong config  |
Warehouse
- Menu: Master data / Warehouse => view Warehouse

config
•  Tab Configuration
  Thêm Group "General"
o
  Thêm config "Required camera"
o

Mặc định = No: không cần
scan camera cho chức năng
được xét điều kiện này
Update chức năng Receiving PO trên App
- Khi user scan nhận PO, chọn "Không đồng kiểm"
•  Required camera = Yes => phải scan camera
•  Required camera = No => bypass bước scan
camera (giống case PO "Đồng kiểm")
----------
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….  36

37
Nếu mã camera không thuộc kho hoặc không tồn tại
trên hệ thống hiện thông báo
• VN: Mã camera không hợp lệ hoặc không tồn
tại trên hệ thống.
• EN: Camera code is invalid or does not exist
on the system.
Nếu mã camera hợp lệ
• Nếu shop có quản lý location: scan mã vị trí
cần chuyển hàng vào hoặc chọn chuyển hàng
vào giỏ
• Nếu shop không có quản lý location: chuyển
qua bước scan sản phẩm cần nhận hàng
5 Scan vị trí / mã giỏ Scan vị trí / mã giỏ Scan location / User chỉ phải scan mã vị trí, mã gỏ cần chuyển hàng
cần chuyển hàng cần chuyển hàng Cart code nếu shop/kho có quản lý theo location
vào vào Hệ thống tự động detect thông tin user scan/nhập vào
là mã Bin hay mã giỏ để chuyển hàng vào
Nếu PO nhận vào là PO zone
Sau khi scan mã camera (nếu có) thì hệ thống sẽ hiện
thông báo
Lưu ý: với PO zone chỉ được phép chuyển hàng vào
các location có type Di động, không được chuyển hàng
vào giỏ hoặc location khác
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 37

38
- Nếu mã vị trí không thuộc kho hoặc không tồn tại
trên hệ thống hiện thông báo
• VN: Vị trí không hợp lệ hoặc không tồn tại
trên hệ thống.
• EN: Location code is invalid or does not exist
on the system.
- Nếu mã vị trí không được thiết lập là bin Di động, hệ
thống hiện thông báo
• VN: Vị trí F2-AP-01-01-01-01 không được thiết
lập để lưu trữ hàng cho PO zone.
• EN: Location F2-AP-01-01-01-01 is not setup
to storage for PO zone.
- Nếu vị trí hợp lệ  chuyển qua bước scan sản phẩm
cần nhận
- Nếu user scan mã giỏ, hiện thông báo
Nếu PO nhận vào là PO thường
- Nếu mã vị trí không thuộc kho hoặc không tồn tại
trên hệ thống hiện thông báo
• VN: Vị trí không hợp lệ hoặc không tồn tại
trên hệ thống.
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 38

39
• EN: Location code is invalid or does not exist
on the system.
Lưu ý: PO thường có thể nhận vào bất kỳ location
nào cũng được
- Nếu mã vị trí config là bin Di động, hệ thống hiện
thông báo
• VN: Vị trí F0-A1-PL-50-01-01 là bin Di động,
nên không thể lưu trữ hàng cho PO.
• EN: Location F2-AP-01-01-01-01 is not setup
to storage for PO.
- Nếu vị trí hợp lệ  chuyển qua bước scan sản phẩm
cần nhận
Nếu user scan mã giỏ
- Nếu mã giỏ không thuộc kho hoặc không tồn tại trên
hệ thống hiện thông báo
• VN: Mã giỏ không hợp lệ hoặc không tồn tại
trên hệ thống.
• EN: Cart code is invalid or does not exist on
the system.
- Nếu mã giỏ có trạng thái khác Available hoặc
Transfer Bin, hệ thống hiện thông báo
• VN: Mã giỏ 404005 có trạng thái không hợp
lệ.
• EN: Cart code 404005 has invalid status.
- Nếu mã giỏ hợp lệ  chuyển qua bước scan sản
phẩm cần nhận
5.1 27-02-2024: bổ sung rules check và cập nhật thông tin location Di động (Pallet)
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 39

40
1 Bin location sẽ có thông tin stock_id và location_id (bổ sung)
1 Bin location sẽ sử dụng chung cho nhiều stock trong cùng location_id
• VD Bin A có thể sử dụng chung cho Shop 170 QL1A, WH 170 QL1A, WH 170 QL1A KT1...cùng thuộc location 170 QL1A
• Ở 1 thời điểm thì Bin A chỉ thuộc 1 stock duy nhất
Update rules khi nhận hàng PO vào Bin di động (Pallet)
• Thời điểm trước khi nhận Bin A đang thuộc Shop 170 QL1A (thuộc location 170 QL1A)
• Khi scan nhận PO mới vào Bin A sẽ check
Nếu PO đang nhận thuộc Shop 170 QL1A thì cho phép nhận vào bình thường (xử lý theo luồng bình thường như trước đây)
o
Nếu PO đang nhận thuộc WH 170 QL1A thì check
o
 Nếu Bin A đang có hàng (tức đang còn UID ) thì báo lỗi không cho nhận
 Nếu Bin A không còn hàng thì cho nhận vào, đồng thời cập nhật lại stock_id cho Bin A từ Shop 170QL1A thành WH 170QL1A
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 40

41
Case 1 : Chỉ nhận riêng PO thường (không có PO Gift đi kèm)
Step Action UI Field (VN) Field (EN) Description
1 Nhập số lượng + Tổng tiền Total Amount User nhập số lượng + scan SKU/barcode để nhận hàng
Scan SKU cần nhận Tổng SKU Total SKU - Nếu SKU không tồn tại trong PO, hiện thông báo
hàng Tổng sản phẩm Total item • VN: SKU 100540031 không có trong PO.
• EN: SKU 100540031 is not in PO.
- Nếu số lượng của SKU vượt quá số lượng confirm
trong PO, hiện thông báo
• VN: Số lượng của SKU 100540031 lớn hơn số
lượng cần nhận trong PO.
• EN: The quantity of SKU 100540031 is greater
Thông tin sản phẩm sau khi scan nhận than the quantity required in the PO.
thành công Nếu SKU hợp lệ
- Nếu SKU không yêu cầu nhập date, cập nhật thông
Sản phẩm có hạn sử dụng tin sản phẩm và số lượng scan lên màn hình
- Nếu SKU có yêu cầu nhập date, show thông tin để
nhập HSD cho sản phẩm
• Số lượng: lấy từ thông tin nhập ở màn hình
scan SKU và cho phép chỉnh sửa
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 41

42
• Nếu HSD nhỏ hơn yêu cầu cho phép nhận
hàng, hiện thông báo
Sản phẩm có HSD và số lô VN: Hạn sử dụng nhỏ hơn yêu cầu
o
được phép nhận hàng của PO (9
tháng).
EN: Expiration date is less than the PO
o
permission request (9 months)
06-01-2025: cập nhật rules tính ngày nhận
hàng tối thiếu của PO cho SKU
•
Thông báo cập nhật
Hạn sử dụng nhỏ hơn yêu cầu được
o
phép nhận hàng của PO (HSD tối thiếu
Sản phẩm có serial/imei [Ngày hệ thống tính toán]
Rules tính HSD tối thiểu: [% Allowed
o
Shelf Life PO] * [Product’s Shelf Life]
=> tính ra được số tháng tương ứng
(không làm tròn, VD: 20,16 tháng), từ
số tháng tính được cộng với ngày
nhận hàng để ra được HSD tối thiểu
có thể nhận
Lưu ý: Khi nhận hàng thì HSD của sản
o
phẩm trùng với tháng trong HSD tối
thiểu thì vẫn cho nhận (do HSD của
sản phẩm sẽ tính về ngày cuối tháng)
• Nếu HSD nhập vào lớn hơn vòng đời của sản
phẩm, hiện thông báo
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 42

43
VN: Hạn sử dụng lớn hơn vòng đời
o
được thiết lập của sản phẩm (24
Update 02-11-2024 tháng).
Bổ sung icon để xem ghi chú cho PO EN: Expiration date is greater than the
o
product shelf life (24 months).
• (08-01-2025) Nếu PO là tester thì tất cả SKU
trong PO tester được phép nhận vào nếu HSD
của sản phẩm >=3 tháng
• Nếu số lượng của SKU vượt quá số lượng
confirm trong PO, hiện thông báo
VN: Số lượng của SKU 100540031 lớn
o
hơn số lượng cần nhận trong PO.
EN: The quantity of SKU 100540031 is
o
greater than the quantity required in
the PO.
- Nếu SKU có yêu cầu nhập số lô và HSD thì show
popup để nhập thông tin
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 43

44
- Số lượng: lấy từ thông tin nhập ở màn hình
scan SKU và cho phép chỉnh sửa
- Validate HSD tương tự như trên
- Số lô check trùng nếu số lô của cùng SKU đã
tồn tại trên hệ thống, hiện thông báo
• VN: Số lô của sản phẩm đã tồn tại trên
hệ thống
• EN: Batch code of product already
exists in the system
• Nếu số lượng của SKU vượt quá số lượng
confirm trong PO, hiện thông báo
VN: Số lượng của SKU 100540031 lớn
o
hơn số lượng cần nhận trong PO.
EN: The quantity of SKU 100540031 is
o
greater than the quantity required in
the PO.
Nếu SKU là công cụ dụng cụ và được config có yêu cầu
nhập Serial/Imei thì show popup để nhập Serial / Imei
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 44

45
• Nếu serial/imei của sản phẩm đã tồn tại trên
hệ thống (của cùng SKU), hiện thông báo
VN: Serial/Imei của sản phẩm đã tồn
o
tại trên hệ thống.
EN: Serial/Imei of prodcut already
o
exists in the system.
• Nếu số lượng của SKU vượt quá số lượng
confirm trong PO, hiện thông báo
VN: Số lượng của SKU 100540031 lớn
o
hơn số lượng cần nhận trong PO.
EN: The quantity of SKU 100540031 is
o
greater than the quantity required in
the PO.
Lưu ý: đối với SKU công cụ dụng cụ có yêu cầu nhập
serial/imei thì 1 lần scan chỉ nhận SL = 1, nếu nhập SL
> 1 hiện thông báo
Lưu ý: (24-10-2024) ở phase này với SKU có yêu cầu
nhập Serial/imei thì sẽ by pass bước nhập Serial/Imei,
chỉ cần nhập số lượng và date (nếu có yêu cầu)
 Tiếp tục scan nhận hàng cho tới khi hoàn thành
05-01-2025
Bổ sung thêm button “Thay đổi vị trí nhận hàng”
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 45

46
- Button này chỉ hiện cho Shop 170 QL1A và Kho
170 QL1A (kho bật config location)
- Nếu chọn thì sẽ quay về bước scan vị trí / mã
giỏ cần chuyển hàng vào
Lưu ý: các sản phẩm được scan nhận sẽ được ghi nhận
vào vị trí được scan trước đó, tới khi có thay đổi vị trí
nhận hàng mới
1 PO chỉ được nhận vào 1 giỏ duy nhất để đi push
hàng về kệ, không được nhận vào nhiều giỏ khác nhau
(do 1 user tại 1 thời điểm chỉ được giữ 1 giỏ duy nhất)
Update 30-05-2025
Khi nhận hàng PO nếu là SKU combo, check:
- SKU combo required date và chỉ có 1 con lẻ required
date => show popup để user nhập theo SKU lẻ
- SKU combo ko required date thì ko yêu cầu nhập
date (cho dù SKU lẻ có required date => lỗi data)
- SKU combo required date và có từ 2 con lẻ required
date, show popup để user input date cho từng cho lẻ
(số lượng con lẻ lấy theo số lượng của combo)
- Thông tin show trên Popup
Update 04-06-2025
• Không quan tâm tới con combo có required
date hay không, chỉ cần có con lẻ có required
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 46

47
date thì sẽ show popup cho user nhập date
cho con lẻ
• Nếu SKU combo có required date mà SKU con
lẻ không có required date thì vẫn show popup
để nhập date cho SKU combo (vẫn thông tin
SKU lẻ để check)
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 47

48
1.1 Scan nhận SKU có Nếu PO có SKU thoả điều kiện
RFID - Category: Thời trang
- Brand: Synctives
- SKU có yêu cầu RFID
Thì sẽ scan RFID khi nhận hàng, không khai báo ở
bước VAS, khi này sẽ auto VAS
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 48

49
1.2 Xoá sản phẩm vừa Sản phẩm có HSD và số lô Nếu khai báo sai thông tin (HSD, Batch code, Serial)
scan nhận hàng trong quá trình nhận hàng có SKU
- Nếu SKU có HSD +batch code thì sẽ xoá hết tất cả số
lượng đã scan nhận của phiên đang nhận để tiền hành
scan nhận lại
• EN: Do you want to delete SKU 253900004
from the receiving session? (This will delete all
scanned quantities in the current receiving
session)
Sản phẩm có serial/imei
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 49

50
- Nếu SKU có Serial thì sẽ chọn xoá Serial nhận sai để
scan nhận lại
• EN: Do you want to delete serial 2UA49P120
of SKU 253900004 from the receiving session?
2 Xem danh sách SKU Danh sách sản List of products User chọn vào dấu + chọn “Danh sách sản phẩm” để
đã nhận trong PO phẩm xem thông tin sản phẩm đã nhận của PO
Phiên nhận hàng Receiving session Lưu ý : nếu chỉ có 1 PO thì không cần phải chọn PO
cần xem
Thông tin gồm 2 tab :
- Tab sản phẩm Đã nhận đủ
Tab Chưa nhận đủ Thông của sản phẩm gồm
- Tên sản phẩm
- SKU
- Barcode
- Vị trí nhận hàng: chỉ hiện cho Shop 170 QL1A
và Kho 170 QL1A
Chỉ hiện cho những SKU đã có số
o
lượng scan nhận
- Số lượng đã scan nhận/Số lượng cần nhận
• Chọn vào “Chi tiết” để xem thông tin chi tiết
của hạn sử dụng hay serial/imei đã nhận
SKU có hạn sử dụng
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 50

51
SKU có serial/imei
Tab Đã nhận đủ
2.1 Xem phiên nhận Danh sách sản List of products User chọn vào dấu + chọn “Phiên nhận hàng” để xem
hàng trong PO phẩm thông tin chi tiết của phiên đang hoặc đã nhận của PO
Phiên nhận hàng Receiving session
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 51

52
User chọn vào phiên để xem thông tin chi tiết
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 52

  53

2.2  Khai báo sản phẩm  Khai báo theo sản phẩm  Khai báo lý do  Declare reason  Với những sản phẩm đang nhận hàng chưa đủ số
| thiếu & không phù  | thiếu hàng  | for missing  |
| ------------------ | ----------- | ------------ |
lượng, có thêm button   để user có thể khai báo số
| hợp (nếu có)  | Số lượng thiếu  | Qty missing  |
| ------------- | --------------- | ------------ |
lượng hàng thiếu hoặc không phù hợp
|     | Lý do thiếu hàng  | Reason for  |
| --- | ----------------- | ----------- |
-  Hoặc user có thể chọn nhiều sản phẩm chưa
|     |     | missing  |
| --- | --- | -------- |
nhận đủ số lượng  Khi này dấu “+” ở gốc trái
|     | Ghi chú  | Note  |
| --- | -------- | ----- |
sẽ hiện lên  chọn “Khai báo lý do thiếu
|     | Hình ảnh sản  | Product Image  |
| --- | ------------- | -------------- |
hàng” để khai báo nhiều sản phẩm cùng lúc
phẩm
Thông tin gồm
-  Tên sản phẩm
-  SKU
-  Barcode
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….  53

54
- Số lượng thiếu: hệ thống tự động lấy số lượng
chưa nhận theo PO  cho user chỉnh sửa số
lượng
Bắt buộc: nếu để trống hiện thông
o
báo “Vui lòng nhập số lượng thiếu”
- Lý do thiếu
Bắt buộc
o
Giá trị
o
 Giao thiếu hàng
 Bổ sung thêm “Nhà
cung cấp giao bù”:
Yes/No
 Sản phẩm không phù hợp
 Bổ sung thêm Tình
trạng hàng hoá
 Hư hỏng
 Cận date
 Hết date
 Khác
 Hạn sử dụng
 Format: YYYY-
MM
- Ghi chú
- Hình ảnh sản phẩm
Nếu là SPKPH thì yêu cầu chụp hình
o
ảnh  chọn + để mở camera
Nếu thiếu hàng thì không cần chụp
o
hình ảnh
 Sau khi cập nhật thành công thì button
sẽ chuyển xanh lá cây
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 54

55
User chọn vào button để xem lại thông tin đã
Khai báo nhiều sản phẩm cùng lúc khai báo
Nếu muốn xoá thông tin đã khai báo, chọn nút “Xoá”
Hiện thông báo
- EN: Do you want to delete the “Declare
reason for missing” of SKU 253900004?
2.3 Khai báo thiếu hàng Khai báo thiếu Declare missing Tại màn hình danh sách sản phẩm, bổ sung thêm
cho tất cả sản phẩm hàng cho tất cả goods for all action “Khai báo thiếu hàng cho tất cả sản phẩm”, để
sản phẩm products user có thể khai báo nhanh
Thông tin gồm:
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 55

56
- Số lượng SKU: tổng SKU chưa nhận đủ
- Số lượng sản phẩm: tổng sản phẩm chưa nhận
đủ
- Lý do thiếu hàng: mặc định = “Giao thiếu
hàng”, disable không cho user edit
- Nhà cung cấp giao bù: mặc định = “Có”, cho
phép edit
Chọn “Yes” để cập nhật lý do thiếu hàng cho tất cả sản
phẩm trong danh sách chưa nhận đủ theo số lượng
tương ứng
Nếu user chọn “Xoá tất cả” thì sẽ xoá tất cả các khai
báo thiếu hàng cho tất cả SKU chưa nhận đủ hàng đã
khai báo trước đó
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 56

57
2.4 Xoá sản phẩm đã Để xoá sản phẩm đã scan nhận trước đó, vào Danh
scan nhận sách sản phẩm  chọn Chi tiết  chọn “Xoá sản
phẩm”
Lưu ý: khi xác nhận Xoá hệ thống sẽ xoá tất cả số
lượng đã scan nhận trước đó, bao gồm cả thông tin
khai báo thiếu hàng (nếu có)
3 Kết thúc nhận hàng Kết thúc nhận End of receive Sau khi user nhận hết hàng từ nhà cung cấp giao tới
hàng - Nếu số lượng thực nhận chưa đủ theo số lượng của
PO => user phải khai báo lý thiếu hàng cho các SKU
chưa nhận đủ số lượng thì button “Kết thúc nhận
hàng” hiện lên
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 57

  58

- Nếu nhận đủ theo số lượng của PO => user chọn “Kết
thúc nhận hàng” để chuyển qua màn hình tiếp theo
Lưu ý: khi này mới gọi API để update PO trên
Inside thành “Receiving”
4  Cập nhật hình ảnh  Hoàn thành PO  Complete PO  User chọn “Thêm biên bản giao hàng”, để cập nhật
chứng từ cho PO  Thêm biên bản  Add delivery  hình ảnh chứng từ
|     | giao hàng        | document          | -  Nếu PO có đồng kiểm thì chụp hình ảnh biên        |
| --- | ---------------- | ----------------- | ---------------------------------------------------- |
|     | Kho              | Warehouse         | bản giao nhận hàng hoá                               |
|     | Tổng tiền        | Total amount      | -  Nếu PO không đồng kiếm thì chụp hình ảnh          |
|     | Không đồng kiểm  | No check of       | biên bản bàn giao kiện hàng                          |
|     |   / Đồng kiểm    | goods / check of  | Cập nhật ghi chú (nếu có)                            |
|     |                  | goods             | Chọn dấu “+” để mở camera và chụp hình ảnh chứng     |
|     | Vị trí           | Location          | từ bàn giao                                          |
|     | Tổng SKU         | Total SKU         | -  Hỗ trợ chụp tối đa 2 hình                         |
|     | Tổng sản phẩm    | Total items       | -  Chọn “Xoá hình” để xoá hình vừa chụp để           |
|     | Ghi chú          | Note              | chụp lại                                             |
|     | Hình ảnh chứng   | Document image    | Sau khi cập nhật hình ảnh chứng từ, user chọn “Lưu”  |
|     | từ               |                   | để lưu lại hình ảnh                                  |

| 5  Hoàn thành PO  |     |     | User chọn “Hoàn thành PO”        |
| ----------------- | --- | --- | -------------------------------- |
|                   |     |     |     Button này chỉ hiện lên khi  |

-  Số lượng sản phẩm đã scan nhận đủ theo PO

(bao gồm cả case có hàng không phù hợp)
Lưu ý:
-  PO đã cập nhật hình ảnh chứng từ giao hàng
Sau khi user đã cập nhật biên bản bàn
-  Hoặc số lượng nhận chưa đủ nhưng user đã
giao thì hệ thống sẽ check để show
khai báo tất cả sản phẩm thiếu và Nhà cung
button “Hoàn thành PO” hay “Hoàn
cấp không giao bù
thành phiên nhận hàng”
-  Nếu PO cần thêm hoá đơn thì phải thêm đầy

đủ thông tin của hoá đơn
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….  58

59
Nút Hoàn thành PO show lên khi Nếu chưa nhận đủ số lượng của 1 SKU trong PO, hiện
- Đã add biên bản giao giao hàng cảnh báo
- Đã nhận đủ SL theo PO
- Nếu nhận thiếu thì tất cả số
lượng thiếu đều có cùng reason
“Nhà cung cấp giao bù = No”
Nút “Hoàn thành phiên nhận hàng”
show lên khi
- Đã add biên bản giao hàng
- Điều kiện còn lại ngược lại với
nút “Hoàn thành PO” Lưu ý: cho phép nhận thiếu theo PO nhưng
phải nhận đủ số lượng của SKU trong PO
Nếu PO chưa cập nhật hình ảnh biên bản giao hàng,
hiện thông báo
- EN: Please update the delivery document
image.
Nếu chọn “Hoàn thành PO” hiện thông báo xác nhận
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 59

60
• EN: Do you want to confirm
completion of PO 10012402010027?
- Chọn “No” để tắt thông báo
- Chọn “Yes” xác nhận hoàn thành cho PO
• Cập nhật status cho PO = Received
• Cập nhật status cho ASN tương ứng =
Received
• Update tồn kho tương ứng
• Gọi API đồng bộ status Received lên
Inside
Nếu nhận thiếu số lượng
o
update thêm PO config =
“Waiting Adj Invoice”
Nếu nhận có item sản phẩm
o
không phù hợp update thêm
PO config = “Receiving Issue”
Bổ sung 17-10-2024
Khi gọi API receiving item PO bên inside
• Trường hợp có hàng không phù hợp thì gửi
thêm
“check_issue”:1, “issue”:{“note”: string (nếu
có), “unsuitable”:{“qty”: số lượng sản phẩm
không phù hợp, “media”: []string (nếu có)}}
• trường hợp số lượng item của sku không đủ
số lượng và ncc không giao lại thì gửi thêm
(inside sẽ tự compare số trên PO và số đã
nhận từ WMS để có được số thiếu)
“check_issue”:1, “issue”:{“note”: string (bắt
buộc)}
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 60

61
Bổ sung 24-10-2024
Khi kết thúc phiên nhận hàng hoặc Hoàn thành PO mà
có khai báo SPKPH thì vẫn import stock và update UID
có product status = “Damaged”
- Nếu có tạo lệnh vendor return thì sẽ dựa vào
PO source để lấy đúng UID có product status =
“Damaged” để Out ra
User chọn button “Hoàn thành phiên nhận hàng”
- Nếu chưa nhận đủ số lượng theo PO, hiện thông
báo xác nhận
-
• Chọn “Đóng” để tắt thông báo
• Chọn “Xác nhận” để xác nhận hoàn thành
phiên nhận hàng
Update status cho ASN (phiên nhận
o
hàng) tương ứng = Received
Update tồn kho tương ứng với số
o
lượng thực nhận theo phiên nhận
hàng
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 61

62
Thêm hoá đơn cho PO
Step Action UI Field (VN) Field (EN) Description
1 Show màn hình yêu Sau khi kết thúc nhận hàng mà số lượng thực nhận đã
cầu thêm hoá đơn đủ với số lượng confirm của PO, nếu PO chưa được bổ
cho PO sung hoá đơn trên hệ thống, hiện button “Thêm hoá
đơn”
User chọn “Thêm hoá đơn”
Show 2 lưu ý như sau
• Chọn “Kiểm tra lại” để tắt thông báo
• Chọn “Xác nhận” để tiếp tục
• Chọn “Kiểm tra lại” để tắt thông báo
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 62

63
• Chọn “Tôi đã hiểu” để chuyển qua bước
tiếp theo
2 Nhập thông tin hoá Show màn hình nhập thông tin hoá đơn gồm
đơn • Bổ sung thêm thông tin PO đang cần add hoá
đơn
• Tax code (mã số thuế)
Bắt buộc, nếu không nhập hiện thông
o
báo “Thông tin là bắt buộc”
(Information is required.)
MST phải từ 1 đến 8 ký tự bao gồm
o
chữ và số, không bao gồm ký tự đặc
biệt, nếu nhập không đúng hiện thông
báo “Mã số thuế phải từ 1 đến 8 chữ
số” (Tax code must be from 1 to 8
digits)
• Serial (ký hiệu)
Bắt buộc, nếu không nhập hiện thông
o
báo “Thông tin là bắt buộc”
(Information is required.)
Serial phải từ 1 đến 8 ký tự bao gồm
o
chữ và số, không bao gồm ký tự đặc
biệt, nếu nhập không đúng hiện thông
báo “Ký hiệu phải từ 1 đến 8 chữ số”
(Serial must be from 1 to 8 digits)
• Form (mẫu số)
Bắt buộc, nếu không nhập hiện thông
o
báo “Thông tin là bắt buộc”
(Information is required.)
• Total (Tổng tiền)
Phải bằng hoặc chênh lệch với tổng
o
tiền trên PO không quá 1.000 đồng,
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 63

64
nếu không sẽ hiện cảnh báo “Tổng số
tiền tren hoá đơn không hợp lệ”
(Total amount on invoice is invalid)
Lưu ý: nếu PO được add nhiều hoá
o
đơn thì tổng tiền của các hoá đơn
phải bằng tổng tiền trên PO hoặc
không lệch quá 1.000 đồng, không sẽ
báo lỗi “Tổng số tiền tren hoá đơn
không hợp lệ” (Total amount on
invoice is invalid)
• Ngày (mặc định ngày hiện tại, format : YYYY-
MM-DD), chỉ cho chọn ngày hiện tại hoặc quá
khứ, không cho chọn ngày của tương lai
• Chọn “Đóng” để tắt popup
• Chọn “Thêm” để cập nhật thông tin hoá
đơn (nếu chưa nhập đầy đủ thông tin thì
cảnh báo nhập thông tin tương ứng)
• Nhập ghi chú
• Hình ảnh hoá đơn: Chọn “+” để mở camera
để chụp hình hoá đơn hoặc lấy hình từ thư
viện ảnh (chụp tối đa 2 hình cho 1 hoá đơn)
Lưu ý: user có thể thêm nhiều hoá đơn
Thông tin hoá đơn sau khi thêm thành công
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 64

65
2.1 Chọn PO cần add Khi nhận PO gốc và PO gift cùng lúc, nhưng cả 2 PO
hoá đơn, cho case cùng yêu cầu add invoice thì khi user chọn add invocie
PO gốc và PO gift thì hệ thống sẽ yêu cầu user chọn PO cần add invoice
đều yêu cầu add - Bước add hoá đơn và cập nhật tương tự như
Hoá đơn chỉ add invoice cho PO gốc
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 65

66
3 Hoàn thành PO Button “Hoàn thành PO” chỉ hiện lên khi tất cả thông
tin của hoá đơn đã cập nhật đầy đủ thông tin bao gồm
hình ảnh
Tham khảo mô tả khi chọn “Hoàn thành PO”
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 66

67
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 67

68
Case 2 : Nhận PO Gift chung với PO thường
Step Action UI Field (VN) Field (EN) Description
1 Scan PO Gift để Nếu PO có PO gift đi kèm, sau khi, sau khi scan PO
nhận chung với PO thường thành công thì hiện cảnh báo
thường
User phải scan PO Gift để nhận chung với PO thường,
- Nếu PO không thuộc PO đang nhận, hiện thông báo
- Nếu PO chưa được verify invoice (trừ PO Gift 0
đồng), hiện thông báo
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 68

69
- Nếu PO đã được nhận hàng (status = Received), hiện
thông báo
- Nếu PO hợp lệ thì hiện thông tin PO lên màn hình (PO
2)
1.1 Chọn Loại nhận Tham khảo mô tả
hàng cho PO
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 69

70
1.2 Scan vị trí hoặc giỏ Scan vị trí hoặc giỏ cần chuyển hàng vào giống như ở
cần chuyển hàng case 1
vào (Tham khảo bước scan vị trí hoặc scan giỏ ở bước 5)
Sau khi scan vị trí hoặc giỏ hợp lệ  chuyển qua bước
tiếp theo
2 Scan sản phẩm cần - Việc scan sản phẩm để nhận hàng tương tự như nhận
nhận hàng hàng PO thường
Lưu ý : nếu trong PO thường và PO Gift có cùng SKU
cần nhận
• Nếu scan 1 lần mà SL SKU không bằng tổng
SL của 2 PO thì SL nhận sẽ ưu tiên cho PO
Gift trước sau đó mới tới PO thường (để
đảm bảo PO Gift luôn phải nhận đủ hàng –
dựa vào giá của sản phẩm nhỏ hơn để
phân biệt SKU của PO Gift)
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 70

71
3 Xem danh sách sản Khi chọn xem danh sách sản phẩm, do có 2 PO nên
phẩm đã nhận user sẽ chọn PO nào cần xem thông tin
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 71

  72

4  Cập nhật hình ảnh  Hoàn thành PO  Complete PO  User chọn “Thêm biên bản giao hàng”, để cập nhật
chứng từ cho PO  Thêm biên bản  Add delivery  hình ảnh chứng từ
gốc và PO gift  giao hàng  document  -  Nếu PO có đồng kiểm thì chụp hình ảnh biên
| Kho              | Warehouse         | bản giao nhận hàng hoá                               |
| ---------------- | ----------------- | ---------------------------------------------------- |
| Tổng tiền        | Total amount      | -  Nếu PO không đồng kiếm thì chụp hình ảnh          |
| Không đồng kiểm  | No check of       | biên bản bàn giao kiện hàng                          |
|   / Đồng kiểm    | goods / check of  | Cập nhật ghi chú (nếu có)                            |
|                  | goods             | Chọn icon camera để mở camera và chụp hình ảnh       |
| Vị trí           | Location          | chứng từ bàn giao                                    |
| Tổng SKU         | Total SKU         | -  Hỗ trợ chụp tối đa 2 hình                         |
| Tổng sản phẩm    | Total items       | -  Chọn “Xoá hình” để xoá hình vừa chụp để           |
| Ghi chú          | Note              | chụp lại                                             |
| Hình ảnh chứng   | Document image    | Sau khi cập nhật hình ảnh chứng từ, user chọn “Lưu”  |
| từ               |                   | để lưu lại hình ảnh                                  |

Update 20-11-2024
-  Bổ sung thêm thông biên bản giao hàng của
PO Gift
-  Cập nhật đầy đủ hình ảnh của PO gốc và PO
gift thì button “Lưu” sẽ hiện lên cho user chọn
Khi này button
-  Button “Kết thúc nhận hàng” với case 2 PO thì
đổi thành “Kết thúc nhận hàng cả 2 PO”
-  Button “Hoàn thành PO” với case 2 PO thì đổi
thành “Hoàn thành cả 2 PO”
Thông báo xác nhận đổi thành

Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….  72

73
 Các bước còn lại thực hiện tương tự như nhận PO thường
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 73

74
Nhận hàng Vải khai báo Group UID
- Khi scan nhận hàng cho các sản phẩm Vải thuộc cate thời trang (NVL)
Update 10-11-2025
Áp dụng cho các SKU không quản lý theo UID
o
Các SKU thuộc category sau
o
 Thời trang (bán thành phẩm)
 Thời trang (Phụ liệu)
 Thời trang (NVL)
Trong tên sản phẩm có từ “Vải”
o
• Nếu SKU không quản lý số lô và hạn sử dụng, hiện thông tin cho user cập nhật thông tin
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 74

75
Nhóm UID: scan nhóm UID đại diện cho cây/tấm vải được nhập hàng vào
o
 Không bắt buộc
• Nếu không khai báo UID group thì chỉ cần nhập số lượng và xác nhận như nhận SKU số lượng như bình thường
 Nhóm UID scan vào phải có trạng thái New, không đúng thì báo lỗi
• Nhóm UID phải có trạng thái New
 10-11-2025: có thể chuyển qua scan RFID mapping
• Lưu ý: nếu chỉ khai báo số lượng và chọn + để thêm vào danh sách thì input “Nhóm UID” và số lượng sẽ ẩn đi và
không cho thêm mới, tương tự như nhận sản phẩm theo số lượng. Tức 1 SKU chỉ có thể nhận hoặc theo RFID
mapping/UID Group hoặc là theo số lượng, không thể nhận cùng lúc 2 loại cho 1 SKU
Số lượng: là số Kg hoặc Mét của cây/tấm vải được quy đổi ra số lượng khi nhận hàng
o
 Số lượng này sẽ cộng lại cho tất các cây/tấm vải để ra được tổng số lượng của SKU cần nhận cho PO
 Sau khi scan nhận, chọn xác nhận để ghi nhận vào danh sách
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 75

76
• Nếu SKU có quản lý số lô và hạn sử dụng, hiện thông tin cho user cập nhật thông tin
Nhóm UID: scan nhóm UID đại diện cho cây/tấm vải được nhập hàng vào
o
Số lượng: là số Kg hoặc Mét của cây/tấm vải được quy đổi ra số lượng khi nhận hàng
o
 Số lượng này sẽ cộng lại cho tất các cây/tấm vải để ra được tổng số lượng của SKU cần nhận cho PO
Cập nhật thông tin số lô và hạn sử dụng cho sản phẩm
o
Sau khi scan nhận, chọn xác nhận để ghi nhận vào danh sách
o
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 76

77
Update màn hình chi tiết sản phẩm của các sản phẩm đã nhận đủ số lượng
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 77

78
Update 10-12-2025
- Với những SKU có quản lý UID group, user có thể scan nhận bằng RFID mapping, có những case sau có thể xảy ra
Nếu RFID mapping chưa tồn tại trên hệ thống thì giống như khai báo 1 UID group mới như luồng ban đầu, khi user submit hệ thống sẽ tự
o
gen ra 1 UID group mới và mapping với RFID được scan vào
Nếu RFID mapping hoặc UID group được scan vào đã tồn tại trên hệ thống (chạy cho luồng Transfer company, khi nào RFID mapping hoặc
o
UID group ở công ty xuất đã được out ra) hệ thống sẽ suggest số lượng sản phẩm của UID group (và cho phép user edit số lượng theo UID
group)  khi user submit hệ thống sẽ tự gen ra 1 UID group mới và mapping với RFID được scan vào
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 78

79
Bổ sung rules nhận PO gift riêng
Update 25-11-2024
- Với case 1 PO gốc có 1 PO gift thì
Có thể nhận chung PO gốc và PO gift nếu scan PO gốc trước
o
Có thể nhận riêng PO gift
o
- Với case 1 PO gốc có nhiều PO gift thì
Hiện thông báo
o
 VN: PO [10012402010027] có nhiều hơn 1 PO gift (10012402010028, 10012402010029), vui lòng hoàn thành tất cả PO gift trước
khi nhận PO gốc.
 EN: PO [10012402010027] has more than 1 gift PO (10012402010028, 10012402010029), please complete all gift PO before
receiving original PO.
Khi này user sẽ scan nhận từng PO gift cho tới khi hoàn thành, sau đó mới scan PO gốc để nhận vào
o
Update 22-01-2025
- Nếu tại thời điểm scan nhận PO gốc mà PO gift chưa đủ điều kiện để nhận (VD như chưa verify invoice) thì sẽ không hiện thông báo và cho nhận
PO gift, sau đó PO gift đủ điều kiện thì scan nhận sau
- Nếu PO gift thiếu hàng thì chỉ được nhận chung PO gốc lần đầu (PO có thể nhận thiếu hoặc không)  thì lần sau khi giao lại thì phải nhận riêng
cho cả Gift và Gốc
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 79

80
Nhận hàng SKU không barcode (update 22-05-2025)
- Với những SKU không có barcode, áp dụng cho tất cả các category nên người nhận không có barcode để scan, phải nhập SKU rất bất tiện, nên bổ
sung thêm tiện ích cho user xác nhận theo SKU
Tại màn hình scan SKU để nhận hàng, chọn “Nhận SKU không barcode” , show danh sách các SKU không có
o
barcode trong PO cần nhận hàng
 Hỗ trợ tìm kiếm sản phẩm theo SKU hoặc tên
 Thông tin gồm
• SKU - Tên sản phẩm
• Số lượng cần nhận
 SKU nào không có config HSD hoặc số lô thì cho user nhập số lượng thực nhận ngay dưới thông tin của SKU
• Chọn “Nhận hàng” để xác nhận đã nhận hàng cho SKU
SKU nào không có config theo HSD hoặc số lô thì sẽ hiện số lượng cho xác nhận
o
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 80

81
SKU có config theo HSD hoặc số lô thì không hiện số lượng cho xác nhận mà sẽ hiện popup để user nhập chung
o
với thông tin HSD và số lô
 Cập nhật thông tin số lượng đã nhận
 Hạn sử dụng
 Số lô
 Chọn “Nhận hàng” để xác nhận
 Sau khi xác nhận thì ghi nhận vào danh sách SKU đã nhận cho PO
Lưu ý: Khi nhận hàng cho SKU không barcode thì nếu vẫn còn SKU trong danh sách không có barcode chưa nhận thì vẫn
giữ lại tooltip để cho user nhận xong thì mới tắt
Hoặc nếu user muốn thoát ra thì nhấn ra ngoài
 Các thao tác còn lại vẫn như bình thường
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 81

82
Update 31-07-2025
- Ẩn thông tin số lượng cần nhận
- SL => đổi thành "Số lượng thực nhận",
• Nếu SL thực nhận = SL cần nhận thì cập nhật vào danh sách đã nhận như hiện tại => nếu còn SKU ko barcode cần nhận thì user nhận tiếp
(giữ như hiện tại)
• Nếu SL thực nhận > SL cần nhận hiện thông báo (đã có)
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 82

83
• Nếu SL thực nhận < SL cần nhận hiện thông báo
• "Số lượng thực nhận nhỏ hơn số lượng của PO (300/400). Bạn có muốn xác nhận không?"
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 83

84
Confirm paste ID (App)
• User login vào app với tài khoản được cung cấp
• Vào Purchase order  tính năng “Confirm pase ID”
Step Action UI Field (VN) Field (EN) Description
1 Scan mã PO cần xác Xác nhận dán ID Confirm paste ID User scan PO cần xác nhận dán ID
nhận dán ID Nếu PO chưa được nhận hàng, tức chưa chuyển status
Receiving hoặc Received thì hiện thông báo
- VN: PO [PO code] chưa được nhận hàng.
- EN: PO [PO code] has not received yet.
Nếu PO không tồn tại trên hệ thống thì hiện thông báo
- VN: PO [PO code] không tồn tại trên hệ thống.
- EN: PO [PO code] does not exist in the system.
Nếu PO không thuộc kho đang xử lý thì hiện thông báo
- VN: PO [PO code] không thuộc kho đang xử lý.
- EN: PO [PO code] is not in the warehouse
being processed.
Nếu PO đã hoàn thành dán ID cho sản phẩm, tức VAS
của PO đã Completed thì hiện thông báo
- VN: PO [PO code] đã hoàn thành việc dán ID
cho sản phẩm.
- EN: PO [PO code] has completed pasting ID for
the products.
 Nếu PO hợp lệ chuyên qua bước tiếp theo
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 84

  85

2  Chọn phiên cần dán  Tìm SKU,  Search SKU,  Khi user scan mã PO hợp lệ, show danh sách các phiên
ID  barcode, tên sản  barcode, Product  nhận hàng (ASN) có status Received nhưng chưa xác
| phẩm             | name              | nhận dán ID tương ứng của PO                   |
| ---------------- | ----------------- | ---------------------------------------------- |
|                  | PO note           | Thông tin gồm                                  |
| Ghi chú PO       | List of sessions  | -  Mã VAS                                      |
| Danh sách phiên  | waiting to be     | -  Trạng thái VAS                              |
| chờ dán          | pasted            | -  Loại VAS                                    |
|                  | Paste session     | -  Đánh giá chất lượng                         |
| Phiên dán (VAS)  | (VAS)             | -  Người dán: không có để trống, nếu phiên có  |
|                  | Pasted by         | nhiều người dán thì hiện thông tin người dán   |
| Người dán        | Received session  | đầu tiên                                       |
| Phiên nhận       | (ASN)             | -  Phiên nhận ASN                              |
| (ASN)            | Received by       | -  Người nhận theo phiên ASN                   |
|                  | Total SKU         | -  Ngày nhận: lấy theo ngày received           |
| Người nhận       | Total item        | -  Tổng SKU đã nhận trong ASN                  |
| Tổng SKU         |                   | -  Tổng sản phẩm đã nhận trong ASN             |
| Tổng sản phẩm    |                   | -  Vị trí: vị trí lưu trữ của ASN              |
Phân biệt màu theo VAS
-  Xám: Mới, chưa đánh giá và có thể xác nhận
dán
-  Xanh dương: đang thực hiện xác nhận dán ID
-  Cam: Mới, chưa đánh giá và chưa thể xác nhận
dán do chưa đánh giá chất lượng
User chọn phiên cần dán

-  Chỉ cho chọn 1 VAS cho 1 lần dán
-  Update status cho VAS = “Đang xử lý” (In-
Propress”
  Chuyển qua bước tiếp theo

24-12-2024: bổ sung rules khi hiển thị phiên dán VAS
-  Nếu VAS chuyển qua “Đang xử lý” (In-
Progress) thì chuyển xanh dương
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….  85

86
- Nếu VAS “Đang xử lý” của 1 user khác thì user
chỉ thấy và không được chọn để dán (disable
không cho chọn), chỉ được chọn phiên có
trạng thái “Mới” (Open), hoặc “Đang xử lý” mà
của user đó đang làm trước đó
- Hỗ trợ cho phép 1 VAS có nhiều người thực
hiện cùng lúc (khi cập nhật 1 thông tin hệ
thống sẽ gọi API để validation, nên vẫn đảm
bảo được data không bị trùng)
- Nếu user đang dán chưa lưu lại thông tin và
chưa xác nhận Hoàn thành 1 phần mà bị crash
app hoặc thoát app thì khi vào scan lại mã PO
thì vào lại màn hình dán của phiên đã chọn
trước đó, mà không cần phải chọn lại phiên
cần dán
Update 09-07-2025
Nếu VAS có yêu cầu đánh giá chất lượng sản phẩm
nhưng chưa được đánh giá mà chọn vào để xác nhận
dán thì hiện thông báo
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 86

87
3 Chụp hình, quay Lưu ý: ở bước này chỉ áp dụng cho các Category,
video cho sản phẩm không bao gồm các category sau đây:
- Sức khoẻ làm đẹp: quản lý/không quản lý
date, quản lý Imei
- Thuốc, Thuốc (GPP)
- (có thể bổ sung thêm 1 số category khác – sẽ
update sau)
Update 23-04-2025
- Áp dụng cho các sản phẩm có required
Serial/Imei và không thuộc category Sức khoẻ
- Làm đẹp
Sau khi user chọn vào phiên cần dán, hiện các thông
tin
- Tổng SKU cần dán : tổng SKU đã dán/ SKU cần
dán
- Tổng item cần dán: tổng item đã dán/ item
cần dán
- Vị trí lưu trữ của ASN tương ứng
Danh sách sản phẩm
- Tên sản phẩm
- SKU
- Barcode
- Số lượng đã cập nhật/Số lượng cần dán
User chọn vào sản phẩm cần cập nhật thông tin, show
thông tin gồm
- Tên sản phẩm
- SKU Barcode
- Số lượng cần chụp hình
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 87

88
User chọn vào dấu + để chọn Chụp hình hoặc quay
video cho sản phẩm
- Cho phép chụp tối đa 5 hình
- Chỉ quay 1 video, giới hạn 15 giây để đảm bảo
dung lượng khi up lên hệ thống
- User có thể chụp hình ảnh hoặc quay video
hoặc cả 2
Nhấn “Lưu” để qua bước tiếp theo
Lưu ý: Nếu sản phẩm không có quản lý Imei thì sau khi
chụp hình, quay video  nhấn Lưu thì xem như hoàn
thành VAS cho SKU đó
Khi này các UID sẽ được chuyển từ trạng thái
“Received” qua “In-Bin”  khi này thì các SKU này mới
có thể sử dụng cho đơn hàng hoặc IT
4 Cập nhật thông tin Tổng SKU cần Total SKUs to be Thông tin sản phẩm cần dán gồm
Serial/Imei/Label dán paste - Tên sản phẩm
code cho sản phẩm Total items to be - SKU Barcode
Tổng item cần paste
- Số lượng đã cập nhật/ Số lượng cần cập nhật
dán List of product
- Tuỳ chọn thông tin cần cập nhật cho SKU: hệ
Danh sách sản
thống auto chọn thông tin cần cập nhật
phẩm Location
Nếu là cate: CCDC, CCDC PB...là những cate sẽ
Vị trí
thực hiện theo luồng VAS
• Và wms_product.wms_config&131072
> 0 => required QR, tức bật ON cập nhật
QRCode
• Hoặc wms_product.config&8 > 0 =>
required Imei, tức bật ON cập nhật
Sau khi cập nhật thông tin nếu muốn
Serial/Imei
chỉnh sửa thông tin thì chọn vào icon Cập nhật 25-02-2025
o
để chỉnh sửa thông tin và lưu lại  Hiện tại sẽ luôn tắt option
Serial dưới BE, user chỉ cần
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 88

89
cập nhật QRCode, sau này cần
sẽ mở ra sau
 Serial nếu không có thông tin
thì hệ thống WMS sẽ tự gen
mã theo rules sau:
[1023][YYMMDD][6 số tăng
dần]
• Nếu sau này có kiểm kê mà
user count lại theo Serial
thì sẽ update Serial mới đè
lên Serial mà hệ thống gen
ra trước đó
• Update 22-05-2025
• Nếu SKU có config required Imei
thì sẽ auto bật, nhưng không bắt
buộc nhập, nếu nhập thì lưu vào
còn không nhập thì để trống
Ngược lại với 2 case trên thì chỉ cần chụp hình, bỏ
qua bước cập nhật QRCode hoặc Serial
Lưu ý: do mã QRCode in ra có dạng Object nên khi
scan hệ thống sẽ tự động cắt chuỗi để lấy đúng thông
tin cần lấy
 Lấy thông tin “Code”
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 89

90
 Thông tin nào được tích chọn thì ô scan của
thông tin đó sẽ được show lên để user scan
• Nếu chỉ cập nhật 1 thông tin thì khi user scan
thì tự động add vào danh sách. Nếu user nhập
thì nhấn icon dấu + để add vào danh sách
• Nếu chọn cập nhật cả 2 thông tin thì khi scan
Qrcode hợp lệ, sẽ tự động chuyển focus qua ô
scan Serial/Imei để tiếp tục scan và add vào
danh sách
Sau khi cập nhật thì nhấn Lưu
- Nếu cập nhật chưa đủ số dòng thông tin thì
hiện thông báo xác nhận
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 90

91
• Chọn “Đóng” để tắt thông báo
• Chọn “Xác nhận” để lưu lại thông tin
đã cập nhật
- Đồng thời update số lượng đã cập nhật thông
tin tương ứng ở danh bên ngoài
Phân biệt màu
- Màu xám: chưa cập nhật thông tin
- Màu xanh dương: cập nhật 1 phần
- Màu xanh lá: đã cập nhật đủ số lượng yêu cầu
4.1 Scan RFID cho sản Scan RFID để xác nhận dán ID cho sản Lưu ý: đối với SKU required RFID thì không cần qua
phẩm phẩm có 2 option bước chụp hình sản phẩm khi VAS
1. Scan RFID cho nhiều SKU cùng lúc, dùng
để xác nhận dán ID nhanh cho nhiều sản Chọn để scan RFID cho sản phẩm
phẩm có trong VAS
Hệ thống đọc RFID từ đầu đọc và trả thông tin lên màn
hình App
Case 1: nhận RFID đã define trên hệ thống, tức hàng
được chuyển từ nhà máy Long An chuyển về các
Shop (trong cùng hệ thống nội bộ của Hasaki)
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 91

92
Với case này thì có thể scan RFID cho cả 2 option là
cho nhiều SKU hoặc từng SKU
Tab Hợp lệ
2. Scan RFID cho từng SKU, dùng để xác
nhận dán cho từng ID
Tab không hợp lệ
Xem chi tiết RFID của từng SKU hợp lệ
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 92

93
Case 2: nhận hàng từ vendor bên ngoài, khi này mới
dán RFID lên sản phẩm, chưa có sẵn trên hệ thống
Với case này thì chỉ cho scan khai báo RFID cho từng
SKU, không cho scan nhiều SKU cùng lúc
Khi này tab không hợp lệ sẽ không có data, chỉ có tab
Hợp lệ sẽ load các RFID đã scan lên màn hình
Sau khi scan xong RFID cho sản phẩm thì nhấn Xác
nhận để submit thông tin cho từng sản phẩm
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 93

94
5 Xác nhận Hoàn Hoàn thành Complete Nếu chưa cập nhật đủ số lượng yêu cầu mà user chọn
thành “Hoàn thành”, hiện thông báo xác nhận
- Chọn “No” để tắt thông báo
- Chọn “Yes” để xác nhận hoàn thành
• Khi này VAS vẫn giữ nguyên status “In-
Progress
• Đồng thời update QRCode, Serial/Imei
cho những UID tương ứng
Nếu đã cập nhật đủ số lượng yêu cầu mà user chọn
“Hoàn thành”, hiện thông báo xác nhận
- Chọn “No” để tắt thông báo
- Chọn “Yes” để xác nhận hoàn thành
• Khi này VAS sẽ update status
“Completed”
• Đồng thời update QRCode, Serial/Imei
cho những UID tương ứng
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 94

95
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 95

1
01-12-2025: Create/Update VAS manual
Link Mockup: https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO?node-
id=1562-910&t=AQkfWtXPxrajXThC-4
Web: Update màn hình quản lý VAS
- Ở màn hìn danh sách VAS (Menu: Inbound / VAS)
Thông tin “Type” bổ sung thêm giá trị “Manual” để phân biệt với những VAS được
o
tạo tự động
- Ở màn hình VAS detail
Với những VAS được tạo manual và có trạng thái là Open hoặc In-Progress thì cho
o
user có quyền update lại số lượng “Qty received”
Do trong quá trình khai báo RFID hoặc Serial thì số lượng hàng vật lý có thể không khớp với số lượng
đã khai báo trước đó

97
Nhận hàng PO SKU có RFID của vendor ngoài
- Menu: Purchase order / Comfirm paste ID
- Với SKU có config RFID và KHÔNG thuộc Cate Thời trang và Brand Synctive thì khi nhận PO
vẫn scan nhận theo số lượng giống Serial, và sinh VAS yêu cầu khai báo RFID
- Khai báo VAS với VAS type = RFID
Chọn VAS cần khai báo
o
Chọn SKU cần khai báo
o
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 97

98
User có thể scan từng barcode RFID (nếu có) hoặc chọn để scan RFID hàng loạt
o
bằng máy scan RFID
 Validate
• Với luồng này thì tất cả RFID phải chưa tồn tại trên hệ thống thì
được hiểu là hợp lệ
• Nếu RFID đã tồn tại trên hệ thống thì là không hợp lệ
 Lưu ý khi scan bằng máy scan RFID thì phải đảm bảo chỉ có RFID của sản
phẩm cần khai báo, không để lẫn hàng khác vào để tránh hệ thống ghi nhận
sai
 Nếu số lượng RFID scan vào lớn hơn số lượng RFID cần khai báo, hiện thông
báo
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 98

99
• Xoá các RFID dư hoặc scan lại cho đúng số lượng và nhấn Lưu
• Ghi nhận thông tin RFID cho SKU chọn khai báo
 Làm tương tự cho tới khi khai báo đẩy đủ SKU có trong VAS
 Sau khi khai báo đầy đủ thì nhấn “Hoàn thành” để kết thúc VAS
• Nút “Hoàn thành” chỉ hiện lên khi tất cả các SKU đã khai báo đủ số
lượng
Tạo thủ công VAS
- Menu: Purchase order / Comfirm paste ID
- Tại màn hình quản lý các VAS cần khai báo, chọn “Tạo mới”
Kho: lấy thông tin ở màn hình ngoài đã chọn
o
 Bắt buộc chọn
 Hoặc user có thể chọn lại theo nhu cầu
 Load thông tin kho theo phân quyền user
Loại VAS
o
 Mặc định: không chọn
 Bắt buộc chọn
 Giá trị
• RFID: để tạo VAS cho các SKU có config serial cần khai báo bổ sung
• Serial: để tạo VAS cho các SKU có config serial cần khai báo bổ sung
Mã phiếu nhập nguồn
o
 Thường là mã PO đã nhập hàng cho SKU cần khai báo
 Không bắt buộc
 Nếu có nhập thì validate mã nhập vào có tồn tại trên hệ thống hay không,
nếu không thì hiện thông báo
• Mã [Code] không tồn tại trên hệ thống.
Thêm sản phẩm cần khai báo
o
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 99

100
 Hỗ trợ scan barcode, SKU hoặc tìm theo tên sản phẩm
• Chọn tìm theo tên để mở modal tìm sản phẩm theo tên có sẵn
 Số lượng tồn kho hệ thống
• Sau khi scan hoặc chọn SKU hợp lệ, hệ thống sẽ check tồn kho các
UID có trạng thái In-Bin và Picklisted và hiện lên màn hình để user
biết
 Số lượng cần khai báo VAS
• User nhập số lượng cần khai báo theo số lượng gợi ý từ hệ thống
• Chỉ cho nhập số nhỏ hơn hoặc bằng số lượng tồn kho của hệ thống,
nếu nhập lớn hơn thì báo lỗi
Số lượng cần khai báo (125) không được lớn hơn số lượng
o
tồn kho trên hệ thống (120).
 Tuỳ vào loại VAS lựa chọn, SKU được add vào danh sách khai báo phải được
config tương ứng, nếu không sẽ hiện thông báo
Có thể chọn để xoá SKU ra khỏi danh sách đã add trước đó, hiện thông báo xác
o
nhận
Sau khi add đủ SKU cần khai báo, chọn “Tạo mới” để tiến hành tạo VAS, hiện thông
o
báo xác nhận
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 100

101
 Chọn “Xác nhận” để tạo VAS và chuyển qua bước khai báo cho VAS vừa tạo
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 101

  102

Import packing list
-  Template import

Lưu ý: Nếu import lại nhưng các thông ti PO code, SKU, Roll code, Batcode trung với data đã
có trên hệ thống thì sẽ cho update lại số lượng yêu cầu
Validate
| Validate  | Thông báo tiếng Việt  | Thông báo tiếng Anh  |
| --------- | --------------------- | -------------------- |
PO code để trống  Dòng N – Mã PO không được  Line N – PO code cannot be
|     | để trống.  | empty.  |
| --- | ---------- | ------- |
PO code không tồn tại trên hệ  Dòng N – Mã PO không tồn tại  Line N – PO code does not
| thống  | trên hệ thống.  | exist in the system.  |
| ------ | --------------- | --------------------- |
SKU để trống  Dòng N – SKU không được để  Line N – SKU cannot be empty.
trống.
SKU không tồn tại trên hệ  Dòng N – SKU không tồn tại  Line N – SKU does not exist in
| thống  | trên hệ thống.  | the system.  |
| ------ | --------------- | ------------ |
SKU không tồn tại trong PO  Dòng N – SKU không tồn tại  Line N – SKU does not exist in
|     | tronng PO  | the PO.  |
| --- | ---------- | -------- |
Roll code để trống  Dòng N – Mã cuộn không được  Line N – Roll code cannot be
|     | để trống.  | empty.  |
| --- | ---------- | ------- |
Batch code để trống  Dòng N – Mã lô không được để  Line N – Batch code cannot be
|     | trống.  | empty.  |
| --- | ------- | ------- |
Số lượng yêu cầu không được  Dòng N – Số lượng yêu cầu  Line N – Requested quantity
| để trống  | không được để trống.  | cannot be empty.  |
| --------- | --------------------- | ----------------- |
Số lượng yêu cầu nhập số âm  Dòng N – Số lượng yêu cầu  Line N – Requested quantity is
| hoặc ký tự  | không hợp lệ  | invalid.  |
| ----------- | ------------- | --------- |
Thông tin bị trùng lặp giữa các  Dòng N – Dữ liệu đã tồn tại  Line N – Data already exists in
dòng (2 dòng giống hệt thông  trên file import  the import file.
tin nhưng khác qty request)

Màn hình quản lý thông tin packing list được import

Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS….
102

103
- Với những PO có trạng thái khác Received, hỗ trợ cho user
Chọn nhiều dòng để xoá và import lại
o
Chọn edit số lượng yêu cầu
o
Update 29-01-2026
Các phần cần update cho Packing list PO và validate khi scan nhận PO cate Thời trang (NVL) và tên
sản phẩm có chữ "Vải"
Import Packing list PO
• Sau khi check validate data trên file import hợp lệ => tới bước Save data vào hệ thống, bổ
sung thêm validate
Nếu tổng Qty request của SKU > ± 5% Qty confirm của SKU trong PO thì hiện cảnh
o
báo
 VN: PO 10012601001737, SKU 422504712 có tổng số lượng trong packing list
lớn hơn ± 5% so với số lượng yêu cầu trên PO. Nếu xác nhận import thì liên hệ
BOD để được duyệt trước khi nhân hàng.
 EN: PO 10012601001737, SKU 422504712: The total quantity in the packing list
exceeds ±5% of the PO quantity. If confirming the import, please contact BOD
for approval before receiving.
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 103

104
 Action "Kiểm tra lại" để tắt thông báo => ko lưu data
 Action "Xác nhận Import" để xác nhận import date
Nếu PO đã chuyển receiving thì khi import packing list bổ sung thì mặc định các SKU
o
sẽ auto approved
Inbound
• Data table
Bổ sung cột Packing list PO, value
o
 Chờ duyệt / Waiting for Approval
 Khi PO vải vừa rớt xuống WMS thì sẽ ở trạng thái này
 Có button Approve (dưới trạng thái), hiện thông báo xác nhận
 VN: Bạn có chắc chắn muốn duyệt cho nhận hàng theo packing
list không?
 EN: Do you want to approve receiving based on the packing list?
 Đã duyệt / Approved
 Nếu Packing list PO import vào vẫn nằm trong khoảng cho
phép ± 5% thì sẽ auto approved
 Link: nhấp vào để hyperlink và trang Packing list theo filter của PO
 (03-02-2026) Bổ sung rules khi staus packing list PO đang là Approved
 Nếu có import lại Packing list mà validate tổng Qty request của SKU
> ± 5% Qty confirm của SKU trong PO thì vẫn sẽ chuyển về Waiting
for
 Nếu có update lại số lượng hay xoá bớt đi thì trạng thái sẽ không
thay đổi (do chưa thể tính toán lại nên tạm thời chưa control trên
UI)
• More filter
Packing list PO, value
o
 Chờ duyệt / Waiting Approve
 Đã duyệt / Approved
• Detail
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 104

105
Hiện thêm thông tin Packing list PO và button Approve cho trạng thái Waiting
o
Approve
Receving PO - App
• Bổ sung validate khi scan nhận PO
Nếu Packing list ở trạng thái Waiting Approve thì không cho nhận, hiện thông báo
o
"PO chưa được duyệt Packing list nên không thể nhận hàng."
Nếu Packing list của PO chưa được import thì không cho nhận, hiện thông báo "PO
o
chưa import Packing list nên không thể nhận hàng."
Nếu Packing list PO đã Approved nhưng ko có data import thì vẫn passed cho nhận
o
PO
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 105

106
Nhận hàng PO cho SKU vải theo packing list
SKU vải là con lẻ
- Khi scan nhận SKU combo vải
Nếu PO chưa import packing list thì vẫn cho nhận theo UID group như bình thường
o
Nếu PO đã import packing list thì
o
 Khi user nhập số lô hệ thống suggest danh sách mã theo packing list để user
chọn (user vẫn có thể nhập mã cuộn khác suggest)
 Sau khi có đầy đủ thông tin số lô + mã cuộn thì sẽ show thông tin số lượng
yêu cầu từ packing list
 User nhập số lượng thực nhận sau khi cân
• Chọn hệ số cần quy đổi ra đơn vị cần nhận (pcs)
• Mặc định là x1
 Khai báo nhóm UID và hạn sử dụng cho sản phẩm
 Nhấn + để thêm vào danh sách đã nhận
• Lưu ý: số lượng thực nhận sẽ được nhân với hệ số được chọn khi
cập nhật vào danh sách
 Chụp hình cho sản phẩm đang khai báo nhận
 Tiếp tục thực hiện cho đến khi nhận đủ số lượng của PO
• Thông tin khai báo sau khi scan nhận và khai báo hợp lệ
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 106

107
Thông tin ghi nhận sau khi nhấn thêm
o
 Mã cuộn: theo user nhập
 Nhóm UID: theo user nhập
 Hình ảnh mà user chụp
 Số lô: theo user nhập
 SL yêu cầu: lấy từ packing list (nếu có)
 SL thực nhận: theo user nhập và nhân với hệ số quy đổi (nếu có)
 Nhận lệch = SL thực nhận – SL yêu cầu
 HSD: theo user nhập
 Lưu ý:
• Nếu số lượng thực nhận > số lượng yêu cầu từ packing list thì ghi
nhận số lượng theo packing list
• Ngược lại thì ghi nhận theo số thực nhận
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 107

108
SKU vải là combo
- Khi scan nhận SKU combo vải
Nếu PO chưa import packing list thì vẫn cho nhận theo UID group như bình thường
o
Nếu PO đã import packing list thì
o
 Khi user nhập số lô hệ thống suggest danh sách mã theo packing list để user
chọn (user vẫn có thể nhập mã cuộn khác suggest)
 Sau khi có đầy đủ thông tin số lô + mã cuộn thì sẽ show thông tin số lượng
yêu cầu từ packing list
 User nhập số lượng thực nhận sau khi cân
• Cho nhập số thập phân
 Khai báo nhóm UID và hạn sử dụng cho sản phẩm
 Nhấn + để thêm vào danh sách đã nhận
• Lưu ý: số lượng thực nhận khi này sẽ là số thực theo combo trong
packing list (không nhân với với hệ số quy đổi từ combo qua con lẻ)
 Chụp hình cho sản phẩm đang khai báo nhận
 Tiếp tục thực hiện cho đến khi nhận đủ số lượng của PO
• Lưu ý: Tổng số lượng thực nhận khai báo nhóm UID cho SKU combo
phải là số nguyên dương.
• Thông tin khai báo sau khi scan nhận và khai báo hợp lệ
Thông tin ghi nhận sau khi nhận thêm
o
 Mã cuộn: theo user nhập
 Nhóm UID: theo user nhập
 Hình ảnh mà user chụp
 Số lô: theo user nhập
 SL yêu cầu: lấy từ packing list (nếu có)
 SL thực nhận: theo user nhập và nhân với hệ số quy đổi (nếu có)
 Nhận lệch = SL thực nhận – SL yêu cầu
 HSD: theo user nhập
 Lưu ý:
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 108

109
• Nếu số lượng thực nhận > số lượng yêu cầu từ packing list thì ghi
nhận số lượng theo packing list
• Ngược lại thì ghi nhận theo số thực nhận
 Sau khi xác nhận thì hệ thống sẽ tự động nhân với hệ số của con lẻ để cập nhật đúng stock
cho con lẻ
02-04-2026: Bổ sung thông tin “Trừ lõi”
- Tại màn hình khai báo UID group cho SKU vải, bổ sung thêm thông tin “Trừ lõi” (Tare
(weight))
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 109

110
SKU normal SKU combo
- Thông tin “Trừ lõi”: cho phép user nhập số thập phân
Với SKU normal
o
 Giá trị mặc định = 0
 Khi user thay đổi số thì sẽ lưu lại cho những lần thao tác sau
 Sau khi user nhập đầy đủ thông tin và submit thì sẽ lấy
• [Số lượng thực nhận] – [Trừ lõi]
• Và so sánh với Số lượng yêu cầu từ Packing list theo rule để ghi nhận
số lượng thực nhận
 Lưu ý: khi số lượng thực nhận có nhân với hệ thống thì
• [Số lượng thực nhận] * [Hệ số] – [Trừ lõi]
Với SKU combo
o
 Tương tự như SKU normal, chỉ khác là không có chỗ nhân hệ số quy đổi
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 110

111
Update 16-04-2026
(12-05-2026: Pending lại không làm tiếp do vận hành Purchase order gặp kho khăn khi làm việc với
Vendor)
Import Packing list
- Update template import bổ sung thêm các cột sau
Delivery method: có 2 lựa chọn
o
 Giao 1 phần (Partial)
• Nếu chọn option này thì khi import sẽ không validate chỗ lệch +-5%,
chỉ cần total số lượng trong Packing list nhỏ hơn total số lượng trong
PO là cho import
• Nếu PO đã chọn option này thì những lần import sau cũng sẽ dùng
option này cho packing list
 Giao full PO (Full PO)
• Chọn option này thì giữ nguyên validate như cũ
Khổ vải (Width)(m)
o
 Thông tin khổ vải do NCC cung cấp
 Sử dụng khi SKU được đặt hàng bằng đơn vị tính là Yard hoặc Mét, dùng để
quy đổi từ cân nặng (Kg) qua Yard và Mét
Định lượng vải (GSM)(g/m2)
o
 Thông tin định lượng vải do NCC cung cấp
 Sử dụng khi SKU được đặt hàng bằng đơn vị tính là Yard hoặc Mét, dùng để
quy đổi từ cân nặng (Kg) qua Yard và Mét
Gross quantity(Kg) (thay thế cho cột Quantity request cũ) cân nặng bao gồm lõi và
o
bao bì (nếu có)
 Nếu đơn vị tính là Kg thì đây là cân nặng thực tế của sản phẩm đã bao gồm
lõi, bao bì
 Ngược lại là trọng lượng thực của sản phẩm mà nhà cung cấp giao qua
Net quantity (Kg) cân nặng thực của sản phẩm không bao gồm lõi và bao bì (nếu có)
o
 Nếu đơn vị tính là Kg thì đây là cân nặng thực tế của sản phẩm KHÔNG bao
gồm lõi, bao bì
 Ngược lại là trọng lượng thực của sản phẩm mà NCC giao qua
Lưu ý: Nếu sản phẩm không có bao bì, lõi thì Gross quantiy sẽ bằng Net quantity
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 111

112
Page quản lý Packing list
- Menu: Inobount / Packing list PO
- Bổ sung thêm các cột tương ứng như trên file excel import
- Tạm thời ẩn tính năng edit số lượng trên giao diện của packing list để hạn chế các case phát
sinh, người dùng cần thì import lại để update lại thông tin
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 112

113
Update UI nhận SKU có UID group
UI update: https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO?node-
id=2302-771&t=SP4WzMQ9GNwBPqgj-4
- Màn hình khi scan nhận SKU vải có yêu cầu khai báo UID group
- Số lượng yêu cầu
Cho hiển thị 2 thông tin Gross Qty và Net Qty trên file Packing list theo số lô và số
o
cuộn tương ứng đã chọn
- Thông tin “Trừ lõi” hệ thống tự tính dựa vào thông tin “Gross Qty” và “Net Qty”
Trừ lõi = Gross Qty - Net Qty
o
 Nếu 2 số này bằng nhau thì trừ lõi sẽ = 0
 Disable không cho edit
- Công thức quy đổi từ Kg thành
Yard = [Weight(Kg) * 1000] / [Width(m) * GSM(g/m²) * 0.9144]
o
Mét = [Weight(Kg) * 1000] / [Width(m) * GSM(g/m²)]
o
Lưu ý: case quy đổi này chỉ áp dụng khi nhận PO cho SKU có đơn vị tính (lấy từ
o
Inside) là Yard hoặc Mét. Còn các đơn vị tính khác thì vẫn ghi nhận theo số lượng
(Kg) lấy từ cân
Trong đó
 Đơn vị tính của SKU: lấy từ đơn vị tính trong Attributes của Inside
 Weight: cân nặng của SKU lấy từ cân
 Khổ vải (Width): lấy từ Packing list của mã lô và mã cuộn tương ứng
 Định lượng vải (GSM): lấy từ Packing list của mã lô và mã cuộn tương ứng
- VD cách ghi nhận số lượng thực nhận cho UID group cho SKU nhập hàng theo Yard
Thông tin import trên Packing list
o
 Width = 1.5 (m)
 GSM = 200 (g/m²)
 Gross qty = 15.3 (kg)
 Net qty = 15 (kg)
• => Tính ra Lõi, bao bì = 0.3
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 113

114
Tính ra số Yard cần nhận theo cân nặng theo công thức
o
 Yard cần nhận = (15 * 1000)/((180 * 200) * 0.9144)
 Ghi nhận số này vào số thực nhận
 Do SKU đặt hàng bằng đơn vị Yard hoặc Mét nên trên Packing list sẽ không
có thông tin này, nên khi submit thì thông tin SL yêu cầu và Nhận lệch sẽ
không có (để trống)
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 114

115
Update rules nhận dư cho PO vải (20-04-2026)
- UI update ASN detail: https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-
Receiving-PO?node-id=2328-217&t=vqPSxx7QkeN94Zjm-4
Màn hình chi tiết ASN
o
 Qty received: vẫn là số lượng thực nhận theo PO như hiện tại (không bao
gồm số lượng dư)
 Qty per ADJ (Số lượng theo ADJ): số lượng dư mà hệ thống tự động tạo
phiếu điều chỉnh để import vào hệ thống để ghi nhận stock theo đúng số
thực nhận
Màn hình chi tiết UID group theo SKU
o
 Bổ sung thêm 2 cột
• Số lượng theo PO (Qty per PO): số lượng mà hệ thống ghi nhận theo
số trên PO
• Số lượng theo ADJ (Qty per ADJ)
Rules update:
• Khi khai báo nhận cho từng cuộn vải (UID group), Ghi nhận hết theo số lượng thực nhận,
không quan tâm SL thực nhận nhỏ hay lớn hơn Packing list
Nếu total SKU thực nhận < SL trên PO => ghi nhận theo số lượng thực nhận và yêu
o
cầu NCC điều chỉnh hoá đơn như luồng hiện tại
Nếu total SKU > SL trên PO
o
 Ghi nhận Qty cho UID group theo số của Packing list
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 115

116
 Số dư sẽ được ADJ vào và sinh ra UID mới vẫn là UID group được khai báo khi
nhận
Khi khai báo UID group cho từng cây vải, nếu số lượng thực nhận > 10% số lượng
o
trên Packing list thì hiện thông báo để user check lại trước khi xác nhận
 VN: Số lượng thực nhận lớn hơn 10% so với Packing list, bạn có muốn xác nhận
nhận hàng không?
 EN: The actual received quantity exceeds the packing list by more than 10%. Do
you want to confirm the receipt?
 Chọn "Kiểm tra lại" tắt thông báo và giữ nguyên màn hình đang khai báo để
user check lại
 Chọn "Xác nhận" để ghi nhận vào danh sách nhận hàng
VD (xem file excel đính kèm)
o
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 116

117
 SKUA, PO order 105 mét, PKL = 106.15, Thực nhận 106.60
 Packing list NCC giao qua tổng 10 cây, mỗi cây dao động từ 9-12m
 Với những cây có qty thực nhận <= qty trên packing list thì ghi nhận UID và UID
gr theo qty thực nhận như cũ
 Với những cây có qty thực nhận > qty trên packing list thì
 Ghi nhận UID gr có qty = qty của packing list
 (Total) Số lượng dư ra sẽ được tạo ADJ import vào và phần chênh lệch của 1
cuộn sẽ sinh ra 1 UID mới có cũng UID gr với cây đã khai báo
• Sau khi nhận hàng xong dưới WMS thì khi push lên Inside
Nếu total SKU < SL trên PO => yêu cầu điều chỉnh hoá đơn
o
Nếu total SKU > SL trên PO => chỉ push theo số của PO, số còn lại WMS sẽ tự tạo ADJ để
o
imp vào
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 117

118
Update 17-05-2026
PO sample & PO chính
- Trên Inside sẽ bổ sung thêm 1 type mới cho PO là "Sample", tính chất của PO type Sample sẽ
tương tự với PO Gift chỉ là 1 type mới để phân biệt với type Gift để phục vụ cho luồng
quality control
Cần ghi nhận thông tin PO "Sample" thuộc PO gốc nào và ngược lại
o
Khi NCC giao hàng thì PO "Sample" sẽ được nhận vào trước và thực hiện Quality
o
control trước (khi này sẽ chưa nhận PO gốc trên WMS)
 Quality control SKU của PO "Sample" như luồng thông thường
 Tiêu chí thiết lập cho SKU của PO sample và PO gốc sẽ giống nhau (phase 1)
• Sau này nếu tiêu chí nào của 2 PO map với nhau thì có thể link kết
quả đánh giá từ SKU của PO "Sample" qua SKU của PO gốc (xem xét
làm sau)
Sau khi PO "Sample" và Quality control của SKU trong PO "Sample" Completed" và
o
có kết quả Đạt => thì mới cho nhận PO gốc, nếu không thoả điều kiện thì cảnh báo
và không cho nhận PO gốc vào
 Thông báo khi scan nhận PO gốc khi PO "Sample" chưa completed và kết
quả QC không Đạt
• VN: PO mẫu thử 10012510205805 của PO gốc 10012510205801
chưa được nhận hàng hoặc kết quả đánh giá chất lượng KHÔNG ĐẠT
nên không thể nhận hàng cho PO gốc.
• EN: Sample PO 10012510205805 of original PO 10012510205801
has not been received or the quality evaluation result is FAILED,
therefore the original PO cannot be received.
- Sau khi nhận PO sample và đánh giá Passed
Nhận PO chính lần đầu sẽ cho nhận max 30% và tạo request QC cho 30% UID gr
o
nhận vào
 Khi mới nhận vào mà chưa đánh giá QC thì UID sẽ treo trạng thái
“Received”, sau khi đánh giá xong (passed/failed) thì sẽ chuyển về trạng thái
Inbin
 Nếu QC failed thì không cho nhận phần còn lại, trả lại nhà cung cấp
 Nếu QC passed thì cho nhận vào bình thường và treo status cho UID group,
cột “Đánh giá đạt = No”, khi này UID chỉ được transfer, không cho IT các UID
group này qua kho khác
VD: SKUA packing list có 18 cây thì chỉ cho nhận max 30% là 5.4 cây, làm tròn lên 6
o
cây, nếu nhận hơn thì báo lỗi
 VN: PO chỉ cho nhận tối đa 30% cuộn vải theo từng lô cho phiên nhận đầu
tiên.
 EN: The PO only allows receiving up to 30% of the fabric rolls per batch for
the first receiving session.
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 118

119
Cho nhiều user cùng nhận cùng lúc
Rules
- Mỗi 1 user scan nhận thì tạo 1 ASN riêng, trong cùng 1 thời điểm có thể có nhiều hơn 1 ASN
status Receiving
- 1 SKU cho phép nhiều user cùng nhận
Vấn đề: khi nhận SKU normal có UID group thì sau khi khai báo submit thì đã tính
o
vào total qty đã nhận nên sẽ validate được khi nào sẽ vượt số lượng để warning
 Nếu SKU là combo thì sau khi khai báo xong hết mới tính vào total qty nên sẽ
ko check được số lượng vượt realtime
 Và case nhận UID group cũng đang cho nhận dư nên càng khó control hơn
Giải pháp:
- Với PO loại này sẽ bổ sung thêm cờ để force cho nhiều PO cùng nhận hàng (có thể force cho
PO open và receiving)
Button force trong Inbound detail, type PO "Cho phép nhiều người cùng nhận hàng"
o
(Allow multiple users to receive)
- Mỗi 1 user scan nhận thì tạo 1 ASN riêng, trong cùng 1 thời điểm có thể có nhiều hơn 1 ASN
status Receiving
Nếu là SKU normal (ko khai báo UID gr) thì nhận như bình thường => nêu Qty thực
o
nhận từ nhiều user > qty của PO thì báo lỗi
Nếu là SKU nhận và khai báo UID group - Nhận và mapping theo SỐ LOT + Mã cuộn
o
theo Packing list
 Nếu SKU là con normal: báo lỗi nếu có user nhận trùng số Lô và mã cuộn
 Nếu SKU là combo: do ko check realtime nên sẽ báo lỗi khi user submit (nếu
cải tiến check được realtime lúc khai báo thì càng tốt)
 Case nhận thiếu
 Nếu PO có cờ force cho nhận nhiều user cùng lúc, user không cần khai báo
SL thiếu, sau khi nhận hết hàng vật lý thì vẫn kết thúc nhận hàng như
bthường (không cần khai báo thiếu)
 Nếu người nhận cuối mà tổng số lượng thực nhận >= Qty của PO thì sẽ là
người complete PO
• Nếu SL thiếu và NCC không giao lại thì sẽ có 1 người dại diện vào
khai báo và complete PO (htại thì cho người nào khai báo cũng
được)
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 119