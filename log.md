---
tags: [log, system]
status: Done
created: 2026-05-23
---

- [2026-05-24 12:00:00] [lint-sync] | Enhance verify debug output: TC/API errors now include line number, cell count, section context, actual cell values; KANBAN mismatch shows per-section breakdown; duplicate TC ID detection added; API row open-ref check added.
- [2026-05-24 11:30:00] [lint-sync] | Fix verify: is_test_case_row now requires ≥9 pipes to exclude Blocked Coverage table rows; fix fix_test_suites.py to clear cells[2] when marking 🚫 Blocked and check Phạm vi in header line only; fix TC-VAS-019 swapped Loại case/Kỹ thuật test; 0 governance errors remain.
- [2026-05-24 11:30:00] [lint-sync] | Add Unreadable Source Rule to WIKI_RULES.md §1.6 and wiki-requirement-analyzer guardrails: any inaccessible link in raw source must be logged as ❓ Chưa đọc được in Nguồn tài liệu + Open question in Câu hỏi chưa rõ.
- [2026-05-24 11:30:00] [task-update] | Add missing ℹ️ qc_setup back-link in hasaki_receiving_po_app Mối quan hệ section; QC ↔ Receiving PO inter-feature relationships now complete across all 6 features.

- [2026-05-24 10:29:12] [lint-sync] | Tighten lint-and-sync command: safe verify-first behavior, Gate 4 sync rule, API Spec section checks, API suite link checks, and mojibake guardrail.

- [2026-05-24 10:17:55] [lint-sync] | Add API Spec artifact model: separate api_specs docs, API test scopes, no-inference API TC guardrails, and verify support for API scopes.

- [2026-05-24 09:55:56] [lint-sync] | Add Feature Group MOC structure for Hasaki receiving-po and update rules/templates/verify to require group pages for qa/feature-group tags.
- [2026-05-24 09:49:16] [lint-sync] | Update governance guardrails: question lifecycle, no-inference testcase policy, impact/regression matrix, UTF-8/timezone verify, and expanded wiki_sync verify.
- [2026-05-23 00:40:00] [create] | Tạo Dashboard tiến độ progress_dashboard — tự động hiển thị Feature/Test Suite còn chờ Gate 1/Gate 2 qua Obsidian Dataview theo tag #qa/feature-group/receiving-po.
- [2026-05-23 00:35:00] [lint-sync] | Bổ sung tag nhóm tính năng `#qa/feature-group/receiving-po` vào 6 Feature Specs và 6 Test Suites project_hasaki. Cập nhật WIKI_RULES.md §1.3 (quy tắc Feature Group Tag) + templates/tpl_requirement.md + tpl_test_suite.md.
- [2026-05-23 00:30:00] [ingest] | Khởi tạo Test Suite #6/6: [[wiki/project_hasaki/test_suites/test_hasaki_qc_evaluation|test_hasaki_qc_evaluation]] — 34 test cases (TC-QCE-001–TC-QCE-034). Coverage: R1–R25, AC-01–AC-10. Status: Draft — chờ Gate 2.
- [2026-05-23 00:25:00] [ingest] | Khởi tạo Test Suite #5/6: [[wiki/project_hasaki/test_suites/test_hasaki_qc_setup|test_hasaki_qc_setup]] — 32 test cases (TC-QCS-001–TC-QCS-032). Coverage: R1–R24, AC-01–AC-10. Status: Draft — chờ Gate 2.
- [2026-05-23 00:20:00] [ingest] | Khởi tạo Test Suite #4/6: [[wiki/project_hasaki/test_suites/test_hasaki_receiving_packing_list|test_hasaki_receiving_packing_list]] — 27 test cases (TC-PL-001–TC-PL-027). Coverage: R1–R20, AC-01–AC-07. Status: Draft — chờ Gate 2.
- [2026-05-23 00:15:00] [ingest] | Khởi tạo Test Suite #3/6: [[wiki/project_hasaki/test_suites/test_hasaki_receiving_vas|test_hasaki_receiving_vas]] — 27 test cases (TC-VAS-001–TC-VAS-027). Coverage: R1–R21, AC-01–AC-08. Status: Draft — chờ Gate 2.
- [2026-05-23 00:10:00] [ingest] | Khởi tạo Test Suite #2/6: [[wiki/project_hasaki/test_suites/test_hasaki_receiving_po_app|test_hasaki_receiving_po_app]] — 42 test cases (TC-PO-001–TC-PO-042). Coverage: R1–R24, AC-01–AC-10. Status: Draft — chờ Gate 2.
- [2026-05-23 00:09:00] [ingest] | Khởi tạo Test Suite #1/6: [[wiki/project_hasaki/test_suites/test_hasaki_receiving_inbound_shipment|test_hasaki_receiving_inbound_shipment]] — 25 test cases (TC-INB-001–TC-INB-025). Coverage: R1–R20, AC-01–AC-10. Status: Draft — chờ Gate 2.
- [2026-05-23 00:08:00] [lint-sync] | Chuẩn hóa quy tắc liên kết Feature ↔ Feature: bổ sung quy tắc `Mối quan hệ` vào WIKI_RULES.md §1.3 và thêm trường tương ứng vào templates/tpl_requirement.md. Áp dụng cho 6 feature specs project_hasaki đã tạo.
- [2026-05-23 00:06:00] [ingest] | Khởi tạo Feature Spec #6/6 từ PDF v1.5 (07105_Quality_Control_Docs_ver1.5.pdf): [[wiki/project_hasaki/features/hasaki_qc_evaluation|hasaki_qc_evaluation]] — 25 Requirement IDs (R1–R25), 10 Acceptance Criteria, 5 câu hỏi chưa rõ. Status: Draft — chờ Gate 1.
- [2026-05-23 00:05:00] [ingest] | Khởi tạo Feature Spec #5/6 từ PDF v1.5 (07105_Quality_Control_Docs_ver1.5.pdf): [[wiki/project_hasaki/features/hasaki_qc_setup|hasaki_qc_setup]] — 24 Requirement IDs (R1–R24), 10 Acceptance Criteria, 5 câu hỏi chưa rõ. Status: Draft — chờ Gate 1.
- [2026-05-23 00:04:00] [ingest] | Khởi tạo Feature Spec #4/6 từ PDF v2.17 (07062_Receiving_PO_Docs_ver2.17.pdf): [[wiki/project_hasaki/features/hasaki_receiving_packing_list|hasaki_receiving_packing_list]] — 20 Requirement IDs (R1–R20), 7 Acceptance Criteria, 5 câu hỏi chưa rõ. Status: Draft — chờ Gate 1.
- [2026-05-23 00:03:00] [ingest] | Khởi tạo Feature Spec #3/6 từ PDF v2.17 (07062_Receiving_PO_Docs_ver2.17.pdf): [[wiki/project_hasaki/features/hasaki_receiving_vas|hasaki_receiving_vas]] — 21 Requirement IDs (R1–R21), 8 Acceptance Criteria, 5 câu hỏi chưa rõ. Status: Draft — chờ Gate 1.
- [2026-05-23 00:02:00] [ingest] | Khởi tạo Feature Spec #2/6 từ PDF v2.17 (07062_Receiving_PO_Docs_ver2.17.pdf): [[wiki/project_hasaki/features/hasaki_receiving_po_app|hasaki_receiving_po_app]] — 24 Requirement IDs (R1–R24), 10 Acceptance Criteria, 5 câu hỏi chưa rõ. Status: Draft — chờ Gate 1.
- [2026-05-23 00:01:00] [ingest] | Khởi tạo Feature Spec #1/6 từ PDF v2.17 (07062_Receiving_PO_Docs_ver2.17.pdf): [[wiki/project_hasaki/features/hasaki_receiving_inbound_shipment|hasaki_receiving_inbound_shipment]] — 20 Requirement IDs (R1–R20), 10 Acceptance Criteria, 5 câu hỏi chưa rõ. Status: Draft — chờ Gate 1 (PO/QA Lead duyệt).
- [2026-05-23 00:00:00] [create] | Khởi tạo Test Plan tháng 5/2026 cho project_hasaki: [[wiki/project_hasaki/test_plans/testplan_hasaki_2026_05|testplan_hasaki_2026_05]] — status Draft, golive TBD, scope chờ ingest 2 PDF requirements.
- [2026-05-23 15:36:00] [create] | Bổ sung thẻ Kanban [QA Internal] cho `project_hasaki` vào cột InProgress — nhắc điền environments & test_data trước khi nhận task đầu tiên.
- [2026-05-23 15:35:00] [create] | Khởi tạo dự án mới `project_hasaki`: Tạo đầy đủ cấu trúc thư mục chuẩn (features, test_suites, test_plans, releases, bugs_knowledge, operations, daily_notes), 3 file vận hành tối thiểu ([[wiki/project_hasaki/operations/environments|environments]], [[wiki/project_hasaki/operations/test_data|test_data]], [[wiki/project_hasaki/operations/team_contacts|team_contacts]]), thư mục raw_sources và cập nhật index.md.
- [2026-05-23 15:32:00] [lint-sync] | Nâng cấp bộ quy chuẩn vận hành WIKI_RULES.md: Tích hợp triết lý Human-in-the-Loop (HITL) và thiết lập 5 Cổng kiểm soát (Gate 1 đến Gate 5) phê duyệt bắt buộc trên toàn chu kỳ kiểm thử.
- [2026-05-23 15:27:00] [create] | Khởi tạo trọn bộ tính năng Quên mật khẩu OrangeHRM: Ticket CR-ORANGE-205, Specs orangehrm_forgot_password (Bước A - Analysis), và Test Suite test_orangehrm_forgot_password (Bước B - Design). *(project đã xóa)*
- [2026-05-23 15:26:00] [lint-sync] | Triển khai cặp đôi Custom Skills chuẩn ISTQB: `wiki-requirement-analyzer` (Test Analysis) và `wiki-test-designer` (Test Design), tích hợp vào WIKI_RULES.md và nâng cấp verify_wiki.py đạt 100% compliant.


- [2026-05-23 15:06:40] [sync-daily] | Đồng bộ thành công Daily Note ngày [[wiki/project_orange/operations/daily_notes/2026-05-24.md]].

- [2026-05-23 15:06:40] [test-blocked] | Đồng bộ Kanban: Task project_orange bị nghẽn (🔴 Đính kèm bug BUG-OH-888).

- [2026-05-23 15:06:40] [create] | Tự động tạo Bug RCA từ Standup Blocked: Loi nut dang nhap khong click duoc (BUG-OH-888). *(project đã xóa)*

- [2026-05-23 15:06:23] [lint-sync] | Đồng bộ Kanban thành công: Đã chuyển 1 Test Suites sang 'Passed' và Features sang 'Done' (test_orangehrm_auth).

- [2026-05-23 15:06:08] [lint-sync] | Đồng bộ Kanban thành công: Đã chuyển 1 Test Suites sang 'Passed' và Features sang 'Done' (test_orangehrm_auth).

# 📅 Nhật Ký Hoạt Động — QA LLM Wiki

> Ghi chép tự động mọi hoạt động của AI và người dùng trên hệ thống theo thời gian thực (Audit Trail).

---

- [2026-05-23 14:58:00] [lint-sync] | Hoàn tất tái cấu trúc dự án tự quản (Self-Contained Multi-Project): Di chuyển phân vùng 'bugs_knowledge' và 'operations' vào riêng từng dự án, tách biệt 100% môi trường, data test, danh bạ nhân sự, cập nhật liên kết và nâng cấp scripts/verify_wiki.py đạt 100% compliant.
- [2026-05-23 14:50:00] [lint-sync] | Chuẩn hóa toàn bộ WIKI_RULES.md, đồng bộ hóa các đường dẫn thư mục thực tế (releases, test_plans), tích hợp bộ lọc kiểm định tự động trong scripts/verify_wiki.py đạt 100% compliant.
- [2026-05-23 14:44:15] [task-update] | Đồng bộ Kanban: Bổ sung thẻ Kế hoạch kiểm thử [QA Internal] vào InProgress và thẻ Triển khai Production [Release] vào TODO để theo dõi toàn diện đợt phát hành CR-ORANGE-200.
- [2026-05-23 14:39:50] [lint-sync] | Hoàn tất tái cấu trúc Multi-Project toàn diện: Tách biệt tri thức thành 'project_demo' và 'project_orange', chuẩn hóa phân vùng 'test_plans' và 'releases' độc lập, cập nhật đồng bộ liên kết đồ thị và bảng index.md.
- [2026-05-23 14:38:35] [create] | Khởi tạo Mẫu Kế hoạch Kiểm thử [[templates/tpl_test_plan|tpl_test_plan]] và cập nhật Mẫu Go-Live [[templates/tpl_cr_golive|tpl_cr_golive]] theo mô hình tách biệt tĩnh/động chuẩn QA.
- [2026-05-23 14:36:10] [test-progress] | Task CR-ORANGE-200 đã chuyển sang InProgress trên Kanban. Đã tự động cập nhật trạng thái kiểm thử test_orangehrm_auth.md sang 'Testing'.
- [2026-05-23 14:35:40] [create] | Khởi tạo trọn bộ tính năng Đăng nhập & Đăng xuất OrangeHRM: Ticket orangehrm_auth, Specs orangehrm_auth, Test Suite test_orangehrm_auth, Kế hoạch Test testplan_cr_orange_200 và Biên bản Go-Live cr_orangehrm_golive_30052026 cho ngày 30/05/2026. *(project đã xóa)*
- [2026-05-23 14:32:15] [create] | Khởi tạo Biên bản Nghiệm thu CR Go-Live đầu tiên cr_CR101_golive_23052026 sử dụng mô hình Hybrid mới. *(project đã xóa)*
- [2026-05-23 14:31:45] [create] | Khởi tạo Mẫu Biên bản Đóng gói CR Go-Live Hybrid [[templates/tpl_cr_golive|tpl_cr_golive]] tích hợp Test Plan Staging và Kịch bản Vận hành Production.
- [2026-05-23 14:30:10] [lint-sync] | Cập nhật [[WIKI_RULES|WIKI_RULES.md]] bổ sung quy chuẩn đặt tên file và Quy trình 2.6: Đóng gói & Nghiệm thu CR Go-Live.
- [2026-05-23 10:38:09] [test-run] | Hoàn thành toàn bộ kiểm thử JIRA-101. Đã tự động cập nhật 5/5 kịch bản test thành PASS, đổi trạng thái Specs & Test Suite thành 'evergreen' sau khi task được lưu trữ (Archived) trên Kanban.
- [2026-05-23 10:29:33] [task-update] | Đồng bộ thay đổi JIRA-101: Cập nhật Specs (auth_login) mật khẩu tối thiểu 10 ký tự, thêm TC-005 vào Test Suite (test_auth_login) và reset trạng thái kiểm thử sang 'testing'.
- [2026-05-23 10:22:34] [test-progress] | Task JIRA-101 đã chuyển sang InProgress trên Kanban. Đã tự động cập nhật trạng thái kịch bản test test_auth_login.md sang 'testing'.
- [2026-05-23 10:21:11] [lint-sync] | Hoàn thành quét hệ thống. Đã tự động đồng bộ trạng thái Kanban và sửa lỗi định dạng tag cho 3 file environments.md, test_data.md, và team_contacts.md sang #qa/operations.
- [2026-05-23 10:10:29] [create] | Khởi tạo trọn bộ tính năng mẫu Đăng nhập Email: Ticket JIRA-101, Specs auth_login, Test Suite test_auth_login, và Kanban Task. *(project đã xóa)*
- [2026-05-23 09:57:06] [create] | Khởi tạo hệ thống QA LLM Wiki. Tạo cấu trúc thư mục, templates, và các file điều khiển.
