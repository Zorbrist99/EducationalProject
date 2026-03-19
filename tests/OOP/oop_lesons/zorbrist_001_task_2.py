class Animal:
    def speak(self):
        print('Животное издаёт звук')


class Dog(Animal):
    def speak(self):
        print('Гав-гав!')


class Cat(Animal):
    def speak(self):
        print('Мяу-мяу!')


animals = [Dog(), Cat()]
for a in animals:
    a.speak()
