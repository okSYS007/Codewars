# Сможете ли вы найти иголку в стоге сена?

# Напишите функцию findNeedle(), которая принимает объект, arrayполный мусора, но содержащий один"needle"

# После того, как ваша функция обнаружит иглу, она должна вернуть сообщение (в виде строки), содержащее следующий текст:

# "found the needle at position "плюс, что indexигла была найдена, так что:

# Пример (Ввод --> Вывод)

# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
# Примечание: В COBOL это должно вернуть "found the needle at position 6"

def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))