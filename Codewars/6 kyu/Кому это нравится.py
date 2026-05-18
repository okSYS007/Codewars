# Вы, вероятно, знакомы с системой «лайков» в Facebook и других социальных сетях. Люди могут «лайкать» 
#записи в блогах, фотографии или другие материалы. Мы хотим создать текст, который должен отображаться рядом с такими элементами.

# Реализуйте функцию, которая принимает массив, содержащий имена людей, которым понравился товар. Она должна возвращать текст, отображаемый на экране, 
# как показано в примерах:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Примечание: При наличии 4 и более имен число "and 2 others"просто увеличивается.



def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"