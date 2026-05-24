# Enterprise Controls

## Baseline
- Active project: `project_hasaki`
- Governance source: `WIKI_RULES.md` and `.claude/rules/*.md`
- Verify command: `python .claude/scripts/wiki_sync.py verify`

## Approval Expectations
- Security-sensitive or status-transition changes require explicit reviewer confirmation.
- Suppressions and overrides must include reason and narrow scope.

## Audit
- Keep `log.md` updated for sync and governance actions.
- Re-run verify after any structural, rule, or testcase migration.
