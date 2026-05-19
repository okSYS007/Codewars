# Вам будет дана строка, и ваша задача — проверить, можно ли преобразовать эту строку в палиндром, удалив один символ. 
# Если строка уже является палиндромом, верните значение "OK". Если нет, и мы можем преобразовать 
# её в палиндром, удалив один символ, верните значение "remove one", в противном случае верните значение "not possible". Порядок символов не должен изменяться.

# Например:

# "abba"   -> "OK"           - this is a palindrome
# "abbaa"  -> "remove one"   - remove the 'a' at the extreme right
# "abbaab" -> "not possible" - cannot be made a palindrome 
# Удачи!

# Если вам понравилась эта ката, попробуйте также «Палиндромы из одного символа II».

def solve(s):
    if s == s[::-1]:
        return "OK"
    
    for i in range(len(s)):
        if s[:i] + s[i+1:] == (s[:i] + s[i+1:])[::-1]:
            return "remove one"
    
    return "not possible"