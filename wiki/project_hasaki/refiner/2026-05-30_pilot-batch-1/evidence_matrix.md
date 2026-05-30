# Evidence Matrix — pilot-batch-1 (2026-05-30)

> Verify mode: Spec-scoped. 5 specs. 128 claims (47 R + 36 AC + 32 BR + 13 MSG) + 29 Q Open.

## stub_receiving_po_po_sample (07062 S-60, v2.17)

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| 07062#L2582-L2584 | R001 — PO type `Sample` (tương tự Gift) phục vụ QC | SUPPORTED | Keep |
| 07062#L2585 | R002 — Liên kết 2 chiều PO Sample ↔ gốc | SUPPORTED | Keep |
| 07062#L2587-L2589 | R003 — PO Sample nhận trước + QC trước; PO gốc chưa nhận giai đoạn này | SUPPORTED | Keep |
| 07062#L2590 | R004 — QC luồng thông thường | SUPPORTED | Keep |
| 07062#L2591 | R005 — Phase 1 tiêu chí Sample = gốc | SUPPORTED | Keep |
| 07062#L2595-L2598 | R006 — Block nhận gốc nếu Sample chưa Completed/QC Failed | SUPPORTED | Keep |
| 07062#L2599-L2606 | R007 — Thông báo VN+EN khi block | SUPPORTED (verbatim VN+EN match raw) | Keep |
| 07062#L2607-L2610 | R008 — Lần đầu nhận PO chính max 30% + auto request QC | SUPPORTED | Keep |
| 07062#L2611-L2613 | R009 — UID `Received` → `Inbin` sau QC (passed/failed) | SUPPORTED | Keep |
| 07062#L2614 | R010 — QC failed: không nhận phần còn lại, trả NCC | SUPPORTED | Keep |
| 07062#L2615-L2617 | R011 — QC passed: `Đánh giá đạt = No`, chỉ transfer nội kho, không IT | SUPPORTED (raw "chỉ được transfer, không cho IT" — spec interpret "transfer nội kho" — đồng nghĩa) | Keep |
| 07062#L2618-L2624 | R012 — Làm tròn lên (ceil) 30% packing list + message verbatim VN+EN | SUPPORTED | Keep |
| AC-01..AC-07 derived from R001-R012 | All SUPPORTED | Keep |
| BR table (7 rules) | Mapped to R001-R012 | All SUPPORTED | Keep |
| ERR-POS-001, ERR-POS-002 | Verbatim VN+EN match raw | SUPPORTED | Keep |
| 6 Questions (Q-001..Q-006) | Open, đúng phạm vi | N/A | Track to Gate 1B |

## stub_receiving_po_concurrent (07062 S-61, v2.17)

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| 07062#L2631-L2632 | R001 — 1 user scan = 1 ASN; nhiều ASN `Receiving` đồng thời cho cùng PO | SUPPORTED | Keep |
| 07062#L2633 | R002 — 1 SKU cho nhiều user cùng nhận | SUPPORTED | Keep |
| 07062#L2641-L2642 | R003 — Cờ force trên PO; apply khi PO `Open` hoặc `Receiving`. Raw có typo "nhiều PO cùng nhận" — spec interpret "nhiều user" (đúng context) | SUPPORTED (raw L2641 typo `PO` → `user`, spec corrective but trivial — không cần Q riêng vì context và L2643 "Cho phép nhiều người cùng nhận" rõ ràng) | Keep |
| 07062#L2643-L2645 | R004 — Button "Cho phép nhiều người cùng nhận hàng" / "Allow multiple users to receive" trong Inbound detail, type PO | SUPPORTED | Keep |
| 07062#L2648-L2650 | R005 — SKU normal không UID: tổng qty > qty PO → báo lỗi | SUPPORTED (raw typo "nêu" → spec "nếu") | Keep |
| 07062#L2651-L2653 | R006 — SKU UID group: mapping theo Lot + Mã cuộn theo Packing list | SUPPORTED | Keep |
| 07062#L2654 | R007 — SKU con normal: trùng Lô + Mã cuộn → báo lỗi | SUPPORTED | Keep |
| 07062#L2655-L2656 | R008 — SKU combo: không realtime, báo lỗi khi submit | SUPPORTED | Keep |
| 07062#L2657-L2660 | R009 — Cờ force: không bắt buộc khai báo thiếu, kết thúc bình thường | SUPPORTED (raw "bthường" → spec "bình thường") | Keep |
| 07062#L2661-L2662 | R010 — Người submit cuối có total ≥ qty PO → complete PO | SUPPORTED | Keep |
| 07062#L2663-L2665 | R011 — Thiếu hàng + NCC không giao lại: 1 user đại diện khai báo | SUPPORTED (raw "dại diện" / "htại" → spec sửa typo) | Keep |
| AC-01..AC-08 | Derived from R001-R011 | All SUPPORTED | Keep |
| BR table (7 rules) | Mapped | All SUPPORTED | Keep |
| ERR-CONC-001/-002/-003 | Verbatim chưa cung cấp (Q-003 captured) — spec không claim verbatim | SUPPORTED (proper Q handling) | Keep |
| 6 Questions (Q-001..Q-006) | Open | N/A | Track to Gate 1B |

## stub_qc_criteria_approval (07105 S-13, v1.5)

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| 07105#L534-L535 | R001 — Màn quản lý hiển thị status `Chờ duyệt` | SUPPORTED | Keep |
| 07105#L536-L547 | R002 — 2 phương thức: bulk + single | SUPPORTED | Keep |
| 07105#L537-L542 | R003 — Bulk Duyệt: confirm dialog → `Yes` → `Đã duyệt` | SUPPORTED | Keep |
| 07105#L543-L546 | R004 — Bulk Từ chối → `Từ chối` | SUPPORTED | Keep |
| 07105#L552-L554 | R005 — Single Duyệt với SKU code | SUPPORTED | Keep |
| 07105#L555-L557 | R006 — Single Từ chối với SKU code | SUPPORTED | Keep |
| 07105#L558-L561 | R007 — Single Mở lại revert `Open` | SUPPORTED | Keep |
| AC-01..AC-05 | Derived from R001-R007 | All SUPPORTED | Keep |
| BR table (6 rules) | Status enum + transitions | All SUPPORTED | Keep |
| MSG-APR-001..005 (5 confirm dialogs) | EN verbatim từ raw L540-L541, L544-L545, L553, L556, L559 — match exact | SUPPORTED | Keep |
| 6 Questions (Q-001..Q-006) | Open | N/A | Track to Gate 1B |

## stub_receiving_po_gift (07062 S-34 + S-35, v2.17)

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| 07062#L1740-L1742 | R001 — Case 1 gốc + 1 gift: nhận chung nếu scan gốc trước | SUPPORTED | Keep |
| 07062#L1743-L1744 | R002 — Case 1 gốc + 1 gift: nhận riêng PO gift | SUPPORTED (spec thêm "không qua PO gốc" — interpret từ context) | Keep |
| 07062#L1745-L1751 | R003 — Case nhiều gift: thông báo VN+EN, hoàn thành tất cả gift trước | SUPPORTED (verbatim VN+EN match) | Keep |
| 07062#L1752-L1753 | R004 — Scan từng PO gift đến hoàn thành, sau đó scan gốc | SUPPORTED | Keep |
| 07062#L1755-L1756 | **R005 — Override khi PO gift chưa đủ điều kiện** | **⚠️ UNCLEAR** | **FIX-001 (add Q-007)** |
| 07062#L1757-L1758 | R006 — Gift thiếu hàng: lần đầu nhận chung; lần sau bắt buộc riêng | SUPPORTED | Keep |
| AC-01..AC-07 | Derived from R001-R006 (AC-05 dùng R005 nên cần update theo FIX-001) | SUPPORTED (logic chuẩn theo spec interpretation) | Keep + AC-05 reference Q-007 |
| BR table (6 rules) | Mapped | All SUPPORTED | Keep |
| ERR-GIFT-001 | Verbatim VN+EN match L1748-L1751 | SUPPORTED | Keep |
| 5 Questions (Q-001..Q-005) + 1 mới (Q-007 từ FIX-001) | Open | N/A | Track to Gate 1B |

### UNCLEAR detail — gift R005

- **Spec text:** "Override (Update 22-01-2025): nếu tại thời điểm scan nhận PO gốc mà PO gift chưa đủ điều kiện nhận (vd chưa verify invoice), hệ thống không hiện thông báo R003 và cho nhận **PO gốc**"
- **Raw L1755-L1756 verbatim:** "Nếu tại thời điểm scan nhận PO gốc mà PO gift chưa đủ điều kiện để nhận (VD như chưa verify invoice) thì sẽ không hiện thông báo và cho nhận **PO gift**"
- **Discrepancy:** Raw nói "cho nhận PO gift" nhưng context (PO gift chưa đủ điều kiện) → logically should be "cho nhận PO gốc". Có khả năng raw typo.
- **Spec action:** Corrective interpretation. Cần PO confirm raw typo → FIX-001 thêm Q-007.

## stub_receiving_po_no_barcode (07062 S-36 + S-37, v2.17)

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| 07062#L1763-L1767 | R001 — Option `Nhận SKU không barcode` áp dụng all category | SUPPORTED | Keep |
| 07062#L1765-L1767 | R002 — Danh sách SKU không barcode trong PO | SUPPORTED | Keep |
| 07062#L1768 | R003 — Search theo SKU/tên | SUPPORTED | Keep |
| 07062#L1769-L1771 | R004 — Item info: SKU - Tên + Số lượng cần nhận | SUPPORTED | Keep |
| 07062#L1772-L1775 | R005 — SKU không HSD/lô: nhập SL ngay; click `Nhận hàng` | SUPPORTED | Keep |
| 07062#L1779-L1785 | R006 — SKU có HSD/lô: popup nhập SL + HSD + Lô | SUPPORTED | Keep |
| 07062#L1786-L1789 | R007 — Ghi nhận danh sách + tooltip retention + tap ngoài thoát | SUPPORTED | Keep |
| 07062#L1795-L1796 | R008 — Update 31-07-2025: ẩn SL cần nhận, đổi label | SUPPORTED | Keep |
| 07062#L1797-L1798 | R009 — = SL cần nhận → cập nhật danh sách | SUPPORTED | Keep |
| 07062#L1799 | R010 — > SL cần nhận → thông báo "đã có" (UNCLEAR verbatim) | SUPPORTED (Q-002 đã capture đúng cách — spec không claim verbatim) | Keep |
| 07062#L1803-L1804 | R011 — < SL cần nhận → confirm dialog verbatim VN match | SUPPORTED | Keep |
| AC-01..AC-09 | Derived from R001-R011 | All SUPPORTED | Keep |
| BR table (6 rules) | Mapped | All SUPPORTED | Keep |
| ERR-NBC-001 (>) | "thông báo đã có" — Q-002 captured | SUPPORTED (proper Q handling) | Keep |
| MSG-NBC-002 (<) | Verbatim VN match L1804 | SUPPORTED | Keep |
| 6 Questions (Q-001..Q-006) | Open | N/A | Track to Gate 1B |

---

## Summary

| Spec | R | AC | BR | MSG | Q | Findings |
|:-----|:-:|:-:|:--:|:---:|:-:|:---------|
| stub_receiving_po_po_sample | 12 | 7 | 7 | 2 | 6 | 0 |
| stub_receiving_po_concurrent | 11 | 8 | 7 | 3 | 6 | 0 |
| stub_qc_criteria_approval | 7 | 5 | 6 | 5 | 6 | 0 |
| stub_receiving_po_gift | 6 | 7 | 6 | 1 | 5+1* | **1 UNCLEAR (R005)** |
| stub_receiving_po_no_barcode | 11 | 9 | 6 | 2 | 6 | 0 |
| **Total** | **47** | **36** | **32** | **13** | **29+1** | **1 UNCLEAR → FIX-001** |

\* gift sẽ thêm Q-007 mới sau khi apply FIX-001 (chờ user confirm).
