# Напишите функцию, которая вычисляет среднее арифметическое чисел в заданном массиве.

# Примечание: Пустые массивы должны возвращать 0.

def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0