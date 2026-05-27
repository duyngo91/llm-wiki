import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


WIKI_TZ = ZoneInfo("Asia/Ho_Chi_Minh")


def now_iso() -> str:
    return datetime.now(WIKI_TZ).isoformat(timespec="seconds")


def parse_table_rows(lines: list[str], start_idx: int) -> tuple[list[list[str]], int]:
    rows: list[list[str]] = []
    i = start_idx
    while i < len(lines):
        line = lines[i].rstrip("\n")
        if not line.startswith("|"):
            break
        if set(line.replace("|", "").replace(":", "").replace("-", "").strip()) == set():
            i += 1
            continue
        cells = [cell.strip() for cell in line.strip().split("|")[1:-1]]
        rows.append(cells)
        i += 1
    return rows, i


def read_frontmatter(md_text: str) -> dict:
    if not md_text.startswith("---"):
        return {}
    end = md_text.find("\n---", 3)
    if end == -1:
        return {}
    block = md_text[3:end].splitlines()
    data = {}
    for line in block:
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip().strip('"')
    return data


def build_evidence_index(vault_root: Path, project: str) -> dict:
    features_dir = vault_root / "wiki" / project / "features"
    out = {
        "project_id": project,
        "generated_at": now_iso(),
        "records": [],
    }

    for feature_path in sorted(features_dir.glob("*.md")):
        text = feature_path.read_text(encoding="utf-8")
        frontmatter = read_frontmatter(text)
        feature_name = frontmatter.get("feature", feature_path.stem)
        source_version = frontmatter.get("source_version", "")
        partial_read = frontmatter.get("partial_read", "false")
        verification_status = frontmatter.get("verification_status", "Unknown")
        last_verified_at = frontmatter.get("last_verified_at", "")

        lines = text.splitlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith("| ID | Requirement |") or line.startswith("| ID | Requirement"):
                rows, i = parse_table_rows(lines, i + 2)
                for row in rows:
                    if len(row) < 6:
                        continue
                    rid, req, _, _, _, source = row[:6]
                    source_match = re.search(
                        r"([A-Za-z0-9_.-]+)#L?(\d+)(?:-L?(\d+))?",
                        source,
                    )
                    source_doc = source_match.group(1) if source_match else ""
                    start_line = int(source_match.group(2)) if source_match else None
                    end_line = int(source_match.group(3)) if source_match and source_match.group(3) else start_line
                    out["records"].append(
                        {
                            "claim_id": f"{feature_name}:{rid}",
                            "claim_type": "requirement",
                            "feature": feature_name,
                            "feature_file": str(feature_path.relative_to(vault_root)).replace("\\", "/"),
                            "requirement_id": rid,
                            "ac_id": "",
                            "question_id": "",
                            "testcase_ids": [],
                            "source_doc": source_doc,
                            "source_version": source_version,
                            "source_line_start": start_line,
                            "source_line_end": end_line,
                            "partial_read": partial_read.lower() == "true",
                            "verification_status": verification_status,
                            "last_verified_at": last_verified_at,
                        }
                    )
                continue
            if line.startswith("| Q-") or line.startswith("| Q"):
                # Question table rows are parsed as direct rows.
                cells = [cell.strip() for cell in line.split("|")[1:-1]]
                if len(cells) >= 5:
                    qid = cells[0]
                    out["records"].append(
                        {
                            "claim_id": f"{feature_name}:{qid}",
                            "claim_type": "question",
                            "feature": feature_name,
                            "feature_file": str(feature_path.relative_to(vault_root)).replace("\\", "/"),
                            "requirement_id": "",
                            "ac_id": "",
                            "question_id": qid,
                            "testcase_ids": [],
                            "source_doc": "",
                            "source_version": source_version,
                            "source_line_start": None,
                            "source_line_end": None,
                            "partial_read": partial_read.lower() == "true",
                            "verification_status": "Open" if "Open" in line else verification_status,
                            "last_verified_at": last_verified_at,
                        }
                    )
            i += 1

    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Build evidence index from feature specs")
    parser.add_argument("--project", default="project_hasaki")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    payload = build_evidence_index(root, args.project)
    out_path = root / "wiki" / args.project / "evidence_index.json"
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(out_path.relative_to(root)).replace("\\", "/"), "records": len(payload["records"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
