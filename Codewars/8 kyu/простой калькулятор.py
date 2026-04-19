# Вам необходимо создать простой калькулятор, который будет возвращать результат сложения, вычитания, умножения или деления двух чисел.

# Ваша функция будет принимать три аргумента:
# первый и второй аргументы должны быть числами.
# Третий аргумент должен представлять собой знак, указывающий на операцию, которую необходимо выполнить над этими двумя числами.

# Вам следует вернуть результат применения данной операции к этим числам.

# Примечание : В языках с динамической типизацией (JS, PHP, Python) первый и второй аргументы могут быть не числами. В этом случае возвращается значение "unknown value".

# Если указанная операция, которую необходимо выполнить над двумя числами, не входит в число четырех упомянутых выше, вам следует:

# вернуть значение:
# "unknown value"(JS, PHP, Python)
# вызвать исключение:
# std::invalid_argument(C++)
# ArgumentException(C#)
# IllegalArgumentException(Ява)
# Пример:
# arguments: 1, 2, "+"
# should return 3

# arguments: 1, 2, "&"
# refer to the description for what you should return in this case

# # Specifically for dynamically-typed languages:

# arguments: 1, "k", "*"
# should return "unknown value"

def calculator(x, y, op):
    if type(x) not in (int, float) or type(y) not in (int, float):
        return "unknown value"
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    else:
        return "unknown value"