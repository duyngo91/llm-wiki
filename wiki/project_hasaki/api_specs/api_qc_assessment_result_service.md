---
aliases: [QC Result Service, api-qc-result]
tags: [qa/api-spec, qa/feature-group/quality_control]
status: Draft
project: project_hasaki
feature: stub_qc_evaluation_result
feature_group: quality_control
api_spec: api_qc_assessment_result_service
created: "2026-05-31"
updated: "2026-05-31"
approved_by:
approved_at:
approval_note:
---

# 🔌 API Spec: QC Assessment Result Service (WMS Internal)

## Tổng quan
- **Feature liên quan:** [[wiki/project_hasaki/features/stub_qc_evaluation_result|stub_qc_evaluation_result]]
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Source chính:** 07105_Quality_Control_Docs_ver1.5.md#L649-L658 (architectural service description)
- **Test Suite API tương ứng:** (TBD — chờ test design)
- **Ghi chú no-inference:** Raw mô tả architectural intent (aggregate QC results từ nhiều source). **Chi tiết kỹ thuật hầu như không có** (endpoint, method, schema, persistence). KHÔNG suy diễn implementation → Open questions rất nhiều.

## API / Interface List

| API ID | Method | Endpoint | Mục đích | Feature R/AC | Source | Status |
|:-------|:-------|:---------|:---------|:-------------|:-------|:-------|
| API-003 | TBD | TBD (WMS internal service?) | Persist QC assessment results; aggregate multi-source evaluations per VAS + Group UID | stub_qc_evaluation_result | 07105#L649-L658 | Draft |

## API Detail

### API-003 - QC Assessment Result Service

**Architectural intent (từ raw L649-658):**

Raw describes:
> "Dựng 1 service để ghi nhận kết quả đánh giá để sau này nhận thông tin từ nhiều nguồn đánh giá khác nhau
> => WMS ghi nhận kết quả cuối cùng
> 
> VAS_ID + Group UID sẽ gắn với từng Service
> Mỗi service gồm các thông tin gồm:
> • Group UID
> • Mã tiêu chí
> • Kết quả
> => mỗi service được hiểu như 1 kết quả đánh giá của 1 group UID"

**Conceptual data structure:**
- `VAS_ID`: identifier linking to VAS record
- `Group_UID`: identifier for product group/batch
- `Criteria_Code`: QC criterion (e.g., color, size, packaging)
- `Result`: evaluation outcome (Pass/Fail/Review?)

**Purpose:** Aggregate assessments from multiple evaluation channels (manual QC, automated inspection, 3rd-party verification) into single WMS source-of-truth per VAS + Group UID.

**Missing from raw (almost all technical detail — see Open questions):**
- **Service type:** (not specified in raw)
- **Method:** (not specified in raw)
- **Endpoint:** (not specified in raw)
- **Auth:** (not specified in raw)
- **Headers:** (not specified in raw)
- **Request body schema:** (conceptual only: VAS_ID, Group_UID, Criteria_Code, Result; format not in raw)
- **Success response:** (not specified in raw)
- **Error response:** (not specified in raw)
- **Persistence:** (not specified in raw)
- **Query API:** (not specified in raw)
- **Integration:** (not specified in raw)
- **Aggregation logic:** (not specified in raw)

**Traceability:** Related to stub_qc_evaluation_result (QC result persistence)

**Source:** Explicit từ raw L649-L658 (architectural description only)

---

## ❓ Câu hỏi API chưa rõ

| Q-ID | Liên kết API/R/AC | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:------------------|:--------|:-------|:-----------|
| Q-API-QC-001 | API-003 | Is this a REST API service, microservice, message queue consumer, or internal WMS function? | BA/Architect | Open |
| Q-API-QC-002 | API-003 | If REST: endpoint URL? | BA/Dev | Open |
| Q-API-QC-003 | API-003 | HTTP method (POST/PUT/PATCH)? | BA/Dev | Open |
| Q-API-QC-004 | API-003 | Request body schema — what fields are required vs optional? | BA/Dev | Open |
| Q-API-QC-005 | API-003 | Response schema (HTTP 200) — return full result document or just ACK? | BA/Dev | Open |
| Q-API-QC-006 | API-003 | Error handling: HTTP codes + error message format? Validation errors for duplicate Group_UID + Criteria_Code? | BA/Dev | Open |
| Q-API-QC-007 | API-003 | Persistence mechanism — which database/store holds results? | BA/Architect | Open |
| Q-API-QC-008 | API-003 | How to query/retrieve stored results? Separate GET endpoint? | BA/Dev | Open |
| Q-API-QC-009 | API-003 | Integration with external QC sources (manual, 3rd-party labs) — how do they submit results? | BA/Architect | Open |
| Q-API-QC-010 | API-003 | Aggregation logic: if multiple results for same VAS + Group_UID, which one takes precedence? | BA/Product | Open |

---

## API Test Coverage

| API/R/AC | Test Case(s) | Status | Ghi chú |
|:---------|:-------------|:-------|:-------|
| API-003 (baseline) | (TBD) | ❌ Blocked | Chờ Q-API-QC-001..010 answered; almost no technical spec in raw |

---

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-31 | v1.0 | Khởi tạo stub từ raw architectural description (L649-L658); conceptual data structure only | Wave 3 / 07105 |
