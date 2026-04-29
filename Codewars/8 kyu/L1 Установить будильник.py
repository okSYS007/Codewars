# Напишите функцию с именем setAlarm/ set_alarm/ set-alarm/ setalarm(в зависимости от языка программирования), 
# которая принимает два параметра. Первый параметр, employed, равен true, когда вы работаете, а второй параметр, 
# vacationравен true, когда вы в отпуске.

# Функция должна возвращать true, если вы работаете, а не находитесь в отпуске 
# (поскольку именно при таких обстоятельствах необходимо устанавливать будильник).
# В противном случае она должна возвращать false. Примеры:

# employed | vacation 
# true     | true     => false
# true     | false    => true
# false    | true     => false
# false    | false    => false

def set_alarm(employed, vacation):
    return employed and not vacation