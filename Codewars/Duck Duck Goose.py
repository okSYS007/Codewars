
# Цель игры «Утка, утка, гусь» — ходить по кругу , постукивая по голове каждого игрока, пока не будет выбран один из них.

# Имея массив объектов Player и позицию (первая позиция равна 1), верните идентификатор nameвыбранного игрока.
# name— это свойство Playerобъектов, например,Player.name
# duck_duck_goose([a, b, c, d], 1) should return a.name
# duck_duck_goose([a, b, c, d], 5) should return a.name
# duck_duck_goose([a, b, c, d], 4) should return d.name

def duck_duck_goose(players, goose):
    pass

class Player:
    name: str

players = [Player(name) for name in "abcdcefghz"]

print(duck_duck_goose(players, 1)) # "a"
print(duck_duck_goose(players, 3)) # "c"
print(duck_duck_goose(players, 10)) # "z"  
print(duck_duck_goose(players, 20)) # "z"   
# test.assert_equals(duck_duck_goose(players, 1),  "a")
# test.assert_equals(duck_duck_goose(players, 3),  "c")
# test.assert_equals(duck_duck_goose(players, 10), "z")
# test.assert_equals(duck_duck_goose(players, 20), "z")
# test.assert_equals(duck_duck_goose(players, 30), "z")
# test.assert_equals(duck_duck_goose(players, 18), "g")
# test.assert_equals(duck_duck_goose(players, 28), "g")
# test.assert_equals(duck_duck_goose(players, 12), "b")
# test.assert_equals(duck_duck_goose(players, 2),  "b")
# test.assert_equals(duck_duck_goose(players, 7),  "f")