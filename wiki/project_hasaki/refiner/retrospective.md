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

---

## 2026-05-31 / spec-scoped-batch-3

**Pattern threshold đạt (≥3 sessions consecutive):** Lớp lỗi *"Silent spec interpretation/generalization khi raw thiếu chi tiết hoặc có typo — spec điền khoảng trống mà không kèm Q-ID + raw quote"* xác nhận instance thứ 4 trong session này: `stub_qc_evaluation_mobile` BR "10% group UID" → spec tự suy `ceil(lot_uid_count × 0.10)` (INF-01 / FIX-004), trong khi raw `07105#L902-L904` chỉ nói "10% số lượng cây vải của từng lô" + VD. Cộng 3 instance 2 session trước (gift→gốc, Đến ngày ≥ typo, Sai số scope) → 4 instances / 3 sessions.

**Quyết định:** Defer condition ("chờ ≥3 sessions") từ batch-2 đã pass → đề xuất **PATCH-001** chính thức vào `.claude/rules/20-no-inference.md` (Verbatim-deviation trace rule). Counterfactual PASS. **Pending user confirm — KHÔNG auto-apply.**

**Lesson tái sử dụng:** Khi refine stub → full, mọi spec text khác raw verbatim (formula, enum count, typo-fix, scope assumption) phải đính Q-ID + raw quote ngay lúc viết, không để refiner phát hiện ngược ở L_inference. Đây là defect-prevention rẻ hơn nhiều so với verify-then-fix.

**Observation mới (defer):** Range-based stub splitting cắt theo line cứng làm content out-of-feature (App UID SL/tem QC `L1128-L1147`; xã vải/PO sample `L1152-L1168`) lẫn vào line-range manual → risk orphan/misattributed. Track tới khi lặp ≥2 session.

**no skill patch auto-applied** — PATCH-001 ở trạng thái Pending; chỉ apply sau user confirm + pass quality gates.

---

## 2026-05-31 / spec-scoped-batch-4

**no new patterns** — PATCH-001 (apply ở batch-3) lần đầu kiểm chứng trên data thật và bắt đúng 2 deviation cùng lớp "spec interpret/generalize beyond raw không trace Q-ID":
- `stub_qc_uid_group` BR `Tiêu chí PO chính map PO sample` → spec tự thêm "giá trị PO sample đạt **thấp nhất**" (min-aggregation) trong khi raw `07105#L1160-L1168` chỉ nói "dựa vào điều kiện của tiêu chí trên PO sample" + 1 ví dụ → INFERRED / FIX-001. Mâu thuẫn nội bộ với chính Q-006 của spec.
- `stub_qc_criteria_setup` R002 → spec interpret typo raw L141 "Đến ngày ≥ đến ngày" thành "Đến ngày ≥ Từ ngày" mà chưa có Q-ID → UNCLEAR / FIX-002 (PATCH-001 violation).

Cả 2 đều thuộc lớp PATCH-001 đã cover — không có pattern MỚI. L_root_cause short-circuit (không có cùng-loại-violation ≥2 là lỗi spec thật + không có pattern mới). PATCH-001 chứng minh hiệu quả: nếu refine tuân PATCH-001 ngay lúc viết, 2 fix này đã không phát sinh.

**Observation (vẫn defer, chưa lặp đủ):** Range-based stub splitting (batch-3 note) — batch-4 không tái xuất hiện rõ rệt (uid_group đã gom App UID L1128-1147 + PO sample L1160-1168 đúng feature). Giữ defer, chưa đủ ≥2 session liên tiếp để patch.

**Pending-source handling đúng (positive lesson):** `ERR-UIG-001/002` — spec ghi "(raw không có verbatim — Q-002)" thay vì bịa message text. Đây là cách xử lý ĐÚNG khi validation requirement có thật nhưng message verbatim không tồn tại trong raw → UNCLEAR/pending, không phải PHANTOM, không trừ điểm. Pattern tốt nên giữ làm reference.

---

## 2026-05-31 / spec-scoped-batch-5

**no new patterns** — batch đầu tiên dùng source doc khác (`07062_Receiving_PO_Docs_ver2.17.md`, không phải 07105 QC). 71 critical claim SUPPORTED, **0 violation severity ≥ INFERRED**. PATCH-001 tiếp tục hoạt động đúng: mọi deviation interpretive (typo `Desciption`→Q-005 overview, typo `kiếm`→Q-005 invoice, typo `tren`→Q-004, verbatim missing→Q-009/Q-010, raw truncated R028→Q-010) đều đã đính Q-ID ngay lúc refine. Đây là bằng chứng PATCH-001 chuyển từ verify-then-fix sang defect-prevention thành công — batch-5 không sinh fix cho deviation thiếu Q-ID nào.

**Pending-source handling tái xác nhận đúng:** `MSG-INV-005..008` (invoice) — 4 message verbatim chưa có trong raw → spec ghi "(chưa có verbatim — Q-009)" thay vì bịa. UNCLEAR/pending, không trừ điểm. Cùng pattern tốt như ERR-UIG-001/002 (batch-4). R028 raw bị cắt giữa câu ("Thông báo xác nhận đổi thành" + dòng trống) → spec flag Q-010 đúng, không suy diễn nội dung message.

**Watch-item MỚI (chưa đủ ngưỡng patch, 1 instance):** *Raw-internal inconsistency* — invoice rule R003/R004 mô tả Tax code/Serial "1-8 ký tự bao gồm **chữ và số**" (alphanumeric, raw L1521) nhưng error message verbatim ghi "phải từ 1 đến 8 **chữ số**" (digits only, raw L1525). Spec giữ cả 2 verbatim đúng nhưng KHÔNG có Q-ID bắt mâu thuẫn → FIX-003 đề xuất thêm Q-013. Khác với lớp PATCH-001 (spec interpret beyond raw): đây là **nguồn raw tự mâu thuẫn**, spec không sai khi quote, nhưng nên flag Q để dev/PO disambiguate. Mới 1 lần → defer, theo dõi tới khi lặp ≥2 session thì cân nhắc thêm checklist item "raw self-contradiction → bắt buộc Q-ID" vào no-inference rule.

**MISSING_DETAIL low-severity (không generalize):** 3 instance không cùng root cause — FIX-001 (template-hoá sample ID `1002240906000004`→`{asn_code}`, cosmetic), FIX-002 (công thức SL thiếu derive faithful từ VD số), FIX-003 (raw inconsistency trên). Không phải systemic pattern → no skill patch.

---

## 2026-05-31 / spec-scoped-batch-6

**no new spec-defect patterns** — cùng source doc `07062_Receiving_PO_Docs_ver2.17.md` (VAS L522-783, APP L784-1069, FABRIC L1676-1737). 104 critical claim verified, **0 violation severity ≥ INFERRED** cho cả 3 specs (VAS PASS, FABRIC+APP CONDITIONAL). PATCH-001 tiếp tục hoạt động đúng — batch thứ 3 liên tiếp (batch-4/5/6) không sinh fix cho deviation thiếu Q-ID. Mọi diễn giải đều đính Q-ID ngay lúc refine (FABRIC AC-12 phân biệt Update 10-11 vs 10-12 → Q-003; APP Q-001..Q-012; VAS Q-001..Q-013).

**Enum completeness tái xác nhận đúng:** 6/6 enum PASS đầy đủ count (VAS Filter+Listing Trạng thái 4/4, APP Loại nhận 2/2, Phương án SPKPH 2/2, giỏ status {Available, Transfer Bin} 2/2, Required camera {Yes,No} 2/2). Formula VAS Group UID `ceil(SL×10%)` = raw "làm tròn lên" verbatim + worked-example "25→2,5→3" — KHÁC batch-3 `stub_qc_evaluation_mobile` (ở đó raw chỉ "10% số lượng cây vải", spec tự thêm biến `lot_uid_count` → INFERRED). Phân biệt: ceil = round up là phép toán tương đương "làm tròn lên", không phải generalization.

**Pending-source handling tái xác nhận đúng (3 lần liên tiếp batch-4/5/6):** FABRIC ERR-FAB-001/002 (raw L1696-1701 không có verbatim message) + R010 (raw L1722 heading-only) + APP R024 (raw L984 chỉ "hiện thông báo") → spec ghi "(raw không có verbatim — Q-xxx)" thay vì bịa. UNCLEAR/pending, không trừ điểm. Cùng pattern tốt như ERR-UIG-001/002 (batch-4) + MSG-INV-005..008 (batch-5).

**Watch-item RAW SELF-CONTRADICTION — đạt instance thứ 2 liên tiếp (ngưỡng theo dõi):**
- **batch-5** (1 instance): invoice Tax code/Serial "1-8 ký tự bao gồm chữ và số" (alphanumeric, raw L1521) vs error message "phải từ 1 đến 8 chữ số" (digits, raw L1525) → FIX-003 + Q-013.
- **batch-6** (1 instance): APP ERR-APP-004 — VN "Vị trí F0-A1-PL-50-01-01 là bin Di động, nên không thể lưu trữ hàng cho PO." vs EN "Location F2-AP-01-01-01-01 is not setup to storage for PO." (raw L997-1002) — cả mã vị trí LẪN nội dung khác nhau giữa VN/EN → spec quote cả 2 verbatim + Q-004.
- → **2 instances / 2 sessions liên tiếp.** Root cause: nguồn raw tự mâu thuẫn (VN≠EN, hoặc rule≠message), spec KHÔNG sai khi quote verbatim nhưng phải flag Q-ID. Cả 2 lần spec xử lý ĐÚNG (đính Q-ID) → đây là pattern xử lý tốt, KHÔNG phải defect cần prevent.

**Decision (defer auto-patch):** Pattern raw self-contradiction đạt 2 instances liên tiếp NHƯNG: (1) spec xử lý đúng cả 2 lần → không có defect; (2) PATCH-001 hiện đã cover "spec text ≠ raw verbatim → bắt buộc Q-ID", bao gồm trường hợp raw VN≠EN; (3) đề xuất nhẹ (advisory, NOT applied): cân nhắc bổ sung 1 dòng ví dụ vào PATCH-001 (`.claude/rules/20-no-inference.md`) làm rõ "raw self-contradiction (VN≠EN, rule≠message) cũng thuộc phạm vi bắt buộc Q-ID". Track tới session sau, chỉ apply khi user confirm + pass quality gates. **no skill patch auto-applied.**

**Verdict semantics note:** FORMAT_VIOLATION (FABRIC+APP) ở L_structural KHÔNG nâng thành FAIL ở L_inference vì root cause là pending-source / raw self-contradiction (raw thiếu/mâu thuẫn), không phải spec defect — spec đã xử lý đúng. → CONDITIONAL (= Verified + note). Nhất quán với batch-4 (ERR-UIG-001/002 missing verbatim → PASS) + batch-5 (MSG-INV-005..008 → PASS).

---

## 2026-05-31 / spec-scoped-batch-7

**no new spec-defect patterns** — cùng source doc `07062_Receiving_PO_Docs_ver2.17.md` (date_rules L1070-1496, confirm_paste_id L1808-2070, vas_manual L2071-2181, packing_list L2182-2580). 244 critical claim verified raw-first, **0 violation severity ≥ INFERRED** cho cả 4 specs → PASS 4/4. PATCH-001 hoạt động đúng — batch thứ 4 liên tiếp (batch-4/5/6/7) hầu hết deviation đính Q-ID ngay lúc refine.

**Enum completeness tái xác nhận đúng (10/10 PASS):** màu phiên VAS 3/3 + màu Step 4 3/3 + category exclusion 3/3 (confirm_paste_id); Loại VAS 2/2 + Qty status 2/2 + UID status In-Bin/Picklisted 2/2 (vas_manual); Lý do thiếu 2/2 + Tình trạng hàng hoá 4/4 (date_rules); Packing list PO status 2/2 + Delivery method 2/2 (packing_list). Formula 6/6 verbatim (HSD min, Serial pattern, Trừ lõi x2, quy đổi Yard/Mét, hệ số). API payload check_issue/unsuitable verbatim.

**Pending-source handling tái xác nhận đúng (4 lần liên tiếp batch-4/5/6/7):** 18 message thiếu verbatim VN hoặc EN → spec ghi "(raw không có verbatim — Q-xxx)" thay vì bịa. UNCLEAR/pending, không trừ điểm. Raw typo giữ verbatim + Q-ID đúng (prodcut date_rules, tronng packing_list, nhân packing_list). Pattern tốt nhất quán từ ERR-UIG-001/002 (batch-4).

**Watch-item RAW-INTERNAL INCONSISTENCY — đạt instance #3 + #4 liên tiếp (vượt ngưỡng theo dõi 4 instance / batch-3→7):**
- **batch-5** (#1): invoice "chữ và số" (alphanumeric, L1521) vs message "chữ số" (digits, L1525) → FIX-003 + Q-013.
- **batch-6** (#2): APP ERR-APP-004 VN≠EN cả mã vị trí lẫn nội dung (L997-1002) → Q-004.
- **batch-7** (#3): packing_list AC-20 — raw formula L2479 dùng `Width(m)=1.5` nhưng VD tính L2506 plug `180` → spec resolve im lặng dùng 1.5 → `54.69 Yard` (Q-010 chỉ cover constant 0.9144, KHÔNG cover 180-vs-1.5) → FIX-002.
- **batch-7** (#4): date_rules R001 — raw VN L1076 typo "HSD tối thiếu", spec silent fix → "HSD tối thiểu" mark SUPPORTED không có Q-ID (Q-002 cover prodcut, Q-004 cover kiếm, Q-005 cover EN missing — không cover typo VN này) → FIX-001.

**Khác biệt batch-7 so với batch-5/6:** ở batch-5/6 spec xử lý ĐÚNG (đính Q-ID cho raw self-contradiction). Ở batch-7, 2 instance này spec **quên áp dụng PATCH-001** (silent resolution không Q-ID) → đây là **compliance gap thực thi**, KHÔNG phải PATCH-001 thiếu phạm vi. Counterfactual: nếu spec author tuân PATCH-001 đầy đủ → FIX-001/002 đã không phát sinh. Vì vậy giữ verdict PASS (MISSING_DETAIL Low, -2 mỗi cái) thay vì hạ CONDITIONAL — đây là deviation chưa-trace cần thêm Q-ID, không phải suy diễn nội dung sai.

**Decision (PATCH-002 candidate, NOT applied):** Watch-item raw-internal inconsistency nay 4 instance liên tiếp + batch-7 lần đầu thấy spec resolve IM LẶNG (không Q-ID) → đủ ngưỡng đề xuất PATCH-002: bổ sung ví dụ rõ vào PATCH-001 / checklist phase ingest — "Khi raw có VD/example số học mâu thuẫn formula/rule cùng tài liệu (Width 1.5 vs 180), hoặc typo VN/EN cần sửa, KHÔNG resolve im lặng bằng cách chọn 1 nhánh — bắt buộc Q-ID raw-internal-inconsistency + giữ verbatim cả 2 nhánh." Track `improvement_patch_plan.md`. **no skill patch auto-applied** — chờ user confirm + pass quality gates.
