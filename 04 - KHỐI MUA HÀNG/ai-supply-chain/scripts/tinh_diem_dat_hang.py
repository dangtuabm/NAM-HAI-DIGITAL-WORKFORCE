#!/usr/bin/env python3
"""Tinh tieu thu, ton an toan, diem dat hang lai tu CSV (chi dung thu vien chuan).

Cot dau vao bat buoc: ma_hang, ton_hien_tai, thoi_gian_cho_ngay, ky_ngay (so ngay moi ky),
  xuat_ky_1 ... xuat_ky_N (so luong xuat moi ky, N >= 1)
Cot tuy chon: hang_dang_ve, moq, quy_cach, muc_dich_vu (0.90/0.95/0.98), ngay_dem
Dung: python3 tinh_diem_dat_hang.py dau_vao.csv > ket_qua.csv
Ket qua la de xuat de nguoi duyet; khong thay the kiem tra.
"""
import csv, math, sys

Z = {0.90: 1.28, 0.95: 1.65, 0.98: 2.05}

def num(row, key, default=None):
    v = (row.get(key) or "").strip()
    if v == "":
        return default
    return float(v.replace(",", "."))

def main(path):
    out = csv.writer(sys.stdout)
    out.writerow(["ma_hang", "so_ky", "do_tin_cay", "d_ngay", "s_ngay", "ton_an_toan", "diem_dat_lai",
                  "so_ngay_du_dung", "trang_thai", "so_luong_de_xuat_chua_lam_tron", "so_luong_de_xuat", "ghi_chu"])
    with open(path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            ma = (row.get("ma_hang") or "").strip()
            try:
                ton = num(row, "ton_hien_tai"); L = num(row, "thoi_gian_cho_ngay"); kd = num(row, "ky_ngay")
            except ValueError:
                out.writerow([ma, "", "", "", "", "", "", "", "THIEU DU LIEU", "", "", "gia tri khong phai so"]); continue
            kys = []
            for k in sorted(c for c in row if c.startswith("xuat_ky_")):
                try:
                    v = num(row, k)
                except ValueError:
                    v = None
                if v is not None:
                    kys.append(v)
            if not ma or ton is None or L is None or not kd or not kys:
                out.writerow([ma, len(kys), "", "", "", "", "", "", "THIEU DU LIEU", "", "", "thieu ma, ton, thoi gian cho, do dai ky hoac lich su xuat"]); continue
            daily = [x / kd for x in kys]
            d = sum(daily) / len(daily)
            s = math.sqrt(sum((x - d) ** 2 for x in daily) / (len(daily) - 1)) if len(daily) > 1 else 0.0
            sl = num(row, "muc_dich_vu", 0.95)
            z = Z.get(round(sl, 2))
            if z is None:
                out.writerow([ma, len(kys), "", "", "", "", "", "", "THIEU DU LIEU", "", "", "muc dich vu khong thuoc 0.90/0.95/0.98"]); continue
            ss = z * s * math.sqrt(L)
            rop = d * L + ss
            dem = num(row, "ngay_dem", 0.0)
            ve = num(row, "hang_dang_ve", 0.0)
            days = ton / d if d > 0 else float("inf")
            pos = ton + ve
            if pos <= rop:
                st = "DAT NGAY"
            elif pos < 1.25 * rop:
                st = "SAP DEN DIEM DAT"
            else:
                st = "DU"
            raw = max(0.0, d * (L + dem) + ss - pos) if st != "DU" else 0.0
            moq = num(row, "moq", 1.0) or 1.0
            qc = num(row, "quy_cach", 1.0) or 1.0
            step = max(moq, qc)
            qty = math.ceil(raw / qc) * qc if raw > 0 else 0
            if 0 < qty < moq:
                qty = moq
            n = len(kys)
            conf = "CAO" if n >= 12 else ("TRUNG BINH" if n >= 6 else "THAP")
            out.writerow([ma, n, conf, round(d, 3), round(s, 3), math.ceil(ss), math.ceil(rop),
                          ("" if days == float("inf") else round(days, 1)), st, round(raw, 2), qty, ""])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
