---
description: "Lay thong tin task tu Hasaki Workplace (work.hasaki.vn) bang task code, numeric ID hoac URL"
allowed-tools: Read, Bash
---

# Skill: Get Hasaki Task

Fetch thong tin mot task tu Hasaki Workplace.
Mac dinh chi hien thi, khong luu task markdown vao vault.
Neu dung `--images` thi se tai anh ve `raw_sources/project_hasaki/assets/` (co ghi file vao vault).
Dung `/import-hasaki-task` neu muon phan tich va luu day du vao workflow wiki.

## Input

- **Task code**: `HSK-40187ZYO`
- **Numeric ID**: `12032444`
- **URL**: `https://work.hasaki.vn/tasks?...&task_id=12032444&...`
- **Kem `--images`**: download anh ve `raw_sources/project_hasaki/assets/`

## Thuc hien

### Buoc 1 - Kiem tra token

Token luu tai `token.txt` (root vault). Neu het han, thong bao cach lay lai token.

### Buoc 2 - Chay script

```powershell
$env:PYTHONUTF8 = "1"
python ".claude/scripts/hasaki_task.py" <TASK_CODE_OR_ID>
```

Neu muon tai anh:

```powershell
$env:PYTHONUTF8 = "1"
python ".claude/scripts/hasaki_task.py" <TASK_CODE_OR_ID> --images --output "raw_sources/project_hasaki/assets"
```

Lay JSON de xu ly tiep:

```powershell
$env:PYTHONUTF8 = "1"
python ".claude/scripts/hasaki_task.py" <TASK_CODE_OR_ID> --json
```

### Buoc 3 - Xu ly loi

| Loi | Nguyen nhan | Xu ly |
|-----|-------------|-------|
| `401 Unauthorized` | Token het han (>48h) | Yeu cau user cap nhat `token.txt` |
| `Task '...' not found` | Task khong trong my-task list | Thu numeric ID truc tiep |
| `UnicodeEncodeError` | Thieu `PYTHONUTF8=1` | Them `$env:PYTHONUTF8 = "1"` |

### Buoc 4 - Hien thi ket qua

Hien thi output truc tiep.
Neu user muon phan tich + luu + cap nhat kanban/suite thi goi y `/import-hasaki-task`.
Cac cau noi tu nhien nhu `get my task HSK-XXXXX` duoc map vao skill nay (che do tra cuu).
