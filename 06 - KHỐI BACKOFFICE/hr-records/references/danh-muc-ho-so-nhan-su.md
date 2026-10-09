# DANH MỤC HỒ SƠ NHÂN SỰ, QUY ƯỚC LƯU TRỮ VÀ PHÂN QUYỀN — NAM HẢI CNC

Bản đề xuất [GIẢ ĐỊNH] chờ Phó giám đốc Backoffice xác nhận. Không phải ý kiến pháp lý: loại giấy tờ bắt buộc theo luật và thời gian lưu giữ do người có thẩm quyền và chuyên gia xác nhận.

## Mục lục
1. Nguyên tắc làm việc trên siêu dữ liệu
2. Danh mục hồ sơ theo nhóm vị trí
3. Quy ước đặt tên và thư mục
4. Dữ liệu Đỏ và cách che
5. Ma trận phân quyền đề xuất
6. Ngưỡng cảnh báo hạn

## 1. Nguyên tắc làm việc trên siêu dữ liệu
- A.I chỉ nhận: mã nhân viên, chức danh, khối, nhóm, loại hồ sơ, có/không, ngày ký, ngày hiệu lực, ngày hết hạn, nơi lưu, người được xem.
- Bảng nối mã nhân viên với họ tên do Backoffice giữ ngoài công cụ A.I.
- Không mở nội dung hợp đồng, lý lịch, giấy khám sức khỏe để tóm tắt hay "đoán loại".

## 2. Danh mục hồ sơ theo nhóm vị trí

### 2.1. Nhóm chung — mọi nhân viên
| Mã loại | Hồ sơ | Có hạn? | Ghi chú |
|---|---|---|---|
| HD | Hợp đồng lao động (hoặc hợp đồng thử việc, hợp đồng cộng tác) | Có, theo loại hợp đồng | Mỗi lần ký mới là một file riêng |
| PL | Phụ lục hợp đồng | Theo phụ lục | Gắn số hợp đồng gốc |
| QD | Quyết định nhân sự (tiếp nhận, bổ nhiệm, điều chuyển, thôi việc) | Theo quyết định | Chỉ lưu bản đã ký |
| LL | Sơ yếu lý lịch | Không | Bản đã che dữ liệu Đỏ khi cần đưa vào công cụ A.I |
| GT | Giấy tờ tùy thân (bản sao) | Có thể có | Dữ liệu Đỏ: chỉ ghi có/không và ngày hết hạn |
| BC | Bằng cấp, chứng chỉ chuyên môn | Tùy loại | Ghi tên bằng, nơi cấp, ngày cấp |
| SK | Giấy khám sức khỏe | Theo quy định nội bộ | Dữ liệu Đỏ: chỉ ghi có/không và ngày |
| CK | Cam kết bảo mật thông tin, nội quy đã ký | Không | Đặc biệt cho người tiếp cận giá, hồ sơ thương vụ |
| BG | Biên bản bàn giao tài sản, thiết bị, tài khoản | Không | Cập nhật khi vào và khi nghỉ |

### 2.2. Bổ sung — Khối Kỹ thuật (tổ Gia công nguội, tổ Hàn – Cắt laser)
| Mã loại | Hồ sơ | Có hạn? | Ghi chú |
|---|---|---|---|
| AT | Thẻ hoặc chứng nhận huấn luyện an toàn, vệ sinh lao động | Có | Nhóm huấn luyện và hạn theo văn bản cấp; Trưởng nhóm Kỹ thuật xác nhận yêu cầu cho vị trí |
| CN | Chứng chỉ nghề hoặc chứng nhận đào tạo của hãng thiết bị | Tùy loại | Ghi hãng, dòng máy theo văn bản, không suy rộng sang model khác |
| DV | Chứng chỉ vận hành thiết bị đặc thù nếu vị trí yêu cầu (ví dụ nâng hạ, điện) | Có | Danh sách thiết bị cần chứng chỉ do Trưởng nhóm xác nhận |

### 2.3. Bổ sung — Nhân viên kho
| AT | Huấn luyện an toàn khi bốc xếp, nâng hạ nếu được giao | Có | Theo xác nhận của Phó giám đốc Backoffice |

### 2.4. Bổ sung — Mua hàng quốc tế, Kinh doanh, quản lý
- CK bắt buộc cho người tiếp cận giá nhập, giá bán, hồ sơ nhà cung cấp.
- QD ủy quyền nếu được giao ký hoặc duyệt trong hạn mức.

## 3. Quy ước đặt tên và thư mục
- Thư mục: `NHAN SU/<Ma NV>/<Ma loai>/` ; người đã nghỉ chuyển sang `NHAN SU/_DA NGHI/<Ma NV>/`.
- Tên file: `<Ma NV>_<Ma loai>_<So hieu neu co>_<YYYYMMDD ngay ky>_v<so>`; ví dụ [Minh họa] `NV012_HD_03-2026_20260115_v1.pdf`.
- Không ghi họ tên, số căn cước, mức lương vào tên file hay tên thư mục.
- Bản sửa không ghi đè: tăng số phiên bản; bản hết hiệu lực giữ nguyên, chuyển thư mục con `_HET HIEU LUC`.

## 4. Dữ liệu Đỏ và cách che
| Dữ liệu | Cách xử lý trước khi đưa vào công cụ A.I |
|---|---|
| Số căn cước, hộ chiếu | Bỏ hẳn; chỉ ghi "có bản sao: Có/Không", ngày hết hạn |
| Số tài khoản ngân hàng | Bỏ hẳn |
| Lương, phụ cấp, thưởng | Bỏ hẳn |
| Kết quả khám sức khỏe, bệnh lý | Bỏ hẳn; chỉ ghi có giấy và ngày |
| Địa chỉ nhà, số điện thoại cá nhân, người thân | Bỏ hẳn |
| Họ tên | Thay bằng mã nhân viên |
| Mật khẩu, OTP, khóa truy cập | Không bao giờ đưa vào |

## 5. Ma trận phân quyền đề xuất
| Nhóm hồ sơ | Xem | Sửa, thêm | Ghi chú |
|---|---|---|---|
| HD, PL, QD | Giám đốc, Phó giám đốc Backoffice | Phó giám đốc Backoffice hoặc người được giao | Kế toán xem phần cần cho lương theo phân công |
| LL, GT, SK | Phó giám đốc Backoffice | Phó giám đốc Backoffice | Dữ liệu Đỏ, hạn chế tối đa |
| BC, AT, CN, DV | Phó giám đốc Backoffice; Trưởng nhóm Kỹ thuật xem của tổ mình | Phó giám đốc Backoffice | Phục vụ phân công lắp đặt, chạy thử |
| CK, BG | Phó giám đốc Backoffice; phó giám đốc khối của người đó | Phó giám đốc Backoffice | |
| Mỗi nhân viên | Được xem hồ sơ của chính mình theo quy định nội bộ | Không | |

Công cụ A.I không được cấp quyền đọc thư mục gốc; chỉ nhận bản liệt kê hoặc bản đã che.

## 6. Ngưỡng cảnh báo hạn
| Mức | Điều kiện | Người nhận |
|---|---|---|
| QUÁ HẠN | Ngày hết hạn trước ngày chốt | Phó giám đốc Backoffice, ngay |
| DƯỚI 30 NGÀY | Còn 0–30 ngày | Phó giám đốc Backoffice; Trưởng nhóm nếu là AT, CN, DV |
| DƯỚI 60 NGÀY | Còn 31–60 ngày | Phó giám đốc Backoffice |
| CHƯA CÓ NGÀY | Hồ sơ có hạn nhưng thiếu ngày hết hạn | Phó giám đốc Backoffice bổ sung |

Ngưỡng 60/30 ngày là [GIẢ ĐỊNH]. Hợp đồng sắp hết hạn chỉ được trình, không kèm ý kiến gia hạn hay không.
