"""CLI entry point cho wiki maintenance — dispatcher mỏng, logic ở `wiki_sync_core.py`.

Subcommands:

| Command | Mục đích | Output |
|:--------|:---------|:-------|
| `sync` | Re-link Kanban ↔ specs ↔ test suites, recompute coverage counts, refresh changelog | KANBAN.md, daily index |
| `daily-sync` | Append daily activity note (cần `--project` + `--date`) | `wiki/<p>/daily-notes/YYYY-MM-DD.md` |
| `verify` | Lint format, broken wikilinks, encoding (BOM/mojibake), frontmatter compliance. Exit 2 on fail. | stdout report |
| `repair` | Auto-fix common verify findings | stdout summary |
| `sync-my-open-tasks` | Delegate sang `sync_my_open_tasks.py` — fetch Hasaki open tasks, snapshot raw, upsert task_spec, update Kanban | raw_sources/.../tasks/, task_specs/, KANBAN.md, traceability.json, project_registry.json |

Core logic trong `wiki_sync_core.py:WikiSyncCore`. Subcommand `sync-my-open-tasks`
dùng lazy import vì `sync_my_open_tasks.py` cần `hasaki_client.py` (mạng), tách
để verify/repair chạy được offline.

Usage:
    py .claude/scripts/wiki_sync.py verify
    py .claude/scripts/wiki_sync.py daily-sync --project project_hasaki --date 2026-05-30
    py .claude/scripts/wiki_sync.py sync-my-open-tasks --limit 20 [--dry-run]
"""

import sys
from pathlib import Path


def vault_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_core():
    root = vault_root()
    sys.path.insert(0, str(root / ".claude" / "scripts"))
    from wiki_sync_core import WikiSyncCore

    return WikiSyncCore(root)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python .claude/scripts/wiki_sync.py [sync | daily-sync | verify | repair | sync-my-open-tasks]")
        print("For daily-sync: python .claude/scripts/wiki_sync.py daily-sync --project <project_name> --date <YYYY-MM-DD>")
        print("For open tasks: python .claude/scripts/wiki_sync.py sync-my-open-tasks [--limit N] [--images] [--dry-run]")
        return 1

    core = load_core()
    command = sys.argv[1]
    if command == "sync":
        return core.run_sync()
    if command == "verify":
        return core.run_verify()
    if command == "repair":
        return core.run_repair()
    if command == "daily-sync":
        project = None
        date_str = None
        for index in range(2, len(sys.argv)):
            if sys.argv[index] == "--project" and index + 1 < len(sys.argv):
                project = sys.argv[index + 1]
            elif sys.argv[index] == "--date" and index + 1 < len(sys.argv):
                date_str = sys.argv[index + 1]
        if not project or not date_str:
            print("[ERROR] Missing arguments for daily-sync. Please specify --project and --date.")
            return 1
        return core.run_daily_sync(project, date_str)
    if command == "sync-my-open-tasks":
        from sync_my_open_tasks import main as sync_open_tasks_main

        passthrough = [sys.argv[0], *sys.argv[2:]]
        old_argv = sys.argv
        try:
            sys.argv = passthrough
            return sync_open_tasks_main()
        finally:
            sys.argv = old_argv

    print(f"[ERROR] Unknown command: {command}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
