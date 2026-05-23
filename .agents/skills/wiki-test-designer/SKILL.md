---
name: wiki-test-designer
description: Use this skill when generating QA LLM Wiki test cases, creating or updating test suites in wiki/[project]/test_suites, mapping tests to Requirement IDs or Acceptance Criteria, applying ISTQB test design techniques, or labeling positive/negative and AI-inferred test cases for review.
metadata:
  short-description: Design traceable test suites
---

# Wiki Test Designer

Use for ISTQB Test Design: decide **how to test** an approved or draft feature spec.

## Required inputs

Read these before writing test cases:
- `../../../WIKI_RULES.md`
- `../../../templates/tpl_test_suite.md`
- `../../../wiki/[project]/features/[feature_name].md`
- `../../../wiki/[project]/operations/environments.md`
- `../../../wiki/[project]/operations/test_data.md`
- related files in `../../../wiki/[project]/bugs_knowledge/` when regression risk exists

## Workflow

1. Confirm target project, feature, source task/CR, and expected test suite path.
2. Extract Requirement IDs (`R1`, `R2`...) and Acceptance Criteria / BDD scenarios from the feature spec.
3. Design coverage using relevant techniques:
   - `Happy Path`
   - `Equivalence Partitioning`
   - `Boundary Value Analysis`
   - `Decision Table`
   - `State Transition`
   - `Error Guessing`
   - `Security`
   - `Regression`
4. Create or update `../../../wiki/[project]/test_suites/test_[feature_name].md`.
5. Update `../../../index.md`, `../../../KANBAN.md`, and `../../../log.md` according to `WIKI_RULES.md`.
6. From the vault root, run `python scripts/verify_wiki.py` when the suite update is complete.

## Test case row rules

Every test case row must include:
- `AC/Req Cover`: requirement and/or AC/BDD scenario covered, e.g. `AC-01 / R1`.
- `Loại case`: `Positive` or `Negative`. Regression/security/performance cases still need this label.
- `Kỹ thuật test`: the test design technique used.
- `Nguồn / Suy diễn`: `Explicit từ [source]` or `AI-Inferred từ [source/logic]`.
- `Status`: default `⏳` for new cases.

Do not finalize a test case without a source. If coverage is needed but the source is unclear, add a clarification question instead.

## Output

Summarize:
- test suite path and status;
- total cases by positive/negative;
- techniques used;
- Requirement/AC coverage;
- count of `AI-Inferred` cases and why they need review;
- validation result.
