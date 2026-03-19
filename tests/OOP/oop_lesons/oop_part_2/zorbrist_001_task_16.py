from collections import defaultdict


class Teacher:
    def __init__(self, name: str, list_lesson: list):
        self.name = name
        self.list_lesson = list_lesson

    def __repr__(self):
        return f'{self.name}'


class Schedule:
    def __init__(self):
        self.dict_day_of_week = {}
    #     defaultdict(dict)

    def add_lesson(self, day: str, subject: str, teacher: Teacher):
        if subject in teacher.list_lesson:
            # self.dict_day_of_week[day][subject] = teacher
            if day not in self.dict_day_of_week:
                self.dict_day_of_week[day]={}

            self.dict_day_of_week[day][subject] = teacher
        else:
            raise ValueError('Учитель не может вести этот предмет')

    def get_day_schedule(self, day: str):
        d = self.dict_day_of_week[day]
        ls = []

        for key in d.keys():
            ls.append(f'Предмет: {key}, Преподаватель: {d[key]}')
        return ls


t1 = Teacher("Иванов", ["Математика"])
t2 = Teacher("Петров", ["Физика", "Химия"])

s = Schedule()
s.add_lesson("Понедельник", "Математика", t1)
s.add_lesson("Понедельник", "Физика", t2)
s.add_lesson("Вторник", "Химия", t2)

print(s.get_day_schedule("Вторник"))
