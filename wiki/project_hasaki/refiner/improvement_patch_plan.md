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
