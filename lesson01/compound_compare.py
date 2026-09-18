# -*- coding: utf-8 -*-
"""
对比版：逐年对比单利与复利
  单利公式：本息 = 本金 * (1 + 年利率 * 年限)
  复利公式：本息 = 本金 * (1 + 年利率) ** 年限
检查点：本金 10000、年利率 5%、30 年后，复利比单利多 18219.42 元
表格使用固定列宽，中文按终端占 2 列计算，保证对齐。
"""

import unicodedata

P = 10000.0        # 本金（元）
r = 0.05           # 年利率
YEARS = 30         # 对比年限


def simple_amount(P, r, t):
    """单利本息。"""
    return P * (1 + r * t)


def compound_amount(P, r, t):
    """按年复利本息。"""
    return P * (1 + r) ** t


def display_width(text):
    """计算字符串在终端的显示宽度：中文/全角字符占 2 列。"""
    return sum(2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1
               for ch in text)


def pad_left(text, width):
    """右对齐：左侧补空格到指定显示宽度。"""
    return " " * (width - display_width(text)) + text


W0 = 6     # 年限列宽
W = 16     # 三个金额列宽

print("====== 单利与复利逐年对比（本金 10000 元，年利率 5%）======")
print(pad_left("年限", W0)
      + pad_left("单利本息(元)", W)
      + pad_left("复利本息(元)", W)
      + pad_left("差额(元)", W))
print("-" * (W0 + 3 * W))

for t in range(1, YEARS + 1):
    s = simple_amount(P, r, t)
    c = compound_amount(P, r, t)
    print(pad_left(str(t), W0)
          + f"{s:>{W},.2f}"
          + f"{c:>{W},.2f}"
          + f"{c - s:>{W},.2f}")

s30 = simple_amount(P, r, YEARS)
c30 = compound_amount(P, r, YEARS)
print("-" * (W0 + 3 * W))
print(f"{YEARS} 年后：单利 {s30:,.2f} 元，复利 {c30:,.2f} 元")
print(f"复利比单利多 {c30 - s30:,.2f} 元（检查点：18219.42）")
