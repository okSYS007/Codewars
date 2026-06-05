# История
# Алекс — большой поклонник снукера, и ему нравится записывать результаты своих любимых игроков, 
# отмечая шары, попадающие в лузы стола. Он просит вас помочь ему с программой, которая подсчитывает очки, 
# набранные игроком в данном сете, используя его записи. К сожалению, его записи довольно беспорядочны... 
# Иногда Алекс забывает, что уже записал цвет шара, и записывает его несколько раз.

# Задача
# Используя его сокращенную запись в виде строки, рассчитайте количество очков, набранных игроком в сете.

# Он обозначает цвета мячей буквами:

# - R  = red     -->  1 point
# - Y  = yellow  -->  2 points
# - G  = green   -->  3 points
# - Bn = brown   -->  4 points
# - Be = blue    -->  5 points
# - P  = pink    -->  6 points
# - Bk = black   -->  7 points
# - W  = white   -->  no points because it's a foul
# Цвет может сопровождаться числом, например, R12это означает, что в лунку забито 12 красных шаров. Если число не указано, шар забит один раз.

# Примечания:

# Если в строке присутствует белый шарик, верните значение.'Foul'
# Если общий балл превышает 147, вернитесь.'invalid data'
# Для вашего удобства баллы для каждого цвета представлены в виде хеша/словаря с указанием названия.blz

# Примеры
# 'R15P3G1Bk4Y1Bn1Be3'          -->  85
# 'R13Bk14YRGBnBkRBePBk1'       -->  147
# 'G9G11P9Bn2Bn1Be10G7WBn10G3'  -->  'Foul'
# 'Bn14Bn14Bn8P9'               -->  'invalid data'


def frame(balls):
    scores = {
        'R': 1,
        'Y': 2,
        'G': 3,
        'Bn': 4,
        'Be': 5,
        'P': 6,
        'Bk': 7,
        'W': 0,
    }

    total = 0
    i = 0
    n = len(balls)

    while i < n:
        if balls[i] == 'B' and i + 1 < n and balls[i + 1] in {'n', 'e', 'k'}:
            ball = balls[i:i + 2]
            i += 2
        else:
            ball = balls[i]
            i += 1

        count_start = i
        while i < n and balls[i].isdigit():
            i += 1

        count = int(balls[count_start:i]) if count_start < i else 1

        if ball == 'W':
            return 'Foul'

        total += scores.get(ball, 0) * count

    if total > 147:
        return 'invalid data'

    return total


if __name__ == "__main__":
    from scripts.kata_check import run_tests

    run_tests(frame, [
        (('R15P3G1Bk4Y1Bn1Be3',), 85),
        (('R13Bk14YRGBnBkRBePBk1',), 147),
        (('G9G11P9Bn2Bn1Be10G7WBn10G3',), 'Foul'),
        (('Bn14Bn14Bn8P9',), 'invalid data'),
        (('R',), 1),
        (('Be2Bk3',), 5 * 2 + 7 * 3),
        (('W1',), 'Foul'),
        (('Y10G10',), 2 * 10 + 3 * 10),
        (('Bk21',), 'invalid data'),
    ])