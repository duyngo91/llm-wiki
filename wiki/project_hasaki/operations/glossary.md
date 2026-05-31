---
aliases: [Glossary, Thuật ngữ]
tags: [qa/operations, qa/glossary]
status: Draft
project: project_hasaki
created: "2026-05-31"
updated: "2026-05-31"
---

# 📚 Glossary — Thuật ngữ & Viết tắt

*Tập hợp các thuật ngữ sử dụng trong raw docs (07062, 07105) và Feature Specs. Phân loại theo: định nghĩa rõ từ raw vs. suy từ ngữ cảnh (cần PO confirm).*

---

## Thuật ngữ rõ ràng từ Raw Doc

| Term | Viết tắt | Định nghĩa (Verbatim từ Raw) | Nguồn |
|:-----|:---------|:---------------------------|:------|
| **Warehouse Management System** | WMS | Hệ thống quản lý kho | 07062#L3 |
| **Hạn Sử Dụng** | HSD | Hạn sử dụng (sản phẩm có HSD) | 07062#L1063 |
| **Nhóm UID** | Group UID | Scan nhóm UID đại diện cho cây/tấm vải được nhập hàng vào | 07062#L1692 |

---

## Thuật ngữ Suy từ Ngữ cảnh — Cần PO Confirm

| Term | Viết tắt | Suy từ Ngữ cảnh | Ví dụ từ Raw | Ghi chú |
|:-----|:---------|:------------------|:-----------|:-------|
| **Value Added Service** | VAS | Phiên dán/gắn ID cho sản phẩm sau khi nhập | "hệ thống sẽ tự động sinh VAS và auto completed" (L531) | [cần confirm] |
| **Advance Shipment Notice** | ASN | Thông báo shipment trước với chi tiết hàng | "hệ thống sẽ sinh ra 1 VAS tương ứng với ASN với status = Open" (L536) | [cần confirm] |
| **Unique Identifier** | UID | Mã định danh duy nhất cho sản phẩm | Dùng trong "Group UID", "scan UID" | [cần confirm] |
| **Radio Frequency Identification** | RFID | Công nghệ quét từ xa gắn ID cho sản phẩm | "Scan RFID để xác nhận dán ID" (L2016) | [cần confirm] |
| **Sản Phẩm Không Phù Hợp** | SPKPH | Sản phẩm không đúng yêu cầu PO, trigger return vendor | "khai báo SPKPH => sinh return vendor" (L82) | [cần confirm] |
| **Đồng kiểm** | (không viết tắt) | Kiểm tra chất lượng hàng khi nhập | "Đồng kiểm / Check of goods" (L245); "Không đồng kiểm vs Có đồng kiểm" (L909-912) | [cần confirm] |
| **Purchase Order** | PO | Đơn đặt hàng (gốc) | Dùng trong "PO chính", "PO 1", "PO sample", "PO Gift" | [cần confirm] |
| **Purchase Order Gift** | PO Gift | Phần quà tặng dính kèm PO chính | "Nhận PO Gift chung với PO thường" (L159) | [cần confirm] |
| **Purchase Order Zone** | PO Zone | PO theo vùng/kho cụ thể | "PO Zone cho Shop 170 QL1A và Kho 170 QL1A" (L60) | [cần confirm] |
| **PO Sample / PO chính** | (không viết tắt) | PO mẫu vs PO chính thức | "PO sample & PO chính" (L183) | [cần confirm] |
| **Số lô** | LOT | Mã batch sản xuất | "Sản phẩm có HSD và số lô VN" (L1063) | [cần confirm] |
| **Lot/Batch** | LOT | Lô hàng sản xuất cùng một lô | "Blocked UID group của SKU của PO cùng LOT" (L53) | [cần confirm] |
| **Xã vải** | (không viết tắt) | Phần vải dư thừa/không sử dụng từ cuộn vải | "QC xã vải" (L35); "Các SKU thuộc category... tên sản phẩm có từ 'Vải'" (L1686) | [cần confirm] |
| **Packing list** | (không viết tắt) | Danh sách chi tiết sản phẩm trong kiện hàng | "Packing list PO: Update template import" (L130) | [cần confirm] |
| **Bin** | (không viết tắt) | Thùng/giỏ chứa hàng trong kho | "mã Bin hay mã giỏ để chuyển hàng vào" (L960) | [cần confirm] |
| **Inside** | (không viết tắt) | Hệ thống back-end quản lý PO (khác WMS) | "Gọi Inside update PO Receiving" (L34); "Mapping status PO giữa Inside và WMS" (L264-265) | [cần confirm] |
| **Stock Keeping Unit** | SKU | Mã sản phẩm duy nhất trong hệ thống | Dùng khắp trong cả 2 raw | [cần confirm] |
| **Serial Number / IMEI** | Serial/Imei | Mã định danh sản phẩm (IMEI cho điện thoại/thiết bị) | "Xoá SKU có HSDK hoặc Serial đã scan" (L30); "update serial/imei/label code" (L48-49) | [cần confirm] |

---

## ❓ Câu hỏi chưa rõ

| Q-ID | Câu hỏi | Hỏi ai | Trạng thái |
|:-----|:--------|:-------|:-----------|
| Q-GLOSSARY-001 | Raw glossary section (07062#L198-206 + 07105#L102-110) đều **rỗng** (chỉ placeholder). Cần PO cung cấp định nghĩa chính thức cho **18 thuật ngữ suy từ ngữ cảnh** để bịt lỗ này. | PO / BA | Open |

---

## 📝 Ghi chú

- **Phạm vi:** Glossary này gom các term DÙNG NHIỀU trong cả 2 raw docs (Receiving PO v2.17 + Quality Control v1.5) + feature specs liên quan.
- **Chuẩn:** Ưu tiên định nghĩa verbatim từ raw (3 term). Các term còn lại suy từ ngữ cảnh và cần PO xác nhận.
- **Cập nhật:** Mỗi khi phát hiện term mới hoặc PO cung cấp definition → update bảng thứ 2 hoặc move sang bảng thứ 1.

---

## 📅 Changelog

| Thời gian | Version | Nội dung thay đổi | Nguồn |
|:----------|:--------|:-----------------|:------|
| 2026-05-31 | v1.0 | Khởi tạo glossary từ 2 raw docs; 3 term rõ + 18 term cần confirm | Wave 2 / 07062 + 07105 |
