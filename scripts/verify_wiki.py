import subprocess
import sys
from pathlib import Path


def main() -> int:
    vault_root = Path(__file__).resolve().parents[1]
    skill_script = vault_root / ".agents" / "skills" / "wiki-sync-helper" / "scripts" / "wiki_sync.py"
    return subprocess.call([sys.executable, str(skill_script), "verify"], cwd=str(vault_root))


if __name__ == "__main__":
    raise SystemExit(main())
