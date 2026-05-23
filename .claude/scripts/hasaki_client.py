"""
Hasaki Workplace API Client
Reusable class for all Hasaki internal API calls.
Auth: JWT token via Authorization: Bearer header.
"""

import json
import requests
from pathlib import Path

TOKEN_PATH = Path(__file__).resolve().parents[2] / "token.txt"
MEDIA_BASE = "https://hr-media.hasaki.vn/production/hr"


def load_token() -> str | None:
    if TOKEN_PATH.exists():
        return TOKEN_PATH.read_text(encoding="utf-8").strip() or None
    return None


class HasakiClient:
    BASE = "https://wshr.hasaki.vn/api"

    def __init__(self, token: str):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "Origin": "https://work.hasaki.vn",
            "Referer": "https://work.hasaki.vn/",
        })

    # ── Task ──────────────────────────────────────────────────────────────

    def get_task(self, task_id: int) -> dict:
        """Full task detail by numeric ID."""
        r = self.session.get(f"{self.BASE}/hr/projects/task-input/{task_id}")
        r.raise_for_status()
        return r.json()["data"]

    def find_task_by_code(self, code: str) -> dict:
        """Find task by display code (e.g. HSK-40187ZYO). Searches across all statuses."""
        for status in ("_00_01", "_02", None):
            params = {"limit": 500, "offset": 0, "option": "my-task"}
            if status:
                params["status"] = status
            r = self.session.get(f"{self.BASE}/hr/projects/mytasks-es", params=params)
            r.raise_for_status()
            tasks = r.json().get("data", [])
            match = next((t for t in tasks if t.get("code") == code), None)
            if match:
                return self.get_task(match["id"])
        raise ValueError(f"Task '{code}' not found.")

    def get_task_comments(self, task_id: int) -> list:
        """All comments on a task."""
        r = self.session.get(f"{self.BASE}/v2/task/comment", params={"obj_id": task_id})
        r.raise_for_status()
        return r.json().get("data", [])

    def get_subtasks(self, parent_id: int, project_id: int, milestone_id: int) -> list:
        """Subtasks of a task from project board."""
        r = self.session.get(
            f"{self.BASE}/hr/projects/{project_id}/tasks-es",
            params={"limit": 1000, "milestone_id": milestone_id},
        )
        r.raise_for_status()
        all_tasks = r.json().get("data", [])
        return [t for t in all_tasks if str(t.get("parent_id")) == str(parent_id)]

    # ── My Tasks ──────────────────────────────────────────────────────────

    def get_my_tasks(self, status: str = None, limit: int = 100) -> list:
        """List current user's tasks. status: _00_01=Todo/Processing, _02=Done"""
        params = {"limit": limit, "offset": 0, "option": "my-task"}
        if status:
            params["status"] = status
        r = self.session.get(f"{self.BASE}/hr/projects/mytasks-es", params=params)
        r.raise_for_status()
        return r.json().get("data", [])

    # ── Project ───────────────────────────────────────────────────────────

    def get_project(self, project_id: int) -> dict:
        r = self.session.get(f"{self.BASE}/hr/projects/{project_id}")
        r.raise_for_status()
        return r.json().get("data", {})

    def get_project_tasks(self, project_id: int, milestone_id: int = None, limit: int = 1000) -> list:
        params = {"limit": limit}
        if milestone_id:
            params["milestone_id"] = milestone_id
        r = self.session.get(f"{self.BASE}/hr/projects/{project_id}/tasks-es", params=params)
        r.raise_for_status()
        return r.json().get("data", [])

    # ── User / Profile ────────────────────────────────────────────────────

    def validate_token(self) -> bool:
        """Quick check: returns True if token is valid, False if expired/invalid."""
        try:
            r = self.session.get(f"{self.BASE}/setting/user/profile", params={"employee": 1})
            return r.status_code == 200
        except Exception:
            return False

    def get_profile(self) -> dict:
        r = self.session.get(f"{self.BASE}/setting/user/profile", params={"employee": 1})
        r.raise_for_status()
        return r.json().get("data", {})

    # ── Notifications ─────────────────────────────────────────────────────

    def get_notifications(self, limit: int = 20) -> list:
        r = self.session.get(f"{self.BASE}/v2/news/notifications", params={"limit": limit})
        r.raise_for_status()
        return r.json().get("data", [])

    # ── Media ─────────────────────────────────────────────────────────────

    def download_task_images(self, note_files: list[str], output_dir: str = ".") -> list[str]:
        """Download task attachment images. Media is public, no auth needed."""
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        saved = []
        for rel_path in note_files:
            url = f"{MEDIA_BASE}/{rel_path}"
            filename = Path(rel_path).name
            dest = out / filename
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
            dest.write_bytes(resp.content)
            saved.append(str(dest))
        return saved
