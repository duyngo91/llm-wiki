# Task Spec Layer Policy

- Use two-layer model: Task Spec (execution layer) + Feature Spec (domain layer).
- Task Spec path: `wiki/project_hasaki/task_specs/task_<tbb2_code>.md`.
- Every TBB2 must link to related HSK, feature group, feature specs, and test suites.
- Keep traceability chain machine-readable: `TBB2 -> HSK -> Task Spec -> Feature Group -> Feature -> Requirement/AC -> Testcase`.
- If related question is Open, do not generate testcase for unclear behavior; record Blocked Coverage.
