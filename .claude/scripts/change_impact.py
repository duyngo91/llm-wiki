import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


WIKI_TZ = ZoneInfo("Asia/Ho_Chi_Minh")


def now_iso() -> str:
    return datetime.now(WIKI_TZ).isoformat(timespec="seconds")


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


def find_latest_source_versions(raw_index_dir: Path) -> dict:
    versions: dict[str, str] = {}
    for idx_file in sorted(raw_index_dir.glob("*_index.json")):
        try:
            payload = json.loads(idx_file.read_text(encoding="utf-8"))
        except Exception:
            continue
        doc_name = idx_file.stem.replace("_index", "")
        version = payload.get("version") or payload.get("source_version") or ""
        if not version:
            # fallback by filename convention (e.g., *_ver2.17)
            m = re.search(r"_ver([0-9.]+)", doc_name, flags=re.IGNORECASE)
            version = f"ver{m.group(1)}" if m else ""
        versions[doc_name] = version
    return versions


def build_change_impact(vault_root: Path, project: str) -> dict:
    features_dir = vault_root / "wiki" / project / "features"
    raw_index_dir = vault_root / "raw_sources" / project / "requirements"
    source_versions = find_latest_source_versions(raw_index_dir)

    report = {
        "project_id": project,
        "generated_at": now_iso(),
        "summary": {
            "changed_features": 0,
            "stale_features": 0,
            "partial_read_features": 0,
            "open_question_features": 0,
        },
        "items": [],
    }

    for feature_path in sorted(features_dir.glob("*.md")):
        text = feature_path.read_text(encoding="utf-8")
        fm = read_frontmatter(text)
        feature_name = fm.get("feature", feature_path.stem)
        feature_source_version = fm.get("source_version", "")
        partial_read = fm.get("partial_read", "").lower() == "true"
        has_open_question = " | Open |" in text or "| Open |" in text

        # infer raw source doc from source_version in frontmatter text, ex: "07062 ver2.17"
        doc_match = re.search(r"(\d{5}_[A-Za-z0-9_]+)", text)
        doc_key = doc_match.group(1) if doc_match else ""
        latest = source_versions.get(doc_key, "")
        stale = bool(latest and feature_source_version and latest not in feature_source_version)
        changed = stale

        if partial_read:
            report["summary"]["partial_read_features"] += 1
        if has_open_question:
            report["summary"]["open_question_features"] += 1
        if stale:
            report["summary"]["stale_features"] += 1
        if changed:
            report["summary"]["changed_features"] += 1

        report["items"].append(
            {
                "feature": feature_name,
                "feature_file": str(feature_path.relative_to(vault_root)).replace("\\", "/"),
                "source_doc": doc_key,
                "feature_source_version": feature_source_version,
                "latest_source_version": latest,
                "status": "Stale" if stale else "Aligned",
                "partial_read": partial_read,
                "has_open_question": has_open_question,
                "recommended_action": "Re-verify + update Impact/Regression + keep testcase blocked if question open"
                if stale or has_open_question or partial_read
                else "No immediate action",
            }
        )

    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Build change impact report for project")
    parser.add_argument("--project", default="project_hasaki")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    payload = build_change_impact(root, args.project)
    out_path = root / "wiki" / args.project / "change_impact_report.json"
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(out_path.relative_to(root)).replace("\\", "/"), "items": len(payload["items"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
