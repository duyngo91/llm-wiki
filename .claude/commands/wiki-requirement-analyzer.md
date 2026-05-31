---
description: "ISTQB Test Analysis — Phân tích requirement từ raw_sources và tạo/cập nhật Feature Spec (+ API Spec nếu có API explicit). Delegate sang @hasaki-ingest (opus)."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Wiki Requirement Analyzer (router)

Delegate yêu cầu này sang sub-agent **`hasaki-ingest`** (model opus, phase ingest của skill `hasaki-wiki`).

Input từ user: $ARGUMENTS

Worker sẽ đọc `.claude/skills/hasaki-wiki/references/phase_ingest.md` (single source of truth cho ISTQB Test Analysis: WHAT to test) và thực thi đầy đủ Workflow 2.0/2.1/2.1b/2.2 + chuẩn Feature/API Spec + Stub lifecycle ở đó. Tuân thủ `.claude/rules/` (no-inference, encoding) + `references/shared.md`.

Nếu user yêu cầu rõ "không delegate / tự làm" → main session tự đọc `phase_ingest.md` và thực thi.
