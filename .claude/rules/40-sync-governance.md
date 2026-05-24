# Sync Governance

- Verify-first by default.
- Sync status transitions only after Gate confirmation.
- Any requirement or testcase update must propagate to related artifacts.
- Keep audit trail in `log.md` with UTC+07:00 timestamps.
- Final quality gate: `python .claude/scripts/wiki_sync.py verify`.
