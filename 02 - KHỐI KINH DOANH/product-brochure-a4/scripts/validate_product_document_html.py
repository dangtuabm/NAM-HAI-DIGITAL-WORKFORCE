#!/usr/bin/env python3
"""Kiểm tra cấu trúc tĩnh của tài liệu sản phẩm HTML A4 Nam Hải CNC."""

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class DocumentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pages = 0
        self.page_labels = []
        self.images = []
        self.text = []
        self._ignored = 0

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        classes = values.get("class", "").split()
        if tag == "section" and "page" in classes:
            self.pages += 1
            self.page_labels.append(values.get("aria-label", ""))
        if tag == "img" and values.get("src"):
            self.images.append(values["src"])
        if tag in {"script", "style"}:
            self._ignored += 1

    def handle_endtag(self, tag):
        if tag in {"script", "style"} and self._ignored:
            self._ignored -= 1

    def handle_data(self, data):
        if not self._ignored:
            self.text.append(data)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser()
    parser.add_argument("html", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--allow-placeholders", action="store_true")
    args = parser.parse_args()

    errors, warnings = [], []
    if not args.html.is_file():
        errors.append(f"Không tìm thấy file: {args.html}")
        result = {"passed": False, "errors": errors, "warnings": warnings}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        raise SystemExit(1)

    raw = args.html.read_text(encoding="utf-8")
    document = DocumentParser()
    document.feed(raw)

    if document.pages != 30:
        errors.append(f"Số trang là {document.pages}, yêu cầu 30")
    if len(set(document.page_labels)) != len(document.page_labels):
        errors.append("Có aria-label trang bị trùng")
    if any(not label for label in document.page_labels):
        warnings.append("Có trang thiếu aria-label")
    if "@media print" not in raw:
        errors.append("Không tìm thấy CSS dành cho in/PDF")
    if not re.search(r"@page\s*\{[^}]*size\s*:\s*A4\s+portrait", raw, re.I | re.S):
        errors.append("Không xác nhận được cấu hình in A4 portrait")
    if not any("logo" in src.lower() for src in document.images):
        errors.append("Không tìm thấy ảnh logo trong HTML")

    missing_assets = []
    for src in document.images:
        parsed = urlparse(src)
        if parsed.scheme in {"http", "https", "data"}:
            continue
        asset = (args.html.parent / unquote(parsed.path)).resolve()
        if not asset.is_file():
            missing_assets.append(src)
    if missing_assets:
        errors.append("Thiếu tài nguyên ảnh: " + ", ".join(sorted(set(missing_assets))))

    visible_text = " ".join(document.text)
    placeholders = sorted(set(re.findall(r"\[[^\]\r\n]{2,100}\]", visible_text)))
    if placeholders:
        message = "Placeholder còn lại: " + ", ".join(placeholders)
        if args.allow_placeholders:
            warnings.append(message)
        else:
            errors.append(message)

    if "logo-nam-hai-cnc-transparent.png" not in raw:
        warnings.append("Không thấy tên asset logo PNG chuẩn trong HTML")

    result = {
        "passed": not errors,
        "pages": document.pages,
        "page_labels": len(document.page_labels),
        "images": len(document.images),
        "placeholders": len(placeholders),
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
