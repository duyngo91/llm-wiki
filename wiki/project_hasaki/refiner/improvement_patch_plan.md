# Improvement Patch Plan

> Append-only. Đánh số PATCH liên tiếp. Chỉ apply sau khi user confirm.

---

## PATCH-001: Bắt buộc toàn bộ 14 sections ngay cả trong stub spec

- **File:** `.claude/skills/hasaki-wiki/references/phase_ingest.md`
- **Loại:** Update
- **Nội dung:** Thêm quy tắc rõ ràng vào Workflow 2.1 (Bước 2b): "Stub spec (`partial_read: true`) phải có đủ 14 mục bắt buộc như spec đầy đủ. Mục chưa đọc được → ghi placeholder `> Chưa đủ dữ liệu — STUB, cần đọc trang [X–Y] của raw source`. Xem `receiving_po_app.md` làm mẫu stub chuẩn."
- **Lý do:** 4 stub specs trong batch này (confirm_paste_id, vas_manual, packing_list, fabric_uid_group) thiếu nhiều sections vì instruction không enforce đủ. Chỉ spec receiving_po_app.md (tạo đầu tiên) được làm đúng. Thiếu consistency làm L1 fail.
- **Expected impact:** L1_FORMAT_PASS gate sẽ pass cho các stubs trong các batch tiếp theo.
- **Trạng thái:** ✅ Done (2026-05-26) — Refactored: bỏ reference file cụ thể, dùng principle "cấu trúc template bất biến bất kể content availability"

---

## PATCH-002: Giá trị chính xác phải copy verbatim trong L3 (generalized)

- **File:** `.claude/skills/hasaki-skill-refiner/SKILL.md`
- **Loại:** Update
- **Nội dung:** Thay 2 bullets cũ (Numeric threshold + Format string) bằng 1 bullet chung "Giá trị chính xác": mọi giá trị machine-comparable (số ngưỡng, count, length, percentage, datetime format, regex, error code) phải copy verbatim. Spec khác raw → INFERRED. Giá trị trong raw trông bất thường so với standard của loại dữ liệu → UNCLEAR.
- **Lý do (general):** Bất kỳ giá trị cụ thể nào — dù là số ngưỡng, format string, hay pattern — đều xác định test boundary. Normalize hay re-interpret dù "có vẻ tương đương" là nguồn gốc của INFERRED. Rule phải cover toàn bộ loại giá trị, không chỉ từng trường hợp riêng lẻ.
- **Expected impact:** L3_NO_INFERENCE_PASS bền vững qua mọi loại requirement, không chỉ numeric.
- **Trạng thái:** ✅ Done (2026-05-26)

---

## PATCH-003: Phát hiện giá trị bất thường trong Question Lifecycle (generalized)

- **File:** `.claude/skills/hasaki-wiki/references/phase_ingest.md`
- **Loại:** Update
- **Nội dung:** Thay bullet "Format string bất thường" bằng "Giá trị trông bất thường" — áp dụng cho bất kỳ loại giá trị nào inconsistent với standard của loại dữ liệu đó: format thiếu component, số ngưỡng không hợp lý, enum value lẻ loi trong nhóm, pattern trông như typo. Action: mark UNCLEAR + câu hỏi, không assume raw correct.
- **Lý do (general):** Raw source là do con người viết và có thể chứa typo ở bất kỳ loại giá trị nào. Rule phải áp dụng cho toàn bộ loại "giá trị kỳ lạ", không chỉ datetime format.
- **Expected impact:** QA không tạo test data dựa trên giá trị sai/typo trong raw source.
- **Trạng thái:** ✅ Done (2026-05-26)
