# USER COMMANDS

Trang này dành cho người dùng cuối. Chỉ cần bỏ file vào đúng thư mục `raw_sources/` rồi dùng các câu lệnh bên dưới.

---

## 📋 Luồng SDLC chuẩn

- **Bước 1** — Khởi tạo project mới (nếu chưa có):
  - `tạo project mới tên project_xxx theo chuẩn wiki rules`

- **Bước 2** — Nạp requirement mới (bỏ PDF vào `raw_sources/[project]/requirements/` trước):
  - `ingest file [tên file] trong raw_sources/[project]/requirements`
  - Nếu PDF có API/interface explicit, AI tạo thêm API Spec riêng trong `wiki/[project]/api_specs/`.

- **Bước 3a** — Phân tích task từ file Jira/ticket (bỏ file vào `raw_sources/[project]/tasks/` trước):
  - `phân tích task [tên file] thuộc [project] và tạo specs + test suite`
  - Nếu task nhắc API nhưng thiếu endpoint/method/payload/status rõ ràng, AI chỉ ghi question, chưa sinh API test case.

- **Bước 3b** — Import task từ Hasaki Workplace:
  - `import task HSK-XXXXX`
  - `tôi cần test task HSK-XXXXX`
  - paste URL: `https://work.hasaki.vn/tasks?...&task_id=...`

- **Bước 4** — Tạo Test Plan cho CR:
  - `tạo test plan cho CR-[ID] thuộc [project]`

- **Bước 5** — Đồng bộ daily note trong quá trình test:
  - `daily sync [project] ngày YYYY-MM-DD`

- **Bước 6** — Chốt task đã test xong:
  - `chuyển task [MÃ-TASK] sang Done và cập nhật suite/feature/plan`

- **Bước 7** — Khởi tạo CR Go-Live:
  - `tạo CR golive cho CR-[ID] ngày DD/MM/YYYY thuộc [project]`

- **Bước 8** — Chốt CR sau smoke test production:
  - `cập nhật kết quả smoke test và chốt CR [MÃ-CR] sang Done`

- **Bất kỳ lúc nào** — Kiểm định toàn bộ wiki:
  - `lint và sync toàn bộ wiki`
  - Mặc định chạy audit-only (`verify`) nếu bạn chưa xác nhận đã test thực tế thành công.
  - Chỉ sync trạng thái `Done/Passed` khi có xác nhận Gate 4 rõ ràng.

---

## 🔍 Tra cứu task Hasaki (không lưu vault)

Chỉ xem thông tin, không phân tích:
- `lấy task HSK-XXXXX`
- `đọc task 12032444 và tải hình về`

---

## 💻 Chạy lệnh tay (terminal)

```powershell
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

# Đồng bộ daily note
python .claude/scripts/wiki_sync.py daily-sync --project project_hasaki --date 2026-05-23

# Sync Kanban + coverage
python .claude/scripts/wiki_sync.py sync

# Audit broken links + status
python .claude/scripts/wiki_sync.py verify

# Fetch task Hasaki (chỉ xem)
$env:PYTHONUTF8 = "1"
python .claude/scripts/hasaki_task.py HSK-XXXXX

# Fetch task Hasaki kèm tải ảnh
$env:PYTHONUTF8 = "1"
python .claude/scripts/hasaki_task.py HSK-XXXXX --images --output raw_sources/project_hasaki/assets
```

---

## 📥 Nơi bỏ file đầu vào

| Loại file | Thư mục |
|-----------|---------|
| Requirement / PDF / FSD / BRD | `raw_sources/[project]/requirements/` |
| Task / Jira ticket | `raw_sources/[project]/tasks/` |
| API document / interface contract | `raw_sources/[project]/requirements/` hoặc link trong task |
| Log lỗi thô / crash log | `raw_sources/[project]/issues/` |
| Ảnh / video bằng chứng | `raw_sources/[project]/assets/` |

> **Hasaki Workplace tasks** không cần bỏ file thủ công — dùng `/import-hasaki-task` để AI tự fetch qua API.

---

## 🔑 Token Hasaki

Token lưu tại `token.txt` (root vault). Hết hạn sau ~48h kể từ lúc đăng nhập.

Cách lấy token mới:
1. Đăng nhập `work.hasaki.vn`
2. F12 → Application → Cookies → `work.hasaki.vn`
3. Copy giá trị cookie `wshr-token`
4. Paste vào `token.txt` (xoá nội dung cũ)
