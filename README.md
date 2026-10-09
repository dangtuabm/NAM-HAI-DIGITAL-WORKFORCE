# NAM HẢI DIGITAL WORKFORCE

Kho **86 Skill A.I** cho đội ngũ số của **Nam Hải CNC** (thiết bị gia công kim loại), chia theo 7 nhóm chức năng. Mỗi Skill là một năng lực đóng gói chuẩn gồm `SKILL.md` (7 phần), `evals.json` (ca kiểm thử) và tài nguyên đi kèm (`references/`, `templates/`, `scripts/`, `assets/`) nếu có.

> Phiên bản **2.0 · 09/10/2026** · Trạng thái: **BẢN NHÁP — CHỜ DUYỆT**. Đầu ra của mỗi Skill là bản dự thảo; người có trách nhiệm kiểm tra và duyệt trước khi dùng, gửi hoặc công bố.

## Số lượng theo nhóm

| # | Nhóm | Số Skill |
|---|---|---:|
| 01 | CEO · Giám đốc | 11 |
| 02 | Khối Kinh doanh | 18 |
| 03 | Marketing | 12 |
| 04 | Khối Mua hàng | 10 |
| 05 | Khối Kỹ thuật | 11 |
| 06 | Khối Backoffice | 10 |
| 07 | Toàn công ty · Dữ liệu A.I & Văn hóa | 14 |
| | **Tổng** | **86** |

## Cấu trúc kho

- `01 … 07 - …/` — các nhóm Skill theo khối chức năng.
- `00 - INDEX KHO SKILL NAM HAI CNC - v2.0 - …md` — danh mục đầy đủ 86 Skill, ưu tiên và ranh giới giữa các Skill dễ chồng việc.
- `00 - CHUẨN SKILL NAM HẢI CNC/` — khung chuẩn 7 phần, mẫu `evals`, bộ kiểm `kiem_tra_skill.py`.
- `00 - SO DO DIGITAL WORKFORCE/` — sơ đồ tương tác **Nam Hải CNC Digital Workforce** (`nam-hai-cnc-digital-workforce.html`): chuỗi giá trị 7 khối, drill-down từng khối, bấm vào từng Skill để xem mô tả.

## Cách dùng

1. Đọc bộ **ABOUT ME** của Nam Hải CNC trước khi dùng bất kỳ Skill nào (nguồn thông tin chuẩn về công ty, sản phẩm, khách hàng, tổ chức).
2. Chọn Skill theo việc cần làm (xem INDEX hoặc mở sơ đồ Digital Workforce).
3. Nạp `SKILL.md` của Skill đó vào trợ lý A.I, cung cấp dữ liệu đầu vào theo yêu cầu, rà đầu ra trước khi dùng.

## Nguyên tắc & ranh giới

- Mỗi Skill ghi rõ **LÀM GÌ · DÙNG KHI · KHÔNG DÙNG ĐỂ**. Tôn trọng phần ranh giới để A.I không vượt thẩm quyền.
- Dữ liệu nhạy cảm (tài sản, thuế, doanh thu, dòng tiền, hợp đồng, thông tin cá nhân) tuân theo phân loại **Xanh – Vàng – Đỏ**; không đưa dữ liệu Đỏ lên công cụ A.I ngoài.

---

*Thiết kế bởi **ABM** cho Nam Hải CNC · Bản nháp phục vụ triển khai nội bộ.*
