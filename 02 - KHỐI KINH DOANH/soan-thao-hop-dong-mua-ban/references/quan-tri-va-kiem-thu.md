# QUẢN TRỊ VÀ KIỂM THỬ

## Trạng thái và căn cứ

Nội dung được Phó giám đốc Backoffice duyệt trong chat ngày 02/10/2026 và yêu cầu lưu HUB. Phê duyệt nội dung Skill không phải phê duyệt hợp đồng, chính sách hoặc kết quả kiểm thử.

Chuẩn đối chiếu: khung Skill 07 phần của kho Skill HUB (`4. SKILL - KỸ NĂNG/`, tính từ gốc HUB); cùng quy tắc HUB và hướng dẫn tạo Skill của hệ thống. Không tự chuyển nội dung khung chung thành quy tắc công ty.

## Nguồn cần xác nhận trước nghiệm thu

| Nguồn hoặc quyết định | Trạng thái tại ngày 02/10/2026 | Cách xử lý |
|---|---|---|
| Mẫu hợp đồng công ty đã duyệt | Chưa có trong TEMPLATE đã kiểm ngày 02/10; từ 09/10 có MẪU 02.01–02.05 tại `2. TEMPLATE - BIỂU MẪU/02 - HỢP ĐỒNG & BIÊN BẢN/` | Xác nhận phiên bản, trạng thái duyệt và quyền dùng từng mẫu; giữ nguyên nguồn |
| Bảng giá và chính sách đang áp dụng | Chưa có trong DATA đã kiểm ngày 02/10; từ 09/10 có bảng giá nhà cung cấp tại `3. DATA - DỮ LIỆU/02 - BẢNG GIÁ NIÊM YẾT [ĐỎ]/` (chưa phải chính sách giá bán) | Xác nhận hiệu lực, phạm vi, phê duyệt ngoại lệ |
| Hồ sơ giao dịch thực tế | Chưa có trong DATA đã kiểm | Thu thập nguồn được phép, khử định danh phù hợp |
| Phân quyền chi tiết theo giao dịch | ABOUT ME có nguyên tắc; chưa đủ hạn mức/quyền cụ thể | Xác nhận đầu mối và phạm vi phê duyệt |
| Quy định Xanh–Vàng–Đỏ và công cụ ngoài được phép | Chưa được cung cấp trong nhiệm vụ | Không tự đặt phân loại hoặc quyền truyền dữ liệu |
| Điểm dừng bổ sung theo lựa chọn 10B | Chưa được chị quy định cụ thể | Áp dụng ranh giới đã duyệt; hỏi nếu phát sinh quyết định phụ thuộc |
| Chu kỳ rà soát và người kiểm chuyên môn | Chưa xác nhận chi tiết | Phó giám đốc Backoffice xác nhận trước nghiệm thu |

## Thiết kế và thực hiện kiểm thử

`evals.json` chứa đề kiểm thiết kế, không phải bằng chứng ca thật. Trường dữ liệu và kết quả chưa có dùng null hoặc danh sách rỗng, không dùng số giả.

1. Chọn ít nhất 5 ca từ tình huống thực tế đã xảy ra. Một ca có thể phủ nhiều nhãn; số ca không thay độ phủ. Ghi nguồn gốc được phép và vai trò người xác nhận.
2. Chuẩn bị bộ đầu vào tối thiểu, bản đối chiếu chuyên môn và quyền sử dụng. Chỉ khử định danh trên bản sao được phép; không sửa nguồn.
3. Giữ kết quả mong đợi ngoài nguồn cung cấp cho A.I thực thi. Không đưa evals.json hoặc hồ sơ chấm vào đầu vào tác vụ khi kiểm thực thi.
4. Kiểm nhận diện bằng câu tự nhiên trong danh mục có năng lực lân cận, không ép gọi Skill. Ghi lựa chọn quan sát được; không quan sát được thì selected_skill và routing_passed là null kèm lý do.
5. Kiểm thực thi riêng có thể nạp Skill tường minh. Không suy nhận diện đạt từ kết quả thực thi đẹp.
6. Chạy hai nhánh có Skill và baseline độc lập; nhánh baseline không được nạp Skill. Có thể dùng kết quả làm tay đã được chuyên môn kiểm như Human Baseline. Chạy song song nếu môi trường và quyền cho phép; không tự tạo chat mới hoặc cấp thêm quyền để thực hiện.
7. Kiểm đầu ra dự kiến dùng đối ngoại bằng pass^3. Các lượt không gửi, ký hoặc tác động bên thứ ba. Đạt cả ba lượt trên tiêu chí bắt buộc; lỗi ranh giới phải sửa và kiểm lại phần liên quan.
8. Ghi passed, evidence, mode, runtime/model, phiên bản danh mục, selected_skill, routing_passed, execution_passed, output_passed, total_tokens và duration_ms. Không đo được thì ghi null và lý do.
9. Tách bộ ca phát triển năng lực và bộ chống thoái hóa. Bộ chống thoái hóa phải đạt toàn bộ khi nâng cấp.
10. Tổng hợp nghiệm thu dựa vào bằng chứng, không tự chấm đủ 12 tiêu chí khi thiếu số đo hoặc ca thật. Phó giám đốc Backoffice xác nhận kết quả trong phạm vi quản lý; nội dung chuyên môn theo người có thẩm quyền.

## Cài đặt sau kiểm thử

Chưa cài đặt khi hồ sơ thực tế/baseline/pass^3 chưa đạt. Đây là điều kiện chị đã chọn ở 12C, không phải yêu cầu duyệt lại việc đã giao.

Khi đủ điều kiện, cài vào thư mục skills của CODEX_HOME hoặc `~/.codex/skills` nếu không cấu hình CODEX_HOME. Giữ tên `soan-thao-hop-dong-mua-ban`; kiểm xung đột trước. Không ghi đè bản có sẵn khi chưa có quyền và bản khôi phục đọc được. Không dùng liên kết tự cập nhật khiến thay đổi trong HUB tự tác động bản cài.

Bản cài giữ SKILL.md, agents/openai.yaml và tài nguyên thực thi; hồ sơ chấm/đáp án kiểm thử giữ tại HUB, không nạp vào tác vụ kiểm thực thi. Xác nhận công cụ nhận diện Skill sau cài; nếu không quan sát được, báo chưa xác minh.

## Phiên bản và khôi phục

Bản 1.0.0: lưu nội dung đã duyệt và tài nguyên vận hành ngày 02/10/2026. Chưa nghiệm thu thực tế.

Nâng cấp chỉ khi có vấn đề cụ thể hoặc thay đổi nguồn/quy tắc; lưu bản khôi phục tại nơi được cho phép trước khi thay thế. Khôi phục bản cài đã kiểm nếu nâng cấp lỗi trong phạm vi được cấp; không dùng ARCHIVE làm nơi sao lưu mặc định. Không tự sửa AGENTS.md hoặc mẫu chính thức.
