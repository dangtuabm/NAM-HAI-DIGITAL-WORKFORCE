#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm máy một gói Skill theo chuẩn Nam Hải CNC (09/10/2026).

Cách dùng:
    python3 kiem_tra_skill.py "<đường dẫn thư mục Skill>" [phiên bản] [...]
    python3 kiem_tra_skill.py --nhom "<đường dẫn thư mục nhóm>"   (kiểm mọi Skill trong nhóm)

Kiểm: khối YAML; name = tên thư mục; description <= 600 ký tự; metadata đủ trường,
skill_id "NHC-<SLUG-IN-HOA>", owner "Nam Hải CNC — <chức danh>", status hợp lệ;
07 phần đúng tên và thứ tự + phần ngoài 07 phần; thân 120–300 dòng;
không có chữ "AI" trần; không còn placeholder rỗng; không emoji;
evals.json (>= 8 ca, đủ khóa, baseline no-skill, đủ loại ca);
file references/ và templates/ được nhắc phải tồn tại; reference > 100 dòng có Mục lục.
Kết quả: PASS / FAIL kèm danh sách lỗi; mã thoát 0 khi tất cả PASS.
"""
import glob
import json
import os
import re
import sys
import unicodedata

HEADINGS = [
    "1. MÔ TẢ",
    "2. KHI NÀO DÙNG – KHI NÀO KHÔNG DÙNG",
    "3. INPUT",
    "4. OUTPUT",
    "5. PROCESS",
    "6. CHECKLIST TIÊU CHUẨN ĐẦU RA",
    "7. CÁC LƯU Ý – ĐIỀU KHOẢN",
]
TAIL = "## TÀI NGUYÊN, KIỂM THỬ VÀ QUẢN TRỊ — NGOÀI 07 PHẦN"
STATUS_OK = {"draft", "pilot", "active"}
EVAL_KEYS = ["id", "type", "source", "prompt", "expected_behavior", "evidence"]
EVAL_TYPES = ["must_trigger", "semantic_positive", "missing_input", "red_line", "no_false_ask", "injection"]
MIN_EVALS = 8
PLACEHOLDER = re.compile(
    r"\[(?:ĐIỀN|DIEN|TODO|TBD|\.\.\.|…)[^\]]*\]|\bTODO\b|\bTBD\b|\bXXX\b|\{\{[^}]*\}\}|<điền[^>]*>",
    re.IGNORECASE,
)
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F02F]")
CODE_SPAN = re.compile(r"`[^`\n]*`")


def nfc(s):
    return unicodedata.normalize("NFC", s)


def read(p):
    with open(p, encoding="utf-8") as f:
        return nfc(f.read())


def parse_yaml(fm):
    try:
        import yaml  # type: ignore
        y = yaml.safe_load(fm) or {}
        return y, None
    except ImportError:
        pass
    except Exception as e:  # YAML lỗi cú pháp
        return None, "YAML không đọc được: %s" % e
    # Dự phòng khi máy không có PyYAML: đọc các trường cần kiểm
    y = {"metadata": {}}
    m = re.search(r"^name:\s*(.+)$", fm, re.M)
    y["name"] = m.group(1).strip().strip('"') if m else None
    m = re.search(r"^description:\s*>?\s*\n((?:[ \t]+.*\n?)+)", fm, re.M)
    if m:
        y["description"] = " ".join(l.strip() for l in m.group(1).splitlines())
    else:
        m = re.search(r"^description:\s*(.+)$", fm, re.M)
        y["description"] = m.group(1).strip().strip('"') if m else None
    for k in ["version", "updated", "owner", "skill_id", "status"]:
        m = re.search(r"^[ \t]+%s:\s*\"?([^\"\n]*)\"?" % k, fm, re.M)
        if m:
            y["metadata"][k] = m.group(1).strip()
    return y, None


def check(path, ver=None):
    path = path.rstrip("/\\")
    slug = nfc(os.path.basename(path))
    err, warn = [], []
    sk = os.path.join(path, "SKILL.md")
    if not os.path.isfile(sk):
        return "FAIL", ["thiếu SKILL.md"], [], ""
    t = read(sk)
    m = re.match(r"---\n(.*?)\n---\n(.*)", t, re.S)
    if not m:
        return "FAIL", ["không có khối YAML ở đầu file"], [], ""
    fm, body = m.group(1), m.group(2)
    y, yerr = parse_yaml(fm)
    if yerr:
        return "FAIL", [yerr], [], ""
    name = str(y.get("name") or "")
    desc = " ".join(str(y.get("description") or "").split())
    md = y.get("metadata") or {}
    if name != slug:
        err.append("name (%s) khác tên thư mục (%s)" % (name, slug))
    if not desc:
        err.append("thiếu description")
    elif len(desc) > 600:
        err.append("description %d ký tự > 600" % len(desc))
    for k in ["version", "updated", "owner", "skill_id", "status"]:
        if not md.get(k):
            err.append("metadata thiếu %s" % k)
    if md.get("skill_id") and str(md["skill_id"]) != "NHC-" + slug.upper():
        err.append("skill_id phải là NHC-%s" % slug.upper())
    if md.get("owner") and not str(md["owner"]).startswith("Nam Hải CNC — "):
        err.append('owner phải dạng "Nam Hải CNC — <chức danh>"')
    st = str(md.get("status") or "")
    if st and st not in STATUS_OK and not st.startswith("approved") and not st.startswith("noi-dung-da-duyet"):
        err.append("status '%s' không hợp lệ (draft/pilot/active, approved-... hoặc noi-dung-da-duyet-...)" % st)
    if ver and str(md.get("version")) != ver:
        err.append("version %s khác %s" % (md.get("version"), ver))
    if md.get("updated") and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(md["updated"])):
        err.append("updated phải dạng YYYY-MM-DD")

    heads = re.findall(r"^## (\d\..*?)\s*$", body, re.M)
    if heads != HEADINGS:
        err.append("07 phần sai tên/thứ tự: %s" % heads)
    if TAIL not in body:
        err.append("thiếu phần '%s'" % TAIL[3:])
    elif heads and body.find(TAIL) < body.find("## 7."):
        err.append("phần ngoài 07 phần phải đặt sau phần 7")
    nl = len(body.strip().splitlines())
    if not 120 <= nl <= 300:
        err.append("thân %d dòng (chuẩn 120–300)" % nl)

    # Nội dung chữ để kiểm: SKILL.md, references, evals (bỏ templates vì mẫu được phép có ô điền)
    files = [sk] + glob.glob(os.path.join(path, "references", "**", "*.md"), recursive=True)
    ev_path = os.path.join(path, "evals.json")
    if os.path.isfile(ev_path):
        files.append(ev_path)
    for f in files:
        rel = os.path.relpath(f, path)
        txt = read(f)
        plain = CODE_SPAN.sub("", re.sub(r"^\s*skill_id:.*$", "", txt, flags=re.M))
        n_ai = len(re.findall(r"\bAI\b", plain))
        if n_ai:
            err.append('%s: %d chữ "AI" trần (viết "A.I")' % (rel, n_ai))
        ph = PLACEHOLDER.findall(txt)
        if ph:
            warn.append("%s: có placeholder %s — kiểm xem là trường mẫu có chủ đích hay chỗ quên điền" % (rel, sorted(set(ph))[:5]))
        if EMOJI.search(txt):
            err.append("%s: có emoji" % rel)
        if rel.startswith("references") and len(txt.splitlines()) > 100 and "mục lục" not in txt.lower():
            err.append("%s: dài hơn 100 dòng nhưng thiếu Mục lục" % rel)

    # evals.json
    if not os.path.isfile(ev_path):
        err.append("thiếu evals.json")
        nev = 0
    else:
        try:
            e = json.load(open(ev_path, encoding="utf-8"))
            ev = e.get("evals", [])
            nev = len(ev)
            if nev < MIN_EVALS:
                err.append("evals %d ca < %d" % (nev, MIN_EVALS))
            if e.get("baseline") != "no-skill":
                err.append('evals: baseline phải là "no-skill"')
            for x in ev:
                miss = [k for k in EVAL_KEYS if k not in x or x[k] in (None, "", [])]
                if miss:
                    err.append("evals ca %s thiếu %s" % (x.get("id"), miss))
                if not isinstance(x.get("expected_behavior"), list):
                    err.append("evals ca %s: expected_behavior phải là danh sách" % x.get("id"))
            types = {x.get("type") for x in ev}
            for tt in EVAL_TYPES:
                if tt not in types:
                    err.append("evals thiếu loại ca %s" % tt)
            if not ({"must_not_trigger", "boundary"} & types):
                err.append("evals thiếu ca must_not_trigger hoặc boundary")
        except Exception as ex:
            err.append("evals.json không đọc được: %s" % ex)
            nev = 0

    # Tài nguyên được nhắc phải tồn tại
    refs = set(re.findall(r"`((?:references|templates|assets|scripts)/[^`\s]+)`", body))
    refs |= set(re.findall(r"\]\(((?:references|templates|assets|scripts)/[^)\s]+)\)", body))
    for r in sorted(refs):
        if not os.path.exists(os.path.join(path, r)):
            err.append("tài nguyên không tồn tại: %s" % r)
    for d in ["references", "templates", "assets", "scripts"]:
        dp = os.path.join(path, d)
        if os.path.isdir(dp) and not os.listdir(dp):
            warn.append("thư mục %s rỗng" % d)

    info = "dòng thân=%d · description=%d ký tự · số ca=%d · status=%s" % (nl, len(desc), nev, st)
    return ("PASS" if not err else "FAIL"), err, warn, info


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    paths, ver = [], None
    if argv[0] == "--nhom":
        root = argv[1]
        paths = sorted(p for p in glob.glob(os.path.join(root, "*")) if os.path.isfile(os.path.join(p, "SKILL.md")))
    else:
        paths = [argv[0]]
        ver = argv[1] if len(argv) > 1 else None
    all_ok = True
    for p in paths:
        kq, err, warn, info = check(p, ver)
        all_ok &= kq == "PASS"
        print("%s  %s  (%s)" % (kq, nfc(os.path.basename(p.rstrip("/\\"))), info))
        for x in err:
            print("   - LỖI: " + x)
        for x in warn:
            print("   - LƯU Ý: " + x)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
