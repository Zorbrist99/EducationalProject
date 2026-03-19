class GradeBook:
    def __init__(self):
        self.__evaluations = []

    def add_grade(self, value):
        self.__evaluations.append(value)

    def average(self):
        # Функция которая фиксирует вывод количества знаков после запятой
        return round(sum(self.__evaluations) / len(self.__evaluations), 1)


gradeBook = GradeBook()
gradeBook.add_grade(10)
gradeBook.add_grade(50.3)
gradeBook.add_grade(60.99)
print(gradeBook.average())
