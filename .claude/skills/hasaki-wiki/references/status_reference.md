---
tags: [wiki-rules, reference]
status: Done
created: 2026-05-24
---

# 📊 Status Reference — Trạng thái hợp lệ theo từng loại tài liệu

Tài liệu tham chiếu nhanh cho AI và QA team. Mọi giá trị `status:` trong frontmatter và bảng phải nằm trong danh sách này.

---

## 1. Feature Spec (`features/`)

| Status | Ý nghĩa | Điều kiện chuyển |
|:-------|:--------|:-----------------|
| `Draft` | Đang soạn thảo, chưa được duyệt | Mặc định khi tạo mới |
| `Done` | Đã được PO/QA Lead duyệt | **Gate 1**: có đủ `approved_by` · `approved_at` · `approval_note` |

> Không được dùng: `Approved`, `Active`, `Review`, `Final`.

---

## 2. API Spec (`api_specs/`)

| Status | Ý nghĩa | Điều kiện chuyển |
|:-------|:--------|:-----------------|
| `Draft` | Đang soạn thảo, chờ xác nhận contract | Mặc định khi tạo mới |
| `Done` | Contract đã xác nhận, đồng bộ với Feature Spec | **Gate 1**: cùng approval với Feature Spec liên kết |

---

## 3. Test Suite (`test_suites/`)

| Status | Ý nghĩa | Điều kiện chuyển |
|:-------|:--------|:-----------------|
| `Draft` | Test cases đang thiết kế, chưa review | Mặc định khi tạo mới |
| `Testing` | Đã được QA Lead duyệt, đang chạy test | **Gate 2**: có đủ `approved_by` · `approved_at` · `approval_note` |
| `Passed` | Toàn bộ TC pass (hoặc blocked được chấp nhận) | **Gate 4**: người dùng xác nhận kết quả thực tế |
| `Failed` | Có TC fail chưa được xử lý | Khi có TC fail sau Gate 4 |

---

## 4. Test Plan (`test_plans/`)

| Status | Ý nghĩa | Điều kiện chuyển |
|:-------|:--------|:-----------------|
| `Draft` | Đang lập kế hoạch test | Mặc định khi tạo mới |
| `Testing` | Sprint đang chạy test | Khi bắt đầu test execution |
| `Passed` | Sprint test hoàn tất, tất cả TC pass | **Gate 4** + **Gate 5** (Production smoke test pass) |
| `Outdated` | Test Plan không còn áp dụng (CR bị hủy, sprint cũ) | Khi bị supersede hoặc cancel |

---

## 5. CR / Release (`releases/`)

| Status | Ý nghĩa | Điều kiện chuyển |
|:-------|:--------|:-----------------|
| `Draft` | Đang chuẩn bị go-live | Mặc định khi tạo |
| `Testing` | Staging test đã pass, đang chuẩn bị deploy | Khi Staging PASS |
| `Done` | Đã deploy Production và smoke test PASS | **Gate 5**: PO + QA Lead ký duyệt |

---

## 6. Bug (`bugs_knowledge/`)

| Status | Ý nghĩa | Điều kiện chuyển |
|:-------|:--------|:-----------------|
| `Open` | Bug mới phát hiện, chờ fix | Mặc định khi tạo; **Gate 3** (Bug Triage) xác nhận hợp lệ |
| `Fixed` | Dev đã fix, chờ retest | Dev báo fix xong |
| `Retest` | QA đang retest | QA bắt đầu retest |
| `Closed` | Retest pass, bug đã giải quyết | QA xác nhận pass |

> Tag tương ứng: `#qa/bug/open` khi Open/Fixed/Retest; `#qa/bug/fixed` khi Closed.

---

## 7. Feature Group (`feature_groups/`)

| Status | Ý nghĩa |
|:-------|:--------|
| `Draft` | Group page đang cập nhật, có feature chưa `Done` |
| `Done` | Tất cả Feature Specs trong group đã `Done` |

---

## 8. Test Case (individual — cột Status trong bảng TC)

| Icon | Ý nghĩa |
|:-----|:--------|
| `⏳` | Chưa chạy (pending) |
| `✅` | Pass |
| `❌` | Fail |
| `🚫 Blocked` | Không chạy được do R/AC có question `Open` liên quan trực tiếp |

> `🚫 Blocked` phải được liệt kê trong bảng `## 🚧 Blocked Coverage` của Test Suite.

---

## 9. Câu hỏi chưa rõ (Question lifecycle — cột Trạng thái)

| Trạng thái | Ý nghĩa |
|:-----------|:--------|
| `Open` | Chưa có câu trả lời — **chặn sinh TC** cho R/AC liên quan |
| `Answered` | Đã có câu trả lời chính thức kèm nguồn — cho phép tạo/cập nhật R/AC/TC |
| `Deferred` | Tạm hoãn giải quyết (ví dụ: phạm vi out of sprint) — không chặn TC cho R/AC không liên quan |

---

## 10. KANBAN Card

| Cột | Ý nghĩa |
|:----|:--------|
| `## TODO` | Chưa bắt đầu |
| `## InProgress` | Đang thực hiện |
| `## Done` | Hoàn tất (test passed + wiki synced) |

> KANBAN không dùng `status:` frontmatter — không có Changelog — mọi thay đổi ghi vào `log.md`.

---

## 11. Approval Evidence (bắt buộc cho Gate 1 / Gate 2 / Gate 5)

Khi chuyển status từ `Draft` → `Done`/`Testing` qua Gate 1/2/5, file phải có đủ 3 trường trong frontmatter:

```yaml
approved_by: "Tên người duyệt"
approved_at: "YYYY-MM-DD HH:mm:ss"
approval_note: "Ghi chú ngắn về quyết định duyệt"
```

---

## 12. Raw Task File Hasaki (`raw_sources/project_hasaki/tasks/`)

Raw file không có wiki status lifecycle. Frontmatter `status` phản ánh trạng thái task trên Workplace:

| Giá trị | Nguồn |
|:--------|:------|
| `Todo` | API status = 0 |
| `Processing` | API status = 1 |
| `Done` | API status = 2 |

> Raw file chỉ đọc từ góc nhìn wiki. Cập nhật qua script `hasaki_my_tasks.py`, không sửa tay.

---

## Tổng hợp nhanh

| Loại file | Status hợp lệ |
|:----------|:-------------|
| Feature Spec | `Draft` → `Done` |
| API Spec | `Draft` → `Done` |
| Test Suite | `Draft` → `Testing` → `Passed` / `Failed` |
| Test Plan | `Draft` → `Testing` → `Passed` / `Outdated` |
| CR / Release | `Draft` → `Testing` → `Done` |
| Bug | `Open` → `Fixed` → `Retest` → `Closed` |
| Feature Group | `Draft` → `Done` |
| Test Case (icon) | `⏳` / `✅` / `❌` / `🚫 Blocked` |
| Question | `Open` / `Answered` / `Deferred` |
