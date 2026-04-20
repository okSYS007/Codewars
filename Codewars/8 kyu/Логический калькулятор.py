# Ваше задание
# Имея массив логических значений и логический оператор, верните логический результат, последовательно применяя оператор к значениям в массиве.

# Примеры
# логические значения = [True, True, False], оператор ="AND"
# True AND True ->True
# True AND False->False
# возвращатьсяFalse
# логические значения = [True, True, False], оператор ="OR"
# True OR True ->True
# True OR False->True
# возвращатьсяTrue
# логические значения = [True, True, False], оператор ="XOR"
# True XOR True ->False
# False XOR False->False
# возвращатьсяFalse
# Вход
# массив логических значений(1 <= array_length <= 50)
# Строка, указывающая логический оператор: "AND", "OR","XOR"
# Выход
# Логическое значение ( Trueили False).

def logical_calc(array, op):
    if op == 'AND':
        return all(array)
    elif op == 'OR':
        return any(array)
    elif op == 'XOR':
        result = False
        for value in array:
            result ^= value
        return result