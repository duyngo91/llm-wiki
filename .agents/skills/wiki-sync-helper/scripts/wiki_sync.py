import subprocess
import sys
from pathlib import Path


def vault_root() -> Path:
    return Path(__file__).resolve().parents[4]


def main() -> int:
    root = vault_root()
    manager = root / "scripts" / "wiki_manager.py"
    verifier = root / "scripts" / "verify_wiki.py"

    if len(sys.argv) < 2:
        print("Usage: python .agents/skills/wiki-sync-helper/scripts/wiki_sync.py [sync | daily-sync | verify] ...")
        return 1

    command = sys.argv[1]
    if command == "verify":
        cmd = [sys.executable, str(verifier)]
    else:
        cmd = [sys.executable, str(manager), *sys.argv[1:]]

    return subprocess.call(cmd, cwd=str(root))


if __name__ == "__main__":
    raise SystemExit(main())
