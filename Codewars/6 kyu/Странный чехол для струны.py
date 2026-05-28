# Напишите функцию, которая принимает строку и возвращает ту же строку, в которой все символы 
# с четными индексами в каждом слове написаны заглавными буквами, а все символы с нечетными индексами — строчными. 
# Индексация, описанная выше, начинается с нуля, поэтому нулевой индекс — четный, следовательно, 
# этот символ должен быть заглавным. Индексация сбрасывается для каждого слова . Другими словами, 
# первая буква каждого слова имеет четный индекс 0, поэтому она всегда должна быть заглавной и т.д.

# Переданная строка будет состоять только из букв и пробелов ( ' '). Пробелы будут присутствовать 
# только в том случае, если слов несколько. Слова будут разделены одним пробелом ( ' ').

# Примеры:
# "String" => "StRiNg"
# "Weird string case" => "WeIrD StRiNg CaSe"

def to_weird_case(words):
    return " ".join(
        "".join(char.upper() if index % 2 == 0 else char.lower()
                for index, char in enumerate(word))
        for word in words.split(" ")
    )

# --- local tests ---
if __name__ == "__main__":
    from scripts.kata_check import run_tests

    run_tests(to_weird_case, [
        (('This',), 'ThIs'),
        (('is',), 'Is'),
        (('String',), 'StRiNg'),
        (('Weird string case',), 'WeIrD StRiNg CaSe'),
        (('This is a test Looks like you passed',), 'ThIs Is A TeSt LoOkS LiKe YoU PaSsEd'),
        (('a',), 'A'),
        (('ab',), 'Ab'),
        (('abc def ghi',), 'AbC DeF GhI'),
        (('already MIXED case',), 'AlReAdY MiXeD CaSe'),
        (('abcdefghijklmnopqrstuvwxyz',), 'AbCdEfGhIjKlMnOpQrStUvWxYz'),
    ])
