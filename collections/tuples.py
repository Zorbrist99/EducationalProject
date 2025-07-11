"""
✅ Задание 1: Создание и доступ по индексу
Создай кортеж a = (10, 20, 30, 40, 50)
Выведи:

Первый элемент

Последний элемент
"""


def primer_1():
    a = (10, 20, 30, 40, 50)
    print(a[0])
    print(a[-1])


"""
✅ Задание 2: Подсчёт количества элементов
Дан кортеж: a = (1, 2, 3, 2, 4, 2)
Сколько раз встречается число 2?
"""


def primer_2():
    a = (1, 2, 3, 2, 4, 2)
    print(a.count(2))


"""
✅ Задание 3: Поиск индекса
Дан кортеж: a = ('яблоко', 'банан', 'вишня')
Выведи индекс элемента 'банан'.
"""


def primer_3():
    a = ('яблоко', 'банан', 'вишня')
    print(a.index('банан'))


"""
✅ Задание 4: Срез кортежа
Создай кортеж из чисел от 1 до 10.
Выведи:

Первые 5 элементов

Последние 3 элемента

Чётные индексы
"""


def primer_4():
    a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(a[:5])
    print(a[-3:])
    print(a[2::2])


"""
✅ Задание 5: Сумма и максимум
Дан кортеж a = (5, 12, 7, 3, 9)
Выведи сумму и максимальное значение элементов.
"""


def primer_5():
    a = (5, 12, 7, 3, 9)
    # summa = 0
    # for i in a:
    #     summa += i
    print(sum(a))

    # maximum = 0
    # for i in a:
    #     if i > maximum:
    #         maximum = i
    print(max(a))


"""
✅ Задание 6: Сортировка кортежа (через список)
Дан кортеж a = (4, 1, 7, 3, 2)
Отсортируй элементы по возрастанию и выведи новый кортеж.
"""


def primer_6():
    a = (4, 1, 7, 3, 2)
    """
    В этом случае sorted возвращает отсортированный список. То есть он под капотом понимает, что a нужно приорбразовать в list. 
    После  sorted мы возвращаем его обратно в кортеж 
    """
    sorted_tuple = tuple(sorted(a))

    # b = list(a)
    # b.sort()
    # a = b
    print(sorted_tuple)


"""
✅ Задание 7: Объединение кортежей
Есть два кортежа:

a = (1, 2, 3)  
b = (4, 5)  
Создай третий кортеж, объединив a и b.
"""


def primer_7():
    a = (1, 2, 3)
    b = (4, 5)
    c = a + b
    # p = list(a)
    # g = list(b)
    #
    # for i in g:
    #     p.append(i)
    #
    # h = tuple(p)
    print(c)


"""
✅ Задание 8: Проверка наличия элемента
Проверь, содержится ли число 7 в кортеже a = (3, 5, 7, 9)
Ожидаемый вывод: True или False.

"""


def primer_8():
    a = (3, 5, 7, 9)
    print(7 in a)
    # print("True" if 7 in a else "False")

"""
✅ Задание 9: Перебор кортежа с индексами
Выведи каждый элемент кортежа ('яблоко', 'банан', 'вишня') с его индексом.
"""

def primer_9():
    a = ('яблоко', 'банан', 'вишня')
    for i in a:
        print(f"Элемент с индексом {a.index(i)} содержит значение {i}")

"""
✅ Задание 10: Объединить кортежи и посчитать длину
Дано два кортежа:
a = (1, 2, 3)
b = (4, 5, 6, 7)
Объедини их и выведи длину нового кортежа.
"""

def primer_10():
    a = (1, 2, 3)
    b = (4, 5, 6, 7)
    c = a+b
    print(len(c))

"""
✅ Задание 11: Найти минимальное и максимальное значение
Найди минимум и максимум в кортеже a = (12, 7, 21, 3, 9).
"""

def primer_11():
    a = (12, 7, 21, 3, 9)
    print(min(a))
    print(max(a))

"""
✅ Задание 12: Преобразование строки в кортеж
Пользователь вводит слово. Преобразуй его в кортеж, где каждый символ — отдельный элемент.
"""

def primer_12():
    b= tuple(input("Введите слово: "))
    print(b)

"""
✅ Задание 13: Чётные числа в кортеже
Выведи все чётные числа из кортежа a = (1, 4, 5, 6, 9, 12).
"""

def primer_13():
    a = (1, 4, 5, 6, 9, 12)
    for i in a:
        if i%2==0:
            print(i)

"""
✅ Задание 14: Подсчёт уникальных элементов
В кортеже a = (1, 2, 2, 3, 3, 3, 4) — сколько разных чисел?
"""

def primer_14():
    a = (1, 2, 2, 3, 3, 3, 4)
    b = set(a)
    print(len(b))
