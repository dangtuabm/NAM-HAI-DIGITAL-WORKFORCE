# Sơ đồ DATA và ví dụ cây thư mục — Nam Hải CNC

Đọc ở Bước 4 khi đặt cây đề xuất vào HUB. Cây thật luôn lấy từ nguồn của nhiệm vụ; các ví dụ dưới đây chỉ để minh họa vị trí và cách đặt tên.

## 1. Sơ đồ DATA cố định

```
3. DATA - DỮ LIỆU/
  00 - INDEX DATA NAM HAI CNC.md
  01 - NHÀ CUNG CẤP & SẢN PHẨM/<HÃNG>/<NHÓM MÁY>/<DÒNG hoặc MODEL>/<HỒ SƠ ...>/
  02 - BẢNG GIÁ NIÊM YẾT [ĐỎ]/<HÃNG> - <NHÓM MÁY> - <năm hiệu lực>/
  03 - QUY CHẾ & CHÍNH SÁCH NỘI BỘ/
  04 - HÌNH ẢNH & LOGO/
    01 - LOGO NAM HAI CNC
    02 - LOGO THUONG HIEU NHA CUNG CAP
    03 - ANH MAY THEO HANG/<HÃNG>/<NHÓM MÁY>/<MODEL>/
    04 - HINH ANH MO TA DUNG CHUNG
  05 - HỒ SƠ DOANH NGHIỆP/
```

Ánh xạ cấp phân loại của Skill vào sơ đồ:

| Cấp phân loại | Cấp thư mục trong `01 - NHÀ CUNG CẤP & SẢN PHẨM` |
|---|---|
| Nhà cung cấp | `<HÃNG>` — tên chuẩn: ACCURPRESS · CNHAWE · SENFENG · JQ LASER · NHCTECH · HYMSON · REEGAO · DEHAHA · ZMDE · JIANMENG |
| Loại máy | `<NHÓM MÁY>` — dùng tên nhóm sản phẩm chuẩn (file 11 mục 2), ví dụ MÁY CHẤN CNC, MÁY CẮT LASER, MÁY CẮT ỐNG LASER |
| Dòng máy | `DÒNG <tên dòng>` khi nguồn có dòng máy |
| Model | `<MODEL>` hoặc thư mục hồ sơ ghi model, khi nguồn có model |
| Hồ sơ | `HỒ SƠ <loại> <model/dòng> <mốc nguồn>` chứa `index.html`, tệp nguồn, `assets/`, `NGUỒN.txt` |

Hãng chưa có trong danh sách tên chuẩn: ghi tên theo nguồn và đánh dấu "chờ xác nhận tên chuẩn".

## 2. Ví dụ cây (theo cấu trúc HUB hiện có)

```
01 - NHÀ CUNG CẤP & SẢN PHẨM/
  JQ LASER/
    MÁY CẮT ỐNG LASER/
      DÒNG HTS/
        HỒ SƠ BÁO GIÁ FLT-12050HTS 2025/
      DÒNG KS/
        HỒ SƠ BÁO GIÁ KS120 1.5-3KW 2025/
  NHCTECH/
    MÁY CẮT ỐNG LASER/
      DÒNG C/
        HỒ SƠ G120C 6000W 23-07-2026/
  CNHAWE/
    MÁY CHẤN CNC/
      DÒNG HPC/                      [Minh họa]
        HPC-110-3100/                [Minh họa]
```

Ảnh máy cùng model đặt ở `04 - HÌNH ẢNH & LOGO/03 - ANH MAY THEO HANG/CNHAWE/MÁY CHẤN CNC/HPC-110-3100/` [Minh họa], tên ảnh `HPC-110-3100_1.jpg`, `HPC-110-3100_2.png`.

## 3. Quy ước đi kèm

- Bảng giá hãng không đặt trong cây sản phẩm; đặt ở `02 - BẢNG GIÁ NIÊM YẾT [ĐỎ]/<HÃNG> - <NHÓM MÁY> - <năm hiệu lực>/`.
- Không ghi đè: bản mới đặt cạnh bản cũ với mốc hiệu lực mới; bản cũ chuyển sang `7. ARCHIVE - LƯU TẠM TRƯỚC KHI XÓA` khi người có thẩm quyền đồng ý.
- Tên thư mục chuẩn hóa Unicode dạng NFC; giữ dấu tiếng Việt.

*Nam Hải CNC — 09/10/2026 · Bản nháp chờ duyệt*
