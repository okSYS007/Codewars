# Задача
# Джон — программист. Он очень ценит своё время. Он живёт на nэтаже многоквартирного дома. Каждое утро он как можно быстрее спускается вниз, чтобы начать свою сегодняшнюю важную работу.

# Спуститься вниз он может двумя способами: пешком или на лифте.

# Когда Джон воспользуется лифтом, он пройдет следующие этапы:

# 1. Waiting the elevator from m floor to n floor;
# 1a. Or take the stairs to m floor;
# 2. Waiting the elevator open the door and go in;
# 3. Waiting the elevator close the door;
# 4. Waiting the elevator down to 0 floor;
# 5. Waiting the elevator open the door and go out;
# (the time of go in/go out the elevator will be ignored)
# Учитывая следующие аргументы:

# n: An integer. The floor of John(0-based).
# m: An integer. The floor of the elevator(0-based).
# speeds: An array of integer. It contains four integer [a,b,c,d]
#         a: The seconds required when the elevator rises or falls 1 floor
#         b: The seconds required when the elevator open the door
#         c: The seconds required when the elevator close the door
#         d: The seconds required when John walks to n-1 or n+1 floor
# Пожалуйста, помогите Джону рассчитать кратчайшее время спуска вниз.

# Пример
# В этом случае n = 4, m = 5 and speeds = [1,2,3,10]на выходе должно быть 12.

# Джон спускается вниз на лифте:

# 1 + 2 + 3 + 4 + 2 = 12

# В этом случае n = 0, m = 5 and speeds = [1,2,3,10]на выходе должно быть 0.

# Джон уже находится на 0уровне пола, поэтому результат будет 0.

# В этом случае n = 4, m = 3 and speeds = [2,3,4,5]на выходе должно быть 20.

# Джон спускается вниз пешком:

# 5 x 4 = 20

# В этом случае n = 7, m = 6 and speeds = [3,1,1,4]на выходе должно быть 25.

# Джон спускается на один этаж вниз и оттуда поднимается на лифте.

# 1×4 + 1 + 1 + 6×3 + 1 = 25

# Простая прогулка заняла бы столько же 7×4 = 28времени, сколько поездка на лифте 1×3 + 1 + 1 + 7×3 + 1 = 27.

# Примечание
# Это голландские полы. Они пронумерованы от 0 ( 0обычно их называют "begane grond").

def shorterest_time(n, m, speeds):
    elevator_speed, open_time, close_time, walk_speed = speeds

    if n == 0:
        return 0

    stairs_only = n * walk_speed
    wait_for_elevator = (
        abs(m - n) * elevator_speed
        + open_time
        + close_time
        + n * elevator_speed
        + open_time
    )

    best = min(stairs_only, wait_for_elevator)
    if m < n:
        walk_to_elevator = (
            (n - m) * walk_speed
            + open_time
            + close_time
            + m * elevator_speed
            + open_time
        )
        best = min(best, walk_to_elevator)

    return best

# --- local tests ---
if __name__ == "__main__":
    from scripts.kata_check import run_tests

    run_tests(shorterest_time, [
        ((4, 5, [1, 2, 3, 10]), 12),
        ((0, 5, [1, 2, 3, 10]), 0),
        ((4, 4, [1, 2, 3, 10]), 11),
        ((1, 1, [1, 2, 3, 10]), 8),
        ((1, 1, [2, 3, 4, 10]), 10),
        ((4, 3, [1, 2, 3, 10]), 12),
        ((4, 3, [2, 3, 4, 5]), 20),
        ((7, 6, [3, 1, 1, 4]), 25),
        ((10, 0, [1, 2, 3, 2]), 15),
        ((1000000, 999999, [1, 1, 1, 10]), 1000002),
    ])
