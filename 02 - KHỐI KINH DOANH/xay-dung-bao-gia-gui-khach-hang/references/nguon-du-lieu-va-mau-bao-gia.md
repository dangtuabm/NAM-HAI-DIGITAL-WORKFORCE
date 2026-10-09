# NGUỒN DỮ LIỆU VÀ MẪU BÁO GIÁ

## Mục lục
1. Định tuyến mẫu theo dòng máy
2. Nguồn dữ liệu trong HUB
3. Ghi chú nguồn bảng giá máy chấn CNHAWE HPC
4. Ghi chú nguồn thông số máy chấn NHCTECH
5. Quy tắc tên file
6. Kiểm tra trước khi áp dụng nguồn

Nguồn gộp: bản 0.2 (08/10/2026, gồm `data-sources.md`) và bản 1.1 (08/10/2026) của Skill; đường dẫn cập nhật sang cấu trúc HUB ngày 09/10/2026. Sự hiện diện của tệp trong HUB không tự xác nhận ngày hiệu lực hoặc trạng thái phê duyệt; đọc `README.md` của từng mẫu để biết trạng thái ĐÃ DUYỆT / CHỜ DUYỆT / BẢN NHÁP.

## 1. Định tuyến mẫu theo dòng máy

Tất cả mẫu nằm trong `2. TEMPLATE - BIỂU MẪU/01 - BÁO GIÁ/`. Dùng mẫu người dùng chỉ định; nếu không chỉ định, chọn theo dòng máy. Các mẫu không thay thế lẫn nhau.

| Mã mẫu | Dòng máy / phạm vi | Ghi chú nguồn cũ |
|---|---|---|
| MẪU 01.01 | Báo giá thiết bị dùng chung (thiết bị, phụ kiện chưa có mẫu riêng) | Mẫu báo giá dùng chung của core team |
| MẪU 01.02 | Máy chấn CNHAWE HPC | Trước đây: `Bao_gia_HPC-250-4000_HW66S_CN-HAWE.html` |
| MẪU 01.03 | Máy chấn NHCTECH | Trước đây: `MẪU BÁO GIÁ MÁY CHẤN NHCTECH.07.10.2026.html`; bản in đúng 7 trang |
| MẪU 01.04 | Máy cắt laser SENFENG dòng N | |
| MẪU 01.05 | Máy cắt laser SENFENG dòng R | |
| MẪU 01.06 | Máy cắt ống laser JQ KS120 | |
| MẪU 01.07 | Máy cắt ống laser JQ HTS | |
| MẪU 01.08 | Máy cắt ống laser NHCTECH | |

Mẫu tương ứng thiếu hoặc không đọc được: dừng và báo; không lấy mẫu của dòng máy khác. Dùng MẪU 01.01 cho dòng máy chưa có mẫu riêng chỉ khi người dùng đồng ý.

## 2. Nguồn dữ liệu trong HUB

| Nhu cầu | Vị trí | Cách dùng |
|---|---|---|
| Hồ sơ kỹ thuật theo hãng/dòng | `3. DATA - DỮ LIỆU/01 - NHÀ CUNG CẤP & SẢN PHẨM/<HÃNG>/<NHÓM MÁY>/<DÒNG hoặc MODEL>/<HỒ SƠ>/` | Đọc `index.html` (bản phẳng) để tra; truy ngược PDF/DOCX nguồn qua `NGUỒN.txt` khi cần xác minh |
| Bảng giá nhà cung cấp [ĐỎ] | `3. DATA - DỮ LIỆU/02 - BẢNG GIÁ NIÊM YẾT [ĐỎ]/<HÃNG> - <NHÓM MÁY> - <năm>/` | Chỉ Kinh doanh, Mua hàng, CEO; xác minh hiệu lực trước khi dùng |
| Logo Nam Hải, logo thương hiệu, ảnh máy | `3. DATA - DỮ LIỆU/04 - HÌNH ẢNH & LOGO/` | Tài sản hình ảnh; không phải nguồn giá, cấu hình hay chính sách |
| Hồ sơ doanh nghiệp | `3. DATA - DỮ LIỆU/05 - HỒ SƠ DOANH NGHIỆP/`; `1. ABOUT ME - BỘ NÃO/01_HO_SO_DOANH_NGHIEP_VA_PHAP_LY.md` | Thông tin bên bán trên báo giá |
| Vai trò Kinh doanh, nguyên tắc A.I | `1. ABOUT ME - BỘ NÃO/VAI_TRO/02_KINH_DOANH.md`; `12_NGUYEN_TAC_LAM_VIEC_VOI_A.I.md` | Chỉ đọc phần liên quan |

Hãng dùng tên chuẩn: ACCURPRESS · CNHAWE · SENFENG · JQ LASER · NHCTECH · HYMSON · REEGAO · DEHAHA · ZMDE · JIANMENG. Bảng giá hiện có trong HUB ngày 09/10/2026: ACCURPRESS - MÁY CHẤN ĐỘT CHẶT - 2026; CNHAWE - MÁY CHẤN - 2026; JQ LASER - MÁY CẮT ỐNG LASER - 2026; NHCTECH - MÁY CẮT ỐNG LASER - 2026; SENFENG - LASER CẮT & HÀN - 2026.

## 3. Ghi chú nguồn bảng giá máy chấn CNHAWE HPC

Thư mục: `3. DATA - DỮ LIỆU/02 - BẢNG GIÁ NIÊM YẾT [ĐỎ]/CNHAWE - MÁY CHẤN - 2026/`.

| Tệp | Dữ liệu | Cách sử dụng |
|---|---|---|
| `Bảng giá niêm yết máy chấn HPC CN-HAWE.md` | Giá máy, giá option, tỷ giá USD/VNĐ, nguyên tắc làm tròn, ghi chú VAT | Căn cứ giá sau khi xác minh còn hiệu lực và được phép áp dụng cho giao dịch |
| `Bảng giá niêm yết + Thông số kỹ thuật + Cấu hình linh kiện máy chấn HPC CN-HAWE.md` | Bảng giá, thông số máy, cấu hình linh kiện tiêu chuẩn | Tra cứu có điều kiện; xác minh hiệu lực giá riêng; đối chiếu thông số/cấu hình với hồ sơ hãng |

- Hai tệp cùng có bảng giá HPC: đối chiếu đúng dòng model và option; giá hoặc điều kiện khác nhau thì ghi sai khác, không tự chọn một bản.
- Nguồn đang ghi: giá chưa gồm VAT 8%, tỷ giá `1 USD = 26.500 VNĐ`, làm tròn đến hàng triệu đồng. Đây là nội dung tài liệu ghi, không phải xác nhận độc lập rằng quy tắc còn hiệu lực cho giao dịch.
- Bảng thông số ghi chiều dài chấn `4100 mm` cho một số model mang hậu tố `4000`, và ghi đã hiệu chỉnh công suất HPC-110-3100/HPC-110-4000 thành `12.4 kW`, trọng lượng sang đơn vị tấn. Giữ nguyên nội dung nguồn khi đối chiếu; xác minh với hồ sơ hãng hoặc Kỹ thuật trước khi đưa trường đang tranh chấp vào báo giá.
- Mục option khác theo báo giá dòng HPA ghi chưa có giá cụ thể: không tự điền giá hoặc đưa vào tổng tiền.
- Nguồn giúp tra bảng giá và thông số, nhưng không thay chính sách thương mại được phê duyệt, hồ sơ hãng từng giao dịch, hoặc xác nhận giá còn hiệu lực.

## 4. Ghi chú nguồn thông số máy chấn NHCTECH

- Tệp nguồn của core team: `Thông số kỹ thuật máy chấn NHC.md` (trước đây trong thư mục BIỂU MẪU/Máy chấn NHC). Vị trí trong HUB mới: thư mục mẫu MẪU 01.03 hoặc `3. DATA - DỮ LIỆU/01 - NHÀ CUNG CẤP & SẢN PHẨM/NHCTECH/` [CHỜ XÁC NHẬN vị trí].
- Trường `ĐVT` và `Nguồn gốc` đọc theo định nghĩa/căn cứ tại nguồn; “Nguồn gốc” là quốc gia thương hiệu nếu nguồn ghi như vậy, không suy ra quốc gia sản xuất.
- Không tự bổ sung ĐVT, nguồn gốc hoặc thông số còn thiếu; ghi rõ trường cần xác nhận.
- Mẫu NHCTECH đã chốt theo yêu cầu người dùng vẫn không chứng minh điều khoản thương mại trong mẫu đã được duyệt độc lập.

## 5. Quy tắc tên file

- Báo giá theo khách: `NAMHAICNC. HSBG [TÊN THIẾT BỊ] GỬI CTY [TÊN KHÁCH HÀNG].DD.MM.YYYY`. [Minh họa]: `NAMHAICNC. HSBG MÁY CHẤN NHC-110-3100 GỬI CTY [TÊN KHÁCH HÀNG].07.10.2026.html`.
- Thay trường trong ngoặc bằng dữ liệu giao dịch và ngày báo giá; giữ nguyên bố cục tên. Tên này không dùng làm tên mẫu tổng quát.
- Mẫu dùng lại: tên ghi rõ `MẪU`, không mang tên hoặc dữ liệu giao dịch của khách.

## 6. Kiểm tra trước khi áp dụng nguồn

- Xác minh ngày hiệu lực, phiên bản, người phê duyệt và phạm vi áp dụng của bảng giá/chính sách; không xác minh được thì dừng phần giá hoặc điều khoản bị ảnh hưởng và hỏi người có thẩm quyền.
- Ngày sửa mới hơn tự nó không chứng minh tài liệu đã được duyệt hoặc thay thế nguồn chính thức.
- Ghi tên tệp, vị trí (trang/sheet/mục) cho mỗi số liệu dùng trong báo giá.

*Nam Hải CNC — 09/10/2026 · Bản nháp chờ duyệt*
