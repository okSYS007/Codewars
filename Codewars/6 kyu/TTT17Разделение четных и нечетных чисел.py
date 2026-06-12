# Задача
# Полная функция splitOddAndEvenпринимает число n(n>0) и возвращает массив, содержащий последовательные части нечетных или четных цифр.

# Не беспокойтесь о цифре 0, она не появится ;-)

# Примеры
# splitOddAndEven(123)  ===  [1,2,3]

# splitOddAndEven(223)  ===  [22,3]

# splitOddAndEven(111)  ===  [111]

# splitOddAndEven(13579)  ===  [13579]

# splitOddAndEven(135246)  ===  [135,246]

# splitOddAndEven(123456)  ===  [1,2,3,4,5,6]

def split_odd_and_even(n):
    digits = str(n)
    parts = []
    start = 0
    current_parity = int(digits[0]) % 2

    for index, digit in enumerate(digits[1:], start=1):
        parity = int(digit) % 2
        if parity != current_parity:
            parts.append(int(digits[start:index]))
            start = index
            current_parity = parity

    parts.append(int(digits[start:]))
    return parts

# --- local tests ---
if __name__ == "__main__":
    from scripts.kata_check import run_tests

    run_tests(split_odd_and_even, [
        ((123,), [1, 2, 3]),
        ((223,), [22, 3]),
        ((111,), [111]),
        ((13579,), [13579]),
        ((2468642,), [2468642]),
        ((135246,), [135, 246]),
        ((123456,), [1, 2, 3, 4, 5, 6]),
        ((8123456,), [8, 1, 2, 3, 4, 5, 6]),
        ((82123456,), [82, 1, 2, 3, 4, 5, 6]),
        ((88123456,), [88, 1, 2, 3, 4, 5, 6]),
    ])
