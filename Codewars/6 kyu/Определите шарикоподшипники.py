# Сбой на заводе!! Одна коробка с «элитными» шарикоподшипниками оказалась перемешана со всеми коробками 
# с «обычными» шарикоподшипниками! Нам нужна ваша помощь, чтобы определить, какая коробка правильная!

# Информация
# Что вам известно о подшипниках:

# «Роскошные» шарикоподшипники весят ровно столько-то.11 grams
# Обычные шарикоподшипники весят ровно столько-то.10 grams
# Помимо веса, оба типа шарикоподшипников идентичны.
# В каждой коробке (фактически) находится бесконечное количество подшипников.
# В каждой коробке находится исключительно один тип подшипников (обычный или "люксовый").
# Чтобы помочь вам определить нужную коробку, в вашем распоряжении также есть весы Super Scale™ ,
# которые точно покажут вес всего, что вы на них положите. К сожалению, подготовка к каждому измерению занимает много времени, поэтому у вас будет время использовать их только один раз!

# Задача
# Напишите функцию, которая принимает два аргумента:

# bearingsСписок типов подшипников, содержащихся в каждой «коробке». (длина от 1до 200включительно)
# weigh: функция, которая принимает любое количество аргументов и возвращает общий вес всех аргументов. Может быть использована только один раз!
# Ваша функция должна идентифицировать и вернуть единственный образец подшипника класса «люкс» из bearings.

# Пример
# def identify_bb(bearings, weigh):
#     a, b, c = bearings
#     if weigh(a, b) == 20:
#         # bearings 'a' and 'b' must both be 10, so 'c' must be deluxe
#         return c 
#     if weigh(a) == 10: # Error: weigh has already been used!
#         return b
#     return a
# Примечание: модули sysотключены inspect.

def identify_bb(bearings, weigh):
    samples = []
    normal_weight = 0

    for count, bearing in enumerate(bearings, 1):
        samples.extend([bearing] * count)
        normal_weight += count * 10

    deluxe_count = weigh(*samples) - normal_weight
    return bearings[deluxe_count - 1]


if __name__ == "__main__":
    from scripts.kata_check import run_tests

    def make_weigh(deluxe):
        used = False

        def weigh(*items):
            nonlocal used
            if used:
                raise AssertionError("weigh can only be used once")
            used = True
            return sum(11 if item == deluxe else 10 for item in items)

        return weigh

    def check_case(data):
        bearings, deluxe = data
        return identify_bb(bearings, make_weigh(deluxe))

    large = list(range(1, 201))

    run_tests(check_case, [
        (((["a"], "a"),), "a"),
        (((["a", "b"], "a"),), "a"),
        (((["a", "b"], "b"),), "b"),
        (((["a", "b", "c"], "c"),), "c"),
        ((((10, 20, 30, 40, 50), 30),), 30),
        (((list("abcdefghi"), "e"),), "e"),
        (((large, 1),), 1),
        (((large, 137),), 137),
        (((large, 200),), 200),
    ])


