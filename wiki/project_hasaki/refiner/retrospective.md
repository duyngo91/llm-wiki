# Retrospective — Refiner Skill Patches

> Append-only. Mỗi entry là 1 lesson hoặc skill patch.

---

## 2026-05-30 / pilot-batch-1

**no new patterns** — first refiner session, không có cùng-loại-violation ≥ 2 trong batch (chỉ 1 UNCLEAR). L_root_cause short-circuit applied.

---

## 2026-05-30 / spec-scoped-batch-2

**Pattern phát hiện (cross-session):** "Silent spec interpretation when raw is ambiguous/typo" — 2 instances trong batch này (FIX-002 R008 typo Đến/Từ ngày, FIX-003 R027 Sai số scope) + 1 instance pilot-batch-1 (gift→gốc, applied FIX-001). Tổng 3 instances qua 2 sessions.

**Skill patch candidate (advisory, NOT applied):** Thêm checklist item vào template refinement (`.claude/skills/hasaki-wiki/references/phase_test_design.md` hoặc tương đương) yêu cầu: *"Đối với mỗi R-ID, nếu spec text ≠ raw verbatim (correction, generalization, condition-stripping), bắt buộc có Q-ID tương ứng trong `## ❓ Câu hỏi chưa rõ` section, kèm raw quote trong câu hỏi."*

**Decision:** Defer auto-patch — chờ ≥ 3 sessions xác nhận pattern. Track trong `improvement_patch_plan.md` Pending observations.

**Cross-cutting observation cũ vẫn pending:** Index `flags=[]` cho mọi sections (S-05, S-06, S-07, S-08, S-17, S-18 trong batch này) dù spec content có enum/state_transition/business_rule/error_messages/formula. Cùng observation như pilot-batch-1. Defer.
