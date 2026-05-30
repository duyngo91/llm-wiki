# Improvement Patch Plan

> Refiner skill patches dựa trên cùng-loại-violation lặp. Append-only.

---

## 2026-05-30 / pilot-batch-1

**no patches required** — L_root_cause short-circuit (no patterns lặp). See `2026-05-30_pilot-batch-1/refiner_report.md` cho FIX-001 (UNCLEAR fix suggestion — Medium priority).

### FIX-001 — Applied 2026-05-30 23:00

- **Target:** `wiki/project_hasaki/features/stub_receiving_po_gift.md`
- **Changes applied by user request:**
  1. R005 claim text — thêm `**Lưu ý:**` inline note giải thích spec interpretation và link Q-007. Cột Testable đổi từ ✅ sang ⚠️ để phản ánh status pending PO confirm.
  2. `## ❓ Câu hỏi chưa rõ` — thêm Q-007 capture raw typo (gift→gốc) cần PO clarify.
  3. `## 🚧 Blocked Coverage` — thêm dòng "R005, AC-05 — chờ Q-007".
  4. Changelog — append v1.2 entry.
  5. Frontmatter `approval_note` updated từ "FIX-001 pending" → "FIX-001 applied... Awaits PO Gate 1B answer".
- **Verify:** `check_ingest.py` exit 0 sau apply; Q count 245 → 246 (Q-007 ingested).

### Pending observations (advisory, không phải patch)

1. **Index.json flags chưa được set** cho 5 pilot sections (S-13, S-34, S-35, S-36, S-37, S-60, S-61) mặc dù spec content có:
   - Error messages (S-13 5 confirm, S-36/S-60 verbatim, S-34 verbatim)
   - Business rules + Validation rules (tất cả 5 sections)
   - State transition (S-60 R009, S-13 R003/R004/R007)
   - Enum (S-13 status, S-60 PO type, S-36 popup type)
   
   → Khi có nhiều specs verify hơn, considera patch `index_skeleton.py` để auto-detect và set flags theo spec content. Hoặc viết script utility `index_flag_updater.py` đọc spec → cross-check → update index flags. Để observation pending tới khi pattern lặp ≥ 2 session.

2. **PowerShell + Python UTF-8 stdout encoding** — recurring across batches (CP1252 fallback gây UnicodeEncodeError). Workaround đã có: `$env:PYTHONUTF8="1"` trước khi gọi `py`. Đã document trong `.claude/rules/05-language-and-encoding.md`. Không phải refiner skill patch.

---

## 2026-05-30 / spec-scoped-batch-2

**no skill patches applied** — 2 FIX suggestions (FIX-002, FIX-003) generated cho `stub_qc_criteria_sku.md` only, không phải skill patch. Xem `2026-05-30_spec-scoped-batch-2/refiner_report.md` cho chi tiết.

### FIX-002 — Applied 2026-05-30 21:30

- **Target:** `wiki/project_hasaki/features/stub_qc_criteria_sku.md`
- **Changes applied:**
  1. R008 (dòng 55) — Testable đổi từ ✅ sang ⚠️; claim text thêm note "(spec interpretation — raw L249 có raw typo, chờ Q-011)".
  2. `## ❓ Câu hỏi chưa rõ` — thêm Q-011 cho raw typo `Đến ngày phải ≥ đến ngày`.
  3. `## 🚧 Blocked Coverage` — thêm `R008 — chờ Q-011`.
  4. Test Coverage + Impact Analysis Q range cập nhật `Q-001..Q-012`.
  5. Changelog — append v1.2 entry.
  6. Frontmatter `approval_note` updated; `last_verified_at` → `21:30:00`.

### FIX-003 — Applied 2026-05-30 21:30

- **Target:** `wiki/project_hasaki/features/stub_qc_criteria_sku.md`
- **Changes applied:**
  1. R027 (dòng 74) — Testable đổi từ ✅ sang ⚠️; claim text thêm note "(raw chỉ explicit Sai số ở `=`, scope cho 4 toán tử còn lại chờ Q-012)".
  2. `## ❓ Câu hỏi chưa rõ` — thêm Q-012 cho Sai số applicability.
  3. `## 🚧 Blocked Coverage` — thêm `R027, AC-08 — chờ Q-012`.
- **Verify:** `check_ingest.py` exit 0 sau apply; encoding OK (no BOM/mojibake).

### Cross-session pattern (tracked, NOT auto-patched yet)

**Pattern:** "Silent spec interpretation when raw is ambiguous/typo" — 3 instances qua 2 sessions:
1. pilot-batch-1 FIX-001: `stub_receiving_po_gift` R005 "gift→gốc" typo correction
2. spec-scoped-batch-2 FIX-002: `stub_qc_criteria_sku` R008 "Đến ngày phải ≥ đến ngày" raw typo
3. spec-scoped-batch-2 FIX-003: `stub_qc_criteria_sku` R027 Sai số applicability assumption

**Patch candidate (defer):** Update `.claude/skills/hasaki-wiki/references/phase_test_design.md` checklist hoặc tạo new refinement template hint: *"Mỗi R-ID có spec text ≠ raw verbatim → bắt buộc có Q-ID kèm raw quote."*

**Decision:** Chờ ≥ 3 sessions consecutive (đã 2). Nếu session-3 phát hiện cùng pattern → apply patch chính thức.

### Scripts inventory cleanup — Resolved 2026-05-30 21:50

Review 23 scripts trong `.claude/scripts/` phát hiện gap visibility:

1. **Wire spec-verifier scripts vào SKILL.md** ✅ — thêm "Helper scripts" subsection trong `hasaki-spec-verifier/SKILL.md` ref `refiner_writeback.py` + `index_flag_updater.py` + `refiner_findings_diag.py`. Cũng add vào `hasaki-wiki/references/shared.md` Scripts table cho discoverability cross-skill.
2. **Fix BOM** ✅ — `reset_project.py` + `sync_my_open_tasks.py` start byte `EF BB BF` → strip. AST parse OK sau fix.
3. **Add docstring** ✅ — 6 scripts thiếu (`change_impact`, `generate_stub_features_from_index`, `mcp_health_check`, `wiki_sync`, `wiki_sync_core`, `reset_project`, `sync_my_open_tasks`) đều có module docstring đầy đủ mô tả purpose + usage + caveats.
4. **`sync_my_open_tasks` vs `hasaki_my_tasks` overlap** ✅ — confirm KHÔNG overlap: `sync_my_open_tasks` là WRITE side (snapshot + task_spec + Kanban update); `hasaki_my_tasks` là READ side (scan + diff + download HSK-centric). Docstring clarify khác biệt.
5. **Wire `spec_status_dashboard.py`** ✅ — thêm vào `hasaki-wiki/references/shared.md`. Đáng giữ: 24 specs total breakdown by status per feature group.

### Pending observations (continued from pilot-batch-1)

3. **Index flags=[] cho mọi sections trong batch-2** (S-05, S-06, S-07, S-08, S-17, S-18) — cùng pattern observation #1 từ pilot-batch-1. ~~Defer auto-flag-update script.~~ **RESOLVED 2026-05-30 21:35** — `.claude/scripts/index_flag_updater.py` đã tồn tại sẵn (AI session này mới phát hiện). Applied cho 6 sections của 3 specs batch-2: tất cả 6 flags → True. `check_ingest.py` exit 0 sau apply. Legacy fix cho ~18 sections của pilot-batch-1 + chưa-verify specs còn pending — chạy `py .claude/scripts/index_flag_updater.py --project project_hasaki --apply` (không filter specs) khi sẵn sàng.
