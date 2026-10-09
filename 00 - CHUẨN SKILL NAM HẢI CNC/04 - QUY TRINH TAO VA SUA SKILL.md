# QUY TRÌNH TẠO VÀ SỬA SKILL — NAM HẢI CNC

Phiên bản 1.0 · 09/10/2026 · Trạng thái: Bản nháp chờ duyệt · Căn cứ phân quyền: `1. ABOUT ME - BỘ NÃO/10_CO_CAU_TO_CHUC_VAI_TRO_PHAN_QUYEN.md`

## 1. Vai trò

| Vai trò | Ai (chức danh) | Việc |
|---|---|---|
| Người đề xuất | Bất kỳ nhân sự nào trong khối, hoặc A.I khi phát hiện việc lặp lại | Ghi đề xuất theo Mục 3; không tự đưa Skill vào kho |
| Người viết | Nhân sự được Phó giám đốc khối giao (có thể dùng A.I hỗ trợ) | Dựng gói theo `01 - KHUNG SKILL 07 PHẦN.md`, chạy `kiem_tra_skill.py` |
| Owner | Phó giám đốc khối chủ trì nghiệp vụ (ghi trong `metadata.owner`) | Chịu trách nhiệm nội dung, rà soát định kỳ, đề xuất nâng trạng thái |
| Người duyệt | Phó giám đốc khối với Skill trong khối; Giám đốc với Skill nhóm 01, nhóm 07 (dùng chung toàn công ty) và Skill có đầu ra đối ngoại quan trọng | Duyệt chuyển `pilot` và `active` theo `02 - CHECKLIST NGHIỆM THU SKILL.md` |
| Duyệt chuyên môn | Kỹ thuật duyệt nội dung kỹ thuật; người có thẩm quyền thương mại duyệt giá, chiết khấu, hợp đồng (file 10 mục 8; file 12 nguyên tắc 8–9) | Xác nhận phần chuyên môn trước khi Skill lên `active` |

A.I không có thẩm quyền phê duyệt, ban hành Skill hay đổi trạng thái (file 10 mục 8).

## 2. Đặt vào nhóm nào

| Nhóm trong `4. SKILL - KỸ NĂNG/` | Đặt khi |
|---|---|
| `01 - CEO - GIÁM ĐỐC` | Người dùng chính là Giám đốc: quyết định, ưu tiên, điều hành |
| `02 - KHỐI KINH DOANH` | Khách hàng, cơ hội, báo giá, hợp đồng bán, chăm sóc trước bán |
| `03 - MARKETING` | Thương hiệu, nội dung, ấn phẩm, slide, kênh truyền thông |
| `04 - KHỐI MUA HÀNG` | Nhà cung cấp, RFQ, đặt hàng, chứng từ, logistics, bóc dữ liệu nhà cung cấp |
| `05 - KHỐI KỸ THUẬT` | Khảo sát, cấu hình, lắp đặt, chạy thử, đào tạo, dịch vụ sau bán, dao/cối |
| `06 - KHỐI BACKOFFICE` | Hành chính, nhân sự, kế toán, tài chính, kho, hồ sơ |
| `07 - TOÀN CÔNG TY - DỮ LIỆU A.I VĂN HÓA` | Năng lực dùng chung nhiều khối: dữ liệu, làm rõ đề bài, quản trị A.I, học tập |

Skill dùng được cho nhiều khối thì đặt ở nhóm 07 và ghi người dùng chính trong phần 1. Skill cá nhân (một người sở hữu duy nhất) đặt ở nhóm của khối người đó, ghi rõ "Skill cá nhân" trong description và phần 1.

## 3. Các bước tạo Skill mới

| Bước | Việc | Người | Đầu ra |
|---|---|---|---|
| 1 | Ghi đề xuất: việc lặp lại nào, ai dùng, đầu vào/đầu ra, Skill lân cận đã có | Người đề xuất | Đề xuất 5–10 dòng gửi owner |
| 2 | Kiểm trùng: tra `00 - INDEX KHO SKILL NAM HAI CNC` xem đã có Skill cùng nhiệm vụ chưa; có thì đề xuất sửa Skill đó (Mục 5) | Người viết | Kết luận tạo mới hay sửa |
| 3 | Đặt slug: chữ thường, không dấu, gạch nối, tối đa 64 ký tự, mô tả nhiệm vụ (ví dụ `lam-ro-nhu-cau`, `pipeline-management`); không đổi slug sau khi đã `pilot` | Người viết | Tên thư mục |
| 4 | Dựng gói theo khung; viết `evals.json` từ `03 - MAU EVALS.json` | Người viết | Gói `draft` |
| 5 | Chạy `python3 "kiem_tra_skill.py" "<đường dẫn Skill>"`; sửa đến khi PASS | Người viết | Kết quả kiểm máy |
| 6 | Chạy bộ ca song song có Skill / không Skill; ghi kết quả | Người viết | Hồ sơ chạy thử |
| 7 | Nghiệm thu theo checklist 15 tiêu chí; quyết định trạng thái | Owner, người duyệt | Biên bản nghiệm thu |
| 8 | Cập nhật INDEX (Mục 6) | Người viết, owner xác nhận | INDEX bản mới |

## 4. Đặt tên và mã

- `name` = slug = tên thư mục.
- `skill_id` = "NHC-" + slug in hoa (ví dụ `NHC-LAM-RO-NHU-CAU`).
- `owner` = "Nam Hải CNC — <chức danh>"; không họ tên.
- Phiên bản: sửa câu chữ, bổ sung ca, chuẩn hóa khung → tăng bậc nhỏ (1.0 → 1.1); đổi quy trình, phạm vi, đầu ra → tăng bậc lớn (1.x → 2.0).

## 5. Sửa Skill đang có

1. Ghi lý do sửa (lỗi thực tế, đổi quy định, đổi công cụ, góp ý của owner).
2. **Lưu bản cũ trước khi sửa:** sao nguyên thư mục Skill vào `7. ARCHIVE - LƯU TẠM TRƯỚC KHI XÓA/4. SKILL/<slug>-v<phiên bản cũ>-<YYYYMMDD>/`; kiểm bản lưu mở được.
3. Sửa trên thư mục Skill hiện hành; giữ nguyên slug.
4. Tăng `version`, cập nhật `updated`, thêm một dòng vào bảng phiên bản (ngày, thay đổi, người duyệt).
5. Chạy lại `kiem_tra_skill.py` và các ca liên quan đến phần sửa.
6. Sửa làm đổi phạm vi hoặc Redlines thì Skill quay về `pilot` cho đến khi người duyệt xác nhận lại.
7. Skill bị thay thế bởi Skill khác: chuyển cả thư mục sang `7. ARCHIVE - LƯU TẠM TRƯỚC KHI XÓA/4. SKILL/`, ghi Skill thay thế trong INDEX; Skill mới ghi "thay thế <slug cũ>" trong mục Gợi ý tra cứu.

Không xóa Skill trực tiếp. Xóa hẳn khỏi ARCHIVE do người có thẩm quyền quyết định.

## 6. Cập nhật INDEX

Mỗi lần thêm, sửa bậc lớn, đổi trạng thái hoặc lưu trữ Skill:
- Cập nhật bảng số lượng theo nhóm và dòng của Skill trong `00 - INDEX KHO SKILL NAM HAI CNC - v<x.y> - <YYYYMMDD>.md`.
- Ghi dòng vào bảng "Thay đổi so với bản trước": Skill, thay đổi, căn cứ (chức danh duyệt).
- Đặt tên file INDEX theo phiên bản mới; bản INDEX cũ chuyển vào `7. ARCHIVE - LƯU TẠM TRƯỚC KHI XÓA`.
- Cập nhật sơ đồ Digital Workforce trong `00 - SO DO DIGITAL WORKFORCE/` khi Skill mới đổi số lượng của nhóm.

## 7. Rà soát định kỳ

Owner rà mỗi Skill `active` khi có lỗi thực tế, khi quy chế/ABOUT ME thay đổi, hoặc theo chu kỳ owner đặt [CHỜ XÁC NHẬN chu kỳ]. Bài học rút ra là đề xuất cho owner; A.I không tự ban hành bản mới.

*Nam Hải CNC — 09/10/2026 · Bản nháp chờ duyệt*
