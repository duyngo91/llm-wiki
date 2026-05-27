---
aliases: [QC Approval, Duyệt từ chối tiêu chí SKU]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-26
updated: 2026-05-26
feature: quality_control_approval
project: project_hasaki
source_version: "07105 ver1.5"
partial_read: false
partial_read_note: ""
approved_by:
approved_at:
approval_note:
---

# 📋 REQ: Duyệt/Từ chối thiết lập tiêu chí cho SKU

## Tổng quan
- **Mã tính năng:** quality_control_approval
- **Feature:** Approve/Reject SKU Criteria Setup
- **Mô tả ngắn:** Luồng duyệt hoặc từ chối thiết lập tiêu chí cho SKU — hỗ trợ duyệt/từ chối hàng loạt (chọn nhiều dòng) hoặc từng dòng riêng lẻ. Bao gồm action Mở lại (Reopen) để revert về Open.
- **Source chính:** `07105_Quality_Control_Docs_ver1.5.md` – section "Duyệt/Từ chối"
- **Đối tượng sử dụng (Actors):** QC Manager (người có quyền duyệt)
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** *(chưa tạo)*
- **API Spec liên quan:** N/A
- **Mối quan hệ:**
  - ⬅️ [[quality_control_sku_setup]] — Sau khi thiết lập "Yêu cầu duyệt" thì cần duyệt ở đây

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD (converted) | 07105_Quality_Control_Docs_ver1.5.md | ver1.5 | ✅ Hiện hành |

## Phân rã Requirement

### Duyệt/Từ chối hàng loạt (Bulk)
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-APR-01 | Chọn nhiều dòng có status "Chờ duyệt" → action Duyệt/Từ chối | Functional | High | ✅ | 07105#537-538 |
| R-APR-02 | Bulk Duyệt: confirm "Do you want to confirm APPROVE setting criteria for SKUs of all selected lines?" → Chọn "Yes" → trạng thái chuyển "Đã duyệt" (Approved) | Functional | High | ✅ | 07105#539-542 |
| R-APR-03 | Bulk Từ chối: confirm "Do you want to confirm REJECT setting criteria for SKUs of all selected lines?" → Chọn "Yes" → trạng thái chuyển "Từ chối" (Rejected) | Functional | High | ✅ | 07105#543-546 |

### Duyệt/Từ chối từng dòng
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R-APR-04 | Chọn vào từng dòng → vào trang chi tiết → action Duyệt | Functional | High | ✅ | 07105#547-548 |
| R-APR-05 | Duyệt đơn: confirm "Do you want to confirm APPROVE criteria setup for SKU [code]?" → Chọn "Yes" → chuyển "Đã duyệt" (Approved) | Functional | High | ✅ | 07105#552-554 |
| R-APR-06 | Từ chối đơn: confirm "Do you want to confirm REJECT criteria setup for SKU [code]?" → Chọn "Yes" → chuyển "Từ chối" (Rejected) | Functional | High | ✅ | 07105#555-557 |
| R-APR-07 | Mở lại (Reopen): confirm "Do you want to confirm RE-OPEN criteria setup for SKU [code]?" → Chọn Yes → revert trạng thái về "Open" để user cập nhật lại | Functional | High | ✅ | 07105#558-561 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- Có ít nhất 1 thiết lập SKU với status = "Chờ duyệt".
- User có quyền duyệt QC criteria.

### Luồng chuẩn (Happy Path) — Duyệt đơn
1. User vào listing Thiết lập SKU, lọc theo status "Chờ duyệt".
2. User chọn vào dòng thiết lập cần duyệt.
3. User chọn action "Duyệt" → popup confirm xuất hiện.
4. User chọn "Yes" → status chuyển "Đã duyệt" (Approved).

### Luồng rẽ nhánh (Alternative Paths)
- **Alt-Flow 1 – Bulk approve:** User tích nhiều dòng "Chờ duyệt" → action Duyệt → confirm tất cả → tất cả chuyển Approved.
- **Alt-Flow 2 – Từ chối:** User chọn action "Từ chối" → confirm → chuyển Rejected.
- **Alt-Flow 3 – Mở lại:** User chọn action "Mở lại" → confirm → chuyển về Open để cập nhật lại.

### Luồng ngoại lệ (Exception Paths)
- *(Không có exception flow explicit trong source)*

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)
| Hành động | Điều kiện | Kết quả |
|:----------|:----------|:--------|
| Duyệt | Status = Chờ duyệt | → Approved |
| Từ chối | Status = Chờ duyệt | → Rejected |
| Mở lại | Status = (từ chi tiết — ngụ ý Chờ duyệt hoặc Rejected) | → Open |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)
| Thao tác | Confirm message EN |
|:---------|:------------------|
| Bulk Duyệt | Do you want to confirm APPROVE setting criteria for SKUs of all selected lines? |
| Bulk Từ chối | Do you want to confirm REJECT setting criteria for SKUs of all selected lines? |
| Duyệt đơn | Do you want to confirm APPROVE criteria setup for SKU [code]? |
| Từ chối đơn | Do you want to confirm REJECT criteria setup for SKU [code]? |
| Mở lại | Do you want to confirm RE-OPEN criteria setup for SKU [code]? |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-APR-01: Duyệt đơn thành công**
  - **Given:** Thiết lập SKU A có status = Chờ duyệt
  - **When:** User vào chi tiết, chọn Duyệt, chọn Yes trong confirm
  - **Then:** Status chuyển thành "Đã duyệt" (Approved)

- **AC-APR-02: Bulk Từ chối**
  - **Given:** 3 thiết lập SKU có status = Chờ duyệt được tích chọn
  - **When:** User chọn action "Từ chối" → Yes trong confirm
  - **Then:** Cả 3 thiết lập chuyển status = Rejected

- **AC-APR-03: Mở lại về Open**
  - **Given:** Thiết lập SKU có status = Chờ duyệt
  - **When:** User chọn "Mở lại" → Yes
  - **Then:** Status chuyển về Open; user có thể vào cập nhật lại thiết lập

## ❓ Câu hỏi chưa rõ
| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-APR-01 | R-APR-07 | Action "Mở lại" có thể thực hiện từ status nào? Source chỉ mô tả trong context chi tiết — từ Chờ duyệt hay cả Rejected? | BA | Open | | | |

## 📝 Thay đổi so với version cũ
*(Không có changelog rõ ràng cho section này trong source)*

## Test Coverage
| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R-APR-02 / AC-APR-01 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-APR-03 / AC-APR-02 | | ❌ Chưa tạo | Chờ Gate 1 |
| R-APR-07 / AC-APR-03 | | ❌ Chưa tạo | Chờ Gate 1 |
| Q-APR-01 | | ❌ Blocked | Chờ câu trả lời |

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-26 09:00:00 | v1.0 | Khởi tạo spec từ 07105 ver1.5, section Duyệt/Từ chối | 07105#532-561 |
