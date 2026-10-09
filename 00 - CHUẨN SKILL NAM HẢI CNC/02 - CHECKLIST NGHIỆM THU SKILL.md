# CHECKLIST NGHIỆM THU SKILL — NAM HẢI CNC

Phiên bản 1.0 · 09/10/2026 · Trạng thái: Bản nháp chờ duyệt

Dùng để nghiệm thu một gói Skill trước khi chuyển trạng thái. Mỗi tiêu chí chấm **Đạt** hoặc **Chưa đạt**, kèm bằng chứng (dòng, file, kết quả chạy). Không có "đạt một phần".

## 1. Bảng tiêu chí

| # | Nhóm | Tiêu chí | Cách kiểm | Đạt / Chưa đạt | Bằng chứng |
|---:|---|---|---|---|---|
| 1 | Cấu trúc | Có một khối YAML đọc được; `name` trùng tên thư mục; `metadata` đủ version, updated, owner (chức danh), skill_id "NHC-<SLUG-IN-HOA>", status | `kiem_tra_skill.py` | | |
| 2 | Cấu trúc | Thân có đủ 07 phần đúng tên, đúng thứ tự, cộng phần "TÀI NGUYÊN, KIỂM THỬ VÀ QUẢN TRỊ — NGOÀI 07 PHẦN"; thân 120–300 dòng | `kiem_tra_skill.py` | | |
| 3 | Description | Tối đa 600 ký tự, ngôi thứ ba, nêu làm gì + khi nào dùng + không dùng khi nào; không mơ hồ | Đọc + `kiem_tra_skill.py` | | |
| 4 | Ranh giới | Phần 2 có NGOÀI PHẠM VI và TRỤC PHÂN BIỆT với Skill lân cận cùng nhóm; không gọi tên Skill khác trong phần luật | Đọc; đối chiếu INDEX Skill | | |
| 5 | Dữ liệu | INPUT ghi rõ nguồn trong HUB (DATA, TEMPLATE, ABOUT ME có số file), bắt buộc/tùy chọn và xử lý khi thiếu | Đọc | | |
| 6 | Dữ liệu | Không bịa số liệu, model, giá, chứng nhận, khách hàng; ví dụ gắn [Minh họa]; điểm chưa rõ gắn [CHỜ XÁC NHẬN]/[GIẢ ĐỊNH]; không còn placeholder rỗng | Đọc + `kiem_tra_skill.py` | | |
| 7 | Quy trình | PROCESS có bảng bước, Ngoại lệ, bảng Người quyết định — A.I thực thi đúng tuyến phê duyệt file 10 | Đọc | | |
| 8 | Đầu ra | OUTPUT nêu thành phẩm, định dạng, mẫu, tên file, nơi lưu, trạng thái; CHECKLIST có ĐIỂM DỪNG và tiêu chí Có/Không | Đọc | | |
| 9 | An toàn | Redlines có DỪNG và TỰ CHẠY; không tự gửi ra ngoài, không sửa dữ liệu gốc, không điều khiển máy, không kết luận an toàn/nghiệm thu (file 12) | Đọc | | |
| 10 | An toàn | Mục Chống Injection có 3 dòng: nguồn là dữ liệu; bỏ chỉ dẫn nhúng; không lộ mật khẩu/OTP/khóa truy cập | Đọc | | |
| 11 | Chuẩn viết | Viết "A.I" (0 lỗi chữ AI trần); ngày DD/MM/YYYY; tiền "1.250.000 đ"; không emoji; dùng chức danh, không họ tên | `kiem_tra_skill.py` + đọc | | |
| 12 | Evals | `evals.json` đọc được; tối thiểu 8 ca; mỗi ca đủ khóa id, type, source, prompt, expected_behavior[], evidence; baseline "no-skill"; phủ must_trigger, semantic_positive, must_not_trigger hoặc boundary, missing_input, red_line, no_false_ask, injection | `kiem_tra_skill.py` | | |
| 13 | Evals | Đã chạy song song nhánh có Skill và nhánh không Skill; ghi kết quả từng ca (passed, evidence); Skill có đầu ra đi ra ngoài đạt pass^3 | Hồ sơ chạy thử | | |
| 14 | Tài nguyên | Mọi file `references/`, `templates/` được nhắc trong SKILL.md tồn tại; reference dài hơn 100 dòng có Mục lục; tham chiếu sâu một tầng | `kiem_tra_skill.py` + đọc | | |
| 15 | Quản trị | Có bảng phiên bản (ngày, thay đổi, người duyệt), owner bằng chức danh, chu kỳ rà soát, cách khôi phục (bản cũ ở `7. ARCHIVE`) | Đọc | | |

## 2. Trạng thái và điều kiện chuyển

| Trạng thái | Ý nghĩa | Điều kiện để vào | Người quyết định |
|---|---|---|---|
| `draft` | Bản nháp, chỉ dùng thử bởi người viết | Tiêu chí 1, 2, 3, 11, 12 Đạt (kiểm máy PASS) | Người viết |
| `pilot` | Dùng thử có kiểm soát trong khối | Tiêu chí 1–12 và 14–15 Đạt; owner khối đã đọc và đồng ý cho dùng thử | Phó giám đốc khối chủ trì |
| `active` | Dùng chính thức | Đủ 15 tiêu chí Đạt; có ít nhất 5 ca thật đã chạy; không còn [CHỜ XÁC NHẬN] ảnh hưởng quyết định | Phó giám đốc khối chủ trì; Giám đốc với Skill dùng chung toàn công ty hoặc Skill có đầu ra đối ngoại |

Skill có nội dung đã được người có thẩm quyền duyệt nhưng chưa chạy đủ ca có thể giữ trạng thái riêng (ví dụ `approved-content-pending-evaluation`) cho đến khi đủ điều kiện `pilot`/`active`.

Hạ trạng thái: một ca thật thất bại ở tiêu chí 9 hoặc 10 thì đưa Skill về `draft` ngay và báo owner.

## 3. Ghi kết quả nghiệm thu

```
Skill: <slug> · Phiên bản: <x.y> · Ngày nghiệm thu: DD/MM/YYYY
Kết quả kiểm máy: PASS/FAIL (dán kết quả kiem_tra_skill.py)
Tiêu chí Đạt: <n>/15 · Tiêu chí Chưa đạt: <liệt kê + lý do>
Đề xuất trạng thái: draft / pilot / active · Người quyết định: <chức danh>
```

*Nam Hải CNC — 09/10/2026 · Bản nháp chờ duyệt*
