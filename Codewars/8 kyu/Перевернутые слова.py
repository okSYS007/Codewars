# Дополните решение так, чтобы оно переворачивало все слова в переданной строке.

# Слова разделены ровно одним пробелом, пробелов в начале и в конце нет.

# Пример (Ввод --> Вывод):

# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

def reverse_words(s):
    return ' '.join(s.split()[::-1])