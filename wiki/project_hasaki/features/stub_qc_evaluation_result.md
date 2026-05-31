---
aliases: [stub_qc_evaluation_result]
tags: [qa/requirement, qa/feature-group/quality_control]
status: Draft
created: 2026-05-30
updated: 2026-05-30
feature: stub_qc_evaluation_result
project: project_hasaki
source_version: 1.5
source_doc: 07105_Quality_Control_Docs_ver1.5.md
source_range: 07105#L570-L1127
partial_read: false
partial_read_note: ""
last_verified_at: "2026-05-31 17:50:34"
verification_status: Verified
approved_by:
approved_at:
approval_note:
last_verified_source_version: 1.5

---

# REQ: stub_qc_evaluation_result

## Tổng quan
- **Mã tính năng:** stub_qc_evaluation_result
- **Feature:** Kết quả đánh giá QC — Listing + Chi tiết (Web + App)
- **Mô tả ngắn:** Trang `Inbound / Quality control / Tab Kết quả đánh giá` cho phép user filter, listing và xem chi tiết kết quả đánh giá QC. Hỗ trợ 3 type: Bình thường / Nhóm UID / Xã vải. Chi tiết kết quả gồm: tiêu chí thường (đạt/không đạt), tiêu chí lỗi 4 điểm (group theo loại lỗi 1/2/3/4 điểm + tổng điểm chưa/đã nhân hệ số), tiêu chí theo bước (image + kết quả + ghi chú). Update 18-09-2025: tách màn hình chi tiết theo Type. Update Web (S-25): bổ sung `Số lượng cần đánh giá`, `Hình ảnh tem QC`, field `Đánh giá đạt` cho UID group (N/A / No / Yes).
- **Source chính:** 07105_Quality_Control_Docs_ver1.5.md (v1.5)
- **Đối tượng sử dụng (Actors):** QC team, kho.
- **Feature Group:** [[wiki/project_hasaki/feature_groups/quality_control|quality_control]]
- **Test Suite tương ứng:** [[ts_qc_evaluation_result]]
- **API Spec liên quan:** [[api_qc_assessment_result_service]] — raw mô tả architectural service (conceptual; chi tiết kỹ thuật cần confirm).
- **Mối quan hệ:** ⬅️ phụ thuộc [[stub_qc_criteria_setup]] (tiêu chí thiết lập), [[stub_qc_criteria_sku]] (tiêu chí SKU), [[stub_qc_evaluation_mobile]] (input đánh giá từ App), [[stub_qc_evaluation_manual]] (input đánh giá Manual). ➡️ feed [[stub_qc_vas]] (kết quả tổng hợp cho VAS), [[stub_qc_uid_group]] (kết quả tổng hợp cho group UID).

## Nguồn tài liệu
| # | Loại | Tên / Link | Version | Status |
|:--|:-----|:-----------|:--------|:-------|
| 1 | MD | 07105_Quality_Control_Docs_ver1.5.md | 1.5 | ✅ Hiện hành |

## API / Interface liên quan
| API Spec | API/Interface | Requirement/AC liên quan | Source | Trạng thái |
|:---------|:--------------|:-------------------------|:-------|:-----------|
| [[api_qc_assessment_result_service]] | WMS Internal QC Result Service (aggregate multi-source evaluations per VAS + Group UID) | R009 (result persistence) | 07105#L649-L658 | Draft — 10 open questions |

## Phân rã Requirement

| ID | Requirement | Loại | Priority | Testable? | Source |
|:---|:-----------|:-----|:---------|:----------|:-------|
| R001 | Trang `Kết quả đánh giá` (Assessment Result) nằm tại `Menu: Inbound / Quality control` → Tab `Kết quả đánh giá` | UI + Navigation | High | ✅ | 07105#L571-L573 |
| R002 | Filter — `SKU, barcode`: hỗ trợ tìm theo SKU hoặc barcode của sản phẩm; **tìm theo mã chính xác nhập vào** | Filter | High | ✅ | 07105#L578-L579 |
| R003 | Filter — `VAS`: hỗ trợ tìm theo mã VAS; **tìm theo mã chính xác** | Filter | High | ✅ | 07105#L580-L582 |
| R004 | Filter — `Kho` (Warehouse): tìm theo kho cần đánh giá; **hỗ trợ tìm theo tên kho khi nhập từ 3 ký tự** | Filter | High | ✅ | 07105#L583-L585 |
| R005 | Filter — `Mã PO` (PO code): hỗ trợ tìm theo mã PO nguồn (mã PO inside); **tìm theo mã chính xác** | Filter | High | ✅ | 07105#L586-L588 |
| R006 | Filter — `Trạng thái` (Status): 3 values — `Mới (New)`: yêu cầu đánh giá vừa sinh; `Đang đánh giá (Processing)`: đang đánh giá chưa hoàn thành; `Hoàn thành (Completed)`: yêu cầu đã xác nhận hoàn thành | Filter + Enum | High | ✅ | 07105#L589-L595 |
| R007 | Filter — `Phân loại` (Type): 2 trục enum kết hợp. Trục nguồn gốc: `Tự động (Automation)` — tự sinh theo thiết lập SKU; `Thủ công (Manual)` — user tạo. Trục flow: `Bình thường (Normal)`; `Nhóm UID (Group UID)` — cho SP Vải; `Xã vải (Fabric Relaxing)` — cho khâu xã vải trước khi may thành phẩm | Filter + Enum | High | ✅ | 07105#L596-L606 |
| R008 | Filter — `Người đánh giá` (Assessment by): người thực hiện đánh giá. **Format hiển thị: Email Hasaki + Thời gian hoàn thành đánh giá** | Filter + UI | High | ✅ | 07105#L607-L611 |
| R009 | Filter — `Có tiêu chí không đạt` (Have criteria fail): `Có (Yes)` — có ít nhất 1 tiêu chí không đạt; `Không (No)` — không có tiêu chí không đạt | Filter + Enum | High | ✅ | 07105#L612-L616 |
| R010 | Filter — `Ngày đánh giá` (Assessment at): chọn `Từ ngày` đến `Đến ngày`. Validation: `Từ ngày` ≤ `Đến ngày` | Filter + Validation | High | ✅ | 07105#L617-L624 |
| R011 | Listing — Cột `VAS`: hyperlink, click chuyển sang trang detail của VAS tương ứng | UI + Navigation | High | ✅ | 07105#L629 |
| R012 | Listing — Cột `Kho` (Warehouse) | UI | Medium | ✅ | 07105#L630 |
| R013 | Listing — Cột `Sản phẩm` (Product): format `SKU – tên sản phẩm` | UI | High | ✅ | 07105#L632 |
| R014 | Listing — Cột `Tiêu chí đạt` (Criteria passed): hiển thị `tổng số tiêu chí đạt / tổng tiêu chí cần đánh giá cho SKU` | UI + Business rule | High | ✅ | 07105#L633 |
| R015 | Listing — Cột `Tiêu chí không đạt` (Criteria failed): hiển thị `tổng số tiêu chí không đạt / tổng tiêu chí cần đánh giá cho SKU` | UI + Business rule | High | ✅ | 07105#L634 |
| R016 | Listing — Cột `Phân loại` (Type): hiển thị giá trị enum theo R007 | UI | Medium | ✅ | 07105#L635-L636 |
| R017 | Listing — Cột `Mã PO nguồn` (PO source number): hyperlink, click chuyển sang trang detail của PO trên Inside | UI + Navigation | High | ✅ | 07105#L637 |
| R018 | Listing — Các cột thông tin SP: `Nhà cung cấp` (Vendor), `Danh mục` (Category), `Thương hiệu` (Brand), `Ghi chú` (Note), `Người đánh giá` (email Hasaki + thời gian hoàn thành đánh giá), `Trạng thái` (Status) | UI | Medium | ✅ | 07105#L638-L645 |
| R019 | Listing — Cột `Thao tác`: chọn icon để xem chi tiết kết quả đánh giá | UI + Functional | High | ✅ | 07105#L646-L647 |
| R020 | Service ghi nhận kết quả đánh giá: dựng 1 service nhận thông tin từ nhiều nguồn → WMS ghi nhận kết quả cuối cùng. `VAS_ID + Group UID` gắn với từng service. Mỗi service gồm: `Group UID`, `Mã tiêu chí`, `Kết quả`. Mỗi service = 1 kết quả đánh giá của 1 group UID. Tổng hợp các service → kết quả cho cả group UID và VAS | Architecture + Business rule | High | ⚠️ | 07105#L649-L658 |
| R021 | Update 18-09-2025 — Chi tiết kết quả đánh giá khi `Type = Bình thường`: hiển thị chi tiết kết quả đánh giá chất lượng sản phẩm (raw chỉ nêu heading, format chi tiết Q-002) | UI + Functional | High | ⚠️ | 07105#L659-L662 |
| R022 | Update 18-09-2025 — Chi tiết kết quả đánh giá khi `Type = Nhóm UID`: user chọn icon để xem chi tiết kết quả đánh giá **theo từng nhóm UID** | UI + Functional | High | ✅ | 07105#L665-L666 |
| R023 | Tiêu chí lỗi 4 điểm — lưu trữ và hiển thị **riêng** do loại tiêu chí này đặc thù | Business rule + UI | High | ✅ | 07105#L667-L668 |
| R024 | Tiêu chí lỗi 4 điểm — mỗi loại lỗi là 1 group, có thể **thu gọn hoặc mở rộng** | UI | Medium | ✅ | 07105#L672 |
| R025 | Tiêu chí lỗi 4 điểm — hiển thị `Tổng điểm lỗi = tổng số điểm của 4 loại lỗi chưa nhân hệ số` và `Tổng điểm lỗi đã nhân hệ số` | Business rule + UI | High | ✅ | 07105#L674-L675 |
| R026 | Tiêu chí lỗi 4 điểm — trong mỗi loại lỗi, hiển thị thông tin chi tiết từng lỗi: `Loại lỗi`, `Hình ảnh lỗi`, `Ghi chú`. Áp dụng cho **4 nhóm**: lỗi 1 điểm, 2 điểm, 3 điểm, 4 điểm | UI + Business rule | High | ✅ | 07105#L676-L684 |
| R027 | Tiêu chí thiết lập theo bước — mỗi bước hiển thị 1 nhóm thông tin gồm: `Hình ảnh`, `Kết quả ghi nhận`, `Ghi chú` | UI + Business rule | High | ✅ | 07105#L685-L689 |
| R028 | Update S-25 (Web) — Chi tiết kết quả đánh giá bổ sung thêm 2 thông tin: `Số lượng cần đánh giá`, `Hình ảnh tem QC` | UI | High | ✅ | 07105#L1103-L1106 |
| R029 | Update S-25 (Web) — Cột `Phân loại` (Type) **bổ sung giá trị `Xã vải / Fabric Relaxing`**: luồng đánh giá cho khâu xã vải trước khi chuyển qua may thành phẩm | Enum + UI | High | ✅ | 07105#L1108-L1111 |
| R030 | Update S-25 (Web) — `UID group (Web)` tại `Menu: Inventory / Group UID / Tab Danh sách`: bổ sung field `Đánh giá đạt` với 3 values: `N/A` — SKU có khai báo UID group nhưng không thuộc Thời trang (NVL) và không phải SKU vải; `No` — SKU thuộc Thời trang (NVL) và là SKU vải, sau khi nhận PO mặc định = `No`, sau khi đánh giá xã vải Đạt → chuyển `No → Yes`; `Yes` — SKU thuộc Thời trang (NVL) và là SKU vải, sau khi nhận PO và hoàn thành đánh giá xã vải có kết quả Đạt | Enum + State transition + UI | High | ✅ | 07105#L1112-L1123 |

## 🔄 Luồng Nghiệp Vụ Chi Tiết (User Flows)

### Điều kiện tiên quyết (Pre-conditions)
- User có quyền truy cập menu `Inbound / Quality control`.
- Có ít nhất 1 yêu cầu đánh giá QC đã sinh (Automation hoặc Manual).

### Luồng chuẩn (Happy Path) — Listing + Filter + Xem chi tiết
1. User mở `Menu: Inbound / Quality control / Tab Kết quả đánh giá` (R001).
2. User filter theo nhu cầu (SKU/barcode/VAS/Kho/Mã PO/Trạng thái/Phân loại/Người đánh giá/Có tiêu chí không đạt/Ngày đánh giá) (R002–R010).
3. Hệ thống hiển thị listing với các cột R011–R018.
4. User click icon `Thao tác` ở 1 dòng → mở chi tiết kết quả đánh giá (R019).
5. Tuỳ `Type`:
   - `Bình thường` → trang chi tiết kết quả đánh giá chất lượng SP (R021).
   - `Nhóm UID` → trang chi tiết theo từng nhóm UID (R022).
6. Nếu kết quả có tiêu chí lỗi 4 điểm → hiển thị group riêng (R023–R026).
7. Nếu kết quả có tiêu chí theo bước → mỗi bước là 1 nhóm thông tin (R027).

### Luồng chuẩn (Happy Path) — VAS hyperlink
1. User click cell `VAS` ở 1 dòng → chuyển sang trang detail VAS tương ứng (R011).

### Luồng chuẩn (Happy Path) — PO hyperlink
1. User click cell `Mã PO nguồn` → chuyển sang trang detail PO trên Inside (R017).

### Luồng chuẩn (Happy Path) — UID group state transition (Update S-25)
1. PO nhận xong, SKU thuộc Thời trang (NVL) là SKU vải → field `Đánh giá đạt` của UID group = `No` (R030 default).
2. QC đánh giá xã vải Đạt → field chuyển `No → Yes` (R030 transition).

### Luồng rẽ nhánh (Alternative Paths)
- **A1 — Type = Xã vải (Update S-25):** filter có thêm value Xã vải; chi tiết kết quả theo flow xã vải (R029).
- **A2 — Service ghi nhận từ nhiều nguồn:** kết quả tổng hợp = sum các service của cùng VAS_ID + Group UID (R020).
- **A3 — Có tiêu chí không đạt = Có:** filter trả về các kết quả có ≥ 1 tiêu chí không đạt; UI cột `Tiêu chí không đạt` hiển thị tỷ lệ > 0 (R009, R015).
- **A4 — UID group N/A:** SKU không thuộc Thời trang (NVL) và không phải SKU vải → field `Đánh giá đạt` luôn là `N/A`, không cho transition (R030).

### Luồng ngoại lệ (Exception Paths)
- **E1 — Ngày đánh giá Từ > Đến:** validation block, không apply filter (R010).
- **E2 — Tên kho < 3 ký tự:** filter Kho không trigger search (R004).
- **E3 — Mã PO sai chính xác:** filter trả 0 record (R005).

## ⚙️ Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu (Business Rules)

| Tên trường / Rule | Định dạng | Bắt buộc? | Ràng buộc (Validation & Logic) |
|:-----------------|:---------|:----------|:-------------------------------|
| Filter SKU/barcode | string | ❌ | Match exact mã nhập vào |
| Filter VAS | string | ❌ | Match exact mã VAS |
| Filter Kho | string | ❌ | Nhập ≥ 3 ký tự mới trigger search; match theo tên kho |
| Filter Mã PO | string | ❌ | Match exact mã PO inside |
| Filter Trạng thái | enum | ❌ | ∈ {`Mới`, `Đang đánh giá`, `Hoàn thành`} |
| Filter Phân loại nguồn | enum | ❌ | ∈ {`Tự động`, `Thủ công`} |
| Filter Phân loại flow | enum | ❌ | ∈ {`Bình thường`, `Nhóm UID`, `Xã vải`} |
| Filter Có tiêu chí không đạt | enum | ❌ | ∈ {`Có`, `Không`} |
| Filter Ngày đánh giá | date range | ❌ | `Từ` ≤ `Đến` |
| Listing Tiêu chí đạt/Không đạt | ratio | — | Format `count_pass / total` và `count_fail / total` theo SKU |
| Listing Sản phẩm | string | — | Format `SKU – tên sản phẩm` |
| Service ghi nhận | record | ✅ | Mỗi service = 1 kết quả đánh giá của 1 group UID; gồm Group UID + Mã tiêu chí + Kết quả; gắn theo VAS_ID + Group UID |
| Tiêu chí lỗi 4 điểm — group | rule | ✅ | Lưu trữ + hiển thị riêng; mỗi loại lỗi (1/2/3/4 điểm) là 1 group thu gọn/mở rộng |
| Tổng điểm lỗi 4 điểm | number | ✅ | `Tổng chưa nhân hệ số = sum(điểm 4 loại)`; `Tổng đã nhân hệ số` (raw không nêu công thức hệ số — Q-003) |
| Tiêu chí theo bước | record | ✅ | Mỗi bước = nhóm thông tin gồm Hình ảnh + Kết quả ghi nhận + Ghi chú |
| UID group `Đánh giá đạt` | enum | ✅ | ∈ {`N/A`, `No`, `Yes`}; transition `No → Yes` chỉ khi đánh giá xã vải có kết quả Đạt |

## 🚨 Đặc Tả Thông Điệp Báo Lỗi (Error Messages Map)

| Mã lỗi | Loại | Trigger | Message VN | Message EN | Source |
|:-------|:-----|:--------|:-----------|:-----------|:-------|
| ERR-QCR-001 | Validation | Filter Ngày đánh giá: `Từ ngày` > `Đến ngày` | (raw không có verbatim — Q-004) | (raw không có verbatim — Q-004) | 07105#L624 |

## 🏁 Tiêu Chí Nghiệm Thu (Acceptance Criteria — BDD)

- **AC-01 — Truy cập trang Kết quả đánh giá**
  - **Given:** User có quyền QC.
  - **When:** User vào `Menu: Inbound / Quality control / Tab Kết quả đánh giá`.
  - **Then:** Hệ thống hiển thị listing kết quả đánh giá với toolbar filter (R001).
- **AC-02 — Filter SKU/barcode match exact**
  - **Given:** Có kết quả với SKU = `SKU-001` và `SKU-001-X`.
  - **When:** User nhập filter `SKU-001`.
  - **Then:** Chỉ kết quả với SKU = exact `SKU-001` được hiển thị (R002).
- **AC-03 — Filter Kho ≥ 3 ký tự mới trigger**
  - **Given:** Có Kho `Hà Nội`, `Hồ Chí Minh`.
  - **When:** User nhập filter Kho = `Hà` (2 ký tự).
  - **Then:** Filter chưa trigger; nhập tiếp `Hà N` (4 ký tự) → trigger search (R004).
- **AC-04 — Filter Trạng thái 3 values**
  - **Given:** Có kết quả với cả 3 status (Mới, Đang đánh giá, Hoàn thành).
  - **When:** User chọn filter Trạng thái = `Đang đánh giá`.
  - **Then:** Chỉ kết quả status `Processing` hiển thị (R006).
- **AC-05 — Filter Phân loại hỗ trợ 5 giá trị enum**
  - **Given:** Có kết quả với cả 5 type (Tự động, Thủ công, Bình thường, Nhóm UID, Xã vải).
  - **When:** User chọn filter Phân loại = `Xã vải`.
  - **Then:** Chỉ kết quả type `Fabric Relaxing` hiển thị (R007, R029).
- **AC-06 — Filter Có tiêu chí không đạt = Có**
  - **Given:** Có 5 kết quả, trong đó 3 có ≥ 1 tiêu chí fail.
  - **When:** User filter = `Có`.
  - **Then:** 3 kết quả hiển thị (R009).
- **AC-07 — Filter Ngày đánh giá Từ > Đến**
  - **Given:** User filter Ngày từ `2026-05-30`.
  - **When:** User chọn Ngày đến `2026-05-29`.
  - **Then:** Hệ thống block apply filter, hiện message ERR-QCR-001 (R010).
- **AC-08 — Hyperlink VAS**
  - **Given:** Listing có dòng với VAS = `VAS-001`.
  - **When:** User click cell `VAS-001`.
  - **Then:** Chuyển sang trang detail VAS-001 (R011).
- **AC-09 — Hyperlink Mã PO nguồn**
  - **Given:** Dòng có Mã PO = `PO-001` (mã inside).
  - **When:** User click cell `PO-001`.
  - **Then:** Chuyển sang trang detail PO-001 trên Inside (R017).
- **AC-10 — Format Sản phẩm**
  - **Given:** SKU = `SKU-001`, tên = `Vải lụa`.
  - **When:** User xem listing.
  - **Then:** Cell `Sản phẩm` = `SKU-001 – Vải lụa` (R013).
- **AC-11 — Tiêu chí đạt ratio**
  - **Given:** SKU có 10 tiêu chí, 7 đạt, 3 không đạt.
  - **When:** User xem listing.
  - **Then:** Cell `Tiêu chí đạt` = `7/10`; cell `Tiêu chí không đạt` = `3/10` (R014, R015).
- **AC-12 — Xem chi tiết Type = Bình thường**
  - **Given:** Dòng có Type = `Bình thường`.
  - **When:** User click `Thao tác` → xem chi tiết.
  - **Then:** Mở trang chi tiết kết quả đánh giá chất lượng sản phẩm (R019, R021).
- **AC-13 — Xem chi tiết Type = Nhóm UID**
  - **Given:** Dòng có Type = `Nhóm UID`.
  - **When:** User click `Thao tác`.
  - **Then:** Mở trang chi tiết kết quả đánh giá **theo từng nhóm UID** (R019, R022).
- **AC-14 — Tiêu chí lỗi 4 điểm hiển thị riêng**
  - **Given:** Kết quả có tiêu chí lỗi 4 điểm.
  - **When:** User xem chi tiết.
  - **Then:** Phần tiêu chí lỗi 4 điểm hiển thị thành 4 group (1/2/3/4 điểm), có thể thu gọn/mở rộng (R023, R024, R026).
- **AC-15 — Tổng điểm lỗi 4 điểm**
  - **Given:** Loại lỗi 1 điểm = 2 lỗi, 2 điểm = 1 lỗi, 3 điểm = 0 lỗi, 4 điểm = 1 lỗi.
  - **When:** User xem chi tiết.
  - **Then:** `Tổng chưa nhân hệ số` = 2×1 + 1×2 + 0×3 + 1×4 = 8 điểm. `Tổng đã nhân hệ số` = (formula chưa rõ — Q-003) (R025).
- **AC-16 — Tiêu chí theo bước**
  - **Given:** Kết quả có tiêu chí thiết lập theo bước (3 bước).
  - **When:** User xem chi tiết.
  - **Then:** Mỗi bước hiển thị 1 nhóm gồm `Hình ảnh`, `Kết quả ghi nhận`, `Ghi chú` (R027).
- **AC-17 — Update S-25 Web: bổ sung 2 info chi tiết**
  - **Given:** Kết quả đánh giá xã vải.
  - **When:** User xem chi tiết trên Web.
  - **Then:** Trang chi tiết có thêm `Số lượng cần đánh giá` và `Hình ảnh tem QC` (R028).
- **AC-18 — UID group `Đánh giá đạt` default = No cho SKU vải**
  - **Given:** PO mới nhận, SKU thuộc Thời trang (NVL) và là SKU vải.
  - **When:** User xem trang `Inventory / Group UID / Tab Danh sách`.
  - **Then:** Field `Đánh giá đạt` của UID group = `No` (R030).
- **AC-19 — UID group `Đánh giá đạt` transition No → Yes**
  - **Given:** UID group SKU vải đang `Đánh giá đạt = No`.
  - **When:** QC hoàn thành đánh giá xã vải với kết quả Đạt.
  - **Then:** Field transition `No → Yes` (R030).
- **AC-20 — UID group N/A cho SKU không phải Thời trang (NVL) vải**
  - **Given:** SKU thuộc category `Mỹ phẩm`.
  - **When:** User xem UID group.
  - **Then:** Field `Đánh giá đạt` = `N/A`, không transition được (R030).

## ❓ Câu hỏi chưa rõ

| Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời |
|:-----|:--------------|:--------|:-------|:-----------|:------------|:--------------|:-------------|
| Q-001 | R020, API table | Service ghi nhận kết quả đánh giá — có API endpoint cụ thể, schema request/response không? Hoặc đây là service internal (queue/message)? | Dev | Open | | | |
| Q-002 | R021, AC-12 | Update 18-09-2025 — chi tiết kết quả khi `Type = Bình thường` cụ thể có những thông tin gì? Raw chỉ có heading, không nêu format/fields. | PO/UX | Open | | | |
| Q-003 | R025, AC-15 | Công thức tính `Tổng điểm lỗi đã nhân hệ số` — hệ số nhân của từng loại lỗi (1/2/3/4 điểm) là bao nhiêu? Per SKU hay global? | PO/Dev | Open | | | |
| Q-004 | R010, ERR-QCR-001 | Verbatim VN+EN cho message khi user chọn Ngày đánh giá `Từ > Đến`. Hoặc UI block date picker mà không hiện message? | PO/UX | Open | | | |
| Q-005 | R007, R029 | `Phân loại` là 1 cột enum 5 values hay là 2 cột (nguồn + flow)? Raw có 2 bảng riêng cho `Phân loại` — verify cấu trúc thực tế. | PO/UX | Open | | | |
| Q-006 | R008 | Cột `Người đánh giá` listing — format hiển thị là 2 dòng (email + thời gian) hay 1 dòng có separator? Verbatim layout. | UX | Open | | | |
| Q-007 | R019 | Cột `Thao tác` — icon cụ thể là gì (eye/view/chevron)? Có bao nhiêu action khả dụng ngoài "xem chi tiết"? | UX | Open | | | |
| Q-008 | R030 | Khi đánh giá xã vải có kết quả `Không đạt`, field `Đánh giá đạt` giữ ở `No` hay chuyển sang status khác (vd `Failed`)? Raw chỉ nêu transition `No → Yes` khi Đạt. | PO | Open | | | |
| Q-009 | R030 | Sau khi UID group đã `Đánh giá đạt = Yes`, có cho phép đánh giá lại không? Nếu đánh giá lại kết quả `Không đạt` → transition về `No`? | PO | Open | | | |
| Q-010 | R002, R003 | "Tìm theo mã chính xác nhập vào" — match exact bao gồm khoảng trắng, case-sensitive, ký tự đặc biệt? Vd `sku-001` vs `SKU-001`. | Dev | Open | | | |

## 📝 Thay đổi so với version cũ

| Change ID | Loại thay đổi | Nội dung thay đổi | Version cũ | Version mới | Requirement/AC ảnh hưởng | Trạng thái |
|:----------|:--------------|:------------------|:-----------|:------------|:--------------------------|:-----------|
| CHG-001 | Add | Refine từ stub `partial_read: true` sang full spec sau khi đọc raw S-14, S-15, S-16, S-25 | 1.5 (stub) | 1.5 | All R + AC | Draft |
| CHG-002 | Update | Update 18-09-2025: chi tiết kết quả đánh giá tách màn hình theo Type (Bình thường vs Nhóm UID); tiêu chí lỗi 4 điểm lưu trữ + hiển thị riêng; tiêu chí theo bước có format chuẩn (Hình ảnh + Kết quả + Ghi chú) | (trước 1.5) | 1.5 | R021–R027, AC-12..AC-16 | Done (đã trong raw v1.5) |
| CHG-003 | Update | Update S-25 Web: bổ sung `Số lượng cần đánh giá` + `Hình ảnh tem QC` ở chi tiết; cột Phân loại thêm `Xã vải`; UID group bổ sung field `Đánh giá đạt` (N/A/No/Yes) với transition rule | (trước 1.5) | 1.5 | R028–R030, AC-17, AC-18, AC-19, AC-20 | Done (đã trong raw v1.5) |

## 🔎 Impact Analysis & Regression Proposal

| Change ID | Affected Feature(s) | Affected Test Suite(s) | Test Case action | Regression candidates | Open questions / Gate |
|:----------|:--------------------|:-----------------------|:-----------------|:----------------------|:----------------------|
| CHG-001 | stub_qc_evaluation_result | test_stub_qc_evaluation_result | Add (chờ Gate 1B) | [[stub_qc_criteria_setup]] (tiêu chí 4 điểm + tiêu chí theo bước), [[stub_qc_evaluation_mobile]] (input từ App), [[stub_qc_evaluation_manual]] (input Manual), [[stub_qc_vas]] (VAS detail hyperlink), [[stub_qc_uid_group]] (UID group state Đánh giá đạt) | Q-001..Q-010 Open; Gate 1B pending |

## Test Coverage

| Requirement/AC | Test Case(s) | Status | Ghi chú |
|:---------------|:-------------|:-------|:-------|
| R001..R030, AC-01..AC-20 | | ⏳ Chưa thiết kế | Chờ Gate 1B + answer Q-001..Q-010 |

## 🚧 Blocked Coverage

- R020, API service — chờ Q-001 (API/service endpoint definition)
- R021, AC-12 — chờ Q-002 (format chi tiết Type = Bình thường)
- R025, AC-15 — chờ Q-003 (công thức hệ số 4 điểm)
- R010, ERR-QCR-001, AC-07 — chờ Q-004 (verbatim message ngày từ > đến)
- R007, R029, AC-05 — chờ Q-005 (cấu trúc cột Phân loại)
- R008 — chờ Q-006 (layout cell người đánh giá)
- R019 — chờ Q-007 (icon + actions cột Thao tác)
- R030 — chờ Q-008, Q-009 (rules state Failed + đánh giá lại)
- R002, R003 — chờ Q-010 (match exact rule)

Test cases liên quan tới các R-ID trên bị block đến khi câu hỏi `Answered`.

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:------------------|:------|
| 2026-05-30 14:45:51 | v1.0 | Tách từ monster stub thành per-feature stub | split-stubs-2026-05-30 |
| 2026-05-30 18:15:00 | v1.1 | Refine stub → full spec: 30 R-ID, 20 AC, 16 BR, 1 message (verbatim missing — Q-004), 10 questions Open. `partial_read: false`. | refine-batch-3-2026-05-30 |
