"""
CLI: Get Hasaki Workplace task details.
Usage:
  python hasaki_task.py HSK-40187ZYO
  python hasaki_task.py 12032444 --images --output ./imgs
  python hasaki_task.py HSK-40187ZYO --json
"""

import sys
import io
import json
import argparse
import requests
from pathlib import Path
from urllib.parse import urlparse, parse_qs

# Force UTF-8 output on Windows
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent))
from hasaki_client import HasakiClient, load_token, TOKEN_PATH


def format_task(task: dict, subtasks: list, comments: list) -> str:
    lines = []

    lines.append(f"# {task['code']} — {task['name']}")
    lines.append("")

    status_map = {0: "Todo", 1: "Processing", 2: "Done"}
    priority_map = {0: "Normal", 1: "High", 2: "Urgent"}
    section = (task.get("section") or {}).get("name", "")
    lines.append(f"**Status:** {status_map.get(task.get('status', 0), task.get('status'))} ({section})")
    lines.append(f"**Priority:** {priority_map.get(task.get('piority', 0), 'Normal')}")
    lines.append(f"**Project:** {(task.get('project') or {}).get('name', '')} (ID: {task.get('prid')})")
    lines.append(f"**Milestone:** {(task.get('milestone') or {}).get('name', '')}")
    lines.append(f"**Created:** {task.get('created_at')}  |  **Updated:** {task.get('updated_at')}")
    lines.append(f"**Deadline:** {task.get('date_end') or '—'}")
    lines.append(f"**Planned hours:** {task.get('planned_hours', 0)}  |  **% done:** {task.get('percent', 0)}%")
    lines.append("")

    assigner = task.get("created_by_user") or {}
    lines.append(f"**Người giao:** {assigner.get('staff_name', '')} <{assigner.get('staff_email', '')}>")

    assignees = task.get("assign_to_user") or []
    for p in assignees:
        lines.append(f"**Người thực hiện:** {p.get('staff_name')} <{p.get('staff_email')}> — {p.get('staff_title', '')}")
    lines.append("")

    note = (task.get("note") or "").strip()
    if note:
        lines.append("## Nội dung")
        lines.append("")
        lines.append(note)
        lines.append("")

    note_files = task.get("note_files") or []
    if note_files:
        lines.append("## Hình ảnh đính kèm")
        for f in note_files:
            lines.append(f"- https://hr-media.hasaki.vn/production/hr/{f}")
        lines.append("")

    if subtasks:
        lines.append("## Subtasks")
        lines.append("")
        status_map2 = {0: "Todo", 1: "Processing", 2: "Done"}
        for st in subtasks:
            assignee_names = ", ".join(
                p.get("info", {}).get("staff_name", "") for p in (st.get("staff") or [])
            )
            lines.append(
                f"- [{st.get('code')}] **{st.get('name')}** | "
                f"Status: {status_map2.get(st.get('status', 0))} | "
                f"Assignee: {assignee_names} | "
                f"Planned: {st.get('planned_hours', 0)}h"
            )
        lines.append("")

    if comments:
        lines.append("## Comments")
        lines.append("")
        for c in comments:
            user = (c.get("created_by_user") or {}).get("staff_name", "?")
            lines.append(f"**{user}** ({c.get('created_at')}):")
            lines.append((c.get("content") or "").strip())
            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Get Hasaki task details")
    parser.add_argument("task", nargs="?", help="Task code (HSK-XXXXX) or numeric ID")
    parser.add_argument("--token", help="JWT token (overrides token.txt)")
    parser.add_argument("--images", action="store_true", help="Download attachment images")
    parser.add_argument("--output", default=".", help="Output directory for images (default: .)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of formatted text")
    args = parser.parse_args()

    token = args.token or load_token()
    if not token:
        print("ERROR: Không tìm thấy token.")
        print(f"  Vui lòng paste token vào file: {TOKEN_PATH}")
        print("  Cách lấy token: Đăng nhập work.hasaki.vn → DevTools (F12)")
        print("  → Application → Cookies → work.hasaki.vn → copy giá trị 'wshr-token'")
        sys.exit(1)

    client = HasakiClient(token)

    if not client.validate_token():
        print("TOKEN HẾT HẠN hoặc không hợp lệ.")
        print(f"  1. Đăng nhập lại work.hasaki.vn")
        print(f"  2. DevTools (F12) → Application → Cookies → work.hasaki.vn → wshr-token")
        print(f"  3. Paste token mới vào: {TOKEN_PATH}")
        sys.exit(1)

    task_input = args.task
    task_id_from_url = None
    if task_input.startswith("http"):
        qs = parse_qs(urlparse(task_input).query)
        tid = qs.get("task_id", [None])[0]
        if not tid:
            print("ERROR: URL không chứa tham số task_id.")
            sys.exit(1)
        task_id_from_url = int(tid)

    try:
        if task_id_from_url is not None:
            task = client.get_task(task_id_from_url)
        elif task_input.isdigit():
            task = client.get_task(int(task_input))
        else:
            task = client.find_task_by_code(task_input)
    except requests.HTTPError as e:
        code = e.response.status_code
        body = e.response.text.lower()
        is_auth_error = code in (401, 403) or (
            code == 500 and any(k in body for k in ("unauthenticated", "token", "unauthorized", "invalid"))
        )
        if is_auth_error:
            print("TOKEN HẾT HẠN hoặc không hợp lệ.")
            print(f"  1. Đăng nhập lại work.hasaki.vn")
            print(f"  2. DevTools (F12) → Application → Cookies → work.hasaki.vn → wshr-token")
            print(f"  3. Paste token mới vào: {TOKEN_PATH}")
        else:
            print(f"ERROR {code}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    task_id = task["id"]
    project_id = task.get("prid")
    milestone_id = (task.get("milestone") or {}).get("id")

    comments = client.get_task_comments(task_id)
    subtasks = []
    if project_id and milestone_id:
        subtasks = client.get_subtasks(task_id, project_id, milestone_id)

    downloaded = []
    if args.images and task.get("note_files"):
        downloaded = client.download_task_images(task["note_files"], args.output)
        print(f"Downloaded {len(downloaded)} image(s) to {args.output}", file=sys.stderr)

    if args.json:
        print(json.dumps({
            "task": task,
            "subtasks": subtasks,
            "comments": comments,
            "downloaded_images": downloaded,
        }, ensure_ascii=False, indent=2))
    else:
        print(format_task(task, subtasks, comments))
        if downloaded:
            print(f"\n**Downloaded images:** {', '.join(downloaded)}")


if __name__ == "__main__":
    main()
