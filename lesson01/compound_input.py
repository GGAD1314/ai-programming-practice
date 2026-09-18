# -*- coding: utf-8 -*-
"""
交互版：从键盘输入本金、年利率、年限，校验通过后再计算复利
校验规则：
  1. 输入必须是数字（非数字要重新输入）
  2. 本金必须大于 0
  3. 年利率不能为负数（检查点：拦截负利率）
  4. 年限必须大于 0
"""


def input_number(prompt):
    """反复提示，直到用户输入一个合法数字。"""
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("  [提示] 输入无效，请输入数字。")


def input_until(prompt, condition, tip):
    """反复提示，直到输入的数字满足 condition 条件。"""
    value = input_number(prompt)
    while not condition(value):
        print(f"  [拦截] {tip}")
        value = input_number(prompt)
    return value


print("====== 交互版：复利计算器 ======")

# 本金必须大于 0
P = input_until("请输入本金（元）：",
                lambda x: x > 0,
                "本金必须大于 0，请重新输入。")

# 年利率不能为负数（允许 0%）
r = input_until("请输入年利率（如 0.05 表示 5%）：",
                lambda x: x >= 0,
                "利率不能为负数，请重新输入。")

# 年限必须大于 0
t = input_until("请输入年限（年）：",
                lambda x: x > 0,
                "年限必须大于 0，请重新输入。")

amount = P * (1 + r) ** t

print("------ 计算结果 ------")
print(f"本金：{P:.2f} 元")
print(f"年利率：{r:.2%}")
print(f"年限：{t:g} 年")
print(f"到期本息：{amount:.2f} 元")
