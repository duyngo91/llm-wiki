---
name: obsidian-search
description: Tìm kiếm ghi chú trong Obsidian vault sử dụng Omnisearch MCP hoặc HTTP API. Dùng khi cần tìm Feature Spec, Test Suite, Task Spec, raw source, hoặc bất kỳ note nào trong vault theo từ khóa. Kết quả trả về ranked list với excerpt — có thể feed trực tiếp vào các skill khác. Trigger: "tìm note", "tìm spec", "search vault", "tìm file liên quan đến", "có note nào về", "tìm test suite của".
metadata:
  author: Yen Ngo
  version: "1.0"
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
---

# Obsidian Search Skill

Skill tìm kiếm trong Obsidian vault, ưu tiên dùng **Omnisearch MCP** (đã config sẵn). Fallback sang **HTTP API** nếu MCP không available. Fallback cuối cùng là **Grep** native.

## Thứ tự ưu tiên (Search Strategy)

```
1. Omnisearch MCP Tool  →  mcp-server-obsidian-omnisearch (semantic ranking)
2. Omnisearch HTTP API  →  GET http://localhost:51361/search?q=...
3. Grep fallback        →  Grep trực tiếp trong vault directory
```

---

## Cách thực hiện

### Bước 1 — Xác định query

Trích query từ yêu cầu của user. Nếu yêu cầu mơ hồ, hỏi lại trước khi tìm.

Query tips:
- Dùng tiếng Việt hoặc tiếng Anh theo ngôn ngữ trong vault
- Kết hợp từ khóa nghiệp vụ: tên feature, mã task (HSK-xxxxx, TBB2-xxxxx)
- Tách query phức tạp thành nhiều query đơn, merge kết quả

### Bước 2 — Thực thi search

#### Phương thức A: Omnisearch MCP Tool (ưu tiên)

Gọi tool `obsidian_notes_search` với query string. Tool trả về danh sách absolute paths.

Sau khi có paths → đọc từng file để lấy excerpt/context nếu cần.

#### Phương thức B: Omnisearch HTTP API (fallback khi MCP lỗi)

```bash
curl -s "http://localhost:51361/search?q=QUERY_ENCODED" -o /tmp/omni.json && py -c "
import json; data=json.load(open('/tmp/omni.json'))
[print(f'{i+1}. [{r[\"score\"]:.1f}] {r[\"path\"]}\n   {r[\"excerpt\"][:200]}') for i,r in enumerate(data[:8])]
"
```

**Windows notes:**
- Dùng `py` (không phải `python`) — alias `python` không tồn tại trên máy này
- Không pipe curl thẳng vào `py -c` — dễ bị empty stdin khi API trả rỗng; luôn save ra file `-o /tmp/omni.json` rồi đọc file
- Query nên dùng ASCII/English — Vietnamese URL-encoded có thể trả về empty response từ Omnisearch
- Nếu API trả về empty (`[]` hoặc `""`): fallback sang Grep

Response là JSON array `ResultNoteApi[]`:
```json
[
  {
    "score": 9.5,
    "vault": "llm-wiki",
    "path": "wiki/project_hasaki/features/receiving_po.md",
    "basename": "receiving_po",
    "foundWords": ["receiving", "PO"],
    "matches": [{"match": "Receiving PO", "offset": 42}],
    "excerpt": "...nhận hàng từ PO được xử lý qua màn hình..."
  }
]
```

Sắp xếp theo `score` giảm dần, lấy top 10.

#### Phương thức C: Grep fallback (khi Obsidian không chạy)

```
Grep pattern=KEYWORD path=wiki/ output_mode=files_with_matches
```

Giới hạn trong `wiki/` và `raw_sources/` theo AI Knowledge Scope.

### Bước 3 — Format kết quả

Trả kết quả theo bảng:

| # | File | Excerpt | Score |
|---|------|---------|-------|
| 1 | `wiki/.../feature_x.md` | "...đoạn trích liên quan..." | 9.5 |
| 2 | `raw_sources/.../HSK-12345.md` | "...đoạn trích..." | 7.2 |

Kèm theo:
- Tổng số kết quả tìm thấy
- Phương thức đã dùng (MCP / HTTP / Grep)
- Gợi ý bước tiếp theo (mở file, feed vào skill nào)

---

## Tích hợp với các skill khác

Obsidian Search có thể được gọi **trước** các skill sau để tìm đúng file cần làm việc:

| Skill tiếp theo | Dùng Obsidian Search để tìm |
|---|---|
| `wiki-requirement-analyzer` | Feature Spec draft cần update |
| `wiki-test-designer` | Spec đã Gate 1, cần thiết kế test |
| `wiki-sync-helper` | Task Spec, suite cần sync |
| `hasaki-spec-verifier` | Raw source + wiki artifact để đối soát |

**Pattern gọi chuỗi:**
```
User: "tìm test suite liên quan đến Quality Control"
→ obsidian-search query="Quality Control test suite"
→ trả về: wiki/project_hasaki/test_suites/ts_quality_control.md
→ gợi ý: "Bạn muốn mở file này hay chạy /wiki-test-designer?"
```

---

## Vault path

Vault root: `C:\project\NB_Hasaki\llm-wiki`

Các thư mục search theo scope:
- `wiki/project_hasaki/features/` — Feature Specs
- `wiki/project_hasaki/test_suites/` — Test Suites
- `wiki/project_hasaki/task_specs/` — Task Specs
- `wiki/project_hasaki/api_specs/` — API Specs
- `raw_sources/project_hasaki/` — Raw sources (PDF, task export)

Excluded (theo AI Knowledge Scope): `.obsidian/`, `.git/`, `*.sqlite*`

---

## Xử lý lỗi

| Lỗi | Xử lý |
|---|---|
| MCP tool không available | Thử HTTP API |
| HTTP API trả về `connection refused` | Obsidian chưa chạy hoặc HTTP server chưa bật → fallback Grep, thông báo user |
| HTTP API trả về empty / `JSONDecodeError` | Lưu ra file trước (`-o /tmp/omni.json`), thử query ASCII, nếu vẫn rỗng → fallback Grep |
| `python` command not found | Dùng `py` thay thế (Windows alias) |
| Query không có kết quả | Thử broad query (bỏ bớt từ), gợi ý từ khóa thay thế |
| Kết quả quá nhiều (>20) | Yêu cầu user thu hẹp query hoặc chỉ định loại file |

---

## Ví dụ

```
User: "tìm spec của màn hình nhận hàng"
→ query: "receiving PO nhận hàng"
→ kết quả: wiki/project_hasaki/features/feature_receiving_po.md (score: 9.2)
→ output: hiển thị bảng + gợi ý "/wiki-test-designer nếu spec đã Gate 1"
```

```
User: "có task spec nào liên quan TBB2-07062 không"
→ query: "TBB2-07062"
→ kết quả: wiki/project_hasaki/task_specs/task_TBB2-07062.md
→ output: hiển thị path + frontmatter status
```
