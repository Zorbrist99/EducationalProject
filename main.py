"""
Пример того, как можно в лоб найти минимальное, среднее, максимальное значение и понять может ли эта последовательность
быть арифметической прогрессией
"""
import math
import random
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


def primer_5():
    # Если нужно быстро наполнить массив значениями. Сначала считывается input в range и далее код идет с права на лево
    ls_strok = [int(input()) for _ in range(int(input()))]

    ls_new = []

    for i in ls_strok:
        if i < 0:
            ls_new.append(i)

    for i in ls_strok:
        if i == 0:
            ls_new.append(i)

    for i in ls_strok:
        if i > 0:
            ls_new.append(i)

    for i in ls_new:
        print(i)


# объявление функции
def primer_6():
    gran_diapozon = int(input('Введите правую границу диапозона: '))
    n = random.randint(1, gran_diapozon)
    print('Добро пожаловать в числовую угадайку')
    count = 0

    while True:
        a = input(f'Введите число от 0 до {gran_diapozon}: ')
        if not is_valid(a, gran_diapozon):
            print(f'А может быть все-таки введем целое число от 1 до {gran_diapozon}?')
            continue
        a = int(a)

        if a > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
            continue
        elif a < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
            continue
        else:
            print('Вы угадали, поздравляем!')
            print(f'Количество попыток {count}')
            break

    print('-----')
    print('Хотите еще раз сыграть Y = да / N = нет: ')
    answer = input()
    if answer == 'Y':
        primer_6()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


def primer_7():
    answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
               "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
               "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
               "Определённо да", "Знаки говорят - да", "Сейчас нельзя предсказать", "Перспективы не очень хорошие",
               "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')

    name = input('Как я могу к вам обращаться ?\n')
    print(f'Привет {name}')

    while True:
        input('Какой у тебя вопрос ?\n')

        print(random.choice(answers))

        print('------')
        prodolgenie = input('Ты хочешь задать еще один вопрос ? Y=да / N=нет\n')
        if prodolgenie == 'Y':
            continue
        else:
            print('Возвращайся, если возникнут вопросы!')
            break


def primer_8():
    digits = "0123456789"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuation = "!#$%&*+-=?@^_"
    neodnaznach_sm = 'il1Lo0O'
    chars = ''

    col_answer = int(input('Какое количество паролей вам сгенерировать ?\n'))
    len_answer = int(input('Какая длинна пароля вам нужна ?\n'))
    vkl_cf = bool(input(f'Включать ли цифры {digits} в пароль ? True/False\n'))
    vkl_prop_bk = bool(input(f'Включать ли прописные буквы {uppercase_letters} в пароль ? True/False\n'))
    vkl_stroch_bk = bool(input(f'Включать ли строчные буквы {lowercase_letters} в пароль ? True/False\n'))
    vkl_simvols = bool(input(f'Включать ли символы {punctuation} в пароль ? True/False\n'))
    iskl_neodnaznach_sm = bool(input(f'Исключить ли неодначнаые символы {neodnaznach_sm} из пароля ? True/False\n'))

    if vkl_cf:
        chars += digits
    if vkl_prop_bk:
        chars += uppercase_letters
    if vkl_stroch_bk:
        chars += lowercase_letters
    if vkl_simvols:
        chars += punctuation
    if iskl_neodnaznach_sm:
        for i in neodnaznach_sm:
            chars = chars.replace(i, '')

    for _ in range(col_answer):
        print(*generate_password(len_answer, chars), sep='')


def generate_password(length, chars):
    return random.sample(chars, length)


def primer_9():
    stroka = 'To be, or not to be, that is the question!'
    value = 17
    alfavit = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

    for i in stroka:
        if i in [' ', ',', '!']:
            print(i, end='')
            continue
        if i.isupper():
            znak = alfavit.find(i.lower())
            print(alfavit[znak + value].upper(), end='')
        else:
            znak = alfavit.find(i)
            print(alfavit[znak + value], end='')


def primer_10():
    word_list = ['околесица', 'околица', 'окрошка']

    play(get_word(word_list))


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6
    word_completion = list(word_completion)

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(''.join(word_completion))

    while True:
        # Клиент вводит букву или слово
        people = input("Введи букву или слово целиком: ").upper()

        # Если клиент угадал слово сразу, поздравляем и прерываем игру
        if people == word:
            print('Поздравляем, вы угадали слово! Вы победили!')
            break

        # Если клиент указывает значение, которое уже называл, мы убираем одну жизнь и не выполняем то, что указано дальше
        if people in ''.join(word_completion):
            print('Уже называл')
            tries -= 1
            print(display_hangman(tries))
            continue

        # Если то, что указал клиент является буквами
        if people.isalpha() and len(people) == 1:
            # Если условие True, значит буква есть в слове
            if word.find(people) != -1:
                # Делаем перебор по длине слова
                for i in range(len(word)):
                    # Если введеная буква клиентом совпадает с буквой i в слове
                    if people == word[i]:
                        # Мы меняем по номеру индекса с _ на букву.
                        word_completion[i] = people
                print(''.join(word_completion))
            else:
                tries -= 1
                print(display_hangman(tries))

        # Если клиент укажет не буквы, отнимаем жизнь
        else:
            print("Необходимо вводить только буквы или слово целиком")
            tries -= 1
            print(display_hangman(tries))

        # Если клиент угадал слово по буквам, поздравляем и выходим из цикла
        if ''.join(word_completion) == word:
            print('Поздравляем, вы угадали слово! Вы победили!')
            break

        # Если у клиента закончились жизни, то выводим загаданное слово и выходим из цикла
        if tries == 0:
            print(word)
            break

    print('-----')
    answer = input('Вы хотите сыграть еще раз ? Y=да / N=нет\n')
    if answer == 'Y':
        primer_10()
    else:
        print('Возвращайтесь к нам еще')


def get_word(word_list):
    return str(random.choice(word_list)).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


primer_10()
