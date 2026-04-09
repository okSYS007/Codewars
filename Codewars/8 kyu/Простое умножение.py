# Эта ката посвящена умножению заданного числа на восемь, если оно четное, и на девять в противном случае.

def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9