# Аналогично предыдущему заданию , вам потребуется вернуть логическое значение, если базовая строка может быть выражена как повторение одного подшаблона.

# На этот раз есть два небольших изменения:

# Если подшаблон был использован, он будет присутствовать как минимум дважды, то есть подшаблон должен быть короче исходной строки;
# Предоставленные вам строки могут быть созданы с повторением заданного подшаблона, а могут и не быть, а затем результат может быть перемешан.
# Например:

# "a"    --> false //no repeated shorter sub-pattern, just one character
# "aaaa" --> true  //just one character repeated
# "abcd" --> false //no repetitions
# "babababababababa" --> true //repeated "ba"
# "bbabbaaabbaaaabb" --> true //same as above, just shuffled
# Строки никогда не бывают пустыми и могут состоять из любых символов 
# (просто рассматривайте заглавные и строчные буквы как разные сущности), а также могут быть довольно длинными (следите за производительностью!).

# Если вам понравилось, переходите либо к предыдущей , либо к следующей ката из этой серии!

def has_subpattern(st):
    from collections import Counter
    from math import gcd
    from functools import reduce

    return reduce(gcd, Counter(st).values()) > 1

# --- local tests ---
if __name__ == "__main__":
    from scripts.kata_check import run_tests

    run_tests(has_subpattern, [
        (('a',), False),
        (('AA',), True),
        (('444',), True),
        (('aaaa',), True),
        (('abcd',), False),
        (('babababababababa',), True),
        (('bbabbaaabbaaaabb',), True),
        (('ababababa',), False),
        (('aaaabb',), True),
        (('abbb',), False),
        (('123a123a123a',), True),
        (('123A123a123a',), False),
        (('12aa13a21233',), True),
        (('12aa13a21233A',), False),
        (('aabbbbbbaa',), True),
        (('abcdabcaccd',), False),
        (('aaabbbccccdddddd',), False),
        (('aaabbbccccdddddddd',), False),
    ])
