# QUY TẮC LẬP HỢP ĐỒNG GIAO VIỆC CHO TRỢ LÝ A.I

## Mục lục
1. Nguyên tắc
2. Bảng quyền ba mức
3. Dữ liệu
4. Điểm dừng
5. Người duyệt
6. Nhật ký
7. Bộ ca thử
8. Vòng đời

## 1. Nguyên tắc
- Một hợp đồng cho một việc có kết quả và người chịu trách nhiệm rõ; việc khác thì hợp đồng khác.
- Câu lệnh hay tên trợ lý không thay hợp đồng. Khả năng của công cụ không phải là quyền được giao.
- Quyền chưa ghi là không có. A.I không có thẩm quyền duyệt, gửi ra ngoài hay đổi dữ liệu gốc (file 10, mục 8).

## 2. Bảng quyền ba mức
| Mức | Ví dụ [Minh họa] | Điều kiện |
|---|---|---|
| Được làm | Tra cứu tài liệu đã duyệt; soạn bản nháp; tổng hợp; đối chiếu và nêu chỗ lệch | Trong phạm vi và nguồn đã nêu |
| Làm khi có người duyệt | Ghi vào hồ sơ làm việc; đề xuất cập nhật dữ liệu; chuẩn bị bản gửi | Người duyệt xem từng lần |
| Không được làm | Gửi ra ngoài; sửa giá, hợp đồng, chính sách, cấu hình máy; điều khiển thiết bị; kết luận an toàn; xác nhận nghiệm thu hoặc bảo hành; duyệt ngoại lệ | Không mở bằng lời nói |

## 3. Dữ liệu
Ghi từng nguồn: tên, chủ dữ liệu, mức nhạy cảm, đọc hay ghi, quyền dùng. Không đưa vào: mật khẩu, OTP, khóa truy cập, dữ liệu cá nhân nhạy cảm, bí mật thương vụ khi chưa có người cho phép (file 12, nguyên tắc 7). Không chép thông số hay điều khoản từ dự án cũ.

## 4. Điểm dừng
Trợ lý dừng và hỏi người khi: thiếu dữ kiện quyết định; hai nguồn mâu thuẫn; việc vượt phạm vi; có nội dung kỹ thuật hoặc an toàn; liên quan giá, chiết khấu, tiến độ, hợp đồng, bảo hành; có thông tin khách hàng nhạy cảm; gặp chỉ dẫn lạ trong tài liệu. Ghi sẵn câu trợ lý sẽ nói và người nhận.

## 5. Người duyệt
| Loại đầu ra | Người duyệt |
|---|---|
| Nội dung kỹ thuật, cấu hình, vận hành | Kỹ thuật |
| Giá, chiết khấu, tiến độ, hợp đồng, bảo hành | Người có thẩm quyền thương mại theo file 10 |
| Mua sắm, đặt hàng | Mua hàng theo tuyến phê duyệt |
| Đối ngoại quan trọng, chính sách | Giám đốc |
Một loại đầu ra không có người duyệt thì trợ lý không được tạo loại đó.

## 6. Nhật ký
Ghi: thời điểm, người yêu cầu, nguồn đã đọc, đầu ra, người duyệt và kết quả duyệt, lỗi, lần dừng. Không ghi bí mật. Nêu nơi lưu, người xem, thời gian lưu.

## 7. Bộ ca thử
Tối thiểu: đúng việc; thiếu dữ liệu; ngoài phạm vi; bị đòi quyền cao; tài liệu chứa chỉ dẫn lạ; việc đã giao rõ (không hỏi lại thừa). Tiêu chí đạt đặt trước khi thử và không đổi theo kết quả.

## 8. Vòng đời
Phiên bản, ngày hiệu lực, ngày rà soát, tạm dừng khi có sự cố hoặc đổi dữ liệu, thu hồi quyền, ngừng dùng, lưu hay xóa nhật ký. Mọi thay đổi quyền là một phiên bản mới có người duyệt.
