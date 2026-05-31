---
spec: stub_receiving_po_no_barcode
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI, Functional]
---

# Test Suite — Nhận hàng SKU không barcode (App)

## Phạm vi
- Source spec: [[stub_receiving_po_no_barcode]]
- Active requirements: 7 (R001, R002, R004, R005, R007, R008, R009, R011 — phần clear)
- Blocked: 6 R-ID chờ open questions (R006/Q-001, R010+ERR-NBC-001/Q-002, R011/Q-003, R008/Q-004, R003/Q-005, R002/Q-006)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-NBC-001 | Hiển thị option "Nhận SKU không barcode" tại màn hình scan SKU | R001 / AC-01 | UI | User mở màn hình scan SKU cho PO có ≥ 1 SKU không barcode | Option "Nhận SKU không barcode" hiển thị | High |
| TC-NBC-002 | Chọn "Nhận SKU không barcode" → hiển thị danh sách SKU không barcode trong PO | R002 / AC-02 | UI + Functional | PO có 3 SKU không barcode; User chọn "Nhận SKU không barcode" | App show danh sách 3 SKU không barcode | High |
| TC-NBC-003 | Danh sách hiển thị SKU và Tên sản phẩm | R004 | UI | Danh sách đang hiển thị | Mỗi item hiển thị định dạng: SKU - Tên sản phẩm | High |
| TC-NBC-004 | Update 31-07-2025: label "Số lượng thực nhận" — ẩn "Số lượng cần nhận" | R008 / AC-05 | UI | Màn hình sau update 31-07-2025 | Hiển thị label "Số lượng thực nhận"; không hiển thị "Số lượng cần nhận" | High |
| TC-NBC-005 | Nhận SKU không config HSD/số lô — SL thực nhận = SL cần nhận | R005 / AC-03 | Functional | SKU_A không config HSD/lô; SL cần nhận = 100; User nhập 100 | Ghi nhận qty=100 vào danh sách đã nhận; tooltip giữ nguyên nếu còn SKU | High |
| TC-NBC-006 | SL thực nhận < SL cần nhận → hiển thị confirm dialog | R011 / AC-07 | UI + Functional | SKU_A cần 400; User nhập 300 | App hiển thị: `Số lượng thực nhận nhỏ hơn số lượng của PO (300/400). Bạn có muốn xác nhận không?` | High |
| TC-NBC-007 | Confirm dialog MSG-NBC-002 — xác nhận "Có" → ghi nhận | R011 | Functional | Confirm dialog đang hiển thị; User chọn "Có" | Ghi nhận qty=300 vào danh sách | High |
| TC-NBC-008 | Tooltip giữ lại khi còn SKU không barcode chưa nhận | R007 / AC-09 | UI | PO 3 SKU không barcode; User vừa nhận xong 1 SKU | Tooltip vẫn hiển thị 2 SKU còn lại | High |
| TC-NBC-009 | Thoát tooltip khi tap ra ngoài | R007 / AC-08 | UI | Tooltip danh sách SKU không barcode đang mở | User tap ra ngoài → tooltip đóng | High |
| TC-NBC-010 | Update 31-07-2025: SL thực nhận = SL cần nhận → ghi nhận bình thường | R009 / AC-03 | Functional | SL thực nhận = SL cần nhận | Cập nhật vào danh sách đã nhận; nếu còn SKU → user nhận tiếp | High |
| TC-NBC-011 | EP — SKU không barcode trong PO phải xuất hiện trong danh sách | R002 | Functional | PO có SKU_A không barcode, SKU_B có barcode | Danh sách chỉ hiển thị SKU_A; SKU_B không xuất hiện | High |
| TC-NBC-012 | BVA — SL thực nhận = 0 | R005 | Functional | User nhập SL = 0 | Xử lý hợp lý (không cho nhận 0, hoặc báo lỗi tùy rule hệ thống) | Medium |

## 🚧 Blocked Coverage

- **R006 (AC-04, Q-001)** — chờ xác nhận `Hạn sử dụng` và `Số lô` trong popup có bắt buộc nhập không và validate format. Không thể test validation popup HSD/lô.
- **R010 (AC-06, Q-002)** — chờ verbatim message VN+EN khi SL thực nhận > SL cần nhận (raw ghi "thông báo đã có"). Không thể test message text và behavior (block hay confirm).
- **R011 (Q-003)** — chờ xác nhận behavior khi user chọn "Không" trong confirm dialog MSG-NBC-002 (quay lại nhập hay đóng popup). Không thể test luồng hủy.
- **R008 (Q-004)** — chờ xác nhận case popup HSD/số lô (R006) có còn hiển thị "Số lượng cần nhận" không sau Update 31-07-2025. Không thể test UI popup.
- **R003 (Q-005)** — chờ xác nhận search match exact/partial/case-insensitive. Không thể test boundary cho search.
- **R002 (Q-006)** — chờ xác nhận pagination/scroll và sort default cho danh sách. Không thể test danh sách dài.

## Regression Impact
- [[stub_receiving_po_app]] — UI scan PO trên App là parent feature
- [[stub_receiving_po_date_rules]] — rules HSD/số lô liên quan

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.1. 12 TC active, 6 blocked coverage item.
