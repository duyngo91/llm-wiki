---
aliases: [Inside PO Status Sync, api-receiving-status]
tags: [qa/api-spec, qa/feature-group/receiving_po]
status: Draft
project: project_hasaki
feature: stub_receiving_po_app
feature_group: receiving_po
api_spec: api_receiving_po_update_status
created: "2026-05-31"
updated: "2026-05-31"
approved_by:
approved_at:
approval_note:
---

# 🔌 API Spec: Inside PO Status Update (Complete PO → Receiving/Received)

## Tổng quan
- **Feature liên quan:** [[wiki/project_hasaki/features/stub_receiving_po_app|stub_receiving_po_app]]
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md#L880-L881, L1447 (mention "Gọi API đồng bộ status Received lên Inside")
- **Test Suite API tương ứng:** (TBD — chờ test design)
- **Ghi chú no-inference:** Raw mention trigger và status value ("Received" enum). Request/response schema, endpoint, method **chưa rõ** → Open questions. KHÔNG suy diễn từ "implied POST".

## API / Interface List

| API ID | Method | Endpoint | Mục đích | Feature R/AC | Source | Status |
|:-------|:-------|:---------|:---------|:-------------|:-------|:-------|
| API-002 | TBD | TBD | Sync PO status (Receiving → Received) to Inside after delivery documents complete | stub_receiving_po_app | 07062#L880-881, L1447 | Draft |

## API Detail

### API-002 - Inside PO Status Update

**Trigger:** User clicks "Complete PO" button → WMS has finished receiving and updating all delivery documents (ASN, Invoice, etc.)

**Business context (từ raw):**
- Trigger point: "Khi user hoàn tất bước nhập hàng (update documents)" → "Gọi API đồng bộ status Received lên Inside" (L1447)
- Status transition: PO status ở WMS thay đổi từ `Receiving` → `Received`
- Note: Raw có câu "Lưu ý khi này chưa gọi API" (L880) → indication API chưa được implement ở thời điểm raw viết

**Status enum (từ raw L879-881):**
```
Inside PO status: Verified → Open → Receiving → Received → Canceled
WMS ← mapping → Inside status
```

**Missing from raw (see Open questions):**
- **Method:** (not specified in raw)
- **Endpoint:** (not specified in raw)
- **Auth:** (not specified in raw)
- **Headers:** (not specified in raw)
- **Path params:** (not specified in raw)
- **Request body schema:** (not specified in raw)
- **Success response:** (not specified in raw)
- **Error response:** (not specified in raw)
- **Idempotency:** (not specified in raw)
- **Side effects:** (not specified in raw)

**Traceability:** Related to stub_receiving_po_app (Complete PO flow)

**Source:** Explicit từ raw L880-881 (mention) + L1447 (trigger description)

---

## ❓ Câu hỏi API chưa rõ

| Q-ID | Liên kết API/R/AC | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:------------------|:--------|:-------|:-----------|
| Q-API-STATUS-001 | API-002 | Inside API endpoint URL? | BA/Dev (Inside team) | Open |
| Q-API-STATUS-002 | API-002 | HTTP method (POST/PUT/PATCH)? | BA/Dev (Inside team) | Open |
| Q-API-STATUS-003 | API-002 | Request body schema — chỉ status? hay gồm PO details khác? | BA/Dev (Inside team) | Open |
| Q-API-STATUS-004 | API-002 | Response schema (HTTP 200)? | BA/Dev (Inside team) | Open |
| Q-API-STATUS-005 | API-002 | Error handling: HTTP codes + error message format? | BA/Dev (Inside team) | Open |
| Q-API-STATUS-006 | API-002 | PO ID truyền ở đâu (path param / body / header)? | BA/Dev (Inside team) | Open |
| Q-API-STATUS-007 | API-002 | Idempotent? Gọi lại API same PO multiple times có safe không? | BA/Dev (Inside team) | Open |
| Q-API-STATUS-008 | API-002 | Synchronous hay asynchronous? WMS chờ response hay fire-and-forget? | BA/Dev (Inside team) | Open |

---

## API Test Coverage

| API/R/AC | Test Case(s) | Status | Ghi chú |
|:---------|:-------------|:-------|:-------|
| API-002 (Receiving → Received) | (TBD) | ❌ Blocked | Chờ Q-API-STATUS-001..008 answered |
| API-002 (Error case) | (TBD) | ❌ Blocked | Chờ Q-API-STATUS-005 answered |

---

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-31 | v1.0 | Khởi tạo stub từ raw mention (L880-881, L1447); trigger + status enum documented | Wave 3 / 07062 |
