---
tags: [guide, system]
status: 🌳 evergreen
created: 2026-05-23
updated: 2026-05-23
---

# 🗺️ CẨM NANG CẤU HÌNH & TỐI ƯU OBSIDIAN CHO QA WIKI

Để biến hệ thống này thành một trợ lý kiểm thử mạnh mẽ nhất cho cả **bạn** và **AI**, hãy làm theo hướng dẫn thiết lập các plugin cộng đồng cực kỳ quan trọng dưới đây.

---

## 🔌 1. Cài đặt các Plugin cộng đồng (Community Plugins)

Trong Obsidian, hãy vào **Settings ➔ Community plugins ➔ Turn on community plugins ➔ Browse** và tìm các plugin sau:

### 1.1. 🔍 Omnisearch (Tìm kiếm thông minh)
*   **Mục đích:** Tìm kiếm tức thì trong toàn bộ note, file PDF tài liệu gốc, và thậm chí tự động đọc chữ trong hình ảnh chụp màn hình bug (OCR) trong thư mục `raw_sources/assets/`.
*   **Cấu hình khuyên dùng:**
    1.  Sau khi cài, vào **Settings ➔ Omnisearch**.
    2.  Bật tính năng **Search in PDFs** (Tìm trong file PDF).
    3.  Bật tính năng **Text extraction (OCR)** để tìm được chữ trong các ảnh chụp màn hình lỗi.

### 1.2. 📊 Dataview (Tự động cập nhật bảng biểu)
*   **Mục đích:** Giúp trang `index.md` tự động thu thập và hiển thị danh sách Requirement, Test Suite, và Bug mà không cần bạn hoặc AI phải sửa bằng tay.
*   **Cấu hình khuyên dùng:**
    1.  Sau khi cài, vào **Settings ➔ Dataview**.
    2.  Bật tùy chọn **Enable JavaScript Queries** và **Enable Inline Queries** để hỗ trợ các câu lệnh thống kê nâng cao.

### 1.3. 📋 Kanban (Giao diện Quản lý Task kéo thả)
*   **Mục đích:** Quản lý các task kiểm thử trực quan dạng bảng với các cột **TODO**, **InProgress**, và **Done**.
*   **Cấu hình khuyên dùng:**
    1.  Cài đặt plugin **Kanban**.
    2.  Hệ thống đã có sẵn file `KANBAN.md` chuẩn cấu hình Obsidian Kanban.
    3.  Chỉ cần mở file `KANBAN.md` trong Obsidian ➔ bảng Kanban tuyệt đẹp sẽ tự động hiển thị để bạn kéo thả quản lý.

### 1.4. 📝 Templater (Trình tạo mẫu tự động hóa nâng cao)
*   **Mục đích:** Thay thế hệ thống template cơ bản của Obsidian. Giúp tự động chèn tiêu đề, ngày giờ động và **tự động áp dụng đúng template khi tạo file mới trong từng thư mục**.
*   **Cấu hình khuyên dùng:**
    1.  Vào **Settings ➔ Templater**.
    2.  Tại mục **Template folder location**, trỏ đến thư mục `templates/`.
    3.  Cuộn xuống mục **Folder Templates** (Mẫu tự động theo thư mục) và cấu hình như sau:
        *   Thư mục `wiki/features/` ➔ Chọn template `tpl_requirement.md`.
        *   Thư mục `wiki/test_suites/` ➔ Chọn template `tpl_test_suite.md`.
        *   Thư mục `wiki/bugs_knowledge/` ➔ Chọn template `tpl_bug_rca.md`.
        *   Thư mục `wiki/operations/daily_notes/` ➔ Chọn template `tpl_daily.md`.
    4.  Bật tùy chọn **Trigger Templater on new file creation** (Tự động kích hoạt khi tạo file mới).
    *   *(Từ bây giờ, bạn chỉ cần tạo file trống trong thư mục tương ứng, Obsidian sẽ tự chèn và điền thông tin chuẩn ngay lập tức).*

### 1.5. 🤖 Smart Connections hoặc Copilot (AI Chat với Notes)
*   **Mục đích:** Cho phép bạn trò chuyện trực tiếp với toàn bộ tài liệu kiểm thử của mình. Bạn có thể hỏi: *"Hôm nay có bug nào nghiêm trọng cần test lại không?"*
*   **Cấu hình khuyên dùng:**
    1.  Cài đặt plugin **Smart Connections** hoặc **Copilot**.
    2.  Nhập API Key của Gemini/OpenAI hoặc cấu hình chạy offline bằng Ollama.
    3.  Chạy **Index** để AI quét toàn bộ tài liệu trong Vault.

---

## 🎨 2. Tối ưu hóa giao diện đồ thị (Graph View)

Graph View trong Obsidian giúp bạn nhìn thấy mối quan hệ giữa Specs, Test Cases và Bugs. Hãy cấu hình như sau:

1.  Mở **Graph View** từ thanh bên trái.
2.  Mở phần **Groups** và thêm các màu sắc cho Tag để phân biệt trực quan:
    *   `#qa/requirement` ➔ **Màu Xanh lá** 🟢 (Yêu cầu nghiệp vụ)
    *   `#qa/test-suite` ➔ **Màu Xanh dương** 🔵 (Kịch bản kiểm thử)
    *   `#qa/bug/open` ➔ **Màu Đỏ** 🔴 (Lỗi đang mở)
    *   `#qa/bug/fixed` ➔ **Màu Xám** ⚫ (Lỗi đã sửa)
3.  **Bật Display:** Chọn bật **Arrows** (Mũi tên liên kết) để biết luồng kế thừa thông tin từ Specs sang Test Cases.

---

## 🚀 3. Cách sử dụng hàng ngày của Tester (Quy trình chuẩn)

1.  **Nhập Requirement:** Ném file PDF specs của PO vào `raw_sources/requirements/`. Ra lệnh cho AI: *"Nạp tài liệu PDF này và tạo Requirement, Test Suite cho tôi"*.
2.  **Cập nhật quyết định họp:** Cuối ngày, bạn chỉ cần gõ nhanh quyết định nghiệp vụ vào `operations/daily_notes/YYYY-MM-DD.md`. AI sẽ tự động đọc file này mỗi sáng và cập nhật lại Specs cũng như Test Suite tương ứng.
3.  **Tạo Bug nhanh:** Khi phát hiện bug, dùng template `tpl_bug_rca.md` tạo note mới. AI sẽ phân tích nguyên nhân gốc rễ (RCA) và tự đề xuất thêm kịch bản test mới để ngăn lỗi lặp lại trong tương lai.
