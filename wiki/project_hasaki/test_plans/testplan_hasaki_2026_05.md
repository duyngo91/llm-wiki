---
aliases: [Test Plan Hasaki Tháng 5, testplan-hasaki-may-2026]
tags: [qa/test-plan]
status: Draft
project: project_hasaki
created: 2026-05-23
updated: 2026-05-23
golive_date: TBD
---

# 📋 TEST PLAN: Hasaki WMS — Tháng 5/2026

> **Kế hoạch kiểm thử tháng 5/2026 cho dự án Hasaki WMS.**
> Ngày Go-Live chưa xác định — sẽ cập nhật khi có lịch deploy chính thức.

---

## 🔍 1. Phạm vi Kiểm thử (Testing Scope)

### 1.1. Trong phạm vi kiểm thử (In-Scope)

> ⚠️ Phạm vi chính xác sẽ được xác định sau khi ingest và duyệt Feature Specs từ 2 tài liệu nguồn dưới đây.

**Tài liệu nguồn đang chờ ingest:**
- `raw_sources/project_hasaki/requirements/07062_Receiving_PO_Docs_ver2.17.pdf`
- `raw_sources/project_hasaki/requirements/07105_Quality_Control_Docs_ver1.5.pdf`

**Tính năng dự kiến (cần xác nhận sau khi phân tích specs):**
- Receiving PO — ver2.17
- Quality Control — ver1.5

**Phạm vi hồi quy (Regression Scope):**
- TBD — xác định sau khi Feature Specs được duyệt.

### 1.2. Ngoài phạm vi kiểm thử (Out-of-Scope)

- Các module WMS không thuộc 2 tài liệu trên.
- Performance testing, Load testing.

---

## 🛠️ 2. Chiến lược & Môi trường Kiểm thử

### 2.1. Thiết bị & Trình duyệt

- [ ] Web: Chrome (latest), Firefox (latest).
- [ ] Responsive Mobile: iOS, Android (nếu có giao diện web mobile).

### 2.2. Môi trường Test chính

- [[wiki/project_hasaki/operations/environments|🌐 Môi trường Test Staging/UAT]] — ⚠️ Chưa điền URL & tài khoản test, cần cập nhật trước khi chạy test.

### 2.3. Dữ liệu Test yêu cầu

- [[wiki/project_hasaki/operations/test_data|📦 Kho dữ liệu test mẫu]] — ⚠️ Chưa có data mẫu, cần chuẩn bị song song với quá trình ingest Specs.

---

## 📈 3. Test Coverage & Độ phủ kịch bản

| Module / Tính năng | Feature Spec | Test Suite | Số TC | Trạng thái |
|:-------------------|:-------------|:-----------|:------|:-----------|
| Receiving PO | _(chờ ingest)_ | _(chờ thiết kế)_ | — | ⏳ |
| Quality Control | _(chờ ingest)_ | _(chờ thiết kế)_ | — | ⏳ |

> Bảng này sẽ được điền đầy đủ sau khi `/wiki-requirement-analyzer` và `/wiki-test-designer` hoàn thành.

---

## 🏁 4. Tiêu chí dừng kiểm thử (Exit Criteria)

**Tiêu chí vào Staging (Entry Criteria):**
- [ ] Tất cả Feature Specs đã được PO/QA Lead duyệt (`status: Done`).
- [ ] Test Suites đã được QA Lead duyệt (`status: Testing`).
- [ ] Môi trường Staging và data test đã sẵn sàng.

**Tiêu chí kết thúc (Exit Criteria):**
- [ ] 100% test cases trong phạm vi đạt `✅ Pass` trên Staging.
- [ ] Không còn bug `Blocker` hoặc `Critical` tồn đọng.
- [ ] Mọi điểm mập mờ nghiệp vụ đã được BA xác nhận và cập nhật vào Specs.

---

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-23 00:00:00 | v1.0 | Khởi tạo Test Plan tháng 5/2026 — scope TBD, golive TBD | Yêu cầu QA Lead |
