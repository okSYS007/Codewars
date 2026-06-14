# В одном из своих доказательств Георг Кантор использовал следующую последовательность:

# 1/1 1/2 1/3 1/4 1/5 ...
# 2/1 2/2 2/3 2/4 ...
# 3/1 3/2 3/3 ...
# 4/1 4/2 ...
# 5/1 ...
# Существует множество способов упорядочить эти выражения. В этом задании мы будем использовать следующий подход:



# Таким образом, последовательность такова:

# 1/1, 1/2, 2/1, 3/1, 2/2, 1/3, 1/4 ...
# Ваша задача — вернуть nthэлемент этой последовательности.

# Входные данные: nположительное целое число (максимум 268435455)

# Вывод: строка - nthвыражение последовательности - 'a/b'где aи - bцелые числа.

from math import isqrt


def cantor(n : int) -> str:
    diagonal = (isqrt(8 * n + 1) - 1) // 2
    if diagonal * (diagonal + 1) // 2 < n:
        diagonal += 1

    previous_count = diagonal * (diagonal - 1) // 2
    position = n - previous_count

    if diagonal % 2 == 0:
        numerator = position
        denominator = diagonal + 1 - position
    else:
        numerator = diagonal + 1 - position
        denominator = position

    return f"{numerator}/{denominator}"


if __name__ == "__main__":
    from scripts.kata_check import run_tests

    run_tests(cantor, [
        ((1,), "1/1"),
        ((2,), "1/2"),
        ((3,), "2/1"),
        ((4,), "3/1"),
        ((5,), "2/2"),
        ((6,), "1/3"),
        ((7,), "1/4"),
        ((10,), "4/1"),
        ((15,), "1/5"),
        ((268435455,), "22590/581"),
    ])
