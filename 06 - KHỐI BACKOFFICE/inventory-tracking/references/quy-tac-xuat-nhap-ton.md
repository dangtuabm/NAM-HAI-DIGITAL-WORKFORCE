# QUY TẮC XUẤT – NHẬP – TỒN, TUỔI TỒN VÀ BẢO QUẢN — NAM HẢI CNC

Bản đề xuất [GIẢ ĐỊNH] chờ Phó giám đốc Backoffice xác nhận. Không thay thế quy trình kho và chuẩn mực kế toán do Kế toán tổng hợp áp dụng.

## Mục lục
1. Nguyên tắc chung
2. Chủng loại và khóa mã
3. Cân đối, kiểm kê và tuổi tồn
4. Chi phí lưu kho
5. Rủi ro bảo quản theo chủng loại
6. Cảnh báo và người nhận

## 1. Nguyên tắc chung
- Chỉ đọc bản xuất hoặc bản sao; mọi chênh lệch là đề xuất cho người có quyền.
- Một mã là một dòng; không gộp mã gần giống, không suy mã thay thế (file 04, mục 1.2).
- Tồn khả dụng = tồn thực tế − hàng đã giữ cho đơn có chứng từ − hàng không bán được (hỏng chờ xử lý, bảo hành chờ trả).

## 2. Chủng loại và khóa mã
| Chủng loại | Đơn vị theo dõi | Khóa nhận dạng | Ghi chú |
|---|---|---|---|
| MÁY — máy nguyên chiếc (laser, hàn laser, chấn CNC, xén tôn thủy lực, đột, bào rãnh V, gấp, lốc, cán CZ, robot) | Chiếc | Hãng, model, serial, cấu hình | Theo dõi từng serial; trạng thái: khả dụng / đã giữ cho đơn / trưng bày / gửi tại khách |
| DCH — cụm dây chuyền (DECK, xả tấm, xẻ băng, xả cuộn) | Bộ, cụm | Mã cấu hình, danh mục kiện | Nhiều kiện một bộ: kiểm đủ kiện |
| PK — phụ kiện | Theo mã | Mã hàng của hãng | Gắn hãng và model áp dụng theo tài liệu |
| PT — phụ tùng | Theo mã | Mã hàng của hãng | Không suy dùng chung giữa model |
| VT — vật tư tiêu hao (bép cắt, lăng kính, kính bảo vệ...) | Theo mã, quy cách đóng gói | Mã hàng, lô | Theo lô để xuất trước nhập trước |

## 3. Cân đối, kiểm kê và tuổi tồn

### 3.1. Cân đối
Tồn đầu kỳ + Nhập trong kỳ − Xuất trong kỳ = Tồn cuối kỳ theo sổ. Lệch hoặc âm: đánh dấu LỖI CÂN ĐỐI, liệt kê chứng từ của mã.

### 3.2. Đối chiếu kiểm kê
| Kết quả | Điều kiện | Việc tiếp |
|---|---|---|
| KHỚP | Sổ = đếm | Không |
| THỪA | Đếm > sổ | Tìm phiếu nhập chưa ghi; Kế toán quyết điều chỉnh |
| THIẾU | Đếm < sổ | Tìm phiếu xuất chưa ghi, hàng gửi khách; Kế toán quyết điều chỉnh |

Nguyên nhân luôn ghi là Suy luận đến khi có chứng từ.

### 3.3. Tuổi tồn
- Tính từ ngày nhập của lô hoặc serial đến ngày chốt.
- Nhóm tuổi đề xuất [GIẢ ĐỊNH]: dưới 90 ngày · 90–180 · 181–365 · trên 365.
- Ứ đọng: không phát sinh xuất trong số ngày theo ngưỡng Phó giám đốc Backoffice duyệt; chưa có ngưỡng thì liệt kê nhóm trên 180 ngày kèm nhãn GIẢ ĐỊNH.
- Hàng đã giữ cho đơn có chứng từ không xếp vào ứ đọng.

## 4. Chi phí lưu kho
Các khoản cần Kế toán cung cấp nếu muốn lượng hóa: thuê kho hoặc khấu hao mặt bằng, điện, nhân công kho, bảo hiểm hàng, vật tư bảo quản, hao hụt và hư hỏng, vốn nằm trong hàng tồn. Không có số liệu thì chỉ đề xuất định tính.

Hướng giảm chi phí đề xuất (chờ người quyết):
- Xếp vị trí theo tần suất xuất: vật tư tiêu hao xuất nhiều đặt gần cửa.
- Xuất trước nhập trước theo lô cho vật tư tiêu hao.
- Rà ứ đọng định kỳ, trình người có thẩm quyền phương án xử lý.
- Giảm hàng gửi tại khách không có biên bản.

## 5. Rủi ro bảo quản theo chủng loại
| Chủng loại | Rủi ro thường gặp | Việc kiểm đề xuất | Căn cứ |
|---|---|---|---|
| Máy nguyên chiếc | Ẩm, gỉ bề mặt dẫn hướng, bụi vào tủ điện | Che phủ, kiểm định kỳ theo hướng dẫn hãng | Tài liệu hãng; Kỹ thuật xác nhận |
| Quang học laser (lăng kính, kính bảo vệ, đầu cắt) | Bụi, vân tay, ẩm, va đập | Giữ nguyên bao gói, kho khô, không mở hộp khi chưa dùng | Tài liệu hãng |
| Phụ tùng cơ khí | Gỉ, va đập | Bôi bảo quản nếu hãng yêu cầu, kệ riêng | Tài liệu hãng |
| Linh kiện điện, điện tử | Ẩm, tĩnh điện | Bao chống ẩm, chống tĩnh điện | Tài liệu hãng |
| Vật tư có hạn dùng (keo, dầu, khí) | Quá hạn | Theo dõi lô và hạn | Nhãn sản phẩm |

Không ghi trị số nhiệt độ, độ ẩm nếu tài liệu hãng chưa có; ghi "cần Kỹ thuật xác nhận".

## 6. Cảnh báo và người nhận
| Cảnh báo | Điều kiện | Người nhận |
|---|---|---|
| THIẾU HỤT | Tồn khả dụng bằng 0 hoặc dưới mức tối thiểu Mua hàng đã duyệt | Phó giám đốc Mua hàng |
| ĐÃ GIỮ HẾT | Toàn bộ tồn đã giữ cho đơn | Phó giám đốc Mua hàng, Kinh doanh |
| Ứ ĐỌNG | Theo mục 3.3 | Phó giám đốc Backoffice; Giám đốc nếu cần quyết xả |
| LỆCH KIỂM KÊ | Mục 3.2 | Kế toán tổng hợp |
| RỦI RO BẢO QUẢN | Mục 5 | Nhân viên kho, Kỹ thuật |
