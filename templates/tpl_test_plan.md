---
aliases: [Mã-Test-Plan, Kế hoạch test Sprint-x]
tags: [qa/test-plan]
status: Draft       # Draft | Testing | Passed | Outdated
project: 
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
---

# 📋 TEST PLAN: {{title}}

> **Kế hoạch kiểm thử:** Định hình phạm vi, chiến lược, môi trường, dữ liệu kiểm thử và tiêu chí đạt chất lượng (Exit Criteria) cho đợt kiểm thử này.

---

## 🔍 1. Phạm vi Kiểm thử (Testing Scope)

### 1.1. Trong phạm vi kiểm thử (In-Scope)
- **Các tính năng kiểm thử mới / thay đổi:**
  - [[wiki/features/feature_name|Feature Name]] — Mô tả nghiệp vụ thay đổi.
- **API Specs liên quan nếu có:**
  - [[wiki/api_specs/api_feature_name|API Feature Name]] — Chỉ đưa vào scope khi API contract có nguồn explicit.
- **Phạm vi kiểm thử hồi quy (Regression Scope):**
  - [[wiki/features/related_feature|Related Feature]] — Module bị ảnh hưởng cần test lại.

### 1.1.1. Change Impact & Regression Matrix

| Change ID / Source | Feature | API Spec | Test Suite | Added TC | Updated TC | Deprecated TC | Regression TC | Open questions |
|:-------------------|:--------|:---------|:-----------|:---------|:-----------|:--------------|:--------------|:---------------|
| | | | | | | | | |

### 1.2. Ngoài phạm vi kiểm thử (Out-of-Scope)
- **Những phần tạm thời không kiểm thử (và lý do):**
  - ...

---

## 🛠️ 2. Chiến lược & Môi trường Kiểm thử

### 2.1. Thiết bị & Trình duyệt
- [ ] Web: Chrome, Firefox, Safari (Responsive Mobile).
- [ ] Mobile App: iOS 17+, Android 14+.

### 2.2. Môi trường Test chính
- [[wiki/operations/environments|🌐 Cấu hình Môi trường Test Staging/UAT]]

### 2.3. Dữ liệu Test yêu cầu (Test Data Required)
- [[wiki/operations/test_data|📦 Kho dữ liệu test mẫu]]
- Dữ liệu chi tiết: ...

---

## 📈 3. Test Coverage & Độ phủ kịch bản
| Module / Yêu cầu / API | API Spec | Test Suite tương ứng | Số kịch bản | Blocked coverage | Trạng thái kịch bản |
|:-----------------------|:---------|:---------------------|:------------|:-----------------|:-------------------|
| | [[wiki/api_specs/api_xxx|API XXX]] | [[wiki/test_suites/test_xxx|Test Suite XXX]] | | | ⏳ |

---

## 🏁 4. Tiêu chí dừng kiểm thử (Exit Criteria)
- [ ] 100% các kịch bản test thuộc phạm vi đạt trạng thái **`✅ Pass`** trên Staging.
- [ ] Không còn tồn đọng lỗi nghiêm trọng (`Blocker`, `Critical`, `Major`).
- [ ] Mọi mâu thuẫn nghiệp vụ phát sinh đã được làm rõ và cập nhật vào Specs.

---

## 📅 Changelog
| Thời gian | Version | Nội dung thay đổi | Người thực hiện |
|:----------|:--------|:------------------|:----------------|
| {{date:YYYY-MM-DD HH:mm:ss}} | v1.0 | Khởi tạo Kế hoạch kiểm thử (Test Plan). | QA_Lead |
