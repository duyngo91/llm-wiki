# LLM Wiki

Kho tri thức QA/Test theo mô hình wiki (Obsidian-first), dùng để quản lý:
- Feature/Requirement
- Test Suite, Test Plan
- Release/Go-live
- Bug knowledge & RCA
- Tài liệu vận hành theo từng dự án

Repo: [duyngo91/llm-wiki](https://github.com/duyngo91/llm-wiki)

## Cấu trúc chính

```text
LLM_Wiki/
├─ wiki/                 # Nội dung wiki theo project
│  ├─ project_demo/
│  └─ project_orange/
├─ templates/            # Mẫu tài liệu markdown
├─ raw_sources/          # Dữ liệu đầu vào (task, issue, asset...)
├─ scripts/              # Script hỗ trợ quản lý/kiểm tra wiki
├─ index.md              # Mục lục trung tâm (MOC)
├─ WIKI_RULES.md         # Quy tắc vận hành wiki
├─ KANBAN.md             # Bảng task
└─ log.md                # Nhật ký hoạt động
```

## Bắt đầu nhanh

1. Clone repo:
```bash
git clone https://github.com/duyngo91/llm-wiki.git
cd llm-wiki
```

2. Mở thư mục bằng Obsidian:
- `Open folder as vault` và chọn thư mục `llm-wiki`.
- Mở `index.md` để điều hướng toàn bộ nội dung.

3. Bật plugin cần thiết trong Obsidian:
- Dataview
- Kanban
- Omnisearch / Smart Connections (nếu cần tìm kiếm nâng cao)

## Skills trong vault

Thư mục `.agent/` đang chứa các skill hỗ trợ workflow QA wiki:
- `wiki-sync-helper`: hỗ trợ đồng bộ trạng thái/task trong wiki.
- `wiki-requirement-analyzer` (mới): phân tích requirement theo ISTQB Test Analysis để tạo/cập nhật feature spec.
- `wiki-test-designer` (mới): thiết kế test case/test suite theo ISTQB Test Design.

## Quy ước làm việc

- Tạo/sửa nội dung theo chuẩn trong `WIKI_RULES.md`.
- Ưu tiên dùng template trong `templates/`.
- Commit theo lô nhỏ, message rõ ràng.

Ví dụ:
```bash
git add .
git commit -m "docs: update test suite and release notes"
git push
```
