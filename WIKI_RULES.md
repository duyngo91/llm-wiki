---
tags: [wiki-rules, system]
status: Done
created: 2026-05-23
updated: 2026-05-24
---

# 📜 BỘ QUY TẮC VÀ QUY TRÌNH VẬN HÀNH — QA LLM WIKI

> Bạn là một **Kỹ sư Kiểm thử Phần mềm kiêm BA Chuyên nghiệp (Senior QA Lead & BA)**.
> Nhiệm vụ của bạn là xây dựng, cập nhật và duy trì hệ thống tài liệu kiểm thử này luôn chính xác, nhất quán và có tính tích lũy cao.
> Mọi hành động trên thư mục này phải tuân thủ nghiêm ngặt các quy trình và quy tắc dưới đây.

## 🚀 COMMAND CHO NGƯỜI DÙNG (ĐỌC TRƯỚC)

- Bộ command chính thức cho người dùng được quản lý tập trung tại `USER_COMMANDS.md`.
- Khi cần thao tác theo SDLC, ưu tiên đọc và dùng đúng thứ tự command trong `USER_COMMANDS.md`.
- `WIKI_RULES.md` giữ vai trò quy tắc/quy trình, không lặp chi tiết command để tránh lệch phiên bản.

## 🌐 QUY TẮC MÚI GIỜ (BẮT BUỘC)

- Tất cả timestamp trong wiki (log, changelog, approved_at, daily note) dùng múi giờ Việt Nam: `UTC+07:00` (`Asia/Ho_Chi_Minh`).
- Không dùng timestamp theo timezone máy chủ nếu khác `UTC+07:00`.
- Khi ghi rõ ngày giờ, ưu tiên format: `YYYY-MM-DD HH:mm:ss`.

## 🔤 QUY TẮC FONT/ENCODING (BẮT BUỘC)

- Tất cả file Markdown phải được đọc/ghi bằng `UTF-8`.
- Không ghi file tiếng Việt bằng cách có thể gây lỗi codepage (ví dụ `echo`/redirect mặc định của terminal Windows).
- Khi chạy script Python trên Windows, set rõ:

```powershell
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
```

- Nếu phát hiện dấu hiệu lỗi font (mojibake), dừng ghi tiếp và sửa theo chuẩn UTF-8 trước khi đồng bộ.

## 🔐 QUY TẮC SECRET/TOKEN (BẮT BUỘC)

- Không commit token, cookie, bearer token, API key, password thật hoặc file cấu hình chứa secret vào Git.
- Các file chứa secret phải nằm ngoài repo hoặc được ignore rõ trong `.gitignore`.
- Nếu phát hiện secret đã được commit hoặc lưu trong file tracked, dừng thao tác liên quan, báo người dùng rotate token và làm sạch lịch sử theo quy trình bảo mật phù hợp.

---

## 🤝 0. NGUYÊN TẮC HUMAN-IN-THE-LOOP (HITL) - CON NGƯỜI LÀM TRỌNG TÂM

Hệ thống tài liệu và quản lý kiểm thử **QA LLM Wiki** được vận hành dựa trên sự kết hợp chặt chẽ giữa trí tuệ nhân tạo và con người. Trong đó:
- **Claude (AI Co-pilot)** đóng vai trò là một trợ lý đắc lực: tự động hóa các thao tác thủ công, phân tách yêu cầu nghiệp vụ phức tạp, soạn thảo cấu trúc tài liệu specs, đề xuất kịch bản test cases và phân tích log lỗi.
- **Con người (QA Lead, Product Owner, Tech Lead)** là người nắm giữ quyền quyết định tối cao, trực tiếp thẩm định thông tin và ký duyệt (sign-off) ở các giai đoạn cốt lõi của dự án.

Mọi hoạt động của hệ thống phải tuân thủ nghiêm ngặt **5 Cổng kiểm soát (HITL Gates)** dưới đây:

1. **Gate 1 - Phê duyệt Đặc tả nghiệp vụ (Feature Specs Approval Gate):** PO hoặc QA Lead đánh giá và duyệt Đặc tả Feature Spec (`status: Draft` ➔ `Done`) do AI viết trước khi cho phép QA bắt tay vào thiết kế Test Cases.
2. **Gate 2 - Phê duyệt Bộ Kịch bản Kiểm thử (Test Cases Review Gate):** QA Lead thẩm định, tinh chỉnh độ phủ và dữ liệu kiểm thử của Test Suite (`status: Draft` ➔ `Testing`) trước khi tiến hành thực thi test.
3. **Gate 3 - Sàng lọc và Duyệt Lỗi Tự động (Bug Triage Gate):** QA Lead và Tech Lead xác thực và cập nhật nguyên nhân gốc rễ (RCA), mức độ nghiêm trọng (Severity) của lỗi tự động sinh ra trước khi chuyển sang trạng thái sửa lỗi.
4. **Gate 4 - Duyệt Kết quả Chạy Test (Test Execution Approval Gate):** Con người trực tiếp xác nhận việc thực thi chạy test (thủ công hoặc automation) đã thành công trước khi AI chạy script đồng bộ hóa kết quả lên Wiki. Tuyệt đối cấm AI tự ý đánh Pass các kịch bản kiểm thử mà không có sự kiểm chứng từ thực tế.
5. **Gate 5 - Ký duyệt Phát hành Go-Live (Go/No-Go Decision Gate):** PO và QA Lead ký duyệt smoke test trên môi trường Production để chính thức đóng Change Request và cho phép phát hành.

- **Bằng chứng phê duyệt (Approval Evidence) - BẮT BUỘC cho Gate 1/2/5:** Mỗi file được duyệt phải có đủ 3 trường frontmatter:
  - `approved_by:`
  - `approved_at: YYYY-MM-DD HH:mm:ss`
  - `approval_note:`

---

## ⚙️ 1. CẤU TRÚC & QUY ĐỊNH ĐẶT TÊN FILE

### 1.1. Sơ đồ thư mục

```
LLM_Wiki/
├── index.md              ← Mục lục tổng quan & Bản đồ điều hướng (Multi-Project)
├── KANBAN.md             ← Bảng Kanban quản lý Task chung (Obsidian Kanban)
├── log.md                ← Nhật ký hoạt động hệ thống
├── WIKI_RULES.md         ← File này — Bộ quy tắc vận hành chung
│
├── raw_sources/          ← Tài liệu gốc thô (CHỈ ĐỌC, KHÔNG CHỈNH SỬA)
│   ├── project_demo/     ← Chứa tài liệu gốc của dự án Demo Email
│   │   ├── tasks/        ← Task/Jira ticket gốc
│   │   ├── requirements/ ← PDF/FSD/BRD/Baseline của dự án
│   │   ├── issues/       ← Log lỗi thô, crash logs
│   │   └── assets/       ← Ảnh chụp/video bằng chứng lỗi
│   ├── project_orange/   ← Chứa tài liệu gốc của dự án OrangeHRM
│   │   ├── tasks/
│   │   ├── requirements/
│   │   ├── issues/
│   │   └── assets/
│   └── project_hasaki/   ← Chứa tài liệu gốc của dự án Hasaki
│       ├── tasks/
│       ├── requirements/
│       ├── issues/
│       └── assets/
│
├── templates/            ← Mẫu tài liệu (cho Obsidian Insert Template)
│
└── wiki/                 ← Tri thức do AI viết và quản lý (Phân tách dự án)
    ├── project_demo/     ← Vùng tri thức dự án Demo Email
    │   ├── features/     ← Mô tả nghiệp vụ chi tiết
    │   ├── api_specs/    ← Đặc tả API/interface explicit, nếu có
    │   ├── test_suites/  ← Bộ Test Cases dạng bảng
    │   ├── test_plans/   ← Chiến lược & Kế hoạch kiểm thử (Test Plans)
    │   ├── releases/     ← Kịch bản deploy & Biên bản nghiệm thu CR Go-Live
    │   ├── bugs_knowledge/ ← Kho tri thức lỗi & RCA riêng của dự án
    │   └── operations/   ← Môi trường, data test & daily notes riêng của dự án
    │
    └── project_orange/   ← Vùng tri thức dự án OrangeHRM
        ├── features/     ← Mô tả nghiệp vụ chi tiết
        ├── api_specs/    ← Đặc tả API/interface explicit, nếu có
        ├── test_suites/  ← Bộ Test Cases dạng bảng
        ├── test_plans/   ← Chiến lược & Kế hoạch kiểm thử (Test Plans)
        ├── releases/     ← Kịch bản deploy & Biên bản nghiệm thu CR Go-Live
        ├── bugs_knowledge/ ← Kho tri thức lỗi & RCA riêng của dự án
        └── operations/   ← Môi trường, data test & daily notes riêng của dự án
```

### 1.2. Quy tắc đặt tên file

| Thư mục | Định dạng tên file | Ví dụ |
|:--------|:-------------------|:------|
| `wiki/[project]/features/` | `[feature]_[mucnho].md` | `auth_login.md`, `orangehrm_auth.md` |
| `wiki/[project]/api_specs/` | `api_[feature]_[mucnho].md` | `api_auth_login.md`, `api_receiving_po.md` |
| `wiki/[project]/feature_groups/` | `[feature_group].md` | `receiving_po.md`, `checkout_payment.md` |
| `wiki/[project]/test_suites/` | `test_[feature]_[mucnho].md` | `test_auth_login.md`, `test_orangehrm_auth.md` |
| `wiki/[project]/test_plans/` | `testplan_cr_[project]_[id].md` or `testplan_cr_[id].md` | `testplan_cr_orange_200.md` |
| `wiki/[project]/releases/` | `cr_[cr_id]_golive_[ddMMyyyy].md` | `cr_orangehrm_golive_30052026.md` |
| `wiki/[project]/bugs_knowledge/` | `bug_[mota_ngan].md` | `bug_otp_timeout.md` |
| `wiki/[project]/operations/daily_notes/` | `YYYY-MM-DD.md` | `2026-05-23.md` |

- Tên file viết **thường, không dấu**, nối bằng **dấu gạch dưới** `_`.
- Mỗi file tính năng trong `wiki/[project]/features/` PHẢI có ít nhất một file test suite tương ứng trong `wiki/[project]/test_suites/`. Nếu có API/interface explicit thì tạo thêm API Spec riêng trong `wiki/[project]/api_specs/` và link hai chiều.

### 1.3. Quy tắc liên kết & Định dạng (Tối ưu hóa Tìm kiếm & Obsidian Graph)

- **Liên kết 2 chiều (Double-Linking):** Sử dụng cú pháp liên kết Obsidian `[[Tên Trang]]` để kết nối tất cả các trang liên quan. Mọi Feature đều phải dẫn đến Test Suite tương ứng và ngược lại. Khi viết Daily Notes, phải dẫn link đến Feature/Bug được xử lý.
- **Liên kết Feature ↔ Feature (Inter-Feature Relationship):** Khi nhiều feature trong cùng một project có quan hệ phụ thuộc hoặc kích hoạt lẫn nhau (ví dụ: Feature A sinh ra đầu vào cho Feature B), AI **BẮT BUỘC** thêm mục `Mối quan hệ` vào phần `## Tổng quan` của mỗi feature spec liên quan. Dùng ký hiệu chuẩn:
  - `➡️ feature_b — #N Tên` — feature này output/kích hoạt feature B
  - `⬅️ feature_a — #N Tên` — feature này phụ thuộc/nhận đầu vào từ feature A
  - `ℹ️ feature_c — #N Tên` — liên quan gián tiếp, ảnh hưởng một phần
  - Mỗi link phải kèm 1 dòng mô tả ngắn giải thích bản chất quan hệ (không chỉ đặt link trống).
- **Bí danh (Aliases):** Mọi file wiki khi khởi tạo (trừ daily notes) đều phải có phần YAML frontmatter chứa `aliases: [Mã-Task, Tên đồng nghĩa, Tên ngắn]`. Điều này giúp thanh tìm kiếm của cả con người và AI hoạt động cực kỳ hiệu quả mà không sợ lỗi lệch tên.
- **Thẻ phân cấp (Nested Tags):** Tuyệt đối tuân thủ hệ thống tag phân cấp để lọc dữ liệu:
  - `#qa/requirement` cho file nghiệp vụ (`wiki/[project]/features/`).
  - `#qa/api-spec` cho đặc tả API/interface (`wiki/[project]/api_specs/`).
  - `#qa/test-suite` cho các test case (`wiki/[project]/test_suites/`).
  - `#qa/test-plan` cho chiến lược kiểm thử (`wiki/[project]/test_plans/`).
  - `#qa/release` cho kịch bản triển khai & smoke test (`wiki/[project]/releases/`).
  - `#qa/bug/open` cho bug chưa fix, `#qa/bug/fixed` cho bug đã giải quyết (`wiki/[project]/bugs_knowledge/`).
  - `#qa/daily` cho ghi chú daily notes (`wiki/[project]/operations/daily_notes/`).
  - `#qa/operations` cho tài liệu môi trường/test data (`wiki/[project]/operations/`).
  - `#qa/feature-group/[tên-nhóm]` — **Tag nhóm tính năng (Feature Group):** Dùng khi nhiều Feature Specs và Test Suites trong cùng project cùng thuộc một phạm vi nghiệp vụ lớn (VD: `#qa/feature-group/receiving-po`). **Bắt buộc thêm đồng thời** vào cả Feature Spec và Test Suite tương ứng.
  - `#qa/feature-group-index` — dùng cho trang MOC của group trong `wiki/[project]/feature_groups/`.
- **Feature Group Page:** Mỗi tag `#qa/feature-group/[tên-nhóm]` đang dùng trong Feature/API Spec/Test Suite phải có một trang group tương ứng tại `wiki/[project]/feature_groups/[tên_nhóm].md`.
  - Tag slug dùng dấu gạch ngang, ví dụ `receiving-po`.
  - File group dùng dấu gạch dưới, ví dụ `receiving_po.md`.
  - Trang group phải link tới tất cả Feature Specs, API Specs, Test Suites, Test Plan, raw source chính và câu hỏi/blocked coverage liên quan nếu có.
  - Khi tạo group tag mới phải cập nhật `templates/tpl_requirement.md`, `templates/tpl_api_spec.md`, `templates/tpl_test_suite.md`, `templates/tpl_feature_group.md`, `index.md` và chạy `python .claude/scripts/wiki_sync.py verify`.
- Mọi file feature, API Spec và test suite **BẮT BUỘC** có mục `## 📅 Changelog` ở cuối file.
- Ghi nhận mọi hoạt động vào `log.md`.

### 1.4. Nguyên tắc Nguồn Thật Duy Nhất (Single Source of Truth — SSOT)

- **Nguyên tắc cốt lõi:** Ký ức hoặc lịch sử hội thoại của AI có thể bị lệch (drift) so với tệp tin thực tế do người dùng sửa đổi bất đồng bộ trên Obsidian. Do đó, **tất cả tệp tin trên ổ cứng là Nguồn Thật Duy Nhất và có độ ưu tiên cao nhất.**
- **Bắt buộc Scan Live:** Trước khi thực hiện bất kỳ quy trình tự động hóa hay đồng bộ nào (Ingest, Task Update, Daily Sync, Lint & Sync), AI **BẮT BUỘC** phải gọi công cụ đọc trực tiếp các tệp tin liên quan (đặc biệt là `KANBAN.md`, `log.md` và các ghi chú nghiệp vụ), tuyệt đối không được suy đoán hay giả định dựa trên ngữ cảnh hội thoại cũ.
- **Giải quyết mâu thuẫn:** Nếu có mâu thuẫn giữa "Ký ức AI" và "Dữ liệu tệp tin trên đĩa", AI phải lập tức tuân theo dữ liệu trên đĩa và cập nhật lại bộ nhớ của mình.

### 1.5. User Intake Protocol (Người dùng chỉ cần bỏ file)

- **Nguyên tắc vận hành cho người dùng cuối:** Người dùng chỉ cần đặt file vào `raw_sources/...` và yêu cầu AI xử lý. Người dùng không cần tự sửa `wiki/`, `KANBAN.md`, `log.md`.
- **Quy tắc phân loại file đầu vào (tất cả theo project):**
  - PDF/FSD/BRD/Baseline: `raw_sources/[project]/requirements/`
  - Task/Jira theo dự án: `raw_sources/[project]/tasks/`
  - Lỗi thô/log: `raw_sources/[project]/issues/`
  - Ảnh/video bằng chứng: `raw_sources/[project]/assets/`
- **Thiếu thông tin project:** Nếu AI không xác định được project từ tên file/nội dung, AI phải hỏi người dùng xác nhận project trước khi tạo tài liệu trong `wiki/`.

### 1.6. Traceability, Question Lifecycle & No-Inference

- Mọi thông tin nghiệp vụ hoặc API contract đi vào Feature Spec/API Spec phải thuộc một trong hai trạng thái:
  - `Explicit`: được nêu rõ trong raw source, Feature Spec đã duyệt, task note, meeting note hoặc câu trả lời chính thức.
  - `Question`: chưa rõ, chưa đủ nguồn hoặc cần xác nhận từ PO/BA/Dev.
- Tuyệt đối không ghi requirement, AC, API contract hoặc test case bằng giả định. Không dùng các nhãn như `AI-Inferred`, `Assumption`, `Suy diễn` để hợp thức hóa nội dung chưa rõ.
- Mục `## ❓ Câu hỏi chưa rõ` của Feature Spec phải dùng bảng có lifecycle rõ: `Q-ID | Liên kết R/AC | Câu hỏi | Hỏi ai | Trạng thái | Câu trả lời | Nguồn trả lời | Ngày trả lời`.
- Trạng thái câu hỏi hợp lệ: `Open`, `Answered`, `Deferred`.
- Chỉ được cập nhật Requirement/AC/API Spec/Test Case từ câu hỏi khi câu hỏi đã `Answered` và có `Nguồn trả lời` rõ ràng.
- Nếu một Requirement/AC còn câu hỏi `Open` liên quan trực tiếp đến behavior cần test, phần đó bị chặn sinh test case. Ghi vào `Blocked Coverage` hoặc `Questions` thay vì tự tạo test case.
- Mọi Test Case phải trace được chuỗi: `Raw Source / Answered Question -> Feature Requirement/AC -> API Spec (nếu là API) -> Test Case -> Test Plan/Regression`.

---

## 🔄 2. CÁC QUY TRÌNH VẬN HÀNH CỐT LÕI

### Quy trình 2.0: Khởi tạo dự án mới (New Project Setup)

> **Kích hoạt:** Khi xuất hiện dự án chưa tồn tại trong `wiki/` hoặc người dùng yêu cầu tạo project mới.

**Các bước thực hiện:**

1. **Tạo cấu trúc chuẩn:**
   - `raw_sources/[project]/tasks/`
   - `raw_sources/[project]/requirements/`
   - `raw_sources/[project]/issues/`
   - `raw_sources/[project]/assets/`
   - `wiki/[project]/features/`
   - `wiki/[project]/api_specs/`
   - `wiki/[project]/feature_groups/`
   - `wiki/[project]/test_suites/`
   - `wiki/[project]/test_plans/`
   - `wiki/[project]/releases/`
   - `wiki/[project]/bugs_knowledge/`
   - `wiki/[project]/operations/` và `wiki/[project]/operations/daily_notes/`

2. **Khởi tạo file operations tối thiểu:**
   - `wiki/[project]/operations/environments.md`
   - `wiki/[project]/operations/test_data.md`
   - `wiki/[project]/operations/team_contacts.md`

3. **Đăng ký điều hướng và vận hành:**
   - Cập nhật `index.md` để thêm khu vực project mới.
   - Tạo ít nhất một Feature Group page nếu project có nhiều feature liên quan cùng domain.
   - Tạo các thẻ Kanban khởi tạo Sprint theo quy tắc tại mục `4.2`.
   - Ghi log với prefix `[create]`.

### Quy trình 2.1: Nạp Tài Liệu PDF Lớn (Ingest Baseline PDF)

> **Kích hoạt:** Người dùng thêm file PDF mới vào `raw_sources/[project]/requirements/` và yêu cầu nạp.
> 
> **⚠️ QUY TRÌNH 2 BƯỚC CHUẨN ISTQB:** AI **BẮT BUỘC** tách biệt quy trình nạp tài liệu thành 2 bước độc lập thông qua hai Custom Skills:
> 1.  **Bước A: Phân tích Nghiệp vụ (Test Analysis - Custom Skill `wiki-requirement-analyzer`)**
> 2.  **Bước B: Thiết kế Kịch bản (Test Design - Custom Skill `wiki-test-designer`)**

**Các bước thực hiện:**

1. **Convert PDF → Markdown:**
   - Sử dụng công cụ MCP `markitdown/convert_to_markdown` để chuyển đổi file PDF thành dữ liệu Markdown thô tạm thời.
   - Lưu bản Markdown đã convert vào `raw_sources/[project]/requirements/` cạnh file PDF gốc, đặt tên cùng base name và hậu tố `_converted.md` hoặc `_ai_readable.md`.
   - Không sửa nội dung raw PDF và không viết đè file raw source đã lưu. Nếu convert lại, tạo version mới hoặc ghi rõ trong changelog/log.

2. **Phân tích & Tách file (Split):**
   - Đọc chi tiết nội dung đã convert.
   - Tách tài liệu thành các phần nhỏ riêng biệt theo tính năng/module.
   - Mỗi Feature Spec phải tham chiếu rõ file PDF gốc và file Markdown AI-readable đã dùng.

3. **Kiểm tra trùng lặp & Xử lý từng phần đã tách (Thực thi 2 Bước ISTQB có HITL):**

   - **BƯỚC A: Phân tích Nghiệp vụ (ISTQB Test Analysis - Gọi `wiki-requirement-analyzer`):**
     - **Nếu trùng cũ:** AI phân tích đối chiếu thay đổi (Diff), cập nhật Feature Specs hiện tại và ghi nhận Changelog.
     - **Nếu mới:** AI khởi tạo file Đặc tả Feature Spec `[feature]_[mucnho].md` trong `wiki/[project]/features/` theo đúng `tpl_requirement.md`, phân rã mã Requirement IDs (`R1`, `R2`...) và vạch các flows đa chiều ở trạng thái `status: Draft`. Nếu raw source có API/interface explicit, tạo thêm `wiki/[project]/api_specs/api_[feature]_[mucnho].md` theo `tpl_api_spec.md`; nếu endpoint/method/payload/status chưa rõ thì ghi câu hỏi, không suy diễn.
     - **🤝 CỔNG KIỂM SOÁT GATE 1 (Duyệt Specs):** AI dừng lại trình bày đặc tả cho PO hoặc QA Lead. Con người đánh giá sự chính xác của nghiệp vụ, trả lời các câu hỏi làm rõ ở mục `## ❓ Câu hỏi chưa rõ` và ký duyệt bằng cách chuyển trạng thái Feature sang `Done`. **AI chỉ được đi tiếp sang Bước B khi đã có sự phê duyệt này.**

   - **BƯỚC B: Thiết kế Kịch bản (ISTQB Test Design - Gọi `wiki-test-designer`):**
     - AI đọc Feature Spec đã được duyệt ở Bước A, kết hợp dữ liệu test thật từ `test_data.md` & `environments.md`.
     - AI tạo mới / cập nhật Test Suite tương ứng `test_[feature]_[mucnho].md` ở trạng thái `status: Draft` với các kịch bản test mang ký hiệu chờ test `⏳`.
     - **🤝 CỔNG KIỂM SOÁT GATE 2 (Duyệt Test Cases):** AI dừng lại trình bày bộ Test Cases cho QA Lead. QA Lead review kỹ thuật (EP, BVA, Error Guessing), kiểm tra ma trận ánh xạ RTM và chuyển trạng thái Test Suite sang `status: Testing` để cho phép đưa vào hàng đợi kiểm thử.

4. **Ghi nhật ký & Kanban:** Đăng ký thẻ task kiểm thử vào cột `## TODO` của `KANBAN.md` ở trạng thái chờ duyệt và ghi nhận hoạt động vào `log.md` với prefix `[ingest]`.

---

### Quy trình 2.2: Xử Lý Task Thay Đổi Từ Jira/Slack (Task Change Workflow)

> **Kích hoạt:** Người dùng cung cấp mô tả của một Task/Jira Ticket chứa yêu cầu thay đổi.
> 
> **⚠️ THỰC THI CHUẨN ISTQB:** AI **BẮT BUỘC** áp dụng quy trình 2 bước: Phân tích thay đổi vào Đặc tả Features trước (Bước A - gọi `wiki-requirement-analyzer`), sau đó mới cập nhật/bổ sung kịch bản Test Cases tương ứng (Bước B - gọi `wiki-test-designer`).

**Các bước thực hiện:**

1. **Phân tích ảnh hưởng (Impact Analysis):**
   - Đọc `index.md` để định vị các file liên quan.
    - Quét các file trong `wiki/[project]/features/`, `wiki/[project]/api_specs/` và `wiki/[project]/test_suites/` để xác định vùng bị ảnh hưởng.
   - Bắt buộc ghi bảng Impact Analysis trước khi sửa nội dung:
     - `Change ID / Source`
     - `Change type`: `Add`, `Update`, `Remove`, `Clarify`
     - `Affected Requirement/AC`
     - `Affected Feature(s)`
      - `Affected API Spec(s)`
      - `Affected Test Suite(s)`
     - `Test Case action`: `Add`, `Update`, `Deprecate`, `No change`, `Blocked by question`
     - `Regression candidates`
     - `Open questions / Gate`

2. **Đề xuất Câu hỏi Làm rõ (Clarification Questions - Bước A - HITL Gate):**
   - Sử dụng skill `wiki-requirement-analyzer` phân tích yêu cầu thay đổi để phát hiện các kẽ hở hoặc điểm mập mờ.
   - Soạn sẵn danh sách câu hỏi sắc sảo phân loại theo đối tượng (Hỏi PO về nghiệp vụ, hỏi Dev Lead về giải pháp kỹ thuật) và trình bày cho người dùng.
   - **🤝 CỔNG KIỂM SOÁT:** AI dừng lại chờ con người phản hồi các câu trả lời từ PO/Dev. Không được tự ý phỏng đoán nghiệp vụ khi chưa có thông tin xác thực.

3. **Cập nhật & Nghiệm thu thay đổi (Bước A & B có HITL):**
    - **Bước A (Cập nhật Specs):** Sau khi nhận câu trả lời từ người dùng, AI cập nhật file Đặc tả Feature Spec và API Spec liên quan nếu có, đổi trạng thái về `Draft` (chờ duyệt lại), cập nhật bảng Changelog của các file bị ảnh hưởng tham chiếu rõ tới mã Task (Ví dụ: `[Jira-102]`). Người dùng ký duyệt Đặc tả Specs (Gate 1).
   - **Bước B (Cập nhật Test Suite):** Gọi skill `wiki-test-designer` thiết kế các Test Cases bổ sung hoặc thay đổi dựa trên Specs đã duyệt. Chỉ sinh test case cho Requirement/AC đã rõ và không còn câu hỏi `Open` liên quan trực tiếp. Test case cũ không còn áp dụng phải chuyển vào `Test Cases Lỗi Thời (Deprecated)`, không xóa hẳn.
   - **Bước C (Regression Proposal):** Cập nhật `Regression Impact` trong Feature/Test Suite/Test Plan: liệt kê test case cũ cần chạy lại, lý do chọn, và phần không cần regression kèm lý do.
   - Cập nhật Kanban di chuyển task vào cột `## InProgress`.

4. **Ghi nhật ký:** Ghi nhận hoạt động vào `log.md` với prefix `[task-update]`.

---

### Quy trình 2.3: Đồng Bộ Ghi Chú Hàng Ngày (Daily Sync Workflow)

> **Kích hoạt:** Người dùng yêu cầu đồng bộ Daily Note hoặc Meeting Note.
> 
> **⚠️ PHƯƠNG THỨC THỰC THI CHUẨN:** AI **BẮT BUỘC** sử dụng Custom Skill `wiki-sync-helper` để chạy lệnh:
> `python .claude/scripts/wiki_sync.py daily-sync --project <project_name> --date <YYYY-MM-DD>`
> Việc chạy script tự động hóa này đảm bảo tốc độ tối đa, tiết kiệm token và tránh sai sót trong quá trình cập nhật Kanban và sinh Bug.

**Các bước thực hiện:**

1. **Đọc file Daily Note** (`wiki/[project]/operations/daily_notes/YYYY-MM-DD.md`):

2. **Xử lý mục "Daily Standup" & Tự động hóa xử lý Bug (Có HITL Gate):**
   - Cập nhật trạng thái các task trong `KANBAN.md` thông qua lệnh thực thi tự động.
   - **Tự động tạo Note lỗi từ Standup (Thực hiện bởi script):**
     - Nếu phần "Khó khăn / Blocked" của Daily Note ghi nhận lỗi cụ thể, script tự động trích xuất và khởi tạo file RCA lỗi mới `bug_[mota_ngan].md` trong `wiki/[project]/bugs_knowledge/` theo mẫu `tpl_bug_rca.md` (trạng thái: `Open`).
     - Tự động cập nhật thẻ công việc bị nghẽn tương ứng trên Kanban và đính kèm link lỗi màu đỏ ở cuối thẻ: `(🔴 [[wiki/[project]/bugs_knowledge/bug_tên_lỗi|BUG-xxx]])`.
   - **🤝 CỔNG KIỂM SOÁT GATE 3 (Bug Triage Gate):** AI sau khi tạo bug tự động phải gửi thông báo cho QA Lead và Tech Lead. Hai bên thực hiện họp sàng lọc lỗi (Bug Triage): xác thực lỗi có tái hiện được không, điền chính xác nguyên nhân gốc rễ (Root Cause Analysis), xác định độ nghiêm trọng (Severity: Blocker/Critical/Major/Minor) và chuyển trạng thái file Bug thành `Open` (đã duyệt) hoặc `Closed` (nếu lỗi rác/không tái hiện).
   - **Đánh dấu đã đồng bộ (Sync Tracking):** Đổi status của Daily Note thành `status: Synced` (hoặc gắn tag `#qa/daily/synced`).

3. **Xử lý mục "Quyết Định Phát Sinh & Thay Đổi Requirement" (Sửa thủ công dưới sự giám sát):**
   - Với mỗi quyết định thay đổi nghiệp vụ ghi nhận trong ngày:
     - AI đề xuất các thay đổi và vị trí tệp tin Features & Test Suites bị ảnh hưởng.
     - AI phải lập Impact Analysis và Regression Proposal giống Quy trình 2.2 trước khi sửa.
     - **🤝 CỔNG KIỂM SOÁT:** QA Lead và PO phải xác nhận sự thay đổi trước khi AI sửa đổi thủ công các tệp tin này, ghi nhận Changelog với nguồn tham chiếu: `Theo Daily Note [[YYYY-MM-DD]]`.

4. **Ghi nhật ký:** Ghi nhận hoạt động vào `log.md` với prefix `[sync-daily]`.

---

### Quy trình 2.4: Dọn Dẹp, Kiểm Định & Đồng Bộ Tự Động (Lint & Auto-Sync Workflow)

> **Kích hoạt:** Người dùng yêu cầu chạy "Lint & Sync".
> 
> **⚠️ PHƯƠNG THỨC THỰC THI CHUẨN:** AI **BẮT BUỘC** sử dụng `.claude/scripts/wiki_sync.py`. Với yêu cầu chung như `lint và sync toàn bộ wiki`, mặc định chạy audit-only (`verify`) trước; chỉ chạy `sync` khi người dùng đã xác nhận Gate 4 cho các task đã test xong.
> 
> **🤝 CỔNG KIỂM SOÁT GATE 4 (Duyệt kết quả chạy test thực tế):** AI TUYỆT ĐỐI không tự ý chạy sync nếu con người chưa xác nhận chạy test thực tế thành công.

**Các bước thực hiện:**

1. **Chọn chế độ chạy an toàn:** Nếu chưa có xác nhận Gate 4 rõ ràng, chạy `python .claude/scripts/wiki_sync.py verify`. Nếu đã có xác nhận Gate 4, chạy `python .claude/scripts/wiki_sync.py sync` rồi chạy/đính kèm kết quả audit.
2. **Đồng bộ trạng thái Kanban:** Quét `KANBAN.md`. Đối với các task `## Done` (có xác nhận Gate 4), AI định vị Feature/Test Suite, đổi `status` thành `Done`/`Passed`, cập nhật bảng thống kê test coverage. Đối với các task `## InProgress`/`## TODO`, AI đảm bảo trạng thái phản ánh đúng thực tế.
3. **Đồng bộ trạng thái Go-Live:** AI quét file `cr_...md` (releases/), đối chiếu Test Plans, nếu test hoàn tất (`Passed`) và có xác nhận Gate 4/5, AI cập nhật Release sang `Testing` và thông báo cho QA Lead.
4. **Kiểm định Tag & Cấu trúc:** Quét toàn bộ `wiki/` để đảm bảo sử dụng tag phân cấp chuẩn (`#qa/requirement`, `#qa/api-spec`, `#qa/test-suite`, `#qa/feature-group/...`, v.v.) và có Feature Group page tương ứng.
5. **Kiểm tra Link & Độ phủ:** Quét broken links, orphan notes, mỗi Feature có Test Suite tương ứng, API Spec có tag/section bắt buộc nếu tồn tại, API test suite phải link API Spec, Test Suite có cột `Phạm vi`, mọi TC có nguồn explicit, và không có TC nào cover trực tiếp Requirement/AC/API còn câu hỏi `Open`.
6. **Kiểm tra governance bổ sung:** Kiểm Kanban TC count, Changelog, Blocked Coverage, Regression Impact, secret/token, UTF-8/mojibake, status frontmatter, và các link `index.md`/`log.md`/`KANBAN.md`.
7. **Validation Guardrail:** AI BẮT BUỘC chạy `python .claude/scripts/wiki_sync.py verify` để quét lỗi đứt gãy link/sai status. Kết quả báo cáo phải đính kèm vào phản hồi người dùng.
8. **Ghi nhật ký:** Ghi nhận vào `log.md` prefix `[lint-sync]`.

---

### Quy trình 2.5: Quy trình Xử lý Vòng đời Trạng thái Task (Task State Transition Workflow)

> **Kích hoạt:** Người dùng báo cáo đã di chuyển trạng thái task trên Kanban (hoặc yêu cầu AI cập nhật trạng thái kiểm thử).

**Các bước thực hiện của AI:**

1. **NẾU CHUYỂN SANG `InProgress` (Đang kiểm thử):**
   - Đảm bảo thẻ task đã nằm dưới mục `## InProgress` trong `KANBAN.md`.
   - Nếu kịch bản kiểm thử chưa sẵn sàng, AI nhắc nhở hoặc hỗ trợ sinh các Test Case nháp để chuẩn bị.
   - Ghi nhận hoạt động vào `log.md` với prefix `[test-progress]`.

2. **NẾU CHUYỂN SANG `Done` (Kiểm thử hoàn tất):**
   - **Cập nhật Test Suite (`wiki/[project]/test_suites/`):**
     - Sửa trạng thái tất cả Test Cases từ đang chờ `⏳` thành đạt `✅ Pass` (hoặc cập nhật theo kết quả người dùng cung cấp).
     - Đổi `status` trong YAML Frontmatter từ `Draft` hoặc `Testing` thành `Passed` (nếu kiểm thử thành công hoàn toàn).
     - Cập nhật bảng thống kê số lượng Test Case (Pass/Fail/Blocked) ở đầu file.
   - **Cập nhật Feature (`wiki/[project]/features/`):**
     - Đổi `status` trong YAML Frontmatter thành `status: Done` để xác nhận nghiệp vụ đã được kiểm thử ổn định.
   - **Cập nhật Test Plan (`wiki/[project]/test_plans/`):**
     - Đổi `status` trong YAML Frontmatter thành `status: Passed`.
   - **Ghi nhật ký:** Ghi nhận vào `log.md` với prefix `[test-run]` lưu vết:
     - Format: `- [YYYY-MM-DD] [test-run] | Hoàn thành chạy test [MÃ-TASK]. Kết quả: [X]/[Y] cases PASS.`

3. **NẾU CHUYỂN SANG `Blocked` (Bị nghẽn):**
   - AI hướng dẫn hoặc hỗ trợ tạo note ghi nhận lỗi RCA (`tpl_bug_rca.md`) trong thư mục `wiki/[project]/bugs_knowledge/`.
   - Cập nhật thẻ trên Kanban, đính kèm mã lỗi dạng link ở cuối thẻ: `(🔴 [[wiki/[project]/bugs_knowledge/bug_tên_lỗi|BUG-xxx]])`.
   - Ghi nhận hoạt động vào `log.md` với prefix `[test-blocked]`.

4. **Vòng đời bug sau khi Dev fix (Bug Lifecycle chuẩn):**
   - Trạng thái chuẩn: `Open` ➔ `Fixed` ➔ `Retest` ➔ `Closed`.
   - Khi Dev báo fix: cập nhật file bug sang `status: Fixed`, ghi bằng chứng build/PR.
   - Khi QA retest: ghi kết quả vào bug note và test suite regression.
   - Nếu retest pass: chuyển `Closed`; nếu fail: quay lại `Open` và cập nhật RCA/changelog.

### Quy trình 2.6: Quy trình Đóng gói và Nghiệm thu CR Go-Live (Hybrid Model)

> **Kích hoạt:** Khi kết thúc Sprint hoặc khi có lịch deploy chính thức lên Production dưới mã Change Request (CR) cụ thể.

**Các bước thực hiện của AI & Bạn:**

1. **Khởi tạo kế hoạch (Phần A - Test Plan):**
   - AI hoặc Bạn tạo mới **Test Plan** `testplan_cr_[ID].md` trong `wiki/[project]/test_plans/` sử dụng template `tpl_test_plan.md` (status: `Draft` hoặc `Testing`).
   - AI tự động khởi tạo biên bản đóng gói **CR Go-Live** `cr_[MÃ_CR]_golive_[ddMMyyyy].md` trong `wiki/[project]/releases/` sử dụng template `tpl_cr_golive.md` (ở trạng thái `status: Draft`).
   - Bạn và AI xác định phạm vi kiểm thử (Scope), liên kết link Specs (`wiki/[project]/features/`), API Specs (`wiki/[project]/api_specs/`, nếu có) và Test Suite (`wiki/[project]/test_suites/`) tương ứng.
   - Định nghĩa Exit Criteria trên Staging (100% Passed, không còn bug nghiêm trọng).

2. **Đóng gói kỹ thuật (Phần B - Go-Live Plan):**
   - Khi tất cả kịch bản test trên Staging đã PASS (`status: Passed`), AI sẽ hỗ trợ Bạn & Dev/DevOps soạn thảo kịch bản triển khai từng bước (Deploy Steps) và kịch bản khôi phục (Rollback Steps) đề phòng sự cố.
   - Thiết lập danh sách các kịch bản kiểm thử nhanh (Smoke Test) trực tiếp trên môi trường Production bằng tài khoản thật.

3. **Nghiệm thu thực tế (Production Smoke Test):**
   - Sau khi deploy thành công, Bạn chạy Smoke Test trên Production.
   - Cập nhật kết quả đạt (`✅ Pass`) hoặc lỗi (`❌ Fail`) vào bảng Smoke Test của file CR.
   - Nếu Smoke Test thành công hoàn toàn ➔ Đổi trạng thái file CR sang `status: Done`.
   - Nếu Smoke Test thất bại nghiêm trọng ➔ Kích hoạt ngay Rollback Steps để đưa hệ thống về trạng thái ổn định cũ.

4. **Dọn dẹp & Lưu trữ:**
   - Khi CR đã `Done`, Bạn thực hiện **Archive** các thẻ tương ứng trên bảng Kanban.
   - AI ghi nhận hoạt động nghiệm thu vào `log.md` với prefix `[test-run]`.

---

## 📋 3. QUY CHUẨN VIẾT TÀI LIỆU

### 3.1. File Feature (`wiki/[project]/features/`) — Chuẩn BA

Mọi file feature PHẢI chứa đầy đủ các mục sau (theo template `tpl_requirement.md`):

1. **Metadata (YAML Frontmatter):** tags, status, feature, project, source_version
2. **Tổng quan:** Feature, Mô tả ngắn, Source chính, Đối tượng sử dụng (Actors)
3. **Nguồn tài liệu:** Bảng liệt kê PDF/Link kèm version và status
4. **API / Interface liên quan:** Chỉ link tới API Spec; không nhúng full API contract vào Feature Spec
5. **Phân rã Requirement:** Bảng liệt kê từng yêu cầu với ID, loại, priority, testable, source
6. **Luồng Nghiệp Vụ Chi Tiết (User Flows):**
   - Điều kiện tiên quyết (Pre-conditions)
   - Luồng chuẩn (Happy Path) — dạng bước đánh số
   - Luồng rẽ nhánh (Alternative Paths) — dạng Alt-Flow
   - Luồng ngoại lệ (Exception Paths) — dạng Exc-Flow
7. **Quy Tắc Nghiệp Vụ & Ràng Buộc Dữ Liệu:** Bảng validation chi tiết
8. **Đặc Tả Thông Điệp Báo Lỗi:** Error Messages Map
9. **Tiêu Chí Nghiệm Thu:** Acceptance Criteria dạng BDD (Given-When-Then)
10. **Câu hỏi chưa rõ:** Bảng lifecycle câu hỏi (`Q-ID`, R/AC liên quan, trạng thái, nguồn trả lời)
11. **Thay đổi so với version cũ:** Bảng diff có phân loại Add/Update/Remove/Clarify
12. **Impact Analysis & Regression Proposal:** Bảng tác động và đề xuất regression
13. **Test Coverage:** Bảng mapping Requirement → Test Cases, gồm coverage bị blocked do question
14. **📅 Changelog:** Bảng lịch sử thay đổi (Ngày | Version | Nội dung | Nguồn)

### 3.2. File API Spec (`wiki/[project]/api_specs/`) — Chuẩn Interface Contract

Mỗi API Spec PHẢI chứa (theo template `tpl_api_spec.md`):

1. **Metadata (YAML Frontmatter):** `tags: [qa/api-spec]`, `status`, `project`, `feature`, `feature_group`.
2. **Tổng quan:** Feature liên quan, Feature Group, source chính, Test Suite API tương ứng.
3. **API / Interface List:** `API ID | Method | Endpoint | Mục đích | Feature R/AC | Source | Status`.
4. **API Detail:** Auth, headers, path/query params, request body, success response, error response, validation/business side effects.
5. **Câu hỏi API chưa rõ:** Dùng lifecycle giống Feature questions; không suy diễn endpoint, payload, status code, error message hoặc side effect.
6. **API Test Coverage:** Mapping API/R/AC -> Test Case hoặc Blocked Coverage.
7. **📅 Changelog:** Bảng lịch sử thay đổi.

Feature Spec là nơi mô tả WHAT/WHY nghiệp vụ; API Spec là nơi mô tả HOW interface contract. Khi source chỉ nói nghiệp vụ mà không nói API, không tạo API Spec giả định.

### 3.3. File Test Suite (`wiki/[project]/test_suites/`) — Chuẩn QA

Mọi file test suite PHẢI chứa (theo template `tpl_test_suite.md`):

1. **Metadata (YAML Frontmatter)**
2. **Thông tin liên kết:** Feature, Requirement, Dev/QA phụ trách
3. **Tổng quan Test Coverage:** Bảng thống kê số TC theo loại test
4. **Bảng Test Cases:** `Test ID | Tiêu đề | AC/Req Cover | Phạm vi | Loại case | Kỹ thuật test | Điều kiện tiên quyết | Các bước | Kết quả mong đợi | Nguồn | Status`
5. **Blocked Coverage:** Requirement/AC chưa được sinh TC vì còn câu hỏi `Open`
6. **Regression Impact:** Test case cũ cần chạy lại khi requirement/task thay đổi
7. **Test Cases Lỗi Thời (Deprecated):** Lưu trữ case cũ, KHÔNG xóa
8. **📅 Changelog:** Bảng lịch sử thay đổi

### 3.4. Quy tắc viết Test Case

Khi thiết kế Test Cases, AI PHẢI đọc các file sau để có đủ ngữ cảnh:

| File cần đọc | Mục đích |
|:-------------|:---------|
| File Feature tương ứng (`wiki/[project]/features/`) | Lấy logic nghiệp vụ, luồng đi, ràng buộc dữ liệu |
| API Spec liên quan (`wiki/[project]/api_specs/`) | Lấy method, endpoint, payload, response, error contract cho test API nếu có |
| `wiki/[project]/operations/environments.md` | Lấy URL, tài khoản test mẫu thực tế |
| `wiki/[project]/operations/test_data.md` | Lấy dữ liệu test mẫu (SĐT, thẻ, payload) |
| Các file bug liên quan (`wiki/[project]/bugs_knowledge/`) | Bổ sung Regression Test Cases từ lỗi cũ |
| `WIKI_RULES.md` (file này) | Tuân thủ định dạng và quy tắc đặt tên |

Mỗi Test Case BẮT BUỘC ghi rõ:
- **AC/Req Cover:** Requirement ID (`R1`, `R2`...) và/hoặc Acceptance Criteria/BDD Scenario được cover (`AC-01`, `Scenario 1`...).
- **Phạm vi:** `UI`, `API`, `Functional`, `UI+Functional`, `API+Functional`, `UI+API`, hoặc `E2E`.
- **Loại case:** `Positive` hoặc `Negative`. Nếu là regression/security/performance thì vẫn phải nêu rõ positive/negative theo kỳ vọng hành vi.
- **Kỹ thuật test:** Ví dụ `Happy Path`, `Equivalence Partitioning`, `Boundary Value Analysis`, `Decision Table`, `State Transition`, `Error Guessing`, `Security`, `Regression`.
- **Nguồn:** Chỉ ghi `Explicit từ [nguồn]` cho test case bám trực tiếp từ Requirement/AC/API Spec đã mô tả rõ.
- **Không suy diễn:** Không tạo test case từ giả định hoặc suy luận. Mọi điểm chưa rõ phải đưa về `## ❓ Câu hỏi chưa rõ` của Feature Spec hoặc `## ❓ Câu hỏi API chưa rõ` của API Spec.
- **Không sinh TC từ câu hỏi mở:** Nếu TC phụ thuộc vào câu hỏi chưa trả lời, không ghi vào bảng Test Cases; ghi vào `Blocked Coverage`, Feature Questions hoặc API Spec Questions. Khi câu hỏi được trả lời, cập nhật Feature Spec/API Spec trước rồi mới sinh TC.
- **API TC:** Chỉ tạo khi có API Spec explicit hoặc câu trả lời `Answered` nêu rõ method/endpoint/auth/header/request/response/status/error. Nếu thiếu status code, payload, error response hoặc side effect thì ghi question/blocked coverage, không tự đoán theo convention REST.
- **Traceability:** Không tạo test case nếu không truy ngược được về Requirement/AC rõ ràng; test API phải truy ngược thêm về API ID trong API Spec.

### 3.5. File Feature Group (`wiki/[project]/feature_groups/`) — Group MOC

Mỗi Feature Group page PHẢI chứa:
1. **Metadata:** `tags: [qa/feature-group-index, qa/feature-group/[slug]]`, `status`, `project`, `feature_group`.
2. **Tổng quan:** mục đích group, phạm vi nghiệp vụ, raw source chính.
3. **Feature Specs trong group:** bảng link Feature, vai trò, status, Gate.
4. **API Specs trong group:** bảng link API Spec, feature cover, API/interface cover, open questions, status.
5. **Test Suites trong group:** bảng link Test Suite, số TC, blocked coverage, status.
6. **Test Plan / Release liên quan:** link tới plan/release nếu có.
7. **Open Questions & Blocked Coverage:** tổng hợp link tới các feature/API Spec/test suite còn question/blocker.
8. **Impact & Regression Notes:** nơi tổng hợp change impact cấp group.
9. **Changelog:** mọi cập nhật group page.

---

## 📄 4. QUY TẮC CÁC FILE ĐIỀU KHIỂN

### 4.1. `index.md` — Bản đồ điều hướng
- Liệt kê TẤT CẢ các trang trong wiki kèm link `[[...]]` và mô tả 1 dòng.
- Phân loại theo: Feature Groups, Features, API Specs, Test Suites, Bugs, Operations.
- AI đọc file này ĐẦU TIÊN khi xử lý bất kỳ câu hỏi nào.
- Cập nhật ngay khi có trang mới được tạo.

### 4.2. `KANBAN.md` — Bảng Kanban & Quy trình Quản lý Task
- **Sự đồng bộ 2 chiều (Markdown ➔ Kanban UI):** File `KANBAN.md` được lưu dưới dạng danh sách gạch đầu dòng Markdown nhưng hiển thị dưới dạng bảng Kanban kéo thả trên Obsidian. AI cập nhật file bằng cách chỉnh sửa danh sách text, con người tương tác qua giao diện kéo thả.
- **Cấu trúc cột chuẩn:** Bảng gồm 3 cột tương ứng với các tiêu đề Markdown của plugin Kanban:
  - `## TODO`: Hàng đợi kiểm thử.
  - `## InProgress`: Các task đang thực hiện hoặc bị nghẽn.
  - `## Done`: Các task đã pass test hoàn toàn.
- **Quy tắc ghi Task & Quản lý ID (AI & Con người):**
  - **Task từ dự án (Specs/Tickets - active testing):** Bắt buộc thừa hưởng nguyên vẹn ID gốc của dự án (ví dụ: `JIRA-xxx`, `TICKET-xxx`) để đồng bộ với Dev/PO.
    - Cú pháp: `- [ ] [[raw_sources/[project]/tasks/MÃ-TASK|MÃ-TASK]] ➔ [[wiki/[project]/test_suites/test_tên_feature|Test Suite Tên Tính Năng]] [Độ_ưu_tiên]`.
    - *Ví dụ:* `- [ ] <raw_sources/[project]/tasks/[task-code]> ➔ <wiki/[project]/test_suites/test_[feature]> [High]`.
  - **Task Kế hoạch kiểm thử (Test Plans):** Dành cho việc chuẩn bị và duyệt chiến lược test.
    - Cú pháp: `- [ ] [QA Internal] [[wiki/[project]/test_plans/testplan_xxx|Test Plan Mã]] ➔ Mô tả công việc`.
    - *Ví dụ:* `- [ ] [QA Internal] <wiki/[project]/test_plans/testplan_cr_[id]> ➔ Review chiến lược & chuẩn bị data test Staging`.
  - **Task đợt triển khai Go-Live (Releases/Deploy):** Dành cho quy trình deploy và nghiệm thu Production.
    - Cú pháp: `- [ ] [Release] [[wiki/[project]/releases/cr_xxx|Mã-CR]] ➔ Phối hợp deploy & chạy Smoke Test Prod [Ngày]`.
    - *Ví dụ:* `- [ ] [Release] <wiki/[project]/releases/cr_[id]_golive_[ddMMyyyy]> ➔ Phối hợp deploy & chạy Smoke Test Production [30/05/2026]`.
  - **Task sửa lỗi (Bug Reports):** Sử dụng trực tiếp mã lỗi của dự án.
    - Cú pháp: `- [ ] [[wiki/bugs_knowledge/bug_tên_lỗi|BUG-xxx]] ➔ Kiểm thử lại lỗi [Độ_ưu_tiên]`.
  - **Task bị nghẽn (Blocked):** Nếu task đang test bị nghẽn do phát sinh bug, bắt buộc ghi kèm mã bug dạng link ở cuối thẻ để dễ truy vết: `... ➔ Test Suite [High] (🔴 [[wiki/bugs_knowledge/bug_tên_lỗi|BUG-xxx]])`.
- **Luồng cập nhật tự động của AI:**
  - **Khi Khởi tạo Sprint (Sprint planning & Setup):** AI tự động tạo 3 loại thẻ công việc liên quan và phân bổ vào đúng cột trạng thái:
    - **Thẻ Kế hoạch kiểm thử (`[QA Internal] testplan_...`)**: Đặt dưới cột `## InProgress` (vì QA Lead sẽ triển khai viết chiến lược và chuẩn bị dữ liệu test ngay lập tức ở đầu Sprint).
    - **Thẻ kịch bản chạy test (`[Mã-Task] ➔ Test Suite...`)**: Đặt dưới cột `## TODO` (chờ Dev code xong và bàn giao bản build trên Staging).
    - **Thẻ đợt triển khai Go-Live (`[Release] cr_...`)**: Đặt dưới cột `## TODO` (đóng vai trò cột mốc Milestone theo dõi thời hạn phát hành cuối Sprint).
  - **Khi nạp Specs mới lẻ (Ingest):** AI tự động chèn một dòng check-list chạy test mới vào dưới cột `## TODO` trong `KANBAN.md`.
  - **Khi đồng bộ Daily Note (Daily Sync):** AI đọc Daily Note của ngày hôm đó, nếu thấy task được báo đã hoàn thành hoặc bị nghẽn, AI phải chủ động di chuyển dòng check-list tương ứng sang cột `## Done` hoặc `## InProgress` trong `KANBAN.md`.
- KHÔNG ghi Changelog trong file này để giữ bảng Kanban luôn sạch đẹp. Mọi thay đổi trạng thái được ghi nhận tại `log.md`.

### 4.3. `log.md` — Nhật ký hệ thống
- Ghi chép TOÀN BỘ hành động AI thực hiện theo thời gian thực để đảm bảo tính truy vết (Audit Trail).
- **Quy tắc sắp xếp:** Bắt buộc xếp dòng nhật ký **Mới nhất lên đầu tiên** (ngay dưới dòng tiêu đề `---` ở phần nội dung) để dễ theo dõi tức thì mà không cần cuộn chuột xuống đáy file.
- Format bắt buộc: `- [YYYY-MM-DD HH:mm:ss] [action-type] | Mô tả ngắn gọn`
  - *Ví dụ:* `- [2026-05-23 10:25:20] [lint-sync] | Hoàn thành quét hệ thống...`
- Các action-type: `[ingest]`, `[task-update]`, `[sync-daily]`, `[lint]`, `[lint-sync]`, `[test-progress]`, `[test-run]`, `[test-blocked]`, `[create]`

### 4.5. Quy tắc Git vận hành

- Sau mỗi batch xử lý (ingest/task-update/daily-sync/lint-sync), AI bắt buộc chạy kiểm tra thay đổi bằng `git status`.
- Commit theo lô nhỏ, message rõ nghiệp vụ, ví dụ:
  - `docs: update feature spec for CR-ORANGE-200`
  - `test: add regression cases for BUG-123`
- Không sửa hoặc revert các thay đổi ngoài phạm vi yêu cầu hiện tại.
- Chỉ push khi người dùng yêu cầu hoặc khi quy trình kết thúc và đã được xác nhận.


### 4.4. Changelog (trong từng file feature, API spec & test suite)
- BẮT BUỘC ghi nhận MỌI thay đổi nội dung của tài liệu nghiệp vụ và kịch bản test.
- **Quy tắc sắp xếp:** Bắt buộc xếp dòng thay đổi **Mới nhất lên đầu tiên** của bảng Changelog (dưới dòng tiêu đề cột `|:---|...`).
- Format bảng tiêu chuẩn: `| Thời gian | Version | Nội dung thay đổi | Nguồn |`
  - Trường **Thời gian** phải ghi đầy đủ: `YYYY-MM-DD HH:mm:ss` để phục vụ cho các phiên bản thay đổi nhanh trong ngày.
  - *Ví dụ:* `| 2026-05-23 10:10:29 | v1.0 | Khởi tạo Specs | <raw_sources/[project]/tasks/[task-code]> |`
- Nguồn phải tham chiếu rõ ràng bằng link liên kết: Mã Task Jira, Daily Note, hoặc tên file PDF gốc.

### 4.6. Update Propagation Checklist

Khi có thay đổi requirement/task/test case, AI phải kiểm tra và cập nhật đủ các nơi liên quan:
- `raw_sources/[project]/...`: lưu raw task/PDF/converted markdown nếu có nguồn mới.
- `wiki/[project]/features/`: cập nhật Requirement/AC, Questions, Impact Analysis, Regression Proposal, Test Coverage, Changelog.
- `wiki/[project]/api_specs/`: cập nhật API contract explicit, API Questions, API Test Coverage, Changelog và link Feature/Test Suite nếu API/interface thay đổi.
- `wiki/[project]/feature_groups/`: cập nhật group page nếu feature/API Spec/test suite thuộc group được thêm, đổi tên, deprecated hoặc thay đổi trạng thái.
- `wiki/[project]/test_suites/`: add/update/deprecate TC theo Feature/API Spec đã duyệt, cập nhật Blocked Coverage, Regression Impact, tổng số TC, Changelog.
- `wiki/[project]/test_plans/`: cập nhật In-Scope, Regression Scope, Coverage và Entry/Exit Criteria nếu phạm vi test thay đổi.
- `KANBAN.md`: cập nhật thẻ, trạng thái và số lượng TC nếu có thay đổi số TC.
- `index.md`: thêm/xóa link khi có page mới hoặc archive.
- `log.md`: ghi một dòng audit cho batch thay đổi với timestamp `UTC+07:00`.
- `git status`: kiểm tra thay đổi cuối batch, không revert file ngoài phạm vi.


## AI Knowledge Scope

- Allowed scope: `wiki/`, `raw_sources/`, `templates/`, `.claude/commands/`, `.claude/scripts/`, va cac file control root.
- Excluded by default: `.obsidian/`, `.smart-env/`, `.karate_cache/`, `.git/`, plugin/cache/db.
- Khong suy dien requirement/AC/API/test case tu du lieu nam ngoai allowed scope.
- Neu thong tin chua ro thi dua vao Question va Blocked Coverage.
- Timezone chuan: `Asia/Saigon` (`UTC+07:00`).
- Encoding chuan: UTF-8, khong mojibake.
