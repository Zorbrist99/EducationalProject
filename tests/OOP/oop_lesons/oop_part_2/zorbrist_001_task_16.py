# class Teacher:
#     def __init__(self, name: str, list_lesson: list):
#         self.name = name
#         self.list_lesson = list_lesson
#
#     def __repr__(self):
#         return f'{self.name}'
#
#
# class Schedule:
#     def __init__(self):
#         self.dict_day_of_week = {}
#
#     #     defaultdict(dict)
#
#     def add_lesson(self, day: str, subject: str, teacher: Teacher):
#         if subject in teacher.list_lesson:
#             # self.dict_day_of_week[day][subject] = teacher
#             if day not in self.dict_day_of_week:
#                 self.dict_day_of_week[day] = {}
#
#             self.dict_day_of_week[day][subject] = teacher
#         else:
#             raise ValueError('Учитель не может вести этот предмет')
#
#     def get_day_schedule(self, day: str):
#         d = self.dict_day_of_week[day]
#         ls = []
#
#         for key in d.keys():
#             ls.append(f'Предмет: {key}, Преподаватель: {d[key]}')
#         return ls
#
#
# t1 = Teacher("Иванов", ["Математика"])
# t2 = Teacher("Петров", ["Физика", "Химия"])
#
# s = Schedule()
# s.add_lesson("Понедельник", "Математика", t1)
# s.add_lesson("Понедельник", "Физика", t2)
# s.add_lesson("Вторник", "Химия", t2)
#
# print(s.get_day_schedule("Вторник"))

# Вариант 2

"""
Создай класс Teacher, у которого:
имя
список предметов, которые он ведёт
Создай класс Schedule, в котором:
метод add_lesson(day: str, subject: str, teacher: Teacher). Оптимально добавить проверку, что введенный предмет может вести этот учитель.
метод get_day_schedule(day: str) — возвращает список строк вида "Предмет: [subject], Преподаватель: [name]"
Ожидаемое поведение:
t1 = Teacher("Иванов", ["Математика"])
t2 = Teacher("Петров", ["Физика", "Химия"])

s = Schedule()
s.add_lesson("Понедельник", "Математика", t1)
s.add_lesson("Понедельник", "Физика", t2)

print(s.get_day_schedule("Понедельник"))
# ['Предмет: Математика, Преподаватель: Иванов', 'Предмет: Физика, Преподаватель: Петров']
"""


class Teacher:
    def __init__(self, name: str, list_lesson: list):
        self.name = name
        self.list_lesson = list_lesson

    def __repr__(self):
        return f'{self.name}'


class Schedule:
    def __init__(self):
        self.dict_schedule = {
            'Понедельник': [],
            'Вторник': [],
            'Среда': [],
            'Четверг': [],
            'Пятница': [],
            'Суббота': [],
            'Воскресенье': []
        }

    def add_lesson(self, day: str, subject: str, teacher: Teacher):
        if day not in self.dict_schedule.keys():
            raise KeyError(f'Такого дня недели не существует: {day}')

        if subject not in teacher.list_lesson:
            raise ValueError(f'Преподаватель не ведет: {subject}')

        self.dict_schedule[day].append(f'Предмет: {subject}, Преподаватель: {teacher.name}')

    def get_day_schedule(self, day: str):
        return self.dict_schedule[day]


t1 = Teacher("Иванов", ["Математика"])
t2 = Teacher("Петров", ["Физика", "Химия"])

s = Schedule()
s.add_lesson("Понедельник", "Математика", t1)
s.add_lesson("Понедельник", "Физика", t2)
s.add_lesson("Вторник", "Химия", t2)

print(s.get_day_schedule("Вторник"))
