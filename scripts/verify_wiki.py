import os
import re
import sys

# Force UTF-8 stdout if possible (essential for Windows encoding)
if sys.platform.startswith('win'):
    import sys, codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

vault_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
wiki_dir = os.path.join(vault_dir, "wiki")

all_pages = {}
broken_links = []
orphan_pages = []
invalid_statuses = []

# Valid statuses defined in WIKI_RULES.md
valid_feature_statuses = {"Draft", "Done", "Outdated"}
valid_suite_statuses = {"Draft", "Testing", "Passed", "Failed", "Outdated"}
valid_bug_statuses = {"Open", "Fixed", "Closed", "closed", "open", "fixed"}
valid_plan_statuses = {"Draft", "Testing", "Passed", "Outdated"}
valid_release_statuses = {"Draft", "Testing", "Done"}
valid_control_statuses = {"Done"}

# Scan all markdown files in vault (excluding templates, raw_sources, .obsidian, scripts, .agent, .agents)
exclude_dirs = {".obsidian", ".smart-env", "templates", "raw_sources", "scripts", ".agent", ".agents"}

print(f"Starting LLM Wiki Vault Audit in: {vault_dir}...")

for root, dirs, files in os.walk(vault_dir):
    # Filter out excluded directories
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            # Use relative path as the page key (without extension)
            rel_path = os.path.relpath(filepath, vault_dir)
            page_name = os.path.splitext(os.path.basename(file))[0]
            
            all_pages[page_name] = {
                "filepath": filepath,
                "rel_path": rel_path,
                "incoming_links": [],
                "outgoing_links": [],
                "status": None,
                "tags": []
            }

# Regex patterns
link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
frontmatter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

for page_name, info in all_pages.items():
    with open(info["filepath"], "r", encoding="utf-8") as f:
        content = f.read()
        
        # Parse Frontmatter
        fm_match = frontmatter_pattern.match(content)
        if fm_match:
            fm_text = fm_match.group(1)
            for line in fm_text.split("\n"):
                if line.startswith("status:"):
                    status_val = line.split(":", 1)[1].strip()
                    info["status"] = status_val
                elif line.startswith("tags:"):
                    tags_text = line.split(":", 1)[1].strip()
                    # extract tags
                    tags = re.findall(r'#?[\w/-]+', tags_text)
                    info["tags"] = [t.strip("[]# ") for t in tags]
        
        # Parse Links
        links = link_pattern.findall(content)
        for link in links:
            link_clean = link.strip().split("#")[0].replace("\\|", "|").split("|")[0].strip().rstrip("\\")
            # get basename
            link_base = os.path.splitext(os.path.basename(link_clean))[0]
            if link_base:
                info["outgoing_links"].append(link_base)
                if link_base in all_pages:
                    all_pages[link_base]["incoming_links"].append(page_name)

# Verification
print("\n--- AUDIT RESULTS ---")

# 1. Check Broken Links
placeholder_patterns = [
    r'^[.]{3}$', r'^[.]{2,}$', r'Tên Trang', r'tên_lỗi', r'YYYY-MM-DD', r'MÃ-TASK', r'MÃ_CR', r'Note', r'^auth_login$', r'^test_auth_login$'
]

for page_name, info in all_pages.items():
    with open(info["filepath"], "r", encoding="utf-8") as f:
        content = f.read()
        links = link_pattern.findall(content)
        for link in links:
            link_clean = link.strip().split("#")[0].replace("\\|", "|").split("|")[0].strip().rstrip("\\")
            if not link_clean:
                continue
            
            # Ignore placeholder links in illustrative rules/guides
            is_placeholder = False
            for pat in placeholder_patterns:
                if re.search(pat, link_clean, re.IGNORECASE):
                    is_placeholder = True
                    break
            if is_placeholder:
                continue
                
            link_base = os.path.splitext(os.path.basename(link_clean))[0]
            
            # Check if it exists in scanned pages or matches system pages
            if link_base in all_pages or link_base in {"KANBAN", "WIKI_RULES", "log", "index", "OBSIDIAN_GUIDE"}:
                continue
                
            # Check if it physically exists on disk (for templates or raw_sources)
            normalized_link = link_clean.replace("\\", "/").strip("/")
            possible_paths = [
                os.path.join(vault_dir, normalized_link),
                os.path.join(vault_dir, normalized_link + ".md")
            ]
            
            file_exists = False
            for p in possible_paths:
                if os.path.exists(p) and os.path.isfile(p):
                    file_exists = True
                    break
                    
            if not file_exists:
                broken_links.append((info["rel_path"], link))

# 2. Check Orphan Pages
for page_name, info in all_pages.items():
    # Ignore index, rules, log, KANBAN, guide, templates and daily notes
    if page_name in {"index", "WIKI_RULES", "log", "KANBAN", "OBSIDIAN_GUIDE"}:
        continue
    if "daily_notes" in info["rel_path"]:
        continue
    if not info["incoming_links"]:
        orphan_pages.append(info["rel_path"])

# 3. Check Frontmatter Status
for page_name, info in all_pages.items():
    status = info["status"]
    rel_path = info["rel_path"]
    rel_path_norm = rel_path.replace("\\", "/").lower()
    
    if "/features/" in "/" + rel_path_norm + "/":
        if status not in valid_feature_statuses:
            invalid_statuses.append((rel_path, status, "Features (Valid: Draft, Done, Outdated)"))
    elif "/test_suites/" in "/" + rel_path_norm + "/":
        if status not in valid_suite_statuses:
            invalid_statuses.append((rel_path, status, "Test Suites (Valid: Draft, Testing, Passed, Failed, Outdated)"))
    elif "/bugs_knowledge/" in "/" + rel_path_norm + "/":
        if status not in valid_bug_statuses:
            invalid_statuses.append((rel_path, status, "Bugs (Valid: Open, Fixed, Closed)"))
    elif "/test_plans/" in "/" + rel_path_norm + "/":
        if status not in valid_plan_statuses:
            invalid_statuses.append((rel_path, status, f"Test Plans (Valid: {valid_plan_statuses})"))
    elif "/releases/" in "/" + rel_path_norm + "/":
        if status not in valid_release_statuses:
            invalid_statuses.append((rel_path, status, f"Releases (Valid: {valid_release_statuses})"))
    elif page_name in {"index", "WIKI_RULES", "log"}:
        if status not in valid_control_statuses:
            invalid_statuses.append((rel_path, status, "Control Files (Valid: Done)"))

# Output results
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

print("\nAudit complete.")
sys.exit(1 if broken_links or invalid_statuses else 0)
