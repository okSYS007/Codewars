# Предоставлена ​​функция, которая принимает два параметра в 
# следующем порядке: array, elementи возвращает индекс 
# найденного элемента, в "Not found"противном случае — индекс.
# Ваша задача — максимально сократить код, чтобы соответствовать 
# требованиям к количеству символов, установленным в задании.

# Можно предположить, что все элементы массива уникальны.

# Ограничение по количеству символов: 60(CoffeeScript), 85(JavaScript, Python), 161(Java).

def find(a,e):
    return a.index(e) if e in a else 'Not found'


array = [2,3,5,7,11]
print("")
print(find(array, 5))# 2
print(find(array, 11)) # 4
print(find(array, 3)) # 1
print(find(array, 2)) # 0
print(find(array, 8)) # 0

# array = [2,3,5,7,11]
#         test.assert_equals(find(array, 5), 2)
#         test.assert_equals(find(array, 11), 4)
#         test.assert_equals(find(array, 3), 1)
#         test.assert_equals(find(array, 2), 0)
#         test.assert_equals(find(array, 7), 3)
#         test.assert_equals(find(array, 1), 'Not found')
#         test.assert_equals(find(array, 8), 'Not found')

#         array = [True, 'Hello World', False, 'Lorem Ipsum', 6, pi];
#         test.assert_equals(find(array, 'Hello World'), 1)
#         test.assert_equals(find(array, 'lorem ipsum'), 'Not found')
#         test.assert_equals(find(array, 'Lorem Ipsum'), 3)
#         test.assert_equals(find(array, False), 2)
#         test.assert_equals(find(array, True), 0)
#         test.assert_equals(find(array, pi), 5)
#         test.assert_equals(find(array, 3.14), 'Not found')
#         test.assert_equals(find(array, 6), 4)