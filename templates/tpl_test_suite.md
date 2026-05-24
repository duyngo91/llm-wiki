---
aliases: [Mã-Test-Suite, Tên viết tắt]
tags: [qa/test-suite, qa/feature-group/{{feature-group}}]
status: Draft
feature: 
requirement: 
api_spec:
dev: 
qa: 
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
approved_by:
approved_at:
approval_note:
---

# 🧪 Test Suite: {{title}}

- **Feature liên quan:** [[...]]
- **Feature Group:** [[wiki/{{project}}/feature_groups/{{feature-group-file}}|{{feature-group}}]]
- **Requirement:** [[REQ ...]]
- **API Spec liên quan:** N/A *(nếu suite có phạm vi API thì link `[[wiki/{{project}}/api_specs/api_{{feature-file}}|api_{{feature-file}}]]`)*
- **Dev phụ trách:** 
- **QA phụ trách:** 
- **Ngày cập nhật cuối:** {{date:YYYY-MM-DD}}

## 📊 Tổng quan Test Coverage
| Loại Test | Số lượng TC | Pass | Fail | Blocked | Chưa test |
|:----------|:-----------|:-----|:-----|:--------|:----------|
| Happy Path | | | | | |
| Negative | | | | | |
| Boundary | | | | | |
| API Contract | | | | | |
| API Negative | | | | | |
| Security | | | | | |
| Performance | | | | | |
| **Tổng** | | | | | |

## ✅ Test Cases
*Chỉ giữ dòng API khi `API Spec liên quan` có link thật và API contract explicit. Nếu API chưa rõ, chuyển sang `Blocked Coverage`.*

| Test ID | Tiêu đề | AC/Req Cover | Phạm vi | Loại case | Kỹ thuật test | Điều kiện tiên quyết | Các bước thực hiện | Kết quả mong đợi | Nguồn | Status |
|:--------|:--------|:-------------|:--------|:----------|:--------------|:--------------------|:-------------------|:-----------------|:------|:-------|
| TC-001 | | AC-01 / R1 | Functional | Positive | Happy Path | | 1. ...  2. ... | | Explicit từ Feature Spec | ⏳ |
| TC-002 | | AC-02 / R2 | UI | Negative | Equivalence Partitioning | | 1. ...  2. ... | | Explicit từ Business Rule | ⏳ |
| TC-003 | | AC-03 / R3 | UI+Functional | Negative | Boundary Value Analysis | | 1. ...  2. ... | | Explicit từ Requirement R3 | ⏳ |
| TC-API-001 | | API-001 / R1 / AC-01 | API | Positive | Contract Testing | | 1. Gửi request theo API Spec 2. Kiểm tra response | | Explicit từ API Spec | ⏳ |

## 🚧 Blocked Coverage
*Requirement/AC/API chưa được sinh test case vì còn câu hỏi Open hoặc thiếu nguồn explicit.*

| Requirement/AC | Lý do blocked | Question ID | Cần ai trả lời | Trạng thái |
|:---------------|:--------------|:------------|:---------------|:-----------|
| R4 / AC-04 | Chưa rõ expected result | Q-001 | PO/BA/Dev | Open |
| API-002 / R2 / AC-02 | Chưa rõ status code/payload/error response | Q-API-001 | PO/BA/Dev | Open |

## 🔁 Regression Impact
*Khi requirement/task thay đổi, ghi rõ test case cũ cần chạy lại và lý do.*

| Change ID / Source | Test Case(s) cần regression | Lý do | Ưu tiên | Ghi chú |
|:-------------------|:----------------------------|:------|:--------|:-------|
| CHG-001 | TC-001 | Flow chính bị ảnh hưởng | High | |

## 🚫 Test Cases Lỗi Thời (Deprecated)
*Các test case không còn áp dụng do thay đổi requirement. Lưu lại để tham khảo.*

| Test ID | Tiêu đề | Lý do deprecated | Ngày | Nguồn |
|:--------|:--------|:-----------------|:-----|:------|
| | | | | |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| {{date:YYYY-MM-DD HH:mm:ss}} | v1.0 | Khởi tạo Test Suite | |
