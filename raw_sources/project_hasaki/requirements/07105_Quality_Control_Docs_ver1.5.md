|     |     |     | 42  |     |     |
| --- | --- | --- | --- | --- | --- |
Warehouse Management System
Features name
I.  Phê duyệt
| Phiên bản  |     | Ngày duyệt  | Người đánh giá  | Người duyệt  |     |
| ---------- | --- | ----------- | --------------- | ------------ | --- |
| 1.0        |     |             |                 |              |     |
II.  Lịch sử thay đổi
| Phiên bản  | Ngày        | Người thực hiện  |           | Mô tả  |     |
| ---------- | ----------- | ---------------- | --------- | ------ | --- |
| 1.0        | 28-07-2025  | Phù Minh Tú      | Creation  |        |     |
| 1.1        | 07-08-2025  | Phù Minh Tú      | Update    |        |     |
Thiết lập tiêu chí: bổ sung thông tin hướng dẫn
Thiết lập tiêu chí cho SKU: bổ sung
-  Yêu cầu chụp hình
-  Hình chụp mẫu
-  Loại đánh giá theo điều kiện (phase 2)
Chi tiết kết quá đánh giá (Web)
-  Bổ sung thông tin kết quả đánh giá
Đánh giá trên App
-  Bổ sung hình chụp mẫu
-  Đánh giá theo điều kiện, nhập kết quả đánh giá
để trả ra kết quả đạt hay không đạt
1.2  17-09-2025  Phù Minh Tú  Bổ sung thiết lập và quy trình đánh giá vải nguyên vật liệu
1.3  27-09-2025  Phù Minh Tú  Bổ sung thêm bước thiết lập nội dung cho tiêu chí đánh
giá lỗi 4 điểm
1.3  01-10-2025  Phù Minh Tú  Update phần thiết lập nội dung cho tiêu chí đánh giá lỗi 4
điểm
1.4  23-02-2025  Phù Minh Tú  Update 1 số rules sau khi chốt yêu cầu từ vận hành và

2
BOM
Web
- Thiết lập tiêu chí: bổ sung thêm cột “QC xã vải”
- Bổ sung bước chụp hình tem pass/fail sau khi
hoàn thành đánh giá cho SKU
• Hiển thị thêm thông tin hình ảnh tem
trong kết quả đánh giá
- Bổ sung thông tin “SL cần đánh giá” trong chi tiết
kết quả đánh giá theo UID group
- Group UID: bổ sung thêm cột “Đánh giá Đạt” cho
trang quản lý UID group để chặn không cho IT
nếu UID group chưa được đánh giá
App
- Ở bước scan UID group khi thực hiện đánh giá,
bổ sung thêm cho user cập nhật số lượng cần
đánh giá
- Sau khi xác nhận “Hoàn thành” đánh giá cho
SKU, bổ sung thêm bước chụp hình tem QC
1.5 20-04-2025 Phù Minh Tú - Khi đánh giá SKU thường bị failed thì có thêm option cho
user chọn để tạo Adjustment trả hàng nhà cung cấp
- Blocked UID group của SKU của PO cùng LOT và chuyển
product status = Damaged
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

3
CONTENT
TỔNG QUAN ............................................................................................................................................... 4
THUẬT NGỮ & VIẾT TẮT ...................................................................................................................... 5
QUY TRÌNH (WORKFLOW) ................................................................................................................... 5
GIAO DIỆN (WIREFRAME) .................................................................................................................... 5
YÊU CẦU CHỨC NĂNG ............................................................................................................................. 6
Thiết lập tiêu chí ..................................................................................................................................................... 6
Tạo tiêu chí ................................................................................................................................................................. 7
Import tiêu chí............................................................................................................................................................ 8
Thiết lập tiêu chí cho SKU ....................................................................................................................................... 9
Tạo tiêu chí cho SKU ................................................................................................................................................. 10
17-09-2025: thiết lập đánh giá từng bước cho tiêu chí ........................................................................................... 15
27-09-2025: thiết lập nội dung đánh giá cho tiêu chí lỗi 4 điểm ............................................................................. 17
Duyệt/Từ chối .......................................................................................................................................................... 19
Kết quả đánh giá ................................................................................................................................................... 22
18-09-2025: Chi tiết kết quả đánh giá ...................................................................................................................... 23
VAS updated.......................................................................................................................................................... 27
Update 18-09-2025 .................................................................................................................................................. 30
Đánh giá chất lượng sản phẩm - Mobile ................................................................................................................ 31
Update 18-09-2025 – Đánh giá chất lượng vải ....................................................................................................... 34
Tạo mới đánh giá – Manual (bỏ) .............................................................................................................................. 39
Update 11-02-2026 ................................................................................................................................................ 42
Thêm cột khi thiết lập tiêu chí (Web) ...................................................................................................................... 42
Kết quả đánh giá (Web) ........................................................................................................................................... 43
UID group (Web) ...................................................................................................................................................... 43
Khai báo số lượng cần đánh giá cho UID group (App) ............................................................................................. 44
Chụp hình tem QC .................................................................................................................................................... 44
Một số lưu ý cho luồng đánh giá mới ...................................................................................................................... 45
Tạo mới đánh giá – Manual ..................................................................................................................................... 46
Update 20-04-2026 ................................................................................................................................................ 50
Đánh giá SKU phụ liệu (SKU thường) ....................................................................................................................... 50
Blocked UID group và chuyển Damaged .................................................................................................................. 51
Update 10-05-2026 ................................................................................................................................................ 52
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

4
Thiết lập tiêu chí 4 điểm khi thiết lập tiêu chí .......................................................................................................... 52
Thiết lập đánh giá từng bước khi thiết lập tiêu chí .................................................................................................. 52
TỔNG QUAN
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

|     |     | 5   |     |
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
-  Link: https://drive.hasaki.vn/d/d45615dafe0b441785ff/

Giao diện (Wireframe)
-
Link: https://www.figma.com/design/CLtzJtUv6sA4rxyaBPnbz5/34.-Quality-Control?node-
id=366-229&t=dvLSI74zHLKyyM0v-1

Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

  6

Yêu cầu chức năng
Thiết lập tiêu chí
-  Menu: Inbound / Quality control (kiểm soát chất lượng)
o   Tab Thiết lập tiêu chí (Setup criteria)
|   Giao diện  |     |     |
| ------------ | --- | --- |

Filter
| Tiếng Việt  | Tiếng Anh  | Description  |
| ----------- | ---------- | ------------ |
Mã, tên tiêu  Code, Criteria name  Hỗ trợ tìm kiếm theo mã và tên tiêu chí
| chí        |         | Tìm theo giá trị gần đúng, nhập từ 3 ký tự  |
| ---------- | ------- | ------------------------------------------- |
| Đang hoạt  | Active  |                                             |
động
| Từ ngày…đến  | From date…to date  | Hỗ trợ tìm theo ngày tạo                  |
| ------------ | ------------------ | ----------------------------------------- |
| ngày         |                    | Đến ngày phải lớn hơn hoặc bằng đến ngày  |
Mặc định không chọn ngày

Listing
| Tiếng Việt    | Tiếng Anh      | Description         |
| ------------- | -------------- | ------------------- |
| TT            | No             | Số thứ tự tăng dần  |
| Mã tiêu chí   | Criteria code  | Theo user nhập vào  |
| Tên tiêu chí  | Criteria name  |                     |
| Mô tả         | Description    |                     |
| Hướng dẫn     | instruct       |                     |
Đang hoạt động  Active  Mặc định khi tiêu chí mới được tạo thì sẽ ở trạng thái Active
Khi muốn Active/Inactive thiết lập cho SKU thì hiện thông báo
xác nhận

Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

7
- Do you want to DEACTIVATE criterion 1001?
- Do you want to ACTIVATE criterion 1001?
Người tạo Created by Format
- Người tạo: email Hasaki
- Thời gian tạo: YYYY-MM-DD HH:SS
Người cập nhật Updated by Format
- Người cập nhạt cuối cùng: email Hasaki
- Thời gian cập nhật cuối cùng: YYYY-MM-DD HH:SS
Thao tác Action
Chọn để cập nhật thông tin cho tiêu chí
- Không cho cập nhật mã tiêu chí
- Các thông tin còn lại được phép cập nhật
Tạo tiêu chí
- Tại màn hình quản lý tiêu chí, chọn “Tạo mới”
- Mã tiêu chí / Criteria code
Bắt buộc
o
Không được trùng, nếu trùng hiện thông báo
o
 VN: Mã tiêu chí đã tồn tại.
 EN: The criteria code already exists.
- Tên tiêu chí / Criteria name
Bắt buộc
o
Không được trùng, nếu trùng hiện thông báo
o
 VN: Tên tiêu chí đã tồn tại.
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

8
 EN: The criteria name already exists.
- Mô tả / Description
Không bắt buộc
o
- Hướng dẫn / instruct
Không bắt buộc
o
- Chọn “Đóng” để tắt popup
- Chọn “Lưu và đóng” để lưu tiêu chí và tắt popup
- Chọn “Lưu và tiếp tục” để lưu tiêu chí và clear thông tin để tiếp tục tạo
Import tiêu chí
- Template import
- Validate
Nội dung Tiếng Việt Tiếng Anh
Mã tiêu chí đã tồn tại Mã tiêu chí đã tồn tại trên hệ The criteria code already exists in
trên hệ thống thống the systems.
Mã tiêu chí đã tồn tại Mã tiêu chí đã tồn tại trong file The criteria code already exists in
trong file import import the template import.
Tên tiêu chí đã tồn tại Tên tiêu chí đã tồn tại trên hệ The criteria name already exists
trên hệ thống thống in the systems.
Tên tiêu chí đã tồn tại Tên tiêu chí đã tồn tại trong file The criteria name already exists
trong file import import in the template import.
 Luồng import sử dụng lại page import dùng chung cho các tính năng đã làm trước đó
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

|     |     | 9   |
| --- | --- | --- |

Thiết lập tiêu chí cho SKU
-  Menu: Inbound / Quality control (kiểm soát chất lượng)
  Tab Thiết lập SKU (Setup criteria by SKU)
o

| Giao diện  |     |     |
| ---------- | --- | --- |

Filter
| Tiếng Việt  | Tiếng Anh  | Description  |
| ----------- | ---------- | ------------ |
SKU, Barcode, Tên  SKU, Barcode, Product  Hỗ trợ tìm theo SKU, Barcode, tên của SKU
| sản phẩm        | name      |                           |
| --------------- | --------- | ------------------------- |
| Danh mục        | Category  | Hỗ trợ tìm theo category  |
| Thương hiệu     | Brand     | Hỗ trợ tìm theo brand     |
| Đang hoạt động  | Active    | Mặc định không chọn       |
Giá trị
-  Đang hoạt động / Active
-  Ngưng hoạt động / Inactive
| Trạng thái          | Status           |                      |
| ------------------- | ---------------- | -------------------- |
| Thời điểm đánh giá  | Assessment time  | Mặc định không chọn  |
Giá trị
-  Khi nhận PO / Receiving PO
-  Sau khi nhận PO / After receive of PO
| Tần suất đánh giá  | Assessment frequency  | Mặc định không chọn  |
| ------------------ | --------------------- | -------------------- |
Giá trị
-  Tất cả PO / All PO
-  Ngẫu nhiên / Random
Từ ngày…đến ngày  From date…to date  Hỗ trợ tìm theo ngày tạo
Đến ngày phải lớn hơn hoặc bằng đến ngày
Mặc định không chọn ngày

Listing
| Tiếng Việt      | Tiếng Anh        | Description         |
| --------------- | ---------------- | ------------------- |
| TT              | No               | Số thứ tự tăng dần  |
| Sản phẩm        | Product          | SKU – Tên sản phẩm  |
| Danh mục        | Category         |                     |
| Thương hiệu     | Brand            |                     |
| Thời điểm đánh  | Assessment time  |                     |
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

10
giá
Tần suất đánh giá Assessment
frequency
Số lượng tiêu chí Number of criteria
Đang hoạt động Active Mặc định khi SKU mới được tạo thì sẽ ở trạng thái Active
Khi muốn Active/Inactive thiết lập cho SKU thì hiện thông báo
xác nhận
- Do you want to DEACTIVATE setup by SKU 422280022?
- Do you want to ACTIVATE setup by SKU 422280022?
Lưu ý: tại 1 thời điểm 1 SKU không thể cùng active 2 thiết lập,
phải inactive cái cũ trước khi muốn active cái mới
Người tạo Created by Format
- Người tạo: email Hasaki
- Thời gian tạo: YYYY-MM-DD HH:SS
Người cập nhật Updated by Format
- Người cập nhạt cuối cùng: email Hasaki
- Thời gian cập nhật cuối cùng: YYYY-MM-DD HH:SS
Trạng thái Status
Thao tác Action
Chọn để cập nhật thông tin cho tiêu chí  vào trang cập
nhật tiêu chí cho sản phẩm
- Button này chỉ show lên cho status Mới (New)
Chọn để xem chi tiết thiết lập tiêu chí cho sản phẩm hoặc
để Duyệt/Từ chối
Chọn để xoá thiết lập tiêu chí cho SKU
- Button này chỉ show lên cho status Mới (New)
Tạo tiêu chí cho SKU
- Tại màn hình quản lý tiêu chí, chọn “Tạo mới”
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

11
Tiếng Việt Tiếng Anh Description
Sản phẩm Product Bắt buộc
o
Hỗ trợ tìm sản phẩm bằng SKU, barcode, tên sản
o
phẩm để thiết lập
Nếu chưa chọn thì hiện thông báo (dưới trường
o
tương ứng)
 VN: Thông tin này là bắt buộc.
 EN: This information is required.
Nếu SKU đã được thiết lập nhưng trạng thái đang
o
Active thì hiện thông báo
 VN: SKU 422280022 đã tồn tại và đang hoạt
động trên hệ thống.
 EN: SKU 422280022 already exists and is active
in the system.
Thời điểm đánh giá Assessment time Bắt buộc
o
Nếu chưa chọn thì hiện thông báo (dưới trường
o
tương ứng)
 VN: Thông tin này là bắt buộc.
 EN: This information is required.
Giá trị
o
 Khi nhận PO / Receiving PO (chưa hỗ trợ ở
phase này)
 Sau khi nhận PO / After receive of PO
Tần suất đánh giá Assessment frequency Bắt buộc
o
Nếu chưa chọn thì hiện thông báo (dưới trường
o
tương ứng)
 VN: Thông tin này là bắt buộc.
 EN: This information is required.
Giá trị
o
 Tất cả PO / All PO
• Tự động sinh VAS đánh giá sản phẩm sau
khi kết thúc phiên nhận
 Ngẫu nhiên / Random
• User tự tạo phiên đánh giá sản phẩm khi có
nhu cầu (chưa hỗ trợ ở phase này)
Ghi chú Note Không bắt buộc
Đóng Close Chọn “Đóng” để tắt popup
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

12
Tiếp tục Continue Chọn “Tiếp tục” để qua màn hình thiết lập tiêu chí cho SKU
Nếu SKU đã được thiết lập tiêu chí và đang active thì báo
lỗi
VN: SKU đã được thiết lập và đang hoạt động.
EN: SKU has been set up and is currently active
Màn hình khi chưa thêm tiêu chí cho SKU
Các lựa chọn tương ứng cho “Loại đánh giá” và “Phân loại”
Màn hình sau khi đã thêm tiêu chí cho SKU
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

|     |     | 13  |
| --- | --- | --- |

| Tiếng Việt          | Tiếng Anh             | Description  |
| ------------------- | --------------------- | ------------ |
| Sản phẩm            | Product               |              |
| Danh mục            | Category              |              |
| Thương hiệu         | Brand                 |              |
| Thời điểm đánh giá  | Assessment time       |              |
| Tần suất đánh giá   | Assessment frequency  |              |
| Ghi chú             | Note                  |              |
| Tiêu chí đánh giá   | Assessment criteria   | Bắt buộc     |
Load danh sách tất cả tiêu chí được thiết lập trên hệ thống
để user chọn
Hỗ trợ tìm theo mã hoặc tên tiêu chí, khi nhập từ 3 ký tự
| Yêu cầu chụp hình  | Required Image  | Bắt buộc chọn  |
| ------------------ | --------------- | -------------- |
Giá trị: Yes/No
| Hình chụp mẫu  | Sample image  | Không bắt buộc  |
| -------------- | ------------- | --------------- |
Hỗ trợ upload tối đa 3 hình
| Loại đánh giá  | Assessment type  | - Đạt/  Không đạt: mặc định  |
| -------------- | ---------------- | ---------------------------- |
  Mặc định phân loại = Bình thường và không cho
o
chỉnh sửa
- Theo điều kiện: gồm các lựa chọn sau
•
=
  Giá trị: Bắt buộc, nhập giá trị là số > 0
o
  Đơn vị tính: bắt buộc, text
o
o   Sai số cho phép: không bắt buộc, nhập giá trị
là số >0

•  >
•
>=
•  <
•  <=
  Giá trị: Bắt buộc, nhập giá trị là số > 0
o
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

14
Đơn vị tính: bắt buộc, text
o
• Trong khoảng (between)
Giá trị từ…đến: Bắt buộc, nhập giá trị là số > 0
o
Đơn vị tính: bắt buộc, text
o
- Công thức: dùng để thiết lập công thức, trả kết
quả và so sánh với điều kiện được thiết lập (sẽ bổ
sung rules sau khi trao đổi với Dev)
Lưu ý:
Hiện tại 1 tiêu chí chỉ hỗ trợ 1 điều kiện duy nhất, nên khi
đã thêm 1 điều kiện thì nút Thêm (+) sẽ disable đi, chỉ khi
xoá điều kiện đã thêm thì nút Thêm (+) mới hiện lên
Phân loại Type Gồm 3 lựa chọn
- Bình thường / Normal
Sử dụng theo quy trình đánh giá bình thường
- Lỗi 4 điểm / 4 points error
Được thiết lập theo quy trình đặc thù
- Theo từng bước / Step by step
Được thiết lập theo từng bước
Mô tả Description Không bắt buộc
Thêm Add Sau khi chọn xong thông tin thì chọn “Thêm” để add tiêu
chí vào danh sách tiêu chí được thiết lập cho SKU
Nếu tiêu chí đã tồn tại trong danh sách, hiện thông báo
- VN: Tiêu chí đã tồn tại trong danh sách.
- EN: Criteria already exists in the list.
 Tiếp tục thực hiện cho tới khi hoàn thành
Đóng Close Chọn “Đóng” để tắt popup thêm tiêu chí cho SKU
Lưu Save Chọn “Lưu” để Lưu lại thông tin để tiếp tục cho những lần
sau
Yêu cầu duyệt Request approve Chọn “Hoàn thành” để xác nhận chuyển thiết lập cho SKU
qua trạng thái “Chờ duyệt”
Update 05-08-2025
- Nếu trạng thái thiết lập của SKU đang là Open hoặc Waiting for Approval mà tiêu chí trong SKU bị
inactive thì tiêu chí đó sẽ xoá khỏi danh sách tiêu chí cho SKU
- Nếu trạng thái thiết lập của SKU đang là Approved mà tiêu chí trong SKU bị inactive thì tiêu chí
đó sẽ không hiển thị cho SKU
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

|     |     | 15  |
| --- | --- | --- |

17-09-2025: thiết lập đánh giá từng bước cho tiêu chí
-  Tại màn hình thiết lập tiêu chí cho SKU
  Chọn edit   cho tiêu chí với type = “Theo từng bước”, mở modal để thiết lập các bước
o
cần đánh giá cho tiêu chí
  Lưu ý: khi add tiêu chí cho SKU mà có phân loại = “Theo từng bước” thì tự động
chuyển qua màn hình thiết lập các bước để user có thể thao tác ngay

| Tiếng Việt  | Tiếng Anh  | Description  |
| ----------- | ---------- | ------------ |
Tiêu chí  Criteria  Theo thông tin tiêu chí được chọn để thiết lập
| Bước  | Step  | Số thứ tự từ 1 đến 10  |
| ----- | ----- | ---------------------- |
Số nào đã được chọn thì disable không cho chọn lại
| Nội dung  | Content  | Tên bước cần thực hiện  |
| --------- | -------- | ----------------------- |
Yêu cầu chụp hình  Required image  Bước thực hiện có yêu cầu chụp hình trên app hay không
| Hình ảnh mẫu      | Reference image  | Hình ảnh mẫu  |
| ----------------- | ---------------- | ------------- |
| Ghi nhận kết quả  | Record results   | Value         |
-  Không / No
-  Nhập giá trị / Fill value
Nhập giá trị cho bước thực hiện
-  Đạt / Không đạt – Passed / Failed
Chọn kết quả Đạt hay Không đạt
Từ khoá  Keywords  Chỉ show lên cho user nhập nếu Ghi nhận kết quả chọn khác
giá trị không
Tự động bật in hoa và không cho nhập khoảng trắng
Cho phép nhập các ký tự đặc biệt: gạch dưới “_”, gạch ngang
“-“, dấu chấm “.”
| Hướng dẫn  | Intruction  | Cho nhập text        |
| ---------- | ----------- | -------------------- |
| Công thức  | Formula     | Thiết lập công thức  |
Kiểm tra định dạng  Check format  Sử dụng để check cấu trúc của công thức có hợp lệ và đúng
format hay chưa
-  Hợp lệ: Công thức hợp lệ (chữ xanh lá)
-  Không hợp lệ: Công thức không hợp lệ (chữ đỏ)
| Đóng  | Close  | Tắt popup thiết lập  |
| ----- | ------ | -------------------- |
Lưu  Save  Nút Lưu chỉ hiện lên cho chọn khi có 1 ít nhất 1 bước được
thiết lập, và nếu có nhập công thức thì công thức phải hợp lệ
Nếu user cập nhật công thức nhưng chưa chọn “Kiểm tra
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

16
định đạng” thì khi nhấn Lưu sẽ vaidate thêm 1 lần nữa.
Màn hình sau khi cập nhật đầy đủ các bước và công thức cho 1 tiêu chí
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

17
27-09-2025: thiết lập nội dung đánh giá cho tiêu chí lỗi 4 điểm
- Tại màn hình thiết lập tiêu chí cho SKU
Chọn edit cho tiêu chí với type = “Lỗi 4 điểm”, mở modal để thiết lập nội dung cần
o
đánh giá cho tiêu chí
 Lưu ý: khi thiết lập nội dung tiêu chí cho SKU mà có phân loại = “Lỗi 4 điểm” thì
tự động chuyển qua màn hình thiết lập các bước để user có thể thao tác ngay
Tiếng Việt Tiếng Anh Description
Tiêu chí Criteria Theo thông tin tiêu chí được chọn để thiết lập
Nội dung Content Tên bước cần thực hiện
Yêu cầu chụp hình Required image Bước thực hiện có yêu cầu chụp hình trên app hay không
Ghi nhận kết quả Record results Value
- Không / No
- Nhập giá trị / Fill value
Nhập giá trị cho bước thực hiện
- Đạt / Không đạt – Passed / Failed
Chọn kết quả Đạt hay Không đạt
Từ khoá Keywords Chỉ show lên cho user nhập nếu Ghi nhận kết quả chọn khác
giá trị không
Tự động bật in hoa và không cho nhập khoảng trắng
Cho phép nhập các ký tự đặc biệt: gạch dưới “_”, gạch ngang
“-“, dấu chấm “.”
Hướng dẫn Intruction Cho nhập text
Công thức Formula Thiết lập công thức
Kiểm tra định dạng Check format Sử dụng để check cấu trúc của công thức có hợp lệ và đúng
format hay chưa
- Hợp lệ: Công thức hợp lệ (chữ xanh lá)
- Không hợp lệ: Công thức không hợp lệ (chữ đỏ)
Đóng Close Tắt popup thiết lập
Lưu Save Nút Lưu chỉ hiện lên cho chọn khi có 1 ít nhất 1 bước được
thiết lập, và nếu có nhập công thức thì công thức phải hợp lệ
Nếu user cập nhật công thức nhưng chưa chọn “Kiểm tra
định đạng” thì khi nhấn Lưu sẽ vaidate thêm 1 lần nữa.
Màn hình sau khi cập nhật nội dung và công thức cho 1 tiêu chí
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

18
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

19
Duyệt/Từ chối
- Ở màn hình quản lý danh sách tiêu chí thiết lập cho SKU, với những case có trạng thái “Chờ
duyệt”
- Có 2 cách để quản lý có quyền có thể duyệt thông tin
Chọn nhiều dòng “Chờ duyệt” bằng các tích chọn và chọn Duyệt/Từ chối, hiện thông báo
o
 Chọn “Duyệt”
• EN: Do you want to confirm APPROVE setting criteria for SKUs of all
selected lines?
• Chọn “Yes” để chuyển trạng thái thành “Đã duyệt” (Approved)
 Chọn “Từ chối”
• EN: Do you want to confirm REJECT setting criteria for SKUs of all
selected lines?
• Chọn “Yes” để chuyển trạng thái thành “Từ chối” (Rejected)
Hoặc chọn vào từng dòng thiết lập cần Duyệt/Từ chối
o
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

20
 Chọn “Duyệt”
• EN: Do you want to confirm APPROVE criteria setup for SKU 297500046?
• Chọn “Yes” để chuyển trạng thái thành “Đã duyệt” (Approved)
 Chọn “Từ chối”
• EN: Do you want to confirm REJECT criteria setup for SKU 297500046?
• Chọn “Yes” để chuyển trạng thái thành “Từ chối” (Rejected)
 Chọn “Mở lại” (Reopen)
• EN: Do you want to confirm RE-OPEN criteria setup for SKU 297500046?
• Chọn Yes để revert trạng thái thành “Open” để user có thể cập nhật lại
thiết lập cho SKU
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

21
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

|     |     | 22  |
| --- | --- | --- |

Kết quả đánh giá
-  Menu: Inbound / Quality control (kiểm soát chất lượng)
  Tab Kết quả đánh giá (Assessment Result)
o

Filter
| Tiếng Việt  | Tiếng Anh  | Description  |
| ----------- | ---------- | ------------ |
SKU, barcode  SKU, barcode  Hỗ trợ tìm theo SKU, barcode của sản phẩm
Tìm theo mã chính xác nhập vào
| VAS  | VAS  | Hỗ trợ tìm theo mã VAS  |
| ---- | ---- | ----------------------- |
Tìm theo mã chính xác nhập vào
| Kho  | Warehouse  | Tìm theo kho cần đánh giá  |
| ---- | ---------- | -------------------------- |
Hỗ trợ tìm theo tên kho khi nhập từ 3 ký tự
| Mã PO  | PO code  | Hỗ trợ tìm theo mã PO nguồn (mã PO inside)  |
| ------ | -------- | ------------------------------------------- |
Tìm theo mã chính xác nhập vào
Trạng thái  Status  Tìm theo trạng thái của kết quả đánh giá
Value
-  Mới (New): khi yêu cầu đánh giá mới được sinh ra
-  Đang đánh giá (Processing): khi yêu cầu đang được đánh
giá nhưng chưa hoàn thành
-  Hoàn thành (Completed) khi yêu cầu đánh giá được xác
nhận hoàn thành
| Phân loại  | Type  | Value  |
| ---------- | ----- | ------ |
-  Tự động (Automation): yêu cầu đánh giá tự động sinh ra
theo thiết lập của SKU
-  Thủ công (Manual): yêu cầu đánh giá do user tạo thủ
công
-  Bình thường / Normal: luồng đánh giá bình thường
-  Nhóm UID / Group UID: luồng đánh giá cho nhóm UID
cho các sản phẩm Vải
-  Xã vải / Fabric Relaxing: luồng đánh giá cho khâu xã vải
trước khi chuyển qua may thành phẩm
| Người đánh giá  | Assessment by  | Người thực hiện đánh giá  |
| --------------- | -------------- | ------------------------- |
Format
-  Email của Hasaki
-  Thời gian hoàn thành đánh giá
| Có tiêu chí không  | Have criteria fail  | Value  |
| ------------------ | ------------------- | ------ |
đạt  -  Có (Yes): có ít nhất 1 tiêu cho không đạt trong phần
đánh giá
-  Không (No): không có tiêu chí không đạt
| Ngày đánh giá  | Assessment at  | Từ ngày đến ngày  |
| -------------- | -------------- | ----------------- |
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

|     |     | 23  |
| --- | --- | --- |

Từ ngày phải nhỏ hơn hoặc bằng đến ngày

Listing
| Tiếng Việt  | Tiếng Anh  | Description  |
| ----------- | ---------- | ------------ |
VAS  VAS  Chọn vào VAS để hyperlink qua trang detail của VAS tương ứng
| Kho       | Warehouse  |                             |
| --------- | ---------- | --------------------------- |
| Sản phẩm  | Product    | Format: SKU – tên sản phẩm  |
Tiêu chí đạt  Criteria passed  Tổng số tiêu chí đạt / tổng tiêu chí cần đánh giá cho SKU
Tiêu chí không đạt  Criteria failed  Tổng số tiêu chí không đạt / tổng tiêu chí cần đánh giá cho SKU
| Phân loại  | Type  |     |
| ---------- | ----- | --- |
Mã PO nguồn  PO source number  Chọn vào mã PO hyperlink qua trang detail của PO trên Inside
| Nhà cung cấp    | Vendor         | Nhà cung cấp của PO cần đánh giá    |
| --------------- | -------------- | ----------------------------------- |
| Danh mục        | Category       | Category của sản phẩm cần đánh giá  |
| Thương hiệu     | Brand          | Brand của sản phẩm cần đánh giá     |
| Ghi chú         | Note           |                                     |
| Người đánh giá  | Assessment by  | Email hasaki                        |
Thời gian hoàn thành đánh giá
| Trạng thái  | Status  | Thao tác  |
| ----------- | ------- | --------- |
Chọn   để xem chi tiết kết quả đánh giá

Dựng 1 service để ghi nhận kết quả đánh giá để sau này nhận thông tin từ nhiều nguồn đánh giá khác
nhau => WMS ghi nhận kết quả cuối cùng

VAS_ID + Group UID sẽ gắn với từng Serive
Mỗi service gồm các thông tin gồm:
•  Group UID
•  Mã tiêu chí
•  Kết quả
=> mỗi service được hiểu như 1 kết quả đánh giá của 1 group UID
Dựa vào kết quả đánh giá này sẽ tổng hợp lại và ghi nhận kết quả cho cả group UID và VAS
18-09-2025: Chi tiết kết quả đánh giá
Chi tiết kết quả đánh giá chất lượng sản phẩm
  Type = Bình thường
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

24
Type = Nhóm UID
- Chọn để xem chi tiết kết quả đánh giá theo từng nhóm UID
Với tiêu chí lỗi 4 điểm
- Do loại tiêu chí này hơi đặc thù nên cho lưu trữ và hiển thị riêng
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

25
Mỗi 1 loại lỗi là 1 group, có thể thu gọn hoặc mở rộng
o
 Tổng điểm lỗi = tổng số điểm của 4 loại chưa nhân hệ số
 Tổng điểm lỗi đã nhân hệ số
 Trong mỗi loại lỗi sẽ hiện thông tin chi tiết của từng lỗi, gồm
• Lỗi 1:
Loại lỗi
o
Hình ảnh lỗi
o
Ghi chú
o
 Tương tự cho các loại lỗi 2 điểm, 3 điểm và 4 điểm
Với các tiêu chí được thiết lập theo tứng bước thì 1 bước là hiển thị 1 bước là 1 nhóm thông tin theo
thiết lập, gồm:
- Hinh ảnh
- Kết quả ghi nhận
- Ghi chú
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

26
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

27
VAS updated
- Bổ sung thông tin Loại VAS (VAS type)
Thêm mới
o
Bổ sung filter
o
 Giá trị
• IMEI
• RFID
• Quality Control
• Other
 Hỗ trợ chọn nhiều
Data table
o
 Bổ sung cột VAS type
 Nếu VAS vừa có Quality control, vừa có RFID hoặc IMEI thì hiện cả 2 thông tin,
cách nhau bởi dấu phẩy
- Trạng thái VAS
Bổ sung thêm trạng thái
o
Giá trị
o
 Mới / Open: VAS mới được tạo
 Đang xử lý / In-Progress: VAS đang được đánh giá hoặc đang thực hiện dán ID
 Hoàn thành / Completed
 Đã huỷ / Canceled
 Chờ duyệt / Waiting for approval: VAS sau khi đánh giá chất lượng và có tiêu chí
không đạt thì chuyển trạng thái này
 Chờ dán ID / Wating for paste ID: VAS chờ dán ID cho phiên nhận có SKU
required IMEI, RFID
 Chờ đánh giá / Waiting quality control: VAS chờ đánh giá chất lượng sản phẩm
 Chờ NCC đến lấy / Waiting vendor to pick: Khi VAS được chọn
 Đã trả NCC / Returned to vendor:
Quy trình thay đổi trạng thái của VAS
o
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

28
- Với VAS có trạng thái Chờ duyệt / Waiting for approval
Chọn mã VAS vào xem chi tiết để xác nhận kết quả đánh giá
o
Chọn Mở lại (Re-Open), hiện thông báo
o
 EN: Do you want to confirm RECEIVE for the quality control of VAS
1003241119000039?
 Chọn “Xác nhận” để chuyển kết quả đánh giá về lại Mới (Open) để tiến hành
đánh giá lại nếu cần
Chọn Nhận hàng (Receive), hiện thông báo
o
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

29
 Chọn Xác nhận nhận hàng để xác nhận tất cả tiêu chí Đạt, được hiểu như đánh
giá chất lượng pass (Lưu ý: có thể trong kết quả đánh giá vẫn có tiêu chí không
đạt nhưng vẫn có thể xác nhận nhận hàng)  chuyển qua thực hiện bước tiếp
theo
• Nếu SKU có required IMEI hoặc RFID thì chuyển qua trạng thái tương
ứng Chờ dán ID / Wating for paste ID
• Nếu SKU không required thì chuyển Completed
Chọn Trả nhà cung cấp (Return to vendor), hiện thông báo
o
 Nhập số lượng cần trả nhà cung cấp
• Ở phase này mặc định sẽ trả hết số lượng đã nhận trong ASN, nên số
lượng sẽ bằng số lượng đã nhận và disable
 Chọn Xác nhận
• Ghi nhận số lượng sẽ khai báo VAS và số lượng trả nhà cung cấp
• Chuyển trạng thái của VAS thành “Chờ NCC đến lấy”
Sau khi NCC đến lấy hàng thì user sẽ vào để cập nhật lại trạng
o
thái của VAS từ “Chờ NCC đến lấy” thành “Đã trả NCC”
 Tạo Outbound type Return vendor với thông tin tương
ứng
 Tạo Adjustment type Vendor Return để trả nhà cung cấp
để out hàng ra khỏi kho
• Hiện tại Dev xác nhận chưa thể tạo được
Adjustment cho case này
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

30
Update 18-09-2025
- Update Group UID cho type Quality control với các SKU vải
1 SKU nhận trong ASN theo group UID sẽ lấy ra 10% để thực hiện đánh giá
VD: SKUA nhận trong ASN là 25 group UID thì 10% là 2,5 làm tròn lên thành 3, tức sẽ có 3
o
dòng VAS cần đánh giá chất lượng cho SKUA
- Trong VAS Quality control bổ sung thêm Group UID và kết quả đánh giá theo group UID
Chỉ cần có 1 kết qua Failed thì ghi nhận là Failed
o
VAS sinh ra khi chưa thực hiện đánh giá
VAS đã scan group UID để đánh giá
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS….

|     |     | 42  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Đánh giá chất lượng sản phẩm - Mobile
| -              | User login vào app với tài khoản được cung cấp  |      |             |             |                                         |              |
| -------------- | ----------------------------------------------- | ---- | ----------- | ----------- | --------------------------------------- | ------------ |
| -              | App bổ sung thêm tính năng “Quality Control”    |      |             |             |                                         |              |
| Step           | Action                                          |  UI  | Field (VN)  | Field (EN)  |                                         | Description  |
| Vào tính năng  |                                                 |      |             |             | Menu: Pruchase Order / Quality Control  |              |
1
“Quality Control”  - Chọn kho  show các VAS có type Quality control có
| - Chọn kho  |     |     |     |     | trạng thái Open hoặc In-Progress  |     |
| ----------- | --- | --- | --- | --- | --------------------------------- | --- |
- Hỗ trợ tìm kiếm theo mã PO và VAS

2  Show sản phẩm cần      Chọn vào VAS cần đánh giá, thông tin hiển thị
| đánh giá  |     |     |     |     | -  Shop  |     |
| --------- | --- | --- | --- | --- | -------- | --- |
-  VAS
-  Tổng SKU
-  Mã PO
-  Tổng sản phẩm
-  Tìm kiếm sản phẩm theo SKU, Barcode hoặc
tên sản phẩm (tìm gần đúng)
-  Danh sách sản phẩm
•  Tên sản phẩm
|     |     |     |     |     | •  SKU – Barcode  |     |
| --- | --- | --- | --- | --- | ----------------- | --- |
•  Số lượng sản phẩm
•  Màu xám nhạt: sản phẩm chưa được đánh
giá
•  Màu xanh dương nhạt: sản phẩm đang
đánh giá chưa hoàn thành
•  Màu xanh lá nhạt: sản phẩm đã đánh giá

32
3 Đánh giá sản phẩm Chọn sản phẩm cần đánh giá, thông tin gồm
- Sản phẩm: SKU – Tên sản phẩm
- PO
- Số lượng
- Nhà cung cấp: lấy theo thông tin của PO
- Ghi chú: mặc định trống và cho user edit
- Tiêu chí đạt
- Tiêu chí không đạt
Danh sách tiêu chí cần đánh giá
- Lấy theo danh sách tiêu chí được thiết lập cho
SKU
- Thông tin của từng tiêu chí
• Thứ tự tiêu chí
• Tên tiêu chí
• Mô tả tiêu chí
• Mô tả điều kiện của tiêu chí theo SKU
• Hình chụp mẫu
• Đạt/Không đạt
• Nhập kết quả đánh giá: dành cho tiêu chí
thiết lập theo điều kiện, sau khi nhập giá
trị >0 sẽ nhấn Enter hoặc dấu tích xanh để
hệ thống kiểm tra và so sánh kết quả nhập
vào với điều kiện config để xác định là tiêu
chí đó Đạt hay Không đạt
Lưu ý: user có thể edit lại kết quả
o
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 32

33
đánh giá theo điều kiện và xác
nhận lại
• Hình ảnh: dựa theo config để yêu cầu chụp
hình cho sản phẩm
Những tiêu chí đánh Fail thì yêu cầu
o
chụp hình và nhập ghi chú
Hỗ trợ chụp tối đa 5 hình cho 1 tiêu chí
o
(nếu có yêu cầu)
Đánh giá và cập nhật thông tin cho tất cả các tiêu chí
 chọn Hoàn thành để xác nhận đánh gia xong
4 Đánh giá tất cả các Nếu trong 1 VAS có nhiều hơn 1 sản phẩm cần đánh
sản phẩm trong VAS giá, thì cần đánh giá tất cả các sản phẩm để hoàn
thành đánh giá cho VAS
 Sau khi đánh giá xong tất cả sản phẩm trong
VAS  chọn Hoàn thành đánh giá
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 33

34
Update 18-09-2025 – Đánh giá chất lượng vải
- Quy trình thực hiện đánh giá vải nguyên vật liệu trên App
Step Action UI Description
1 Vào tính năng “Quality Menu: Pruchase Order / Quality Control
Control” - Chọn kho  show các VAS có type Quality control có trạng thái Open hoặc In-
- Chọn kho Progress
- Hỗ trợ tìm kiếm theo mã PO và VAS
2 Show sản phẩm cần đánh Chọn vào VAS cần đánh giá, thông tin hiển thị
giá - Shop
- VAS
- Tổng SKU
- Mã PO
- Tổng sản phẩm
- Tìm kiếm sản phẩm theo SKU, Barcode hoặc tên sản phẩm (tìm gần
đúng)
- Danh sách sản phẩm
• Tên sản phẩm
• SKU – Barcode
• Số lô
• Hạn sử dụng
• Phân biệt màu sắc
Màu xám nhạt: sản phẩm chưa được đánh giá
o
Màu xanh dương nhạt: sản phẩm đang đánh giá chưa hoàn
o
thành
Màu xanh lá nhạt: sản phẩm đã đánh giá và Đạt
o
Màu cam nhạt: sản phẩm đã đánh giá và Không Đạt
o
Lưu ý: do rules đánh giá 10% số lượng cây vải của từng lô, nên nếu 1 lô cần
đánh giá 3 cây vải tương ứng với 3 group UID thì sẽ hiện thành 3 dòng tương
ứng
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 34

35
3 Chọn thông tin sản phẩm Chọn vào sản phẩm cần đánh giá
cần đánh giá - Yêu cầu scan nhóm UID tương ứng với cây vải cần giá
 Nếu nhóm UID không tồn tại hoặc không thuộc PO và số lô
được yêu cầu đánh giá hiện thông báo
- Hỗ trợ suggest các nhóm UID đã nhận cho sản phẩm theo lô để user có
thể chọn nhanh
Sau khi scan hoặc chọn nhóm UID hợp lệ, chọn “Xác nhận” để qua bước tiếp
theo”
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 35

36
4 Chọn tiêu chí cần đánh giá Sau khi chọn nhóm UID hợp lệ, hiện danh sách tiêu chí cần đánh giá cho sản
phẩm đa được thiết lập
Ở phase này sẽ có tổng cộng 3 tiêu chí đánh giá, các thông tin cần hiện cho tiêu
chí trên App gồm:
- Tên tiêu chí
kèm hướng dẫn: mở modal để xem hướng dẫn đã được thiết
o
lập
- Mô tả của tiêu chí
- Điều kiện (nếu có)
1. Kiểm tra lỗi 4 điểm
Các thông tin hiển thị
- Lỗi 1 điểm(lỗi 0 – 3”)
- Lỗi 2 điểm (lỗi 3” – 6”)
- Lỗi 3 điểm (lỗi 6” – 9”)
- Lỗi 4 điêm (lỗi hơn 9”)
- Khi kiểm tra và phát hiện lỗi tương ứng, user sẽ chọn vào dấu + để thêm
thông tin lỗi
Chọn lỗi: bắt buộc
o
 1.Slub : sợi thô cục
 2.Foreign yarn : sợi tạp,sợi màu
 3.Thin yarn, rough yarn: sợi rách,sợi thô
 4.Yarn knot : gút sợi
 5.Missing yarn : mất sợi
 6.Break yarn : đứt sợi
 7.Needle line : lỗi kim
 8.Dark line : sọc đậm màu
 9.Scratch : dập tuyết, trầy xước
 10.Staining : loang màu
 11.Fade of color : bạc màu
 12.Dyeing block : vết dơ trong nhuộm
 13.Color spot : chấm màu
 14.Dirty : dơ
 15.Hole : lỗi rách
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 36

37
 16.Printing erro : lỗi in
 17.Fold,crease : nếp nhăn
 18.Dead fold : nếp gấp chết
 19.Other : lỗi khác
Nhập ghi chú
o
Chụp hình ảnh lỗi: bắt buộc, cho chụp max 3 hình
o
Chọn “Xác nhận” để ghi nhận lỗi tương ứng
o
- Sau khi ghi nhận lỗi cho từng loại thì sẽ tính
Số lỗi của từng loại
o
Tổng điểm lỗi (chưa nhân hệ số)
o
Tổng điểm lỗi đã nhân hệ số
o
- Chọn vào icon để xem thông tin lỗi đã cập nhật trước đó
- Sau khi ghi nhận tất cả các lỗi xong thì chọn “Hoàn thành” để xác nhận
đánh giá xong cho tiêu chí
 Lấy kết quả điểm lỗi đã nhân hệ số so sánh với điều kiện được thiết lập
của tiêu chí để xác định tiêu chí có Đạt hay Không đạt và ghi nhận vào
kết quả bên ngoài
Kết quả = Tổng điểm lỗi đã nhân hệ số
o
Kết quả Đạt hay không đạt dựa vào điều kiện để so sánh
o
2. Kiểm tra độ co rút
Do tiêu chí được thiết lập đánh giá từng bước nên sau khi chọn tiêu chí thì sẽ
thực hiện theo từng bước
- Dựa vào thông tin thiết lập cho từng bước để hiện thông tin tương ứng
trên App cho user cập nhật
Thứ tự bước - Tên bước
o
• Kèm hình ảnh mẫu
Hướng dẫn
o
Yêu cầu chụp hình: theo thiết lập
o
Ghi nhận kết quả: theo thiết lập
o
• Đạt / Không đạt
• Nhập giá trị
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 37

38
Ghi chú
o
Sau khi cập nhật xong thì chọn “Tiếp theo” để qua bước tiếp
o
theo
- Sau khi cập nhật xong bước cuối cùng của thiết lập, chọn Hoàn thành để
xác nhận đánh giá xong cho tiêu chí
 Dựa vào công thức được thiết lập cho tiêu chí (nếu có) để tính ra kết quả
của tiêu chí và so sánh với điều kiện để biết tiêu chí có Đạt hay Không
đạt
3. Kiểm tra độ đồng màu
Thực hiện tương tự như Kiểm tra độ co rút
5 Ghi nhận kết quả cuối cùng Sau khi đánh giá xong các tiêu chí được thiết lập cho sản phẩm, chọn “Hoàn
cho nhóm UID thành” để xác nhận đánh giá xong
- Nếu có ít nhất 1 tiêu chí không đạt thì xem như kết quả của sản phẩm
được đánh giá theo nhóm UID là Không đạt
 Tiếp tục thực hiện cho các nhóm UID còn lại cho tới khi hoàn thành
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 38

39
Tạo mới đánh giá – Manual (bỏ)
(Xem phần update mới của phần update ngày 12-02-2026)
Step Action UI Field (VN) Field (EN) Description
1 Tạo mới đánh giá Menu: Pruchase Order / Quality Control
chất lượng cho sản - Chọn kho
phẩm - Chọn “Tạo mới”
Thông tin gồm
- Tìm sản phẩm cần đánh giá
• Hỗ trợ tìm theo SKU, barcode hoặc tên sản
phẩm
- Load danh sách 10 PO nhận gần nhất của SKU
được chọn
- Ngoài ra có thể tìm mã PO chính xác theo mã
nhập vào, khi tìm thì sẽ tìm trong tất các PO có
chứa SKU đã chọn
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 39

40
2 Đánh giá chất lượng - Chọn vào PO cần đánh giá  chọn “Bắt đầu đánh
cho sản phẩm giá”
• Nếu SKU chưa được thiết lập tiêu chí đánh giá,
hiện thông báo
Thông tin gồm
- Sản phẩm: SKU – Tên sản phẩm
- PO
- Số lượng
- Nhà cung cấp: lấy theo thông tin của PO
- Ghi chú: mặc định trống và cho user edit
- Tiêu chí đạt
- Tiêu chí không đạt
Danh sách tiêu chí cần đánh giá
- Lấy theo danh sách tiêu chí được thiết lập cho
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 40

41
SKU
- Thông tin của từng tiêu chí
• Thứ tự tiêu chí
• Tên tiêu chí
• Mô tả tiêu chí
• Mô tả điều kiện của tiêu chí theo SKU
• Đạt/Không đạt
• Hình ảnh: dựa theo config để yêu cầu chụp
hình cho sản phẩm
Những tiêu chí đánh Fail thì yêu cầu
o
chụp hình và nhập ghi chú
Hỗ trợ chụp tối đa 5 hình cho 1 tiêu chí
o
(nếu có yêu cầu)
Đánh giá và cập nhật thông tin cho tất cả các tiêu chí
 chọn Hoàn thành để xác nhận đánh gia xong
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 41

42
Update 11-02-2026
Link mockup: https://www.figma.com/design/CLtzJtUv6sA4rxyaBPnbz5/34.-Quality-Control?node-
id=1946-1696&t=dt2RYJBFKqYDyulP-4
Thêm cột khi thiết lập tiêu chí (Web)
- Menu: Inbound / Quality control / Tab “Thiết lập tiêu chí”
Bổ sung thêm thông tin “QC xã vải” (Fabric relaxation QC)
o
 Khi tạo hay cập nhật tiêu chí sẽ bổ sung thêm thông tin này
 Thông tin này được dùng để tạo yêu cầu đánh giá xã vải cho các case sau:
• Khi UID group được TF vào location “F0-XV” bằng tính năng transfer
location hoặc transfer UID group thì hệ thống tự động sinh ra 1 yêu
cầu đánh giá Xã vải cho các tiêu chí có bật “QC xã vải” cho SKU
VD: SKU có thiết lập 5 tiêu chí nhưng chỉ có 2 tiêu chí được
o
bật “QC xã vải” thì chỉ sinh yêu cầu đánh giá cho 2 tiêu chi
này thôi
• Lưu ý: Số vải (90%) còn lại được nhận vào sau khi nhận 10% và đánh
giá Đạt đều phải được đánh giá qua khâu Xã vải trước khi đưa và sản
xuất
Khi tạo mới hay cập nhật tiêu chí cũng bổ sung thêm thông tin “QC xã vải”
o

43
Kết quả đánh giá (Web)
- Menu: Menu: Inbound / Quality control / Tab “Kết quả đánh giá”
Chi tiết kết quả đánh giá: bổ sung thêm 2 thông tin
o
 Số lượng cần đánh giá
 Hình ảnh tem QC
- Menu: Menu: Inbound / Quality control / Tab “Kết quả đánh giá”
Cột phân loại (Type): bổ sung thêm giá trị
o
 Xã vải / Fabric Relaxing: luồng đánh giá cho khâu xã vải trước khi chuyển qua
may thành phẩm
UID group (Web)
- Menu: Inventory / Group UID / Tab “Danh sách”
Bổ sung thêm thông tin “Đánh giá đạt” để ghi nhận các UID đã được đánh giá khâu
o
xã vải hay chưa, gồm các giá trị sau
 N/A: các SKU có khai báo UID group nhưng không thuộc category Thời trang
(NVL) và không phải là SKU vải
 No: dành cho SKU thuộc category Thời trang (NVL) và là SKU vải, sau khi
nhận hàng PO thì mặc định giá trị sẽ là No
• Sau khi đánh giá xã vải Đạt thì sẽ chuyển từ No qua Yes
 Yes: dành cho SKU thuộc category Thời trang (NVL) và là SKU vải, sau khi
nhận hàng PO và hoàn thành đánh giá xã vải và có kết quả là Đạt.
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 43

44
Khai báo số lượng cần đánh giá cho UID group (App)
- Menu: App / Purchase order / Quality control
Ở bước scan UID group cần đánh giá, bổ sung thêm thông tin cập nhật số lượng cần
o
đánh giá cho UID group
 Bắt buộc
 Phải là số nguyên dương
 Sau khi xác nhận, hệ thống tự động trừ số lượng đã khai báo ra khỏi UID
group
• VD: UID group có SKU A qty 9500, khi đánh giá user khai báo số
lượng cần đánh giá là 500 thì qty của SKU A trong UID group khi này
sẽ còn 9000
 Bổ sung thông tin này vào phần thông tin chung
Chụp hình tem QC
- Menu: App / Purchase order / Quality control
Sau khi hoàn thành đánh giá tất cả tiêu chí cho SKU, khi nhấn “Hoàn thành” bổ sung
o
thêm bước chụp hình tem QC Pass/Fail để ghi nhận lên hệ thống
 Bắt buộc
 Chỉ cần chụp 1 hình
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 44

45
Một số lưu ý cho luồng đánh giá mới
- Khi transfer UID group qua location xã vải (F0-XV) hoặc type location là “Xã vải” (Fabric
Relaxing) bằng tính năng transfer bin, transfer bin cart, transfer vị trí trong UID group,
validate
Nếu UID group đã sinh yêu cầu và được đánh giá xã vải Đạt thì bỏ qua
o
Nếu chưa được sinh yêu cầu thì sinh yêu cầu đánh giá theo tiêu chi xã vải
o
- Tiêu chí đánh giá trên SKU của PO chính phải map với tiêu chí của SKU khi đánh giá trên PO
sample
SKU PO sample đánh giá chỉ đạt 4/5 tiêu chí được thiết lập nhưng BOD vẫn duyệt
o
cho nhận hàng vào theo Lot này để tiến hành sản xuất  thì tiêu chí đánh giá cho
SKU của PO chính cũng phải dựa vào điều kiện của tiêu chí của SKU trên PO sample
 VD: điều kiện đạt của tiêu chí A của SKU được thiết lập là >6, PO sample
đánh giá chỉ 5.5 (Không đạt) nhưng BOD approve cho nhận Lot này, thì trên
PO chính SKU này cũng chỉ cần đạt từ 5.5 là Đạt yêu cầu
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 45

42
Tạo mới đánh giá – Manual
Step Action UI Description
1 Tạo mới đánh giá Menu: Pruchase Order / Quality Control
chất lượng cho sản - Chọn kho
phẩm - Chọn “Tạo mới”
Thông tin gồm
- Tìm sản phẩm cần đánh giá
• Hỗ trợ tìm theo SKU, barcode hoặc tên sản phẩm
• Chọn để tìm modal tìm kiếm sản phẩm mở rộng
- Load danh sách 10 PO nhận gần nhất của SKU được chọn theo kho
- Ngoài ra có thể tìm mã PO chính xác theo mã nhập vào, khi tìm thì sẽ tìm trong
tất các PO có chứa SKU đã chọn
- Chọn “Tiếp tục”
• Nếu SKU chưa được thiết lập tiêu chí thì hiện thông báo

47
2 Khai báo UID group Thông tin gồm:
và số lượng cần - SKU + tên sản phẩm
đánh giá - Mã PO đã chọn
- Ngày nhận PO
- Nhà cung cấp của PO
- Ghi chú
- UID group
• Bắt buộc
• Khai báo UID group cần đánh giá
- Số lượng cần đánh giá
• Bắt buộc
• Cập nhật số lượng cần đánh giá
Chọn “Bắt đầu đánh giá”, validate
- Nếu UID group không tồn tại, hiện thông báo “Mã UID không tồn tại.”
- Nếu số lượng cần khai báo không đủ số lượng trong UID group, hiện thông báo
“Số lượng trong UID group không đủ số lượng yêu cầu.”
- Ngược lại thì chuyển qua bước tiếp theo
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 47

48
3 Đánh giá chất lượng Thông tin gồm
cho sản phẩm - Nhóm UID
- Số lượng đang có của nhóm UID
- Số lô
- Hạn sử dụng
- SL cần đánh giá
- Mã PO
- Nhà cung cấp: lấy theo thông tin của PO
- Sản phẩm: SKU – Tên sản phẩm
- Ghi chú: mặc định trống và cho user edit
- Tiêu chí đạt
- Tiêu chí không đạt
Danh sách tiêu chí cần đánh giá
- Lấy theo danh sách tiêu chí được thiết lập cho SKU
- Thông tin của từng tiêu chí
• Thứ tự tiêu chí
• Tên tiêu chí
• Mô tả tiêu chí
• Mô tả điều kiện của tiêu chí theo SKU
• Đạt/Không đạt
• Hình ảnh: dựa theo config để yêu cầu chụp hình cho sản phẩm
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 48

49
Những tiêu chí đánh Fail thì yêu cầu chụp hình và nhập ghi chú
o
Hỗ trợ chụp tối đa 5 hình cho 1 tiêu chí (nếu có yêu cầu)
o
Đánh giá và cập nhật thông tin cho tất cả các tiêu chí  chọn Hoàn thành để xác nhận
đánh gia xong
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant, POS…. 49

42
Update 20-04-2026
Đánh giá SKU phụ liệu (SKU thường)
- UI update: https://www.figma.com/design/CLtzJtUv6sA4rxyaBPnbz5/34.-Quality-
Control?node-id=2542-554&t=TFGvAs3EzZ9Aj4sO-4
- Áp dụng cho các SKU KHÔNG PHẢI là cate Thời trang (NVL) và không phải là Vải
- Sau khi đánh giá tất cả các tiêu chí cho SKU, nếu kết quả đánh giá cuối cùng bị Failed (có ít
nhất 1 kết quả bị failed) thì hiển thị thêm màn hình để user xác nhận số lượng cần trả hàng
cho Nhà cung cấp
EN: SKU 422280022 has evaluation criteria marked as FAILED. Do you want to create
o
an adjustment voucher to export the failed quantity for return to vendor?
 Để sau (Later) để tắt thông báo và quay về màn hình danh sách SKU cần
đánh giá
 Chọn “Tạo phiếu điều chỉnh” (Create adjustment)
• Số lượng cần xuất trả nhà cung cấp (Quantity to Return to vendor)
Nhập số lượng cần trả
o
Số lượng phải nhỏ hơn số lượng nhập hàng PO
o
• Chọn “Đóng” để tắt thông báo
• Chọn “Xác nhận” để hệ thống tiến hành tạo 1 Adjustment xuất trả
nhà cung cấp
Warehouse: kho phát sinh
o
Type: Export
o
Reason: Return to vendor
o
Vendor: lấy từ source PO khi đánh giá SKU
o

51
Require VAT: load 3 option khi tạo Adjustment cho user
o
chọn
 No – Trả hàng không xuất hoá đơn
 Yes VAT - Hasaki xuất hoá đơn bán hàng cho NCC
 Yes VAT – NCC xuất hoá đơn điều chỉnh cho HASAKI
Source code: Mã PO khi đánh giá SKU
o
Required picking: No
o
ADJ status = Waiting for approval
o
Thông tin SKU
o
 SKU lấy theo thông tin mà user request
 Số lượng: lấy theo số lượng mà user input vào
 VAT và Price lấy theo thông tin của SKU trên Inside
theo rules của Asjustment hiện tại
Blocked UID group và chuyển Damaged
- Với các SKU vải, khi đánh giá có kết quả Failed thì hệ thống sẽ tự động blocked lại tất cả các
UID group của SKU nhận trong cùng PO và cùng LOT
Đồng thời chuyển Product status của các UID của các UID group này thành Damaged
o
để không cộng vào stock Available để không thể IT
- Khi user Un-Blocked UID group ngoài việc unbock UID group về Available thì sẽ auto chuyển
UID từ Product status Damaged thành Normal
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 51

52
Update 10-05-2026
Thiết lập tiêu chí 4 điểm khi thiết lập tiêu chí
- Tại màn hình thiết lập tiêu chí, nếu chọn phân loại là “Lỗi 4 điểm” (4 points error) thì khi
nhấn “Tạo” thì hệ thống sẽ mở thêm màn hình để thiết lập các nội dung cho thiết lập tiêu chí
4 điểm, giống với khi thiết lập tiêu chí cho SKU
Khi thiết lập tiêu chí cho SKU, nếu chọn tiêu chí 4 điểm thì hệ thống tự lấy các thiết
o
lập của tiêu chí để cập nhật cho SKU, mà không cần phải thiết lập lại cho từng SKU
Thiết lập đánh giá từng bước khi thiết lập tiêu chí
- Tại màn hình thiết lập tiêu chí, nếu chọn phân loại là “Theo từng bước” (Step by step) thì khi
nhấn “Tạo” thì hệ thống sẽ mở thêm màn hình để thiết lập các nội dung từng bước cho thiết
tiêu chí , giống với khi thiết lập tiêu chí cho SKU
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 52

53
- Khi thiết lập tiêu chí cho SKU, nếu chọn tiêu chí “Theo từng bước” thì hệ thống tự lấy các
thiết lập của tiêu chí để cập nhật cho SKU, mà không cần phải thiết lập lại cho từng SKU
Operation, E-commerce, Inside, WMS, Now, CRM, Clinic, Work, HR, Chat, Merchant,
POS…. 53