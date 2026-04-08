# Каждому начинающему хакеру нужен псевдоним! The Phantom Phreak, Acid Burn, Zero Coolи Crash Override— вот несколько ярких примеров из фильма Hackers.

# Ваша задача — создать функцию, которая, получив правильное имя и фамилию, вернет соответствующий псевдоним.

# Примечания:
# Уже предоставлены два объекта, возвращающие имя из одного слова в ответ на первую букву имени, и один объект, 
# возвращающий имя из первой буквы фамилии. Дополнительные сведения см. в примерах ниже.

# Если первый символ любого из имен, переданных функции, не является буквой из списка A - Z, следует вернуть значение."Your name must start with a letter from A - Z."

# Иногда люди могут забывать писать первую букву своего имени с заглавной буквы, поэтому ваша функция должна учитывать эти грамматические ошибки.

# Примеры
# # These two dictionaries are preloaded, you need to use them in your code
# FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', ...}
# SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' ...}

# alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
# alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'
# Удачного хакинга!

from preloaded import FIRST_NAME, SURNAME

def alias_gen(f_name: str, l_name: str) -> str:
    if not f_name or not l_name:
        return "Your name must start with a letter from A - Z."
    first = FIRST_NAME.get(f_name[0].upper(), '')
    last = SURNAME.get(l_name[0].upper(), '')
    if not first or not last:
        return "Your name must start with a letter from A - Z."
    return f"{first} {last}"