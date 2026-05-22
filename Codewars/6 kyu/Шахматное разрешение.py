# Шахматное разрешение
# В этой ката мы будем считать черные квадраты на специальной шахматной доске. Она особенная, потому что имеет систему координат, resolutionкоторая определяет расположение черных и белых квадратов.

# Здесь resolutionподразумеваются размеры квадратов одного цвета. Пример с размерами приведен ниже 11x6:

# С resolution = 1:


# Number of black squares = 33

# А теперь с resolution = 2:

# Number of black squares = 32

# И ещё один пример resolution = 5:

# Number of black squares = 31

# Благодарим awesomead за красивые картинки!

# Как вы могли заметить, верхний левый квадрат всегда белый , и мы считаем отдельные черные квадраты на доске.

# Задача
# Вам необходимо написать функцию, которая будет принимать три параметра:

# width-> Ширина доски
# height-> Высота доски
# resolution-> Размер цветных квадратов на шахматной доске (как показано выше)
# И возвращает общее количество всех отдельных черных квадратов.

# Дополнительная информация
# Все введенные данные будут действительными.
# 0 <= width <= 10**32
# 0 <= height <= 10**32
# 1 <= resolution <= 10**32

def count_checkerboard(width, height, resolution):
    # Calculate the number of black squares in the width and height
    black_squares_width = (width + resolution) // (2 * resolution)
    black_squares_height = (height + resolution) // (2 * resolution)

    # Total number of black squares is the product of the two
    total_black_squares = black_squares_width * black_squares_height

    return total_black_squares