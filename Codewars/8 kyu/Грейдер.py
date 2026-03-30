# Создайте функцию, которая принимает число в качестве аргумента и возвращает оценку, основанную на этом числе.

# Счет	Оценка
# Любое значение больше 1 или меньше 0,6	"Ф"
# 0,9 или более	"А"
# 0,8 или более	"Б"
# 0,7 или более	"С"
# 0,6 или более	"Д"
# Примеры:

# grader(0)   should be "F"
# grader(1.1) should be "F"
# grader(0.9) should be "A"
# grader(0.8) should be "B"
# grader(0.7) should be "C"
# grader(0.6) should be "D"

def grader(score):
    return  "F" if score > 1 or score < 0.6 else "A" if score >= 0.9 else "B" if score >= 0.8 else "C" if score >= 0.7 else "D"