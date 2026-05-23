---
description: "Lấy thông tin task từ Hasaki Workplace (work.hasaki.vn) bằng task code, numeric ID hoặc URL"
allowed-tools: Read, Bash
---

# Skill: Get Hasaki Task

Fetch thông tin một task từ Hasaki Workplace. Chỉ hiển thị — không lưu vào vault. Dùng `/import-hasaki-task` nếu muốn phân tích và lưu.

## Input

- **Task code**: `HSK-40187ZYO`
- **Numeric ID**: `12032444`
- **URL**: `https://work.hasaki.vn/tasks?...&task_id=12032444&...`
- **Kèm `--images`**: download ảnh về `raw_sources/project_hasaki/assets/`

## Thực hiện

### Bước 1 — Kiểm tra token

Token lưu tại `token.txt` (root vault). Nếu hết hạn, thông báo:

> "Token đã hết hạn. Vui lòng:
> 1. Đăng nhập lại tại work.hasaki.vn
> 2. F12 → Application → Cookies → `work.hasaki.vn`
> 3. Copy giá trị cookie `wshr-token`
> 4. Paste vào `token.txt` (xoá nội dung cũ)"

### Bước 2 — Chạy script

```powershell
$env:PYTHONUTF8 = "1"
python ".claude/scripts/hasaki_task.py" <TASK_CODE_OR_ID>
```

Nếu muốn tải ảnh:
```powershell
$env:PYTHONUTF8 = "1"
python ".claude/scripts/hasaki_task.py" <TASK_CODE_OR_ID> --images --output "raw_sources/project_hasaki/assets"
```

Lấy JSON để xử lý tiếp:
```powershell
$env:PYTHONUTF8 = "1"
python ".claude/scripts/hasaki_task.py" <TASK_CODE_OR_ID> --json
```

### Bước 3 — Xử lý lỗi

| Lỗi | Nguyên nhân | Xử lý |
|-----|-------------|-------|
| `401 Unauthorized` | Token hết hạn (>48h) | Yêu cầu user cập nhật `token.txt` |
| `Task '...' not found` | Task không trong my-task list | Thử numeric ID trực tiếp |
| `UnicodeEncodeError` | Thiếu `PYTHONUTF8=1` | Thêm `$env:PYTHONUTF8 = "1"` |

### Bước 4 — Hiển thị kết quả

Hiển thị output trực tiếp. Nếu ảnh được download, đọc và hiển thị bằng `Read` tool.

Nếu user muốn phân tích và lưu vào wiki → gợi ý `/import-hasaki-task`.
