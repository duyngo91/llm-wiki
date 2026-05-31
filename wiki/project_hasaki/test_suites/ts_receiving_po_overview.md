---
spec: stub_receiving_po_overview
version: "1.0"
status: Draft
created_at: "2026-05-31"
scope: [UI]
---

# Test Suite — Receiving PO — Tổng quan, Thuật ngữ, Workflow, Wireframe

## Phạm vi
- Source spec: [[stub_receiving_po_overview]]
- Active requirements: 1 (R006 — phần không bị block)
- Blocked: 5 R-ID chờ open questions (R001+R002/Q-004+Q-007, R003/Q-003+Q-005, R004/Q-001, R005/Q-002, All R/Q-006)

**Ghi chú quan trọng:** Spec Q-006 đặt câu hỏi liệu section overview có scope sinh test case không hay là metadata-only. Dựa trên nguyên tắc no-inference, chỉ thiết kế TC cho R006 vì đây là requirement duy nhất có Testable = ✅ và không nằm trong Blocked Coverage.

## Test Cases

| TC-ID | Tên TC | R-ID/AC | Scope | Input | Expected | Priority |
|-------|--------|---------|-------|-------|----------|---------|
| TC-OVW-001 | Heading "Yêu cầu chức năng" xuất hiện trước section Inbound Shipment | R006 / AC-05 | UI | Tài liệu v2.17 | Heading "Yêu cầu chức năng" xuất hiện ngay trước section "Inbound Shipment – Updated" | Low |

## 🚧 Blocked Coverage

- **R001, R002 (Q-004)** — chờ timeline migration App HSK Work → WMS và kế hoạch dual-run hay cutover hard. Không thể test migration behavior.
- **R001, R002 (Q-007)** — chờ xác nhận App HSK Work có còn được dùng song song không. Không thể test isolation.
- **R003 (Q-003)** — chờ danh sách thuật ngữ cần định nghĩa trong bảng rỗng. Không thể test nội dung bảng thuật ngữ.
- **R003 (Q-005)** — chờ xác nhận typo `Desciption` có được fix không. Không thể test header chính xác.
- **R004 (Q-001)** — chờ nội dung Workflow Drive link. Không thể test nội dung workflow.
- **R005 (Q-002)** — chờ xác nhận ưu tiên giữa Figma update vs Visily old. Không thể test source of truth cho wireframe.
- **All R (Q-006)** — chờ QA Lead xác nhận scope test cho section overview. Phần lớn nội dung bị block cho đến khi có quyết định scope.

## Regression Impact
- Tất cả features con của [[receiving_po]] (đây là gateway section, migration driver kiến trúc)

## Changelog
- v1.0 — 2026-05-31: Initial test design từ spec v1.1. 1 TC active, 6 blocked coverage item. Section overview chủ yếu là metadata — test suite minimal theo nguyên tắc no-inference.
