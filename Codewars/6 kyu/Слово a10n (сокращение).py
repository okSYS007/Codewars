# Это слово i18nявляется распространённым сокращением internationalizationв 
# сообществе разработчиков, используемым вместо того, чтобы набирать слово целиком 
# и пытаться правильно его написать. Аналогично, a11yявляется сокращением от accessibility.

# Напишите функцию, которая принимает строку и преобразует все «слова» (см. ниже) 
# в этой строке длиной 4 или более символов в аббревиатуру, следуя этим правилам:

# «Слово» — это последовательность букв алфавита. Согласно этому определению,
#  любой другой символ, например пробел или дефис (например, «elephant-ride»),
#  разделит последовательность букв на два слова (например, «elephant» и «ride»).
# Сокращенная версия слова должна содержать первую букву, затем количество удаленных символов, 
# а затем последнюю букву (например, "elephant ride" => "e6t r2e").
# Пример
#  input: "elephant-rides are really fun!"
#           ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
#  words (^):   "elephant" "rides" "are" "really" "fun"
#                 123456     123     1     1234     1
#  ignore short words:               X              X

#  abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
#  all non-word characters (*) remain in place
#                      "-"      " "    " "     " "     "!"
# output: "e6t-r3s are r4y fun!"


def abbreviate(s):
    import re

    def shorten(match):
        word = match.group()
        if len(word) < 4:
            return word
        return f"{word[0]}{len(word) - 2}{word[-1]}"

    return re.sub(r"[A-Za-z]+", shorten, s)

# --- local tests ---
if __name__ == "__main__":
    from scripts.kata_check import run_tests

    run_tests(abbreviate, [
        (('internationalization',), 'i18n'),
        (('accessibility',), 'a11y'),
        (('Accessibility',), 'A11y'),
        (('elephant-ride',), 'e6t-r2e'),
        (('elephant-rides are really fun!',), 'e6t-r3s are r4y fun!'),
        (('You need, need not want, to complete this code-wars mission',), 'You n2d, n2d not w2t, to c6e t2s c2e-w2s m5n'),
        (('a ab abc abcd abcde',), 'a ab abc a2d a3e'),
        (('',), ''),
        (('double  spaces...and punctuation!',), 'd4e  s4s...and p9n!'),
    ])
