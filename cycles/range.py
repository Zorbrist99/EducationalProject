"""
Выведи сумму квадратов всех нечётных чисел от 1 до 100.
"""


def primer_1():
    summa = 0
    for i in range(1, 101, 2):
        summa += i ** 2
    print(summa)


"""
Пользователь вводит число n. Нарисуй ступенчатую лестницу из #, где в каждой строке количество символов — это номер строки.
"""


def primer_2():
    a = int(input("Введите число: "))

    for h in range(1, a + 1):
        print('# ' * h)


"""
Выведи таблицу умножения от 1 до 10 в виде квадратной таблицы.
"""


def primer_3():
    # for i in range(1, 11):
    #     for h in range(i, (i * 10) + 1, i):
    #         print(h, end=' ')
    #     print(" ")

    for i in range(1, 11):
        for j in range(1, 11):
            # Такая конструкция выравнивает по ширине, что бы конструкция была красивая
            print(f'{i * j:3}', end=' ')
        print(" ")


"""
Выведи числа от 100 до 0 с шагом -10.
"""


def primer_4():
    for i in range(100, -1, -10):
        print(i)


"""
Пользователь вводит число N. Выведи все простые числа от 2 до N включительно.
"""


def primer_5():
    a = int(input("Введите число: "))

    for i in range(2, a + 1):
        point = 0
        h = 1
        while h <= i:
            if i % h == 0:
                point += 1
            h += 1
        if point == 2:
            print(i)
