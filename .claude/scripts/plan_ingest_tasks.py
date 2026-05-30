"""Generate ingest task plan from {file}_index.json files.

Reads raw_sources/<project>/requirements/*_index.json and emits
wiki/<project>/refiner/ingest_plan.json — a structured plan that
the AI (/wiki-requirement-analyzer) consumes to create TaskCreate
items per section, grouped by parent_id hierarchy.

Status of each section task is derived from `coverage_status` and
`read_log` in the current index, so re-running this script after
partial progress reflects the actual state — no separate state file
to keep in sync.

Output schema v1.0:

{
  "schema_version": "1.0",
  "generated_at": "...",
  "project": "...",
  "max_group_size": 6,
  "summary": {"total_docs", "total_sections", "total_groups",
              "pending", "in_progress", "done", "skipped"},
  "docs": [
    {
      "doc_short": "07062",
      "source_file": "07062_..._converted.md",
      "source_version": "2.17",
      "total_sections": 42,
      "group_count": 9,
      "counts": {"pending": 30, ...},
      "groups": [
        {
          "group_id": "G-01",
          "label": "Tổng quan",
          "anchor_section_id": "S-00",
          "rationale": "top-level ancestor",
          "section_count": 3,
          "tasks": [
            {
              "task_id": "T-07062-S00",
              "section_id": "S-00",
              "title": "[07062 G-01] S-00 — Tổng quan [L1-L80]",
              "source_ref": "...",
              "topic_types": [],
              "flags_active": ["has_enum"],
              "line_count": 80,
              "depth": 1,
              "current_status": "pending",
              "done_criteria_short": "..."
            }
          ]
        }
      ]
    }
  ]
}
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path


TZ_VN = timezone(timedelta(hours=7))
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MAX_GROUP = 6


def derive_doc_short(source_file: str) -> str:
    """07062_Receiving_PO_Docs_ver2.17_converted.md -> 07062."""
    stem = source_file.replace("_converted.md", "")
    parts = stem.split("_")
    return parts[0] if parts else stem


def derive_status(section: dict) -> str:
    cs = section.get("coverage_status", "unmapped")
    rl = section.get("read_log")
    if cs == "deleted":
        return "skipped"
    if cs in ("full", "stub") and rl:
        return "done"
    if cs == "partial" or rl is not None:
        return "in_progress"
    return "pending"


def top_ancestor(section_id: str, by_id: dict) -> str:
    s = by_id.get(section_id)
    if not s:
        return section_id
    while s.get("parent_id"):
        parent = by_id.get(s["parent_id"])
        if not parent:
            break
        s = parent
    return s["id"]


def cluster_sections(sections: list[dict], max_group: int) -> list[dict]:
    if not sections:
        return []
    by_id = {s["id"]: s for s in sections}

    chains: dict[str, list[dict]] = defaultdict(list)
    order: list[str] = []
    for s in sections:
        anchor = top_ancestor(s["id"], by_id)
        if anchor not in chains:
            order.append(anchor)
        chains[anchor].append(s)

    groups: list[dict] = []
    counter = 1
    for anchor in order:
        members = chains[anchor]
        anchor_section = by_id.get(anchor) or members[0]
        anchor_title = (anchor_section.get("title") or "").strip()
        rationale = (
            "top-level ancestor"
            if any(s.get("parent_id") for s in members)
            else "standalone parent"
        )

        for chunk_idx in range(0, len(members), max_group):
            chunk = members[chunk_idx : chunk_idx + max_group]
            suffix = (
                ""
                if len(members) <= max_group
                else f" (part {chunk_idx // max_group + 1})"
            )
            groups.append(
                {
                    "group_id": f"G-{counter:02d}",
                    "label": (anchor_title + suffix)[:80],
                    "anchor_section_id": anchor,
                    "rationale": rationale,
                    "section_count": len(chunk),
                    "members": chunk,
                }
            )
            counter += 1
    return groups


DONE_CRITERIA_SHORT = (
    "read_log filled + coverage_status in {full|partial|stub} + "
    "check_ingest passes (no SUSPECT_UNREAD / UNDERREPORTED_COVERAGE)"
)


def build_plan_for_doc(index_path: Path, max_group: int) -> dict:
    data = json.loads(index_path.read_text(encoding="utf-8"))
    sections = data.get("sections", [])
    source_file = data.get("source_file", index_path.stem)
    doc_short = derive_doc_short(source_file)

    groups_raw = cluster_sections(sections, max_group)

    doc_groups: list[dict] = []
    counts = {"pending": 0, "in_progress": 0, "done": 0, "skipped": 0}
    for g in groups_raw:
        tasks = []
        for s in g["members"]:
            status = derive_status(s)
            counts[status] = counts.get(status, 0) + 1
            flags_active = sorted(
                k for k, v in (s.get("flags") or {}).items() if v
            )
            line_count = max(0, s.get("end_line", 0) - s.get("start_line", 0) + 1)
            short_title = (s.get("title") or "").strip()[:60]
            tasks.append(
                {
                    "task_id": f"T-{doc_short}-{s['id']}",
                    "section_id": s["id"],
                    "title": (
                        f"[{doc_short} {g['group_id']}] {s['id']} — "
                        f"{short_title} "
                        f"[L{s['start_line'] + 1}-L{s['end_line'] + 1}]"
                    ),
                    "source_ref": s.get("source_ref"),
                    "topic_types": s.get("topic_types") or [],
                    "flags_active": flags_active,
                    "line_count": line_count,
                    "depth": s.get("depth"),
                    "current_status": status,
                    "done_criteria_short": DONE_CRITERIA_SHORT,
                }
            )

        doc_groups.append(
            {
                "group_id": g["group_id"],
                "label": g["label"],
                "anchor_section_id": g["anchor_section_id"],
                "rationale": g["rationale"],
                "section_count": g["section_count"],
                "tasks": tasks,
            }
        )

    return {
        "doc_short": doc_short,
        "source_file": source_file,
        "source_version": data.get("source_version"),
        "total_sections": len(sections),
        "group_count": len(doc_groups),
        "counts": counts,
        "groups": doc_groups,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", default="project_hasaki")
    ap.add_argument(
        "--max-group",
        type=int,
        default=DEFAULT_MAX_GROUP,
        help="Max sections per group; larger groups split into parts",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output path. Default: wiki/<project>/refiner/ingest_plan.json",
    )
    args = ap.parse_args()

    raw_dir = PROJECT_ROOT / "raw_sources" / args.project / "requirements"
    if not raw_dir.exists():
        print(f"Error: requirements dir not found: {raw_dir}")
        return 1

    index_files = sorted(raw_dir.glob("*_index.json"))
    if not index_files:
        print(f"No *_index.json files in {raw_dir}")
        return 0

    docs = []
    total = {"pending": 0, "in_progress": 0, "done": 0, "skipped": 0}
    for index_path in index_files:
        doc_plan = build_plan_for_doc(index_path, args.max_group)
        docs.append(doc_plan)
        for k, v in doc_plan["counts"].items():
            total[k] = total.get(k, 0) + v

    plan = {
        "schema_version": "1.0",
        "generated_at": datetime.now(TZ_VN).strftime("%Y-%m-%d %H:%M:%S"),
        "project": args.project,
        "max_group_size": args.max_group,
        "summary": {
            "total_docs": len(docs),
            "total_sections": sum(d["total_sections"] for d in docs),
            "total_groups": sum(d["group_count"] for d in docs),
            **total,
        },
        "docs": docs,
    }

    out_path = args.out or (
        PROJECT_ROOT / "wiki" / args.project / "refiner" / "ingest_plan.json"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    rel = out_path.relative_to(PROJECT_ROOT)
    print(f"OK  {rel}")
    print(f"    Docs       : {plan['summary']['total_docs']}")
    print(f"    Sections   : {plan['summary']['total_sections']}")
    print(f"    Groups     : {plan['summary']['total_groups']}")
    print(
        "    Status     : "
        f"pending={total['pending']} "
        f"in_progress={total['in_progress']} "
        f"done={total['done']} "
        f"skipped={total['skipped']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
