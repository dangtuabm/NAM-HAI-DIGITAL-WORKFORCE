# TRƯỜNG CHUẨN VÀ BỘ CHỈ SỐ KHỞI ĐẦU — NAM HẢI CNC

Đọc ở bước 3 và 4. Đây là khung và đề xuất ban đầu; không có con số, mục tiêu hay ngưỡng nào ở đây. Mọi nguồn dữ liệu nêu là [GIẢ ĐỊNH] cần chủ sở hữu xác nhận. Chủ sở hữu ghi theo chức danh (file 10).

## Mục lục
1. Trường chuẩn của một chỉ số
2. Quy tắc đặt tên và biến thể
3. Bộ chỉ số khởi đầu theo bốn khối
4. Điểm hay lệch
5. Quy tắc thay đổi định nghĩa

## 1. Trường chuẩn của một chỉ số

| Trường | Nội dung |
|---|---|
| Mã và tên chuẩn | Ví dụ KD-01 Doanh số ký hợp đồng |
| Định nghĩa | Một câu, không dùng từ cảm tính |
| Công thức | Tử số, mẫu số, phép tính; điều kiện bao gồm và loại trừ |
| Đơn vị | VNĐ, ngày, phần trăm, số lượng; ngoại tệ ghi rõ |
| Nguồn dữ liệu | Hệ thống hoặc tệp, người cấp, quyền truy cập |
| Kỳ đo và mốc cắt | Tuần, tháng, quý; ngày cắt dữ liệu |
| Mốc sự kiện | Với chỉ số thời gian: sự kiện bắt đầu và kết thúc, người xác nhận |
| Chủ sở hữu | Chức danh chịu trách nhiệm định nghĩa |
| Người xác nhận số | Người xác nhận con số trước khi báo cáo |
| Tần suất | Tuần, tháng, theo giao dịch |
| Phiên bản và ngày hiệu lực | Số bản, DD/MM/YYYY |
| Trạng thái | Nháp, chờ xác nhận, đã chốt, chưa dùng được |

## 2. Quy tắc đặt tên và biến thể

- Một tên một nghĩa. Khái niệm có nhiều cách tính thì mỗi cách một tên riêng (ví dụ doanh số ký hợp đồng, doanh số ghi nhận theo hóa đơn, doanh số đã thu tiền).
- Tên chỉ số nội bộ không gợi cam kết với khách.
- Viết "A.I" nếu nhắc; chỉ số đo kết quả chuyên môn không dùng chữ cảm tính.

## 3. Bộ chỉ số khởi đầu theo bốn khối

Danh sách đề xuất để các khối chọn, sửa hoặc bỏ. Cột "Nguồn có thể" là giả định.

| Khối | Chỉ số đề xuất | Hướng định nghĩa | Nguồn có thể [GIẢ ĐỊNH] | Chủ sở hữu đề xuất |
|---|---|---|---|---|
| Kinh doanh | Doanh số ký hợp đồng | Tổng giá trị hợp đồng và phụ lục có hiệu lực ký trong kỳ, nêu rõ có hay không thuế | Hợp đồng đã duyệt | Phó giám đốc Kinh doanh |
| Kinh doanh | Doanh số ghi nhận theo hóa đơn | Tổng giá trị hóa đơn đầu ra trong kỳ, cơ sở do Kế toán tổng hợp xác nhận | Sổ kế toán | Kế toán tổng hợp |
| Kinh doanh | Tỷ lệ chuyển đổi báo giá thành hợp đồng | Số báo giá dẫn đến hợp đồng chia số báo giá đã gửi cùng nhóm kỳ | Sổ báo giá | Phó giám đốc Kinh doanh |
| Backoffice, Kinh doanh | Biên lợi nhuận gộp theo giao dịch | (Doanh thu giao dịch trừ giá vốn đã xác nhận) chia doanh thu giao dịch; nêu rõ các khoản vào giá vốn | Kế toán, hồ sơ mua | Kế toán tổng hợp |
| Mua hàng | Thời gian từ đặt hàng đến hàng về kho | Ngày hàng nhập kho trừ ngày PO được gửi nhà cung cấp, theo ngày dương lịch | PO, phiếu nhập kho | Phó giám đốc Mua hàng |
| Mua hàng | Tỷ lệ lô hàng đủ chứng từ khi về | Số lô có đủ CO, CQ và chứng từ cần thiết chia tổng số lô về | Hồ sơ lô hàng | Phó giám đốc Mua hàng |
| Kinh doanh, Kỹ thuật | Thời gian giao hàng cho khách | Ngày giao tại điểm thỏa thuận trừ ngày hợp đồng có hiệu lực hoặc ngày khách thanh toán trước, tùy hợp đồng; chọn một mốc bắt đầu và đặt tên riêng | Hợp đồng, biên bản giao nhận | Phó giám đốc Kinh doanh |
| Kỹ thuật | Thời gian từ giao hàng đến nghiệm thu | Ngày biên bản nghiệm thu ký trừ ngày giao; chỉ tính khi có biên bản | Biên bản nghiệm thu | Trưởng nhóm kỹ thuật theo nhóm |
| Kỹ thuật | Thời gian phản hồi sau bán | Thời điểm người phụ trách ghi nhận phản hồi đầu tiên trừ thời điểm tiếp nhận yêu cầu có đủ dữ liệu; tách phản hồi đầu tiên và xử lý xong | Sổ yêu cầu sau bán | Trưởng nhóm kỹ thuật |
| Kỹ thuật | Tỷ lệ yêu cầu sau bán đóng trong kỳ | Số yêu cầu có xác nhận đóng chia số yêu cầu mở trong kỳ | Sổ yêu cầu sau bán | Trưởng nhóm kỹ thuật |
| Backoffice | Số ngày công nợ phải thu | Công nợ phải thu cuối kỳ chia doanh thu kỳ nhân số ngày kỳ; nêu cơ sở doanh thu | Sổ công nợ | Kế toán tổng hợp |

Thời hạn phản hồi hay bảo hành cam kết với khách chỉ theo hợp đồng của từng giao dịch; chỉ số nội bộ không thay thế (file 08, mục 2).

## 4. Điểm hay lệch

- Doanh số tính theo hợp đồng, theo hóa đơn hay theo tiền thu.
- Thời gian giao hàng: bắt đầu từ ngày ký, ngày thanh toán trước hay ngày đặt hàng nhà cung cấp; kết thúc tại kho khách hay tại cảng.
- Thời gian phản hồi: ngày dương lịch hay ngày làm việc; đếm từ lúc khách gọi hay lúc đủ dữ liệu.
- Biên lợi nhuận: giá vốn có gồm phí nhập khẩu, vận chuyển, lắp đặt, bảo hành không.
- Ngoại tệ: quy đổi theo tỷ giá ngày nào và nguồn nào.

## 5. Quy tắc thay đổi định nghĩa

Không đổi định nghĩa giữa kỳ mà không có nhật ký. Mỗi thay đổi ghi: định nghĩa cũ, mới, lý do, ngày hiệu lực, người xác nhận, ảnh hưởng đến số lịch sử (có so sánh được hay không). Số kỳ trước tính theo định nghĩa cũ phải gắn nhãn.

*Nam Hải CNC — 06/10/2026 · Bản nháp chờ duyệt*
