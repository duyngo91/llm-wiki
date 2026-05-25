---
aliases: [Mã-Task, Tên đồng nghĩa]
tags: [qa/requirement, qa/feature-group/{{feature-group}}]
status: Draft
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
feature: 
project: 
source_version: 
partial_read: false
partial_read_note: ""
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: {{title}}

## Tổng quan
- **Mã tính năng:** 
- **Feature:** 
- **Mô tả ngắn:** 
- **Source chính:** (ghi rõ dùng PDF/Link nào, version nào)
- **Đối tượng sử dụng (Actors):** 
- **Feature Group:** [[wiki/{{project}}/feature_groups/{{feature-group-file}}|{{feature-group}}]]
- **Test Suite tương ứng:** [[test_...]]
- **API Spec liên quan:** N/A *(chỉ tạo/link `[[wiki/{{project}}/api_specs/api_{{feature-file}}|api_{{feature-file}}]]` nếu source có API/interface explicit)*
- **Mối quan hệ:** *(Điền nếu feature này có liên kết với feature khác trong cùng project)*
  - ➡️ feature_b — *(mô tả quan hệ và link thật nếu đã có file)*
  - ⬅️ feature_a — *(mô tả quan hệ và link thật nếu đã có file)*

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | PDF | | v1.0 | ⚠️ Outdated |
| 2 | PDF | | v2.1 | ✅ Hiện hành |
| 3 | Link | [tên](url) | | ✅ Hiện hành |

## API / Interface liên quan
*Feature Spec chỉ tham chiếu API/interface. Contract chi tiết phải nằm ở `wiki/[project]/api_specs/`; nếu endpoint/method/payload/status chưa rõ thì ghi vào câu hỏi thay vì mô tả suy diễn.*

| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Không có API/interface explicit | N/A |

## Phân rã Requirement
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R1 | | Functional | High | ✅ | PDF v2.1, mục 3.1 |
| R2 | | Functional | High | ✅ | Link Figma |
| R3 | | Security | Medium | ✅ | PDF v2.1, mục 4.2 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- 

### Luồng chuẩn (Happy Path)
1. 
2. 
3. 

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1:** 
- **Alt-Flow 2:** 

### Luồng ngoại lệ (Exception Paths)
- **Exc-Flow 1:** 
- **Exc-Flow 2:** 

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Tên trường | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------|:---------|:----------|:-------------------------------|
| | | | |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
- **Lỗi bỏ trống trường bắt buộc:** `"Vui lòng nhập [Tên trường]"`
- **Lỗi định dạng sai:** `"..."`

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **Scenario 1: [Tên kịch bản]**
  - **Given:** 
  - **When:** 
  - **Then:** 

- **Scenario 2: [Tên kịch bản]**
  - **Given:** 
  - **When:** 
  - **Then:** 

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R1 / AC-01 | | PO/BA/Dev | Open | | | |
| Q-002 | R2 | | PO/BA/Dev | Open | | | |

## 📝 Thay đổi so với version cũ
| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add/Update/Remove/Clarify | | | | R1 / AC-01 | Draft |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | | | Add/Update/Deprecate/No change/Blocked by question | | |

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R1 / AC-01 | [[TC-001]] | ⏳ | Explicit |
| R2 | | ❌ Blocked | Chờ Q-002 answered |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| {{date:YYYY-MM-DD HH:mm:ss}} | v1.0 | Khởi tạo phiên bản đầu tiên | |
