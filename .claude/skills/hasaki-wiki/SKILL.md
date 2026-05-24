---
name: hasaki-wiki-orchestrator
description: Orchestrate Hasaki wiki workflows for requirement analysis, question lifecycle, testcase design, and sync governance.
---

# Hasaki Wiki Orchestrator

## Purpose
Coordinate the QA wiki flow for `project_hasaki` with strict no-inference policy.

## Use This Skill When
- Ingesting requirement/task sources into feature specs.
- Designing or updating test suites from approved specs.
- Running lint/sync and governance verification.
- Updating traceability, Kanban counts, and linked artifacts.

## Workflow Routing
1. Requirement analysis: use `/wiki-requirement-analyzer`.
2. Test design: use `/wiki-test-designer`.
3. Sync and governance checks: use `/wiki-sync-helper`.
4. Task ingestion from Hasaki workplace: use `/get-hasaki-task` and `/import-hasaki-task`.

## Core Guardrails
- Use `Asia/Saigon` (`UTC+07:00`) timestamps for wiki updates.
- Do not infer requirement/API/testcase details from unclear sources.
- If unclear, write to Question sections and Blocked Coverage instead of active test cases.
- Active test cases must map to explicit requirement/AC.
- Prefer machine-readable traceability updates when test scope changes.

## Knowledge Scope
- Allowed: `wiki/`, `raw_sources/`, `templates/`, `.claude/commands/`, `.claude/scripts/`, control docs.
- Excluded by default: `.obsidian/`, `.smart-env/`, `.karate_cache/`, plugin/cache/db/runtime artifacts.

## Done Criteria
- `python .claude/scripts/wiki_sync.py verify` passes without guardrail errors.
- Linked docs are updated together: feature/testsuite/testplan/Kanban/log/traceability.
