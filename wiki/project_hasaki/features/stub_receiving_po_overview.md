---
aliases: [stub_receiving_po_overview]
tags: [qa/requirement, qa/feature-group/receiving_po]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_receiving_po_overview
project: project_hasaki
source_version: 2.17
source_doc: 07062_Receiving_PO_Docs_ver2.17.md
source_range: 07062#L188-L223
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-30 19:00:00"
verification_status: Pending
approved_by:
approved_at:
approval_note:
---

# REQ: stub_receiving_po_overview

## Tổng quan
- **Mã tính năng:** stub_receiving_po_overview
- **Feature:** Receiving PO — Tổng quan, Thuật ngữ, Workflow, Wireframe, Mục tiêu migration
- **Mô tả ngắn:** Section overview của tài liệu Receiving PO v2.17 — gồm TỔNG QUAN (giải thích lý do migration từ App HSK Work sang WMS để đồng bộ và dễ quản lý), Thuật ngữ & viết tắt (bảng rỗng — chưa định nghĩa), Quy trình (Workflow) link Drive, Giao diện (Wireframe) link Figma update + Visily old, và heading Yêu cầu chức năng dẫn vào nội dung detail bắt đầu từ Inbound Shipment.
- **Source chính:** 07062_Receiving_PO_Docs_ver2.17.md (v2.17)
- **Đối tượng sử dụng (Actors):** N/A — section header/metadata.
- **Feature Group:** [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]
- **Test Suite tương ứng:** [[test_stub_receiving_po_overview]]
- **API Spec liên quan:** N/A — section overview không mô tả API.
- **Mối quan hệ:** Đây là section gateway cho toàn bộ feature group [[wiki/project_hasaki/feature_groups/receiving_po|receiving_po]]. Wireframe Figma cover wireframes các features. Mục tiêu migration App HSK Work → WMS là driver kiến trúc của tất cả features con.

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07062_Receiving_PO_Docs_ver2.17.md | 2.17 | ✅ Hiện hành |
| 2 | Workflow Link | https://drive.hasaki.vn/f/6fecf6ac99424782b12a/ | — | Reference (Q-001) |
| 3 | Wireframe Figma (update) | https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO_Update?node-id=0-1 | — | Hiện hành (Q-002) |
| 4 | Wireframe Visily (old) | https://app.visily.ai/projects/760aa71b-3404-49db-a5ec-bde3412ccdc6/boards/739286 | — | Legacy reference (Q-002) |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| N/A | | | Section overview không mô tả API | N/A |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Hiện tại việc nhận hàng PO đang được thực hiện trên **App HSK Work**. Việc sử dụng đang có nhiều hạn chế cũng như cải tiến cũng gặp nhiều khó khăn | Documentation / Context | Low | ⚠️ | 07062#L189-L190 |
| R002 | Tính năng nhận hàng PO thuộc phạm vi của **Kho** → **move tính năng này qua WMS** để đồng bộ và tiện cho việc quản lý và hỗ trợ sau này | Business Goal / Architecture | High | ⚠️ | 07062#L191-L192 |
| R003 | Tài liệu có section `Thuật ngữ & viết tắt` với bảng 4 cột (`# Code`, `Name`, `Desciption` — typo, xem Q-005). **Bảng có 5 dòng nhưng đều rỗng** — chưa có thuật ngữ nào được định nghĩa trong v2.17 | Documentation | Low | ⚠️ | 07062#L198-L207 |
| R004 | Tài liệu có section `Quy trình (Workflow)` link sang Drive Hasaki: `https://drive.hasaki.vn/f/6fecf6ac99424782b12a/` | Documentation | Low | ⚠️ | 07062#L208-L209 |
| R005 | Tài liệu có section `Giao diện (Wireframe)` với 2 link: (a) Figma update — `https://www.figma.com/design/T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO_Update?node-id=0-1&t=DjHSg0g4aPYPxsTM-1`; (b) Visily old — `https://app.visily.ai/projects/760aa71b-3404-49db-a5ec-bde3412ccdc6/boards/739286` | Documentation | Low | ⚠️ | 07062#L211-L216 |
| R006 | Tài liệu có heading `Yêu cầu chức năng` (Functional requirements) tại L223 dẫn vào nội dung chi tiết bắt đầu từ section `Inbound Shipment – Updated` (S-05) | Documentation | Low | ✅ | 07062#L223-L224 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- N/A — section overview là metadata, không có flow runtime.

### Luồng chuẩn (Happy Path) — Onboard reviewer
1. Reviewer mở tài liệu Receiving PO v2.17.
2. Đọc section TỔNG QUAN — nắm bối cảnh migration App HSK Work → WMS (R001, R002).
3. Tra Workflow tại Drive link (R004).
4. Tra Wireframe tại Figma update (ưu tiên) hoặc Visily old (reference) (R005).
5. Đọc tiếp các yêu cầu chức năng chi tiết từ `Inbound Shipment` trở đi (R006).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — Đọc theo Wireframe trước:** Dev/QA mở Figma trước rồi đối chiếu spec (R005).

### Luồng ngoại lệ (Exception Paths)
- **E1 — Link Drive/Figma/Visily không truy cập:** request quyền truy cập owner.
- **E2 — Figma update khác Visily old:** ưu tiên Figma update — Visily là legacy reference (R005).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Mục tiêu migration | rule | ✅ | Receiving PO phải move từ App HSK Work sang WMS để sync và dễ quản lý — driver kiến trúc cho all sub-features |
| Bảng thuật ngữ | table | ❌ | Hiện trống — cần bổ sung khi có (Q-003) |
| Workflow link | URL | ✅ | Phải là Drive Hasaki link hợp lệ |
| Wireframe link | URL | ✅ | Ưu tiên Figma update (`T103qrHGDj4oGCu88fCU2C/04.-Receiving-PO_Update`); Visily chỉ là legacy reference |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

- Không có error message — section overview không trigger lỗi runtime.

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — TỔNG QUAN nêu rõ context migration**
  - **Given:** User mở tài liệu Receiving PO v2.17.
  - **When:** User đọc section TỔNG QUAN.
  - **Then:** Section nêu rõ App HSK Work có hạn chế + mục tiêu move qua WMS để sync và dễ quản lý (R001, R002).
- **AC-02 — Bảng thuật ngữ có header chuẩn 4 cột**
  - **Given:** Tài liệu v2.17.
  - **When:** User cuộn đến section `Thuật ngữ & viết tắt`.
  - **Then:** Bảng có header `# Code | Name | Desciption` (raw có typo `Desciption`) và 5 row rỗng (R003).
- **AC-03 — Workflow link Drive truy cập được**
  - **Given:** Tài liệu v2.17.
  - **When:** User click link section `Quy trình (Workflow)`.
  - **Then:** Trình duyệt mở `https://drive.hasaki.vn/f/6fecf6ac99424782b12a/` (R004).
- **AC-04 — Wireframe có 2 link Figma update + Visily old**
  - **Given:** Tài liệu v2.17.
  - **When:** User cuộn đến section `Giao diện (Wireframe)`.
  - **Then:** Hiển thị 2 link, label `Figma update` (current) và `Visily (old)` (legacy) (R005).
- **AC-05 — Heading `Yêu cầu chức năng` đặt trước section chức năng chi tiết**
  - **Given:** Tài liệu v2.17.
  - **When:** User đọc sau section Wireframe.
  - **Then:** Heading `Yêu cầu chức năng` xuất hiện ngay trước section `Inbound Shipment – Updated` (R006).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R004 | Workflow Drive link có nội dung gì cụ thể? BPMN, flowchart, hay là 1 folder chứa nhiều file? Có sync với raw doc không? | PO | Open | | | |
| Q-002 | R005 | Wireframe Figma vs Visily — khi 2 wireframes khác nhau, ưu tiên cái nào? Visily là "old" nghĩa là sẽ deprecated trong tương lai? | UX | Open | | | |
| Q-003 | R003 | Bảng thuật ngữ rỗng 5 dòng — các thuật ngữ nào trong doc cần định nghĩa (vd `PO`, `Inbound Shipment`, `ASN`, `VAS`, `UID group`, `Group UID`, `RFID mapping`, `Đồng kiểm`, `Không đồng kiểm`, `PO Gift`, `PO Sample`, `Packing list`)? | PO/BA | Open | | | |
| Q-004 | R001, R002 | Mục tiêu migration App HSK Work → WMS — có timeline release plan / deadline cụ thể không? Có giai đoạn dual-run (App + WMS) hay cutover hard? | PO/PM | Open | | | |
| Q-005 | R003 | Header bảng terms ghi `Desciption` (typo) — fix trong v2.18 hay giữ nguyên? | PO | Open | | | |
| Q-006 | All R | Section overview có scope sinh test case không? Hay là metadata-only, test suite tương ứng (`test_stub_receiving_po_overview`) bị mark `N/A`? | QA Lead | Open | | | |
| Q-007 | R002 | Khi move sang WMS, App HSK Work có còn được dùng song song không (vd cho rollback) hay sẽ tắt hoàn toàn flow nhận PO trên App HSK Work? | PO/Dev | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-00, S-01, S-02, S-03, S-04 | 2.17 (stub) | 2.17 | All R + AC | Draft |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_receiving_po_overview | test_stub_receiving_po_overview | Add (cân nhắc N/A — Q-006) | Tất cả features con của receiving_po (vì là gateway section) | Q-001..Q-007 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R006, AC-01..AC-05 | | ⏳ Chưa thiết kế | Section metadata — có thể skip test case hoặc chỉ smoke validate link (Q-006) |

## 🚧 Blocked Coverage

- R001, R002 — chờ Q-004, Q-007 (timeline migration + dual-run)
- R003 — chờ Q-003, Q-005 (terms + typo)
- R004, R005 — chờ Q-001, Q-002 (scope Workflow + Wireframe)
- All R — chờ Q-006 (scope test cho section overview)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 19:00:00 | v1.1 | Refine stub → full spec: 6 R-ID, 5 AC, 4 BR, 0 messages, 7 questions Open. Section là metadata header — content tối thiểu nhưng có business goal (migration App → WMS). `partial_read: false`. | refine-batch-3-2026-05-30 |
