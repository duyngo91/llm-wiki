---
spec: stub_qc_uid_group
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI, Functional]
---

# Test Suite — UID group: QC xã vải, Khai báo SL, Chụp hình tem QC

## Phạm vi
- Source spec: [[stub_qc_uid_group]]
- Active requirements: 7 testable (R003, R004, R005, R006, R008, R009, R010, R011 — sau khi loại các R bị block)
- Blocked: 9 nhóm chờ open questions

**Blocked analysis:**
- R001 (Q-009 scope flag), R002/R011 (Q-003 phân biệt transfer types + Q-004 scope sinh), R007 (Q-001 SL > qty + Q-008 rollback), ERR-UIG-001/002 (Q-002 verbatim), R009 (Q-005 tem Pass/Fail), R012/R013 (Q-006 nhiều Lot BOD approve + Q-007 carryover)
- Còn testable: R003, R004, R005, R006, R008, R010, R011 (phần validate F0-XV)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Loại case | Kỹ thuật | Pre-conditions | Các bước | Kết quả mong đợi | Nguồn | Status |
|-------|--------|---------|-------|-----------|----------|----------------|----------|------------------|-------|--------|
| TC-UIG-001 | Phạm vi yêu cầu đánh giá xã vải — chỉ tiêu chí có flag QC xã vải | R003, AC-02 | Functional | Positive | Happy Path | SKU có 5 tiêu chí, 2 bật `QC xã vải`. UID group chưa có yêu cầu xã vải | 1. Transfer UID group vào `F0-XV`. 2. Kiểm tra yêu cầu đánh giá được sinh. | Yêu cầu đánh giá sinh chỉ chứa 2 tiêu chí có flag `QC xã vải = true`; 3 tiêu chí còn lại không có trong yêu cầu | Explicit từ 07105#L1090-L1093 (R003) | ⏳ |
| TC-UIG-002 | Số vải còn lại 90% phải qua xã vải trước sản xuất | R004, AC-15 | Functional | Positive | Happy Path | PO sample SKU vải đánh giá Đạt → nhận 10%. Nhận 90% còn lại | 1. 90% SKU vải nhận vào kho. 2. Quan sát luồng đưa vào sản xuất. | Phải sinh yêu cầu đánh giá xã vải và Đạt trước khi đưa vào sản xuất | Explicit từ 07105#L1094-L1096 (R004) | ⏳ |
| TC-UIG-003 | App — Khai báo SL cần đánh giá — flow happy path | R005, R006, R007, AC-05 | Functional | Positive | Happy Path | Đã login App QC. UID group có SKU A qty 9500 | 1. Mở `App / Purchase order / Quality control`. 2. Scan UID group. 3. Nhập `Số lượng cần đánh giá = 500`. 4. Click `Xác nhận`. | SL được lưu; qty SKU A trong UID group còn 9000 | Explicit từ 07105#L1128-L1139 (R005, R006, R007) | ⏳ |
| TC-UIG-004 | App — SL cần đánh giá rỗng bị block | R006, AC-06 | Functional | Negative | EP (invalid) | Form khai báo SL mở | 1. Bỏ trống SL. 2. Click `Xác nhận`. | Block; ERR-UIG-001 hiển thị | Explicit từ 07105#L1133-L1134 (R006) | ⏳ |
| TC-UIG-005 | App — SL cần đánh giá = 0 bị block | R006, AC-07 | Functional | Negative | BVA | Form mở | 1. Nhập `0`. 2. Click `Xác nhận`. | Block; ERR-UIG-001 | Explicit từ 07105#L1133-L1134 (R006) | ⏳ |
| TC-UIG-006 | App — SL cần đánh giá là số thập phân bị block | R006, AC-08 | Functional | Negative | EP (invalid) | Form mở | 1. Nhập `0.5`. 2. Click `Xác nhận`. | Block; ERR-UIG-001 | Explicit từ 07105#L1133-L1134 (R006) | ⏳ |
| TC-UIG-007 | App — SL cần đánh giá là số âm bị block | R006, AC-09 | Functional | Negative | BVA | Form mở | 1. Nhập `-10`. 2. Click `Xác nhận`. | Block; ERR-UIG-001 | Explicit từ 07105#L1133-L1134 (R006) | ⏳ |
| TC-UIG-008 | App — SL cần đánh giá hiển thị trong phần thông tin chung | R008, AC-10 | UI | Positive | Happy Path | UID group đã khai báo SL = 500 | 1. Xem UID group trong phần thông tin chung. | Field `Số lượng cần đánh giá = 500` hiển thị | Explicit từ 07105#L1140 (R008) | ⏳ |
| TC-UIG-009 | App — Sau hoàn thành đánh giá → bước chụp hình tem QC | R009, R010, AC-11 | Functional | Positive | Happy Path | QC đã đánh giá xong tất cả tiêu chí của SKU | 1. User nhấn `Hoàn thành`. | Hệ thống mở bước chụp hình tem QC Pass/Fail | Explicit từ 07105#L1141-L1145 (R009) | ⏳ |
| TC-UIG-010 | App — Chụp 1 hình tem QC + lưu | R009, R010, AC-12 | Functional | Positive | Happy Path | Bước chụp hình mở | 1. Chụp 1 hình. 2. Click `Lưu`. | Hình tem QC được ghi nhận; hoàn thành đánh giá | Explicit từ 07105#L1141-L1147 (R009, R010) | ⏳ |
| TC-UIG-011 | App — Skip chụp hình tem QC bị block | R010, AC-13 | Functional | Negative | Error Guessing | Bước chụp hình mở | 1. Cố thoát mà chưa chụp hình. | Block; ERR-UIG-002 hiển thị | Explicit từ 07105#L1146-L1147 (R010) | ⏳ |
| TC-UIG-012 | Transfer F0-XV — UID group đã Đạt xã vải → bỏ qua sinh yêu cầu | R011, AC-03 | Functional | Positive | State Transition | UID group X đã có yêu cầu xã vải kết quả Đạt | 1. Transfer X vào F0-XV lần 2. | Hệ thống bỏ qua; không sinh yêu cầu mới | Explicit từ 07105#L1153-L1158 (R011) | ⏳ |
| TC-UIG-013 | Transfer F0-XV — UID group chưa có yêu cầu → tự sinh | R011, AC-02 | Functional | Positive | State Transition | UID group Y chưa có yêu cầu xã vải | 1. Transfer Y vào F0-XV. | Hệ thống sinh yêu cầu đánh giá xã vải cho các tiêu chí có flag QC xã vải | Explicit từ 07105#L1153-L1158 (R011) | ⏳ |

## 🚧 Blocked Coverage

- **R001 — Scope flag QC xã vải**: chờ Q-009 (áp dụng tất cả tiêu chí hay chỉ cate Thời trang NVL). TC verify scope flag không thể tạo.
- **R002, R011 — Phân biệt transfer types**: chờ Q-003 (transfer location / transfer bin / transfer bin cart / transfer vị trí UID group — 4 loại hay alias). TC per transfer type không thể tạo.
- **R002, R011 — Scope sinh yêu cầu (1 yêu cầu / SKU hay / UID group)**: chờ Q-004. TC scope không thể tạo.
- **R007 — SL cần đánh giá > qty**: chờ Q-001 (hệ thống chặn không? verbatim message?). TC BVA SL > qty không thể tạo.
- **R007 — Rollback SL**: chờ Q-008. TC rollback không thể tạo.
- **ERR-UIG-001, ERR-UIG-002 — Verbatim VN+EN**: chờ Q-002. TC kiểm tra exact message không thể tạo.
- **R009 — Tem QC Pass/Fail**: chờ Q-005 (2 loại tem riêng hay 1 tem 2 trạng thái). TC kiểm tra loại tem không thể tạo.
- **R012, R013, AC-14 — Tiêu chí PO chính theo PO sample BOD**: chờ Q-006 (nhiều Lot BOD approve khác nhau → dùng điều kiện nào) và Q-007 (carryover sang PO sau). TC không thể tạo.
- **R013 — BOD approve Lot: điều kiện điều chỉnh**: chờ Q-006. TC cụ thể không thể tạo.

## Regression Impact

- [[stub_qc_criteria_setup]]: Flag `QC xã vải` được set khi tạo/cập nhật tiêu chí.
- [[stub_qc_evaluation_mobile]]: App flow đánh giá UID group.
- [[stub_qc_evaluation_result]]: Field `Đánh giá đạt` của UID group.
- [[stub_receiving_po_fabric]]: UID group cho SKU vải là nguồn cho xã vải.

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec stub_qc_uid_group v1.2 (Verified). 13 TC active, 9 nhóm blocked.
