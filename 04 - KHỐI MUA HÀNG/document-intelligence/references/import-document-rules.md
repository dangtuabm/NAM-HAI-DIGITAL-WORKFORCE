# QUY TẮC ĐỌC VÀ ĐỐI CHIẾU CHỨNG TỪ NHẬP KHẨU

Đọc ở bước 2 đến 6.

## 1. Kiểm kê độ phủ trước khi đọc
| Định dạng | Phải kiểm | Dấu hiệu coverage yếu |
|---|---|---|
| PDF | Tổng trang, lớp chữ, bản quét, bảng, con dấu, chữ ký, phụ lục | Trang trống chữ, bảng vỡ cột, thiếu trang |
| Ảnh / bản quét | Chiều trang, vùng chữ, độ rõ số | Nhầm số, mất dấu, bỏ vùng rìa |
| Excel | Sheet ẩn và hiện, công thức, ghi chú | Chỉ đọc sheet đang mở |
| Word | Bảng, đầu cuối trang, ghi chú, thay đổi theo dõi | Bỏ bảng, ghi chú |

Ghi mỗi thành phần: ID, vị trí, trạng thái ĐÃ ĐỌC / KHÔNG ĐỌC ĐƯỢC / NGOÀI PHẠM VI, lý do, hành động khắc phục. File hỏng hoặc có mật khẩu không được tính là đã đọc.

## 2. Dữ liệu trọng yếu cần bóc
| Chứng từ | Trường |
|---|---|
| PO | Số PO, ngày, bên mua và bán (tên pháp lý), hãng, model, mã hàng, số lượng, đơn giá, tổng, tiền tệ, điều kiện giao hàng, điều kiện thanh toán, yêu cầu kèm theo |
| Invoice | Số, ngày, bên bán và mua, dòng hàng, số lượng, đơn giá, tổng, tiền tệ, điều kiện giao hàng, xuất xứ nếu ghi, HS code nếu ghi |
| Packing list | Số kiện, kích thước, trọng lượng cả bì và tịnh, danh mục từng kiện, số serial nếu có |
| CO | Số, ngày, nước và bên cấp, người xuất khẩu, người nhận, mô tả hàng, tiêu chí xuất xứ, HS code nếu ghi |
| CQ | Số, ngày, bên cấp, model hay số serial, kết quả kiểm hoặc cam kết nêu trong tài liệu |
| HS code | Mã ghi ở từng chứng từ hoặc bảng kê, mô tả hàng đi kèm |

Mỗi dòng dữ liệu ghi: UNIT-ID, file, phiên bản, trang hoặc ô, trích đoạn ngắn, nhãn Dữ kiện / Suy luận / Giả định.

## 3. Danh mục đối chiếu chéo
| # | Điểm đối chiếu | Giữa | Lưu ý |
|---|---|---|---|
| 1 | Tên pháp lý và mã số thuế bên mua | PO, invoice, CO | So với hồ sơ doanh nghiệp (file 01) |
| 2 | Hãng, model, mã hàng | PO, invoice, packing list, CQ | Nguyên văn, không suy đoán tương đương |
| 3 | Số lượng từng dòng | PO, invoice, packing list | Phân biệt thiếu, thừa, giao một phần |
| 4 | Đơn giá và tổng | PO, invoice | Tính lại; giữ tiền tệ gốc |
| 5 | Điều kiện giao hàng và thanh toán | PO, invoice | Nêu khác biệt, không đánh giá điều khoản |
| 6 | Số kiện, trọng lượng, kích thước | Invoice, packing list | Không tự đổi đơn vị |
| 7 | Xuất xứ | Invoice, CO | Nêu khác, không kết luận hiệu lực CO |
| 8 | Model và serial | CQ, packing list, PO | Nêu khớp hay không |
| 9 | HS code | Invoice, CO, bảng kê | Chỉ so nhất quán |
| 10 | Ngày tháng và số tham chiếu | Tất cả | Logic ngày: ngày PO trước invoice, v.v. |
| 11 | Phiên bản và thay đổi | PO, invoice | Bản nào mới nhất theo hồ sơ |

Kết quả mỗi điểm: Khớp / Lệch / Thiếu / Không so được.

## 4. Mức tác động
| Mức | Ví dụ | Hành động |
|---|---|---|
| Cao | Lệch số lượng, giá, model, tên pháp lý, thiếu CO hoặc CQ bắt buộc, HS code không nhất quán | Chuyển ngay, tạm dừng việc phụ thuộc |
| Trung bình | Lệch trọng lượng, ngày, mô tả hàng | Yêu cầu làm rõ |
| Thấp | Sai chính tả, định dạng | Ghi chú |

## 5. Quy tắc riêng về HS code
- Chỉ nêu: mã nào xuất hiện ở đâu, có đồng nhất giữa chứng từ không, mô tả hàng đi kèm có nhất quán không.
- Không kết luận mã đúng, sai, thuộc nhóm nào, mức thuế; không đề xuất mã thay thế.
- Khác biệt hoặc không rõ: chuyển người có thẩm quyền về hải quan và thuế.

## 6. Quy tắc OCR và dịch
- Số, tên riêng, mã hàng không chắc: [OCR CẦN XÁC NHẬN]; so ảnh gốc cho dữ liệu tác động cao.
- Chứng từ tiếng Anh hoặc tiếng Trung: giữ nguyên văn phần số hiệu, tên; chỉ diễn giải tiếng Việt cho phần mô tả; không dịch tự do điều khoản.
- Bảng vỡ cột: quay lại bố cục gốc, không suy hàng cột từ thứ tự chữ.

## 7. Không nâng cấp ý nghĩa
"Dự kiến", "khoảng" không phải số xác nhận. Ngày trong ví dụ không phải hạn thật. Bảng tóm tắt không ghi đè dòng chi tiết; giữ cả hai và đánh dấu lệch.
