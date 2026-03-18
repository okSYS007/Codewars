# Напишите функцию, которая удаляет пробелы из строки, а затем возвращает результирующую строку.

# Примеры ( Вход -> Выход ):

# "8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
# "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
# "8aaaaa dddd r     " -> "8aaaaaddddr"

def no_space(x):
    return x.replace(" ", "")