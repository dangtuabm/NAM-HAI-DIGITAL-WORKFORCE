# QUY ƯỚC PHIÊN BẢN HỒ SƠ GIAO DỊCH — NAM HẢI CNC

Đọc ở bước 2, 3 và 6. Mọi quy ước dưới đây là đề xuất mặc định; Phó giám đốc Backoffice ban hành quy ước chính thức.

## 1. Quy ước đặt tên tệp

Mẫu: `<MÃ GIAO DỊCH>_<LOẠI>_<KHÁCH>_v<SỐ BẢN>_<YYYYMMDD>_<TRẠNG THÁI>`

| Thành phần | Quy ước |
|---|---|
| Loại | BG (báo giá), HD (hợp đồng), PL (phụ lục), KT (tài liệu kỹ thuật), NT (hồ sơ nghiệm thu) |
| Số bản | v1, v2, v3 tăng dần; không dùng "final", "moi", "cuoi" |
| Ngày | Ngày tạo bản, định dạng năm tháng ngày liền nhau để sắp xếp |
| Trạng thái | NHAP, CHODUYET, DADUYET, DAGUI, THAYTHE |
| Ký tự | Không dấu, không khoảng trắng, dùng gạch dưới |

Ví dụ minh họa [Minh họa]: `GD0001_BG_KHACHA_v2_20261006_CHODUYET`.

## 2. Vòng đời trạng thái

| Trạng thái | Ý nghĩa | Ai xác nhận chuyển |
|---|---|---|
| NHAP | Đang soạn, chưa ai duyệt | Người soạn |
| CHODUYET | Đã chuyển người có thẩm quyền | Người soạn |
| DADUYET | Người có thẩm quyền đã duyệt | Người có thẩm quyền |
| DAGUI | Đã gửi khách hoặc nhà cung cấp | Người gửi |
| THAYTHE | Bị bản mới thay | Người có thẩm quyền xác nhận bản mới |

A.I chỉ ghi trạng thái theo xác nhận bằng văn bản hoặc lời người có thẩm quyền; không suy từ tên tệp.

## 3. Loại thay đổi và người duyệt (theo file 10, mục 8)

| Loại thay đổi | Ví dụ | Người cần duyệt |
|---|---|---|
| Thương mại | Giá, chiết khấu, điều kiện thanh toán, tiến độ, bảo hành | Người có thẩm quyền thương mại |
| Kỹ thuật | Cấu hình, thông số, phạm vi cung cấp, điều kiện mặt bằng | Kỹ thuật xác nhận |
| Pháp lý | Điều khoản trách nhiệm, phạt, chấm dứt | Người có thẩm quyền, tham vấn chuyên gia pháp lý |
| Hình thức | Lỗi chính tả, định dạng | Người soạn, người rà |

Kinh doanh không tự đổi cấu hình khi chưa có xác nhận kỹ thuật; Kỹ thuật không tự quyết giá.

## 4. Nội dung một dòng trong sổ phiên bản

Số bản, tên tệp, ngày, người soạn, mô tả thay đổi một câu, trạng thái, người duyệt, ngày duyệt, ghi chú, nơi lưu. Ô không biết ghi "chưa rõ", không điền suy đoán.

## 5. Dấu hiệu cần cảnh báo

- Hai bản cùng trạng thái DADUYET cho một hồ sơ.
- Bản DAGUI không có người duyệt ghi nhận.
- Tệp cùng tên khác nội dung.
- Thông số hoặc tên khách trong bản không khớp mã giao dịch (có thể lẫn dự án khác).
- Bản mới bỏ điều khoản mà bản trước có, không có ghi chú lý do.

*Nam Hải CNC — 06/10/2026 · Bản nháp chờ duyệt*
