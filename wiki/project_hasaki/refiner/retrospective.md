# Retrospective — Lessons Learned

> Append-only. Mỗi session thêm bài học mới.

---

## Session 2026-05-26 — Batch 07062 + 07105

### Bài học 1: Stub format phải enforce ngay từ đầu

**Gốc rễ:** receiving_po_app.md (stub đầu tiên được tạo) có đủ 14 section placeholders. 4 stubs tiếp theo (confirm_paste_id, vas_manual, packing_list, fabric_uid_group) bị tạo thiếu nhiều sections. Khi tạo nhiều stubs liên tiếp, AI có xu hướng tối giản để tiết kiệm effort — nhưng thiếu section headers làm phá vỡ 14-mục invariant của feature spec.

**Bài học:** Stub spec chuẩn phải luôn có đủ 14 section headers. Chỉ nội dung bên trong mới được thay bằng placeholder "> Chưa đủ dữ liệu". Format structure phải intact — giống như xây khung nhà trước khi đổ xi măng.

**Áp dụng lần sau:** Khi tạo stub, dùng receiving_po_app.md làm template reference. Luôn kiểm tra có đủ 14 headers không trước khi save.

---

### Bài học 2: Numeric threshold cần verify exact — không "normalize"

**Gốc rễ:** Raw source line 612 ghi "số lượng đã dán > 1" (hơn 1 item). Feature spec ghi "> 0" (bất kỳ item nào). AI có thể đọc "> 1" và interpret là "ít nhất 1 item tồn tại" → convert sang "> 0" vì nghĩ logic tương đương. Nhưng "> 0" và "> 1" là hai boundary condition khác nhau cho test case.

**Bài học:** Khi verify numeric threshold (> N, ≥ N, = N), phải so sánh exact với raw. "Ít nhất 1 item > 1" có thể có UX rationale khác với "> 0" — đừng assume equivalence.

**Áp dụng lần sau:** Trong L3 verify, với mọi numeric threshold: copy số từ raw, so sánh exact với spec. Nếu khác → INFERRED ngay, không analyze why.

---

### Bài học 3: Format string "YYYY-MM-DD HH:SS" — raw typo hay intentional?

**Gốc rễ:** Raw source 07105 line 163 ghi "YYYY-MM-DD HH:SS" (HH = giờ, SS = giây, thiếu MM = phút). Standard datetime format là HH:MM:SS. Spec đã copy đúng từ raw nhưng format trông bất thường.

**Bài học:** Khi raw ghi format string trông không chuẩn (thiếu component, ký tự bất thường), nên mark UNCLEAR và hỏi Dev thay vì copy blind. Test case validation sẽ depend vào format string đúng.

**Áp dụng lần sau:** Double-check format strings (datetime, regex pattern, code format) bằng cách so với known standards. Nếu bất thường → UNCLEAR + question, không accept as-is.

---

### Bài học 4: S-19 unmapped phát hiện qua index scan

**Gốc rễ:** S-19 (Update 17-05-2026 — PO Sample & Multi-user) tồn tại trong index với coverage_status: unmapped. L2 scan index là mechanism duy nhất phát hiện gap này — không thể tìm thấy bằng cách đọc feature specs.

**Bài học:** L2 index scan quan trọng hơn đọc feature specs để phát hiện coverage gap. Index là "map" — nếu không có L2 scan, unmapped sections sẽ bị bỏ qua mãi mãi.

**Áp dụng lần sau:** Luôn chạy L2 index scan đầu tiên, trước khi đọc bất kỳ feature spec nào. Liệt kê tất cả sections có coverage_status ≠ "full" ngay từ đầu session.
