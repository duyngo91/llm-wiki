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

---

## 2026-05-31 / spec-scoped-batch-3

**3 FIX suggestions** (FIX-004 mobile INF-01, FIX-005 OMIT-01 App SL/tem QC, FIX-006 MISS-01 cross-ref xã vải/PO sample) — xem `2026-05-31_spec-scoped-batch-3/refiner_report.md`. Pending user confirm, chưa apply.

### PATCH-001 — Cross-session pattern reached threshold (≥3 sessions) — Pending

- **File:** `.claude/rules/20-no-inference.md`
- **Loại:** Add (strengthen existing no-inference policy)
- **Nội dung:** Thêm rule item:
  > **Verbatim-deviation trace:** Khi spec text của một R-ID / Business Rule / AC **khác raw verbatim** (do correction typo, generalization, đặt placeholder, suy công thức, hoặc assumption về scope), BẮT BUỘC kèm theo: (1) một `Q-ID` trong `## ❓ Câu hỏi chưa rõ` cùng raw quote nguyên văn, và (2) dòng tương ứng trong `## 🚧 Blocked Coverage`. Không được điền vào khoảng trống của raw bằng giá trị/công thức cụ thể (vd raw "10%" → KHÔNG tự viết `ceil(n × 0.10)`; raw typo → KHÔNG silently sửa rồi mark SUPPORTED). Giữ verbatim raw + đẩy phần suy diễn sang Q.
- **Lý do (root cause theo decision tree):** Giai đoạn = "AI đọc raw và VIẾT spec" (refinement). Trạng thái instruction = "có nhưng không đủ rõ" — `20-no-inference.md` cấm suy diễn requirement + có Enum-completeness rule, nhưng chưa explicit cho lớp "verbatim deviation phải kèm Q-ID + raw quote". Clarify/strengthen.
- **Expected impact:** Cải thiện `L_INFERENCE_PASS` — giảm INFERRED/UNCLEAR sót ở batch sau; mọi deviation đều có audit trail (Q-ID + raw quote) để reviewer trace, không cần refiner phát hiện lại.
- **Counterfactual:** Nếu patch tồn tại trước batch-3 → INF-01 không xảy ra (AI buộc giữ "10% số lượng cây vải của lô" verbatim + Q-ID thay vì tự suy `ceil()`). Nhắm đúng giai đoạn VIẾT, không phải verify. PASS.
- **Pattern history (4 instances / 3 sessions):** pilot-batch-1 FIX-001 (gift→gốc typo); batch-2 FIX-002 (Đến ngày ≥ typo) + FIX-003 (Sai số scope); batch-3 FIX-004 (10% → ceil formula).
- **Trạng thái:** ✅ Applied 2026-05-31 — thêm vào `.claude/rules/20-no-inference.md` dòng "Verbatim-deviation trace".

### Pending observations (continued)

4. **Out-of-feature content lẫn trong line-range của spec khác** — raw `07105#L1128-L1147` (App UID SL + tem QC) và `L1152-L1168` (xã vải transfer + PO sample mapping) nằm trong line-range manual (L1023-L1304) nhưng nội dung thuộc feature App / xã vải / PO sample. Hiện tượng: range-based splitting cắt theo line, không theo semantic boundary → content có thể bị orphan (không spec nào own) hoặc bị gán nhầm spec. Observation — nếu lặp ≥2 session, considera patch quy trình split-stubs để align section boundary với heading nghiệp vụ thay vì line cứng.

---

## 2026-05-31 / spec-scoped-batch-7

**2 FIX suggestions** (FIX-001 date_rules typo VN "tối thiếu" silent-fix thiếu Q-ID; FIX-002 packing_list AC-20 raw VD 180-vs-formula-Width-1.5 silent resolution) — cả 2 mức Low (MISSING_DETAIL), xem `2026-05-31_spec-scoped-batch-7/refiner_report.md`. Pending user confirm, chưa apply. **Không block verdict PASS 4/4.**

### PATCH-002 — Candidate (NOT applied) — raw-internal inconsistency silent-resolution

- **File (target):** `.claude/rules/20-no-inference.md` (mở rộng PATCH-001) HOẶC checklist phase ingest `.claude/skills/hasaki-wiki/references/phase_*.md`
- **Loại:** Add example/clarification (strengthen PATCH-001, KHÔNG tạo rule mới độc lập)
- **Nội dung đề xuất:**
  > **Raw-internal inconsistency:** Khi cùng một tài liệu raw có 2 chỗ mâu thuẫn nhau (vd formula dùng `Width=1.5m` nhưng VD tính plug `180`; VN ghi "chữ và số" nhưng message ghi "chữ số"; VN≠EN về mã/nội dung; typo cần sửa), KHÔNG được resolve im lặng bằng cách chọn 1 nhánh rồi mark SUPPORTED. Bắt buộc: (1) giữ verbatim CẢ HAI nhánh raw; (2) thêm `Q-ID` raw-internal-inconsistency nêu rõ 2 chỗ mâu thuẫn + line; (3) dòng Blocked Coverage. AC illustration không được tính giá trị cụ thể từ nhánh chọn mà không trace Q-ID.
- **Lý do (decision tree):** Giai đoạn = "AI đọc raw + VIẾT spec" (refinement). PATCH-001 đã cover "spec text ≠ raw verbatim → Q-ID" nhưng chưa explicit cho trường hợp **raw tự mâu thuẫn** và spec phải chọn nhánh. Clarify/strengthen, không phải gap policy mới.
- **Pattern history (4 instances liên tiếp / batch-3→7):**
  - batch-5 (#1): invoice "chữ và số" L1521 vs message "chữ số" L1525 → FIX-003 + Q-013 (spec xử lý ĐÚNG, có Q-ID).
  - batch-6 (#2): APP ERR-APP-004 VN≠EN L997-1002 → Q-004 (spec xử lý ĐÚNG, có Q-ID).
  - batch-7 (#3): packing_list AC-20 raw VD `180` ≠ formula Width `1.5` → spec resolve IM LẶNG → 54.69 Yard (KHÔNG Q-ID) → FIX-002.
  - batch-7 (#4): date_rules R001 raw VN typo "tối thiếu" → spec silent fix "tối thiểu" (KHÔNG Q-ID) → FIX-001.
- **Counterfactual:** Nếu PATCH-002 tồn tại trước batch-7 → 2 instance #3/#4 đã đính Q-ID raw-internal-inconsistency thay vì silent resolution → FIX-001/002 không phát sinh. Nhắm đúng giai đoạn VIẾT. PASS.
- **Trạng thái:** Candidate — **chờ user confirm + pass quality gates.** Lưu ý: batch-5/6 spec đã xử lý đúng (có Q-ID) → pattern này một phần đã được PATCH-001 cover; PATCH-002 chỉ là làm rõ phạm vi + cấm silent resolution. Cân nhắc apply nhẹ (thêm 1 dòng ví dụ vào PATCH-001) thay vì rule riêng.

### Pending observations (continued)

5. **Index flags={} cho 4 specs batch-7** — confirm_paste_id, vas_manual, date_rules, packing_list trong raw `*_index.json` đều `flags={}` dù content có enum (10 enum)/error_messages (39)/business_rule (106)/formula (6)/state_transition. Cùng observation #1/#3 (đã có script `index_flag_updater.py`). → chạy `index_flag_updater.py --specs <4 specs> --apply` ở write-back. Read-only dry-run đã verify cần apply.
