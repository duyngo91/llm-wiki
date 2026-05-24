"""
fix_encoding.py — Fix mojibake (UTF-8 bytes decoded as cp1252 then re-encoded as UTF-8).

Usage:
  py fix_encoding.py                   # dry-run: scan and report only
  py fix_encoding.py --apply           # fix in-place
  py fix_encoding.py FILE [FILE ...]   # specific files only
  py fix_encoding.py --apply FILE      # fix specific file
"""
import argparse
import sys
from pathlib import Path

SCAN_DIRS = ["wiki", "raw_sources", "templates"]
SCAN_ROOT_FILES = ["CLAUDE.md", "USER_COMMANDS.md", "WIKI_RULES.md", "KANBAN.md", "log.md", "index.md", "README.md"]
SCAN_EXT = {".md", ".json", ".yaml", ".yml", ".txt"}


def fix_char_to_bytes(c: str) -> bytes:
    cp = ord(c)
    if cp < 0x80:
        return bytes([cp])
    # cp1252 covers 0x80-0xFF (with some in 0x80-0x9F mapped to special chars)
    try:
        b = c.encode("cp1252")
        if len(b) == 1:
            return b
    except (UnicodeEncodeError, UnicodeDecodeError):
        pass
    # Fallback for C1 control chars (U+0080-U+009F) not in cp1252
    if 0x0080 <= cp <= 0x009F:
        return bytes([cp])
    # Higher unicode — keep as UTF-8 (already correct, not part of mojibake)
    return c.encode("utf-8")


def fix_mojibake(text: str) -> str:
    # Strip BOM if present
    if text.startswith("﻿"):
        text = text[1:]
    try:
        fixed_bytes = b"".join(fix_char_to_bytes(c) for c in text)
        return fixed_bytes.decode("utf-8")
    except (UnicodeDecodeError, UnicodeEncodeError):
        return text  # Can't fix — return original


def is_mojibake(text: str) -> bool:
    """Heuristic: detect cp1252-over-UTF-8 pattern."""
    if "﻿" in text:
        return True
    # Look for common mojibake sequences
    indicators = [
        "Ã ",  # à → Ã\xa0
        "Ã",  # Ã → Ã\x83 (double-encoded)
        "Æ°",  # ư → Ć°
        "Ã¡",  # á → Ã¡
        "Ã¹",  # ù → Ã¹
        "â",  # em-dash double-encoded
        "Ä",  # ă → Ä\x83
    ]
    count = sum(text.count(s) for s in indicators)
    return count >= 3


def process_file(path: Path, apply: bool) -> tuple[bool, str]:
    """Returns (changed, status_message)."""
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except Exception as e:
        return False, f"SKIP (read error: {e})"

    if not is_mojibake(text):
        return False, "OK"

    fixed = fix_mojibake(text)
    if fixed == text or fixed == text.lstrip("﻿"):
        return False, "UNCHANGED (fix had no effect)"

    if apply:
        path.write_text(fixed, encoding="utf-8")
        return True, "FIXED"
    else:
        return True, "NEEDS FIX (dry-run)"


def collect_files(root: Path, specific: list[Path]) -> list[Path]:
    if specific:
        return specific
    files = []
    for name in SCAN_ROOT_FILES:
        p = root / name
        if p.exists():
            files.append(p)
    for d in SCAN_DIRS:
        base = root / d
        if base.exists():
            for p in base.rglob("*"):
                if p.is_file() and p.suffix in SCAN_EXT:
                    files.append(p)
    return files


def main():
    parser = argparse.ArgumentParser(description="Fix mojibake encoding in wiki markdown files.")
    parser.add_argument("files", nargs="*", help="Specific files to fix (default: scan whole project)")
    parser.add_argument("--apply", action="store_true", help="Apply fixes in-place (default: dry-run)")
    parser.add_argument("--root", default=".", help="Project root (default: current directory)")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    specific = [Path(f).resolve() for f in args.files] if args.files else []
    files = collect_files(root, specific)

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"Fix Encoding Tool — mode: {mode}")
    print(f"Root: {root}")
    print(f"Files to scan: {len(files)}\n")

    fixed_count = 0
    needs_fix = 0
    for path in files:
        changed, status = process_file(path, args.apply)
        rel = str(path.relative_to(root)).replace("\\", "/")
        if status != "OK":
            tag = "[FIXED]" if (changed and args.apply) else ("[NEEDS FIX]" if changed else "[NO CHANGE]")
            print(f"  {tag} {rel}")
        if changed and args.apply:
            fixed_count += 1
        elif changed:
            needs_fix += 1

    print()
    if args.apply:
        print(f"Fixed: {fixed_count} file(s)")
    else:
        print(f"Needs fix: {needs_fix} file(s) — re-run with --apply to fix")
        if needs_fix:
            sys.exit(1)


if __name__ == "__main__":
    main()
