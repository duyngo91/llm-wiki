---
spec: stub_qc_criteria_approval
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI, Functional]
---

# Test Suite — Duyệt / Từ chối / Mở lại tiêu chí QC cho SKU

## Phạm vi
- Source spec: [[stub_qc_criteria_approval]]
- Active requirements: 5 (R003, R004, R005, R006 — testable; R001, R002 có phần không bị block, R003-R006 fully testable)
- Blocked: 4 R/AC chờ open questions (R001 chờ Q-003, R002 chờ Q-002/Q-003, R007/AC-05 chờ Q-001/Q-002/Q-006, E2 chờ Q-004, Messages chờ Q-005)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Loại case | Kỹ thuật | Pre-conditions | Các bước | Kết quả mong đợi | Nguồn | Status |
|-------|--------|---------|-------|-----------|----------|----------------|----------|------------------|-------|--------|
| TC-APR-001 | Hiển thị danh sách tiêu chí có status Chờ duyệt | R001 | UI | Positive | Happy Path | Có ít nhất 1 tiêu chí ở status `Chờ duyệt` | 1. User có quyền duyệt vào màn quản lý danh sách tiêu chí thiết lập cho SKU. 2. Quan sát danh sách | Danh sách hiển thị các dòng status `Chờ duyệt`; các dòng có thể chọn để xử lý | Explicit từ 07105#L534-L535 (R001) | ⏳ |
| TC-APR-002 | Bulk Duyệt — tích chọn nhiều dòng + confirm Yes | R002, R003, AC-01 | Functional | Positive | Happy Path | Có ≥ 2 dòng status `Chờ duyệt` | 1. Tích chọn ≥ 2 dòng `Chờ duyệt`. 2. Click button `Duyệt`. 3. Verify dialog hiển thị nội dung MSG-APR-001. 4. Click `Yes`. | Tất cả dòng đã chọn chuyển status → `Đã duyệt` | Explicit từ 07105#L537-L542 (R003, AC-01) | ⏳ |
| TC-APR-003 | Bulk Duyệt — nội dung dialog confirm EN | R003, AC-01 | UI | Positive | Happy Path | Như TC-APR-002 bước 1-2 | 1. Tích chọn ≥ 2 dòng. 2. Click `Duyệt`. 3. Quan sát dialog | Dialog hiển thị đúng: `Do you want to confirm APPROVE setting criteria for SKUs of all selected lines?` (MSG-APR-001) | Explicit từ 07105#L540-L541 (R003) | ⏳ |
| TC-APR-004 | Bulk Từ chối — tích chọn nhiều dòng + confirm Yes | R002, R004, AC-02 | Functional | Positive | Happy Path | Có ≥ 2 dòng status `Chờ duyệt` | 1. Tích chọn ≥ 2 dòng. 2. Click button `Từ chối`. 3. Verify dialog MSG-APR-002. 4. Click `Yes`. | Các dòng đã chọn chuyển status → `Từ chối` | Explicit từ 07105#L543-L546 (R004, AC-02) | ⏳ |
| TC-APR-005 | Bulk Từ chối — nội dung dialog confirm EN | R004 | UI | Positive | Happy Path | Như TC-APR-004 bước 1-2 | 1. Tích chọn ≥ 2 dòng. 2. Click `Từ chối`. 3. Quan sát dialog | Dialog: `Do you want to confirm REJECT setting criteria for SKUs of all selected lines?` (MSG-APR-002) | Explicit từ 07105#L544-L545 (R004) | ⏳ |
| TC-APR-006 | Single Duyệt — chọn 1 dòng + confirm Yes | R005, AC-03 | Functional | Positive | Happy Path | Có 1 dòng status `Chờ duyệt` cho SKU `297500046` | 1. Click vào 1 dòng `Chờ duyệt`. 2. Click button `Duyệt`. 3. Verify dialog MSG-APR-003 chứa SKU code. 4. Click `Yes`. | Dòng chuyển status → `Đã duyệt` | Explicit từ 07105#L552-L554 (R005, AC-03) | ⏳ |
| TC-APR-007 | Single Duyệt — dialog chứa mã SKU | R005 | UI | Positive | Happy Path | Có 1 dòng `Chờ duyệt` SKU `297500046` | 1. Click dòng → `Duyệt`. 2. Quan sát dialog | Dialog chứa mã SKU: `Do you want to confirm APPROVE criteria setup for SKU 297500046?` (MSG-APR-003) | Explicit từ 07105#L553 (R005) | ⏳ |
| TC-APR-008 | Single Từ chối — chọn 1 dòng + confirm Yes | R006, AC-04 | Functional | Positive | Happy Path | Có 1 dòng status `Chờ duyệt` | 1. Click 1 dòng `Chờ duyệt`. 2. Click `Từ chối`. 3. Verify dialog MSG-APR-004. 4. Click `Yes`. | Dòng chuyển status → `Từ chối` | Explicit từ 07105#L555-L557 (R006, AC-04) | ⏳ |
| TC-APR-009 | Single Từ chối — dialog chứa mã SKU | R006 | UI | Positive | Happy Path | Có 1 dòng `Chờ duyệt` | 1. Click dòng → `Từ chối`. 2. Quan sát dialog | Dialog: `Do you want to confirm REJECT criteria setup for SKU {sku_code}?` (MSG-APR-004) | Explicit từ 07105#L556 (R006) | ⏳ |
| TC-APR-010 | Mọi action đều require confirm dialog | R003, R004, R005, R006 | Functional | Positive | Decision Table | Có dòng `Chờ duyệt` | 1. Thực hiện lần lượt 4 action: Bulk Duyệt / Bulk Từ chối / Single Duyệt / Single Từ chối. 2. Quan sát mỗi action | Mỗi action đều mở dialog confirm trước khi thực hiện; không action nào thực hiện tức thì không qua dialog | Explicit từ R003, R004, R005, R006 (Business Rule Confirm dialog) | ⏳ |
| TC-APR-011 | Transition Approve: Chờ duyệt → Đã duyệt | R003, R005 | Functional | Positive | State Transition | Dòng ở `Chờ duyệt` | 1. Duyệt (bulk hoặc single). 2. Xác nhận Yes. | Status dòng = `Đã duyệt` (Approved) | Explicit từ Business Rules — Transition Approve | ⏳ |
| TC-APR-012 | Transition Reject: Chờ duyệt → Từ chối | R004, R006 | Functional | Positive | State Transition | Dòng ở `Chờ duyệt` | 1. Từ chối (bulk hoặc single). 2. Xác nhận Yes. | Status dòng = `Từ chối` (Rejected) | Explicit từ Business Rules — Transition Reject | ⏳ |

## 🚧 Blocked Coverage

- **R007, AC-05 — Single Mở lại**: chờ Q-001 (Mở lại áp dụng từ `Đã duyệt` và/hoặc `Từ chối`?), Q-002 (có bulk Mở lại không?), Q-006 (audit history sau Mở lại). TC liên quan không thể tạo đến khi answered.
- **R001, R002 — Permission/Authorization**: chờ Q-003 (role/permission chi tiết, behavior khi non-authorized user click). TC kiểm tra unauthorized access không thể tạo.
- **E2 — Dialog No/Cancel behavior**: chờ Q-004 (hành vi khi user click `No` / đóng dialog — spec assume status không đổi nhưng chưa confirmed). TC kiểm tra Cancel dialog không thể tạo.
- **MSG-APR-001..005 — Verbatim VN**: chờ Q-005 (message VN cho 5 dialog). TC kiểm tra VN message không thể tạo.
- **MSG-APR-005 — Single Mở lại dialog**: chờ Q-001 (pre-condition trạng thái nào được Mở lại). TC kiểm tra nội dung dialog Mở lại không thể tạo.

## Regression Impact

- [[stub_qc_criteria_setup]]: thay đổi status ở approval flow ảnh hưởng state nguồn `Chờ duyệt` được tạo từ đây.
- [[stub_qc_criteria_sku]]: sau khi tiêu chí Approved → unlock flow setup SKU downstream.
- [[stub_qc_evaluation_mobile]], [[stub_qc_evaluation_manual]]: tiêu chí phải ở trạng thái Approved thì mới dùng được trong đánh giá.

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec stub_qc_criteria_approval v1.1 (Verified). 12 TC active, 5 nhóm blocked.
