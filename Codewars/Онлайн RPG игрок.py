# Представим, что у нас есть популярная онлайн-ролевая игра. 
# Игрок начинает с нулевым показателем в классе E5. 
# A1 — это наивысший уровень, которого может достичь игрок.

# Допустим, игрок хочет подняться до класса E4. 
# Для этого ему необходимо набрать не менее 
# 100 очков, чтобы пройти в квалификационный этап.

# Напишите скрипт, который будет проверять, 
# набрал ли игрок не менее 100 баллов в своем классе. 
# Если да, то он переходит в квалификационный этап.

# В этом случае мы возвращаемся 
# "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.".

# В противном случае вернуть значение False/false(в соответствии с используемым языком).

def player_rank_up(pts):
     if pts >= 100:
         return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."
     else:
         return False

# test.assert_equals(player_rank_up(64), False)
# test.assert_equals(player_rank_up(180), "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.")