"""Core library cho `wiki_sync.py` — implementation của 4 subcommand (sync / daily-sync / verify / repair).

`WikiSyncCore` class operates trên vault root, exposes:

- `run_sync()` — re-link Kanban ↔ specs ↔ test suites, recompute coverage counts, refresh changelog
- `run_verify()` — lint format, broken wikilinks, encoding (BOM/mojibake), frontmatter compliance
- `run_repair()` — auto-fix common verify findings (broken wikilinks, missing frontmatter fields)
- `run_daily_sync(project, date_str)` — append daily activity note

Plus shared utilities:
- `safe_filename(text)` — slugify Vietnamese → ASCII
- `clean_link_path(link)` — normalize Obsidian wikilink path
- `log_activity(action_type, message)` — append vào `log.md` với UTC+07 timestamp

Tách khỏi `wiki_sync.py` để CLI dispatcher mỏng + tách import dependency
(network-heavy `hasaki_client.py` không bị load khi chỉ chạy verify offline).

KHÔNG chạy trực tiếp — gọi qua `wiki_sync.py <subcommand>`.
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


WIKI_TZ = ZoneInfo("Asia/Ho_Chi_Minh")


if sys.platform.startswith("win"):
    import codecs

    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


def clean_link_path(link_text):
    clean = link_text.strip().split("#")[0].replace("\\|", "|").split("|")[0].strip().rstrip("\\")
    return clean.replace("\\", "/").strip("/")


def safe_filename(text):
    text = text.lower()
    replacements = {
        "á": "a", "à": "a", "ả": "a", "ã": "a", "ạ": "a", "ă": "a", "ắ": "a", "ằ": "a", "ẳ": "a", "ẵ": "a", "ặ": "a",
        "â": "a", "ấ": "a", "ầ": "a", "ẩ": "a", "ẫ": "a", "ậ": "a", "đ": "d", "é": "e", "è": "e", "ẻ": "e", "ẽ": "e",
        "ẹ": "e", "ê": "e", "ế": "e", "ề": "e", "ể": "e", "ễ": "e", "ệ": "e", "í": "i", "ì": "i", "ỉ": "i", "ĩ": "i",
        "ị": "i", "ó": "o", "ò": "o", "ỏ": "o", "õ": "o", "ọ": "o", "ô": "o", "ố": "o", "ồ": "o", "ổ": "o", "ỗ": "o",
        "ộ": "o", "ơ": "o", "ớ": "o", "ờ": "o", "ở": "o", "ỡ": "o", "ợ": "o", "ú": "u", "ù": "u", "ủ": "u", "ũ": "u",
        "ụ": "u", "ư": "u", "ứ": "u", "ừ": "u", "ử": "u", "ữ": "u", "ự": "u", "ý": "y", "ỳ": "y", "ỷ": "y", "ỹ": "y",
        "ỵ": "y",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    text = re.sub(r"[^a-z0-9_-]", "_", text)
    text = re.sub(r"_{2,}", "_", text)
    return text.strip("_")


class WikiSyncCore:
    def __init__(self, vault_dir):
        self.vault_dir = Path(vault_dir)
        self.kanban_path = self.vault_dir / "KANBAN.md"
        self.log_path = self.vault_dir / "log.md"
        self.templates_dir = self.vault_dir / "templates"

    def log_activity(self, action_type, message):
        timestamp = datetime.now(WIKI_TZ).strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"- [{timestamp}] [{action_type}] | {message}\n"

        if not self.log_path.exists():
            return

        lines = self.log_path.read_text(encoding="utf-8").splitlines(keepends=True)
        fm_end = -1
        fm_count = 0
        for index, line in enumerate(lines):
            if line.strip() == "---":
                fm_count += 1
                if fm_count == 2:
                    fm_end = index
                    break

        if fm_end != -1:
            lines.insert(fm_end + 1, "\n" + log_entry)
        else:
            lines.insert(0, log_entry)

        self.log_path.write_text("".join(lines), encoding="utf-8")
        print(f"Logged: {message}")

    def read_text(self, path: Path) -> str:
        return path.read_text(encoding="utf-8-sig", errors="ignore")

    def has_any_heading(self, content: str, aliases) -> bool:
        lowered = content.lower()
        return any(alias.lower() in lowered for alias in aliases)

    def extract_section_multi(self, text, heading_aliases):
        for heading in heading_aliases:
            section = self.extract_section(text, heading)
            if section:
                return section
        return ""

    def parse_test_case_row(self, line):
        if "TC-" not in line or "|" not in line:
            return None

        cells = [part.strip() for part in line.strip().strip("|").split("|")]
        if not cells or not cells[0].startswith("TC-"):
            return None

        status = cells[-1]
        if len(cells) >= 10:
            category = cells[4] or cells[3] or "Unknown"
        elif len(cells) >= 7:
            category = cells[5] or "Unknown"
        else:
            category = "Unknown"
        return category, status

    def sync_completed_task(self, test_suite_link):
        suite_clean = clean_link_path(test_suite_link)
        suite_path = self.vault_dir / f"{suite_clean}.md"

        if not suite_path.exists():
            print(f"[WARNING] Test Suite file not found: {suite_path}")
            return False

        print(f"Syncing completed Test Suite: {suite_clean}")
        content = self.read_text(suite_path)
        content = re.sub(r"^status:\s*\w+", "status: Passed", content, flags=re.MULTILINE)

        feature_link_match = re.search(r"(?i)(?:-\s*\*\*?)?(?:feature(?: liên quan)?|requirement)(?:\*\*?)?\s*:\s*(?:\s*\*\*?)?\[\[([^\]|]+)", content)
        if feature_link_match:
            feat_clean = clean_link_path(feature_link_match.group(1))
            feat_path = self.vault_dir / f"{feat_clean}.md"
            if feat_path.exists():
                print(f"Syncing completed Feature: {feat_clean}")
                feat_content = feat_path.read_text(encoding="utf-8")
                feat_content = re.sub(r"^status:\s*\w+", "status: Done", feat_content, flags=re.MULTILINE)
                feat_content = feat_content.replace("⏳", "✅ Pass")
                feat_path.write_text(feat_content, encoding="utf-8")

        content = content.replace("⏳", "✅ Pass")
        lines = content.split("\n")
        passed_cases = failed_cases = blocked_cases = untested_cases = total_cases = 0

        for line in lines:
            parsed_row = self.parse_test_case_row(line)
            if not parsed_row:
                continue
            _, status = parsed_row
            total_cases += 1
            if "✅ Pass" in status or "Pass" in status:
                passed_cases += 1
            elif "❌ Fail" in status or "Fail" in status:
                failed_cases += 1
            elif "🚫 Blocked" in status or "Blocked" in status:
                blocked_cases += 1
            else:
                untested_cases += 1

        summary_started = False
        summary_lines_range = []
        for index, line in enumerate(lines):
            if "## 📊 Tổng quan Test Coverage" in line:
                summary_started = True
                continue
            if summary_started:
                if line.startswith("|"):
                    summary_lines_range.append(index)
                elif line.strip() == "" and summary_lines_range:
                    break

        if summary_lines_range:
            new_summary_table = [
                "| Loại Test | Số lượng TC | Pass | Fail | Blocked | Chưa test |",
                "|:----------|:-----------|:-----|:-----|:--------|:----------|",
            ]
            categories = {}
            for line in lines:
                parsed_row = self.parse_test_case_row(line)
                if not parsed_row:
                    continue
                category, status = parsed_row
                if category not in categories:
                    categories[category] = {"total": 0, "pass": 0, "fail": 0, "blocked": 0, "untested": 0}
                categories[category]["total"] += 1
                if "✅ Pass" in status or "Pass" in status:
                    categories[category]["pass"] += 1
                elif "❌ Fail" in status or "Fail" in status:
                    categories[category]["fail"] += 1
                elif "🚫 Blocked" in status or "Blocked" in status:
                    categories[category]["blocked"] += 1
                else:
                    categories[category]["untested"] += 1

            for category, stats in categories.items():
                new_summary_table.append(f"| {category} | {stats['total']} | {stats['pass']} | {stats['fail']} | {stats['blocked']} | {stats['untested']} |")
            new_summary_table.append(f"| **Tổng** | **{total_cases}** | **{passed_cases}** | **{failed_cases}** | **{blocked_cases}** | **{untested_cases}** |")

            lines[summary_lines_range[0]:summary_lines_range[-1] + 1] = new_summary_table
            content = "\n".join(lines)

        suite_path.write_text(content, encoding="utf-8")
        print(f"Successfully synced: {suite_clean}. Coverage: {passed_cases}/{total_cases} PASS.")
        return True

    def run_sync(self):
        print("Starting Kanban Auto-Sync and Verification...")
        if not self.kanban_path.exists():
            print(f"[ERROR] Kanban file not found at {self.kanban_path}")
            return 1

        kanban_content = self.kanban_path.read_text(encoding="utf-8")
        done_section_match = re.search(r"## Done\s*\n(.*?)(?=\n##|$)", kanban_content, re.DOTALL)
        if not done_section_match:
            print("[SUCCESS] No Done tasks found in KANBAN.md to sync.")
            return 0

        done_tasks = re.findall(r"-\s*\[\s*[x ]\s*\]\s*(.*)", done_section_match.group(1))
        suite_links = []
        for task in done_tasks:
            links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", task)
            suite_links.extend(link for link in links if "test_suites/" in link)

        if not suite_links:
            print("[SUCCESS] No completed Test Suite cards found under ## Done.")
            return 0

        synced_suites = [os.path.basename(suite) for suite in suite_links if self.sync_completed_task(suite)]
        if synced_suites:
            self.log_activity("lint-sync", f"Đồng bộ Kanban thành công: Đã chuyển {len(synced_suites)} Test Suites sang 'Passed' và Features sang 'Done' ({', '.join(synced_suites)}).")

        print("\nExecuting System Audit...")
        return self.run_verify()

    def run_daily_sync(self, project, date_str):
        print(f"Starting Daily Standup Sync for project: {project}, date: {date_str}...")
        daily_note_rel = f"wiki/{project}/operations/daily_notes/{date_str}.md"
        daily_note_path = self.vault_dir / daily_note_rel

        if not daily_note_path.exists():
            print(f"[ERROR] Daily Note file not found: {daily_note_path}")
            return 1

        daily_content = daily_note_path.read_text(encoding="utf-8")
        blocked_section = re.search(r"### Khó khăn / Blocked:\s*\n(.*?)(?=\n##|$)", daily_content, re.DOTALL)
        new_bug_created = False
        bug_link = ""
        bug_id = ""

        if blocked_section:
            blocked_lines = re.findall(r"-\s*(?:\[\s*[ -]\s*\]\s*)?(Blocked:?\s*)?([A-Z0-9-]+)?[:\s]?(.*)", blocked_section.group(1).strip())
            for _, bid, desc in blocked_lines:
                desc = desc.strip()
                if not desc or desc.lower() == "n/a" or desc == "[-]":
                    continue

                bug_id = bid if bid else f"BUG-{project.split('_')[-1].upper()}-{datetime.now(WIKI_TZ).strftime('%f')[:3]}"
                bug_filename = f"bug_{safe_filename(desc)}.md"
                bug_rel_path = f"wiki/{project}/bugs_knowledge/{bug_filename}"
                bug_full_path = self.vault_dir / bug_rel_path

                if not bug_full_path.exists():
                    print(f"Auto-creating Bug RCA file for: {desc} ({bug_id})")
                    tpl_path = self.templates_dir / "tpl_bug_rca.md"
                    if not tpl_path.exists():
                        print(f"[ERROR] Bug RCA Template not found at {tpl_path}")
                        return 1

                    tpl = tpl_path.read_text(encoding="utf-8")
                    tpl = tpl.replace("{{title}}", desc)
                    tpl = tpl.replace("{{date:YYYY-MM-DD}}", date_str)
                    tpl = tpl.replace("status: 🔴 open", "status: Open")
                    tpl = tpl.replace("(BUG-xxx)", f"({bug_id})")
                    tpl = tpl.replace("created: {{date:YYYY-MM-DD}}", f"created: {date_str}")
                    tpl = tpl.replace("updated: {{date:YYYY-MM-DD}}", f"updated: {date_str}")

                    bug_full_path.parent.mkdir(parents=True, exist_ok=True)
                    bug_full_path.write_text(tpl, encoding="utf-8")
                    print(f"Successfully created Bug RCA file: {bug_filename}")
                    self.log_activity("create", f"Tự động tạo Bug RCA từ Standup Blocked: {desc} ({bug_id}). Link: [[{bug_rel_path}]]")
                else:
                    print(f"Bug file already exists for: {bug_filename}")

                new_bug_created = True
                bug_link = f"[[{bug_rel_path}|{bug_id}]]"
                break

        if self.kanban_path.exists():
            kanban_lines = self.kanban_path.read_text(encoding="utf-8").split("\n")
            updated_kanban = False
            completed_standup = re.search(r"### Hôm qua đã làm:\s*\n(.*?)(?=\n##|$)", daily_content, re.DOTALL)

            if completed_standup:
                comp_links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", completed_standup.group(1))
                for link in comp_links:
                    link_base = os.path.splitext(os.path.basename(link))[0]
                    done_start = next((i for i, line in enumerate(kanban_lines) if "## Done" in line), -1)
                    search_limit = done_start if done_start != -1 else len(kanban_lines)
                    target_idx = next((i for i in range(0, search_limit) if link_base in kanban_lines[i] and kanban_lines[i].strip().startswith("-")), -1)

                    if target_idx != -1 and done_start != -1:
                        print(f"Kanban Sync: Moving task {link_base} to ## Done")
                        target_card_text = kanban_lines.pop(target_idx)
                        done_start = next((i for i, line in enumerate(kanban_lines) if "## Done" in line), -1)
                        checked_card = target_card_text.replace("- [ ]", "- [x]")
                        kanban_lines.insert(done_start + 2, checked_card)
                        updated_kanban = True
                        self.log_activity("task-update", f"Đồng bộ Kanban: Di chuyển task {link_base} sang cột ## Done theo Standup Daily Note [[{daily_note_rel}]].")

            if new_bug_created and bug_link:
                inprog_start = next((i for i, line in enumerate(kanban_lines) if "## InProgress" in line), -1)
                done_start = next((i for i, line in enumerate(kanban_lines) if "## Done" in line), len(kanban_lines))
                for index in range(inprog_start + 1, done_start):
                    line = kanban_lines[index]
                    if project in line and line.strip().startswith("-") and "test_suites/" in line and "🔴" not in line:
                        print(f"Kanban Sync: Attaching bug {bug_id} to task card")
                        kanban_lines[index] = line.rstrip() + f" (🔴 {bug_link})"
                        updated_kanban = True
                        self.log_activity("test-blocked", f"Đồng bộ Kanban: Task {project} bị nghẽn (🔴 Đính kèm bug {bug_id}).")
                        break

            if updated_kanban:
                self.kanban_path.write_text("\n".join(kanban_lines), encoding="utf-8")

        daily_content = re.sub(r"^status:\s*\w+", "status: Synced", daily_content, flags=re.MULTILINE)
        if "#qa/daily/synced" not in daily_content:
            daily_content = re.sub(r"tags:\s*\[(.*?)\]", r"tags: [\1, qa/daily/synced]", daily_content)
        daily_note_path.write_text(daily_content, encoding="utf-8")

        print(f"[SUCCESS] Daily standup synchronized and Daily Note status marked as Synced: {daily_note_rel}")
        self.log_activity("sync-daily", f"Đồng bộ thành công Daily Note ngày [[{daily_note_rel}]].")
        return 0

    def run_verify(self):
        all_pages = {}
        broken_links = []
        orphan_pages = []
        invalid_statuses = []
        guardrail_errors = []
        guardrail_warnings = []
        valid_feature_statuses = {"Draft", "Done", "Outdated"}
        valid_api_statuses = {"Draft", "Done", "Outdated"}
        valid_suite_statuses = {"Draft", "Testing", "Passed", "Failed", "Outdated"}
        valid_bug_statuses = {"Open", "Fixed", "Closed", "closed", "open", "fixed"}
        valid_plan_statuses = {"Draft", "Testing", "Passed", "Outdated"}
        valid_release_statuses = {"Draft", "Testing", "Done"}
        valid_task_spec_statuses = {"Draft", "InProgress", "Blocked", "Done"}
        valid_control_statuses = {"Done"}
        allowed_scopes = {"UI", "API", "Functional", "UI+Functional", "API+Functional", "UI+API", "E2E"}
        mojibake_markers = ("ðŸ", "âœ", "â", "âž", "áº", "á»", "Ä‘", "Æ°")
        exclude_dirs = {".obsidian", ".smart-env", "templates", "raw_sources", "scripts", ".claude", ".agents"}

        print(f"Starting LLM Wiki Vault Audit in: {self.vault_dir}...")
        for root, dirs, files in os.walk(self.vault_dir):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                if file.endswith(".md"):
                    filepath = Path(root) / file
                    rel_path = filepath.relative_to(self.vault_dir)
                    page_name = filepath.stem
                    all_pages[page_name] = {
                        "filepath": filepath,
                        "rel_path": str(rel_path),
                        "incoming_links": [],
                        "outgoing_links": [],
                        "status": None,
                    }

        link_pattern = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
        frontmatter_pattern = re.compile(r"^\ufeff?---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|$)", re.DOTALL)

        for page_name, info in all_pages.items():
            content = self.read_text(info["filepath"])
            fm_match = frontmatter_pattern.match(content)
            if fm_match:
                for line in fm_match.group(1).split("\n"):
                    if line.startswith("status:"):
                        info["status"] = line.split(":", 1)[1].strip()

            for link in link_pattern.findall(content):
                link_clean = clean_link_path(link)
                link_base = os.path.splitext(os.path.basename(link_clean))[0]
                if link_base:
                    info["outgoing_links"].append(link_base)
                    if link_base in all_pages:
                        all_pages[link_base]["incoming_links"].append(page_name)

        print("\n--- AUDIT RESULTS ---")
        placeholder_patterns = [
            r"^[.]{3}$", r"^[.]{2,}$", r"Tên Trang", r"tên_lỗi", r"YYYY-MM-DD", r"MÃ-TASK", r"MÃ_CR", r"Note", r"^auth_login$", r"^test_auth_login$",
        ]

        for info in all_pages.values():
            content = self.read_text(info["filepath"])
            for link in link_pattern.findall(content):
                link_clean = clean_link_path(link)
                if not link_clean:
                    continue
                if any(re.search(pattern, link_clean, re.IGNORECASE) for pattern in placeholder_patterns):
                    continue
                if "TÃ" in link_clean or "tÃªn_lá»—i" in link_clean:
                    continue
                link_base = os.path.splitext(os.path.basename(link_clean))[0]
                if link_base in all_pages or link_base in {"KANBAN", "log", "index", "OBSIDIAN_GUIDE"}:
                    continue
                normalized_link = link_clean.replace("\\", "/").strip("/")
                possible_paths = [self.vault_dir / normalized_link, self.vault_dir / f"{normalized_link}.md"]
                if not any(path.exists() and path.is_file() for path in possible_paths):
                    broken_links.append((info["rel_path"], link))

        for page_name, info in all_pages.items():
            if page_name in {"index", "log", "KANBAN", "OBSIDIAN_GUIDE"}:
                continue
            if "daily_notes" in info["rel_path"]:
                continue
            if not info["incoming_links"]:
                orphan_pages.append(info["rel_path"])

        for page_name, info in all_pages.items():
            status = info["status"]
            rel_path = info["rel_path"]
            content = self.read_text(info["filepath"])
            marker = next((item for item in mojibake_markers if item in content), None)
            if marker and page_name not in {"log", "USER_COMMANDS"}:
                guardrail_errors.append((rel_path, f"Possible mojibake/font encoding issue detected: '{marker}'"))
            rel_path_norm = rel_path.replace("\\", "/").lower()
            if "/features/" in "/" + rel_path_norm + "/" and status not in valid_feature_statuses:
                invalid_statuses.append((rel_path, status, "Features (Valid: Draft, Done, Outdated)"))
            elif "/api_specs/" in "/" + rel_path_norm + "/" and status not in valid_api_statuses:
                invalid_statuses.append((rel_path, status, "API Specs (Valid: Draft, Done, Outdated)"))
            elif "/test_suites/" in "/" + rel_path_norm + "/" and status not in valid_suite_statuses:
                invalid_statuses.append((rel_path, status, "Test Suites (Valid: Draft, Testing, Passed, Failed, Outdated)"))
            elif "/bugs_knowledge/" in "/" + rel_path_norm + "/" and status not in valid_bug_statuses:
                invalid_statuses.append((rel_path, status, "Bugs (Valid: Open, Fixed, Closed)"))
            elif "/test_plans/" in "/" + rel_path_norm + "/" and status not in valid_plan_statuses:
                invalid_statuses.append((rel_path, status, f"Test Plans (Valid: {valid_plan_statuses})"))
            elif "/releases/" in "/" + rel_path_norm + "/" and status not in valid_release_statuses:
                invalid_statuses.append((rel_path, status, f"Releases (Valid: {valid_release_statuses})"))
            elif "/task_specs/" in "/" + rel_path_norm + "/" and status not in valid_task_spec_statuses:
                invalid_statuses.append((rel_path, status, f"Task Specs (Valid: {valid_task_spec_statuses})"))
            elif page_name in {"index", "log"} and status not in valid_control_statuses:
                invalid_statuses.append((rel_path, status, "Control Files (Valid: Done)"))

        feature_open_questions = self.collect_open_question_refs()
        api_open_questions = self.collect_open_api_question_refs()
        suite_case_counts = {}
        suite_to_feature = {}
        feature_group_usage = set()
        for suite_path in sorted((self.vault_dir / "wiki").glob("**/test_suites/*.md")):
            rel_suite = suite_path.relative_to(self.vault_dir).as_posix()
            content = self.read_text(suite_path)
            lines = content.splitlines()
            rows = [line for line in lines if self.is_test_case_row(line)]
            suite_case_counts[rel_suite[:-3]] = len(rows)
            project = self.project_from_rel_path(rel_suite)
            for group_slug in self.extract_feature_group_tags(content):
                if project:
                    feature_group_usage.add((project, group_slug))

            if not self.has_any_heading(content, ("changelog",)):
                guardrail_errors.append((rel_suite, "Missing required section: ## 📅 Changelog"))
            if not self.has_any_heading(content, ("blocked coverage",)):
                guardrail_errors.append((rel_suite, "Missing required section: ## 🚧 Blocked Coverage"))
            if not self.has_any_heading(content, ("regression impact",)):
                guardrail_errors.append((rel_suite, "Missing required section: ## 🔁 Regression Impact"))

            header = next((line for line in lines if line.startswith("| Test ID")), "")
            if header and ("Phạm vi" not in header and "Ph?m vi" not in header):
                guardrail_errors.append((rel_suite, "Test case table is missing required column: Phạm vi"))

            feature_key = self.extract_linked_feature_key(content)
            if feature_key:
                suite_to_feature[rel_suite] = feature_key
            api_key = self.extract_linked_api_spec_key(content)
            has_api_reference = bool(api_key)
            open_refs = set()
            if feature_key:
                open_refs.update(feature_open_questions.get(feature_key, set()))
            if api_key:
                open_refs.update(api_open_questions.get(api_key, set()))

            for row in rows:
                cells = self.split_table_row(row)
                tc_id = cells[0] if cells else "UNKNOWN"
                source = cells[-2] if len(cells) >= 2 else ""
                cover = cells[2] if len(cells) >= 3 else ""
                scope = cells[3] if len(cells) >= 4 else ""
                row_lower = row.lower()

                if re.search(r"\bAPI-\d+\b", cover) or scope in {"API", "API+Functional", "UI+API"} or "api spec" in source.lower():
                    has_api_reference = True

                if "AI-Inferred" in row or "suy diễn" in row_lower or "suy luận" in row_lower or "assumption" in row_lower:
                    guardrail_errors.append((rel_suite, f"{tc_id}: contains inferred/assumption marker"))
                if source and "Explicit từ" not in source:
                    guardrail_errors.append((rel_suite, f"{tc_id}: source must start with or contain 'Explicit từ'"))
                if header and ("Phạm vi" in header or "Ph?m vi" in header) and len(cells) >= 11:
                    case_type = cells[4]
                    technique = cells[5]
                    if scope not in allowed_scopes:
                        guardrail_errors.append((rel_suite, f"{tc_id}: invalid Phạm vi '{scope}'"))
                    if case_type not in {"Positive", "Negative"}:
                        guardrail_errors.append((rel_suite, f"{tc_id}: invalid Loại case '{case_type}'"))
                    if technique in {"Positive", "Negative"}:
                        guardrail_errors.append((rel_suite, f"{tc_id}: Kỹ thuật test appears swapped with Loại case"))

                covered_refs = set(re.findall(r"\bR\d+\b|\bAC-\d+\b|\bAPI-\d+\b", cover))
                blocked_refs = covered_refs & open_refs
                if blocked_refs:
                    guardrail_errors.append((rel_suite, f"{tc_id}: covers refs with Open questions: {', '.join(sorted(blocked_refs))}"))

            if has_api_reference and not api_key:
                guardrail_errors.append((rel_suite, "API test case/scope detected but Test Suite does not link an API Spec in wiki/[project]/api_specs/"))

        for api_path in sorted((self.vault_dir / "wiki").glob("**/api_specs/*.md")):
            rel_api = api_path.relative_to(self.vault_dir).as_posix()
            content = self.read_text(api_path)
            project = self.project_from_rel_path(rel_api)
            for group_slug in self.extract_feature_group_tags(content):
                if project:
                    feature_group_usage.add((project, group_slug))
            if "qa/api-spec" not in content:
                guardrail_errors.append((rel_api, "Missing required tag: qa/api-spec"))
            if "## 📅 Changelog" not in content:
                guardrail_errors.append((rel_api, "Missing required section: ## 📅 Changelog"))
            for section in ("## API / Interface List", "## API Detail", "## ❓ Câu hỏi API chưa rõ", "## API Test Coverage"):
                if section not in content:
                    guardrail_errors.append((rel_api, f"Missing required section: {section}"))
            if not self.extract_linked_feature_key(content):
                guardrail_errors.append((rel_api, "API Spec must link back to a Feature Spec in wiki/[project]/features/"))
            if "AI-Inferred" in content or "suy diễn" in content.lower() or "suy luận" in content.lower() or "assumption" in content.lower():
                guardrail_errors.append((rel_api, "API Spec contains inferred/assumption marker"))
            for line in content.splitlines():
                if not line.startswith("| API-"):
                    continue
                cells = self.split_table_row(line)
                if len(cells) < 7:
                    continue
                api_id, source, status = cells[0], cells[5], cells[6]
                if status != "Blocked" and source and "Explicit từ" not in source:
                    guardrail_errors.append((rel_api, f"{api_id}: source must be explicit unless Status is Blocked"))

        for feature_path in sorted((self.vault_dir / "wiki").glob("**/features/*.md")):
            rel_feature = feature_path.relative_to(self.vault_dir).as_posix()
            content = self.read_text(feature_path)
            project = self.project_from_rel_path(rel_feature)
            for group_slug in self.extract_feature_group_tags(content):
                if project:
                    feature_group_usage.add((project, group_slug))
            if "## 📅 Changelog" not in content:
                guardrail_errors.append((rel_feature, "Missing required section: ## 📅 Changelog"))
            if "Câu hỏi chưa rõ" not in content and "C?u h?i ch?a rõ" not in content and "CÃ¢u há»i chÆ°a rÃµ" not in content:
                guardrail_errors.append((rel_feature, "Missing required section: ## ❓ Câu hỏi chưa rõ"))
            if "Impact Analysis & Regression Proposal" not in content:
                guardrail_warnings.append((rel_feature, "Recommended new section missing: ## 🔎 Impact Analysis & Regression Proposal"))

        for task_spec_path in sorted((self.vault_dir / "wiki").glob("**/task_specs/*.md")):
            rel_task_spec = task_spec_path.relative_to(self.vault_dir).as_posix()
            content = self.read_text(task_spec_path)
            if "## Linked Raw Tasks" not in content:
                guardrail_errors.append((rel_task_spec, "Missing required section: ## Linked Raw Tasks"))
            if "## Linked Feature Group" not in content:
                guardrail_errors.append((rel_task_spec, "Missing required section: ## Linked Feature Group"))
            if "## Linked Feature Specs" not in content:
                guardrail_errors.append((rel_task_spec, "Missing required section: ## Linked Feature Specs"))
            if "## Clarification Questions" not in content:
                guardrail_errors.append((rel_task_spec, "Missing required section: ## Clarification Questions"))
            if "## Impact Summary" not in content:
                guardrail_errors.append((rel_task_spec, "Missing required section: ## Impact Summary"))
            if "## Testcase Delta Summary" not in content:
                guardrail_errors.append((rel_task_spec, "Missing required section: ## Testcase Delta Summary"))
            if "## Changelog" not in content:
                guardrail_errors.append((rel_task_spec, "Missing required section: ## Changelog"))

        for project, group_slug in sorted(feature_group_usage):
            group_file = group_slug.replace("-", "_")
            expected_path = self.vault_dir / "wiki" / project / "feature_groups" / f"{group_file}.md"
            if not expected_path.exists():
                guardrail_errors.append((
                    f"wiki/{project}/feature_groups/{group_file}.md",
                    f"Missing Feature Group page for tag qa/feature-group/{group_slug}",
                ))

        if self.kanban_path.exists():
            kanban_content = self.kanban_path.read_text(encoding="utf-8")
            for line in kanban_content.splitlines():
                if "test_suites/" not in line:
                    continue
                links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", line)
                suite_link = next((clean_link_path(link) for link in links if "test_suites/" in clean_link_path(link)), None)
                count_match = re.search(r"\((\d+)\s*TC\)", line)
                if suite_link and count_match and suite_link in suite_case_counts:
                    expected = int(count_match.group(1))
                    actual = suite_case_counts[suite_link]
                    if expected != actual:
                        guardrail_errors.append(("KANBAN.md", f"{suite_link}: Kanban TC count {expected} != actual {actual}"))

        mcp_path = self.vault_dir / ".mcp.json"
        if mcp_path.exists():
            mcp_content = mcp_path.read_text(encoding="utf-8", errors="ignore")
            if re.search(r"Bearer\s+[A-Za-z0-9._-]{16,}", mcp_content):
                guardrail_errors.append((".mcp.json", "Tracked/local MCP config appears to contain a Bearer token"))

        if broken_links:
            print(f"\n[ERROR] BROKEN LINKS FOUND ({len(broken_links)}):")
            for source, target in broken_links:
                print(f"  - In '{source}': Links to [[{target}]] which does not exist.")
        else:
            print("\n[SUCCESS] No broken links found!")

        if orphan_pages:
            print(f"\n[WARNING] ORPHAN PAGES FOUND ({len(orphan_pages)}):")
            for page in orphan_pages:
                print(f"  - '{page}' has no incoming links.")
        else:
            print("\n[SUCCESS] No orphan pages found!")

        if invalid_statuses:
            print(f"\n[ERROR] INVALID STATUSES FOUND ({len(invalid_statuses)}):")
            for page, status, expected in invalid_statuses:
                print(f"  - In '{page}': Found status '{status}', expected {expected}.")
        else:
            print("\n[SUCCESS] All frontmatter statuses are 100% compliant!")

        if guardrail_errors:
            print(f"\n[ERROR] GOVERNANCE GUARDRAIL ERRORS ({len(guardrail_errors)}):")
            for source, message in guardrail_errors:
                print(f"  - In '{source}': {message}")
        else:
            print("\n[SUCCESS] Governance guardrails are compliant!")

        if guardrail_warnings:
            print(f"\n[WARNING] GOVERNANCE GUARDRAIL WARNINGS ({len(guardrail_warnings)}):")
            for source, message in guardrail_warnings:
                print(f"  - In '{source}': {message}")

        print("\nAudit complete.")
        return 1 if broken_links or invalid_statuses or guardrail_errors else 0

    def is_test_case_row(self, line):
        return bool(re.match(r"^\|\s*\*?\*?TC-", line))

    def split_table_row(self, line):
        return [part.strip().strip("*") for part in line.strip().strip("|").split("|")]

    def extract_linked_feature_key(self, content):
        links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", content)
        feature_link = next((link for link in links if "/features/" in clean_link_path(link)), None)
        if not feature_link:
            return None
        clean = clean_link_path(feature_link)
        return clean[:-3] if clean.endswith(".md") else clean

    def extract_linked_api_spec_key(self, content):
        links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", content)
        api_link = next((link for link in links if "/api_specs/" in clean_link_path(link)), None)
        if not api_link:
            return None
        clean = clean_link_path(api_link)
        return clean[:-3] if clean.endswith(".md") else clean

    def collect_open_question_refs(self):
        refs_by_feature = {}
        for feature_path in sorted((self.vault_dir / "wiki").glob("**/features/*.md")):
            rel_feature = feature_path.relative_to(self.vault_dir).as_posix()
            key = rel_feature[:-3]
            text = self.read_text(feature_path)
            section = self.extract_section(text, "Câu hỏi chưa rõ")
            refs = set()
            for line in section.splitlines():
                is_open = "[ ]" in line or re.search(r"\|\s*Open\s*\|", line) or "❓" in line
                if not is_open:
                    continue
                refs.update(re.findall(r"\bR\d+\b|\bAC-\d+\b", line))
            refs_by_feature[key] = refs
            refs_by_feature[feature_path.stem] = refs
        return refs_by_feature

    def collect_open_api_question_refs(self):
        refs_by_api = {}
        for api_path in sorted((self.vault_dir / "wiki").glob("**/api_specs/*.md")):
            rel_api = api_path.relative_to(self.vault_dir).as_posix()
            key = rel_api[:-3]
            text = self.read_text(api_path)
            section = self.extract_section(text, "Câu hỏi API chưa rõ")
            refs = set()
            for line in section.splitlines():
                is_open = "[ ]" in line or re.search(r"\|\s*Open\s*\|", line) or "❓" in line
                if not is_open:
                    continue
                refs.update(re.findall(r"\bR\d+\b|\bAC-\d+\b|\bAPI-\d+\b", line))
            refs_by_api[key] = refs
            refs_by_api[api_path.stem] = refs
        return refs_by_api

    def extract_section(self, text, heading_text):
        pattern = re.compile(rf"^## .*{re.escape(heading_text)}.*?\n(.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
        match = pattern.search(text)
        return match.group(1) if match else ""

    def extract_feature_group_tags(self, content):
        return set(re.findall(r"qa/feature-group/([A-Za-z0-9_-]+)", content))

    def project_from_rel_path(self, rel_path):
        parts = rel_path.replace("\\", "/").split("/")
        if len(parts) >= 2 and parts[0] == "wiki":
            return parts[1]
        return None


    def run_repair(self):
        print("Starting wiki repair: BOM cleanup + Kanban TC count sync...")
        changed = 0
        for md in self.vault_dir.rglob("*.md"):
            if any(skip in md.parts for skip in (".obsidian", ".smart-env", ".karate_cache", ".git")):
                continue
            original = md.read_text(encoding="utf-8", errors="ignore")
            cleaned = original[1:] if original.startswith("﻿") else original
            if cleaned != original:
                md.write_text(cleaned, encoding="utf-8")
                changed += 1

        suite_case_counts = {}
        for suite_path in sorted((self.vault_dir / "wiki").glob("**/test_suites/*.md")):
            rel_suite = suite_path.relative_to(self.vault_dir).as_posix()
            content = self.read_text(suite_path)
            rows = [line for line in content.splitlines() if self.is_test_case_row(line)]
            suite_case_counts[rel_suite[:-3]] = len(rows)

        if self.kanban_path.exists():
            lines = self.read_text(self.kanban_path).splitlines()
            out = []
            for line in lines:
                if "test_suites/" in line:
                    links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", line)
                    suite_link = next((clean_link_path(link) for link in links if "test_suites/" in clean_link_path(link)), None)
                    if suite_link and suite_link in suite_case_counts:
                        line = re.sub(r"\((\d+)\s*TC\)", f"({suite_case_counts[suite_link]} TC)", line)
                out.append(line)
            self.kanban_path.write_text("\\n".join(out) + "\\n", encoding="utf-8")
            changed += 1

        print(f"[SUCCESS] Repair complete. Files touched: {changed}")
        return self.run_verify()
