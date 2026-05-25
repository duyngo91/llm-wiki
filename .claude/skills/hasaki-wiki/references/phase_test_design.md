---
tags: [wiki-rules, reference]
status: Done
updated: 2026-05-24
---

# Phase: Test Design

> Dùng bởi: `/wiki-test-designer` — thiết kế Test Suite từ Feature Spec đã được Gate 1 duyệt.

---

## Điều kiện tiên quyết

**Phải có Gate 1 trước:** Feature Spec status `Done` với đủ `approved_by`, `approved_at`, `approval_note` trong frontmatter.

---

## Quy tắc đặt tên

| Thư mục | Định dạng | Ví dụ |
|:--------|:----------|:------|
| `test_suites/` | `test_[feature]_[mucnho].md` | `test_auth_login.md` |
| `feature_groups/` | `[feature_group].md` | `receiving_po.md` |
| `task_specs/` | `task_[tbb2_code].md` | `task_TBB2-12345.md` |

**Tags chuẩn:**
- `#qa/test-suite` cho `test_suites/`
- `#qa/feature-group/[slug]` cho test suite thuộc group (slug dùng `-`, file dùng `_`)
- `#qa/feature-group-index` cho trang group MOC (`feature_groups/`)

**Double-linking:** Dùng `[[Tên Trang]]` kết nối Feature ↔ Test Suite ↔ Daily Note. Feature có quan hệ phụ thuộc → thêm `Mối quan hệ` trong Tổng quan, dùng `➡️` (output), `⬅️` (input), `ℹ️` (gián tiếp).

---

## Workflow: Test Design (Bước B — ISTQB Test Design)

**Kích hoạt:** Feature Spec đã Gate 1 (status `Done`).

1. Đọc Feature Spec đã duyệt + `test_data.md` + `environments.md` + bugs liên quan.
2. Tạo/cập nhật `test_[feature]_[mucnho].md` trong `test_suites/`, status `Draft`, TC ký hiệu `⏳`.
3. Tạo Task Spec `task_[tbb2_code].md` nếu có TBB2 liên kết — link đến HSK cha, feature group, feature specs, test suites. Giữ traceability machine-readable: `TBB2 → HSK → Task Spec → Feature Group → Feature → R/AC → Testcase`.
4. **🤝 Gate 2:** Dừng, trình bày Test Suite cho QA Lead. Chờ duyệt (`status: Testing`) trước khi đưa vào hàng đợi test.

Sau Gate 2: ghi log `[ingest]` hoặc `[task-update]` tùy trigger.

---

## Chuẩn viết Test Suite (`test_suites/`)

Dùng `tpl_test_suite.md`. Các mục bắt buộc:
- Frontmatter, Thông tin liên kết, Tổng quan coverage (bảng thống kê TC)
- Bảng Test Cases
- Blocked Coverage (TC không thể tạo do R/AC có question `Open`)
- Regression Impact
- Deprecated TC (không xóa — chỉ chuyển mục)
- `## 📅 Changelog`

**Cột bảng TC:** `Test ID | Tiêu đề | AC/Req Cover | Phạm vi | Loại case | Kỹ thuật | Pre-conditions | Các bước | Kết quả mong đợi | Nguồn | Status`

---

## Quy tắc viết Test Case

Mỗi TC bắt buộc ghi rõ:
- **AC/Req Cover:** R-ID và/hoặc AC/BDD Scenario
- **Phạm vi:** `UI` / `API` / `Functional` / `UI+Functional` / `API+Functional` / `UI+API` / `E2E`
- **Loại case:** `Positive` hoặc `Negative`
- **Kỹ thuật:** Happy Path / EP / BVA / Decision Table / State Transition / Error Guessing / Security / Regression
- **Nguồn:** `Explicit từ [nguồn]` — phải trace trực tiếp về R/AC/API Spec đã rõ

**Không sinh TC từ:** giả định, suy diễn, R/AC còn câu hỏi `Open`. API TC phải trace về API ID trong API Spec. Không tạo TC nếu không trace được về R/AC rõ ràng.

---

## Test Suite Status

| Status | Điều kiện chuyển |
|:-------|:-----------------|
| `Draft` | Mặc định khi tạo mới |
| `Testing` | **Gate 2**: `approved_by` · `approved_at` · `approval_note` đầy đủ |
| `Passed` | **Gate 4**: người dùng xác nhận kết quả thực tế |
| `Failed` | Khi có TC fail sau Gate 4 |

---

## Chuẩn viết Feature Group (`feature_groups/`)

Dùng `tpl_feature_group.md`. Các mục bắt buộc:
- Frontmatter: `tags: [qa/feature-group-index, qa/feature-group/slug]`
- Tổng quan group
- Bảng Feature Specs, bảng API Specs, bảng Test Suites
- Test Plan/Release liên quan
- Open Questions & Blocked Coverage tổng hợp
- Impact & Regression Notes
- `## 📅 Changelog`

Khi tạo group mới: cập nhật templates (tpl_requirement, tpl_api_spec, tpl_test_suite, tpl_feature_group), `index.md`, chạy `python .claude/scripts/wiki_sync.py verify`.
