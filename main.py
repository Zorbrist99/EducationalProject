"""
Пример того, как можно в лоб найти минимальное, среднее, максимальное значение и понять может ли эта последовательность
быть арифметической прогрессией
"""
import math
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