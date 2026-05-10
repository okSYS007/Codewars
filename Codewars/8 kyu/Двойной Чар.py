# Получив строку, необходимо вернуть строку, в которой каждый символ (с учетом регистра) повторяется один раз.

# Примеры (Ввод -> Вывод):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
# Удачи!

def double_char(s):
    return ''.join([i*2 for i in s])