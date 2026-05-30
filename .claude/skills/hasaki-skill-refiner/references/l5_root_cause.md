---
tags: [wiki-rules, reference, refiner]
status: Done
updated: 2026-05-30
---

# Refiner — Tầng L_root_cause: Skill Root Cause Analysis

> Load on-demand chỉ khi **cùng loại lỗi ≥ 2 violations trong batch** hoặc **≥ 2 sessions liên tiếp** có cùng pattern. Nếu không trigger, L5 ghi `no new patterns` 1 dòng trong `retrospective.md` và skip toàn bộ Bước 1-5.

**Mục tiêu:** Phân tích tại sao lỗi xảy ra — do conflict skill, thiếu thông tin, hay instruction chưa rõ — và đề xuất patch vào skill/rule/template.

---

## Bước 0 — Generalization check

Trước khi phân tích bất kỳ violation nào, đặt câu hỏi: *"Lỗi này đại diện cho một lớp tình huống, hay chỉ là case đặc thù của batch này?"* Câu trả lời quyết định liệu có nên viết patch hay không, và patch sẽ cover rộng đến đâu.

- **Tránh:** gắn patch vào tên field, feature, hay example cụ thể từ batch hiện tại.
- **Hướng tới:** mô tả *thuộc tính* của loại lỗi để patch áp dụng được cho mọi tình huống tương tự.
- **Ví dụ minh họa:** được phép trong patch, nhưng phải là ví dụ điển hình của lớp tình huống — không phải copy nguyên case vừa gặp.
- Nếu không tìm được cách diễn đạt tổng quát → ghi `scope: [hẹp]` để biết cần refactor sau.

---

## Bước 1 — Phân nhóm violations theo nguyên nhân gốc (Decision Tree)

Với mỗi violation, đi qua các câu hỏi theo thứ tự:

```
Q1: Lỗi xảy ra ở giai đoạn nào?
├── Khi AI đọc raw và VIẾT spec
│   ├── Template không có chỗ ghi → target: templates/
│   └── Instruction ingest thiếu/mơ hồ → target: phase_ingest.md
├── Khi AI VERIFY spec vs raw (trong refiner này)
│   ├── Layer instruction thiếu rule → target: SKILL.md tầng tương ứng
│   └── Index không đủ thông tin để detect → target: ingest step (tạo index)
├── Khi AI chạy qua GATE / workflow
│   └── Gate bị bỏ qua hoặc thứ tự sai → target: commands/ hoặc hasaki-wiki/SKILL.md
└── Hai instructions MÂU THUẪN nhau
    └── → target: cả hai files, resolve conflict

Q2: Trong nhóm đó, instruction hiện tại đang ở trạng thái nào?
├── Chưa có instruction nào về trường hợp này → Add rule
├── Có instruction nhưng không đủ rõ → Clarify / strengthen
└── Có instruction nhưng bị override bởi context khác → Reorder hoặc emphasize
```

---

## Bước 2 — Đề xuất patch

```
## PATCH-NNN: [Tên ngắn — mô tả lớp lỗi, không phải case cụ thể]
- **File:** đường dẫn file cần sửa
- **Loại:** Add / Update / Remove
- **Nội dung:** mô tả cụ thể
- **Lý do:** root cause (giai đoạn + trạng thái instruction theo decision tree)
- **Expected impact:** gate nào cải thiện
- **Trạng thái:** Pending
```

---

## Bước 3 — Counterfactual test (bắt buộc trước khi finalize patch)

Với mỗi patch đề xuất, trả lời: *"Nếu patch này đã tồn tại trước khi batch này chạy, violation có xảy ra không?"*

- Trace ngược: violation xảy ra tại bước nào → instruction nào đang thiếu/mơ hồ tại bước đó → patch có nhắm đúng chỗ đó không?
- Nếu câu trả lời là "không rõ" hoặc "có thể vẫn xảy ra" → patch đang sửa triệu chứng, không sửa nguyên nhân. Quay lại Bước 1.
- Ghi kết quả counterfactual vào patch: `**Counterfactual:** [mô tả ngắn cơ chế ngăn chặn]`

---

## Bước 4 — Apply patch

Chỉ sau khi user confirm. Đổi `Trạng thái: Pending` → `Trạng thái: ✅ Done`.

---

## Bước 5 — Ghi retrospective

Bài học có thể tái sử dụng cho session sau.

---

## Output L5

- `improvement_patch_plan.md` — cập nhật danh sách PATCH
- `retrospective.md` — append bài học mới (hoặc `no new patterns` nếu skip)
