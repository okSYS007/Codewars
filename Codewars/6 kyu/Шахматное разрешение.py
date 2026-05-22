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
    if width == 0 or height == 0:
        return 0

    bx, rem_x = divmod(width, resolution)
    by, rem_y = divmod(height, resolution)

    # Count full resolution-blocks and multiply by resolution^2
    black_full_blocks = (bx * by) // 2
    black_cells = black_full_blocks * resolution * resolution

    # Partial vertical strip at the right edge
    if rem_x:
        if bx % 2 == 0:
            black_rows = by // 2
        else:
            black_rows = (by + 1) // 2
        black_cells += rem_x * resolution * black_rows

    # Partial horizontal strip at the bottom edge
    if rem_y:
        if by % 2 == 0:
            black_cols = bx // 2
        else:
            black_cols = (bx + 1) // 2
        black_cells += resolution * rem_y * black_cols

    # Bottom-right corner partial block
    if rem_x and rem_y and ((bx + by) % 2 == 1):
        black_cells += rem_x * rem_y

    return black_cells