# Language & Encoding

## Ngôn ngữ nội dung gen

- **Mọi nội dung AI gen ra** (Feature Spec, API Spec, Task Spec, Test Suite, Stub, Feature Group, Changelog, Kanban card, daily note, log entry, Question, Blocked Coverage) **phải viết bằng Tiếng Việt** có dấu đầy đủ.
- Giữ nguyên thuật ngữ Tiếng Anh chuyên ngành khi cần (`Feature Spec`, `R-ID`, `AC`, `Acceptance Criteria`, `Source`, `Gate 1`, `partial_read`, ...). Không dịch thuật ngữ kỹ thuật.
- Quote nguyên văn rule từ raw doc khi cần evidence — không paraphrase tiếng nước ngoài thành Tiếng Việt và ngược lại.
- Frontmatter key (vd `status`, `tags`, `partial_read`) giữ tiếng Anh; **value** ở các field human-readable (như `partial_read_note`, `approval_note`, `change_description`) viết Tiếng Việt.

## Encoding bắt buộc

- File `.md`, `.json`, `.yaml` **phải UTF-8 không BOM**. Byte mở đầu hợp lệ: ký tự nội dung thường (`---`, `{`, `# `), **không phải** `EF BB BF`.
- Mojibake (Vietnamese chars hiển thị `Tá»•ng`, `nháº­n`, `kiá»ƒm`, ...) là **lỗi nghiêm trọng** — block Gate 1.
- Bắt buộc verify sau mỗi lần tạo / chỉnh sửa file:
  ```python
  py -c "from pathlib import Path; b = Path('<file>').read_bytes(); print('OK' if not b.startswith(b'\xef\xbb\xbf') and 'á»' not in b.decode('utf-8','replace') else 'FAIL')"
  ```

## Công cụ an toàn

- **Edit tool (Claude Code)** — luôn an toàn, dùng làm default cho mọi sửa text.
- **Python**: `Path.read_text(encoding="utf-8")` + `Path.write_text(content, encoding="utf-8")`. Set `$env:PYTHONUTF8 = "1"` trước khi chạy.
- **Cấm trên Windows PowerShell 5.1**: chain `Get-Content -Raw` + replace + `Set-Content` cho file UTF-8 chứa Tiếng Việt. Lý do: `Get-Content` mặc định đọc bằng CP1252 → mojibake; `Set-Content -Encoding utf8` thêm BOM. Cả 2 đều phá file. Nếu bắt buộc dùng PowerShell, đọc bằng `[System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)` và viết bằng `[System.IO.File]::WriteAllText($path, $text, (New-Object System.Text.UTF8Encoding $false))` (UTF-8 không BOM).

## Audit

- `wiki_sync.py verify` phải fail nếu phát hiện BOM hoặc mojibake pattern (`á»`, `Æ°`, `Ã£`, `Ã¡`, `Ä‚`, `áº£`, ...) trong `wiki/` hoặc `raw_sources/`.
- Khi script gen output (`generate_stub_features_from_index.py`, `wiki_sync.py daily-sync`, ...) — script phải `write_text(..., encoding="utf-8")` không BOM, **không** dùng `Out-File`/`Set-Content` của PowerShell trong subprocess.
