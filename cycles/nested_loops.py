"""
Выведи таблицу умножения от 1 до 5. Результат должен быть в виде квадратной таблицы.
"""


def primer_1():
    for i in range(1, 6):
        for h in range(1, 6):
            print(f"{i * h:3}", end=" ")
        print()


"""
Построй прямоугольник из символов *, ширина и высота вводятся пользователем.
"""


def primer_2():
    a = int(input("Введите ширину: "))
    b = int(input("Введите высоту: "))

    for i in range(1, b + 1):
        for h in range(1, a + 1):
            print('*', end=" ")
        print()


primer_2()

"""
Построй треугольник из #, где в первой строке 1 символ, во второй — 2 и т.д., до числа N (вводится).

"""


def primer_3():
    a = int(input("Введите число: "))
    for i in range(1, a + 1):
        for h in range(1, i + 1):
            print('#', end=" ")
        print()


"""
Найди все пары чисел от 1 до 5, сумма которых чётная.
"""


def primer_4():
    for i in range(1, 6):
        for h in range(i + 1, 6):
            if (i + h) % 2 == 0:
                print(f'Сумма {i} и {h},четная')


"""
Найди все пары чисел от 1 до 10, где первое число меньше второго.
"""


def primer_5():
    for i in range(1, 11):
        for h in range(i + 1, 11):
            print(f'В паре чисел {i} меньше {h}')
