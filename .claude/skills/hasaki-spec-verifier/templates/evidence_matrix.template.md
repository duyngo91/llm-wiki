---
session: "YYYY-MM-DD"
batch: ""
generated_at: "YYYY-MM-DD HH:MM:SS+07:00"
---

# Evidence Matrix — {batch_name}

> Per-claim verification. Format: Raw evidence (path#line) | Wiki claim (path#line) | Status | Action.
>
> Verify rule: 100% claims mapped đến sections có flag critical (enum / state_transition / formula / business_rule / error_messages / validation_rule); 1/5 sampling cho non-critical.

---

## {spec_name}

| Raw Evidence | Wiki Claim | Status | Action |
|:-------------|:-----------|:-------|:-------|
| `<doc>#L<start>-L<end>` (mô tả ngắn từ raw) | `<spec_path>#L<line>` `<R-ID>` | `SUPPORTED` / `UNCLEAR` / `INFERRED` / `LOGIC_INFERRED` / `STRIPPED_CONDITION` / `NEGATION_FLIP` / `PHANTOM_EVIDENCE` / `POTENTIAL_OMISSION` / `MISSING_DETAIL` | Keep / Move to Q / Remove / Fix |
