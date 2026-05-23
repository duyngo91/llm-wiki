import os
import re
import sys
from datetime import datetime

# Force UTF-8 stdout for Windows
if sys.platform.startswith('win'):
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# Resolve Vault Directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.dirname(SCRIPT_DIR)
KANBAN_PATH = os.path.join(VAULT_DIR, "KANBAN.md")
LOG_PATH = os.path.join(VAULT_DIR, "log.md")
TEMPLATES_DIR = os.path.join(VAULT_DIR, "templates")

# Helper to normalize link path
def clean_link_path(link_text):
    # Strip sections, escaped pipes and trailing backslashes
    clean = link_text.strip().split("#")[0].replace("\\|", "|").split("|")[0].strip().rstrip("\\")
    return clean.replace("\\", "/").strip("/")

# Convert Vietnamese to safe ascii lowercase filename
def safe_filename(text):
    text = text.lower()
    replacements = {
        'á': 'a', 'à': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a', 'ă': 'a', 'ắ': 'a', 'ằ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
        'â': 'a', 'ấ': 'a', 'ầ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a', 'đ': 'd', 'é': 'e', 'è': 'e', 'ẻ': 'e', 'ẽ': 'e',
        'ẹ': 'e', 'ê': 'e', 'ế': 'e', 'ề': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e', 'í': 'i', 'ì': 'i', 'ỉ': 'i', 'ĩ': 'i',
        'ị': 'i', 'ó': 'o', 'ò': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o', 'ô': 'o', 'ố': 'o', 'ồ': 'o', 'ổ': 'o', 'ỗ': 'o',
        'ộ': 'o', 'ơ': 'o', 'ớ': 'o', 'ờ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o', 'ú': 'u', 'ù': 'u', 'ủ': 'u', 'ũ': 'u',
        'ụ': 'u', 'ư': 'u', 'ứ': 'u', 'ừ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u', 'ý': 'y', 'ỳ': 'y', 'ỷ': 'y', 'ỹ': 'y',
        'ỵ': 'y'
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    # Replace non-alphanumeric with underscores
    text = re.sub(r'[^a-z0-9_-]', '_', text)
    # Remove multiple consecutive underscores
    text = re.sub(r'_{2,}', '_', text)
    return text.strip('_')

# Log activity to log.md
def log_activity(action_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"- [{timestamp}] [{action_type}] | {message}\n"
    
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        # Insert after frontmatter
        fm_end = -1
        fm_count = 0
        for i, line in enumerate(lines):
            if line.strip() == "---":
                fm_count += 1
                if fm_count == 2:
                    fm_end = i
                    break
        
        if fm_end != -1:
            lines.insert(fm_end + 1, "\n" + log_entry)
        else:
            lines.insert(0, log_entry)
            
        with open(LOG_PATH, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"Logged: {message}")

# Process and update a single Test Suite and its associated Feature
def sync_completed_task(test_suite_link):
    suite_clean = clean_link_path(test_suite_link)
    suite_path = os.path.join(VAULT_DIR, suite_clean + ".md")
    
    if not os.path.exists(suite_path):
        print(f"[WARNING] Test Suite file not found: {suite_path}")
        return False
        
    print(f"Syncing completed Test Suite: {suite_clean}")
    
    with open(suite_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 1. Update frontmatter status to Passed
    original_content = content
    content = re.sub(r'^status:\s*\w+', 'status: Passed', content, flags=re.MULTILINE)
    
    # 2. Extract Feature link to sync Feature status
    feature_link_match = re.search(r'(?i)(?:-\s*\*\*?)?(?:feature(?: liên quan)?|requirement)(?:\*\*?)?\s*:\s*(?:\s*\*\*?)?\[\[([^\]|]+)', content)
        
    if feature_link_match:
        feat_clean = clean_link_path(feature_link_match.group(1))
        feat_path = os.path.join(VAULT_DIR, feat_clean + ".md")
        if os.path.exists(feat_path):
            print(f"Syncing completed Feature: {feat_clean}")
            with open(feat_path, "r", encoding="utf-8") as ff:
                feat_content = ff.read()
            feat_content = re.sub(r'^status:\s*\w+', 'status: Done', feat_content, flags=re.MULTILINE)
            # Sync individual test coverage status inside feature specs too!
            feat_content = feat_content.replace("⏳", "✅ Pass")
            with open(feat_path, "w", encoding="utf-8") as ff:
                ff.write(feat_content)
    
    # 3. Change all ⏳ status test cases to ✅ Pass
    content = content.replace("⏳", "✅ Pass")
    
    # 4. Recalculate summary metrics table
    # Standard format: | Happy Path | 2 | 0 | 0 | 0 | 2 |
    lines = content.split("\n")
    tc_table_started = False
    passed_cases = 0
    failed_cases = 0
    blocked_cases = 0
    untested_cases = 0
    total_cases = 0

    def parse_test_case_row(line):
        if "TC-" not in line or "|" not in line:
            return None

        cells = [p.strip() for p in line.strip().strip("|").split("|")]
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
    
    # Parse actual test cases
    for line in lines:
        parsed_row = parse_test_case_row(line)
        if parsed_row:
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
                    
    # Rebuild Test Coverage Summary Table
    # Identify type of tests from actual parsed lines or simply rewrite the totals row
    summary_started = False
    summary_lines_range = []
    
    for idx, line in enumerate(lines):
        if "## 📊 Tổng quan Test Coverage" in line:
            summary_started = True
            continue
        if summary_started:
            if line.startswith("|"):
                summary_lines_range.append(idx)
            elif line.strip() == "" and len(summary_lines_range) > 0:
                break
                
    if summary_lines_range:
        # Reconstruct the summary table
        new_summary_table = [
            "| Loại Test | Số lượng TC | Pass | Fail | Blocked | Chưa test |",
            "|:----------|:-----------|:-----|:-----|:--------|:----------|"
        ]
        
        # Parse test categories and count them
        categories = {}
        for line in lines:
            parsed_row = parse_test_case_row(line)
            if parsed_row:
                cat, status = parsed_row
                if cat not in categories:
                    categories[cat] = {"total": 0, "pass": 0, "fail": 0, "blocked": 0, "untested": 0}
                categories[cat]["total"] += 1
                if "✅ Pass" in status or "Pass" in status:
                    categories[cat]["pass"] += 1
                elif "❌ Fail" in status or "Fail" in status:
                    categories[cat]["fail"] += 1
                elif "🚫 Blocked" in status or "Blocked" in status:
                    categories[cat]["blocked"] += 1
                else:
                    categories[cat]["untested"] += 1
                        
        for cat, stats in categories.items():
            new_summary_table.append(f"| {cat} | {stats['total']} | {stats['pass']} | {stats['fail']} | {stats['blocked']} | {stats['untested']} |")
            
        new_summary_table.append(f"| **Tổng** | **{total_cases}** | **{passed_cases}** | **{failed_cases}** | **{blocked_cases}** | **{untested_cases}** |")
        
        # Replace lines
        start_idx = summary_lines_range[0]
        end_idx = summary_lines_range[-1]
        lines[start_idx:end_idx+1] = new_summary_table
        content = "\n".join(lines)

    # Save suite updates
    with open(suite_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Successfully synced: {suite_clean}. Coverage: {passed_cases}/{total_cases} PASS.")
    return True

# Command: Sync (Quy trình 2.4)
def run_sync():
    print("Starting Kanban Auto-Sync and Verification...")
    if not os.path.exists(KANBAN_PATH):
        print(f"[ERROR] Kanban file not found at {KANBAN_PATH}")
        sys.exit(1)
        
    with open(KANBAN_PATH, "r", encoding="utf-8") as f:
        kanban_content = f.read()
        
    # Parse ## Done section
    done_section_match = re.search(r'## Done\s*\n(.*?)(?=\n##|$)', kanban_content, re.DOTALL)
    if not done_section_match:
        print("[SUCCESS] No Done tasks found in KANBAN.md to sync.")
        return
        
    done_text = done_section_match.group(1)
    # Extract all check-list lines
    done_tasks = re.findall(r'-\s*\[\s*[x ]\s*\]\s*(.*)', done_text)
    
    suite_links = []
    for task in done_tasks:
        # Find test suite links: e.g. [[wiki/project_orange/test_suites/test_orangehrm_auth|...]]
        links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', task)
        for link in links:
            if "test_suites/" in link:
                suite_links.append(link)
                
    if not suite_links:
        print("[SUCCESS] No completed Test Suite cards found under ## Done.")
        return
        
    synced_suites = []
    for suite in suite_links:
        if sync_completed_task(suite):
            synced_suites.append(os.path.basename(suite))
            
    if synced_suites:
        log_activity("lint-sync", f"Đồng bộ Kanban thành công: Đã chuyển {len(synced_suites)} Test Suites sang 'Passed' và Features sang 'Done' ({', '.join(synced_suites)}).")
    
    # Auto-run vault verification script
    verify_script = os.path.join(SCRIPT_DIR, "verify_wiki.py")
    if os.path.exists(verify_script):
        print("\nExecuting System Audit (verify_wiki.py)...")
        import subprocess
        result = subprocess.run([sys.executable, verify_script], capture_output=True, text=True, encoding="utf-8")
        print(result.stdout)
        if result.returncode != 0:
            print("[ERROR] System Audit failed. Please resolve broken links or statuses.")
            sys.exit(1)
    else:
        print("[WARNING] verify_wiki.py script not found in scripts directory.")

# Command: Daily Standup Sync & Auto Bug (Quy trình 2.3)
def run_daily_sync(project, date_str):
    print(f"Starting Daily Standup Sync for project: {project}, date: {date_str}...")
    daily_note_rel = f"wiki/{project}/operations/daily_notes/{date_str}.md"
    daily_note_path = os.path.join(VAULT_DIR, daily_note_rel.replace("/", "\\"))
    
    if not os.path.exists(daily_note_path):
        print(f"[ERROR] Daily Note file not found: {daily_note_path}")
        sys.exit(1)
        
    with open(daily_note_path, "r", encoding="utf-8") as f:
        daily_content = f.read()
        
    # 1. Parse Blocked section to extract bugs
    blocked_section = re.search(r'### Khó khăn / Blocked:\s*\n(.*?)(?=\n##|$)', daily_content, re.DOTALL)
    new_bug_created = False
    bug_link = ""
    bug_id = ""
    
    if blocked_section:
        blocked_text = blocked_section.group(1).strip()
        # Find lines starting with - and containing bug descriptions
        blocked_lines = re.findall(r'-\s*(?:\[\s*[ -]\s*\]\s*)?(Blocked:?\s*)?([A-Z0-9-]+)?[:\s]?(.*)', blocked_text)
        
        for prefix, bid, desc in blocked_lines:
            desc = desc.strip()
            if not desc or desc.lower() == "n/a" or desc == "[-]" or desc == "":
                continue
                
            bug_id = bid if bid else f"BUG-{project.split('_')[-1].upper()}-{datetime.now().strftime('%f')[:3]}"
            bug_name = safe_filename(desc)
            bug_filename = f"bug_{bug_name}.md"
            bug_rel_path = f"wiki/{project}/bugs_knowledge/{bug_filename}"
            bug_full_path = os.path.join(VAULT_DIR, bug_rel_path.replace("/", "\\"))
            
            if not os.path.exists(bug_full_path):
                print(f"Auto-creating Bug RCA file for: {desc} ({bug_id})")
                tpl_path = os.path.join(TEMPLATES_DIR, "tpl_bug_rca.md")
                if os.path.exists(tpl_path):
                    with open(tpl_path, "r", encoding="utf-8") as tf:
                        tpl = tf.read()
                    
                    # Fill placeholders
                    tpl = tpl.replace("{{title}}", desc)
                    tpl = tpl.replace("{{date:YYYY-MM-DD}}", date_str)
                    tpl = tpl.replace("status: 🔴 open", "status: Open")
                    tpl = tpl.replace("(BUG-xxx)", f"({bug_id})")
                    tpl = tpl.replace("created: {{date:YYYY-MM-DD}}", f"created: {date_str}")
                    tpl = tpl.replace("updated: {{date:YYYY-MM-DD}}", f"updated: {date_str}")
                    
                    # Write new bug
                    os.makedirs(os.path.dirname(bug_full_path), exist_ok=True)
                    with open(bug_full_path, "w", encoding="utf-8") as bf:
                        bf.write(tpl)
                        
                    new_bug_created = True
                    bug_link = f"[[{bug_rel_path}|{bug_id}]]"
                    print(f"Successfully created Bug RCA file: {bug_filename}")
                    log_activity("create", f"Tự động tạo Bug RCA từ Standup Blocked: {desc} ({bug_id}). Link: [[{bug_rel_path}]]")
                    break
                else:
                    print(f"[ERROR] Bug RCA Template not found at {tpl_path}")
            else:
                print(f"Bug file already exists for: {bug_filename}")
                bug_link = f"[[{bug_rel_path}|{bug_id}]]"
                new_bug_created = True
                break

    # 2. Update Kanban card based on standup
    if os.path.exists(KANBAN_PATH):
        with open(KANBAN_PATH, "r", encoding="utf-8") as kf:
            kanban_text = kf.read()
            
        # Parse today's completed task from Daily standup
        completed_standup = re.search(r'### Hôm qua đã làm:\s*\n(.*?)(?=\n##|$)', daily_content, re.DOTALL)
        todo_standup = re.search(r'### Hôm nay sẽ làm:\s*\n(.*?)(?=\n##|$)', daily_content, re.DOTALL)
        
        kanban_lines = kanban_text.split("\n")
        updated_kanban = False
        
        # 2a. Handle done tasks (Hôm qua đã làm completed checkboxes)
        if completed_standup:
            comp_text = completed_standup.group(1)
            comp_links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', comp_text)
            for link in comp_links:
                # Find that card in Kanban and move to Done
                link_base = os.path.splitext(os.path.basename(link))[0]
                
                # Check if card is in Todo or InProgress, and move it to Done
                todo_start = -1
                inprog_start = -1
                done_start = -1
                
                for idx, line in enumerate(kanban_lines):
                    if "## TODO" in line:
                        todo_start = idx
                    elif "## InProgress" in line:
                        inprog_start = idx
                    elif "## Done" in line:
                        done_start = idx
                        
                target_card_line_idx = -1
                target_card_text = ""
                
                # Search Todo and InProgress
                search_limit = done_start if done_start != -1 else len(kanban_lines)
                for idx in range(todo_start + 1, search_limit):
                    line = kanban_lines[idx]
                    if link_base in line and line.strip().startswith("-"):
                        target_card_line_idx = idx
                        target_card_text = line
                        break
                        
                if target_card_line_idx != -1:
                    print(f"Kanban Sync: Moving task {link_base} to ## Done")
                    # Remove from original line
                    kanban_lines.pop(target_card_line_idx)
                    # Find Done section again to insert
                    for idx, line in enumerate(kanban_lines):
                        if "## Done" in line:
                            done_start = idx
                            break
                    # Insert under Done
                    # Make sure checkbox is checked [x]
                    checked_card = target_card_text.replace("- [ ]", "- [x]").replace("- [ ]", "- [x]")
                    kanban_lines.insert(done_start + 2, checked_card)
                    updated_kanban = True
                    log_activity("task-update", f"Đồng bộ Kanban: Di chuyển task {link_base} sang cột ## Done theo Standup Daily Note [[{daily_note_rel}]].")

        # 2b. Handle blocked task (Attach bug link)
        if new_bug_created and bug_link:
            # Find the active InProgress task for the project
            todo_start = -1
            inprog_start = -1
            done_start = -1
            for idx, line in enumerate(kanban_lines):
                if "## TODO" in line:
                    todo_start = idx
                elif "## InProgress" in line:
                    inprog_start = idx
                elif "## Done" in line:
                    done_start = idx
                    
            target_limit = done_start if done_start != -1 else len(kanban_lines)
            for idx in range(inprog_start + 1, target_limit):
                line = kanban_lines[idx]
                if project in line and line.strip().startswith("-") and "test_suites/" in line:
                    # Append red bug link at the end if not already attached
                    if "🔴" not in line:
                        print(f"Kanban Sync: Attaching bug {bug_id} to task card")
                        kanban_lines[idx] = line.rstrip() + f" (🔴 {bug_link})"
                        updated_kanban = True
                        log_activity("test-blocked", f"Đồng bộ Kanban: Task {project} bị nghẽn (🔴 Đính kèm bug {bug_id}).")
                        break
                        
        if updated_kanban:
            with open(KANBAN_PATH, "w", encoding="utf-8") as kf:
                kf.write("\n".join(kanban_lines))

    # 3. Mark Daily Note as Synced
    daily_content = re.sub(r'^status:\s*\w+', 'status: Synced', daily_content, flags=re.MULTILINE)
    # Add tag if not present
    if "#qa/daily/synced" not in daily_content:
        # replace tags line
        daily_content = re.sub(r'tags:\s*\[(.*?)\]', r'tags: [\1, qa/daily/synced]', daily_content)
        
    with open(daily_note_path, "w", encoding="utf-8") as f:
        f.write(daily_content)
        
    print(f"[SUCCESS] Daily standup synchronized and Daily Note status marked as Synced: {daily_note_rel}")
    log_activity("sync-daily", f"Đồng bộ thành công Daily Note ngày [[{daily_note_rel}]].")

# Main CLI entrypoint
def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/wiki_manager.py [sync | daily-sync]")
        print("For daily-sync: python scripts/wiki_manager.py daily-sync --project <project_name> --date <YYYY-MM-DD>")
        sys.exit(1)
        
    command = sys.argv[1]
    
    if command == "sync":
        run_sync()
    elif command == "daily-sync":
        project = None
        date_str = None
        
        # simple args parsing
        for i in range(2, len(sys.argv)):
            if sys.argv[i] == "--project" and i + 1 < len(sys.argv):
                project = sys.argv[i+1]
            elif sys.argv[i] == "--date" and i + 1 < len(sys.argv):
                date_str = sys.argv[i+1]
                
        if not project or not date_str:
            print("[ERROR] Missing arguments for daily-sync. Please specify --project and --date.")
            sys.exit(1)
            
        run_daily_sync(project, date_str)
    else:
        print(f"[ERROR] Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
