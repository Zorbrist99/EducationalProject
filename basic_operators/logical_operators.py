"""
Пользователь вводит возраст.
Если возраст:
больше или равен 18 и меньше 65 — выведи: "Трудоспособный возраст", иначе — "Не трудоспособный возраст".
"""

def determination_working_capacity():
    age = int(input('Введи свой возраст: '))

    if 18 <= age < 65:
        print("Трудоспособный возраст")
    else:
        print("Не трудоспособный возраст")

determination_working_capacity()

"""
Пользователь вводит два числа.
Если хотя бы одно из них отрицательное — выведи: "Есть отрицательное число".
"""

def number_sign():
    one_number = float(input("Введи первое число: "))
    two_number = float(input("Введи второе число: "))

    if one_number < 0 or two_number < 0:
        print("Есть отрицательное число")
    else:
        print("Оба положительные")

number_sign()

"""
Пользователь вводит логин.
Если логин не равен "admin" — напечатай: "Доступ запрещён".
"""

def login_verification():
    login = input('Введи логин: ')

    if login != 'admin':
        print('Доступ запрещён')
    else:
        print('Доступ открыт')

login_verification()

"""
Пользователь вводит логин и пароль.
Если логин — "admin" и пароль — "1234" — выведи: "Вход выполнен", иначе — "Неверные данные".
"""

def authorization_verification():
    login= input('Введи логин: ')
    password = input('Введи пароль: ')

    if login == 'admin' and password == '1234':
        print('Вход выполнен')
    else:
        print('Неверные данные')

authorization_verification()

"""
Пользователь вводит температуру.
Если температура меньше 0 или больше 35, выведи: "Экстремальные погодные условия".
"""

def temperature_level():
    temp = float(input('Введи температуру: '))

    if temp < 0 or temp > 35:
        print('Экстремальные погодные условия')

temperature_level()