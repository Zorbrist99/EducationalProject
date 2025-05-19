"""
Напиши программу, которая:

Спрашивает у пользователя два числа

Выводит:

их сумму

их разность

результат деления

результат умножения
"""

one_number = float(input("Введи первое число: "))
two_number = float(input("Введи второе число: "))
sum_number = one_number + two_number
minus_number = one_number - two_number
mnog_number = one_number * two_number
if two_number != 0:
    del_number = one_number / two_number
    print(f'Деление чисел: {del_number}')
else:
    print('Ошибка. Деление на ноль не возможно')
print(f'Сумма чисел: {sum_number}')
print(f'Разность чисел: {minus_number}')
print(f'Умножение чисел: {mnog_number}')