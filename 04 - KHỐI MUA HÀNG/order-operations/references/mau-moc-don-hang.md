# Mẫu mốc đơn hàng và chứng từ theo giai đoạn

Khung khởi đầu cho đơn thiết bị nhập khẩu và đơn phụ tùng. Điều chỉnh theo điều kiện giao hàng ghi trên PO; mốc không áp dụng thì ghi "không áp dụng" kèm lý do.

| # | Mốc | Chứng từ/bằng chứng cần có | Người giữ việc mặc định |
|---|---|---|---|
| 1 | Phát hành PO và nhà cung cấp xác nhận | PO đã duyệt, xác nhận đơn hoặc PI | Nhân viên Mua hàng |
| 2 | Thanh toán đặt cọc (nếu có) | Chứng từ thanh toán theo điều kiện PO | Kế toán, Mua hàng đề nghị |
| 3 | Bắt đầu sản xuất | Xác nhận từ nhà cung cấp | Nhân viên Mua hàng |
| 4 | Hoàn tất sản xuất và kiểm tra trước giao | Ảnh, video, biên bản kiểm tra nếu có | Mua hàng, Kỹ thuật xem nội dung kỹ thuật |
| 5 | Xuất hàng | Hóa đơn thương mại, danh sách đóng gói, vận đơn | Nhân viên Mua hàng quốc tế |
| 6 | Vận chuyển quốc tế | Vận đơn, lịch tàu hoặc chuyến | Mua hàng quốc tế |
| 7 | Thông quan | Tờ khai, HS code đúng chứng từ, CO, CQ nếu yêu cầu | Mua hàng, Kế toán |
| 8 | Vận chuyển nội địa và nhập kho | Phiếu nhập kho, biên bản kiểm đếm | Nhân viên kho, Cung ứng |
| 9 | Giao hàng đến khách hoặc hiện trường | Phiếu giao hàng | Kinh doanh phối hợp, Cung ứng |
| 10 | Bàn giao cho Kỹ thuật lắp đặt | Phiếu bàn giao kỹ thuật | Mua hàng bàn giao, Kỹ thuật nhận |

## Quy tắc tính trễ
- Độ lệch = ngày dự kiến trừ ngày cam kết, tính bằng ngày lịch; số dương là trễ.
- Nguy cơ trễ khi mốc trước chưa hoàn tất mà mốc sau đã gần ngày cam kết; ghi là Suy luận.
- Không cập nhật trạng thái hoàn tất khi chưa có bằng chứng từ nguồn.

## Chứng từ hay gây chậm
- Mã hàng hoặc số lượng trên hóa đơn khác PO.
- Thiếu CO hoặc CQ khi PO hoặc quy định yêu cầu.
- Mô tả hàng và HS code không thống nhất giữa các chứng từ.
- Thiếu thông tin điều kiện giao hàng (Incoterms) hoặc địa điểm giao.
