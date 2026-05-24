---
description: "Check MCP configuration and connectivity for Claude Code and Codex."
allowed-tools: Read, Bash
---

# MCP Health Check

Run MCP diagnostics from vault root:

```powershell
python .claude/scripts/mcp_health_check.py
```

This check includes:
- MCP servers in `~/.claude.json`
- MCP servers in `~/.codex/config.toml`
- TCP reachability for HTTP MCP endpoints
- CLI health output from `claude mcp list`

