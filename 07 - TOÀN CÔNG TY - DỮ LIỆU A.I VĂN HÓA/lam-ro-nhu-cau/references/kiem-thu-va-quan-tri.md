# Hồ sơ kiểm thử và quản trị — lam-ro-nhu-cau

## Trạng thái và nguồn

- Chủ sở hữu: Phó giám đốc Backoffice Nam Hải CNC.
- Ngày duyệt nội dung và yêu cầu cài đặt: 02/10/2026, qua cuộc trò chuyện tạo skill.
- Phiên bản 1.0: đóng gói bản đã duyệt; cập nhật metadata, trạng thái, liên kết tài nguyên. Không đổi lựa chọn vận hành.
- Phiên bản 1.1 (09/10/2026): sắp vào khung 7 phần của kho Skill HUB; gom mục kiểm thử và quản trị ra phần ngoài 07 phần; bổ sung phạm vi dùng của Giám đốc khi làm rõ đầu bài giao việc; viết lại `evals.json` theo chuẩn bộ ca của Nam Hải CNC.
- Căn cứ: chuẩn Skill Nam Hải CNC tại `4. SKILL - KỸ NĂNG/00 - CHUẨN SKILL NAM HẢI CNC/`; quy tắc HUB và trả lời 1A, 2A, 3B, 4B, 5A, 6A, 7B, 8B, 9A, 10B của chủ sở hữu.
- Biên bản cài đặt 02/10/2026 (tóm tắt): YAML/JSON đọc được; tên khớp thư mục; đúng 7 mục theo thứ tự; liên kết tài nguyên tồn tại; description 269 ký tự; chưa đo token ở runtime đích.
- Được phép cài đặt; chưa nghiệm thu. Ca thật sẽ bổ sung sau theo lựa chọn 10B.

## Cách dùng bộ ca

`../evals.json` chỉ chứa đề giả lập, không phải tình huống đã xảy ra. Dùng khi kiểm hành vi hoặc sửa phiên bản; không đưa kỳ vọng cho nhánh thực thi trước lượt kiểm.

- Kiểm nhận diện bằng yêu cầu tự nhiên, không ép gọi skill, trong danh mục có năng lực lân cận.
- Kiểm thực thi bằng cách nạp skill để đánh giá hỏi, tổng hợp và dừng đúng điểm.
- Đối chiếu với nhánh không dùng skill và ghi khác biệt quan sát được.
- Ghi model/runtime, danh mục, chế độ, skill thực sự được chọn, bằng chứng và kết quả riêng cho nhận diện/thực thi/đầu ra.
- Ghi token và thời gian nếu công cụ có số đo; không suy số đo từ ước lượng.
- Không quan sát được thì ghi null kèm lý do, không tự gán đạt.

## Điều kiện nghiệm thu còn thiếu

- Ít nhất 5 ca thật đã lược thông tin nhạy cảm và được phép sử dụng.
- Kết quả đối chiếu baseline cùng bằng chứng thực thi.
- Bằng chứng nhận diện trong runtime đích.
- Đánh giá bảng nguyên lý: bảng hiện tại là nguyên lý vận hành, chưa chứng minh tương đương yêu cầu 2–4 trụ nguyên lý có căn cứ. Không tự sửa nội dung đã duyệt để gán đạt.
- Lịch rà soát định kỳ do chủ sở hữu xác nhận.
- Số đo token thân bài theo tokenizer phù hợp runtime đích nếu chưa có công cụ tương ứng.

## Rà soát và khôi phục

Rà soát khi có lỗi thực tế, thay đổi quy định hoặc môi trường. Ghi bài học có thể tái sử dụng để chủ sở hữu xem xét; không tự ban hành.
Giữ nguyên tên skill khi nâng phiên bản. Chỉ sửa sau khi có quyền; trước khi thay thế tạo bản khôi phục tại `7. ARCHIVE - LƯU TẠM TRƯỚC KHI XÓA`, xác minh đọc được.
Bản HUB và bản cài đặt phải đồng nhất. Không tự gỡ cài đặt, xóa hoặc ghi đè phiên bản hiện hành ngoài phạm vi được phê duyệt.

*Nam Hải CNC — 09/10/2026 · Nội dung đã duyệt 02/10/2026 · Chờ kiểm thử*
