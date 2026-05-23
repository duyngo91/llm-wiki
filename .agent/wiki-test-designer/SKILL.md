---
name: wiki-test-designer
description: Provides expert software testing capabilities following ISTQB Test Design standards. Always trigger this skill when the user asks to generate test cases, write a test suite, map a test plan, create test scenarios, perform equivalence partitioning / boundary value analysis, or write a Test Suite markdown file in the `test_suites/` directory of the QA LLM Wiki.
---

# 📐 Wiki Test Designer (ISTQB Test Design)

This skill implements the **ISTQB Test Design** phase (QA kiểm thử). Your primary goal is to determine **"How to test" (Test Cases & Procedures)** by reading feature specifications, applying systematic test design techniques, loading real test data, and generating a highly detailed **Test Suite** file.

---

## 🧭 Trigger Conditions

Activate this skill when the user says:
- "viết test cases", "thiết kế test cases", "tạo test suite"
- "chuyển specs sang test cases", "áp dụng kỹ thuật phân tích biên/phân vùng tương đương"
- "sinh kịch bản kiểm thử", "phủ requirement bằng test cases"
- "chạy Quy trình 2.5 (Task State Transition) - Bước 1" hoặc "Quy trình 2.1 (Ingest) - Bước 2"

---

## 📐 Playbook: ISTQB Test Design Mindset

When designing test cases, do not just write happy paths. You MUST apply systematic test design techniques:

1.  **Read Feature Spec context:** Open the corresponding feature spec `wiki/[project]/features/[feature_name].md` to extract the logic flows, actors, business rules, and BDD scenarios.
2.  **Load Real Operations Context:**
    *   Open `wiki/[project]/operations/environments.md` to get the target URL (e.g., Staging/UAT) and sandbox credentials.
    *   Open `wiki/[project]/operations/test_data.md` to fetch sandbox phone numbers, sandbox credit card numbers, and sample JSON payloads.
3.  **Apply Test Design Techniques:**
    *   **Equivalence Partitioning (Phân vùng tương đương):** Split inputs into valid and invalid classes. Write at least one test case for each class.
    *   **Boundary Value Analysis (Phân tích giá trị biên):** Identify boundary numbers (e.g., min length, max length). Design cases for `Min-1`, `Min`, `Min+1`, `Max-1`, `Max`, `Max+1`.
    *   **Error Guessing (Negative cases):** Write negative cases such as clicking buttons twice, reloading pages during loading, exiting browsers, or typing SQL Injection/XSS payloads in form inputs.
    *   **Security & Session:** Test session timeout, button back behavior after logging out, and unauthorized URL access.
4.  **Traceability & Reviewability:** Every test case MUST explicitly state:
    *   **AC/Req Cover:** Requirement ID (`R1`, `R2`...) and/or Acceptance Criteria / BDD Scenario (`AC-01`, `Scenario 1`...).
    *   **Case Type:** `Positive` or `Negative`. Regression/security/performance cases must still state whether the expected behavior is positive or negative.
    *   **Test Technique:** e.g. `Happy Path`, `Equivalence Partitioning`, `Boundary Value Analysis`, `Decision Table`, `State Transition`, `Error Guessing`, `Security`, `Regression`.
    *   **Source / Inference:** Use `Explicit từ [source]` when the case is directly supported by specs; use `AI-Inferred từ [source/logic]` when the case is inferred from business rules, validation logic, bug history, or testing heuristics.
    *   If no source or AC/Req mapping exists, do NOT finalize the case; add it to clarification questions instead.

---

## 🛠️ Step-by-Step Implementation Flow

### Step 1: Scan Features Spec & Test Data
- Identify the project area (e.g. `project_orange` or `project_demo`).
- Read the Feature Specs file `wiki/[project]/features/[feature_name].md`.
- Read `wiki/[project]/operations/environments.md` and `wiki/[project]/operations/test_data.md`.

### Step 2: Read Template
- Always view [tpl_test_suite.md](file:///e:/2nd_brain/LLM_Wiki/templates/tpl_test_suite.md) to ensure exact structural compliance.

### Step 3: Write Test Suite File
Create or modify `wiki/[project]/test_suites/test_[feature_name].md`:
- Set tags: `tags: [qa/test-suite]`
- Set status: `status: Draft` (or `Testing` if active in Kanban).
- Generate unique Test Case IDs: `TC-[PROJECT_CODE]-[ID]` (e.g. `TC-OH-001`, `TC-OH-002`...).
- Incorporate the exact URLs and sandbox test data into the "Điều kiện tiên quyết" and "Các bước thực hiện" columns.
- For every row in the Test Cases table, fill `AC/Req Cover`, `Loại case`, `Kỹ thuật test`, and `Nguồn / Suy diễn`.
- Mark inferred cases clearly as `AI-Inferred từ ...`; never mix inferred logic with explicit requirements without labeling it.
- Cover every approved Requirement ID / Acceptance Criteria at least once. If coverage is impossible because the spec is unclear, list the missing coverage as a clarification item.
- Set the status of all new test cases to `⏳` (Chờ test).
- Reconstruct the **## 📊 Tổng quan Test Coverage** summary table at the top, initializing `Pass`, `Fail`, `Blocked` to `0`, and placing the count of cases under `Chưa test` and `Số lượng TC`.
- Link each Test Case ID back to its corresponding Requirement ID (`R1`, `R2`, etc.) inside the Test Coverage Mapping table of both the Test Suite and Feature Spec (Requirements Traceability Matrix).

### Step 4: Register and Audit
- Append the new Test Suite link to the multi-project index page: [index.md](file:///e:/2nd_brain/LLM_Wiki/index.md).
- Create/modify a Kanban task card under the `## TODO` column of [KANBAN.md](file:///e:/2nd_brain/LLM_Wiki/KANBAN.md):
  ` - [ ] [[raw_sources/[project]/tasks/[task_name]|[TASK_ID]]] ➔ [[wiki/[project]/test_suites/test_[feature_name]|Test Suite [Feature Title]]] [Priority]`
- Log the activity in [log.md](file:///e:/2nd_brain/LLM_Wiki/log.md) with `[create]` or `[lint-sync]` prefix.
- Run `python scripts/verify_wiki.py` to ensure zero broken links or tag errors.

---

## 📝 Output Presentation Format

After generating or updating the Test Suite, present a concise summary to the user:

```markdown
### 📐 Thiết Kế Kịch Bản Kiểm Thử Hoàn Tất (ISTQB Test Design)
- **Test Suite Đã Khởi Tạo:** `[[wiki/[project]/test_suites/test_[feature_name]|test_[feature_name].md]]` (Trạng thái: `Draft` 🧪)
- **Số lượng Test Cases:** Đã thiết kế **[X] kịch bản kiểm thử** (Status: `⏳` Chờ test):
  - Happy Path: **[A]** cases
  - Negative (EP/BVA): **[B]** cases
  - Security / Session: **[C]** cases
- **Dữ liệu Test Thực Tế:** Đã tích hợp tài khoản sandbox và URL test từ `environments.md` & `test_data.md`.
- **Requirements Traceability Matrix (RTM):** 100% test cases được ánh xạ đầy đủ với Requirement IDs (`R1` đến `R[N]`).
- **Phân loại & Kỹ thuật:** Đã ghi rõ `Positive/Negative`, kỹ thuật test design và `AC/Req Cover` cho từng case.
- **Case suy diễn:** Có **[Z]** test cases được đánh dấu `AI-Inferred`, kèm nguồn/logic suy diễn để QA Lead review.
- **Kanban Task:** Đã bổ sung thẻ kiểm thử vào cột `## TODO` trên `KANBAN.md`.
```
