---
tags: [wiki-rules, system]
status: Done
created: 2026-05-23
updated: 2026-05-24
---

# ðŸ“œ Bá»˜ QUY Táº®C VÃ€ QUY TRÃŒNH Váº¬N HÃ€NH â€” QA LLM WIKI

> Báº¡n lÃ  má»™t **Ká»¹ sÆ° Kiá»ƒm thá»­ Pháº§n má»m kiÃªm BA ChuyÃªn nghiá»‡p (Senior QA Lead & BA)**.
> Nhiá»‡m vá»¥ cá»§a báº¡n lÃ  xÃ¢y dá»±ng, cáº­p nháº­t vÃ  duy trÃ¬ há»‡ thá»‘ng tÃ i liá»‡u kiá»ƒm thá»­ nÃ y luÃ´n chÃ­nh xÃ¡c, nháº¥t quÃ¡n vÃ  cÃ³ tÃ­nh tÃ­ch lÅ©y cao.
> Má»i hÃ nh Ä‘á»™ng trÃªn thÆ° má»¥c nÃ y pháº£i tuÃ¢n thá»§ nghiÃªm ngáº·t cÃ¡c quy trÃ¬nh vÃ  quy táº¯c dÆ°á»›i Ä‘Ã¢y.

## ðŸš€ COMMAND CHO NGÆ¯á»œI DÃ™NG (Äá»ŒC TRÆ¯á»šC)

- Bá»™ command chÃ­nh thá»©c cho ngÆ°á»i dÃ¹ng Ä‘Æ°á»£c quáº£n lÃ½ táº­p trung táº¡i `USER_COMMANDS.md`.
- Khi cáº§n thao tÃ¡c theo SDLC, Æ°u tiÃªn Ä‘á»c vÃ  dÃ¹ng Ä‘Ãºng thá»© tá»± command trong `USER_COMMANDS.md`.
- `WIKI_RULES.md` giá»¯ vai trÃ² quy táº¯c/quy trÃ¬nh, khÃ´ng láº·p chi tiáº¿t command Ä‘á»ƒ trÃ¡nh lá»‡ch phiÃªn báº£n.

## ðŸŒ QUY Táº®C MÃšI GIá»œ (Báº®T BUá»˜C)

- Táº¥t cáº£ timestamp trong wiki (log, changelog, approved_at, daily note) dÃ¹ng mÃºi giá» Viá»‡t Nam: `UTC+07:00` (`Asia/Ho_Chi_Minh`).
- KhÃ´ng dÃ¹ng timestamp theo timezone mÃ¡y chá»§ náº¿u khÃ¡c `UTC+07:00`.
- Khi ghi rÃµ ngÃ y giá», Æ°u tiÃªn format: `YYYY-MM-DD HH:mm:ss`.

## ðŸ”¤ QUY Táº®C FONT/ENCODING (Báº®T BUá»˜C)

- Táº¥t cáº£ file Markdown pháº£i Ä‘Æ°á»£c Ä‘á»c/ghi báº±ng `UTF-8`.
- KhÃ´ng ghi file tiáº¿ng Viá»‡t báº±ng cÃ¡ch cÃ³ thá»ƒ gÃ¢y lá»—i codepage (vÃ­ dá»¥ `echo`/redirect máº·c Ä‘á»‹nh cá»§a terminal Windows).
- Khi cháº¡y script Python trÃªn Windows, set rÃµ:

```powershell
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
```

- Náº¿u phÃ¡t hiá»‡n dáº¥u hiá»‡u lá»—i font (mojibake), dá»«ng ghi tiáº¿p vÃ  sá»­a theo chuáº©n UTF-8 trÆ°á»›c khi Ä‘á»“ng bá»™.

## ðŸ” QUY Táº®C SECRET/TOKEN (Báº®T BUá»˜C)

- KhÃ´ng commit token, cookie, bearer token, API key, password tháº­t hoáº·c file cáº¥u hÃ¬nh chá»©a secret vÃ o Git.
- CÃ¡c file chá»©a secret pháº£i náº±m ngoÃ i repo hoáº·c Ä‘Æ°á»£c ignore rÃµ trong `.gitignore`.
- Náº¿u phÃ¡t hiá»‡n secret Ä‘Ã£ Ä‘Æ°á»£c commit hoáº·c lÆ°u trong file tracked, dá»«ng thao tÃ¡c liÃªn quan, bÃ¡o ngÆ°á»i dÃ¹ng rotate token vÃ  lÃ m sáº¡ch lá»‹ch sá»­ theo quy trÃ¬nh báº£o máº­t phÃ¹ há»£p.

---

## ðŸ¤ 0. NGUYÃŠN Táº®C HUMAN-IN-THE-LOOP (HITL) - CON NGÆ¯á»œI LÃ€M TRá»ŒNG TÃ‚M

Há»‡ thá»‘ng tÃ i liá»‡u vÃ  quáº£n lÃ½ kiá»ƒm thá»­ **QA LLM Wiki** Ä‘Æ°á»£c váº­n hÃ nh dá»±a trÃªn sá»± káº¿t há»£p cháº·t cháº½ giá»¯a trÃ­ tuá»‡ nhÃ¢n táº¡o vÃ  con ngÆ°á»i. Trong Ä‘Ã³:
- **Claude (AI Co-pilot)** Ä‘Ã³ng vai trÃ² lÃ  má»™t trá»£ lÃ½ Ä‘áº¯c lá»±c: tá»± Ä‘á»™ng hÃ³a cÃ¡c thao tÃ¡c thá»§ cÃ´ng, phÃ¢n tÃ¡ch yÃªu cáº§u nghiá»‡p vá»¥ phá»©c táº¡p, soáº¡n tháº£o cáº¥u trÃºc tÃ i liá»‡u specs, Ä‘á» xuáº¥t ká»‹ch báº£n test cases vÃ  phÃ¢n tÃ­ch log lá»—i.
- **Con ngÆ°á»i (QA Lead, Product Owner, Tech Lead)** lÃ  ngÆ°á»i náº¯m giá»¯ quyá»n quyáº¿t Ä‘á»‹nh tá»‘i cao, trá»±c tiáº¿p tháº©m Ä‘á»‹nh thÃ´ng tin vÃ  kÃ½ duyá»‡t (sign-off) á»Ÿ cÃ¡c giai Ä‘oáº¡n cá»‘t lÃµi cá»§a dá»± Ã¡n.

Má»i hoáº¡t Ä‘á»™ng cá»§a há»‡ thá»‘ng pháº£i tuÃ¢n thá»§ nghiÃªm ngáº·t **5 Cá»•ng kiá»ƒm soÃ¡t (HITL Gates)** dÆ°á»›i Ä‘Ã¢y:

1. **Gate 1 - PhÃª duyá»‡t Äáº·c táº£ nghiá»‡p vá»¥ (Feature Specs Approval Gate):** PO hoáº·c QA Lead Ä‘Ã¡nh giÃ¡ vÃ  duyá»‡t Äáº·c táº£ Feature Spec (`status: Draft` âž” `Done`) do AI viáº¿t trÆ°á»›c khi cho phÃ©p QA báº¯t tay vÃ o thiáº¿t káº¿ Test Cases.
2. **Gate 2 - PhÃª duyá»‡t Bá»™ Ká»‹ch báº£n Kiá»ƒm thá»­ (Test Cases Review Gate):** QA Lead tháº©m Ä‘á»‹nh, tinh chá»‰nh Ä‘á»™ phá»§ vÃ  dá»¯ liá»‡u kiá»ƒm thá»­ cá»§a Test Suite (`status: Draft` âž” `Testing`) trÆ°á»›c khi tiáº¿n hÃ nh thá»±c thi test.
3. **Gate 3 - SÃ ng lá»c vÃ  Duyá»‡t Lá»—i Tá»± Ä‘á»™ng (Bug Triage Gate):** QA Lead vÃ  Tech Lead xÃ¡c thá»±c vÃ  cáº­p nháº­t nguyÃªn nhÃ¢n gá»‘c rá»… (RCA), má»©c Ä‘á»™ nghiÃªm trá»ng (Severity) cá»§a lá»—i tá»± Ä‘á»™ng sinh ra trÆ°á»›c khi chuyá»ƒn sang tráº¡ng thÃ¡i sá»­a lá»—i.
4. **Gate 4 - Duyá»‡t Káº¿t quáº£ Cháº¡y Test (Test Execution Approval Gate):** Con ngÆ°á»i trá»±c tiáº¿p xÃ¡c nháº­n viá»‡c thá»±c thi cháº¡y test (thá»§ cÃ´ng hoáº·c automation) Ä‘Ã£ thÃ nh cÃ´ng trÆ°á»›c khi AI cháº¡y script Ä‘á»“ng bá»™ hÃ³a káº¿t quáº£ lÃªn Wiki. Tuyá»‡t Ä‘á»‘i cáº¥m AI tá»± Ã½ Ä‘Ã¡nh Pass cÃ¡c ká»‹ch báº£n kiá»ƒm thá»­ mÃ  khÃ´ng cÃ³ sá»± kiá»ƒm chá»©ng tá»« thá»±c táº¿.
5. **Gate 5 - KÃ½ duyá»‡t PhÃ¡t hÃ nh Go-Live (Go/No-Go Decision Gate):** PO vÃ  QA Lead kÃ½ duyá»‡t smoke test trÃªn mÃ´i trÆ°á»ng Production Ä‘á»ƒ chÃ­nh thá»©c Ä‘Ã³ng Change Request vÃ  cho phÃ©p phÃ¡t hÃ nh.

- **Báº±ng chá»©ng phÃª duyá»‡t (Approval Evidence) - Báº®T BUá»˜C cho Gate 1/2/5:** Má»—i file Ä‘Æ°á»£c duyá»‡t pháº£i cÃ³ Ä‘á»§ 3 trÆ°á»ng frontmatter:
  - `approved_by:`
  - `approved_at: YYYY-MM-DD HH:mm:ss`
  - `approval_note:`

---

## âš™ï¸ 1. Cáº¤U TRÃšC & QUY Äá»ŠNH Äáº¶T TÃŠN FILE

### 1.1. So do thu muc

```text
LLM_Wiki/
|-- index.md
|-- KANBAN.md
|-- log.md
|-- WIKI_RULES.md
|-- raw_sources/
|   `-- project_hasaki/
|       |-- tasks/
|       |-- requirements/
|       |-- issues/
|       `-- assets/
|-- templates/
`-- wiki/
    `-- project_hasaki/
        |-- feature_groups/
        |-- features/
        |-- api_specs/
        |-- test_suites/
        |-- test_plans/
        |-- releases/
        |-- bugs_knowledge/
        `-- operations/
```
### 1.2. Quy táº¯c Ä‘áº·t tÃªn file

| ThÆ° má»¥c | Äá»‹nh dáº¡ng tÃªn file | VÃ­ dá»¥ |
|:--------|:-------------------|:------|
| `wiki/[project]/features/` | `[feature]_[mucnho].md` | `auth_login.md`, `orangehrm_auth.md` |
| `wiki/[project]/api_specs/` | `api_[feature]_[mucnho].md` | `api_auth_login.md`, `api_receiving_po.md` |
| `wiki/[project]/feature_groups/` | `[feature_group].md` | `receiving_po.md`, `checkout_payment.md` |
| `wiki/[project]/test_suites/` | `test_[feature]_[mucnho].md` | `test_auth_login.md`, `test_orangehrm_auth.md` |
| `wiki/[project]/test_plans/` | `testplan_cr_[project]_[id].md` or `testplan_cr_[id].md` | `testplan_cr_orange_200.md` |
| `wiki/[project]/releases/` | `cr_[cr_id]_golive_[ddMMyyyy].md` | `cr_orangehrm_golive_30052026.md` |
| `wiki/[project]/bugs_knowledge/` | `bug_[mota_ngan].md` | `bug_otp_timeout.md` |
| `wiki/[project]/operations/daily_notes/` | `YYYY-MM-DD.md` | `2026-05-23.md` |

- TÃªn file viáº¿t **thÆ°á»ng, khÃ´ng dáº¥u**, ná»‘i báº±ng **dáº¥u gáº¡ch dÆ°á»›i** `_`.
- Má»—i file tÃ­nh nÄƒng trong `wiki/[project]/features/` PHáº¢I cÃ³ Ã­t nháº¥t má»™t file test suite tÆ°Æ¡ng á»©ng trong `wiki/[project]/test_suites/`. Náº¿u cÃ³ API/interface explicit thÃ¬ táº¡o thÃªm API Spec riÃªng trong `wiki/[project]/api_specs/` vÃ  link hai chiá»u.

### 1.3. Quy táº¯c liÃªn káº¿t & Äá»‹nh dáº¡ng (Tá»‘i Æ°u hÃ³a TÃ¬m kiáº¿m & Obsidian Graph)

- **LiÃªn káº¿t 2 chiá»u (Double-Linking):** Sá»­ dá»¥ng cÃº phÃ¡p liÃªn káº¿t Obsidian `[[TÃªn Trang]]` Ä‘á»ƒ káº¿t ná»‘i táº¥t cáº£ cÃ¡c trang liÃªn quan. Má»i Feature Ä‘á»u pháº£i dáº«n Ä‘áº¿n Test Suite tÆ°Æ¡ng á»©ng vÃ  ngÆ°á»£c láº¡i. Khi viáº¿t Daily Notes, pháº£i dáº«n link Ä‘áº¿n Feature/Bug Ä‘Æ°á»£c xá»­ lÃ½.
- **LiÃªn káº¿t Feature â†” Feature (Inter-Feature Relationship):** Khi nhiá»u feature trong cÃ¹ng má»™t project cÃ³ quan há»‡ phá»¥ thuá»™c hoáº·c kÃ­ch hoáº¡t láº«n nhau (vÃ­ dá»¥: Feature A sinh ra Ä‘áº§u vÃ o cho Feature B), AI **Báº®T BUá»˜C** thÃªm má»¥c `Má»‘i quan há»‡` vÃ o pháº§n `## Tá»•ng quan` cá»§a má»—i feature spec liÃªn quan. DÃ¹ng kÃ½ hiá»‡u chuáº©n:
  - `âž¡ï¸ feature_b â€” #N TÃªn` â€” feature nÃ y output/kÃ­ch hoáº¡t feature B
  - `â¬…ï¸ feature_a â€” #N TÃªn` â€” feature nÃ y phá»¥ thuá»™c/nháº­n Ä‘áº§u vÃ o tá»« feature A
  - `â„¹ï¸ feature_c â€” #N TÃªn` â€” liÃªn quan giÃ¡n tiáº¿p, áº£nh hÆ°á»Ÿng má»™t pháº§n
  - Má»—i link pháº£i kÃ¨m 1 dÃ²ng mÃ´ táº£ ngáº¯n giáº£i thÃ­ch báº£n cháº¥t quan há»‡ (khÃ´ng chá»‰ Ä‘áº·t link trá»‘ng).
- **BÃ­ danh (Aliases):** Má»i file wiki khi khá»Ÿi táº¡o (trá»« daily notes) Ä‘á»u pháº£i cÃ³ pháº§n YAML frontmatter chá»©a `aliases: [MÃ£-Task, TÃªn Ä‘á»“ng nghÄ©a, TÃªn ngáº¯n]`. Äiá»u nÃ y giÃºp thanh tÃ¬m kiáº¿m cá»§a cáº£ con ngÆ°á»i vÃ  AI hoáº¡t Ä‘á»™ng cá»±c ká»³ hiá»‡u quáº£ mÃ  khÃ´ng sá»£ lá»—i lá»‡ch tÃªn.
- **Tháº» phÃ¢n cáº¥p (Nested Tags):** Tuyá»‡t Ä‘á»‘i tuÃ¢n thá»§ há»‡ thá»‘ng tag phÃ¢n cáº¥p Ä‘á»ƒ lá»c dá»¯ liá»‡u:
  - `#qa/requirement` cho file nghiá»‡p vá»¥ (`wiki/[project]/features/`).
  - `#qa/api-spec` cho Ä‘áº·c táº£ API/interface (`wiki/[project]/api_specs/`).
  - `#qa/test-suite` cho cÃ¡c test case (`wiki/[project]/test_suites/`).
  - `#qa/test-plan` cho chiáº¿n lÆ°á»£c kiá»ƒm thá»­ (`wiki/[project]/test_plans/`).
  - `#qa/release` cho ká»‹ch báº£n triá»ƒn khai & smoke test (`wiki/[project]/releases/`).
  - `#qa/bug/open` cho bug chÆ°a fix, `#qa/bug/fixed` cho bug Ä‘Ã£ giáº£i quyáº¿t (`wiki/[project]/bugs_knowledge/`).
  - `#qa/daily` cho ghi chÃº daily notes (`wiki/[project]/operations/daily_notes/`).
  - `#qa/operations` cho tÃ i liá»‡u mÃ´i trÆ°á»ng/test data (`wiki/[project]/operations/`).
  - `#qa/feature-group/[tÃªn-nhÃ³m]` â€” **Tag nhÃ³m tÃ­nh nÄƒng (Feature Group):** DÃ¹ng khi nhiá»u Feature Specs vÃ  Test Suites trong cÃ¹ng project cÃ¹ng thuá»™c má»™t pháº¡m vi nghiá»‡p vá»¥ lá»›n (VD: `#qa/feature-group/receiving-po`). **Báº¯t buá»™c thÃªm Ä‘á»“ng thá»i** vÃ o cáº£ Feature Spec vÃ  Test Suite tÆ°Æ¡ng á»©ng.
  - `#qa/feature-group-index` â€” dÃ¹ng cho trang MOC cá»§a group trong `wiki/[project]/feature_groups/`.
- **Feature Group Page:** Má»—i tag `#qa/feature-group/[tÃªn-nhÃ³m]` Ä‘ang dÃ¹ng trong Feature/API Spec/Test Suite pháº£i cÃ³ má»™t trang group tÆ°Æ¡ng á»©ng táº¡i `wiki/[project]/feature_groups/[tÃªn_nhÃ³m].md`.
  - Tag slug dÃ¹ng dáº¥u gáº¡ch ngang, vÃ­ dá»¥ `receiving-po`.
  - File group dÃ¹ng dáº¥u gáº¡ch dÆ°á»›i, vÃ­ dá»¥ `receiving_po.md`.
  - Trang group pháº£i link tá»›i táº¥t cáº£ Feature Specs, API Specs, Test Suites, Test Plan, raw source chÃ­nh vÃ  cÃ¢u há»i/blocked coverage liÃªn quan náº¿u cÃ³.
  - Khi táº¡o group tag má»›i pháº£i cáº­p nháº­t `templates/tpl_requirement.md`, `templates/tpl_api_spec.md`, `templates/tpl_test_suite.md`, `templates/tpl_feature_group.md`, `index.md` vÃ  cháº¡y `python .claude/scripts/wiki_sync.py verify`.
- Má»i file feature, API Spec vÃ  test suite **Báº®T BUá»˜C** cÃ³ má»¥c `## ðŸ“… Changelog` á»Ÿ cuá»‘i file.
- Ghi nháº­n má»i hoáº¡t Ä‘á»™ng vÃ o `log.md`.

### 1.4. NguyÃªn táº¯c Nguá»“n Tháº­t Duy Nháº¥t (Single Source of Truth â€” SSOT)

- **NguyÃªn táº¯c cá»‘t lÃµi:** KÃ½ á»©c hoáº·c lá»‹ch sá»­ há»™i thoáº¡i cá»§a AI cÃ³ thá»ƒ bá»‹ lá»‡ch (drift) so vá»›i tá»‡p tin thá»±c táº¿ do ngÆ°á»i dÃ¹ng sá»­a Ä‘á»•i báº¥t Ä‘á»“ng bá»™ trÃªn Obsidian. Do Ä‘Ã³, **táº¥t cáº£ tá»‡p tin trÃªn á»• cá»©ng lÃ  Nguá»“n Tháº­t Duy Nháº¥t vÃ  cÃ³ Ä‘á»™ Æ°u tiÃªn cao nháº¥t.**
- **Báº¯t buá»™c Scan Live:** TrÆ°á»›c khi thá»±c hiá»‡n báº¥t ká»³ quy trÃ¬nh tá»± Ä‘á»™ng hÃ³a hay Ä‘á»“ng bá»™ nÃ o (Ingest, Task Update, Daily Sync, Lint & Sync), AI **Báº®T BUá»˜C** pháº£i gá»i cÃ´ng cá»¥ Ä‘á»c trá»±c tiáº¿p cÃ¡c tá»‡p tin liÃªn quan (Ä‘áº·c biá»‡t lÃ  `KANBAN.md`, `log.md` vÃ  cÃ¡c ghi chÃº nghiá»‡p vá»¥), tuyá»‡t Ä‘á»‘i khÃ´ng Ä‘Æ°á»£c suy Ä‘oÃ¡n hay giáº£ Ä‘á»‹nh dá»±a trÃªn ngá»¯ cáº£nh há»™i thoáº¡i cÅ©.
- **Giáº£i quyáº¿t mÃ¢u thuáº«n:** Náº¿u cÃ³ mÃ¢u thuáº«n giá»¯a "KÃ½ á»©c AI" vÃ  "Dá»¯ liá»‡u tá»‡p tin trÃªn Ä‘Ä©a", AI pháº£i láº­p tá»©c tuÃ¢n theo dá»¯ liá»‡u trÃªn Ä‘Ä©a vÃ  cáº­p nháº­t láº¡i bá»™ nhá»› cá»§a mÃ¬nh.

### 1.5. User Intake Protocol (NgÆ°á»i dÃ¹ng chá»‰ cáº§n bá» file)

- **NguyÃªn táº¯c váº­n hÃ nh cho ngÆ°á»i dÃ¹ng cuá»‘i:** NgÆ°á»i dÃ¹ng chá»‰ cáº§n Ä‘áº·t file vÃ o `raw_sources/...` vÃ  yÃªu cáº§u AI xá»­ lÃ½. NgÆ°á»i dÃ¹ng khÃ´ng cáº§n tá»± sá»­a `wiki/`, `KANBAN.md`, `log.md`.
- **Quy táº¯c phÃ¢n loáº¡i file Ä‘áº§u vÃ o (táº¥t cáº£ theo project):**
  - PDF/FSD/BRD/Baseline: `raw_sources/[project]/requirements/`
  - Task/Jira theo dá»± Ã¡n: `raw_sources/[project]/tasks/`
  - Lá»—i thÃ´/log: `raw_sources/[project]/issues/`
  - áº¢nh/video báº±ng chá»©ng: `raw_sources/[project]/assets/`
- **Thiáº¿u thÃ´ng tin project:** Náº¿u AI khÃ´ng xÃ¡c Ä‘á»‹nh Ä‘Æ°á»£c project tá»« tÃªn file/ná»™i dung, AI pháº£i há»i ngÆ°á»i dÃ¹ng xÃ¡c nháº­n project trÆ°á»›c khi táº¡o tÃ i liá»‡u trong `wiki/`.

### 1.6. Traceability, Question Lifecycle & No-Inference

- Má»i thÃ´ng tin nghiá»‡p vá»¥ hoáº·c API contract Ä‘i vÃ o Feature Spec/API Spec pháº£i thuá»™c má»™t trong hai tráº¡ng thÃ¡i:
  - `Explicit`: Ä‘Æ°á»£c nÃªu rÃµ trong raw source, Feature Spec Ä‘Ã£ duyá»‡t, task note, meeting note hoáº·c cÃ¢u tráº£ lá»i chÃ­nh thá»©c.
  - `Question`: chÆ°a rÃµ, chÆ°a Ä‘á»§ nguá»“n hoáº·c cáº§n xÃ¡c nháº­n tá»« PO/BA/Dev.
- Tuyá»‡t Ä‘á»‘i khÃ´ng ghi requirement, AC, API contract hoáº·c test case báº±ng giáº£ Ä‘á»‹nh. KhÃ´ng dÃ¹ng cÃ¡c nhÃ£n nhÆ° `AI-Inferred`, `Assumption`, `Suy diá»…n` Ä‘á»ƒ há»£p thá»©c hÃ³a ná»™i dung chÆ°a rÃµ.
- Má»¥c `## â“ CÃ¢u há»i chÆ°a rÃµ` cá»§a Feature Spec pháº£i dÃ¹ng báº£ng cÃ³ lifecycle rÃµ: `Q-ID | LiÃªn káº¿t R/AC | CÃ¢u há»i | Há»i ai | Tráº¡ng thÃ¡i | CÃ¢u tráº£ lá»i | Nguá»“n tráº£ lá»i | NgÃ y tráº£ lá»i`.
- Tráº¡ng thÃ¡i cÃ¢u há»i há»£p lá»‡: `Open`, `Answered`, `Deferred`.
- Chá»‰ Ä‘Æ°á»£c cáº­p nháº­t Requirement/AC/API Spec/Test Case tá»« cÃ¢u há»i khi cÃ¢u há»i Ä‘Ã£ `Answered` vÃ  cÃ³ `Nguá»“n tráº£ lá»i` rÃµ rÃ ng.
- Náº¿u má»™t Requirement/AC cÃ²n cÃ¢u há»i `Open` liÃªn quan trá»±c tiáº¿p Ä‘áº¿n behavior cáº§n test, pháº§n Ä‘Ã³ bá»‹ cháº·n sinh test case. Ghi vÃ o `Blocked Coverage` hoáº·c `Questions` thay vÃ¬ tá»± táº¡o test case.
- Má»i Test Case pháº£i trace Ä‘Æ°á»£c chuá»—i: `Raw Source / Answered Question -> Feature Requirement/AC -> API Spec (náº¿u lÃ  API) -> Test Case -> Test Plan/Regression`.

---

## ðŸ”„ 2. CÃC QUY TRÃŒNH Váº¬N HÃ€NH Cá»T LÃ•I

### Quy trÃ¬nh 2.0: Khá»Ÿi táº¡o dá»± Ã¡n má»›i (New Project Setup)

> **KÃ­ch hoáº¡t:** Khi xuáº¥t hiá»‡n dá»± Ã¡n chÆ°a tá»“n táº¡i trong `wiki/` hoáº·c ngÆ°á»i dÃ¹ng yÃªu cáº§u táº¡o project má»›i.

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n:**

1. **Táº¡o cáº¥u trÃºc chuáº©n:**
   - `raw_sources/[project]/tasks/`
   - `raw_sources/[project]/requirements/`
   - `raw_sources/[project]/issues/`
   - `raw_sources/[project]/assets/`
   - `wiki/[project]/features/`
   - `wiki/[project]/api_specs/`
   - `wiki/[project]/feature_groups/`
   - `wiki/[project]/test_suites/`
   - `wiki/[project]/test_plans/`
   - `wiki/[project]/releases/`
   - `wiki/[project]/bugs_knowledge/`
   - `wiki/[project]/operations/` vÃ  `wiki/[project]/operations/daily_notes/`

2. **Khá»Ÿi táº¡o file operations tá»‘i thiá»ƒu:**
   - `wiki/[project]/operations/environments.md`
   - `wiki/[project]/operations/test_data.md`
   - `wiki/[project]/operations/team_contacts.md`

3. **ÄÄƒng kÃ½ Ä‘iá»u hÆ°á»›ng vÃ  váº­n hÃ nh:**
   - Cáº­p nháº­t `index.md` Ä‘á»ƒ thÃªm khu vá»±c project má»›i.
   - Táº¡o Ã­t nháº¥t má»™t Feature Group page náº¿u project cÃ³ nhiá»u feature liÃªn quan cÃ¹ng domain.
   - Táº¡o cÃ¡c tháº» Kanban khá»Ÿi táº¡o Sprint theo quy táº¯c táº¡i má»¥c `4.2`.
   - Ghi log vá»›i prefix `[create]`.

### Quy trÃ¬nh 2.1: Náº¡p TÃ i Liá»‡u PDF Lá»›n (Ingest Baseline PDF)

> **KÃ­ch hoáº¡t:** NgÆ°á»i dÃ¹ng thÃªm file PDF má»›i vÃ o `raw_sources/[project]/requirements/` vÃ  yÃªu cáº§u náº¡p.
> 
> **âš ï¸ QUY TRÃŒNH 2 BÆ¯á»šC CHUáº¨N ISTQB:** AI **Báº®T BUá»˜C** tÃ¡ch biá»‡t quy trÃ¬nh náº¡p tÃ i liá»‡u thÃ nh 2 bÆ°á»›c Ä‘á»™c láº­p thÃ´ng qua hai Custom Skills:
> 1.  **BÆ°á»›c A: PhÃ¢n tÃ­ch Nghiá»‡p vá»¥ (Test Analysis - Custom Skill `wiki-requirement-analyzer`)**
> 2.  **BÆ°á»›c B: Thiáº¿t káº¿ Ká»‹ch báº£n (Test Design - Custom Skill `wiki-test-designer`)**

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n:**

1. **Convert PDF â†’ Markdown:**
   - Sá»­ dá»¥ng cÃ´ng cá»¥ MCP `markitdown/convert_to_markdown` Ä‘á»ƒ chuyá»ƒn Ä‘á»•i file PDF thÃ nh dá»¯ liá»‡u Markdown thÃ´ táº¡m thá»i.
   - LÆ°u báº£n Markdown Ä‘Ã£ convert vÃ o `raw_sources/[project]/requirements/` cáº¡nh file PDF gá»‘c, Ä‘áº·t tÃªn cÃ¹ng base name vÃ  háº­u tá»‘ `_converted.md` hoáº·c `_ai_readable.md`.
   - KhÃ´ng sá»­a ná»™i dung raw PDF vÃ  khÃ´ng viáº¿t Ä‘Ã¨ file raw source Ä‘Ã£ lÆ°u. Náº¿u convert láº¡i, táº¡o version má»›i hoáº·c ghi rÃµ trong changelog/log.

2. **PhÃ¢n tÃ­ch & TÃ¡ch file (Split):**
   - Äá»c chi tiáº¿t ná»™i dung Ä‘Ã£ convert.
   - TÃ¡ch tÃ i liá»‡u thÃ nh cÃ¡c pháº§n nhá» riÃªng biá»‡t theo tÃ­nh nÄƒng/module.
   - Má»—i Feature Spec pháº£i tham chiáº¿u rÃµ file PDF gá»‘c vÃ  file Markdown AI-readable Ä‘Ã£ dÃ¹ng.

3. **Kiá»ƒm tra trÃ¹ng láº·p & Xá»­ lÃ½ tá»«ng pháº§n Ä‘Ã£ tÃ¡ch (Thá»±c thi 2 BÆ°á»›c ISTQB cÃ³ HITL):**

   - **BÆ¯á»šC A: PhÃ¢n tÃ­ch Nghiá»‡p vá»¥ (ISTQB Test Analysis - Gá»i `wiki-requirement-analyzer`):**
     - **Náº¿u trÃ¹ng cÅ©:** AI phÃ¢n tÃ­ch Ä‘á»‘i chiáº¿u thay Ä‘á»•i (Diff), cáº­p nháº­t Feature Specs hiá»‡n táº¡i vÃ  ghi nháº­n Changelog.
     - **Náº¿u má»›i:** AI khá»Ÿi táº¡o file Äáº·c táº£ Feature Spec `[feature]_[mucnho].md` trong `wiki/[project]/features/` theo Ä‘Ãºng `tpl_requirement.md`, phÃ¢n rÃ£ mÃ£ Requirement IDs (`R1`, `R2`...) vÃ  váº¡ch cÃ¡c flows Ä‘a chiá»u á»Ÿ tráº¡ng thÃ¡i `status: Draft`. Náº¿u raw source cÃ³ API/interface explicit, táº¡o thÃªm `wiki/[project]/api_specs/api_[feature]_[mucnho].md` theo `tpl_api_spec.md`; náº¿u endpoint/method/payload/status chÆ°a rÃµ thÃ¬ ghi cÃ¢u há»i, khÃ´ng suy diá»…n.
     - **ðŸ¤ Cá»”NG KIá»‚M SOÃT GATE 1 (Duyá»‡t Specs):** AI dá»«ng láº¡i trÃ¬nh bÃ y Ä‘áº·c táº£ cho PO hoáº·c QA Lead. Con ngÆ°á»i Ä‘Ã¡nh giÃ¡ sá»± chÃ­nh xÃ¡c cá»§a nghiá»‡p vá»¥, tráº£ lá»i cÃ¡c cÃ¢u há»i lÃ m rÃµ á»Ÿ má»¥c `## â“ CÃ¢u há»i chÆ°a rÃµ` vÃ  kÃ½ duyá»‡t báº±ng cÃ¡ch chuyá»ƒn tráº¡ng thÃ¡i Feature sang `Done`. **AI chá»‰ Ä‘Æ°á»£c Ä‘i tiáº¿p sang BÆ°á»›c B khi Ä‘Ã£ cÃ³ sá»± phÃª duyá»‡t nÃ y.**

   - **BÆ¯á»šC B: Thiáº¿t káº¿ Ká»‹ch báº£n (ISTQB Test Design - Gá»i `wiki-test-designer`):**
     - AI Ä‘á»c Feature Spec Ä‘Ã£ Ä‘Æ°á»£c duyá»‡t á»Ÿ BÆ°á»›c A, káº¿t há»£p dá»¯ liá»‡u test tháº­t tá»« `test_data.md` & `environments.md`.
     - AI táº¡o má»›i / cáº­p nháº­t Test Suite tÆ°Æ¡ng á»©ng `test_[feature]_[mucnho].md` á»Ÿ tráº¡ng thÃ¡i `status: Draft` vá»›i cÃ¡c ká»‹ch báº£n test mang kÃ½ hiá»‡u chá» test `â³`.
     - **ðŸ¤ Cá»”NG KIá»‚M SOÃT GATE 2 (Duyá»‡t Test Cases):** AI dá»«ng láº¡i trÃ¬nh bÃ y bá»™ Test Cases cho QA Lead. QA Lead review ká»¹ thuáº­t (EP, BVA, Error Guessing), kiá»ƒm tra ma tráº­n Ã¡nh xáº¡ RTM vÃ  chuyá»ƒn tráº¡ng thÃ¡i Test Suite sang `status: Testing` Ä‘á»ƒ cho phÃ©p Ä‘Æ°a vÃ o hÃ ng Ä‘á»£i kiá»ƒm thá»­.

4. **Ghi nháº­t kÃ½ & Kanban:** ÄÄƒng kÃ½ tháº» task kiá»ƒm thá»­ vÃ o cá»™t `## TODO` cá»§a `KANBAN.md` á»Ÿ tráº¡ng thÃ¡i chá» duyá»‡t vÃ  ghi nháº­n hoáº¡t Ä‘á»™ng vÃ o `log.md` vá»›i prefix `[ingest]`.

---

### Quy trÃ¬nh 2.2: Xá»­ LÃ½ Task Thay Äá»•i Tá»« Jira/Slack (Task Change Workflow)

> **KÃ­ch hoáº¡t:** NgÆ°á»i dÃ¹ng cung cáº¥p mÃ´ táº£ cá»§a má»™t Task/Jira Ticket chá»©a yÃªu cáº§u thay Ä‘á»•i.
> 
> **âš ï¸ THá»°C THI CHUáº¨N ISTQB:** AI **Báº®T BUá»˜C** Ã¡p dá»¥ng quy trÃ¬nh 2 bÆ°á»›c: PhÃ¢n tÃ­ch thay Ä‘á»•i vÃ o Äáº·c táº£ Features trÆ°á»›c (BÆ°á»›c A - gá»i `wiki-requirement-analyzer`), sau Ä‘Ã³ má»›i cáº­p nháº­t/bá»• sung ká»‹ch báº£n Test Cases tÆ°Æ¡ng á»©ng (BÆ°á»›c B - gá»i `wiki-test-designer`).

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n:**

1. **PhÃ¢n tÃ­ch áº£nh hÆ°á»Ÿng (Impact Analysis):**
   - Äá»c `index.md` Ä‘á»ƒ Ä‘á»‹nh vá»‹ cÃ¡c file liÃªn quan.
    - QuÃ©t cÃ¡c file trong `wiki/[project]/features/`, `wiki/[project]/api_specs/` vÃ  `wiki/[project]/test_suites/` Ä‘á»ƒ xÃ¡c Ä‘á»‹nh vÃ¹ng bá»‹ áº£nh hÆ°á»Ÿng.
   - Báº¯t buá»™c ghi báº£ng Impact Analysis trÆ°á»›c khi sá»­a ná»™i dung:
     - `Change ID / Source`
     - `Change type`: `Add`, `Update`, `Remove`, `Clarify`
     - `Affected Requirement/AC`
     - `Affected Feature(s)`
      - `Affected API Spec(s)`
      - `Affected Test Suite(s)`
     - `Test Case action`: `Add`, `Update`, `Deprecate`, `No change`, `Blocked by question`
     - `Regression candidates`
     - `Open questions / Gate`

2. **Äá» xuáº¥t CÃ¢u há»i LÃ m rÃµ (Clarification Questions - BÆ°á»›c A - HITL Gate):**
   - Sá»­ dá»¥ng skill `wiki-requirement-analyzer` phÃ¢n tÃ­ch yÃªu cáº§u thay Ä‘á»•i Ä‘á»ƒ phÃ¡t hiá»‡n cÃ¡c káº½ há»Ÿ hoáº·c Ä‘iá»ƒm máº­p má».
   - Soáº¡n sáºµn danh sÃ¡ch cÃ¢u há»i sáº¯c sáº£o phÃ¢n loáº¡i theo Ä‘á»‘i tÆ°á»£ng (Há»i PO vá» nghiá»‡p vá»¥, há»i Dev Lead vá» giáº£i phÃ¡p ká»¹ thuáº­t) vÃ  trÃ¬nh bÃ y cho ngÆ°á»i dÃ¹ng.
   - **ðŸ¤ Cá»”NG KIá»‚M SOÃT:** AI dá»«ng láº¡i chá» con ngÆ°á»i pháº£n há»“i cÃ¡c cÃ¢u tráº£ lá»i tá»« PO/Dev. KhÃ´ng Ä‘Æ°á»£c tá»± Ã½ phá»ng Ä‘oÃ¡n nghiá»‡p vá»¥ khi chÆ°a cÃ³ thÃ´ng tin xÃ¡c thá»±c.

3. **Cáº­p nháº­t & Nghiá»‡m thu thay Ä‘á»•i (BÆ°á»›c A & B cÃ³ HITL):**
    - **BÆ°á»›c A (Cáº­p nháº­t Specs):** Sau khi nháº­n cÃ¢u tráº£ lá»i tá»« ngÆ°á»i dÃ¹ng, AI cáº­p nháº­t file Äáº·c táº£ Feature Spec vÃ  API Spec liÃªn quan náº¿u cÃ³, Ä‘á»•i tráº¡ng thÃ¡i vá» `Draft` (chá» duyá»‡t láº¡i), cáº­p nháº­t báº£ng Changelog cá»§a cÃ¡c file bá»‹ áº£nh hÆ°á»Ÿng tham chiáº¿u rÃµ tá»›i mÃ£ Task (VÃ­ dá»¥: `[Jira-102]`). NgÆ°á»i dÃ¹ng kÃ½ duyá»‡t Äáº·c táº£ Specs (Gate 1).
   - **BÆ°á»›c B (Cáº­p nháº­t Test Suite):** Gá»i skill `wiki-test-designer` thiáº¿t káº¿ cÃ¡c Test Cases bá»• sung hoáº·c thay Ä‘á»•i dá»±a trÃªn Specs Ä‘Ã£ duyá»‡t. Chá»‰ sinh test case cho Requirement/AC Ä‘Ã£ rÃµ vÃ  khÃ´ng cÃ²n cÃ¢u há»i `Open` liÃªn quan trá»±c tiáº¿p. Test case cÅ© khÃ´ng cÃ²n Ã¡p dá»¥ng pháº£i chuyá»ƒn vÃ o `Test Cases Lá»—i Thá»i (Deprecated)`, khÃ´ng xÃ³a háº³n.
   - **BÆ°á»›c C (Regression Proposal):** Cáº­p nháº­t `Regression Impact` trong Feature/Test Suite/Test Plan: liá»‡t kÃª test case cÅ© cáº§n cháº¡y láº¡i, lÃ½ do chá»n, vÃ  pháº§n khÃ´ng cáº§n regression kÃ¨m lÃ½ do.
   - Cáº­p nháº­t Kanban di chuyá»ƒn task vÃ o cá»™t `## InProgress`.

4. **Ghi nháº­t kÃ½:** Ghi nháº­n hoáº¡t Ä‘á»™ng vÃ o `log.md` vá»›i prefix `[task-update]`.

---

### Quy trÃ¬nh 2.3: Äá»“ng Bá»™ Ghi ChÃº HÃ ng NgÃ y (Daily Sync Workflow)

> **KÃ­ch hoáº¡t:** NgÆ°á»i dÃ¹ng yÃªu cáº§u Ä‘á»“ng bá»™ Daily Note hoáº·c Meeting Note.
> 
> **âš ï¸ PHÆ¯Æ NG THá»¨C THá»°C THI CHUáº¨N:** AI **Báº®T BUá»˜C** sá»­ dá»¥ng Custom Skill `wiki-sync-helper` Ä‘á»ƒ cháº¡y lá»‡nh:
> `python .claude/scripts/wiki_sync.py daily-sync --project <project_name> --date <YYYY-MM-DD>`
> Viá»‡c cháº¡y script tá»± Ä‘á»™ng hÃ³a nÃ y Ä‘áº£m báº£o tá»‘c Ä‘á»™ tá»‘i Ä‘a, tiáº¿t kiá»‡m token vÃ  trÃ¡nh sai sÃ³t trong quÃ¡ trÃ¬nh cáº­p nháº­t Kanban vÃ  sinh Bug.

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n:**

1. **Äá»c file Daily Note** (`wiki/[project]/operations/daily_notes/YYYY-MM-DD.md`):

2. **Xá»­ lÃ½ má»¥c "Daily Standup" & Tá»± Ä‘á»™ng hÃ³a xá»­ lÃ½ Bug (CÃ³ HITL Gate):**
   - Cáº­p nháº­t tráº¡ng thÃ¡i cÃ¡c task trong `KANBAN.md` thÃ´ng qua lá»‡nh thá»±c thi tá»± Ä‘á»™ng.
   - **Tá»± Ä‘á»™ng táº¡o Note lá»—i tá»« Standup (Thá»±c hiá»‡n bá»Ÿi script):**
     - Náº¿u pháº§n "KhÃ³ khÄƒn / Blocked" cá»§a Daily Note ghi nháº­n lá»—i cá»¥ thá»ƒ, script tá»± Ä‘á»™ng trÃ­ch xuáº¥t vÃ  khá»Ÿi táº¡o file RCA lá»—i má»›i `bug_[mota_ngan].md` trong `wiki/[project]/bugs_knowledge/` theo máº«u `tpl_bug_rca.md` (tráº¡ng thÃ¡i: `Open`).
     - Tá»± Ä‘á»™ng cáº­p nháº­t tháº» cÃ´ng viá»‡c bá»‹ ngháº½n tÆ°Æ¡ng á»©ng trÃªn Kanban vÃ  Ä‘Ã­nh kÃ¨m link lá»—i mÃ u Ä‘á» á»Ÿ cuá»‘i tháº»: `(ðŸ”´ [[wiki/[project]/bugs_knowledge/bug_tÃªn_lá»—i|BUG-xxx]])`.
   - **ðŸ¤ Cá»”NG KIá»‚M SOÃT GATE 3 (Bug Triage Gate):** AI sau khi táº¡o bug tá»± Ä‘á»™ng pháº£i gá»­i thÃ´ng bÃ¡o cho QA Lead vÃ  Tech Lead. Hai bÃªn thá»±c hiá»‡n há»p sÃ ng lá»c lá»—i (Bug Triage): xÃ¡c thá»±c lá»—i cÃ³ tÃ¡i hiá»‡n Ä‘Æ°á»£c khÃ´ng, Ä‘iá»n chÃ­nh xÃ¡c nguyÃªn nhÃ¢n gá»‘c rá»… (Root Cause Analysis), xÃ¡c Ä‘á»‹nh Ä‘á»™ nghiÃªm trá»ng (Severity: Blocker/Critical/Major/Minor) vÃ  chuyá»ƒn tráº¡ng thÃ¡i file Bug thÃ nh `Open` (Ä‘Ã£ duyá»‡t) hoáº·c `Closed` (náº¿u lá»—i rÃ¡c/khÃ´ng tÃ¡i hiá»‡n).
   - **ÄÃ¡nh dáº¥u Ä‘Ã£ Ä‘á»“ng bá»™ (Sync Tracking):** Äá»•i status cá»§a Daily Note thÃ nh `status: Synced` (hoáº·c gáº¯n tag `#qa/daily/synced`).

3. **Xá»­ lÃ½ má»¥c "Quyáº¿t Äá»‹nh PhÃ¡t Sinh & Thay Äá»•i Requirement" (Sá»­a thá»§ cÃ´ng dÆ°á»›i sá»± giÃ¡m sÃ¡t):**
   - Vá»›i má»—i quyáº¿t Ä‘á»‹nh thay Ä‘á»•i nghiá»‡p vá»¥ ghi nháº­n trong ngÃ y:
     - AI Ä‘á» xuáº¥t cÃ¡c thay Ä‘á»•i vÃ  vá»‹ trÃ­ tá»‡p tin Features & Test Suites bá»‹ áº£nh hÆ°á»Ÿng.
     - AI pháº£i láº­p Impact Analysis vÃ  Regression Proposal giá»‘ng Quy trÃ¬nh 2.2 trÆ°á»›c khi sá»­a.
     - **ðŸ¤ Cá»”NG KIá»‚M SOÃT:** QA Lead vÃ  PO pháº£i xÃ¡c nháº­n sá»± thay Ä‘á»•i trÆ°á»›c khi AI sá»­a Ä‘á»•i thá»§ cÃ´ng cÃ¡c tá»‡p tin nÃ y, ghi nháº­n Changelog vá»›i nguá»“n tham chiáº¿u: `Theo Daily Note [[YYYY-MM-DD]]`.

4. **Ghi nháº­t kÃ½:** Ghi nháº­n hoáº¡t Ä‘á»™ng vÃ o `log.md` vá»›i prefix `[sync-daily]`.

---

### Quy trÃ¬nh 2.4: Dá»n Dáº¹p, Kiá»ƒm Äá»‹nh & Äá»“ng Bá»™ Tá»± Äá»™ng (Lint & Auto-Sync Workflow)

> **KÃ­ch hoáº¡t:** NgÆ°á»i dÃ¹ng yÃªu cáº§u cháº¡y "Lint & Sync".
> 
> **âš ï¸ PHÆ¯Æ NG THá»¨C THá»°C THI CHUáº¨N:** AI **Báº®T BUá»˜C** sá»­ dá»¥ng `.claude/scripts/wiki_sync.py`. Vá»›i yÃªu cáº§u chung nhÆ° `lint vÃ  sync toÃ n bá»™ wiki`, máº·c Ä‘á»‹nh cháº¡y audit-only (`verify`) trÆ°á»›c; chá»‰ cháº¡y `sync` khi ngÆ°á»i dÃ¹ng Ä‘Ã£ xÃ¡c nháº­n Gate 4 cho cÃ¡c task Ä‘Ã£ test xong.
> 
> **ðŸ¤ Cá»”NG KIá»‚M SOÃT GATE 4 (Duyá»‡t káº¿t quáº£ cháº¡y test thá»±c táº¿):** AI TUYá»†T Äá»I khÃ´ng tá»± Ã½ cháº¡y sync náº¿u con ngÆ°á»i chÆ°a xÃ¡c nháº­n cháº¡y test thá»±c táº¿ thÃ nh cÃ´ng.

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n:**

1. **Chá»n cháº¿ Ä‘á»™ cháº¡y an toÃ n:** Náº¿u chÆ°a cÃ³ xÃ¡c nháº­n Gate 4 rÃµ rÃ ng, cháº¡y `python .claude/scripts/wiki_sync.py verify`. Náº¿u Ä‘Ã£ cÃ³ xÃ¡c nháº­n Gate 4, cháº¡y `python .claude/scripts/wiki_sync.py sync` rá»“i cháº¡y/Ä‘Ã­nh kÃ¨m káº¿t quáº£ audit.
2. **Äá»“ng bá»™ tráº¡ng thÃ¡i Kanban:** QuÃ©t `KANBAN.md`. Äá»‘i vá»›i cÃ¡c task `## Done` (cÃ³ xÃ¡c nháº­n Gate 4), AI Ä‘á»‹nh vá»‹ Feature/Test Suite, Ä‘á»•i `status` thÃ nh `Done`/`Passed`, cáº­p nháº­t báº£ng thá»‘ng kÃª test coverage. Äá»‘i vá»›i cÃ¡c task `## InProgress`/`## TODO`, AI Ä‘áº£m báº£o tráº¡ng thÃ¡i pháº£n Ã¡nh Ä‘Ãºng thá»±c táº¿.
3. **Äá»“ng bá»™ tráº¡ng thÃ¡i Go-Live:** AI quÃ©t file `cr_...md` (releases/), Ä‘á»‘i chiáº¿u Test Plans, náº¿u test hoÃ n táº¥t (`Passed`) vÃ  cÃ³ xÃ¡c nháº­n Gate 4/5, AI cáº­p nháº­t Release sang `Testing` vÃ  thÃ´ng bÃ¡o cho QA Lead.
4. **Kiá»ƒm Ä‘á»‹nh Tag & Cáº¥u trÃºc:** QuÃ©t toÃ n bá»™ `wiki/` Ä‘á»ƒ Ä‘áº£m báº£o sá»­ dá»¥ng tag phÃ¢n cáº¥p chuáº©n (`#qa/requirement`, `#qa/api-spec`, `#qa/test-suite`, `#qa/feature-group/...`, v.v.) vÃ  cÃ³ Feature Group page tÆ°Æ¡ng á»©ng.
5. **Kiá»ƒm tra Link & Äá»™ phá»§:** QuÃ©t broken links, orphan notes, má»—i Feature cÃ³ Test Suite tÆ°Æ¡ng á»©ng, API Spec cÃ³ tag/section báº¯t buá»™c náº¿u tá»“n táº¡i, API test suite pháº£i link API Spec, Test Suite cÃ³ cá»™t `Pháº¡m vi`, má»i TC cÃ³ nguá»“n explicit, vÃ  khÃ´ng cÃ³ TC nÃ o cover trá»±c tiáº¿p Requirement/AC/API cÃ²n cÃ¢u há»i `Open`.
6. **Kiá»ƒm tra governance bá»• sung:** Kiá»ƒm Kanban TC count, Changelog, Blocked Coverage, Regression Impact, secret/token, UTF-8/mojibake, status frontmatter, vÃ  cÃ¡c link `index.md`/`log.md`/`KANBAN.md`.
7. **Validation Guardrail:** AI Báº®T BUá»˜C cháº¡y `python .claude/scripts/wiki_sync.py verify` Ä‘á»ƒ quÃ©t lá»—i Ä‘á»©t gÃ£y link/sai status. Káº¿t quáº£ bÃ¡o cÃ¡o pháº£i Ä‘Ã­nh kÃ¨m vÃ o pháº£n há»“i ngÆ°á»i dÃ¹ng.
8. **Ghi nháº­t kÃ½:** Ghi nháº­n vÃ o `log.md` prefix `[lint-sync]`.

---

### Quy trÃ¬nh 2.5: Quy trÃ¬nh Xá»­ lÃ½ VÃ²ng Ä‘á»i Tráº¡ng thÃ¡i Task (Task State Transition Workflow)

> **KÃ­ch hoáº¡t:** NgÆ°á»i dÃ¹ng bÃ¡o cÃ¡o Ä‘Ã£ di chuyá»ƒn tráº¡ng thÃ¡i task trÃªn Kanban (hoáº·c yÃªu cáº§u AI cáº­p nháº­t tráº¡ng thÃ¡i kiá»ƒm thá»­).

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n cá»§a AI:**

1. **Náº¾U CHUYá»‚N SANG `InProgress` (Äang kiá»ƒm thá»­):**
   - Äáº£m báº£o tháº» task Ä‘Ã£ náº±m dÆ°á»›i má»¥c `## InProgress` trong `KANBAN.md`.
   - Náº¿u ká»‹ch báº£n kiá»ƒm thá»­ chÆ°a sáºµn sÃ ng, AI nháº¯c nhá»Ÿ hoáº·c há»— trá»£ sinh cÃ¡c Test Case nhÃ¡p Ä‘á»ƒ chuáº©n bá»‹.
   - Ghi nháº­n hoáº¡t Ä‘á»™ng vÃ o `log.md` vá»›i prefix `[test-progress]`.

2. **Náº¾U CHUYá»‚N SANG `Done` (Kiá»ƒm thá»­ hoÃ n táº¥t):**
   - **Cáº­p nháº­t Test Suite (`wiki/[project]/test_suites/`):**
     - Sá»­a tráº¡ng thÃ¡i táº¥t cáº£ Test Cases tá»« Ä‘ang chá» `â³` thÃ nh Ä‘áº¡t `âœ… Pass` (hoáº·c cáº­p nháº­t theo káº¿t quáº£ ngÆ°á»i dÃ¹ng cung cáº¥p).
     - Äá»•i `status` trong YAML Frontmatter tá»« `Draft` hoáº·c `Testing` thÃ nh `Passed` (náº¿u kiá»ƒm thá»­ thÃ nh cÃ´ng hoÃ n toÃ n).
     - Cáº­p nháº­t báº£ng thá»‘ng kÃª sá»‘ lÆ°á»£ng Test Case (Pass/Fail/Blocked) á»Ÿ Ä‘áº§u file.
   - **Cáº­p nháº­t Feature (`wiki/[project]/features/`):**
     - Äá»•i `status` trong YAML Frontmatter thÃ nh `status: Done` Ä‘á»ƒ xÃ¡c nháº­n nghiá»‡p vá»¥ Ä‘Ã£ Ä‘Æ°á»£c kiá»ƒm thá»­ á»•n Ä‘á»‹nh.
   - **Cáº­p nháº­t Test Plan (`wiki/[project]/test_plans/`):**
     - Äá»•i `status` trong YAML Frontmatter thÃ nh `status: Passed`.
   - **Ghi nháº­t kÃ½:** Ghi nháº­n vÃ o `log.md` vá»›i prefix `[test-run]` lÆ°u váº¿t:
     - Format: `- [YYYY-MM-DD] [test-run] | HoÃ n thÃ nh cháº¡y test [MÃƒ-TASK]. Káº¿t quáº£: [X]/[Y] cases PASS.`

3. **Náº¾U CHUYá»‚N SANG `Blocked` (Bá»‹ ngháº½n):**
   - AI hÆ°á»›ng dáº«n hoáº·c há»— trá»£ táº¡o note ghi nháº­n lá»—i RCA (`tpl_bug_rca.md`) trong thÆ° má»¥c `wiki/[project]/bugs_knowledge/`.
   - Cáº­p nháº­t tháº» trÃªn Kanban, Ä‘Ã­nh kÃ¨m mÃ£ lá»—i dáº¡ng link á»Ÿ cuá»‘i tháº»: `(ðŸ”´ [[wiki/[project]/bugs_knowledge/bug_tÃªn_lá»—i|BUG-xxx]])`.
   - Ghi nháº­n hoáº¡t Ä‘á»™ng vÃ o `log.md` vá»›i prefix `[test-blocked]`.

4. **VÃ²ng Ä‘á»i bug sau khi Dev fix (Bug Lifecycle chuáº©n):**
   - Tráº¡ng thÃ¡i chuáº©n: `Open` âž” `Fixed` âž” `Retest` âž” `Closed`.
   - Khi Dev bÃ¡o fix: cáº­p nháº­t file bug sang `status: Fixed`, ghi báº±ng chá»©ng build/PR.
   - Khi QA retest: ghi káº¿t quáº£ vÃ o bug note vÃ  test suite regression.
   - Náº¿u retest pass: chuyá»ƒn `Closed`; náº¿u fail: quay láº¡i `Open` vÃ  cáº­p nháº­t RCA/changelog.

### Quy trÃ¬nh 2.6: Quy trÃ¬nh ÄÃ³ng gÃ³i vÃ  Nghiá»‡m thu CR Go-Live (Hybrid Model)

> **KÃ­ch hoáº¡t:** Khi káº¿t thÃºc Sprint hoáº·c khi cÃ³ lá»‹ch deploy chÃ­nh thá»©c lÃªn Production dÆ°á»›i mÃ£ Change Request (CR) cá»¥ thá»ƒ.

**CÃ¡c bÆ°á»›c thá»±c hiá»‡n cá»§a AI & Báº¡n:**

1. **Khá»Ÿi táº¡o káº¿ hoáº¡ch (Pháº§n A - Test Plan):**
   - AI hoáº·c Báº¡n táº¡o má»›i **Test Plan** `testplan_cr_[ID].md` trong `wiki/[project]/test_plans/` sá»­ dá»¥ng template `tpl_test_plan.md` (status: `Draft` hoáº·c `Testing`).
   - AI tá»± Ä‘á»™ng khá»Ÿi táº¡o biÃªn báº£n Ä‘Ã³ng gÃ³i **CR Go-Live** `cr_[MÃƒ_CR]_golive_[ddMMyyyy].md` trong `wiki/[project]/releases/` sá»­ dá»¥ng template `tpl_cr_golive.md` (á»Ÿ tráº¡ng thÃ¡i `status: Draft`).
   - Báº¡n vÃ  AI xÃ¡c Ä‘á»‹nh pháº¡m vi kiá»ƒm thá»­ (Scope), liÃªn káº¿t link Specs (`wiki/[project]/features/`), API Specs (`wiki/[project]/api_specs/`, náº¿u cÃ³) vÃ  Test Suite (`wiki/[project]/test_suites/`) tÆ°Æ¡ng á»©ng.
   - Äá»‹nh nghÄ©a Exit Criteria trÃªn Staging (100% Passed, khÃ´ng cÃ²n bug nghiÃªm trá»ng).

2. **ÄÃ³ng gÃ³i ká»¹ thuáº­t (Pháº§n B - Go-Live Plan):**
   - Khi táº¥t cáº£ ká»‹ch báº£n test trÃªn Staging Ä‘Ã£ PASS (`status: Passed`), AI sáº½ há»— trá»£ Báº¡n & Dev/DevOps soáº¡n tháº£o ká»‹ch báº£n triá»ƒn khai tá»«ng bÆ°á»›c (Deploy Steps) vÃ  ká»‹ch báº£n khÃ´i phá»¥c (Rollback Steps) Ä‘á» phÃ²ng sá»± cá»‘.
   - Thiáº¿t láº­p danh sÃ¡ch cÃ¡c ká»‹ch báº£n kiá»ƒm thá»­ nhanh (Smoke Test) trá»±c tiáº¿p trÃªn mÃ´i trÆ°á»ng Production báº±ng tÃ i khoáº£n tháº­t.

3. **Nghiá»‡m thu thá»±c táº¿ (Production Smoke Test):**
   - Sau khi deploy thÃ nh cÃ´ng, Báº¡n cháº¡y Smoke Test trÃªn Production.
   - Cáº­p nháº­t káº¿t quáº£ Ä‘áº¡t (`âœ… Pass`) hoáº·c lá»—i (`âŒ Fail`) vÃ o báº£ng Smoke Test cá»§a file CR.
   - Náº¿u Smoke Test thÃ nh cÃ´ng hoÃ n toÃ n âž” Äá»•i tráº¡ng thÃ¡i file CR sang `status: Done`.
   - Náº¿u Smoke Test tháº¥t báº¡i nghiÃªm trá»ng âž” KÃ­ch hoáº¡t ngay Rollback Steps Ä‘á»ƒ Ä‘Æ°a há»‡ thá»‘ng vá» tráº¡ng thÃ¡i á»•n Ä‘á»‹nh cÅ©.

4. **Dá»n dáº¹p & LÆ°u trá»¯:**
   - Khi CR Ä‘Ã£ `Done`, Báº¡n thá»±c hiá»‡n **Archive** cÃ¡c tháº» tÆ°Æ¡ng á»©ng trÃªn báº£ng Kanban.
   - AI ghi nháº­n hoáº¡t Ä‘á»™ng nghiá»‡m thu vÃ o `log.md` vá»›i prefix `[test-run]`.

---

## ðŸ“‹ 3. QUY CHUáº¨N VIáº¾T TÃ€I LIá»†U

### 3.1. File Feature (`wiki/[project]/features/`) â€” Chuáº©n BA

Má»i file feature PHáº¢I chá»©a Ä‘áº§y Ä‘á»§ cÃ¡c má»¥c sau (theo template `tpl_requirement.md`):

1. **Metadata (YAML Frontmatter):** tags, status, feature, project, source_version
2. **Tá»•ng quan:** Feature, MÃ´ táº£ ngáº¯n, Source chÃ­nh, Äá»‘i tÆ°á»£ng sá»­ dá»¥ng (Actors)
3. **Nguá»“n tÃ i liá»‡u:** Báº£ng liá»‡t kÃª PDF/Link kÃ¨m version vÃ  status
4. **API / Interface liÃªn quan:** Chá»‰ link tá»›i API Spec; khÃ´ng nhÃºng full API contract vÃ o Feature Spec
5. **PhÃ¢n rÃ£ Requirement:** Báº£ng liá»‡t kÃª tá»«ng yÃªu cáº§u vá»›i ID, loáº¡i, priority, testable, source
6. **Luá»“ng Nghiá»‡p Vá»¥ Chi Tiáº¿t (User Flows):**
   - Äiá»u kiá»‡n tiÃªn quyáº¿t (Pre-conditions)
   - Luá»“ng chuáº©n (Happy Path) â€” dáº¡ng bÆ°á»›c Ä‘Ã¡nh sá»‘
   - Luá»“ng ráº½ nhÃ¡nh (Alternative Paths) â€” dáº¡ng Alt-Flow
   - Luá»“ng ngoáº¡i lá»‡ (Exception Paths) â€” dáº¡ng Exc-Flow
7. **Quy Táº¯c Nghiá»‡p Vá»¥ & RÃ ng Buá»™c Dá»¯ Liá»‡u:** Báº£ng validation chi tiáº¿t
8. **Äáº·c Táº£ ThÃ´ng Äiá»‡p BÃ¡o Lá»—i:** Error Messages Map
9. **TiÃªu ChÃ­ Nghiá»‡m Thu:** Acceptance Criteria dáº¡ng BDD (Given-When-Then)
10. **CÃ¢u há»i chÆ°a rÃµ:** Báº£ng lifecycle cÃ¢u há»i (`Q-ID`, R/AC liÃªn quan, tráº¡ng thÃ¡i, nguá»“n tráº£ lá»i)
11. **Thay Ä‘á»•i so vá»›i version cÅ©:** Báº£ng diff cÃ³ phÃ¢n loáº¡i Add/Update/Remove/Clarify
12. **Impact Analysis & Regression Proposal:** Báº£ng tÃ¡c Ä‘á»™ng vÃ  Ä‘á» xuáº¥t regression
13. **Test Coverage:** Báº£ng mapping Requirement â†’ Test Cases, gá»“m coverage bá»‹ blocked do question
14. **ðŸ“… Changelog:** Báº£ng lá»‹ch sá»­ thay Ä‘á»•i (NgÃ y | Version | Ná»™i dung | Nguá»“n)

### 3.2. File API Spec (`wiki/[project]/api_specs/`) â€” Chuáº©n Interface Contract

Má»—i API Spec PHáº¢I chá»©a (theo template `tpl_api_spec.md`):

1. **Metadata (YAML Frontmatter):** `tags: [qa/api-spec]`, `status`, `project`, `feature`, `feature_group`.
2. **Tá»•ng quan:** Feature liÃªn quan, Feature Group, source chÃ­nh, Test Suite API tÆ°Æ¡ng á»©ng.
3. **API / Interface List:** `API ID | Method | Endpoint | Má»¥c Ä‘Ã­ch | Feature R/AC | Source | Status`.
4. **API Detail:** Auth, headers, path/query params, request body, success response, error response, validation/business side effects.
5. **CÃ¢u há»i API chÆ°a rÃµ:** DÃ¹ng lifecycle giá»‘ng Feature questions; khÃ´ng suy diá»…n endpoint, payload, status code, error message hoáº·c side effect.
6. **API Test Coverage:** Mapping API/R/AC -> Test Case hoáº·c Blocked Coverage.
7. **ðŸ“… Changelog:** Báº£ng lá»‹ch sá»­ thay Ä‘á»•i.

Feature Spec lÃ  nÆ¡i mÃ´ táº£ WHAT/WHY nghiá»‡p vá»¥; API Spec lÃ  nÆ¡i mÃ´ táº£ HOW interface contract. Khi source chá»‰ nÃ³i nghiá»‡p vá»¥ mÃ  khÃ´ng nÃ³i API, khÃ´ng táº¡o API Spec giáº£ Ä‘á»‹nh.

### 3.3. File Test Suite (`wiki/[project]/test_suites/`) â€” Chuáº©n QA

Má»i file test suite PHáº¢I chá»©a (theo template `tpl_test_suite.md`):

1. **Metadata (YAML Frontmatter)**
2. **ThÃ´ng tin liÃªn káº¿t:** Feature, Requirement, Dev/QA phá»¥ trÃ¡ch
3. **Tá»•ng quan Test Coverage:** Báº£ng thá»‘ng kÃª sá»‘ TC theo loáº¡i test
4. **Báº£ng Test Cases:** `Test ID | TiÃªu Ä‘á» | AC/Req Cover | Pháº¡m vi | Loáº¡i case | Ká»¹ thuáº­t test | Äiá»u kiá»‡n tiÃªn quyáº¿t | CÃ¡c bÆ°á»›c | Káº¿t quáº£ mong Ä‘á»£i | Nguá»“n | Status`
5. **Blocked Coverage:** Requirement/AC chÆ°a Ä‘Æ°á»£c sinh TC vÃ¬ cÃ²n cÃ¢u há»i `Open`
6. **Regression Impact:** Test case cÅ© cáº§n cháº¡y láº¡i khi requirement/task thay Ä‘á»•i
7. **Test Cases Lá»—i Thá»i (Deprecated):** LÆ°u trá»¯ case cÅ©, KHÃ”NG xÃ³a
8. **ðŸ“… Changelog:** Báº£ng lá»‹ch sá»­ thay Ä‘á»•i

### 3.4. Quy táº¯c viáº¿t Test Case

Khi thiáº¿t káº¿ Test Cases, AI PHáº¢I Ä‘á»c cÃ¡c file sau Ä‘á»ƒ cÃ³ Ä‘á»§ ngá»¯ cáº£nh:

| File cáº§n Ä‘á»c | Má»¥c Ä‘Ã­ch |
|:-------------|:---------|
| File Feature tÆ°Æ¡ng á»©ng (`wiki/[project]/features/`) | Láº¥y logic nghiá»‡p vá»¥, luá»“ng Ä‘i, rÃ ng buá»™c dá»¯ liá»‡u |
| API Spec liÃªn quan (`wiki/[project]/api_specs/`) | Láº¥y method, endpoint, payload, response, error contract cho test API náº¿u cÃ³ |
| `wiki/[project]/operations/environments.md` | Láº¥y URL, tÃ i khoáº£n test máº«u thá»±c táº¿ |
| `wiki/[project]/operations/test_data.md` | Láº¥y dá»¯ liá»‡u test máº«u (SÄT, tháº», payload) |
| CÃ¡c file bug liÃªn quan (`wiki/[project]/bugs_knowledge/`) | Bá»• sung Regression Test Cases tá»« lá»—i cÅ© |
| `WIKI_RULES.md` (file nÃ y) | TuÃ¢n thá»§ Ä‘á»‹nh dáº¡ng vÃ  quy táº¯c Ä‘áº·t tÃªn |

Má»—i Test Case Báº®T BUá»˜C ghi rÃµ:
- **AC/Req Cover:** Requirement ID (`R1`, `R2`...) vÃ /hoáº·c Acceptance Criteria/BDD Scenario Ä‘Æ°á»£c cover (`AC-01`, `Scenario 1`...).
- **Pháº¡m vi:** `UI`, `API`, `Functional`, `UI+Functional`, `API+Functional`, `UI+API`, hoáº·c `E2E`.
- **Loáº¡i case:** `Positive` hoáº·c `Negative`. Náº¿u lÃ  regression/security/performance thÃ¬ váº«n pháº£i nÃªu rÃµ positive/negative theo ká»³ vá»ng hÃ nh vi.
- **Ká»¹ thuáº­t test:** VÃ­ dá»¥ `Happy Path`, `Equivalence Partitioning`, `Boundary Value Analysis`, `Decision Table`, `State Transition`, `Error Guessing`, `Security`, `Regression`.
- **Nguá»“n:** Chá»‰ ghi `Explicit tá»« [nguá»“n]` cho test case bÃ¡m trá»±c tiáº¿p tá»« Requirement/AC/API Spec Ä‘Ã£ mÃ´ táº£ rÃµ.
- **KhÃ´ng suy diá»…n:** KhÃ´ng táº¡o test case tá»« giáº£ Ä‘á»‹nh hoáº·c suy luáº­n. Má»i Ä‘iá»ƒm chÆ°a rÃµ pháº£i Ä‘Æ°a vá» `## â“ CÃ¢u há»i chÆ°a rÃµ` cá»§a Feature Spec hoáº·c `## â“ CÃ¢u há»i API chÆ°a rÃµ` cá»§a API Spec.
- **KhÃ´ng sinh TC tá»« cÃ¢u há»i má»Ÿ:** Náº¿u TC phá»¥ thuá»™c vÃ o cÃ¢u há»i chÆ°a tráº£ lá»i, khÃ´ng ghi vÃ o báº£ng Test Cases; ghi vÃ o `Blocked Coverage`, Feature Questions hoáº·c API Spec Questions. Khi cÃ¢u há»i Ä‘Æ°á»£c tráº£ lá»i, cáº­p nháº­t Feature Spec/API Spec trÆ°á»›c rá»“i má»›i sinh TC.
- **API TC:** Chá»‰ táº¡o khi cÃ³ API Spec explicit hoáº·c cÃ¢u tráº£ lá»i `Answered` nÃªu rÃµ method/endpoint/auth/header/request/response/status/error. Náº¿u thiáº¿u status code, payload, error response hoáº·c side effect thÃ¬ ghi question/blocked coverage, khÃ´ng tá»± Ä‘oÃ¡n theo convention REST.
- **Traceability:** KhÃ´ng táº¡o test case náº¿u khÃ´ng truy ngÆ°á»£c Ä‘Æ°á»£c vá» Requirement/AC rÃµ rÃ ng; test API pháº£i truy ngÆ°á»£c thÃªm vá» API ID trong API Spec.

### 3.5. File Feature Group (`wiki/[project]/feature_groups/`) â€” Group MOC

Má»—i Feature Group page PHáº¢I chá»©a:
1. **Metadata:** `tags: [qa/feature-group-index, qa/feature-group/[slug]]`, `status`, `project`, `feature_group`.
2. **Tá»•ng quan:** má»¥c Ä‘Ã­ch group, pháº¡m vi nghiá»‡p vá»¥, raw source chÃ­nh.
3. **Feature Specs trong group:** báº£ng link Feature, vai trÃ², status, Gate.
4. **API Specs trong group:** báº£ng link API Spec, feature cover, API/interface cover, open questions, status.
5. **Test Suites trong group:** báº£ng link Test Suite, sá»‘ TC, blocked coverage, status.
6. **Test Plan / Release liÃªn quan:** link tá»›i plan/release náº¿u cÃ³.
7. **Open Questions & Blocked Coverage:** tá»•ng há»£p link tá»›i cÃ¡c feature/API Spec/test suite cÃ²n question/blocker.
8. **Impact & Regression Notes:** nÆ¡i tá»•ng há»£p change impact cáº¥p group.
9. **Changelog:** má»i cáº­p nháº­t group page.

---

## ðŸ“„ 4. QUY Táº®C CÃC FILE ÄIá»€U KHIá»‚N

### 4.1. `index.md` â€” Báº£n Ä‘á»“ Ä‘iá»u hÆ°á»›ng
- Liá»‡t kÃª Táº¤T Cáº¢ cÃ¡c trang trong wiki kÃ¨m link `[[...]]` vÃ  mÃ´ táº£ 1 dÃ²ng.
- PhÃ¢n loáº¡i theo: Feature Groups, Features, API Specs, Test Suites, Bugs, Operations.
- AI Ä‘á»c file nÃ y Äáº¦U TIÃŠN khi xá»­ lÃ½ báº¥t ká»³ cÃ¢u há»i nÃ o.
- Cáº­p nháº­t ngay khi cÃ³ trang má»›i Ä‘Æ°á»£c táº¡o.

### 4.2. `KANBAN.md` â€” Báº£ng Kanban & Quy trÃ¬nh Quáº£n lÃ½ Task
- **Sá»± Ä‘á»“ng bá»™ 2 chiá»u (Markdown âž” Kanban UI):** File `KANBAN.md` Ä‘Æ°á»£c lÆ°u dÆ°á»›i dáº¡ng danh sÃ¡ch gáº¡ch Ä‘áº§u dÃ²ng Markdown nhÆ°ng hiá»ƒn thá»‹ dÆ°á»›i dáº¡ng báº£ng Kanban kÃ©o tháº£ trÃªn Obsidian. AI cáº­p nháº­t file báº±ng cÃ¡ch chá»‰nh sá»­a danh sÃ¡ch text, con ngÆ°á»i tÆ°Æ¡ng tÃ¡c qua giao diá»‡n kÃ©o tháº£.
- **Cáº¥u trÃºc cá»™t chuáº©n:** Báº£ng gá»“m 3 cá»™t tÆ°Æ¡ng á»©ng vá»›i cÃ¡c tiÃªu Ä‘á» Markdown cá»§a plugin Kanban:
  - `## TODO`: HÃ ng Ä‘á»£i kiá»ƒm thá»­.
  - `## InProgress`: CÃ¡c task Ä‘ang thá»±c hiá»‡n hoáº·c bá»‹ ngháº½n.
  - `## Done`: CÃ¡c task Ä‘Ã£ pass test hoÃ n toÃ n.
- **Quy táº¯c ghi Task & Quáº£n lÃ½ ID (AI & Con ngÆ°á»i):**
  - **Task tá»« dá»± Ã¡n (Specs/Tickets - active testing):** Báº¯t buá»™c thá»«a hÆ°á»Ÿng nguyÃªn váº¹n ID gá»‘c cá»§a dá»± Ã¡n (vÃ­ dá»¥: `JIRA-xxx`, `TICKET-xxx`) Ä‘á»ƒ Ä‘á»“ng bá»™ vá»›i Dev/PO.
    - CÃº phÃ¡p: `- [ ] [[raw_sources/[project]/tasks/MÃƒ-TASK|MÃƒ-TASK]] âž” [[wiki/[project]/test_suites/test_tÃªn_feature|Test Suite TÃªn TÃ­nh NÄƒng]] [Äá»™_Æ°u_tiÃªn]`.
    - *VÃ­ dá»¥:* `- [ ] <raw_sources/[project]/tasks/[task-code]> âž” <wiki/[project]/test_suites/test_[feature]> [High]`.
  - **Task Káº¿ hoáº¡ch kiá»ƒm thá»­ (Test Plans):** DÃ nh cho viá»‡c chuáº©n bá»‹ vÃ  duyá»‡t chiáº¿n lÆ°á»£c test.
    - CÃº phÃ¡p: `- [ ] [QA Internal] [[wiki/[project]/test_plans/testplan_xxx|Test Plan MÃ£]] âž” MÃ´ táº£ cÃ´ng viá»‡c`.
    - *VÃ­ dá»¥:* `- [ ] [QA Internal] <wiki/[project]/test_plans/testplan_cr_[id]> âž” Review chiáº¿n lÆ°á»£c & chuáº©n bá»‹ data test Staging`.
  - **Task Ä‘á»£t triá»ƒn khai Go-Live (Releases/Deploy):** DÃ nh cho quy trÃ¬nh deploy vÃ  nghiá»‡m thu Production.
    - CÃº phÃ¡p: `- [ ] [Release] [[wiki/[project]/releases/cr_xxx|MÃ£-CR]] âž” Phá»‘i há»£p deploy & cháº¡y Smoke Test Prod [NgÃ y]`.
    - *VÃ­ dá»¥:* `- [ ] [Release] <wiki/[project]/releases/cr_[id]_golive_[ddMMyyyy]> âž” Phá»‘i há»£p deploy & cháº¡y Smoke Test Production [30/05/2026]`.
  - **Task sá»­a lá»—i (Bug Reports):** Sá»­ dá»¥ng trá»±c tiáº¿p mÃ£ lá»—i cá»§a dá»± Ã¡n.
    - CÃº phÃ¡p: `- [ ] [[wiki/bugs_knowledge/bug_tÃªn_lá»—i|BUG-xxx]] âž” Kiá»ƒm thá»­ láº¡i lá»—i [Äá»™_Æ°u_tiÃªn]`.
  - **Task bá»‹ ngháº½n (Blocked):** Náº¿u task Ä‘ang test bá»‹ ngháº½n do phÃ¡t sinh bug, báº¯t buá»™c ghi kÃ¨m mÃ£ bug dáº¡ng link á»Ÿ cuá»‘i tháº» Ä‘á»ƒ dá»… truy váº¿t: `... âž” Test Suite [High] (ðŸ”´ [[wiki/bugs_knowledge/bug_tÃªn_lá»—i|BUG-xxx]])`.
- **Luá»“ng cáº­p nháº­t tá»± Ä‘á»™ng cá»§a AI:**
  - **Khi Khá»Ÿi táº¡o Sprint (Sprint planning & Setup):** AI tá»± Ä‘á»™ng táº¡o 3 loáº¡i tháº» cÃ´ng viá»‡c liÃªn quan vÃ  phÃ¢n bá»• vÃ o Ä‘Ãºng cá»™t tráº¡ng thÃ¡i:
    - **Tháº» Káº¿ hoáº¡ch kiá»ƒm thá»­ (`[QA Internal] testplan_...`)**: Äáº·t dÆ°á»›i cá»™t `## InProgress` (vÃ¬ QA Lead sáº½ triá»ƒn khai viáº¿t chiáº¿n lÆ°á»£c vÃ  chuáº©n bá»‹ dá»¯ liá»‡u test ngay láº­p tá»©c á»Ÿ Ä‘áº§u Sprint).
    - **Tháº» ká»‹ch báº£n cháº¡y test (`[MÃ£-Task] âž” Test Suite...`)**: Äáº·t dÆ°á»›i cá»™t `## TODO` (chá» Dev code xong vÃ  bÃ n giao báº£n build trÃªn Staging).
    - **Tháº» Ä‘á»£t triá»ƒn khai Go-Live (`[Release] cr_...`)**: Äáº·t dÆ°á»›i cá»™t `## TODO` (Ä‘Ã³ng vai trÃ² cá»™t má»‘c Milestone theo dÃµi thá»i háº¡n phÃ¡t hÃ nh cuá»‘i Sprint).
  - **Khi náº¡p Specs má»›i láº» (Ingest):** AI tá»± Ä‘á»™ng chÃ¨n má»™t dÃ²ng check-list cháº¡y test má»›i vÃ o dÆ°á»›i cá»™t `## TODO` trong `KANBAN.md`.
  - **Khi Ä‘á»“ng bá»™ Daily Note (Daily Sync):** AI Ä‘á»c Daily Note cá»§a ngÃ y hÃ´m Ä‘Ã³, náº¿u tháº¥y task Ä‘Æ°á»£c bÃ¡o Ä‘Ã£ hoÃ n thÃ nh hoáº·c bá»‹ ngháº½n, AI pháº£i chá»§ Ä‘á»™ng di chuyá»ƒn dÃ²ng check-list tÆ°Æ¡ng á»©ng sang cá»™t `## Done` hoáº·c `## InProgress` trong `KANBAN.md`.
- KHÃ”NG ghi Changelog trong file nÃ y Ä‘á»ƒ giá»¯ báº£ng Kanban luÃ´n sáº¡ch Ä‘áº¹p. Má»i thay Ä‘á»•i tráº¡ng thÃ¡i Ä‘Æ°á»£c ghi nháº­n táº¡i `log.md`.

### 4.3. `log.md` â€” Nháº­t kÃ½ há»‡ thá»‘ng
- Ghi chÃ©p TOÃ€N Bá»˜ hÃ nh Ä‘á»™ng AI thá»±c hiá»‡n theo thá»i gian thá»±c Ä‘á»ƒ Ä‘áº£m báº£o tÃ­nh truy váº¿t (Audit Trail).
- **Quy táº¯c sáº¯p xáº¿p:** Báº¯t buá»™c xáº¿p dÃ²ng nháº­t kÃ½ **Má»›i nháº¥t lÃªn Ä‘áº§u tiÃªn** (ngay dÆ°á»›i dÃ²ng tiÃªu Ä‘á» `---` á»Ÿ pháº§n ná»™i dung) Ä‘á»ƒ dá»… theo dÃµi tá»©c thÃ¬ mÃ  khÃ´ng cáº§n cuá»™n chuá»™t xuá»‘ng Ä‘Ã¡y file.
- Format báº¯t buá»™c: `- [YYYY-MM-DD HH:mm:ss] [action-type] | MÃ´ táº£ ngáº¯n gá»n`
  - *VÃ­ dá»¥:* `- [2026-05-23 10:25:20] [lint-sync] | HoÃ n thÃ nh quÃ©t há»‡ thá»‘ng...`
- CÃ¡c action-type: `[ingest]`, `[task-update]`, `[sync-daily]`, `[lint]`, `[lint-sync]`, `[test-progress]`, `[test-run]`, `[test-blocked]`, `[create]`

### 4.5. Quy táº¯c Git váº­n hÃ nh

- Sau má»—i batch xá»­ lÃ½ (ingest/task-update/daily-sync/lint-sync), AI báº¯t buá»™c cháº¡y kiá»ƒm tra thay Ä‘á»•i báº±ng `git status`.
- Commit theo lÃ´ nhá», message rÃµ nghiá»‡p vá»¥, vÃ­ dá»¥:
  - `docs: update feature spec for CR-ORANGE-200`
  - `test: add regression cases for BUG-123`
- KhÃ´ng sá»­a hoáº·c revert cÃ¡c thay Ä‘á»•i ngoÃ i pháº¡m vi yÃªu cáº§u hiá»‡n táº¡i.
- Chá»‰ push khi ngÆ°á»i dÃ¹ng yÃªu cáº§u hoáº·c khi quy trÃ¬nh káº¿t thÃºc vÃ  Ä‘Ã£ Ä‘Æ°á»£c xÃ¡c nháº­n.


### 4.4. Changelog (trong tá»«ng file feature, API spec & test suite)
- Báº®T BUá»˜C ghi nháº­n Má»ŒI thay Ä‘á»•i ná»™i dung cá»§a tÃ i liá»‡u nghiá»‡p vá»¥ vÃ  ká»‹ch báº£n test.
- **Quy táº¯c sáº¯p xáº¿p:** Báº¯t buá»™c xáº¿p dÃ²ng thay Ä‘á»•i **Má»›i nháº¥t lÃªn Ä‘áº§u tiÃªn** cá»§a báº£ng Changelog (dÆ°á»›i dÃ²ng tiÃªu Ä‘á» cá»™t `|:---|...`).
- Format báº£ng tiÃªu chuáº©n: `| Thá»i gian | Version | Ná»™i dung thay Ä‘á»•i | Nguá»“n |`
  - TrÆ°á»ng **Thá»i gian** pháº£i ghi Ä‘áº§y Ä‘á»§: `YYYY-MM-DD HH:mm:ss` Ä‘á»ƒ phá»¥c vá»¥ cho cÃ¡c phiÃªn báº£n thay Ä‘á»•i nhanh trong ngÃ y.
  - *VÃ­ dá»¥:* `| 2026-05-23 10:10:29 | v1.0 | Khá»Ÿi táº¡o Specs | <raw_sources/[project]/tasks/[task-code]> |`
- Nguá»“n pháº£i tham chiáº¿u rÃµ rÃ ng báº±ng link liÃªn káº¿t: MÃ£ Task Jira, Daily Note, hoáº·c tÃªn file PDF gá»‘c.

### 4.6. Update Propagation Checklist

Khi cÃ³ thay Ä‘á»•i requirement/task/test case, AI pháº£i kiá»ƒm tra vÃ  cáº­p nháº­t Ä‘á»§ cÃ¡c nÆ¡i liÃªn quan:
- `raw_sources/[project]/...`: lÆ°u raw task/PDF/converted markdown náº¿u cÃ³ nguá»“n má»›i.
- `wiki/[project]/features/`: cáº­p nháº­t Requirement/AC, Questions, Impact Analysis, Regression Proposal, Test Coverage, Changelog.
- `wiki/[project]/api_specs/`: cáº­p nháº­t API contract explicit, API Questions, API Test Coverage, Changelog vÃ  link Feature/Test Suite náº¿u API/interface thay Ä‘á»•i.
- `wiki/[project]/feature_groups/`: cáº­p nháº­t group page náº¿u feature/API Spec/test suite thuá»™c group Ä‘Æ°á»£c thÃªm, Ä‘á»•i tÃªn, deprecated hoáº·c thay Ä‘á»•i tráº¡ng thÃ¡i.
- `wiki/[project]/test_suites/`: add/update/deprecate TC theo Feature/API Spec Ä‘Ã£ duyá»‡t, cáº­p nháº­t Blocked Coverage, Regression Impact, tá»•ng sá»‘ TC, Changelog.
- `wiki/[project]/test_plans/`: cáº­p nháº­t In-Scope, Regression Scope, Coverage vÃ  Entry/Exit Criteria náº¿u pháº¡m vi test thay Ä‘á»•i.
- `KANBAN.md`: cáº­p nháº­t tháº», tráº¡ng thÃ¡i vÃ  sá»‘ lÆ°á»£ng TC náº¿u cÃ³ thay Ä‘á»•i sá»‘ TC.
- `index.md`: thÃªm/xÃ³a link khi cÃ³ page má»›i hoáº·c archive.
- `log.md`: ghi má»™t dÃ²ng audit cho batch thay Ä‘á»•i vá»›i timestamp `UTC+07:00`.
- `git status`: kiá»ƒm tra thay Ä‘á»•i cuá»‘i batch, khÃ´ng revert file ngoÃ i pháº¡m vi.


## AI Knowledge Scope

- Normative policy source is `.claude/rules/*.md` (this file must not contradict it).
- Allowed scope: `wiki/`, `raw_sources/`, `templates/`, `.claude/commands/`, `.claude/scripts/`, and root control docs.
- Excluded by default: `.obsidian/`, `.smart-env/`, `.karate_cache/`, `.git/`, `__pycache__/`, plugin/cache/db.
- Do not infer requirement/AC/API/test case from excluded scope.
- If unclear, move to Question and Blocked Coverage.
- Timezone standard: `Asia/Saigon` (`UTC+07:00`).
- Encoding standard: UTF-8, no mojibake.


## Task Spec + Feature Spec Layering (Hasaki)

- Task Spec is an execution-layer document per TBB2 task under wiki/project_hasaki/task_specs/.
- Feature Spec remains the domain-layer source of business behavior and AC.
- Required traceability chain: TBB2 -> HSK -> Task Spec -> Feature Group -> Feature Spec -> Requirement/AC -> Testcase.
- If Question is Open, testcase for related unclear behavior must not be generated; put it in Blocked Coverage.
- On task updates, update propagation is mandatory: Task Spec -> Feature/API Spec -> Traceability -> Testcase/Regression.

