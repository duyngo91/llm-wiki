---
description: "ISTQB Test Design — Thiết kế test cases/test suite traceable từ Feature Spec đã duyệt Gate 1. Delegate sang @hasaki-test-design (sonnet)."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Wiki Test Designer (router)

Delegate yêu cầu này sang sub-agent **`hasaki-test-design`** (model sonnet, phase test design của skill `hasaki-wiki`).

Input từ user: $ARGUMENTS

Worker sẽ đọc `.claude/skills/hasaki-wiki/references/phase_test_design.md` (single source: HOW to test) và thực thi: verify Gate 1 (`status: Done` + approval evidence), trích R/AC, loại R/AC còn question `Open` sang `Blocked Coverage`, thiết kế coverage ISTQB, viết `test_suites/`, chuẩn Test Case + Feature Group, chạy `wiki_sync.py verify`, dừng ở Gate 2. Tuân thủ `.claude/rules/30-testcase-policy.md` + `20-no-inference.md`.

Nếu user yêu cầu "không delegate" → main session tự đọc `phase_test_design.md` và thực thi.
