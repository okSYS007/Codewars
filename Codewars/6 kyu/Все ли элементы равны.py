# Задача
# Создайте функцию , которая определяет, равны eq_allли все элементы любого итерируемого объектаbool ; итерируемый объект может быть бесконечным. Возвращаемое значение — это .

# Примеры
# eq_all('aaa')   : True
# eq_all('abc')   : False
# eq_all('')      : True

# eq_all([0,0,0]) : True
# eq_all([0,1,2]) : False
# eq_all([])      : True
# Примечания
# Для того чтобы результат функции был равен True, элемент iterableдолжен быть конечным; Falseоднако результат может быть получен из элемента, конечно удаленного от левого конца. Проверок с бесконечными рядами равных элементов не будет.
# Элементы будут примитивными значениями.



def eq_all(iterable):
    iterator = iter(iterable)

    try:
        first = next(iterator)
    except StopIteration:
        return True

    return all(item == first for item in iterator)

# --- local tests ---
if __name__ == "__main__":
    from itertools import chain, repeat

    from scripts.kata_check import run_tests

    run_tests(eq_all, [
        (('',), True),
        (([],), True),
        (('aaa',), True),
        (('abc',), False),
        (([0, 0, 0],), True),
        (([0, 1, 2],), False),
        ((('A', 'A', 'A'),), True),
        ((('A', 'A', 'a'),), False),
        (({'a': 32, 'A': 32},), False),
        ((iter([1, 1, 1]),), True),
        ((chain(repeat(7, 1000), (8,), repeat(7)),), False),
    ])
