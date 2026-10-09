# Nơi lưu kết quả làm phẳng và mẫu NGUỒN.txt

Đọc ở Bước 1 (chọn nhánh lưu) và Bước 6 (kiểm gói).

## 1. Chọn nhánh lưu trong `3. DATA - DỮ LIỆU/`

| Loại tài liệu nguồn | Nhánh lưu | Mức dữ liệu |
|---|---|---|
| Catalog, hồ sơ kỹ thuật, báo giá hãng theo một model hoặc một dòng | `01 - NHÀ CUNG CẤP & SẢN PHẨM/<HÃNG>/<NHÓM MÁY>/<DÒNG hoặc MODEL>/<HỒ SƠ ...>/` | Catalog [XANH]; hồ sơ có giá hãng [ĐỎ] |
| Bảng giá niêm yết của nhà cung cấp cho cả nhóm máy | `02 - BẢNG GIÁ NIÊM YẾT [ĐỎ]/<HÃNG> - <NHÓM MÁY> - <năm hiệu lực>/` | [ĐỎ] — Mua hàng, Kinh doanh, CEO |
| Quy chế, chính sách nội bộ | `03 - QUY CHẾ & CHÍNH SÁCH NỘI BỘ/` theo mức Vàng/Đỏ đã ghi trên thư mục | Theo quy chế |
| Hồ sơ doanh nghiệp | `05 - HỒ SƠ DOANH NGHIỆP/` | Theo người phụ trách |

Tên hãng chuẩn: ACCURPRESS · CNHAWE · SENFENG · JQ LASER · NHCTECH · HYMSON · REEGAO · DEHAHA · ZMDE · JIANMENG. Hãng khác: ghi theo nguồn, đánh dấu chờ xác nhận tên chuẩn.

Ví dụ nhánh đang có: `01 - NHÀ CUNG CẤP & SẢN PHẨM/JQ LASER/MÁY CẮT ỐNG LASER/DÒNG HTS/HỒ SƠ BÁO GIÁ FLT-12050HTS 2025/`.

## 2. Thành phần một gói

```
<HỒ SƠ ...>/
  index.html        bản tra cứu phẳng, có liên kết về trang/slide nguồn
  <tệp nguồn>.pdf|docx|pptx   bản sao nguyên trạng
  assets/           ảnh trang/slide, ảnh nhúng
  NGUỒN.txt         dấu vết nguồn
```

## 3. Mẫu NGUỒN.txt

```
File nguồn: <tên file nguồn đúng như bản gốc>
SHA-256 nguồn: <mã băm 64 ký tự của file nguồn>
Trang PDF: <số trang> | Slide: <số slide>
Mốc trong tên file: <DD-MM-YYYY hoặc năm, nếu có>
Ngày trong tài liệu: <nếu có>
Ngày làm phẳng: <DD/MM/YYYY>
Giới hạn trích xuất: <OCR không chắc, trang chỉ có ảnh, bảng ngắt trang... hoặc "Không">
```

## 4. Quy tắc cập nhật

- Không ghi đè gói đã có. Bản mới đặt cạnh bản cũ với mốc hiệu lực mới; bản cũ chuyển sang `7. ARCHIVE - LƯU TẠM TRƯỚC KHI XÓA` khi người phụ trách đồng ý.
- Sau khi tạo gói, đề nghị người phụ trách cập nhật `3. DATA - DỮ LIỆU/00 - INDEX DATA NAM HAI CNC.md`; không tự sửa INDEX khi chưa được giao.

*Nam Hải CNC — 09/10/2026 · Bản nháp chờ duyệt*
