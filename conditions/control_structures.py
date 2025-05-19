"""
Попроси пользователя ввести возраст.
Если ему меньше 18 — выведи: Доступ запрещён,
иначе — Добро пожаловать!
"""

def post_verification():
    age = int(input('Введи свой возраст: '))

    if age < 18:
        print('Доступ запрещён')
    else:
        print('Добро пожаловать!')

post_verification()

"""
Пользователь вводит число.
Выведи: Число чётное или Число нечётное.
"""


def definition_parity():
    value = float(input('Введи число: '))

    if value % 2 == 0:
        print('Число четное')
    else:
        print('Число не четное')


definition_parity()

"""
Пользователь вводит 3 числа.
Выведи самое большое из них.
"""

def comparing_three_numbers():
    one = float(input('Введи первое число'))
    two = float(input('Введи второе число'))
    three = float(input('Введи третье число'))

    #Вариант гораздо быстрее
    max_number = max(one, two,three)
    if one<= two >= three:
        print(f'Самое большое число {two}')
    elif two <= one >= three:
        print(f'Самое большое число {one}')
    elif two <= three >= one:
        print(f'Самое большое число {three}')
    else:
        print(f'Есть одинаковые числа')

comparing_three_numbers()

"""
Пользователь вводит балл (от 0 до 100).
Программа должна напечатать оценку:

90 и выше → Отлично

70–89 → Хорошо

50–69 → Удовлетворительно

Ниже 50 → Неудовлетворительно
"""
def assessment_academic_performance():
    ball = float(input('Введите балл: '))

    if ball >= 90:
        print("Отлично")
    elif 70<=ball<=89:
        print("Хорошо")
    elif 50<= ball <=69:
        print("Удовлетворительно")
    elif ball<50:
        print("Неудовлетворительно")

assessment_academic_performance()

"""
Пользователь вводит логин и пароль.
Если логин admin и пароль 1234, выведи Доступ разрешён.
В остальных случаях — Неверные данные.
"""

def login_password_verification():
    login = input('Введите логин: ')
    password = input('Введите пароль')

    if login == 'admin' and password == '1234':
        print('Доступ разрешён')
    else:
        print('Неверные данные')

login_password_verification()