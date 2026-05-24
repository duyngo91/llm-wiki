# USER COMMANDS

Trang nÃ y dÃ nh cho ngÆ°á»i dÃ¹ng cuá»‘i. Chá»‰ cáº§n bá» file vÃ o Ä‘Ãºng thÆ° má»¥c `raw_sources/` rá»“i dÃ¹ng cÃ¡c cÃ¢u lá»‡nh bÃªn dÆ°á»›i.

---

## ðŸ“‹ Luá»“ng SDLC chuáº©n

- **BÆ°á»›c 1** â€” Khá»Ÿi táº¡o project má»›i (náº¿u chÆ°a cÃ³):
  - `táº¡o project má»›i tÃªn project_xxx theo chuáº©n wiki rules`

- **BÆ°á»›c 2** â€” Náº¡p requirement má»›i (bá» PDF vÃ o `raw_sources/[project]/requirements/` trÆ°á»›c):
  - `ingest file [tÃªn file] trong raw_sources/[project]/requirements`
  - Náº¿u PDF cÃ³ API/interface explicit, AI táº¡o thÃªm API Spec riÃªng trong `wiki/[project]/api_specs/`.

- **BÆ°á»›c 3a** â€” PhÃ¢n tÃ­ch task tá»« file Jira/ticket (bá» file vÃ o `raw_sources/[project]/tasks/` trÆ°á»›c):
  - `phÃ¢n tÃ­ch task [tÃªn file] thuá»™c [project] vÃ  táº¡o specs + test suite`
  - Náº¿u task nháº¯c API nhÆ°ng thiáº¿u endpoint/method/payload/status rÃµ rÃ ng, AI chá»‰ ghi question, chÆ°a sinh API test case.

- **BÆ°á»›c 3b** â€” Import task tá»« Hasaki Workplace:
  - `import task HSK-XXXXX`
  - `tÃ´i cáº§n test task HSK-XXXXX`
  - paste URL: `https://work.hasaki.vn/tasks?...&task_id=...`

- **BÆ°á»›c 4** â€” Táº¡o Test Plan cho CR:
  - `táº¡o test plan cho CR-[ID] thuá»™c [project]`

- **BÆ°á»›c 5** â€” Äá»“ng bá»™ daily note trong quÃ¡ trÃ¬nh test:
  - `daily sync [project] ngÃ y YYYY-MM-DD`

- **BÆ°á»›c 6** â€” Chá»‘t task Ä‘Ã£ test xong:
  - `chuyá»ƒn task [MÃƒ-TASK] sang Done vÃ  cáº­p nháº­t suite/feature/plan`

- **BÆ°á»›c 7** â€” Khá»Ÿi táº¡o CR Go-Live:
  - `táº¡o CR golive cho CR-[ID] ngÃ y DD/MM/YYYY thuá»™c [project]`

- **BÆ°á»›c 8** â€” Chá»‘t CR sau smoke test production:
  - `cáº­p nháº­t káº¿t quáº£ smoke test vÃ  chá»‘t CR [MÃƒ-CR] sang Done`

- **Báº¥t ká»³ lÃºc nÃ o** â€” Kiá»ƒm Ä‘á»‹nh toÃ n bá»™ wiki:
  - `lint vÃ  sync toÃ n bá»™ wiki`
  - Máº·c Ä‘á»‹nh cháº¡y audit-only (`verify`) náº¿u báº¡n chÆ°a xÃ¡c nháº­n Ä‘Ã£ test thá»±c táº¿ thÃ nh cÃ´ng.
  - Chá»‰ sync tráº¡ng thÃ¡i `Done/Passed` khi cÃ³ xÃ¡c nháº­n Gate 4 rÃµ rÃ ng.

---

## ðŸ” Tra cá»©u task Hasaki (máº·c Ä‘á»‹nh khÃ´ng lÆ°u vault)

Chá»‰ xem thÃ´ng tin, khÃ´ng phÃ¢n tÃ­ch:
- `láº¥y task HSK-XXXXX`
- `get my task HSK-XXXXX`
- `Ä‘á»c task 12032444`

LÆ°u Ã½:
- Náº¿u dÃ¹ng biáº¿n thá»ƒ `vÃ  táº£i hÃ¬nh vá»`, áº£nh sáº½ Ä‘Æ°á»£c lÆ°u vÃ o `raw_sources/project_hasaki/assets` (cÃ³ ghi vÃ o vault).
- Náº¿u muá»‘n fetch + phÃ¢n tÃ­ch + lÆ°u task markdown + cáº­p nháº­t kanban, dÃ¹ng `import task HSK-XXXXX` (`/import-hasaki-task`).

---

## ðŸ’» Cháº¡y lá»‡nh tay (terminal)

```powershell
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

# Äá»“ng bá»™ daily note
python .claude/scripts/wiki_sync.py daily-sync --project project_hasaki --date 2026-05-23

# Sync Kanban + coverage
python .claude/scripts/wiki_sync.py sync

# Audit broken links + status
python .claude/scripts/wiki_sync.py verify

# Fetch task Hasaki (chá»‰ xem)
$env:PYTHONUTF8 = "1"
python .claude/scripts/hasaki_task.py HSK-XXXXX

# Fetch task Hasaki kÃ¨m táº£i áº£nh
$env:PYTHONUTF8 = "1"
python .claude/scripts/hasaki_task.py HSK-XXXXX --images --output raw_sources/project_hasaki/assets
```

---

## ðŸ“¥ NÆ¡i bá» file Ä‘áº§u vÃ o

| Loáº¡i file | ThÆ° má»¥c |
|-----------|---------|
| Requirement / PDF / FSD / BRD | `raw_sources/[project]/requirements/` |
| Task / Jira ticket | `raw_sources/[project]/tasks/` |
| API document / interface contract | `raw_sources/[project]/requirements/` hoáº·c link trong task |
| Log lá»—i thÃ´ / crash log | `raw_sources/[project]/issues/` |
| áº¢nh / video báº±ng chá»©ng | `raw_sources/[project]/assets/` |

> **Hasaki Workplace tasks** khÃ´ng cáº§n bá» file thá»§ cÃ´ng â€” dÃ¹ng `/import-hasaki-task` Ä‘á»ƒ AI tá»± fetch qua API.

---

## ðŸ”‘ Token Hasaki

Token lÆ°u táº¡i `token.txt` (root vault). Háº¿t háº¡n sau ~48h ká»ƒ tá»« lÃºc Ä‘Äƒng nháº­p.

CÃ¡ch láº¥y token má»›i:
1. ÄÄƒng nháº­p `work.hasaki.vn`
2. F12 â†’ Application â†’ Cookies â†’ `work.hasaki.vn`
3. Copy giÃ¡ trá»‹ cookie `wshr-token`
4. Paste vÃ o `token.txt` (xoÃ¡ ná»™i dung cÅ©)


## AI Knowledge Scope

- Follow `.claude/rules/*.md` as the normative policy source.
- Allowed scope: `wiki/`, `raw_sources/`, `templates/`, `.claude/commands/`, `.claude/scripts/`, and root control docs.
- Excluded by default: `.obsidian/`, `.smart-env/`, `.karate_cache/`, `.git/`, plugin/cache/db.
- Do not infer requirement/AC/API/test case from excluded scope.
- If unclear, put it into Question and Blocked Coverage.
- Timezone: `Asia/Saigon` (`UTC+07:00`).
- Encoding: UTF-8 (no mojibake).


## Sync My Open Tasks (Hasaki)

- sync my open tasks`r
- sync my open tasks --limit 20`r
- sync my open tasks --images`r
- sync my open tasks --dry-run`r

Behavior:
- Run only when user asks.
- Create/update raw snapshots, task specs, traceability, registry, kanban, and logs.
- Generate testcase only for clear/explicit requirements; unclear parts stay in Questions + Blocked Coverage.

