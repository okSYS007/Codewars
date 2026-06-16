# Введение
# Guess Who? — это игра-угадайка для двух игроков, созданная Орой и Тео Костерами, также известными как Theora Design, и впервые выпущенная компанией Milton Bradley в 1979 году. Впервые она появилась в Великобритании благодаря Джеку Барру-старшему в 1982 году (Источник: Википедия ).
# Connect 4
# Задача
# Ваша задача — создать простой класс под названием GuessWho . Компьютер попытается угадать вашего персонажа, а ваша задача — вернуть компьютеру список возможных персонажей, чтобы он смог успешно угадать. Вам понадобится как минимум один метод в классе с именем   guess , куда компьютер будет отправлять свою догадку.
# Персонажи

# Правила
# 1. Компьютер выдаст вам этот символ при инициализации класса.

# 2. Компьютер отправит предполагаемое значение методу guess.

# 3. Компьютерная модель предположит либо имя персонажа , либо одну из следующих характеристик : ["Мужской","Женский","Очки","Карие глаза","Лысый","Седые волосы","Маленький рот","Усы","Каштановые волосы","Большой рот","Маленький нос","Голубые глаза","Шляпа","Длинные волосы","Черные волосы","Серьги","Светлые волосы","Рыжие волосы","Борода","Большой нос"].

# 4. Если компьютер передаст характеристику, которой обладает ваш персонаж, верните всех персонажей, обладающих этой характеристикой.

# 5. Если компьютер передаёт характеристику, которой нет у вашего персонажа, верните всех персонажей, у которых эта характеристика отсутствует.

# 6. Обновите список персонажей.

# 7. Ведите учет количества ходов, совершенных компьютером.

# 8. Все имена и характеристики пишутся с заглавной буквы.
# Характеристики персонажей — предварительно загружены в исходное решение.
# characteristic = [["Jean-Claude",["Male","Glasses","Brown eyes","Bald","White hair","Small mouth","Small nose"]],
#                   ["Pierre",["Male","Mustache","Brown eyes","Brown hair","Big mouth","Small nose"]],
#                   ["Jean",["Male","White hair","Big nose","Big mouth","Blue eyes"]],
#                   ["Amelie",["Female","Hat","Brown hair","Small mouth","Long hair","Brown eyes","Small nose"]],
#                   ["Mirabelle",["Female","Black hair","Earrings","Small mouth","Brown eyes","Big nose"]],
#                   ["Isabelle",["Female","Blonde hair","Glasses","Hat","Small mouth","Small nose","Brown eyes"]],
#                   ["Antonin",["Male","Brown eyes","Black hair","Small nose","Big mouth"]],
#                   ["Bernard",["Male","Brown eyes","Brown hair","Small nose","Hat"]],
#                   ["Owen",["Male","Blue eyes","Blonde hair","Small nose","Small mouth"]],
#                   ["Dylan",["Male","Brown eyes","Blonde hair","Small nose","Small mouth","Bald","Beard"]],
#                   ["Herbert",["Male","Brown eyes","Blonde hair","Big nose","Small mouth","Bald"]],
#                   ["Christine",["Female","Blue eyes","Blonde hair","Small nose","Small mouth","Long hair"]],
#                   ["Luc",["Male","Brown eyes","White hair","Small nose","Small mouth","Glasses"]],
#                   ["Cecilian",["Male","Brown eyes","Ginger hair","Small nose","Small mouth"]],
#                   ["Lionel",["Male","Brown eyes","Brown hair","Big nose","Big mouth","Mustache"]],
#                   ["Benoit",["Male","Brown eyes","Brown hair","Small mouth","Small nose","Mustache","Beard"]],
#                   ["Robert",["Male","Blue eyes","Brown hair","Big nose","Big mouth"]],
#                   ["Charline",["Female","Brown hair","White hair","Small nose","Big mouth"]],
#                   ["Renaud",["Male","Brown eyes","Blonde hair","Small nose","Big mouth","Mustache"]],
#                   ["Michel",["Male","Brown eyes","Blonde hair","Small nose","Big mouth","Beard"]],
#                   ["Pierre-Louis",["Male","Blue eyes","Brown hair","Small nose","Small mouth","Bald","Glasses"]],
#                   ["Etienne",["Male","Brown eyes","Blonde hair","Small nose","Small mouth","Glasses"]],
#                   ["Henri",["Male","Brown eyes","White hair","Small nose","Big mouth","Hat"]],
#                   ["Damien",["Male","Brown eyes","Blonde hair","Small nose","Big mouth","Hat"]]]
# Возвраты
# Возвращает ["Правильно! за n ходов"] . Где n — количество ходов, которые совершил компьютер, если он угадал правильный символ.

# Возвращает массив возможных символов, если компьютер не угадал правильный символ или характеристику.

# Возвращает массив возможных символов, если компьютер не угадал правильную характеристику.
# Пример
# Игровая настройка с персонажемAmelie

# game = GuessWho("Amelie")
# Компьютер угадывает характеристикуFemale

# game.guess("Female")
# AmeliaЕсли персонаж женского пола, то следует вернуть всех персонажей женского пола.

# ["Amelie", "Mirabelle", "Isabelle", "Christine", "Charline"]
# Удачи и приятного времяпровождения!

class GuessWho():

    def __init__(self, character):
        self.characteristic = [["Jean-Claude",["Male","Glasses","Brown eyes","Bald","White hair","Small mouth","Small nose"]],
                               ["Pierre",["Male","Mustache","Brown eyes","Brown hair","Big mouth","Small nose"]],
                               ["Jean",["Male","White hair","Big nose","Big mouth","Blue eyes"]],
                               ["Amelie",["Female","Hat","Brown hair","Small mouth","Long hair","Brown eyes","Small nose"]],
                               ["Mirabelle",["Female","Black hair","Earrings","Small mouth","Brown eyes","Big nose"]],
                               ["Isabelle",["Female","Blonde hair","Glasses","Hat","Small mouth","Small nose","Brown eyes"]],
                               ["Antonin",["Male","Brown eyes","Black hair","Small nose","Big mouth"]],
                               ["Bernard",["Male","Brown eyes","Brown hair","Small nose","Hat"]],
                               ["Owen",["Male","Blue eyes","Blonde hair","Small nose","Small mouth"]],
                               ["Dylan",["Male","Brown eyes","Blonde hair","Small nose","Small mouth","Bald","Beard"]],
                               ["Herbert",["Male","Brown eyes","Blonde hair","Big nose","Small mouth","Bald"]],
                               ["Christine",["Female","Blue eyes","Blonde hair","Small nose","Small mouth","Long hair"]],
                               ["Luc",["Male","Brown eyes","White hair","Small nose","Small mouth","Glasses"]],
                               ["Cecilian",["Male","Brown eyes","Ginger hair","Small nose","Small mouth"]],
                               ["Lionel",["Male","Brown eyes","Brown hair","Big nose","Big mouth","Mustache"]],
                               ["Benoit",["Male","Brown eyes","Brown hair","Small mouth","Small nose","Mustache","Beard"]],
                               ["Robert",["Male","Blue eyes","Brown hair","Big nose","Big mouth"]],
                               ["Charline",["Female","Brown hair","White hair","Small nose","Big mouth"]],
                               ["Renaud",["Male","Brown eyes","Blonde hair","Small nose","Big mouth","Mustache"]],
                               ["Michel",["Male","Brown eyes","Blonde hair","Small nose","Big mouth","Beard"]],
                               ["Pierre-Louis",["Male","Blue eyes","Brown hair","Small nose","Small mouth","Bald","Glasses"]],
                               ["Etienne",["Male","Brown eyes","Blonde hair","Small nose","Small mouth","Glasses"]],
                               ["Henri",["Male","Brown eyes","White hair","Small nose","Big mouth","Hat"]],
                               ["Damien",["Male","Brown eyes","Blonde hair","Small nose","Big mouth","Hat"]]]
        self.character = character
        self.turns = 0
        self.names = {name for name, _ in self.characteristic}
        self.target_features = next(
            features for name, features in self.characteristic if name == character
        )
        
    def guess(self, guess):
        self.turns += 1

        if guess == self.character:
            return [f"Correct! in {self.turns} turns"]

        if guess in self.names:
            self.characteristic = [
                person for person in self.characteristic if person[0] != guess
            ]
        else:
            target_has_feature = guess in self.target_features
            self.characteristic = [
                person
                for person in self.characteristic
                if (guess in person[1]) == target_has_feature
            ]

        return [name for name, _ in self.characteristic]


if __name__ == "__main__":
    from scripts.kata_check import run_tests

    def play(character, *guesses):
        game = GuessWho(character)
        result = None
        for current_guess in guesses:
            result = game.guess(current_guess)
        return result

    run_tests(play, [
        (("Amelie", "Female"), ["Amelie", "Mirabelle", "Isabelle", "Christine", "Charline"]),
        (("Amelie", "Male"), ["Amelie", "Mirabelle", "Isabelle", "Christine", "Charline"]),
        (("Amelie", "Female", "Hat"), ["Amelie", "Isabelle"]),
        (("Amelie", "Female", "Blue eyes"), ["Amelie", "Mirabelle", "Isabelle", "Charline"]),
        (("Amelie", "Female", "Christine"), ["Amelie", "Mirabelle", "Isabelle", "Charline"]),
        (("Pierre", "Pierre"), ["Correct! in 1 turns"]),
        (("Amelie", "Female", "Hat", "Amelie"), ["Correct! in 3 turns"]),
        (("Michel", "Beard", "Big mouth", "Michel"), ["Correct! in 3 turns"]),
    ])
