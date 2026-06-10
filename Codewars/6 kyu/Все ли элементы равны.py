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
    pass

#  test.assert_equals(eq_all(''), True, "For ''")
#         test.assert_equals(eq_all([]), True, 'For []')
#         test.assert_equals(eq_all(()), True, 'For ()')
#         test.assert_equals(eq_all(set()), True, 'For set()')
#         test.assert_equals(eq_all({}), True, 'For {}')

#  test.assert_equals(eq_all('aaa'), True, "For 'aaa'")
#         test.assert_equals(eq_all([0, 0, 0]), True, 'For [0, 0, 0]')
#         test.assert_equals(eq_all(('A', 'A', 'A')), True, "For ('A', 'A', 'A')")
#         test.assert_equals(eq_all({2}), True, "For {2}")
#         test.assert_equals(eq_all({'a': 32}), True, "For {'a': 32}")

#  test.assert_equals(eq_all('abc'), False, "For 'abc'")
#         test.assert_equals(eq_all([0, 1, 2]), False, 'For [0, 1, 2]')
#         test.assert_equals(eq_all(('A', 'A', 'a')), False, "For ('A', 'A', 'a')")
#         test.assert_equals(eq_all({2, 3}), False, "For {2, 3}")
#         test.assert_equals(eq_all({'a': 32, 'A': 32}), False, "For {'a': 32, 'A': 32}")