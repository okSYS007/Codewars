# Цветной призрак
# Создайте класс Ghost

# Объекты-призраки создаются без каких-либо аргументов.

# При создании объекта-призрака ему присваивается случайный цветовой атрибут: «белый», «жёлтый», «фиолетовый» или «красный».

# ghost = Ghost()
# ghost.color  #=> "white" or "yellow" or "purple" or "red"

class Ghost(object):
    def __init__(self):
        import random
        self.color = random.choice(['white', 'yellow', 'purple', 'red'])