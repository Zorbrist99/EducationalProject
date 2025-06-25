"""
✅ Задание 1: Создание и вывод
Создай словарь с информацией о книге:

название: "1984"

автор: "Джордж Оруэлл"

год: 1949
Выведи весь словарь.
"""
from selene.common.predicate import equals


def primer_1():
    book = {
        'Название': '1984',
        'Автор': 'Джордж Оруэлл',
        'Год': '1949'
    }
    for key in book:
        print(f"{key} : {book[key]}")


"""
✅ Задание 2: Обращение к значению
Дан словарь:

student = {"имя": "Мария", "оценка": 5, "курс": 2}
Выведи значение по ключу "оценка".
"""


def primer_2():
    student = {"имя": "Мария", "оценка": 5, "курс": 2}
    print(student.get('оценка'))


"""
✅ Задание 3: Добавление пары
В словарь:

user = {"логин": "admin", "пароль": "1234"}
Добавь ключ "email" со значением "admin@example.com".
"""


def primer_3():
    user = {"логин": "admin", "пароль": "1234"}
    user['email'] = 'admin@example.com'
    for key in user:
        print(f"{key} : {user[key]}")


"""
✅ Задание 4: Изменение значения
В словаре:

product = {"название": "Хлеб", "цена": 40}
Измени цену на 45.
"""


def primer_4():
    product = {"название": "Хлеб", "цена": 40}
    product["цена"] = 45
    for key in product:
        print(f"{key} : {product[key]}")


"""
✅ Задание 5: Удаление ключа
Из словаря:

car = {"марка": "Toyota", "год": 2020, "цвет": "синий"}
Удалите ключ "цвет".
"""


def primer_5():
    car = {"марка": "Toyota", "год": 2020, "цвет": "синий"}
    del car['цвет']
    for key in car:
        print(f"{key} : {car[key]}")


"""
✅ Задание 6: Перебор ключей и значений
Дан словарь:

person = {"имя": "Анна", "город": "Москва", "возраст": 30}
Выведи каждую пару ключ: значение на новой строке. Используй цикл for.
"""


def primer_6():
    person = {"имя": "Анна", "город": "Москва", "возраст": 30}
    for key, value in person.items():
        print(f"{key} : {value}")


"""
✅ Задание 7: Проверка наличия ключа
Есть словарь:

settings = {"звук": True, "яркость": 80}
Проверь, есть ли в нём ключ "звук", и выведи True или False.
"""


def primer_7():
    settings = {"яркость": True, "звук": 80}
    # name = set()
    # for key in settings:
    #     name.add(key)
    # TODO: Равносильно если написать settings.keys(). По умолчанию поиск происходит по ключу, поскольку он уникален. Можно сделать по значению через settings.values()
    print('звук' in settings)


"""
✅ Задание 8: Получение всех ключей и значений
Дан словарь:

movie = {"название": "Матрица", "режиссёр": "Вачовски", "год": 1999}
Выведи список всех ключей и список всех значений по отдельности.
"""


def primer_8():
    movie = {"название": "Матрица", "режиссёр": "Вачовски", "год": 1999}
    print(movie.keys())
    print(movie.values())


"""
✅ Задание 9: Подсчёт количества ключей
Есть словарь:

inventory = {"яблоко": 10, "банан": 5, "груша": 7}
Выведи количество элементов (пар ключ-значение) в словаре.
"""


def primer_9():
    inventory = {"яблоко": 10, "банан": 5, "груша": 7}
    print(len(inventory.keys()))


"""
✅ Задание 10: Условный вывод
Дан словарь:

marks = {"математика": 5, "физика": 4, "биология": 3}
Выведи только те предметы, где оценка 4 или выше.
"""


def primer_10():
    marks = {"математика": 5, "физика": 4, "биология": 3}
    # for key in marks:
    #     if marks[key] >= 4:
    #         print(f"Оценка по {key} равна {marks[key]}")
    # TODO: Как альтернатива
    for predmet, value in marks.items():
        if value >= 4:
            print(f"По {predmet} оценка: {value}")


"""
✅ Задание 11: Подсчёт повторений слов
Пользователь вводит строку слов.
Составь словарь, где ключ — слово, а значение — сколько раз оно встретилось.
"""


def primer_11():
    spisok = input("Вводи слова: ")
    # Преобразовал в полноценные слова
    v = spisok.split()
    # Сделал кортеж со всеми словами, которые пользователь вписал
    storage1 = tuple(v)
    # Сделал множество уникальных значений для ключей моего словаря
    storage2 = set(storage1)
    # Создали и заполнили словарь ключами
    storage3 = {}
    for value in storage2:
        storage3[value] = None
    # Прогнали множество, узнали сколько раз конкретное слово повторяется в нашем кортеже. Добавили значение по ключу
    for value in storage2:
        a = storage1.count(value)
        storage3[value] = a
    print(storage3)


"""
✅ Задание 12: Инвертирование словаря
Дан словарь:

cities = {"Москва": "Россия", "Париж": "Франция", "Берлин": "Германия"}
Сделай новый словарь, где ключами будут страны, а значениями — города.
"""


def primer_12():
    cities = {"Москва": "Россия", "Париж": "Франция", "Берлин": "Германия"}
    cities_new = dict()
    for city, country in cities.items():
        cities_new[country] = city
    print(cities_new)


"""
✅ Задание 13: Объединение двух словарей
Есть два словаря с количеством фруктов на складе:

store1 = {"яблоко": 5, "банан": 3}
store2 = {"яблоко": 2, "апельсин": 4}
Сложи данные: если фрукт встречается в обоих — суммы, иначе просто добавь.
"""


def primer_13():
    store1 = {"яблоко": 5, "банан": 3}
    store2 = {"яблоко": 2, "апельсин": 4}
    store3 = {}
    store4 = []
    # Двумя циклами переложили все значения ключей в лист
    for fruit in store1:
        store4.append(fruit)
    for fruit in store2:
        store4.append(fruit)
    # Преобразовали лист в сет, для того что бы получить уникальные значения
    unik = set(store4)
    # Через цикл наполнили словарь ключами
    for fruit in unik:
        store3[fruit] = None
    # Берем уникальные значения через цикл. Вытаскиваем у ключа значение в переменную в каждом словаре. Складываю их и присваиваю ключу из результирующего словаря
    for value in unik:
        a = store1.get(value, 0)
        b = store2.get(value, 0)
        c = a + b
        store3[value] = c
    print(store3)


"""
✅ Задание 14: Словарь списков
Составь словарь, где ключ — первая буква слова, а значение — список всех слов, начинающихся с этой буквы.
Ввод: строка слов.
"""


def primer_14():
    a = input("Вводи слова: ")
    b = tuple(a.split())


def primer_15():
    name_1, name_2, name_3 = input(), input(), input()
    maximum = max(len(name_1), len(name_2), len(name_3))
    minimum = min(len(name_1), len(name_2), len(name_3))

    if len(name_1) == minimum:
        print(name_1)
    elif len(name_2) == minimum:
        print(name_2)
    elif len(name_3) == minimum:
        print(name_3)

    if len(name_1) == maximum:
        print(name_1)
    elif len(name_2) == maximum:
        print(name_2)
    elif len(name_3) == maximum:
        print(name_3)
    """
    Аналог 
    names = [input() for _ in range(3)]
    min_name = min(names, key=len)
    max_name = max(names, key=len)
    
    print(min_name)
    print(max_name)
    
    В данном случае поиск наименьшего и наибольшего будет по длине, а не по алфавиту 
    """


primer_15()
