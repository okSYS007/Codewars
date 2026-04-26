# Определите метод, helloкоторый отправляет returns"Hello, Name!" заданному объекту nameили "Hello, World!", если имя не указано (или передано в виде пустой строки).

# Предположим, это nameтак, Stringи система проверяет наличие опечаток у пользователя, чтобы вернуть имя, начинающееся с заглавной буквы (Xxxx).

# Примеры:

# * With `name` = "john"  => return "Hello, John!"
# * With `name` = "aliCE" => return "Hello, Alice!"
# * With `name` not given 
#   or `name` = ""        => return "Hello, World!"

def hello(name = False):
    if not name:
        return "Hello, World!"
    else:
        return f"Hello, {name.capitalize()}!"