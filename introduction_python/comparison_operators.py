"""
Напиши программу, которая сравнивает два числа и говорит, какое больше.

Введи возраст и проверь, является ли пользователь совершеннолетним (>= 18).

Проверь, входят ли два числа в диапазон от 0 до 100 (и то, и другое).
"""

def checking_range():
    per_number = float(input("Введи первое число: "))
    vtor_number = float(input("Введи второе число: "))

    if 0 < per_number < 100:
        print(f'{per_number} входит в диапазон')
    else:
        print(f'{per_number} не входит в диапазон')

    if 0< vtor_number < 100:
        print(f'{vtor_number} входит в диапазон')
    else:
        print(f'{vtor_number} не входит в диапазон')

checking_range()

def comparing_numbers():
    per_number = float(input("Введи первое число: "))
    vtor_number = float(input("Введи второе число: "))

    if per_number > vtor_number:
        print(f'{per_number} больше {vtor_number}')
    if per_number < vtor_number:
        print(f'{per_number} меньше {vtor_number}')
    if per_number == vtor_number:
        print(f'{per_number} равны {vtor_number}')

comparing_numbers()

def age_verification():
    age = int(input('Введи свой возраст: '))

    if age >= 18:
        print('Ты совершеннолетний!')
    else:
        print('Запрет')

age_verification()