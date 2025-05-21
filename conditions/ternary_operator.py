"""
Пользователь вводит возраст.
Выведи:

"Совершеннолетний", если возраст 18 и больше

иначе — "Несовершеннолетний"
Сделай это с тернарным оператором.
"""


def coming_of_age():
    age = int(input('Введи свой возраст: '))

    result = "Совершеннолетний" if age >= 18 else "Несовершеннолетний"
    print(result)


coming_of_age()

"""
Пользователь вводит число.
Выведи:

"Чётное", если число делится на 2

иначе — "Нечётное"
"""


def parity_of_number():
    value = float(input("Введи число: "))

    result = "Чётное" if value % 2 == 0 else "Нечётное"
    print(result)


parity_of_number()

"""
Пользователь вводит два числа.
Выведи меньшее из них, используя тернарный оператор.
"""


def minimum_of_two_numbers():
    one = float(input('Введи первое число: '))
    two = float(input('Введи второе число: '))

    min_value = one if one < two else two
    print(f"Минимальное значение: {min_value}")


minimum_of_two_numbers()

"""
Пользователь вводит строку.
Выведи:

"Строка пуста", если длина строки равна 0

иначе — "Строка не пуста"
"""


def line_empty_or_not():
    string = input('Введи текст: ')

    # len(string) == 0 // Несколько вариантов реализации проверки пустой строки
    result = "Строка пуста" if not string else "Строка не пуста"
    print(result)


line_empty_or_not()

"""
Пользователь вводит пароль.
Если длина пароля меньше 8 символов — выведи "Слабый пароль"
Иначе — "Надёжный пароль"
"""


def password_verification():
    password = input('Введите пароль')

    line = "Слабый пароль" if len(password) < 8 else "Надёжный пароль"
    print(line)


password_verification()

"""
Задачки посложнее
"""

"""
Пользователь вводит число. Выведи:

"Положительное чётное", если число больше 0 и делится на 2

"Положительное нечётное", если больше 0 и не делится на 2

"Ноль", если число равно 0

"Отрицательное", если число меньше 0

📌 Используй вложенные тернарные операторы.
"""


def definition_of_sign_and_parity():
    value = float(input("Введи число: "))

    result = 'Положительное чётное' if value > 0 and value % 2 == 0 \
        else 'Положительное нечётное' if value > 0 and value % 2 != 0 \
        else 'Ноль' if value == 0 \
        else 'Отрицательное'
    print(result)


definition_of_sign_and_parity()

"""
Пользователь вводит логин.
Выведи:

"Привет, админ!", если логин — 'admin'

"Гость", если логин — 'guest'

"Неизвестный пользователь" — во всех остальных случаях
"""


def login_verification():
    login = input('Введите логин: ')

    result = "Привет, админ!" if login == 'admin' \
        else "Гость" if login == 'guest' \
        else "Неизвестный пользователь"
    print(result)


login_verification()

"""
Пользователь вводит строку.
Выведи:

"Пусто" — если строка пустая

"Короткая строка" — если длина < 5

"Длинная строка" — если длина ≥ 5
"""


def checking_string_length():
    string = input('Введи текст: ')

    result = 'Пусто' if not string \
        else "Короткая строка" if len(string) < 5 \
        else "Длинная строка"
    print(result)


checking_string_length()

"""
Пользователь вводит три числа.
Выведи наибольшее из них, используя вложенные тернарные операторы.
"""


def comparing_three_numbers():
    one = float(input('Введи первое число: '))
    two = float(input('Введи второе число: '))
    three = float(input('Введи третье число: '))

    max_value = one if two < one > three \
        else two if one < two > three \
        else three
    print(f'Максимальное значение равно: {max_value}')


comparing_three_numbers()

"""
Пользователь вводит балл (от 0 до 100).
Выведи:

"Отлично" — если 90 и выше

"Хорошо" — если от 70 до 89

"Удовлетворительно" — от 50 до 69

"Плохо" — ниже 50

📌 Сделай это с помощью вложенных тернарных операторов.
"""


def score_by_points():
    ball = float(input("Введите балл: "))

    result = "Отлично" if ball >= 90 \
        else "Хорошо" if 70 <= ball <= 89 \
        else "Удовлетворительно" if 50 <= ball <= 69 \
        else "Плохо"
    print(result)


score_by_points()
