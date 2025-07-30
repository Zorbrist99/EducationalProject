"""
Пример того, как можно в лоб найти минимальное, среднее, максимальное значение и понять может ли эта последовательность
быть арифметической прогрессией
"""
import math
from itertools import count
from math import sqrt, pi, radians, sin, cos, tan


def primer_1():
    s_1, s_2, s_3 = input(), input(), input()

    len_1 = len(s_1)
    len_2 = len(s_2)
    len_3 = len(s_3)
    min_value = min(len(s_1), len(s_2), len(s_3))
    max_value = max(len(s_1), len(s_2), len(s_3))
    sr_value = (len_1 + len_2 + len_3) - max_value - min_value

    if (max_value + min_value) / 2 == sr_value:
        print('YES')
    else:
        print('NO')


def primer_2():
    flag = True
    for i in range(10):
        k = int(input())
        if k % 2 != 0:
            flag = False
    """
    not flag эквивалентно flag == False и наоборот if flag == True эквивалентно if flag  
    """
    if not flag:
        print('NO')
    else:
        print('YES')


"""
Задачка на поиск числа в строке и преобразование его в системе Unicod
"""


def primer_3():
    stroka = input()
    i = 0

    while i < len(stroka):
        if stroka[i] == '[':
            slovo = stroka[i + 3:i + 7]
            stroka = stroka.replace(f'[u-{slovo}]', chr(int(slovo)))
            i = 0
            continue
        i += 1
    print(stroka)


"""
Шифр цезаря 
"""


def primer_4():
    value = int(input())
    stroka = input()

    """
    Двойной алфавит нужен, что бы не уходить в отрицательную зону. 
    Мы находим нужную букву во второй части алфавита и идем в левую часть. 
    Можно представить в виде круга
    """
    alfavit = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

    for n in stroka:
        znak = alfavit.rfind(n)
        print(alfavit[znak - value], end='')


primer_4()
