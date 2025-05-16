"""
Создай переменные:

age — целое число

height — дробное

name — строка

is_student — булево значение

Выведи их и их типы.
"""
from selene.core.query import value

age = 10
print(type(age))
print(str(age))
print(f'Значение {age}, имеет тип {type(age)}')
print('-------')

height = 1.5
print(type(height))
print(height)
print(f'Значение {height}, имеет тип {type(height)}')
print('-------')

name = 'Hi'
print(type(name))
print(name)
print(f'Значение {name}, имеет тип {type(name)}')
print('-------')

is_student = True
print(type(is_student))
print(is_student)
print(f'Значение {is_student}, имеет тип {type(is_student)}')
print('-------')

"""
Напиши скрипт, который:

Запрашивает у пользователя имя и возраст

Выводит сообщение вида:
"Привет, Катя! Тебе 23 года."
"""

name = input("Напиши свое имя: ")
value = int(input('Напиши свой возраст: '))
print(f'Привет, {name}! Тебе {value} года.')
print(f'Формат значения {value}, является {type(value)} ')
print('-------')

"""
Создай переменные x = 5 и y = 2.0.
Сложи их, умножь и выведи результат и тип каждого результата.
"""
x = 5
y = 2.0
sum= x + y
multiplication = x * y
print(f'Сумма выражения равна: {sum}, тип выражения: {type(sum)}')
print(f'Результат умножения равен: {multiplication}, тип выражения: {type(multiplication)}')