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

## Skills trong vault (Claude Code Slash Commands)

Các skill được tổ chức thành **Claude Code slash commands** tại `.claude/commands/`. Gọi trực tiếp bằng `/` trong Claude Code:

| Slash Command | Mô tả |
|:--------------|:------|
| `/wiki-requirement-analyzer` | ISTQB Test Analysis — phân tích requirement, tạo/cập nhật Feature Spec |
| `/wiki-test-designer` | ISTQB Test Design — thiết kế test cases/test suite có traceable |
| `/wiki-sync-helper` | Bảo trì wiki — daily sync, Kanban sync, audit broken links |

Logic nghiệp vụ và script python vẫn nằm tại:
- `.agents/shared/`: thư viện dùng chung cho nhiều skill.
- `.agents/skills/<skill-name>/SKILL.md`: tài liệu kỹ thuật chi tiết của skill.
- `.agents/skills/<skill-name>/scripts/`: entrypoint python phục vụ riêng skill đó.
- `scripts/`: shim tương thích để chạy lệnh ngắn từ root vault.

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
