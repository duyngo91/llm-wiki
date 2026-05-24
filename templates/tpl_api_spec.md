---
aliases: [Tên API Spec, api-feature]
tags: [qa/api-spec, qa/feature-group/{{feature-group}}]
status: Draft
project:
feature:
feature_group: {{feature-group}}
api_spec:
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
approved_by:
approved_at:
approval_note:
---

# 🔌 API Spec: {{title}}

## Tổng quan
- **Feature liên quan:** [[wiki/{{project}}/features/{{feature-file}}|{{feature}}]]
- **Feature Group:** [[wiki/{{project}}/feature_groups/{{feature-group-file}}|{{feature-group}}]]
- **Source chính:** (ghi rõ PDF/task/API doc/answer nào, version nào)
- **Test Suite API tương ứng:** [[wiki/{{project}}/test_suites/test_{{feature-file}}_api|test_{{feature-file}}_api]]
- **Ghi chú no-inference:** Chỉ ghi contract explicit. Endpoint/method/payload/status/error chưa rõ phải đưa xuống `## ❓ Câu hỏi API chưa rõ`.

## API / Interface List
| API ID | Method | Endpoint | Mục đích | Feature R/AC | Source | Status |
|:-------|:-------|:---------|:---------|:-------------|:-------|:-------|
| API-001 | | | | R1 / AC-01 | Explicit từ ... | Draft |
| API-002 | | | | R2 / AC-02 | Chờ câu trả lời | Blocked |

## API Detail

### API-001 - {{api-name}}
- **Method:**
- **Endpoint:**
- **Auth:**
- **Headers:**
- **Path params:**
- **Query params:**
- **Request body:**
- **Success response:**
- **Error response:**
- **Validation / Business side effects:**
- **Traceability:** R1 / AC-01
- **Source:** Explicit từ ...

## ❓ Câu hỏi API chưa rõ
| Q-ID | Liên kết API/R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:------------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-API-001 | API-002 / R2 / AC-02 | | PO/BA/Dev | Open | | | |

## API Test Coverage
| API/R/AC | Test Case(s) | Status | Ghi chú |
|:---------|:-------------|:-------|:-------|
| API-001 / R1 / AC-01 | [[TC-API-001]] | ⏳ | Explicit |
| API-002 / R2 / AC-02 | | ❌ Blocked | Chờ Q-API-001 answered |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| {{date:YYYY-MM-DD HH:mm:ss}} | v1.0 | Khởi tạo API Spec | |
