# QUY TẮC THIẾT KẾ KẾT NỐI HỆ THỐNG VỚI TRỢ LÝ A.I

## Mục lục
1. Nơi ghi nhận chuẩn
2. Phân loại dữ liệu
3. Mức quyền
4. Điểm kiểm soát và nhật ký
5. Kiểm thử và quay về làm tay

Công cụ nêu dưới đây (Misa, Google Drive, Zalo, Excel) là [GIẢ ĐỊNH] theo khảo sát hiện trạng, cần Backoffice xác nhận. Không khẳng định tính năng hoặc giới hạn của công cụ khi chưa có tài liệu của chính công cụ đó.

## 1. Nơi ghi nhận chuẩn
- Mỗi đối tượng dữ liệu có đúng một nơi ghi nhận chuẩn; các nơi khác chỉ là bản sao hoặc bản làm việc.
- Gợi ý ban đầu để xác nhận: [GIẢ ĐỊNH] thông tin khách và công nợ ở Misa; hồ sơ giao dịch, báo giá, tài liệu kỹ thuật ở Google Drive; Zalo là kênh trao đổi, không phải nơi ghi nhận chuẩn; Excel là bản làm việc.
- Bản làm việc không được ghi đè nơi ghi nhận chuẩn nếu chưa qua người duyệt.

## 2. Phân loại dữ liệu (đề xuất, Giám đốc chốt)
| Nhóm | Ví dụ | Cách xử lý với trợ lý A.I |
|---|---|---|
| Công khai | Danh mục nhóm sản phẩm, thông tin website | Dùng được |
| Nội bộ | Quy trình, mẫu biểu, tài liệu kỹ thuật đã duyệt | Dùng trong phạm vi khối được giao |
| Nhạy cảm thương mại | Giá, chiết khấu, hợp đồng, công nợ, nhà cung cấp | Chỉ khi có người cho phép; che bớt khi không cần |
| Cá nhân và bí mật | Dữ liệu cá nhân, mật khẩu, OTP, khóa truy cập | Không đưa vào luồng |

## 3. Mức quyền
| Mức | Nội dung | Điều kiện |
|---|---|---|
| R0 | Không truy cập | Mặc định cho dữ liệu chưa phân loại |
| R1 | Chỉ đọc, đúng thư mục hoặc nhóm bản ghi | Mặc định khi thử |
| R2 | Soạn bản nháp ở khu vực riêng, không ghi vào nơi ghi nhận chuẩn | Giám đốc duyệt |
| R3 | Ghi vào nơi ghi nhận chuẩn | Từng lần có người duyệt; ghi nhật ký trước–sau |
| R4 | Gửi ra ngoài hoặc xóa | Không cấp cho trợ lý A.I; người thực hiện sau khi duyệt |

## 4. Điểm kiểm soát và nhật ký
- Trước khi ghi hoặc gửi: người có thẩm quyền xem bản đề xuất và xác nhận.
- Nhật ký tối thiểu: thời điểm, người yêu cầu, nguồn dữ liệu đọc, đề xuất tạo ra, người duyệt, kết quả; không ghi mật khẩu hay khóa truy cập.
- "Gửi thành công" khác "đúng nghiệp vụ": sau thao tác cần đối chiếu với nơi ghi nhận chuẩn.

## 5. Kiểm thử và quay về làm tay
- Thử trên bản sao hoặc dữ liệu giả: đọc đúng phạm vi; bị từ chối khi vượt phạm vi; lỗi được ghi lại; không có thao tác ghi ngoài ý muốn.
- Tiêu chí đạt do Giám đốc chốt trước khi thử, không điều chỉnh sau kết quả.
- Quay về làm tay: nêu người thực hiện, các bước thủ công thay thế, cách đối chiếu dữ liệu sau khi ngừng nối.
