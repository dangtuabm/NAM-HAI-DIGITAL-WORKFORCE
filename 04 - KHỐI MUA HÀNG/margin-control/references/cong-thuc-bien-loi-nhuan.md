# Công thức biên lợi nhuận, mức giảm giá tối đa và cảnh báo

Nguồn: ABOUT ME Nam Hải CNC — file 03 mục 3 ("Tiết Kiệm Hơn" phải nêu khoản chi phí, kỳ tính, giả định), file 04 mục 2 (giá, thuế, phạm vi là dữ liệu bắt buộc), file 10 mục 8 (giá, chiết khấu đi đúng tuyến), file 11 mục 4 (không tự đổi đơn vị; ghi giá trị gốc, công thức, kết quả), file 12 (nguyên tắc 2, 3, 7, 9), VAI_TRO/03_MUA_HANG (cân nhắc tác động đến biên lợi nhuận). Công thức là khung tính; mọi con số lấy từ nguồn có ngày.

## Mục lục
1. Cấu trúc giá vốn về kho
2. Chi phí triển khai trực tiếp theo đơn
3. Giá bán, lãi gộp và % biên — mẫu số
4. Giá bán tối thiểu và mức giảm giá tối đa
5. Độ nhạy theo tỷ giá và chiết khấu
6. Ngưỡng và mức cảnh báo
7. Đơn nhiều máy và phân bổ chi phí chung
8. Kiểm tay và chỗ hay sai
9. Phân lớp bảo mật đầu ra

## 1. Cấu trúc giá vốn về kho
| Thành phần | Công thức bằng chữ | Ai xác nhận |
|---|---|---|
| Giá trị CIF (USD) | giá hàng + cước quốc tế + bảo hiểm (bỏ khoản đã nằm trong điều kiện giao hàng) | Mua hàng |
| Giá trị CIF (VND) | giá trị CIF USD nhân tỷ giá tính thuế | Kế toán chọn loại tỷ giá |
| Thuế nhập khẩu | giá trị tính thuế nhân thuế suất theo HS code | Kế toán |
| VAT nhập khẩu | (giá trị tính thuế + thuế nhập khẩu) nhân thuế suất VAT | Kế toán |
| Phí nội địa | phí cảng, giao nhận, bốc xếp, kiểm định, lưu kho | Mua hàng |
| Phí khác | ngân hàng, chứng từ | Mua hàng, Kế toán |
| Giá vốn về kho | CIF VND + thuế nhập khẩu + phí nội địa + phí khác (+ VAT nhập khẩu nếu Kế toán xác nhận không được khấu trừ) | Kế toán |

Điều kiện EXW cần thêm chi phí đưa hàng ra cảng đi; điều kiện CIF đã gồm cước và bảo hiểm. Thêm hoặc bớt biến, ghi lý do. Hàng mua nội địa: giá vốn về kho = giá mua chưa VAT + vận chuyển về kho + phí khác.

## 2. Chi phí triển khai trực tiếp theo đơn
| Khoản | Gắn với bước triển khai (file 08) | Người cung cấp số |
|---|---|---|
| Vận chuyển kho đến xưởng khách, cẩu hạ | Bước 4 | Mua hàng, Kỹ thuật |
| Lắp đặt, căn chỉnh | Bước 5 | Kỹ thuật |
| Chạy thử (vật tư, vật liệu thử) | Bước 5, 6 | Kỹ thuật |
| Đào tạo vận hành | Bước 7 | Kỹ thuật |
| Bảo hành dự phòng | Bước 8 | Tỷ lệ trên giá bán hoặc số tiền do người có thẩm quyền đặt |
| Chi phí tài chính (lãi vay, phí bảo lãnh, phí mở L/C) | Theo điều khoản thanh toán | Kế toán |
| Khác (hoa hồng, công tác phí) | Theo đơn | Người phụ trách đơn |

Khoản chưa có số ghi THIẾU, không tính bằng 0. Khoản tính bằng 0 phải ghi lý do (ví dụ "khách tự vận chuyển theo hợp đồng").

## 3. Giá bán, lãi gộp và % biên — mẫu số
- Giá bán thực thu chưa VAT = giá bán đề xuất chưa VAT nhân (1 − tỷ lệ chiết khấu).
- Bảo hành dự phòng (nếu theo tỷ lệ) = giá bán thực thu nhân tỷ lệ bảo hành dự phòng.
- Tổng giá vốn đơn = giá vốn về kho + chi phí triển khai + bảo hành dự phòng.
- Lãi gộp = giá bán thực thu chưa VAT − tổng giá vốn đơn.
- **% biên lãi gộp = lãi gộp / giá bán thực thu chưa VAT.** Mẫu số là giá bán sau chiết khấu, chưa VAT.
- **Tỷ lệ cộng thêm (markup) = lãi gộp / tổng giá vốn đơn.** Mẫu số là giá vốn. Hai chỉ số khác nhau; luôn ghi tên và mẫu số. Ví dụ [Minh họa]: lãi gộp 20 trên giá bán 100 là biên 20%, nhưng markup 25%.
- Không trộn giá có VAT với giá chưa VAT trong cùng một phép tính.

## 4. Giá bán tối thiểu và mức giảm giá tối đa
Gọi C = giá vốn về kho + chi phí triển khai (phần không phụ thuộc giá bán); m = biên mục tiêu; w = tỷ lệ bảo hành dự phòng theo giá bán; P0 = giá bán đề xuất chưa VAT.
- Giá bán tối thiểu để giữ biên mục tiêu: P_min = C / (1 − m − w). Chỉ tính khi 1 − m − w > 0.
- Mức giảm giá tối đa (tỷ lệ) = 1 − P_min / P0. Mức giảm giá tối đa (tiền) = P0 − P_min.
- Phần chiết khấu còn được phép = mức giảm giá tối đa − chiết khấu đang đề nghị.
- Kết quả âm: ngay giá đề xuất đã dưới biên mục tiêu; ghi "không còn dư địa giảm giá", không làm tròn thành 0.
- Tính lặp cho biên sàn để biết mức giảm giá chạm sàn.

## 5. Độ nhạy theo tỷ giá và chiết khấu
- Một chiều: đổi một biến, giữ các biến khác ở kịch bản cơ sở; ghi giới hạn vì tỷ giá và cước có thể đi cùng nhau.
- Hai chiều: lưới tỷ giá × chiết khấu, mỗi ô là % biên; tô theo mức cảnh báo ở Mục 6. Với script, tạo một kịch bản cho mỗi mức chiết khấu rồi chạy độ nhạy tỷ giá trên từng kịch bản.
- Tỷ giá hòa biên: tỷ giá tại đó % biên = biên mục tiêu (hoặc biên sàn). Script trả FOUND khi nghiệm nằm trong khoảng; NOT_BRACKETED thì báo không có nghiệm trong khoảng, không ngoại suy.
- Bước đổi (ví dụ ±1%, ±3%, ±5% tỷ giá) là lựa chọn phân tích, ghi rõ; khoảng dao động "hợp lý" do người có thẩm quyền hoặc nguồn có ngày đưa ra.

## 6. Ngưỡng và mức cảnh báo
| Mức | Điều kiện | Việc cần làm |
|---|---|---|
| XANH | % biên ≥ biên mục tiêu | Trình như bình thường |
| VÀNG | biên sàn ≤ % biên < biên mục tiêu | Nêu khoản kéo biên xuống; trình người có thẩm quyền xem |
| ĐỎ | % biên < biên sàn, hoặc lãi gộp < 0 | Gắn cảnh báo đầu bảng; chỉ người có thẩm quyền quyết tiếp tục |
| CHƯA PHÂN LOẠI | Chưa có ngưỡng được giao | Chỉ trình số, hỏi ngưỡng; không tự tô màu |

Biên mục tiêu và biên sàn do người có thẩm quyền thương mại đặt, có thể khác theo nhóm sản phẩm (máy, phụ kiện, vật tư, dịch vụ). A.I không tự đặt, không lấy ngưỡng của đơn cũ cho đơn mới khi chưa được xác nhận còn hiệu lực.

## 7. Đơn nhiều máy và phân bổ chi phí chung
- Tính từng dòng máy trước, rồi cộng thành tổng đơn; % biên tổng đơn = tổng lãi gộp / tổng giá bán thực thu, không lấy trung bình cộng các %.
- Chi phí chung của đơn (cước chung, phí cảng chung, vận chuyển chung) phân bổ theo tiêu chí Kế toán chọn: theo giá trị, trọng lượng hoặc thể tích. Chưa có chỉ đạo: phân bổ theo giá trị, gắn nhãn GIẢ ĐỊNH.
- Kiểm: tổng phân bổ bằng chi phí chung gốc.

## 8. Kiểm tay và chỗ hay sai
- Kiểm tay ít nhất một kịch bản: giá vốn về kho, tổng giá vốn, lãi gộp, % biên, giá bán tối thiểu.
- Chỗ hay sai: lấy giá có VAT làm mẫu số; nhầm biên với markup; quên chi phí triển khai; dùng một tỷ giá cho cả giá hàng và thuế dù khác loại; giả định VAT được khấu trừ mà chưa hỏi Kế toán; làm tròn giữa các bước; chép chi phí lắp đặt của đơn cũ.
- Làm tròn chỉ ở bước trình bày: tiền đến đồng, tỷ lệ đến 0,1%.

## 9. Phân lớp bảo mật đầu ra
| Bản | Nội dung | Người nhận |
|---|---|---|
| Bản đầy đủ | Giá nhập, từng khoản chi phí, biên, độ nhạy | Phó giám đốc Mua hàng, người có thẩm quyền thương mại, Kế toán |
| Bản xin chiết khấu | % biên sau chiết khấu, mức giảm tối đa, mức cảnh báo; không ghi giá nhập từng khoản | Kinh doanh khi xin chiết khấu [GIẢ ĐỊNH — phạm vi xem do người có thẩm quyền xác nhận] |
| Không có bản gửi khách | Giá nhập, biên, chiết khấu chưa duyệt không đưa ra ngoài | — |
