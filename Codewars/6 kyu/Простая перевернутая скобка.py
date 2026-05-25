# Получив строку, верните минимальное количество перестановок скобок, необходимых для того, чтобы скобки были сбалансированы.

# Например:

# solve(")(") = 2 // Reverse ")" to "(" and "(" to ")". These are 2 reversals.
# solve("(((())") = 1 // Reverse one "(" to ")" to make the string balanced.
# solve("(((") = -1 // It is not possible to form balanced parentheses, so return -1.
# Каждый персонаж будет либо тем (, либо другим ).

# Дополнительные примеры приведены в тестовых примерах.

# Удачи.

def solve(st):
    if len(st) % 2:
        return -1

    open_count = close_count = 0
    for char in st:
        if char == "(":
            open_count += 1
        elif open_count:
            open_count -= 1
        else:
            close_count += 1

    return (open_count + 1) // 2 + (close_count + 1) // 2

# --- local tests ---
if __name__ == "__main__":
    from scripts.kata_check import run_tests

    run_tests(solve, [
        (("",), 0),
        (("()",), 0),
        (("(())",), 0),
        ((')()(',), 2),
        (('((()',), 1),
        (('(((',), -1),
        (("))((",), 2),
        (('())(((',), 3),
        (('())()))))()()(',), 4),
        (("(" * 1000 + ")" * 1000,), 0),
        ((")" * 1000 + "(" * 1000,), 1000),
    ])
