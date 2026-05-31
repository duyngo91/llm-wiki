---
aliases: [Inside Issue API, api-receiving-issue]
tags: [qa/api-spec, qa/feature-group/receiving_po]
status: Draft
project: project_hasaki
feature: stub_receiving_po_app
feature_group: receiving_po
api_spec: api_receiving_po_issue_report
created: "2026-05-31"
updated: "2026-05-31"
approved_by:
approved_at:
approval_note:
---

# 🔌 API Spec: Inside Receiving Issue Report (Unsuitable Items & Missing Qty)

## Tổng quan
- **Feature liên quan:** [[wiki/project_hasaki/features/stub_receiving_po_app|stub_receiving_po_app]]
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md#L1458-L1469 (payload structure để báo unsuitable items + missing qty)
- **Test Suite API tương ứng:** (TBD — chờ test design)
- **Ghi chú no-inference:** Raw chỉ định JSON payload structure cho 2 case (SPKPH & missing qty). Endpoint URL, HTTP method, response schema, error codes **chưa rõ** → trong Open questions. KHÔNG suy diễn.

## API / Interface List

| API ID | Method | Endpoint | Mục đích | Feature R/AC | Source | Status |
|:-------|:-------|:---------|:---------|:-------------|:-------|:-------|
| API-001 | (missing from raw) | (missing from raw) | Report unsuitable items (SPKPH) + missing qty to Inside | stub_receiving_po_app | 07062#L1458-L1469 | Draft |

## API Detail

### API-001 - Inside Receiving Issue Report

**Trigger:** User clicks "Complete PO" button after entering unsuitable items (SPKPH) or missing qty from vendor.

**Request body structure (JSON — explicit từ raw):**

Case 1: **Unsuitable items (SPKPH)**
```json
{
  "check_issue": 1,
  "issue": {
    "note": "string (optional)",
    "unsuitable": {
      "qty": "integer — số lượng sản phẩm không phù hợp",
      "media": ["array of string — ảnh/video chứng cứ"]
    }
  }
}
```

Case 2: **Missing qty from vendor (NCC không giao bù)**
```json
{
  "check_issue": 1,
  "issue": {
    "note": "string (bắt buộc — ghi lý do thiếu)"
  }
}
```

**Fields:**
- `check_issue` (integer): Set to 1 when issue detected
- `issue.note` (string): Optional for SPKPH, mandatory for missing qty
- `issue.unsuitable.qty` (integer): Count of unsuitable items
- `issue.unsuitable.media` (array[string]): Photo/video URLs (format/size limits TBD)

**Missing from raw (see Open questions):**
- **Method:** (not specified in raw)
- **Endpoint:** (not specified in raw)
- **Auth:** (not specified in raw)
- **Headers:** (not specified in raw)
- **Path params:** (not specified in raw)
- **Success response:** (not specified in raw)
- **Error response:** (not specified in raw)
- **Media validation:** (not specified in raw)
- **Side effects:** (not specified in raw)

**Traceability:** Related to stub_receiving_po_app (receiving workflow)

**Source:** Explicit từ raw L1458-L1469

---

## ❓ Câu hỏi API chưa rõ

| Q-ID | Liên kết API/R/AC | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:------------------|:--------|:-------|:-----------|
| Q-API-ISSUE-001 | API-001 | Inside API endpoint URL để submit issue? | BA/Dev (Inside team) | Open |
| Q-API-ISSUE-002 | API-001 | HTTP method (POST/PUT/PATCH)? | BA/Dev (Inside team) | Open |
| Q-API-ISSUE-003 | API-001 | Response schema khi thành công (HTTP 200)? | BA/Dev (Inside team) | Open |
| Q-API-ISSUE-004 | API-001 | Error responses: HTTP codes (400/401/403/500?) + error message format? | BA/Dev (Inside team) | Open |
| Q-API-ISSUE-005 | API-001 | Media array (unsuitable.media): accepted formats, size limits per file, max array length? | BA/Dev (Inside team) | Open |
| Q-API-ISSUE-006 | API-001 | Bao lâu Inside ACK issue? Có async callback hoặc WMS polling lại status không? | BA/Dev (Inside team) | Open |
| Q-API-ISSUE-007 | API-001 | PO ID truyền ở đâu — path param? body? header? | BA/Dev (Inside team) | Open |

---

## API Test Coverage

| API/R/AC | Test Case(s) | Status | Ghi chú |
|:---------|:-------------|:-------|:-------|
| API-001 (SPKPH case) | (TBD) | ❌ Blocked | Chờ Q-API-ISSUE-001..007 answered |
| API-001 (Missing qty case) | (TBD) | ❌ Blocked | Chờ Q-API-ISSUE-001..007 answered |

---

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-31 | v1.0 | Khởi tạo stub từ raw payload (L1458-L1469); 2 case (SPKPH + missing qty) | Wave 3 / 07062 |
