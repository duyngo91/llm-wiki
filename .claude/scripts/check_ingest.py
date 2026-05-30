"""Run the full ingest quality pipeline in one shot.

Order:
  1. wiki_sync.py verify          (format/governance lint)
  2. evidence_index.py            (claims index — R + AC + API + BR)
  3. verify_source_refs.py        (line accuracy vs raw)
  4. coverage_gap_estimator.py    (per-section expected vs actual claims)

Exit code = max severity across stages:
  0 = all clean
  2 = at least one stage reported critical findings

Outputs are individual JSONs under `wiki/<project>/` and `wiki/<project>/refiner/`.

Read by refiner Tầng L_structural.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path


SCRIPTS = [
    ("verify", "wiki_sync.py", ["verify"]),
    ("evidence_index", "evidence_index.py", ["--project", "{project}"]),
    ("verify_source_refs", "verify_source_refs.py", ["--project", "{project}"]),
    ("coverage_gap_estimator", "coverage_gap_estimator.py", ["--project", "{project}"]),
]


def run_stage(stage_name: str, script_name: str, args_template: list[str], project: str, scripts_dir: Path) -> dict:
    args = [arg.format(project=project) for arg in args_template]
    cmd = [sys.executable, str(scripts_dir / script_name), *args]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except OSError as exc:
        return {"stage": stage_name, "exit_code": 127, "error": str(exc), "stdout": "", "stderr": ""}

    stdout = result.stdout.strip()
    parsed = None
    if stdout:
        try:
            parsed = json.loads(stdout)
        except json.JSONDecodeError:
            parsed = None

    return {
        "stage": stage_name,
        "exit_code": result.returncode,
        "stdout": stdout,
        "stderr": result.stderr.strip(),
        "parsed": parsed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run full ingest quality pipeline")
    parser.add_argument("--project", default="project_hasaki")
    parser.add_argument("--fail-fast", action="store_true", help="Stop on first non-zero stage")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    scripts_dir = root / ".claude" / "scripts"

    results = []
    worst = 0
    for stage_name, script_name, arg_template in SCRIPTS:
        outcome = run_stage(stage_name, script_name, arg_template, args.project, scripts_dir)
        results.append(outcome)
        if outcome["exit_code"] > worst:
            worst = outcome["exit_code"]
        if args.fail_fast and outcome["exit_code"] != 0:
            break

    summary = {
        "project": args.project,
        "worst_exit_code": worst,
        "stages": [
            {
                "stage": r["stage"],
                "exit_code": r["exit_code"],
                "summary": (r["parsed"].get("summary") if r["parsed"] else None) or (r["parsed"].get("by_class") if r["parsed"] else None),
                "output": r["parsed"].get("output") if r["parsed"] else None,
            }
            for r in results
        ],
    }

    print(json.dumps(summary, ensure_ascii=False, indent=2))

    # Detail dump for any failed stage.
    for r in results:
        if r["exit_code"] != 0:
            print(f"\n--- stage {r['stage']} FAILED (exit={r['exit_code']}) ---", file=sys.stderr)
            if r["stderr"]:
                print(r["stderr"], file=sys.stderr)
            if r["stdout"] and not r["parsed"]:
                print(r["stdout"], file=sys.stderr)

    return worst


if __name__ == "__main__":
    raise SystemExit(main())
