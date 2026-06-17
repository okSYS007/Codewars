# Палиндром — это слово, фраза, число или другая последовательность символов, которая читается одинаково как в прямом, так и в обратном порядке. Примеры числовых палиндромов:2332, 110011, 54322345

# Для заданного числа numнапишите функцию, которая возвращает массив всех числовых палиндромов, содержащихся в каждом числе. Массив должен быть отсортирован в порядке возрастания, и все дубликаты должны быть удалены.

# В этой ката однозначные числа , а также числа, начинающиеся или заканчивающиеся нулями (например 010, и 00), НЕ считаются допустимыми числовыми палиндромами.

# Если numне содержит допустимых палиндромов, вернуть "No palindromes found". В противном случае вернуть , "Not valid"если входные данные не являются целым числом или меньше 0.

# Примеры
# 1221      -->  [22, 1221]
# 34322122  -->  [22, 212, 343, 22122]
# 1001331   -->  [33, 1001, 1331]
# 1294      -->  "No palindromes found"
# "1221"    -->  "Not valid"


def palindrome(num):
    # Validate input
    if not isinstance(num, int) or num < 0:
        return "Not valid"
    
    s = str(num)
    found_palindromes = set()
    
    # Check all substrings of length >= 2
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):  # Start from i+2 to exclude single digits
            substring = s[i:j]
            
            # Skip if starts or ends with 0
            if substring[0] == '0' or substring[-1] == '0':
                continue
            
            # Check if palindrome
            if substring == substring[::-1]:
                found_palindromes.add(int(substring))
    
    if not found_palindromes:
        return "No palindromes found"
    
    return sorted(list(found_palindromes))


if __name__ == "__main__":
    from scripts.kata_check import run_tests

    run_tests(palindrome, [
        ((1221,), [22, 1221]),
        ((34322122,), [22, 212, 343, 22122]),
        ((1001331,), [33, 1001, 1331]),
        ((1294,), "No palindromes found"),
        (("1221",), "Not valid"),
        ((-5,), "Not valid"),
        ((0,), "No palindromes found"),
        ((9,), "No palindromes found"),
        ((121,), [121]),
        ((12321,), [232, 12321]),
        ((11,), [11]),
        ((101,), "No palindromes found"),  # substring "01" starts with 0
        ((131,), [131]),
        ((1111,), [11, 111, 1111]),
    ])

