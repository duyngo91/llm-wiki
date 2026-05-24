import json
import os
import re
import socket
import subprocess
import sys
import tomllib
from pathlib import Path
from urllib.parse import urlparse


def read_json(path: Path):
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def read_toml(path: Path):
    if not path.exists():
        return {}
    try:
        return tomllib.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def check_tcp(url: str, timeout: float = 2.0):
    parsed = urlparse(url)
    host = parsed.hostname
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    if not host:
        return False, "invalid host"
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True, f"tcp ok ({host}:{port})"
    except Exception as exc:
        return False, f"tcp fail ({host}:{port}) - {exc}"


def command_exists(command: str):
    if os.path.isabs(command):
        return Path(command).exists()
    for p in os.environ.get("PATH", "").split(os.pathsep):
        if not p:
            continue
        candidate = Path(p) / command
        if candidate.exists():
            return True
        if sys.platform.startswith("win"):
            for ext in (".exe", ".cmd", ".bat"):
                if (candidate.with_suffix(ext)).exists():
                    return True
    return False


def print_header(title: str):
    print("")
    print("=" * 10 + f" {title} " + "=" * 10)


def print_http_guidance(server_name: str, url: str):
    parsed = urlparse(url)
    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    print(f"  Guidance ({server_name} / HTTP):")
    print(f"  - Verify service is running at {url}")
    print(f"  - Quick check: `curl {url}` or `Invoke-WebRequest {url}`")
    print(f"  - Ensure host/port reachable: `{host}:{port}`")
    print("  - If auth is required, verify header token in MCP config")


def print_stdio_guidance(server_name: str, cmd: str, args):
    joined_args = " ".join(args) if args else ""
    print(f"  Guidance ({server_name} / STDIO):")
    print(f"  - Verify command exists in PATH: `{cmd}`")
    if joined_args:
        print(f"  - Test run manually: `{cmd} {joined_args}`")
    print("  - If command depends on runtime, verify runtime is installed")
    print("  - If using project-local path, verify file/folder still exists")


def main():
    home = Path.home()
    claude_json = home / ".claude.json"
    codex_toml = home / ".codex" / "config.toml"

    print("MCP Health Check")
    print(f"Home: {home}")
    print(f"Claude config: {claude_json}")
    print(f"Codex config: {codex_toml}")

    claude_cfg = read_json(claude_json)
    codex_cfg = read_toml(codex_toml)
    failures = []

    print_header("CLAUDE MCP SERVERS")
    claude_servers = claude_cfg.get("mcpServers", {})
    if not claude_servers:
        print("No servers found in .claude.json")
    for name, cfg in claude_servers.items():
        if cfg.get("type") == "http" or "url" in cfg:
            url = cfg.get("url", "")
            ok, msg = check_tcp(url)
            print(f"- {name}: HTTP {url} -> {'OK' if ok else 'FAIL'} | {msg}")
            if not ok:
                failures.append(("http", name, url, []))
        else:
            cmd = cfg.get("command", "")
            args = cfg.get("args", [])
            ok = command_exists(cmd)
            print(f"- {name}: STDIO {cmd} -> {'OK' if ok else 'FAIL'}")
            if not ok:
                failures.append(("stdio", name, cmd, args))

    print_header("CODEX MCP SERVERS")
    codex_servers = codex_cfg.get("mcp_servers", {})
    if not codex_servers:
        print("No servers found in .codex/config.toml")
    for name, cfg in codex_servers.items():
        if isinstance(cfg, dict) and "url" in cfg:
            url = cfg.get("url", "")
            ok, msg = check_tcp(url)
            print(f"- {name}: HTTP {url} -> {'OK' if ok else 'FAIL'} | {msg}")
            if not ok:
                failures.append(("http", name, url, []))
        elif isinstance(cfg, dict) and "command" in cfg:
            cmd = cfg.get("command", "")
            args = cfg.get("args", [])
            ok = command_exists(cmd)
            print(f"- {name}: STDIO {cmd} -> {'OK' if ok else 'FAIL'}")
            if not ok:
                failures.append(("stdio", name, cmd, args))

    print_header("CLAUDE BUILT-IN HEALTH")
    try:
        result = subprocess.run(
            ["claude", "mcp", "list"],
            capture_output=True,
            text=True,
            timeout=40,
            check=False,
        )
        print(f"Exit code: {result.returncode}")
        if result.stdout.strip():
            print(result.stdout.strip())
            for line in result.stdout.splitlines():
                lower_line = line.lower()
                if ":" in line and ("✗" in line or "failed" in lower_line):
                    name = line.split(":", 1)[0].strip()
                    failures.append(("claude-health", name, line.strip(), []))
        if result.stderr.strip():
            print(result.stderr.strip())
    except Exception as exc:
        print(f"Failed to run 'claude mcp list': {exc}")
        failures.append(("claude-cli", "claude", str(exc), []))

    if failures:
        print_header("MCP FAIL GUIDANCE")
        seen = set()
        for kind, name, target, args in failures:
            key = (kind, name, target)
            if key in seen:
                continue
            seen.add(key)
            if kind == "http":
                print_http_guidance(name, target)
            elif kind == "stdio":
                print_stdio_guidance(name, target, args)
            elif kind == "claude-health":
                print(f"  Guidance ({name} / Claude health):")
                print(f"  - Failure detail: {target}")
                print(f"  - Run: `claude mcp get {name}` for detail")
                print("  - Verify config scope (local/user/project) and restart Claude Code if needed")
            else:
                print(f"  Guidance ({name}):")
                print(f"  - {target}")
                print("  - Verify Claude CLI installation and PATH")
    else:
        print_header("MCP FAIL GUIDANCE")
        print("No MCP failure detected.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
