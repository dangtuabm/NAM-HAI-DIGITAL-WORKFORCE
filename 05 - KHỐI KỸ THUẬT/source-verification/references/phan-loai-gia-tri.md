# Phân loại giá trị khi đối chiếu nguồn

Nguồn căn cứ: file 04 mục 2–3, file 11 mục 4. Dùng ở bước 3 của quy trình.

## 1. Bốn loại giá trị
| Loại | Là gì | Nguồn hợp lệ | Không được dùng làm |
|---|---|---|---|
| Thông số nhà sản xuất | Giá trị hãng công bố cho model và mã cấu hình | Tài liệu hãng, catalogue hiện hành, thư xác nhận của nhà cung cấp | Cam kết kết quả tại khách |
| Cấu hình chào bán | Phạm vi cung cấp trong báo giá cho một giao dịch | Báo giá đã duyệt | Thông số hãng cho model khác |
| Điều kiện hợp đồng | Điều khoản đã ký: phạm vi, tiến độ, bảo hành, loại trừ | Hợp đồng, phụ lục, biên bản đã ký | Điều khoản của dự án khác |
| Kết quả đo tại khách | Số đo thực tế tại hiện trường | Biên bản chạy thử, phiếu đo có người đo, ngày, dụng cụ | Thông số hãng |

## 2. Quy tắc quyết định
1. Một giá trị chỉ thuộc một loại tại một thời điểm; giá trị hai loại thì tách hai dòng.
2. Giá trị không có hãng, model hoặc mã hàng thì ghi Chưa xác minh.
3. Phụ tùng chỉ Khớp khi mã hàng của phụ tùng nằm trong danh mục tương thích của tài liệu hãng cho đúng model.
4. Lệch giữa cấu hình chào bán và thông số hãng là việc của Kỹ thuật xác nhận.
5. Kết quả đo tại khách chỉ nói về thiết bị và điều kiện đã đo.

## 3. Ví dụ [Minh họa]
- Dòng A: "Độ dày cắt tối đa" của model X, tài liệu hãng phiên bản mới nhất: loại Thông số NSX, kết quả Khớp với báo giá nháp.
- Dòng B: "Bép cắt mã Y dùng cho model Z" chỉ có trong báo giá dự án cũ: kết quả Chưa xác minh, chuyển Mua hàng hỏi nhà cung cấp.
- Dòng C: "Thời gian bảo hành" lấy từ dự án khác: không áp dụng; chỉ lấy từ hợp đồng của giao dịch đang xử lý (file 08 mục 2).
