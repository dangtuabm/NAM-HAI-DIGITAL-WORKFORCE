# Công thức tồn kho và tham số mặc định

Mọi tham số dưới đây là GIẢ ĐỊNH khởi đầu, Phó giám đốc Mua hàng xác nhận hoặc đổi.

## Mục lục
1. Ký hiệu
2. Công thức
3. Mức dịch vụ và hệ số z
4. Nhãn độ tin cậy
5. Phân loại trạng thái
6. Ví dụ [Minh họa]

## 1. Ký hiệu
- d: tiêu thụ trung bình mỗi ngày của mã (tổng xuất trong kỳ chia số ngày kỳ).
- s: độ lệch chuẩn của tiêu thụ ngày, tính từ các kỳ cùng độ dài.
- L: thời gian chờ tính bằng ngày lịch, từ lúc đặt hàng đến khi nhập kho.
- z: hệ số theo mức dịch vụ.
- SS: tồn an toàn. ROP: điểm đặt hàng lại.

## 2. Công thức
- SS = z × s × căn bậc hai của L (khi s tính theo ngày).
- ROP = d × L + SS.
- Số ngày đủ dùng = tồn hiện tại / d.
- Thời điểm đặt muộn nhất = ngày hôm nay + (số ngày đủ dùng − L − ngày đệm).
- Số lượng đề xuất = làm tròn lên theo quy cách và MOQ của (d × (L + chu kỳ rà) + SS − tồn hiện tại − hàng đang về). Ghi cả số chưa làm tròn.
- Tồn chậm luân chuyển: số ngày đủ dùng vượt ngưỡng do Mua hàng đặt (mặc định 365 ngày) hoặc không có xuất trong N kỳ.

## 3. Mức dịch vụ và hệ số z
| Mức dịch vụ | z |
|---|---|
| 90% | 1,28 |
| 95% | 1,65 |
| 98% | 2,05 |

Mặc định: 95% cho vật tư làm máy dừng khi hết (bép cắt, lăng kính đang dùng); 90% cho phụ kiện ít ảnh hưởng. Phân nhóm do Kỹ thuật và Mua hàng xác nhận.

## 4. Nhãn độ tin cậy
| Số kỳ lịch sử | Nhãn |
|---|---|
| 12 kỳ trở lên | CAO |
| 6 đến 11 kỳ | TRUNG BÌNH |
| Dưới 6 kỳ hoặc có đơn đột biến chưa giải thích | THẤP: không dùng để đặt số lượng lớn |

## 5. Phân loại trạng thái
| Trạng thái | Điều kiện |
|---|---|
| ĐẶT NGAY | Tồn hiện tại cộng hàng đang về nhỏ hơn hoặc bằng ROP |
| SẮP ĐẾN ĐIỂM ĐẶT | Tồn trên ROP nhưng dưới 1,25 lần ROP (ngưỡng giả định) |
| ĐỦ | Còn lại |
| TỒN CHẬM | Số ngày đủ dùng vượt ngưỡng chậm |
| THIẾU DỮ LIỆU | Thiếu tồn, tiêu thụ hoặc thời gian chờ |

## 6. Ví dụ [Minh họa, số không phải của Nam Hải CNC]
Mã X: d = 2 cái/ngày, s = 1 cái/ngày, L = 30 ngày, mức dịch vụ 95%.
SS = 1,65 × 1 × 5,477 = 9,04, làm tròn 10. ROP = 2 × 30 + 10 = 70.
Tồn 60 và không có hàng đang về: trạng thái ĐẶT NGAY.

## Lưu ý về tương thích
Bảng mã chỉ liệt kê mã và hãng theo tài liệu; mọi dòng "dùng cho máy nào" lấy từ tài liệu hãng hoặc Kỹ thuật xác nhận, ghi nguồn. Không điền theo trí nhớ hoặc theo hình dạng.
