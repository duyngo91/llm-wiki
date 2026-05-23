# USER COMMANDS

Trang này dành cho người dùng cuối. Chỉ cần bỏ file vào đúng thư mục `raw_sources/` rồi dùng các câu lệnh bên dưới.

## Nhắn AI

- Nạp requirement mới:
  - `ingest file mới trong raw_sources/requirements`
- Xử lý task Jira mới:
  - `phân tích task mới và tạo specs + test suite`
- Đồng bộ daily note:
  - `daily sync project_orange ngày 2026-05-23`
- Dọn dẹp và kiểm định toàn wiki:
  - `lint và sync toàn bộ wiki`
- Chốt task đã test xong:
  - `chuyển task [MÃ-TASK] sang Done và cập nhật suite/feature/plan`
- Tạo project mới:
  - `tạo project mới tên project_xxx theo chuẩn wiki rules`

## Chạy lệnh tay (terminal)

```bash
python scripts/wiki_manager.py daily-sync --project project_orange --date 2026-05-23
python scripts/wiki_manager.py sync
python scripts/verify_wiki.py
```

## Nơi bỏ file đầu vào

- Requirement/PDF: `raw_sources/requirements/`
- Task/Jira theo dự án: `raw_sources/[project]/tasks/`
- Log lỗi thô: `raw_sources/issues/`
- Ảnh/video bằng chứng: `raw_sources/assets/`
