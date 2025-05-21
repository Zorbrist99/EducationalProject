# """
# Напиши программу, которая с помощью цикла while выводит числа от 1 до 10 включительно.
# """
#
#
# def print_numbers():
#     i = 1
#     while i <= 10:
#         print(i)
#         i += 1
#
#
# print_numbers()
#
# """
# Пусть пользователь вводит числа по одному.
# Суммируй введённые числа, пока пользователь не введёт 0.
# После этого выведи сумму всех введённых чисел (не считая 0).
# """
#
#
# def sum_of_numbers():
#     summa = 0
#     while True:
#         n = float(input("Введи число: "))
#         if n == 0:
#             break
#         else:
#             summa += n
#     print(summa)
#
#
# sum_of_numbers()
#
# """
# Программа загадывает число от 1 до 20 (заранее прописано в коде).
# Пользователь вводит число с клавиатуры, пока не угадает загаданное.
# После каждого неправильного ответа выводи подсказку "Больше" или "Меньше".
# """
#
#
# def guess_number():
#     a = 2
#     while True:
#         b = float(input('Вводи число: '))
#         if a == b:
#             print("Ты угадал")
#             break
#         if a > b:
#             print("Больше")
#         else:
#             print("Меньше")
#
#
# guess_number()
#
# """
# Пусть пользователь вводит число.
# Выведи все делители этого числа (числа, на которые оно делится без остатка) с помощью цикла while.
# """
#
#
# def output_of_divisors():
#     a = int(input("Введи число: "))
#
#     i = 1
#     while i <= a:
#         if a % i == 0:
#             print(f'На {i} делится без остатка')
#         i += 1
#
#
# output_of_divisors()

"""
Задачи сложнее
"""

# """
# Пользователь вводит число N.
# Выведи сумму всех чётных чисел от 1 до N включительно с помощью while.
# """
#
#
# def sum_of_even_numbers_from_1_to_n():
#     n = int(input("Введи число: "))
#
#     i = 0
#     summa = 0
#     while i <= n:
#         if i % 2 == 0:
#             summa += i
#         i += 1
#     print(summa)
#
#
# sum_of_even_numbers_from_1_to_n()


# """
# Пользователь вводит число N.
# Выведи числа от N до 1 в обратном порядке, по одному на строку.
# """
#
#
# def countdown():
#     n = int(input("Введите число: "))
#
#     while n >= 1:
#         print(n)
#         n -= 1
#
#
# countdown()

# """
# Пусть пользователь вводит число.
# С помощью цикла while проверь, является ли оно простым (то есть делится только на 1 и само себя).
# Выведи "Простое число" или "Не простое число".
# Например 4 делится на 1, 2 , 4 => Не простое
# """
#
# def checking_for_prime_number():
#     a = int(input("Введите число: "))
#     i = 1
#     point = 0
#     while i <=a :
#         if a%i==0:
#            point += 1
#         i +=1
#     if point > 2:
#         print('Не простое число')
#     else:
#         print('Простое число')
#
# checking_for_prime_number()

# """
# Попроси пользователя вводить числа, пока он не введёт чётное.
# После этого выведи:
# "Вы ввели чётное число: {число}"
# """
#
#
# def entering_up_an_even_number():
#     while True:
#         number = int(input("Вводи число: "))
#
#         if number % 2 == 0:
#             print(f'Вы ввели чётное число: {number}')
#             break
#
#
# entering_up_an_even_number()

"""
Пусть пользователь вводит числа.
Когда он вводит "стоп" (строкой), программа завершает работу и выводит наибольшее из всех введённых чисел.
"""


def largest_of_entered_numbers():
    while True:
        value = int(input('Вводите значение'))
        max_value = 0
        if value != 'стоп':
            if max_value < value:
                max_value = value
        else:
            print(max_value)
            break


largest_of_entered_numbers()
