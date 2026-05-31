---
spec: stub_qc_overview
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI]
---

# Test Suite — Quality Control Tổng quan, Thuật ngữ, Workflow, Wireframe

## Phạm vi
- Source spec: [[stub_qc_overview]]
- Active requirements: 1 (R004 — testable ✅)
- Blocked: 3 R/AC chờ open questions (R001 chờ Q-003/Q-004; R002 chờ Q-001; R003 chờ Q-002; All R chờ Q-005 về scope test section overview)

**Lưu ý:** Spec này là section metadata/header của doc QC. Q-005 đang mở hỏi QA Lead liệu section này có cần test suite hay không. Chỉ có R004 (Heading Yêu cầu chức năng hiện trong doc) là testable và không nằm trong Blocked Coverage.

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Loại case | Kỹ thuật | Pre-conditions | Các bước | Kết quả mong đợi | Nguồn | Status |
|-------|--------|---------|-------|-----------|----------|----------------|----------|------------------|-------|--------|
| TC-OVW-001 | Heading Yêu cầu chức năng có trong doc và dẫn vào Thiết lập tiêu chí | R004, AC-04 | UI | Positive | Happy Path | Tài liệu QC v1.5 mở | 1. Cuộn qua section `Giao diện (Wireframe)`. 2. Quan sát nội dung phía sau. | Heading `Yêu cầu chức năng` xuất hiện; bắt đầu nội dung detail từ section `Thiết lập tiêu chí` | Explicit từ 07105#L124 (R004) | ⏳ |

## 🚧 Blocked Coverage

- **R001, AC-01 — Bảng thuật ngữ**: chờ Q-003 (typo `Desciption` fix) và Q-004 (bổ sung nội dung term). TC kiểm tra nội dung bảng không thể tạo.
- **R002, AC-02 — Link Workflow Drive**: chờ Q-001 (Drive link nội dung gì, sync với doc không). TC kiểm tra link không thể tạo do chưa rõ scope.
- **R003, AC-03 — Link Wireframe Figma**: chờ Q-002 (Figma node `366-229` cover toàn bộ hay 1 màn). TC kiểm tra link Figma không thể tạo.
- **All R — Scope test section overview**: chờ Q-005 (QA Lead confirm có cần test case cho section metadata-only không). Nếu Q-005 = `N/A` thì TC-OVW-001 cũng có thể bị loại.

## Regression Impact

- Section này là gateway của toàn bộ feature group `quality_control`. Nếu section bị thay đổi (update workflow link, wireframe link, thuật ngữ mới) có thể ảnh hưởng tất cả QC stubs downstream.

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec stub_qc_overview v1.1 (Verified). 1 TC active, 4 nhóm blocked (chờ Q-005 confirm scope).
