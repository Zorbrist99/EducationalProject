# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':g
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

s = ('Hello, '
     'world')
print(s)

# Форматирование
a = 'Hello'
b = 'world'
print('{a}, {b}!'.format(a=a, b=b))

print("-----")

print(f"{a}, {b}!")
print("-----")
print(f'{a}, {b.upper()}!')
print("-----")
print(f'{a=}, {b=}!')
print("-----")

a = [1, 2, 3, 4, 5]
print(a)
print(len(a))
print(a[1])
print("-----------")

a.append(1)
print(a)
print("-----------")
a.insert(1, 10)
print(a)
print("-----------")
a.pop(2)
print(a)
print("-----------")
words = ["python", "java", "c++", "go", "kotlin", "rust"]
print(words[0:3])
print("-----------")
print(words[::-1])
print("-----------")
print(words[:3])
url_template = 'https://users.com/v1/api/{}'

user_url = url_template.format('users')
print(user_url)
password_url = url_template.format('pass')
print(password_url)
print("-----")

# Строку в число и наоборот

s = "123"
d = 123

assert s.isdigit()
assert int(s) == d
assert s == str(d)

a = [1, 2, 3, 4, 5]
print(a)
print(len(a))
print(a[1])
print("-----------")

a.append(1)
print(a)
print("-----------")
a.insert(1, 10)
print(a)
print("-----------")
a.pop(2)
print(a)
print("-----------")
words = ["python", "java", "c++", "go", "kotlin", "rust"]
print(words[0:3])
print("-----------")
print(words[::-1])
print("-----------")
print(words[:3])
print("-----------")

a: list[str] = ['a', 'b', 'c', 'd', 'e']
print(a)


def even_indexes(data):
    result = []
    for i, value in enumerate(data):
        if i % 2 == 0:
            result.append(value)
    return result


finish = even_indexes(a)
print(finish)
print("-----------")

'''
Создай код, который:

Создаёт переменную name

Просит пользователя ввести своё имя

Выводит приветствие
'''
# Вывожу приветсвие
print('Напиши своё имя')
# Указываю команду input, которая получает на вход текст из консоли и кладет его в перменную name
#name = input()
# Вывожу приветсвие, указывая текст из перменной
# print('Привет, ' + name + '!')
print("-----------")
"""
Создай скрипт, где:

Считается квадрат числа

А в комментарии указывается TODO: сделать проверку, что ввод — это число
"""
a=3
#TODO: Сделать проверку, что ввод это число
kv = a**2
print(kv)