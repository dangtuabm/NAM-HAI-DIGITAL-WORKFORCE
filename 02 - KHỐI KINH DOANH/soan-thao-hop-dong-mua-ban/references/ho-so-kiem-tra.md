# HỒ SƠ KIỂM TRA BỘ SKILL

Ngày lập: 02/10/2026. Owner: Phó giám đốc Backoffice.

## Trạng thái

- Nội dung SKILL.md: đã được duyệt trong chat; bộ file được yêu cầu lưu vào HUB.
- Nghiệm thu thực tế: CHƯA HOÀN THÀNH.
- Cài đặt hệ thống: CHƯA THỰC HIỆN, chờ đạt kiểm thử thực tế theo lựa chọn 12C.
- Không có mẫu hợp đồng, bảng giá hoặc hồ sơ giao dịch thực tế trong hai thư mục TEMPLATE và DATA được kiểm ngày 02/10/2026; hai thư mục chỉ có README. Không suy rằng nguồn không tồn tại ở nơi khác.
- Thiết kế ca kiểm trong evals.json chưa phải ca thật; chưa chạy nhận diện, thực thi, baseline hoặc pass^3.
- Chưa đánh giá tác dụng trên hợp đồng hoặc xác minh chính sách thuế cho giao dịch cụ thể.

## Kiểm tra kỹ thuật

Đã kiểm trên bộ file lưu trong HUB ngày 02/10/2026:

| Hạng mục | Kết quả/bằng chứng |
|---|---|
| Bộ file | 7 file UTF-8 tồn tại, có nội dung và đọc được |
| YAML SKILL.md | Parse bằng PyYAML 6.0.3; tên khớp thư mục, metadata là chuỗi |
| Bộ kiểm hệ thống | quick_validate.py: Skill is valid! |
| 7 mục | Đúng tên và thứ tự theo khung Skill 07 phần |
| Bảng phân quyền | Có hai cột Người quyết định / A.I thực thi |
| Cách viết A.I | Dùng A.I; không phát hiện cách viết sai (thiếu dấu chấm hoặc có khoảng trắng) trong thân SKILL.md |
| Description | 312 ký tự sau parse YAML, dưới 600 |
| Thân SKILL.md | 226 dòng sau YAML, dưới 500 |
| Đường dẫn tài nguyên | 4 liên kết trực tiếp đều trỏ file tồn tại |
| agents/openai.yaml | Parse được; tên hiển thị, mô tả và câu gọi đúng; tự nhận diện được cấu hình, chưa kiểm thực tế |
| evals.json | Parse được; 10 đề kiểm thiết kế; 0 ca thực tế; kết quả là null, chưa chạy |
| Phần luật | Rà nội dung: bàn giao theo nhiệm vụ, không khóa tên Skill khác |

Không suy kiểm cấu trúc thành nghiệm thu nghiệp vụ. Chưa chạy hợp đồng thực tế, baseline, kiểm nhận diện hoặc pass^3. Token thân ở môi trường đích chưa đo; không sử dụng số ký tự/dòng để suy số token.

## Điều kiện tiếp tục

Cần mẫu công ty, chính sách giá và hồ sơ ít nhất 5 ca thực tế được phép dùng, cùng xác nhận chuyên môn/baseline. Bổ sung quy định bảo mật, điểm dừng bổ sung, phân quyền chi tiết và chu kỳ rà soát trước nghiệm thu. Không tạo hợp đồng giả làm nguồn kiểm thử thực tế.

## Cập nhật 09/10/2026 — chuẩn hóa vào kho Skill HUB

- Kho TEMPLATE của HUB đã được hệ thống hóa theo danh mục cố định: hợp đồng, biên bản tại `2. TEMPLATE - BIỂU MẪU/02 - HỢP ĐỒNG & BIÊN BẢN/` (MẪU 02.01–02.05), công văn thanh toán tại `03 - CÔNG VĂN THANH TOÁN/` (MẪU 03.01–03.07). Trạng thái duyệt từng mẫu đọc trong README của mẫu; chưa suy ra mẫu nào đã được duyệt cho Skill này.
- evals.json viết lại theo chuẩn kho: 13 ca thiết kế, mỗi ca có id, type, source, prompt, expected_behavior, evidence; vẫn là ca giả lập, chưa phải ca thực tế, chưa chạy baseline hoặc pass^3.
- Gộp phần rà soát/đối chiếu/so sánh hợp đồng từ Skill soạn và rà soát hợp đồng (bản 0.1, 05/10/2026, Khối Kinh doanh) thành `references/ra-soat-doi-chieu-hop-dong.md`, ở trạng thái chờ duyệt.
- Thay họ tên người dùng bằng chức danh Phó giám đốc Backoffice trong toàn bộ gói.
