---
tags: [wiki-rules, reference]
status: Done
created: 2026-05-24
---

# 📋 Quy Chuẩn Viết Tài Liệu — QA LLM Wiki

> Dùng bởi: `wiki-requirement-analyzer` (§3.1–3.2) và `wiki-test-designer` (§3.3–3.5).

---

## 3.1 Feature Spec (`features/`) — Chuẩn BA

Dùng `tpl_requirement.md`. File phải có đủ 14 mục:
1. YAML Frontmatter (tags, status, feature, project, source_version)
2. Tổng quan (Feature, Mô tả, Source, Actors, Mối quan hệ nếu có)
3. Nguồn tài liệu (bảng PDF/Link + version + status)
4. API/Interface liên quan (chỉ link → API Spec, không nhúng contract)
5. Phân rã Requirement (bảng ID, loại, priority, testable, source)
6. User Flows (Pre-conditions, Happy Path, Alt-Flows, Exc-Flows)
7. Business Rules & Data Constraints (bảng validation)
8. Error Messages Map
9. Acceptance Criteria — BDD (Given-When-Then)
10. `## ❓ Câu hỏi chưa rõ` (bảng lifecycle)
11. Thay đổi vs version cũ (bảng Add/Update/Remove/Clarify)
12. Impact Analysis & Regression Proposal
13. Test Coverage (R → TC mapping, gồm blocked)
14. `## 📅 Changelog`

---

## 3.2 API Spec (`api_specs/`) — Chuẩn Interface Contract

Dùng `tpl_api_spec.md`. File phải có: Frontmatter (`tags: [qa/api-spec]`, project, feature, feature_group), Tổng quan, API List (`API ID | Method | Endpoint | Mục đích | R/AC | Source | Status`), API Detail (auth, headers, params, request body, success/error response, side effects), `## ❓ Câu hỏi API chưa rõ`, API Test Coverage, `## 📅 Changelog`.

**Nguyên tắc:** Feature Spec = WHAT/WHY; API Spec = HOW contract. Source không đề cập API → không tạo API Spec. Không suy diễn endpoint/payload/status code/error message/side effect.

---

## 3.3 Test Suite (`test_suites/`) — Chuẩn QA

Dùng `tpl_test_suite.md`. File phải có: Frontmatter, Thông tin liên kết, Tổng quan coverage (bảng thống kê TC), Bảng Test Cases, Blocked Coverage, Regression Impact, Deprecated TC (không xóa), `## 📅 Changelog`.

**Cột bảng Test Cases:** `Test ID | Tiêu đề | AC/Req Cover | Phạm vi | Loại case | Kỹ thuật | Pre-conditions | Các bước | Kết quả mong đợi | Nguồn | Status`

---

## 3.4 Quy tắc viết Test Case

Đọc trước: Feature Spec, API Spec (nếu có), `environments.md`, `test_data.md`, bugs liên quan.

Mỗi TC bắt buộc ghi rõ:
- **AC/Req Cover:** R-ID và/hoặc AC/BDD Scenario
- **Phạm vi:** `UI` / `API` / `Functional` / `UI+Functional` / `API+Functional` / `UI+API` / `E2E`
- **Loại case:** `Positive` hoặc `Negative`
- **Kỹ thuật:** Happy Path / EP / BVA / Decision Table / State Transition / Error Guessing / Security / Regression
- **Nguồn:** `Explicit từ [nguồn]` — chỉ khi bám trực tiếp vào R/AC/API Spec đã rõ

**Không sinh TC từ:** giả định, suy diễn, hoặc R/AC còn câu hỏi `Open`. API TC phải trace về API ID trong API Spec. Không tạo TC nếu không trace được về R/AC rõ ràng.

---

## 3.5 Feature Group Page (`feature_groups/`)

Dùng `tpl_feature_group.md`. File phải có: Frontmatter (`tags: [qa/feature-group-index, qa/feature-group/slug]`), Tổng quan group, bảng Feature Specs, bảng API Specs, bảng Test Suites, Test Plan/Release liên quan, Open Questions & Blocked Coverage tổng hợp, Impact & Regression Notes, `## 📅 Changelog`.
