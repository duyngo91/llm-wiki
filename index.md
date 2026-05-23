---
tags: [moc, index]
status: Done
created: 2026-05-23
updated: 2026-05-23
---

# 🗺️ Mục Lục QA LLM Wiki — Multi-Project Portfolio

> Bản đồ điều hướng chính của hệ thống. AI đọc file này ĐẦU TIÊN để định vị thông tin theo từng dự án.
> *(Lưu ý: Hãy cài đặt và bật plugin **Dataview** trong Obsidian để các bảng thống kê động tự động hoạt động).*

## 🧭 Điều hướng nhanh
- [[WIKI_RULES|📜 Bộ quy tắc vận hành]]
- [[KANBAN|📋 Bảng Kanban Task]]
- [[log|📅 Nhật ký hoạt động]]
- [[OBSIDIAN_GUIDE|🗺️ Cẩm nang tối ưu Obsidian]]

---

## 📂 DỰ ÁN 1: DEMO EMAIL (`project_demo`)

### 📋 Nghiệp vụ & Kịch bản Test
```dataview
TABLE status AS "Trạng thái", file.folder AS "Thư mục"
FROM "wiki/project_demo/features" OR "wiki/project_demo/test_suites"
SORT file.name ASC
```

### 📋 Kế hoạch Kiểm thử (Test Plans)
```dataview
TABLE status AS "Trạng thái", created AS "Ngày tạo"
FROM "wiki/project_demo/test_plans"
SORT file.name ASC
```

### 📊 Lịch sử Go-Live / Releases
```dataview
TABLE status AS "Trạng thái", cr_id AS "Mã CR", golive_date AS "Ngày Go-Live", approver AS "Người Duyệt"
FROM "wiki/project_demo/releases"
SORT golive_date DESC
```

### 🐛 Kho Tri Thức Lỗi & RCA
```dataview
TABLE status AS "Trạng thái", severity AS "Mức độ", environment AS "Môi trường"
FROM "wiki/project_demo/bugs_knowledge"
SORT file.ctime DESC
```

### ⚙️ Thông Tin Vận Hành
- [[wiki/project_demo/operations/environments|🌐 Môi trường Test]]
- [[wiki/project_demo/operations/test_data|📦 Dữ liệu Test Mẫu]]
- [[wiki/project_demo/operations/team_contacts|👥 Danh bạ Dự án]]

### 📥 Tài Liệu Gốc (Raw Sources)
- `raw_sources/project_demo/tasks/` — Task/Jira ticket gốc
- `raw_sources/project_demo/requirements/` — PDF/FSD/BRD/Baseline
- `raw_sources/project_demo/issues/` — Log lỗi thô
- `raw_sources/project_demo/assets/` — Ảnh/video bằng chứng

---

## 📂 DỰ ÁN 2: ORANGEHRM PORTAL (`project_orange`)

### 📋 Nghiệp vụ & Kịch bản Test
```dataview
TABLE status AS "Trạng thái", file.folder AS "Thư mục"
FROM "wiki/project_orange/features" OR "wiki/project_orange/test_suites"
SORT file.name ASC
```

### 📋 Kế hoạch Kiểm thử (Test Plans)
```dataview
TABLE status AS "Trạng thái", created AS "Ngày tạo"
FROM "wiki/project_orange/test_plans"
SORT file.name ASC
```

### 📊 Lịch sử Go-Live / Releases
```dataview
TABLE status AS "Trạng thái", cr_id AS "Mã CR", golive_date AS "Ngày Go-Live", approver AS "Người Duyệt"
FROM "wiki/project_orange/releases"
SORT golive_date DESC
```

### 🐛 Kho Tri Thức Lỗi & RCA
```dataview
TABLE status AS "Trạng thái", severity AS "Mức độ", environment AS "Môi trường"
FROM "wiki/project_orange/bugs_knowledge"
SORT file.ctime DESC
```

### ⚙️ Thông Tin Vận Hành
- [[wiki/project_orange/operations/environments|🌐 Môi trường Test]]
- [[wiki/project_orange/operations/test_data|📦 Dữ liệu Test Mẫu]]
- [[wiki/project_orange/operations/team_contacts|👥 Danh bạ Dự án]]

### 📥 Tài Liệu Gốc (Raw Sources)
- `raw_sources/project_orange/tasks/` — Task/Jira ticket gốc
- `raw_sources/project_orange/requirements/` — PDF/FSD/BRD/Baseline
- `raw_sources/project_orange/issues/` — Log lỗi thô
- `raw_sources/project_orange/assets/` — Ảnh/video bằng chứng

---

## 📂 DỰ ÁN 3: HASAKI (`project_hasaki`)

### 📋 Nghiệp vụ & Kịch bản Test
```dataview
TABLE status AS "Trạng thái", file.folder AS "Thư mục"
FROM "wiki/project_hasaki/features" OR "wiki/project_hasaki/test_suites"
SORT file.name ASC
```

### 📋 Kế hoạch Kiểm thử (Test Plans)
```dataview
TABLE status AS "Trạng thái", created AS "Ngày tạo"
FROM "wiki/project_hasaki/test_plans"
SORT file.name ASC
```

### 📊 Lịch sử Go-Live / Releases
```dataview
TABLE status AS "Trạng thái", cr_id AS "Mã CR", golive_date AS "Ngày Go-Live", approver AS "Người Duyệt"
FROM "wiki/project_hasaki/releases"
SORT golive_date DESC
```

### 🐛 Kho Tri Thức Lỗi & RCA
```dataview
TABLE status AS "Trạng thái", severity AS "Mức độ", environment AS "Môi trường"
FROM "wiki/project_hasaki/bugs_knowledge"
SORT file.ctime DESC
```

### ⚙️ Thông Tin Vận Hành
- [[wiki/project_hasaki/operations/environments|🌐 Môi trường Test]]
- [[wiki/project_hasaki/operations/test_data|📦 Dữ liệu Test Mẫu]]
- [[wiki/project_hasaki/operations/team_contacts|👥 Danh bạ Dự án]]

### 📥 Tài Liệu Gốc (Raw Sources)
- `raw_sources/project_hasaki/tasks/` — Task/Jira ticket gốc
- `raw_sources/project_hasaki/requirements/` — PDF/FSD/BRD/Baseline
- `raw_sources/project_hasaki/issues/` — Log lỗi thô
- `raw_sources/project_hasaki/assets/` — Ảnh/video bằng chứng
