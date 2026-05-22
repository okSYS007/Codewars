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
