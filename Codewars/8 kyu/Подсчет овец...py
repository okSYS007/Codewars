# Рассмотрим массив/список овец, в котором некоторые овцы могут отсутствовать на своих местах. 
# Нам нужна функция, которая подсчитывает количество овец, присутствующих в массиве (true означает присутствие).

# Например,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# Правильный ответ будет 17.

# Подсказка: Не забудьте проверить наличие некорректных значений, таких как null/.undefined

def count_sheeps(sheep):
    return sheep.count(True)