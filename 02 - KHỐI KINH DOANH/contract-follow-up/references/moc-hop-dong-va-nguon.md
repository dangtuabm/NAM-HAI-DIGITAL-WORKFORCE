# Chuỗi mốc hợp đồng, khối chủ quản và quy tắc trạng thái

Nguồn: chuỗi triển khai 8 bước (ABOUT ME file 08, mục 1), dữ liệu bắt buộc của giao dịch (file 04, mục 2), vai trò chức năng và phân quyền (file 10, mục 7 và 8), nguyên tắc làm việc với A.I (file 12). Chuỗi mốc dưới đây là đề xuất [GIẢ ĐỊNH]; Phó giám đốc Kinh doanh xác nhận hoặc điều chỉnh theo mẫu hợp đồng đang dùng.

## 1. Chuỗi mốc chuẩn M1–M12
| Mốc | Tên mốc | Khối chủ quản dữ liệu | Bằng chứng để ghi HOÀN THÀNH |
|---|---|---|---|
| M1 | Khách xác nhận đặt hàng | Kinh doanh | Hợp đồng đã ký hai bên hoặc PO của khách |
| M2 | Nhận tạm ứng hoặc đặt cọc đợt 1 (nếu hợp đồng có) | Backoffice | Bảng công nợ phải thu ghi đã thu, có ngày chốt |
| M3 | Đặt hàng với nhà cung cấp | Mua hàng | PO gửi nhà cung cấp đã duyệt, có xác nhận của nhà cung cấp |
| M4 | Hàng sẵn sàng tại nhà cung cấp | Mua hàng | Thông báo hoàn tất sản xuất hoặc kiểm tra trước giao |
| M5 | Vận chuyển và thông quan (hàng nhập khẩu) | Mua hàng | Vận đơn, tờ khai đã thông quan |
| M6 | Hàng về kho Nam Hải CNC hoặc giao thẳng tới khách | Mua hàng, kho Backoffice | Phiếu nhập kho hoặc biên bản giao hàng |
| M7 | Khách sẵn sàng mặt bằng, điện, khí, nước | Kỹ thuật xác nhận với khách | Biên bản khảo sát hoặc xác nhận hạ tầng |
| M8 | Lắp đặt và căn chỉnh | Kỹ thuật | Báo cáo lắp đặt có ngày, người thực hiện |
| M9 | Chạy thử không tải và có tải | Kỹ thuật | Biên bản chạy thử có số đo theo tiêu chí đã thống nhất |
| M10 | Đào tạo vận hành | Kỹ thuật | Biên bản đào tạo có xác nhận của khách |
| M11 | Nghiệm thu và bàn giao | Kỹ thuật, người có thẩm quyền hai bên | Biên bản nghiệm thu đã ký |
| M12 | Thu hết công nợ | Backoffice | Bảng công nợ phải thu ghi còn phải thu bằng 0, có ngày chốt |

Đợt thanh toán giữa các mốc (ví dụ trước giao hàng, sau nghiệm thu, giữ lại bảo hành) lấy đúng theo điều khoản hợp đồng; mỗi đợt là một dòng trong lịch thanh toán, gắn với mốc kích hoạt.

## 2. Quy tắc trạng thái
| Trạng thái | Điều kiện |
|---|---|
| HOÀN THÀNH | Có bằng chứng ở cột cuối bảng mục 1 |
| ĐÚNG HẠN | Chưa xong, ngày dự kiến của khối chủ quản không vượt ngày cam kết |
| CHÚ Ý | Còn trong ngưỡng nhắc trước hạn, hoặc ngày dự kiến vượt cam kết nhưng chưa tới ngày cam kết |
| TRỄ | Đã qua ngày cam kết mà chưa có bằng chứng hoàn thành |
| CHƯA CÓ DỮ LIỆU | Khối chủ quản chưa cập nhật, hoặc cập nhật cũ hơn ngưỡng |

Độ lệch = ngày dự kiến (hoặc ngày chốt nếu chưa có dự kiến) trừ ngày cam kết, tính bằng ngày lịch. Ghi rõ cách tính trong sổ.

## 3. Ngưỡng mặc định [GIẢ ĐỊNH — chờ Phó giám đốc Kinh doanh xác nhận]
- Nhắc trước hạn mốc: 7 ngày lịch.
- Nguồn coi là cũ: không có cập nhật quá 7 ngày lịch với mốc đang chạy.
- Khoản thu: nhắc trước ngày đến hạn 5 ngày lịch; quá hạn từ ngày kế tiếp ngày đến hạn.

## 4. Quy tắc nhắc định kỳ
- Lịch do người dùng quy định (ví dụ [Minh họa] sáng thứ Hai hằng tuần); không tự đặt lịch.
- Người nhận nội bộ theo danh sách Phó giám đốc Kinh doanh duyệt; ghi chức danh.
- Thứ tự nội dung: việc cần hành động trong kỳ → mốc trễ → mốc sắp đến hạn → khoản sắp đến hạn hoặc quá hạn thu → mốc thiếu dữ liệu và khối cần cập nhật.
- Không có thay đổi so với kỳ trước vẫn gửi bản nhắc ngắn ghi "không có thay đổi", kèm ngày chốt.

## 5. Ranh giới với các khối
- Mua hàng theo dõi PO với nhà cung cấp; sổ này chỉ đọc kết quả ở góc khách hàng.
- Kỹ thuật kiểm bằng chứng đóng việc; sổ này chỉ ghi trạng thái theo biên bản.
- Backoffice đối soát công nợ; sổ này chỉ ghi số đã đối soát.
