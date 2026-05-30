---
aliases: [stub_receiving_po_concurrent]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_concurrent
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L2629-L2665
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 22:50:00"
verification_status: Verified
approved_by:
approved_at:
approval_note:
---

# REQ: stub_receiving_po_concurrent

## Tổng quan
- **Mã tính năng:** stub_receiving_po_concurrent
- **Feature:** Cho nhiều user cùng nhận PO cùng lúc
- **Mô tả ngắn:** Bổ sung cờ force cho PO để cho phép nhiều user scan nhận hàng cùng lúc. Mỗi user tạo 1 ASN riêng; hệ thống validate qty vượt và mapping theo Lô + Mã cuộn để tránh trùng. Người scan cuối (vượt qty PO) hoặc người khai báo thiếu cuối cùng là người complete PO.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** Nhân viên kho (user scan nhận), Quản lý kho (bật cờ force), hệ thống Inside (PO master).
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[test_stub_receiving_po_concurrent]]
- **API Spec liên quan:** N/A — raw không mô tả API endpoint explicit.
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_receiving_po_inbound_shipment]] (ASN model), [[stub_receiving_po_packing_list]] (Lô + Mã cuộn từ packing list).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07062_Receiving_PO_Docs_ver2.17.md | 2.17 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Raw không mô tả API explicit | N/A |

## Phân rã Requirement
| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Mỗi user scan nhận tạo 1 ASN riêng; cùng thời điểm có thể có nhiều hơn 1 ASN status `Receiving` cho cùng 1 PO | Functional | High | ✅ | 07062#L2631-L2632 |
| R002 | 1 SKU cho phép nhiều user cùng nhận | Functional | High | ✅ | 07062#L2633 |
| R003 | Bổ sung cờ force trên PO để cho phép nhiều user cùng nhận hàng — áp dụng được khi PO ở status `Open` hoặc `Receiving` | Functional | High | ✅ | 07062#L2641-L2642 |
| R004 | Button force "Cho phép nhiều người cùng nhận hàng" (Allow multiple users to receive) đặt trong Inbound detail, theo type PO | UI | High | ✅ | 07062#L2643-L2645 |
| R005 | SKU normal (không khai báo UID group): user nhận như bình thường; nếu tổng qty thực nhận từ nhiều user > qty PO thì hệ thống báo lỗi | Validation rule | High | ✅ | 07062#L2648-L2650 |
| R006 | SKU có khai báo UID group: hệ thống nhận và mapping theo `Số Lot` + `Mã cuộn` theo Packing list | Functional | High | ✅ | 07062#L2651-L2653 |
| R007 | SKU con normal: báo lỗi nếu có user nhận trùng `Số Lô` và `Mã cuộn` | Validation rule | High | ✅ | 07062#L2654 |
| R008 | SKU combo: không check realtime tại bước khai báo; báo lỗi khi user submit nếu trùng | Validation rule | High | ✅ | 07062#L2655-L2656 |
| R009 | PO có cờ force: user không bắt buộc khai báo SL thiếu sau khi nhận hết hàng vật lý — kết thúc nhận hàng như bình thường, không cần khai báo thiếu | Functional | High | ✅ | 07062#L2657-L2660 |
| R010 | Người nhận cuối có tổng SL thực nhận ≥ Qty PO sẽ là người complete PO | Functional | High | ✅ | 07062#L2661-L2662 |
| R011 | Trường hợp SL thiếu + NCC không giao lại: 1 người đại diện vào khai báo thiếu để complete PO (hiện tại không giới hạn ai khai báo) | Functional | Medium | ✅ | 07062#L2663-L2665 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- PO ở status `Open` hoặc `Receiving`.
- Quản lý kho đã bật cờ force "Allow multiple users to receive" trên Inbound detail của PO (R003, R004).

### Luồng chuẩn (Happy Path) — SKU normal có UID group
1. User A scan nhận PO, hệ thống tạo ASN A status `Receiving`.
2. User B scan nhận cùng PO, hệ thống tạo ASN B status `Receiving` riêng (R001).
3. User A khai báo nhận SKU X với Lot L1, mã cuộn C1. Hệ thống mapping theo packing list (R006).
4. User B khai báo nhận SKU X với Lot L1, mã cuộn C2 (khác cuộn) — chấp nhận.
5. Hệ thống tính total qty nhận realtime sau mỗi submit của UID group; nếu chưa vượt qty PO → tiếp tục.
6. User cuối submit khiến tổng SL thực nhận ≥ qty PO → người này là người complete PO (R010).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — SKU combo:** check không realtime. Hệ thống báo lỗi tại bước submit nếu phát hiện trùng (R008).
- **A2 — Nhận thiếu + NCC không giao lại:** 1 user đại diện vào khai báo SL thiếu để complete PO (R011). Hiện tại không kiểm soát ai khai báo.

### Luồng ngoại lệ (Exception Paths)
- **E1 — Vượt qty PO (SKU normal không UID):** tổng thực nhận từ nhiều user > qty PO → hệ thống báo lỗi (R005).
- **E2 — Trùng Lô + Mã cuộn (SKU con normal):** user nhận với Lô + mã cuộn đã có → báo lỗi (R007).
- **E3 — Trùng Lô + Mã cuộn (SKU combo):** không phát hiện realtime, báo lỗi khi submit (R008).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| `PO.force_multi_user` | flag boolean | ✅ | Mặc định OFF; chỉ được set khi PO status ∈ {`Open`, `Receiving`}; set ở Inbound detail (R003, R004). Tên field/storage chưa rõ — xem Q-001 |
| ASN per receiving session | rule | ✅ | 1 user scan = 1 ASN; cho phép nhiều ASN `Receiving` đồng thời cho cùng PO (R001) |
| Total qty validation (SKU normal) | rule | ✅ | Realtime: sum(qty thực nhận từ mọi ASN) ≤ qty PO; vượt → báo lỗi (R005) |
| UID group mapping | rule | ✅ | SKU có khai báo UID group: mapping theo `Số Lot` + `Mã cuộn` từ packing list (R006); duplicate cặp (Lô, Mã cuộn) → báo lỗi (R007/R008) |
| SKU combo check | rule | ⚠️ | Hiện không check realtime; chỉ check khi submit (R008). Có ghi chú "nếu cải tiến check được realtime lúc khai báo thì càng tốt" → cải tiến future, không phải requirement bắt buộc |
| Complete PO khi đủ qty | rule | ✅ | User submit khiến tổng SL ≥ qty PO → người này complete PO (R010) |
| Complete PO khi thiếu hàng | rule | ✅ | NCC không giao lại → 1 user đại diện khai báo thiếu để complete (R011) |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

> ⚠️ Raw không cung cấp message verbatim (VN/EN) cho các lỗi vượt qty và trùng Lô/Mã cuộn. Để verify khi clarify với BA.

| Mã lỗi | Trigger | Message VN | Message EN | Source |
|:-------|:--------|:-----------|:-----------|:-------|
| ERR-CONC-001 | Tổng qty thực nhận từ nhiều user > qty PO (SKU normal không UID) | (chưa cung cấp — Q-003) | (chưa cung cấp — Q-003) | 07062#L2648-L2650 |
| ERR-CONC-002 | User scan nhận trùng `Lô` + `Mã cuộn` (SKU con normal) | (chưa cung cấp — Q-003) | (chưa cung cấp — Q-003) | 07062#L2654 |
| ERR-CONC-003 | SKU combo submit phát hiện trùng `Lô` + `Mã cuộn` | (chưa cung cấp — Q-003) | (chưa cung cấp — Q-003) | 07062#L2655-L2656 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Bật cờ force để cho nhiều user cùng nhận**
  - **Given:** PO ở status `Open` hoặc `Receiving`.
  - **When:** Quản lý kho click button "Cho phép nhiều người cùng nhận hàng" trong Inbound detail.
  - **Then:** Cờ force được set; nhiều user có thể scan nhận đồng thời (R003, R004).
- **AC-02 — Tạo nhiều ASN cho cùng PO**
  - **Given:** PO có cờ force ON.
  - **When:** 2 user khác nhau scan nhận cùng PO.
  - **Then:** Mỗi user có ASN riêng status `Receiving`; cả 2 ASN cùng tồn tại (R001, R002).
- **AC-03 — Validate qty vượt PO (SKU normal không UID)**
  - **Given:** PO + SKU normal không khai báo UID group; tổng đã nhận từ các user = qty PO.
  - **When:** User cố nhận thêm.
  - **Then:** Hệ thống báo lỗi theo ERR-CONC-001 (R005).
- **AC-04 — Mapping Lô + Mã cuộn theo packing list**
  - **Given:** PO + SKU có khai báo UID group; packing list có Lô L1 với các Mã cuộn C1, C2, C3.
  - **When:** User A nhận C1, user B nhận C2.
  - **Then:** Cả 2 mapping thành công, lưu (Lô, Mã cuộn) đúng (R006).
- **AC-05 — Trùng Lô + Mã cuộn (SKU con normal)**
  - **Given:** User A đã nhận (L1, C1).
  - **When:** User B cố nhận (L1, C1).
  - **Then:** Hệ thống báo lỗi theo ERR-CONC-002 (R007).
- **AC-06 — Trùng Lô + Mã cuộn (SKU combo)**
  - **Given:** SKU combo; user A đã submit khai báo (L1, C1).
  - **When:** User B submit (L1, C1).
  - **Then:** Hệ thống báo lỗi tại bước submit theo ERR-CONC-003 (R008).
- **AC-07 — Người nhận cuối complete PO**
  - **Given:** Tổng SL đã nhận từ các user = qty PO - 1.
  - **When:** User Z submit lô cuối khiến tổng SL ≥ qty PO.
  - **Then:** User Z là người complete PO (R010).
- **AC-08 — Nhận thiếu khi NCC không giao lại**
  - **Given:** PO có cờ force; tổng SL thực nhận < qty PO; NCC xác nhận không giao thêm.
  - **When:** 1 user đại diện khai báo SL thiếu.
  - **Then:** PO được complete (R011); hiện tại không kiểm soát ai khai báo.

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R003 | Tên field/storage cho cờ force trên PO master? Lưu ở Inside hay WMS DB? Có log audit khi bật/tắt không? | Dev Lead | Open | | | |
| Q-002 | R003, R004 | "Type PO" trong "Button force ... type PO" có nghĩa: button hiển thị theo type PO (vd chỉ PO Normal mới có), hay là button áp dụng cho PO bất kỳ type nào (Normal/Gift/Sample)? | PO | Open | | | |
| Q-003 | R005, R007, R008 | Verbatim error messages (VN + EN) cho 3 trigger: qty vượt PO, trùng Lô + Mã cuộn SKU con normal, trùng Lô + Mã cuộn SKU combo? | PO | Open | | | |
| Q-004 | R008 | "Nếu cải tiến check được realtime lúc khai báo thì càng tốt" — câu này là wishlist phase 2 hay yêu cầu bắt buộc? | PO | Open | | | |
| Q-005 | R011 | "Hiện tại thì cho người nào khai báo cũng được" — phase 1 lỏng hay vĩnh viễn? Có role-based control trong tương lai không? | PO | Open | | | |
| Q-006 | R001, R002 | Khi có nhiều ASN `Receiving` cùng lúc, hệ thống display thế nào trên Inbound list — gom group theo PO hay list riêng? Có conflict UI không? | PO/UX | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-61 | 2.17 (stub) | 2.17 | All R + AC | Draft |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_concurrent | test_stub_receiving_po_concurrent | Add (chờ Gate 1B) | [[stub_receiving_po_inbound_shipment]] (ASN), [[stub_receiving_po_packing_list]] (Lô + Mã cuộn) | Q-001..Q-006 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R011, AC-01..AC-08 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-006 |

## 🚧 Blocked Coverage

- R003 — chờ Q-001 (storage + audit cờ force), Q-002 (scope theo PO type)
- R005, R007, R008 — chờ Q-003 (verbatim error messages)
- R008 — chờ Q-004 (realtime improvement là wishlist hay bắt buộc)
- R011 — chờ Q-005 (role-based khai báo thiếu)
- R001, R002 — chờ Q-006 (UI display nhiều ASN đồng thời)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:36:55 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 15:35:00 | v1.1 | Refine stub → full spec: 11 R-ID, 8 AC, 7 BR, 3 error messages (no verbatim), 6 questions Open. `partial_read: false`. | refine-batch-1-2026-05-30 |
