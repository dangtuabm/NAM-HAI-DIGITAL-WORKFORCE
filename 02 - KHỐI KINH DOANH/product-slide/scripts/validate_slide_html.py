#!/usr/bin/env python3
"""Kiểm tra cấu trúc tĩnh của bộ slide HTML Nam Hải CNC."""

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class DeckParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = 0
        self.images = []
        self.text = []
        self._ignored = 0

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        classes = values.get("class", "").split()
        if tag == "section" and "slide" in classes:
            self.slides += 1
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
    args = parser.parse_args()
    errors, warnings = [], []
    if not args.html.is_file():
        errors.append(f"Không tìm thấy file: {args.html}")
        result = {"passed": False, "errors": errors, "warnings": warnings}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        raise SystemExit(1)

    raw = args.html.read_text(encoding="utf-8")
    deck = DeckParser()
    deck.feed(raw)
    if deck.slides != 12:
        errors.append(f"Số slide là {deck.slides}, yêu cầu 12")
    if "@media print" not in raw:
        warnings.append("Không tìm thấy CSS dành cho in/PDF")
    if not any("logo" in src.lower() for src in deck.images):
        errors.append("Không tìm thấy ảnh logo trong HTML")

    missing_assets = []
    for src in deck.images:
        parsed = urlparse(src)
        if parsed.scheme in {"http", "https", "data"}:
            continue
        asset = (args.html.parent / unquote(parsed.path)).resolve()
        if not asset.is_file():
            missing_assets.append(src)
    if missing_assets:
        errors.append("Thiếu tài nguyên ảnh: " + ", ".join(missing_assets))

    visible_text = " ".join(deck.text)
    placeholders = sorted(set(re.findall(r"\[[^\]\r\n]{2,80}\]", visible_text)))
    if placeholders:
        warnings.append("Placeholder còn lại: " + ", ".join(placeholders))

    result = {
        "passed": not errors,
        "slides": deck.slides,
        "images": len(deck.images),
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
