# QUY CHUẨN LÀM SẠCH DỮ LIỆU — TRA CỨU

Đọc ở Bước 4. Căn cứ: ABOUT ME file 04, 07, 11, 12.

## 1. Quy chuẩn tên file
`YYYYMMDD_<khối>_<loại>_<nội-dung>_v<số>`; khối: backoffice, kinh-doanh, mua-hang, ky-thuat. Chữ thường, gạch nối, không dấu, không khoảng trắng. Bản sạch thêm `_sach`. Ví dụ [Minh họa]: `20261006_ky-thuat_anh-model_may-chan_v1`.

## 2. Quy chuẩn giá trị
| Loại | Quy tắc |
|---|---|
| Ngày | DD/MM/YYYY |
| Tiền | VNĐ dạng 1.250.000 đ hoặc 1,25 tỷ; ghi rõ có/không thuế nếu nguồn có |
| Hãng | Viết theo danh sách nhà cung cấp trong file 07; hãng lạ giữ nguyên, đánh dấu chưa đối chiếu |
| Model, mã hàng | Giữ nguyên ký tự, không đoán ký tự mờ |
| Đơn vị, trị số, dung sai | Giữ nguyên; quy đổi phải ghi gốc, công thức, kết quả |
| Tên nhóm sản phẩm | Theo bảng tên chuẩn file 11 (Máy chấn CNC, Máy xén tôn thủy lực, Dây chuyền DECK...) |
| Chức vụ | Dùng chức danh theo file 10, không ghi họ tên cá nhân |

## 3. Mức tin cậy khi đọc ảnh
Rõ: đọc được toàn bộ ký tự. Mờ: có ký tự không chắc, ghi [?] đúng chỗ. Không đọc được: không ghi giá trị. Mọi dòng từ ảnh mang nhãn "chưa xác nhận" cho đến khi Kỹ thuật đối chiếu tài liệu hãng.

## 4. Mẫu nghi vấn thường gặp
Trùng mã khác giá; cùng model viết hai cách; đơn vị lẫn (mm/m, VNĐ/nghìn); ô gộp che dữ liệu; dòng tổng lẫn trong bảng; ngày ghi kiểu tháng/ngày.
