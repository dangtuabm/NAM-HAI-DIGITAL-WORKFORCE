# Quy cách trình bày bản vẽ dao/cối Tully

Chỉ đọc tài liệu này khi người dùng yêu cầu Tully tạo hoặc sửa bản vẽ PDF, PNG hay HTML. Đây là **quy cách trình bày**, không phải nguồn xác nhận kích thước, vật liệu, nhiệt luyện, tải hoặc khả năng chế tạo của dụng cụ mới.

## Mẫu đã đối chiếu

- `04. Bản vẽ dao cối/Dao chấn H117 A26 R0.8.pdf`
- `04. Bản vẽ dao cối/Cối dập bẹp H140 V14.pdf`
- `04. Bản vẽ dao cối/V16 - M8.pdf`
- `04. Bản vẽ dao cối/20260805 Bản vẽ dao cối R80 2400 mm.pdf`
- `04. Bản vẽ dao cối/13082026 Bản vẽ dao cối (dập bẹp) - KH Đức Mạnh.pdf` (2 trang; tham chiếu mới nhất người dùng nêu cho nhóm dập bẹp).
- Hình thông số người dùng đính kèm ngày 03/10/2026: `codex-clipboard-5c409055-5b2f-49f0-a1e0-de419356d781.png`.

Các PDF trên là mẫu hình thức. Nếu các mẫu khác nhau về nội dung hoặc tỷ lệ, ưu tiên bản vẽ cùng loại dao/cối và chỉ đạo mới nhất của người dùng; nêu khác biệt khi nó ảnh hưởng quyết định.

## Bố cục cần giữ

- Giấy A4 ngang, nền giấy trắng, nét và chữ đen, khung kín cách mép khoảng 5 mm. **Hình học dụng cụ tô xám như PDF tham chiếu**, không để toàn bộ bản vẽ thành các ô trắng rỗng: mặt chính tham khảo xám ấm khoảng `#aba9a5`, mặt tối/phối cảnh khoảng `#55534f`, cạnh và đường kích thước màu đen. Tông màu là định hướng thị giác, không quy định vật liệu hoặc xử lý bề mặt.
- Dành không gian lớn nhất cho hình chiếu chính và kích thước. Tùy hình học từng ca mà đặt hình chiếu dài, mặt cắt, phóng to, phối cảnh và khối thông số ở khoảng trống phù hợp; **không cố định tọa độ các hình chiếu**. Tỷ lệ, đường kích thước, dung sai và ký hiệu phải đọc được khi in A4.
- Bảng thông tin kẻ ô ở góc phải dưới, bám cạnh phải và cạnh dưới của khung; khối **yêu cầu kỹ thuật** ở góc trái dưới. Giữ thứ bậc chữ, lề và khoảng trắng cân đối như PDF mẫu. Dùng [mẫu HTML](../templates/ban-ve-dao-coi-A4-ngang.html) làm khung tham chiếu khi tạo HTML hoặc xuất PDF/PNG.
- Logo trong bản vẽ lấy từ [NHC-_1_.jpg](../assets/NHC-_1_.jpg), bản sao nguyên byte từ `D:/00. NAM HẢI CNC/NỘI BỘ/NHC-_1_.jpg`. Thu logo khối thông số còn khoảng **70% so với bản demo đầu tiên** (mẫu HTML dùng bề ngang 55 mm thay 79 mm), điều chỉnh thêm nếu cần để nhường chỗ cho kích thước. Có thể cắt khoảng trắng lúc đặt vào khung; không vẽ lại, méo tỷ lệ, đổi màu hoặc thêm hiệu ứng vào dấu hiệu thương hiệu.
- Dòng trạng thái `PENDING TECHNICAL APPROVAL` đặt ở **góc trên trái** của bản vẽ sơ bộ. Các nhãn, ghi chú và yêu cầu kỹ thuật kế thừa giữ **nguyên tiếng Trung/tiếng Anh** của bản tham chiếu cùng loại; không dịch sang tiếng Việt trên bản vẽ. Phần giải thích tiếng Việt, nếu cần, nằm ở hồ sơ ngoài bản vẽ.
- Bảng giữ vị trí cho chiều dài/số lượng, vật liệu, xử lý bề mặt, nhiệt luyện/độ cứng khi có căn cứ, ghi chú, ngày bản vẽ, ngày giao nếu được cung cấp, và người thiết kế. **Vật liệu, phương pháp xử lý, độ cứng và tên người thiết kế chỉ điền theo dữ liệu được xác nhận cho ca đó.** Không sao chép `42CrMo`, `HRC55-60` hoặc `Jason Xu` từ bản vẽ mẫu sang dụng cụ mới.
- Các ô **mã/tên bản vẽ (Part name), cân nặng, chia đoạn** được giữ trong bố cục nếu cần để giống bảng mẫu nhưng để trống khi người dùng không yêu cầu. Không tự tính, suy ra hoặc điền từ bản mẫu.
- `Drawing date` trong khối thông số lấy **thời điểm tạo hoặc sửa bản cuối** theo `Asia/Saigon`, ghi ngày và giờ rõ ràng rồi cố định trong file đã xuất. Ô `订单日期 / Order date`, `交货日期 / Delivery date`, `定稿日期 / Filing date`, ngày sản xuất, mã lô hoặc chuỗi dạng `#YYYYMMDD#` chỉ điền khi có dữ kiện riêng; không gán chúng bằng ngày tạo file.

## Khối hình thông số kiểu mẫu đính kèm

Đặt logo trên cùng, các dòng thông số ngay dưới, căn trái, đủ khoảng trắng; có thể tạo hình PNG riêng hoặc đặt trực tiếp trên bản vẽ. Chỉ hiển thị đại lượng phù hợp với dụng cụ và được cung cấp/xác minh: `L`, `H`, góc `A`, miệng cối `V`, bán kính `R`, ngày, tải danh định và trang web nếu cần. Ghi đơn vị tại từng đại lượng hoặc trong chú giải rõ ràng. Mọi con số của hình đính kèm chỉ là **minh họa bố cục**.

Không tự dùng `1000 kN/m (100 ton/m)` hay `300 kN/FOOT` trong ảnh làm tải của dao/cối mới. Chỉ ghi `MAX` với nguồn đúng mã dụng cụ, đơn vị, chiều dài chịu tải và điều kiện áp dụng. Nếu đổi kN sang tấn lực, nêu hệ quy đổi và phép tính; không sao chép giá trị làm tròn trong ảnh. Không biến đơn vị tải trên mỗi foot thành tải tổng hoặc tải trên mét khi chưa có cơ sở.

## Năm dòng yêu cầu kỹ thuật kế thừa

Theo lựa chọn trực tiếp của người dùng ngày 03/10/2026, **chép nguyên năm dòng từ bản tham chiếu cùng loại dao/cối của ca đó** vào bản vẽ mới, giữ cả ngôn ngữ và ký hiệu gốc. Nếu có nhiều mẫu cùng loại nhưng năm dòng khác nhau, nêu khác biệt và hỏi người dùng chọn bản tham chiếu. Không trộn câu từ nhiều bản mẫu.

Ví dụ nguyên văn từ `13082026 Bản vẽ dao cối (dập bẹp) - KH Đức Mạnh.pdf`, trang 1–2, khối trái dưới:

```text
Technical requirements:
1. Group exchange docking, interface error should be ≤ 0.03mm
2. The parallelism and perpendicularity errors should be ≤ 0.03mm
3. Sharp angles are all rounded at C0.5/R0.5, and the notch R transitions smoothly
4. Unmarked dimensional tolerance implemented in accordance with GB/T18/04-F
5. Symmetry tolerance shall be implemented according to GB-T1184-H level
```

Các bản khác như `V16 - M8.pdf` có năm dòng khác về câu chữ và nhãn `skills requirement:`. Chỉ sao chép bộ của bản cùng loại đã chọn. Đây là **nội dung kế thừa từ mẫu**, chưa tự xác nhận phù hợp mọi dao/cối. Ký hiệu `GB/T18/04-F` và `GB-T1184-H` trong ví dụ phải được người dùng kiểm lại nếu dùng làm căn cứ chế tạo; Tully không âm thầm sửa thành mã tiêu chuẩn khác. Ghi cảnh báo áp dụng và trạng thái `PENDING TECHNICAL APPROVAL` trên bản vẽ sơ bộ. Nếu một dòng xung đột với thông số cụ thể, vẫn cho thấy nguyên văn và nêu xung đột, không kết luận phần phụ thuộc hoặc phát hành chế tạo.

## Kiểm trước bàn giao

1. So hình xuất với ít nhất một PDF mẫu **cùng loại**: khung, tông xám của hình học, không gian dành cho hình chiếu chính, logo nhỏ, bảng thông tin Trung–Anh, khối thông số, năm dòng kỹ thuật cùng nguồn.
2. Kiểm từng số và đơn vị trên hình chiếu, bảng và khối thông số khớp cùng một bảng nguồn; ô không có dữ kiện để trống hoặc ghi rõ chưa xác minh, không lấy số từ ảnh mẫu.
3. Kiểm ngày/giờ `Asia/Saigon`, không nhầm ngày bản vẽ với mã lô/ngày sản xuất; kiểm bản PDF/PNG/HTML ở kích thước A4, không cắt chữ/nét.
4. Bản vẽ sơ bộ ghi `PENDING TECHNICAL APPROVAL` ở góc trên trái; không gọi là bản vẽ chế tạo đã phát hành hoặc bản CAD.
