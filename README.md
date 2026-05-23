# LLM Wiki

Kho tri thức QA/Test theo mô hình wiki (Obsidian-first), dùng để quản lý:
- Feature/Requirement
- Test Suite, Test Plan
- Release/Go-live
- Bug knowledge & RCA
- Tài liệu vận hành theo từng dự án

Repo: [duyngo91/llm-wiki](https://github.com/duyngo91/llm-wiki)

Bắt đầu sử dụng: đọc [USER_COMMANDS.md](./USER_COMMANDS.md) trước, sau đó dùng [WIKI_RULES.md](./WIKI_RULES.md) khi cần quy tắc/quy trình chi tiết.

Hướng dẫn lệnh cho người dùng (nguồn command duy nhất): [USER_COMMANDS.md](./USER_COMMANDS.md)
Quy tắc vận hành và governance: [WIKI_RULES.md](./WIKI_RULES.md)

## Cấu trúc chính

```text
LLM_Wiki/
├─ .agents/skills/       # Agent Skills cho workflow QA wiki
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

Thư mục `.agents/skills/` chứa các Agent Skills hỗ trợ workflow QA wiki. Mỗi skill dùng cấu trúc chuẩn: `.agents/skills/<skill-name>/SKILL.md` và metadata UI tại `.agents/skills/<skill-name>/agents/openai.yaml`.
- `wiki-sync-helper`: hỗ trợ đồng bộ trạng thái/task trong wiki.
- `wiki-requirement-analyzer`: phân tích requirement theo ISTQB Test Analysis để tạo/cập nhật feature spec.
- `wiki-test-designer`: thiết kế test case/test suite theo ISTQB Test Design.

Quy ước script:
- `.agents/skills/<skill-name>/scripts/`: logic độc lập phục vụ riêng skill đó.
- `scripts/`: shim tương thích để người dùng vẫn chạy command ngắn từ root vault.

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
