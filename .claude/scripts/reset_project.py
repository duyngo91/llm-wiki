"""DANGEROUS: Reset vault state — wipe project data + runtime cache + rebuildable docs.

KHÔNG chạy trừ khi user explicit ask "reset project" / "wipe vault". Mặc định dry-run;
yêu cầu `--apply` mới xóa thật.

Wiped targets:
- Runtime cache: `.smart-env/`, `.karate_cache/`, `.obsidian/cache/`, `.obsidian/workspace.json`
- Rebuildable aggregates: `log.md`, `KANBAN.md`, `index.md`
- Project data: `wiki/project_*/` (toàn bộ subdirs)
- (Optional via flag) raw_sources, templates

Preserved (CORE_KEEP_HINT):
- `.claude/rules/`, `.claude/skills/`, `.claude/commands/`, `.claude/manifests/`
- `CLAUDE.md`, `README.md`, `.mcp.json`

Use cases: bootstrap fresh project, recover từ corrupted state. KHÔNG dùng cho daily cleanup.

Usage:
    py .claude/scripts/reset_project.py                # dry-run, list targets
    py .claude/scripts/reset_project.py --apply        # actually delete
"""

import argparse
import shutil
from pathlib import Path


CORE_KEEP_HINT = [
    ".claude/rules",
    ".claude/skills",
    ".claude/commands",
    ".claude/manifests",
    "CLAUDE.md",
    "README.md",
    ".mcp.json",
]


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root)).replace('\\', '/')
    except Exception:
        return str(path)


def collect_targets(root: Path):
    targets = []

    # Runtime/cache
    targets.extend([
        root / ".smart-env",
        root / ".karate_cache",
        root / ".obsidian" / "cache",
        root / ".obsidian" / "workspace.json",
    ])

    # Rebuildable aggregate docs
    targets.extend([
        root / "log.md",
        root / "KANBAN.md",
        root / "index.md",
    ])

    # Project data folders
    for base in (root / "wiki",):
        if base.exists() and base.is_dir():
            for child in base.iterdir():
                if child.is_dir() and child.name.startswith("project_"):
                    targets.append(child)

    # Unique + existing only
    uniq = []
    seen = set()
    for t in targets:
        key = str(t.resolve()) if t.exists() else str(t)
        if key in seen:
            continue
        seen.add(key)
        if t.exists():
            uniq.append(t)

    return uniq


def delete_path(path: Path):
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(
        description="Reset wiki project data and runtime artifacts, keep core skills/rules/MCP guides."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Workspace root (default: current directory)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually delete targets. Without this flag, script runs in dry-run mode.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not (root / ".git").exists():
        raise SystemExit(f"Refusing to run: '{root}' does not look like a git repo root")

    targets = collect_targets(root)

    print("Reset Project Tool")
    print(f"Root: {root}")
    print(f"Mode: {'APPLY' if args.apply else 'DRY-RUN'}")
    print("Keep core (not touched):")
    for item in CORE_KEEP_HINT:
        print(f"  - {item}")

    if not targets:
        print("\nNo reset targets found.")
        return

    print("\nTargets:")
    for t in targets:
        kind = "dir " if t.is_dir() else "file"
        print(f"  - [{kind}] {rel(t, root)}")

    if not args.apply:
        print("\nDry-run only. Re-run with --apply to delete.")
        return

    deleted = []
    failed = []
    for t in targets:
        try:
            delete_path(t)
            deleted.append(t)
        except Exception as exc:
            failed.append((t, exc))

    print("\nResult:")
    print(f"  Deleted: {len(deleted)}")
    for t in deleted:
        print(f"  - {rel(t, root)}")

    if failed:
        print(f"  Failed: {len(failed)}")
        for t, exc in failed:
            print(f"  - {rel(t, root)} :: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
