# QUY ƯỚC ĐẶT TÊN, BỘ NHÃN VÀ TRẠNG THÁI — THƯ VIỆN HÌNH ẢNH – VIDEO NAM HẢI CNC

Trạng thái: [GIẢ ĐỊNH] — bản đề xuất, chờ Phó giám đốc Backoffice xác nhận. Ngày: 07/10/2026.

## 1. Mã tài nguyên và tên file chuẩn

**Mã tài nguyên:** `TV-<NHÓM>-<NNNN>` — NNNN là số thứ tự 4 chữ số trong nhóm, không tái sử dụng số đã cấp.

**Tên file chuẩn:** `<Mã>_<HÃNG>_<MODEL>_<LOẠI>_<YYYYMMDD>.<đuôi>`
- HÃNG: viết đúng tên nhà cung cấp theo file 07, in hoa, không dấu cách (ví dụ JQLASER).
- MODEL: đúng ký hiệu trong tài liệu sản phẩm; chưa xác định thì ghi `CHUAXD`.
- Ngày: ngày chụp hoặc quay; không có thì ngày nhận file, ghi chú trong sổ.
- Không dấu tiếng Việt, không khoảng trắng, không tên khách hàng trong tên file; dự án dùng mã ẩn danh trong sổ.
- Ví dụ [Minh họa]: `TV-CH-0012_ACCURPRESS_CHUAXD_LD_20260915.jpg`.

**Mã nhóm máy (đề xuất theo file 04, 11):**
| Mã | Nhóm | Mã | Nhóm |
|---|---|---|---|
| CL | Máy cắt laser | LO | Máy lốc tôn CNC |
| HL | Máy hàn laser | CZ | Máy cán CZ |
| CH | Máy chấn CNC | DECK | Dây chuyền DECK |
| XT | Máy xén tôn thủy lực | XC | Dây chuyền xả tấm, xẻ băng, xả cuộn |
| DO | Máy đột CNC, cắt đột đa năng | RB | Robot và tự động hóa |
| BR | Máy bào rãnh V | PT | Thiết bị phụ trợ |
| GA | Máy gấp tự động | PK | Phụ kiện, phụ tùng, vật tư |

**Mã loại tài nguyên:**
| Mã | Loại |
|---|---|
| SP | Ảnh sản phẩm (tại kho, showroom hoặc do nhà cung cấp gửi) |
| LD | Ảnh lắp đặt tại khách |
| VCM | Video chạy máy |
| MGC | Ảnh hoặc video mẫu gia công |

Loại khác (ảnh sự kiện, ảnh đội ngũ) không thuộc bộ này; ghi "Ngoài phân loại" và hỏi người duyệt.

## 2. Bộ nhãn tìm kiếm

Mỗi tài nguyên gắn nhãn theo 6 trục, mỗi trục chọn trong danh sách, không tự đặt nhãn mới khi chưa được duyệt:
| Trục | Giá trị gợi ý |
|---|---|
| Nhóm máy | theo mã nhóm ở mục 1 |
| Nhà cung cấp | 9 nhà cung cấp trong file 07; "Khác — chờ xác nhận" |
| Bối cảnh | kho, showroom, nhà máy nhà cung cấp, nhà xưởng khách |
| Góc nhìn | toàn cảnh, cận chi tiết, bảng điều khiển, sản phẩm đầu ra |
| Vật liệu, công đoạn | chỉ ghi khi có nguồn (ví dụ cắt tấm, chấn, xả cuộn) |
| Thông tin nhạy cảm | có người, có logo khách, có bản vẽ hoặc tài liệu, có logo nhà cung cấp, không có |

## 3. Trạng thái sử dụng theo nguồn

| Nguồn | Điều kiện để đề xuất Được dùng đối ngoại | Mặc định khi thiếu |
|---|---|---|
| Tự chụp tại Nam Hải, không người, không thông tin khách | Người duyệt xác nhận | Chờ xác nhận quyền |
| Nhà cung cấp cung cấp, hoặc có logo, chứng nhận nhà cung cấp làm nội dung chính | Văn bản cho phép của nhà cung cấp do Mua hàng lưu + Giám đốc duyệt dùng ra ngoài (file 07, mục 2) | Chỉ nội bộ |
| Chụp, quay tại khách | Đồng ý ghi nhận được của khách: phạm vi hình ảnh, kênh, thời hạn, người duyệt (file 09, mục 3.5; file 06, điểm 6) | Chờ xác nhận quyền; có người hoặc nhà xưởng khách thì tối đa Chỉ nội bộ |
| Khách gửi | Như trên, kèm xác nhận khách là chủ hình ảnh | Chờ xác nhận quyền |

**Hiệu lực:** Hiện hành / Nghi lỗi thời — chờ xác nhận / Lỗi thời (đã xác nhận). Ảnh lỗi thời giữ trong sổ, không dùng cho tài liệu chào bán mới.

## 4. Kiểm trùng

1. Trùng chắc chắn: cùng nội dung (mã băm file nếu công cụ cho phép) hoặc cùng tên, dung lượng và ngày.
2. Nghi trùng: chụp liên tiếp cùng góc, cùng máy, cách nhau vài giây.
3. Đề xuất bản đại diện: độ phân giải cao hơn, rõ nét hơn, trạng thái quyền tốt hơn. Bản còn lại ghi "đề xuất lưu trữ", không xóa.
