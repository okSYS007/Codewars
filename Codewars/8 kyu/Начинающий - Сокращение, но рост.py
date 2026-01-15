# Дана непустая последовательность целых чисел. 
# Верните результат умножения этих чисел в порядке возрастания. 
# Пример:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    result = 1
    for number in sorted(arr):
        result *= number
    return result