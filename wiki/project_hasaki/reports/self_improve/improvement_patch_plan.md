---
status: Active
updated: 2026-05-25
---

# Improvement Patch Plan

| Patch | File | Loại | Expected impact | Trạng thái |
|:------|:-----|:-----|:----------------|:-----------|
| PATCH-001: Source line reference | `phase_ingest.md` | Update | Giảm INFERRED do missed enum | ✅ Done |
| PATCH-002: `partial_read` frontmatter | `tpl_requirement.md` | Add | Phân biệt spec đầy đủ vs stub | ✅ Done |
| PATCH-003: Enum completeness rule | `20-no-inference.md` | Add | Ngăn partial enum list | ✅ Done |
| PATCH-004: Fix paths + sampling strategy | `hasaki-skill-refiner/SKILL.md` | Update | Reproducibility, correct paths | ✅ Done |
| PATCH-005: Scoring table + phase traceability | `hasaki-skill-refiner/SKILL.md` | Update | Consistent scoring across sessions | ✅ Done |
| PATCH-006: Tách Phase A/B, reading order | `hasaki-skill-refiner/SKILL.md` | Update | Scope control, fewer missed claims | ✅ Done |
| PATCH-007: quality_gates.json append format | `quality_gates.json` schema | Update | Trend tracking across sessions | ✅ Done |
| PATCH-008: improvement_patch_plan format | `hasaki-skill-refiner/SKILL.md` | Add | Consistent patch documentation | ✅ Done |

---

## Chi tiết

### PATCH-001: Source line reference
- **File:** `.claude/skills/hasaki-wiki/references/phase_ingest.md`
- **Loại:** Update
- **Nội dung:** Source format phải là `[doc_name]#[line]` (ví dụ: `07062#234-239`)
- **Lý do:** Không có line anchor → không verify được → bỏ sót enum values
- **Expected impact:** Giảm INFERRED claims, reviewer có thể verify trực tiếp
- **Trạng thái:** ✅ Done

### PATCH-002: `partial_read` frontmatter
- **File:** `templates/tpl_requirement.md`
- **Loại:** Add
- **Nội dung:** Thêm `partial_read: false` và `partial_read_note: ""` vào frontmatter
- **Lý do:** Stub files bị nhầm là spec đầy đủ
- **Expected impact:** Reviewer và verify script phân biệt được stub vs full
- **Trạng thái:** ✅ Done

### PATCH-003: Enum completeness rule
- **File:** `.claude/rules/20-no-inference.md`
- **Loại:** Add
- **Nội dung:** Claim về enumeration phải liệt kê đủ tất cả values; không chắc đủ → UNCLEAR
- **Lý do:** R3 bỏ sót "Completed" vì không verify count
- **Expected impact:** Ngăn lỗi missed enum value
- **Trạng thái:** ✅ Done

### PATCH-004: Fix paths + sampling strategy
- **File:** `.claude/skills/hasaki-skill-refiner/SKILL.md`
- **Loại:** Update
- **Nội dung:** Sửa `.Codex/` → `.claude/`, `python` → `py`, thêm sampling rule "mỗi 5 lấy 1"
- **Lý do:** Đường dẫn sai → VERIFY_PASS không chạy được; "20% ngẫu nhiên" không thực hiện được
- **Expected impact:** Script chạy đúng; sampling tái lặp được
- **Trạng thái:** ✅ Done

### PATCH-005: Scoring table + phase traceability
- **File:** `.claude/skills/hasaki-skill-refiner/SKILL.md`
- **Loại:** Add
- **Nội dung:** Bảng trọng số cố định (NO_INFERENCE=30, VERIFY=25, TRACEABILITY=15...); TRACEABILITY_PASS định nghĩa theo 4 giai đoạn
- **Lý do:** Score mỗi session tự bịa ra → không nhất quán; TRACEABILITY rubber-stamp
- **Expected impact:** Score reproducible; gate TRACEABILITY có teeth
- **Trạng thái:** ✅ Done

### PATCH-006: Tách Phase A/B, thứ tự đọc
- **File:** `.claude/skills/hasaki-skill-refiner/SKILL.md`
- **Loại:** Update
- **Nội dung:** Phase A (verify) và Phase B (meta-improve) tách biệt; thứ tự đọc: spec trước → liệt kê claim → grep raw
- **Lý do:** Scope quá lớn; đọc raw trước dễ bỏ sót claim
- **Expected impact:** Phase A nhanh hơn; fewer missed claims
- **Trạng thái:** ✅ Done

### PATCH-007: quality_gates.json append format
- **File:** `wiki/project_hasaki/reports/self_improve/quality_gates.json`
- **Loại:** Update
- **Nội dung:** Đổi từ object đơn sang `{"sessions": [...]}` — mỗi lần chạy append entry mới
- **Lý do:** Ghi đè → mất trend data; không biết quality tốt lên hay xấu đi
- **Expected impact:** Trend tracking theo thời gian
- **Trạng thái:** ✅ Done

### PATCH-008: improvement_patch_plan format
- **File:** `.claude/skills/hasaki-skill-refiner/SKILL.md`
- **Loại:** Add
- **Nội dung:** Template chuẩn cho `improvement_patch_plan.md` với summary table + chi tiết PATCH-NNN
- **Lý do:** Mỗi session tạo file trông khác nhau → khó đọc lại
- **Expected impact:** Consistent patch documentation
- **Trạng thái:** ✅ Done

---

## Deferred

| Patch | Mô tả | Lý do defer |
|:------|:------|:------------|
| PATCH-D01: Auto enum grep script | Script tự động grep "Giá trị:" trong raw và diff với spec | Cần tooling; không urgent |
| PATCH-D02: Test suite verification | Hướng dẫn verify TC → AC → R → Raw | Chưa có test suite trong project |
