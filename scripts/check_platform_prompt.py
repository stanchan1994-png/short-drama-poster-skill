#!/usr/bin/env python3
"""Lint a platform-ready prompt for length and common contamination."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BANNED_PHRASES = [
    "你给的",
    "你提供的",
    "参考你提供的",
    "如果你要",
    "我可以",
    "下面给你",
    "应该改成",
    "这一版",
    "再给你一版",
    "视觉上让人一眼明白",
    "这是XX设定",
    "改为",
    "改成",
    "保持为",
    "参考示例图",
    "按示例图",
]

REFERENCE_LABEL_PATTERNS = [
    re.compile(r"[\w\-. \u4e00-\u9fff]+?\.(?:png|jpg|jpeg|webp|gif|heic|psd)\b", re.IGNORECASE),
    re.compile(r"(?:/Users/|/Volumes/|[A-Za-z]:\\|\.{1,2}/)[^\s，。；、]+"),
    re.compile(r"(?:参考图|图片|附件|文件)\s*[A-Za-z0-9_-]+"),
]


def load_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def visible_length(text: str) -> int:
    return len("".join(text.split()))


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a platform-ready prompt.")
    parser.add_argument("path", nargs="?", help="Prompt text file. Reads stdin when omitted.")
    parser.add_argument("--max-chars", type=int, default=1900)
    args = parser.parse_args()

    text = load_text(args.path)
    failures: list[str] = []

    length = visible_length(text)
    if length > args.max_chars:
        failures.append(f"length {length} exceeds {args.max_chars}")

    for phrase in BANNED_PHRASES:
        if phrase in text:
            failures.append(f"banned phrase: {phrase}")

    for pattern in REFERENCE_LABEL_PATTERNS:
        for match in pattern.findall(text):
            failures.append(f"reference label/path: {match}")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"PASS length={length}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
