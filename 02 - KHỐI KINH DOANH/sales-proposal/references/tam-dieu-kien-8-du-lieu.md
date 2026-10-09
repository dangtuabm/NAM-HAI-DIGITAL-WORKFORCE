# Tám dữ liệu bắt buộc khi chào một sản phẩm cụ thể

Nguồn: ABOUT ME Nam Hải CNC, file 04, mục 2 (dữ liệu bắt buộc), mục 3 (ranh giới); file 07 (nhà cung cấp); file 08 (dịch vụ sau bán). Mỗi báo giá hoặc đề xuất kiểm đủ 8 mục cho từng sản phẩm được chào.

## 1. Bảng kiểm
| # | Dữ liệu | Nguồn chính | Người xác nhận | Dấu hiệu THIẾU |
|---|---|---|---|---|
| 1 | Hãng, model và mã cấu hình | Dữ liệu Kỹ thuật; tài liệu nhà cung cấp | Kỹ thuật | Chỉ có tên nhóm máy; model do A.I đoán |
| 2 | Thông số kỹ thuật và điều kiện áp dụng | Tài liệu nhà cung cấp; Kỹ thuật | Kỹ thuật | Thông số lấy từ hình ảnh hoặc dự án cũ; thiếu điều kiện đo |
| 3 | Phụ kiện, vật tư và phạm vi cung cấp | Báo giá, cấu hình Kỹ thuật | Kỹ thuật, Kinh doanh | Không nêu cái gì có, cái gì không bao gồm |
| 4 | Xuất xứ theo chứng từ | CO, CQ, chứng từ nhà cung cấp | Mua hàng | Xuất xứ suy từ tên hãng hoặc từ dự án khác |
| 5 | Giá, thuế và điều kiện thanh toán | Báo giá đã được duyệt | Người có thẩm quyền thương mại | Giá điền tạm; thuế chưa rõ |
| 6 | Tiến độ giao hàng, lắp đặt, chạy thử, nghiệm thu | Mua hàng (giao hàng); Kỹ thuật (lắp đặt, chạy thử) | Mua hàng, Kỹ thuật | Tiến độ không có mốc hoặc không có điều kiện |
| 7 | Bảo hành, bảo trì và trường hợp loại trừ | Hồ sơ giao dịch đã duyệt | Người có thẩm quyền thương mại | Điều khoản chép từ dự án khác |
| 8 | Điều kiện mặt bằng, điện, khí, nước và an toàn liên quan | Khảo sát hiện trường | Kỹ thuật | Chưa khảo sát hoặc khách chưa xác nhận |

## 2. Trạng thái từng mục
- ĐỦ: có nguồn, ngày, người xác nhận.
- CHỜ XÁC NHẬN: có dữ liệu nhưng chưa có người xác nhận.
- THIẾU: chưa có dữ liệu; ghi người cần cung cấp.

Còn mục THIẾU hoặc CHỜ thì không ghi đề xuất ở trạng thái sẵn sàng gửi.

## 3. Ranh giới nhắc lại
- Danh mục nhóm sản phẩm không xác nhận mọi model đều có sẵn.
- Không dùng thông số của dự án này cho dự án khác.
- Không suy đoán khả năng thay thế giữa các model của phụ kiện, phụ tùng.
- Phạm vi cuối cùng của từng giao dịch do báo giá, hợp đồng và phụ lục đã duyệt quy định.
