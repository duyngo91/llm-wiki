---
tags: [wiki-rules, reference]
status: Done
updated: 2026-05-30
---

# Phase: Test Design

> Dùng bởi: `/wiki-test-designer` — thiết kế Test Suite từ Feature Spec đã được Gate 1 duyệt.
> Naming/Tags/Status/Gates: [`shared.md`](shared.md).

---

## Điều kiện tiên quyết

**Phải có Gate 1 trước:** Feature Spec status `Done` với đủ `approved_by`, `approved_at`, `approval_note` trong frontmatter.

**Lint test suite:** Format/structure check qua `py .claude/scripts/wiki_sync.py verify`. **Không** chạy `hasaki-spec-verifier` — test case trace về R/AC đã được Gate 1 duyệt, không phải claim mới về raw.

---

## Workflow: Test Design (ISTQB Test Design)

**Kích hoạt:** Feature Spec đã Gate 1 (status `Done`).

1. Đọc Feature Spec đã duyệt + `test_data.md` + `environments.md` + bugs liên quan.
2. Tạo/cập nhật `test_[feature]_[mucnho].md` trong `test_suites/`, status `Draft`, TC ký hiệu `⏳`.
3. Tạo Task Spec `task_[tbb2_code].md` nếu có TBB2 liên kết — link đến HSK cha, feature group, feature specs, test suites. Traceability machine-readable: `TBB2 → HSK → Task Spec → Feature Group → Feature → R/AC → Testcase`.
4. **Gate 2:** Dừng, trình bày Test Suite cho QA Lead. Chờ duyệt (`status: Testing`) trước khi đưa vào hàng đợi test.

Sau Gate 2: ghi log `[ingest]` hoặc `[task-update]` tùy trigger.

---

## Task Spec stub

Khi task chưa đủ source để viết task_spec đầy đủ, cho phép tạo stub để giữ traceability ngay. Stub bắt buộc tối thiểu:
- `tbb2_code`, `hsk_parent`
- link raw HSK source
- link feature specs liên quan (nếu đã có)
- trạng thái blocked rõ ràng nếu chưa đủ source

Stub task_spec là `trace-ready`, **không** `execution-ready`. Trước khi task vào execution-ready, refine thành bản đầy đủ với:
- clear scope và affected features
- explicit links đến feature spec requirements (R/AC)
- blocked/open-question status nơi source chưa rõ

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

**Không sinh TC từ:** giả định, suy diễn, R/AC còn câu hỏi `Open`. API TC phải trace về API ID trong API Spec.

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

Khi tạo group mới: cập nhật templates (tpl_requirement, tpl_api_spec, tpl_test_suite, tpl_feature_group), `index.md`, chạy `py .claude/scripts/wiki_sync.py verify`.
