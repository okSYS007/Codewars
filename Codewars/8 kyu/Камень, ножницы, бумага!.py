# Правила игры «Камень, ножницы, бумага» следующие:

# Рок побеждает ножницы.
# Ножницы побеждают бумагу.
# Бумага побеждает камень.
# Два одинаковых хода приведут к ничьей.
# Давайте играть! Вам будут даны допустимые 
# ходы двух игроков в «Камень, ножницы, бумага»,
# и вы должны будете указать, кто победил: 
# "Player 1 won!"игрок 1 и "Player 2 won!"игрок 2. В случае ничьей укажите свой ход Draw!.

# Примеры:
# "scissors",     "paper"     --> "Player 1 won!"
# "scissors",     "rock"      --> "Player 2 won!"
# "paper",        "paper"     --> "Draw!"

def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    if wins[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"