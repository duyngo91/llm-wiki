---
description: "Scan tất cả tasks Hasaki được assign cho yenngo, phát hiện NEW/UPDATED tasks, hiển thị wiki impact, và download raw files — HITL Gate 1/2 bắt buộc trước khi cập nhật Feature Spec/Test Suite"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Skill: Get My Tasks

Scan tất cả tasks trên Hasaki Workplace được assign cho user hiện tại, so sánh với raw files đã lưu, hiển thị nhóm NEW / UPDATED / CURRENT, phát hiện wiki impact, và download raw files khi user xác nhận.

**Không tự cập nhật Feature Spec, API Spec, hay Test Suite** — chỉ cập nhật raw_sources. Wiki update cần HITL Gate 1/2.

---

## Thực hiện

### Bước 1 — Kiểm tra token

Token lưu tại `token.txt` (root vault). Nếu hết hạn (exit code 2), thông báo:

> "Token đã hết hạn. Vui lòng:
> 1. Đăng nhập lại tại work.hasaki.vn
> 2. F12 → Application → Cookies → work.hasaki.vn
> 3. Copy giá trị cookie `wshr-token`
> 4. Paste vào `token.txt` (xoá nội dung cũ)"

### Bước 2 — Scan + Diff (dry-run)

```powershell
$env:PYTHONUTF8 = "1"; $env:PYTHONIOENCODING = "utf-8"
python ".claude/scripts/hasaki_my_tasks.py"
```

Tùy chọn:
```powershell
# Chỉ lấy tóm tắt nhanh (không hiển thị detail)
python ".claude/scripts/hasaki_my_tasks.py" --check-updates

# Lấy kể cả task Done
python ".claude/scripts/hasaki_my_tasks.py" --status all

# JSON output (để xử lý tiếp)
python ".claude/scripts/hasaki_my_tasks.py" --json
```

### Bước 3 — Hiển thị kết quả theo 3 nhóm

Hiển thị output đầy đủ từ script. Output nhóm theo **HSK task cha**, TBB2 test request hiển thị là sub-item:

**🆕 NEW** — HSK chưa có raw file:
```
HSK-29774D68 — Receiving PO: Update rules nhận PO gốc...
   └─ TBB2-391C5 — Validate PO gốc nếu đánh giá PO sample
   └─ TBB2-D7172 — Update rules nhận PO gốc 30%
```

**🔄 UPDATED** — HSK đã có raw file nhưng `updated_at` thay đổi:
- Code, tên, thời điểm thay đổi, TBB2 liên kết
- **Wiki impact**: file Feature Spec / Test Suite reference HSK code này

**✅ CURRENT** — HSK không thay đổi

**⚠️ ORPHAN TBB2** — TBB2 không resolve được HSK parent (cần check)

### Bước 4 — HITL Gate: Hỏi user

Sau khi hiển thị kết quả, hỏi:

> **Bạn muốn download task nào?**
> - `all` — download tất cả NEW + UPDATED
> - `[HSK-XXXXX]` — chỉ download task cụ thể
> - `skip` — không download gì cả
>
> ⚠️ Lưu ý:
> - Download chỉ cập nhật `raw_sources/project_hasaki/tasks/` (raw file).
> - Để cập nhật Feature Spec hoặc Test Suite, cần chạy `/wiki-requirement-analyzer` SAU KHI PO/QA Lead duyệt (HITL Gate 1/2).
> - Wiki impact ở trên chỉ là danh sách file có thể bị ảnh hưởng — chưa tự cập nhật.

**Đợi user xác nhận** trước khi chạy download.

### Bước 5 — Download (sau khi user xác nhận)

```powershell
# Download tất cả new + updated
$env:PYTHONUTF8 = "1"; $env:PYTHONIOENCODING = "utf-8"
python ".claude/scripts/hasaki_my_tasks.py" --download

# Download task cụ thể
python ".claude/scripts/hasaki_my_tasks.py" --download HSK-40187ZYO
```

### Bước 6 — Sau download: Báo cáo + Hỏi bước tiếp

Hiển thị danh sách file đã lưu, sau đó hỏi:

> "Đã cập nhật X raw file(s) trong `raw_sources/project_hasaki/tasks/`.
>
> **Bước tiếp theo** (chọn theo nhu cầu):
>
> **Nếu có task UPDATED với wiki impact:**
> - Đọc raw file và Feature Spec bị ảnh hưởng
> - Phân tích Impact Analysis (so sánh `task.note` cũ và mới)
> - Khi PO/QA Lead xác nhận cần cập nhật Spec → chạy `/wiki-requirement-analyzer`
>
> **Nếu có task NEW:**
> - `/import-hasaki-task [HSK-XXXXX]` để extract AC List và tạo Task Note đầy đủ
> - Hoặc `/wiki-requirement-analyzer` nếu task chứa requirement rõ ràng
>
> **Cần kiểm tra impact cụ thể không?** Tôi có thể đọc raw file và Feature Spec để phân tích diff."

---

## Xử lý lỗi

| Tình huống | Xử lý |
|-----------|-------|
| Token hết hạn (exit 2) | Hướng dẫn lấy token mới, dừng |
| Không có task nào | Thông báo "Không có task open nào được assign" |
| Task không tìm thấy khi download | Thông báo lỗi, bỏ qua task đó, tiếp tục các task còn lại |
| Wiki dir không tồn tại | Impact check trả về rỗng — thông báo không tìm được reference |
| `UnicodeEncodeError` | Thêm `$env:PYTHONUTF8 = "1"` và `$env:PYTHONIOENCODING = "utf-8"` |

---

## Guardrails

- **KHÔNG tự cập nhật Feature Spec, API Spec, Test Suite** — chỉ cập nhật raw_sources/
- **KHÔNG tự chạy `/wiki-requirement-analyzer`** sau download — đợi user yêu cầu
- **KHÔNG đánh dấu task nào là "đã review"** khi chưa có xác nhận từ PO/QA Lead
- **KHÔNG xóa raw file cũ** khi download bản mới — ghi đè là đủ
- **Wiki impact chỉ là tham chiếu** — không chứng minh task đó thực sự ảnh hưởng đến wiki page
- **Raw file lưu theo HSK code** (`HSK-xxxxx.md`), TBB2 được embed vào section `## Test Requests (TBB2)` — không tạo file riêng cho TBB2
- **Wiki impact check theo HSK code** — Feature Spec/Test Suite reference HSK, không phải TBB2
- Mọi download phải ghi `log.md` với prefix `[ingest]`

---

## Ghi log sau khi download

Sau khi download xong, ghi vào `log.md`:

```
- [YYYY-MM-DD HH:mm:ss] [ingest] | get-my-tasks: download X tasks (Y new, Z updated). Files: [danh sách codes]
```
