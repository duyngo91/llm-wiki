# No Inference Policy

- Requirement, AC, API contract, and testcases must be explicit from approved sources.
- If unclear, add entries to Question sections.
- Content based on open questions must stay in Blocked Coverage, not active testcases.
- Generate testcases from question-derived content only after question is answered and spec is updated.
- **Enum completeness:** Khi claim về enumeration (dropdown, status list, giá trị hợp lệ), phải liệt kê ĐỦ tất cả values từ source. Nếu không chắc đã đủ → đánh dấu UNCLEAR, ghi vào Câu hỏi. Không mark SUPPORTED khi chưa verify đủ count.
- **Source line reference:** Khi ghi Source trong bảng Requirement, ưu tiên format `[doc_name]#[line]` để reviewer có thể verify trực tiếp.
