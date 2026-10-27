#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_page.py —「我最鍾意嘅地方」網站結構檢查工具
Structure checker for the HTML Final Project website.

【這個檔案唔需要交去學校（not part of the submission）】
它只是幫你在交功課之前，用電腦檢查一次網站是否符合題目要求：
    * 有 index.html 及 intro.html，加上其他網頁（至少 3 頁）
    * 有學過的所有 HTML 元素：<h1>-<h6>、<p>、<b>、<img>、<a href>、
      <ul>、<ol>、<li>、<table>、<tr>、<th>、<td>、style ...
    * 完全離線都用得（冇 JavaScript、冇外部圖片／字體）

用法 Usage:  python3 check_page.py
"""

import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES = ["index.html", "intro.html", "attractions.html", "visit.html"]

# 題目要求要有的 HTML 元素（全站合計）
REQUIRED_TAGS = [
    "h1", "h2", "h3", "h4", "h5", "h6", "p", "b", "i", "u", "small", "sup",
    "hr", "br", "img", "a", "ul", "ol", "li", "table", "tr", "th", "td",
    "style", "link",
]

results = []          # (是否通過, 描述)


def ok(passed, message):
    results.append((bool(passed), message))


class Collector(HTMLParser):
    """把一個 HTML 檔案的標籤、屬性、id、內文收集起來。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = {}          # 標籤 -> 出現次數
        self.elements = []      # (標籤, 屬性 dict)
        self.ids = set()
        self.text = ""
        self.script_count = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags[tag] = self.tags.get(tag, 0) + 1
        self.elements.append((tag, attrs))
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "script":
            self.script_count += 1

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_data(self, data):
        self.text += data


def parse(path):
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    p = Collector()
    p.feed(raw)
    return p, raw


def main():
    # ---------- 0. 檔案是否存在 ----------
    for name in PAGES:
        ok(os.path.isfile(os.path.join(ROOT, name)), f"檔案存在 file exists：{name}")
    for extra in ["css/style.css", "images/castle.svg", "images/train.svg",
                  "images/carousel.svg", "images/fireworks.svg"]:
        ok(os.path.isfile(os.path.join(ROOT, extra)), f"檔案存在 file exists：{extra}")
    if not all(p for p, _ in results):
        report()
        return 1

    parsed = {name: parse(os.path.join(ROOT, name)) for name in PAGES}

    # ---------- 1. 全站合計的標籤 ----------
    total = {}
    for p, _ in parsed.values():
        for tag, n in p.tags.items():
            total[tag] = total.get(tag, 0) + n
    for tag in REQUIRED_TAGS:
        ok(total.get(tag, 0) > 0, f"用了 <{tag}> 共 {total.get(tag, 0)} 次")

    # style 屬性的寫法（style="..."）也要用過
    inline_style = sum(1 for p, _ in parsed.values()
                       for t, d in p.elements if "style" in d
                       and t not in ("style", "link"))
    ok(inline_style >= 1, f"用了 style=\"...\" 行內樣式共 {inline_style} 次")

    # ---------- 2. 每頁的基本結構 ----------
    for name, (p, raw) in parsed.items():
        ok("lang" in dict(p.elements[0][1]) if p.elements else False,
           f"{name}：<html> 有 lang 屬性")
        ok('<meta charset="UTF-8">' in raw or "charset=\"UTF-8\"" in raw,
           f"{name}：有設定 UTF-8 編碼（中文才不會變亂碼）")
        ok(p.tags.get("title", 0) == 1, f"{name}：有一個 <title>")
        ok(p.tags.get("h1", 0) >= 1, f"{name}：有 <h1> 大標題")
        ok(p.tags.get("nav", 0) == 1, f"{name}：有一個導覽列 <nav>")
        ok(p.tags.get("main", 0) == 1, f"{name}：有一個 <main> 主要內容")
        ok(p.tags.get("footer", 0) == 1, f"{name}：有一個 <footer> 填姓名班別")

        # 導覽列要有 4 個連結（4 個網頁互相連通）
        nav_links = [d.get("href") for t, d in p.elements
                     if t == "a" and d.get("href", "").endswith(".html")]
        for target in PAGES:
            ok(target in nav_links, f"{name}：導覽列有連去 {target}")

        # 圖片一定要有 alt 屬性
        imgs = [d for t, d in p.elements if t == "img"]
        ok(len(imgs) >= 1, f"{name}：有 <img> 圖片")
        ok(all("alt" in d and d["alt"].strip() for d in imgs),
           f"{name}：所有圖片都有 alt 文字")

        # 表格要有表頭 <th>
        if p.tags.get("table", 0):
            ok(p.tags.get("th", 0) >= 1, f"{name}：表格用了 <th> 表頭")

        # 清單要有 <li>
        list_items = p.tags.get("ul", 0) + p.tags.get("ol", 0)
        ok(p.tags.get("li", 0) >= list_items, f"{name}：清單有 <li> 項目")

        # ---------- 3. 離線要求 ----------
        ok(p.script_count == 0, f"{name}：冇使用 <script>（老師要求不用 JavaScript）")
        external = [d.get("src") or d.get("href") for t, d in p.elements
                    if t in ("img", "link") and (d.get("src") or d.get("href"))
                    and str(d.get("src") or d.get("href")).startswith(("http://", "https://", "//"))]
        ok(not external,
           f"{name}：圖片和樣式表都是本機檔案（沒有連去網上）"
           + (f"　發現：{external}" if external else ""))

        # 內部連結的檔案和錨點要真的存在
        for t, d in p.elements:
            if t != "a":
                continue
            href = d.get("href", "")
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            target, _, anchor = href.partition("#")
            if target:          # 另一個網頁
                ok(os.path.isfile(os.path.join(ROOT, target)),
                   f"{name}：連結 {href} 的檔案存在")
            if anchor:          # 頁內錨點
                tp, _ = parsed.get(target or name, (None, None))
                ok(tp is not None and anchor in tp.ids,
                   f"{name}：連結 {href} 的錨點存在")

        # 圖片檔案真的存在
        for d in imgs:
            src = d.get("src", "")
            ok(os.path.isfile(os.path.join(ROOT, src)) if src and not src.startswith("http") else False,
               f"{name}：圖片檔案存在 {src}")

    # ---------- 4. CSS 也要離線 ----------
    with open(os.path.join(ROOT, "css", "style.css"), encoding="utf-8") as f:
        css = f.read()
    ok("url(http" not in css, "style.css：冇載入網上字體或圖片（離線都用得）")

    return report()


def report():
    passed = sum(1 for p, _ in results if p)
    failed = len(results) - passed
    print("=" * 68)
    print("「我最鍾意嘅地方」網站結構檢查報告")
    print("=" * 68)
    for p, msg in results:
        print(("  ✔ " if p else "  ✘ ") + msg)
    print("-" * 68)
    print(f"通過 passed: {passed}　失敗 failed: {failed}")
    if failed:
        print("請先修正上面 ✘ 的項目，再交功課。")
    else:
        print("全部檢查通過，可以交功課了！All checks passed.")
    print("=" * 68)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())