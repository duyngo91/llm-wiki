---
name: wiki-requirement-analyzer
description: Use this skill when ingesting QA LLM Wiki requirements from raw_sources, PDF/BRD/FSD/Jira/Slack/task notes, analyzing business rules, writing or updating feature specs in wiki/[project]/features, mapping Requirement IDs and Acceptance Criteria, or preparing clarification questions before test design.
metadata:
  short-description: Analyze requirements into feature specs
---

# Wiki Requirement Analyzer

Use for ISTQB Test Analysis: decide **what to test** before any test case design.

## Workflow

1. Read `../../../WIKI_RULES.md`, `../../../USER_COMMANDS.md`, and the relevant raw source under `../../../raw_sources/`.
2. Identify the target project. If the project is unclear, ask before writing files.
3. Read `../../../templates/tpl_requirement.md` and preserve its structure.
4. Create or update `../../../wiki/[project]/features/[feature_name].md`.
5. Write the feature spec with:
   - YAML: `tags: [qa/requirement]`, `status: Draft`, `project`, `feature`, source metadata.
   - Requirement IDs: `R1`, `R2`, `R3`...
   - User flows: happy, alternative, exception.
   - Business rules, validation rules, and error message map.
   - BDD acceptance criteria / scenarios that test design can later cover.
   - Clarification questions for unclear PO/Dev decisions.
   - Changelog, latest entry first.
6. Update `../../../index.md`, `../../../KANBAN.md`, and `../../../log.md` according to `WIKI_RULES.md`.

## Guardrails

- Do not write test cases in this skill. Hand off to `wiki-test-designer` only after the feature spec is reviewed.
- Do not invent business behavior as fact. Put uncertain logic in the clarification section.
- Keep raw sources read-only.
- Every generated requirement must trace to a source document, task, or clearly marked assumption.

## Output

Summarize:
- feature spec path and status;
- extracted Requirement IDs;
- acceptance criteria count;
- unresolved questions;
- files updated.
