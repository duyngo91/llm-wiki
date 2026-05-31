---
spec: stub_receiving_po_asn
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI, Functional]
---

# Test Suite — ASN list + detail + xem chi tiết sản phẩm

## Phạm vi
- Source spec: [[stub_receiving_po_asn]]
- Active requirements: 16 (R001-R006, R008-R012, R014, R016, R018-R022 — phần không bị block hoàn toàn)
- Blocked: 10 R-ID chờ open questions (R015/Q-001, R018/Q-002, R007/Q-003, R013/Q-004, R015+MSG-ASN-001/Q-005, R019/Q-006, R023/Q-007, R024/Q-008, R026/Q-009, R025/Q-010)

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-ASN-001 | Filter Mã ASN exact match | R002 / AC-01 | UI | Nhập `1002240906000004` | Chỉ ASN khớp chính xác xuất hiện | High |
| TC-ASN-002 | Filter Kho gợi ý từ ≥ 3 ký tự | R004 / AC-02 | UI | Nhập 2 ký tự → chưa gợi ý; nhập 3 ký tự → gợi ý xuất hiện | Suggestion chỉ xuất hiện từ 3 ký tự (BVA min 3) | High |
| TC-ASN-003 | Filter Loại multi-select — 4 values | R006 / AC-03 | UI | Chọn "Purchase order" + "Customer return" | Danh sách lọc đúng ASN thuộc 2 type này | High |
| TC-ASN-004 | Filter Trạng thái multi-select — 4 values | R008 | UI | Chọn nhiều status: Open + Receiving | Listing hiển thị ASN thuộc 2 status | High |
| TC-ASN-005 | Filter Đồng kiểm Yes/No | R009 / AC-04 | UI | Filter Đồng kiểm=Yes | Chỉ ASN có Đồng kiểm=Yes xuất hiện | High |
| TC-ASN-006 | Tùy chọn "In tất cả sản phẩm" — default OFF | R011 / AC-05 | UI + Functional | Listing; chưa tích "In tất cả sản phẩm" | Biên bản chỉ in SKU có khai báo thiếu hoặc SPKPH | High |
| TC-ASN-007 | "In tất cả sản phẩm" = ON → in toàn bộ SKU | R011 | Functional | Tích "In tất cả sản phẩm" → in | Biên bản bao gồm tất cả SKU đã nhận trong ASN | High |
| TC-ASN-008 | Thiết lập khổ giấy default = A5 | R012 | UI | Màn hình listing, chưa đổi khổ giấy | Khổ giấy mặc định hiển thị "A5" | High |
| TC-ASN-009 | Thiết lập khổ giấy lưu local theo máy tính | R013 / AC-06 | Functional | User chọn "In Bill" trên máy A; Mở lại lần 2 trên máy A | In Bill được áp dụng; trên máy B vẫn A5 | Medium |
| TC-ASN-010 | Button ReOpen — chỉ hiện khi status=Receiving + chưa scan item | R015 / AC-07 | UI | ASN status Receiving, chưa scan item | Button ReOpen hiển thị | High |
| TC-ASN-011 | Button ReOpen — không hiện khi đã scan item | R015 / AC-08 | UI | ASN status Receiving, đã scan 1 item | Button ReOpen không hiển thị | High |
| TC-ASN-012 | ReOpen — confirm dialog EN + kết quả | R015 / AC-09 | Functional | Click ReOpen; confirm dialog hiển thị `Do you want to ReOpen for ticket ASN {asn_code}?`; User click Yes | ASN về status Open + xóa employee assignment | High |
| TC-ASN-013 | Button "In biên bản" chỉ hiển thị khi Receiving hoặc Received | R016 / AC-10 | UI | ASN status Receiving và Received | Button In biên bản hiển thị. Khi status Open hoặc Canceled → ẩn | High |
| TC-ASN-014 | Số hoá đơn trong biên bản lấy từ Taxcode Inside | R018 / AC-11 | Functional | PO_A Taxcode = TX-001; In biên bản | Số hoá đơn = TX-001 | High |
| TC-ASN-015 | ASN detail — 3 field mới: Đồng kiểm, Camera, Mã vị trí | R019 / AC-12 | UI | ASN detail mở | Section Thông tin chung hiển thị 3 field: Đồng kiểm, Camera, Mã vị trí | High |
| TC-ASN-016 | ASN detail — SL xác nhận không thay đổi qua phiên | R021 / AC-13 | Functional | PO SKU_X SL=10; phiên 1 nhận 5 | SL xác nhận trong ASN detail phiên 2 vẫn = 10 (theo PO, không decrement) | High |
| TC-ASN-017 | ASN detail — SL thực nhận theo phiên (không cumulative) | R022 / AC-14 | Functional | PO SKU_X PO=10; phiên 1 nhận 5, phiên 2 nhận 3 | ASN detail phiên 2: SL thực nhận = 3 | High |
| TC-ASN-018 | ASN detail — SL thiếu decremental qua phiên | R023 / AC-15 | Functional | Như TC-ASN-017 | ASN detail phiên 2: SL thiếu = 10 - 5 - 3 = 2 | High |
| TC-ASN-019 | Vị trí default cho Shop — location mặc định | R024 / AC-16 | Functional | Shop 170 không yêu cầu scan bin; ASN tạo | Vị trí trong ASN detail = location mặc định của Shop | High |
| TC-ASN-020 | ASN detail — Mô tả khi user khai báo thiếu | R025 / AC-17 | UI | User trên App khai báo 4 thông tin (lý do, tình trạng, NCC giao bù, ghi chú) | Column Mô tả hiển thị đủ 4 thông tin | High |
| TC-ASN-021 | ASN detail — Group UID (Update 16-09-2025) | R026 / AC-18 | Functional | ASN_X có Group UID UID-G-1, UID-G-2 | Detail hiển thị thông tin Group UID đã nhận | High |
| TC-ASN-022 | Filter Người sở hữu multi-select — 3 values | R007 | UI | Chọn "Hasaki Cosmetics" + "Hasaki WMS" | Listing lọc đúng 2 owner | High |
| TC-ASN-023 | Listing columns đầy đủ 16 cột | R014 | UI | Màn hình listing | 16 cột hiển thị: Mã ASN, Kho, Loại, Mã phiếu nhập, Phiếu nhập nguồn, Mã phiếu xuất, Phiếu xuất nguồn, Người sở hữu, Đồng kiểm, Mã camera, Mã vị trí, Mã giỏ, Ngày tạo, Ngày cập nhật, Trạng thái, Thao tác | High |
| TC-ASN-024 | BVA — SL thiếu = 0 khi đã nhận đủ | R023 | Functional | PO SKU SL=10; nhận đủ 10 trong các phiên | SL thiếu = 0 | Medium |

## 🚧 Blocked Coverage

- **R015, E1 (Q-001)** — chờ xác nhận workflow undo item để có thể ReOpen ASN đã scan. Không thể test reverse flow.
- **R018, E2 (Q-002)** — chờ xác nhận hiển thị biên bản khi Taxcode trùng giữa PO gift và PO gốc. Không thể test disambiguate.
- **R007 (Q-003)** — chờ xác nhận Owner enum đầy đủ (còn entity khác ngoài 3 values). Không thể test edge case owner.
- **R013 (Q-004)** — chờ xác nhận storage mechanism khổ giấy (cookie/localStorage). Không thể test persistence mechanism.
- **R015, MSG-ASN-001 (Q-005)** — chờ verbatim VN cho confirm dialog ReOpen. TC-ASN-012 chỉ test behavior, không verify VN text.
- **R019 (Q-006)** — chờ xác nhận Camera field semantics (mã camera hay flag Yes/No). Không thể test nội dung Camera field.
- **R023 (Q-007)** — chờ xác nhận formula SL thiếu khi phiên giao bù phần thiếu phiên trước. Không thể test retroactive recalculation.
- **R024 (Q-008)** — chờ xác nhận scope Shop 170 và Kho 170 (hardcoded hay config). Không thể test các kho khác.
- **R026 (Q-009)** — chờ xác nhận Group UID có filter/search hay chỉ display. Không thể test filter Group UID.
- **R025 (Q-010)** — chờ xác nhận Mô tả trống khi không có khai báo thiếu. Không thể test empty state.

## Regression Impact
- [[stub_receiving_po_inbound_shipment]] — filter Đồng kiểm move từ Inbound Shipment qua ASN
- [[stub_receiving_po_invoice]] — Taxcode từ Inside → Số hoá đơn trong biên bản

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.1. 24 TC active, 10 blocked coverage item.
