# TẠO MẪU DÙNG LẠI VÀ KIỂM BẢN IN

Nguồn: bản 0.2 (08/10/2026) của Skill; giữ nguyên quy trình, cập nhật đường dẫn 09/10/2026.

## 1. Tạo mẫu dùng lại từ báo giá đã lập
- Chỉ chuyển thành mẫu khi người dùng giao rõ việc tạo mẫu. Tạo bản sao mới từ mẫu phù hợp; không sửa mẫu gốc tại chỗ.
- Xóa dữ liệu nhận diện khách hàng cũ (tên, địa chỉ, người liên hệ, điện thoại, email), số báo giá/giao dịch, ngày giao dịch và mọi nội dung riêng cho khách. Để placeholder dễ nhận biết dạng `[[TÊN TRƯỜNG IN HOA]]` cho trường cần điền sau. Kiểm cả nội dung ẩn/metadata nếu công cụ cho phép.
- Chỉ giữ tên model/cấu hình khi mẫu được xác định riêng cho model đó. Không mang giá, chiết khấu, tiến độ, điều khoản hoặc xác nhận chưa được duyệt từ báo giá cũ sang mẫu.
- Kiểm lại nội dung hiển thị sau khi xóa; không để ghi chú biên tập hoặc câu giải thích nội bộ trong mẫu cuối nếu người dùng yêu cầu bỏ ghi chú.
- Mẫu mới đặt trạng thái BẢN NHÁP hoặc CHỜ DUYỆT; chỉ người có thẩm quyền đưa vào `2. TEMPLATE - BIỂU MẪU/01 - BÁO GIÁ/` kèm `README.md`.

## 2. Kiểm bản in HTML/PDF
- Render/xuất PDF và kiểm: đủ số trang dự kiến, số trang/footer liên tục, không có trang trắng hoặc phần nội dung rơi sang trang thừa.
- Mẫu máy chấn NHCTECH (MẪU 01.03): PDF đúng 7 trang, footer đánh số liên tục. Cấu trúc HTML có 7 section không tự chứng minh PDF có 7 trang; phải render/xem PDF để xác nhận.
- Kiểm logo, ảnh máy, đường dẫn tài nguyên tương đối; không phụ thuộc ảnh từ nguồn ngoài.
- Chưa render được thì ghi rõ “phân trang trực quan chưa xác minh”; không tìm cách vượt chặn quyền của công cụ.

## 3. Checklist bổ sung
- [ ] Tên tệp khách hàng đúng cấu trúc; mẫu dùng lại ghi rõ “MẪU”.
- [ ] Mẫu dùng lại đã loại dữ liệu nhận diện/giao dịch của khách cũ; trường cần nhập để placeholder rõ ràng.
- [ ] Bản render đã kiểm số trang, footer, trang trắng; hoặc ghi rõ chưa xác minh trực quan.

*Nam Hải CNC — 09/10/2026 · Bản nháp chờ duyệt*
