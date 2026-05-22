# Task
#
# Consider a series of functions S_m(n) where:
#
# S_0(n) = 1
#
# S_(m + 1)(n) = sum(S_m(k) for k in range(1, n + 1))
#
# Write a function s which takes two integer arguments m and n
# and returns the value defined by S_m(n).
#
# Inputs:
# 0 <= m <= 100
# 1 <= n <= 10**100

from math import comb


def s(m, n):
    return comb(n + m - 1, m)


# --- local tests ---
if __name__ == "__main__":
    from scripts.kata_check import run_tests

    run_tests(s, [
        ((0, 53), 1),
        ((1, 49), 49),
        ((1, 101), 101),
        ((2, 5), 15),
        ((2, 99), 4950),
        ((3, 7), 84),
        ((3, 32), 5984),
        ((4, 8), 330),
        ((5, 17), 20349),
        ((10, 4), 286),
    ])
