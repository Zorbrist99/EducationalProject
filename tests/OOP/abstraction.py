from abc import ABC, abstractmethod

"""
Создаем абстрактный класс. Делаем наследование от встроенной библиотеки abc. 
Абстрактный класс, тот который содержит хотябы один абстрактный метод.
Абстрактный метод — это метод, который объявлен, но не имеет реализации (только сигнатура).
"""


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass


"""
Создаем классы, которые наследуются от абстрактного класса.
В таком случае эти классы обязаны реализовать абстрактные методы наследуемого класса, иначе будет ошибка.
"""


class Car(Vehicle):

    def drive(self):
        print('Машина поехала')

    def start_engine(self):
        print('Машина заведена')


class Buss(Vehicle):
    def start_engine(self):
        print('Автобус заведен')

    def drive(self):
        print('Автобус поехал')


class Motorcycle:
    def start_engine(self):
        print('Мотоцикл заведен')

    def drive(self):
        print('Мотоцикл поехал')


"""
Создаем класс, которому не важно как реализованы классы транспортного средства.
Он использует абстракцию транспорта.
"""


class Driver:
    """
    Поскольку Vehicle это абстрактный класс, все наследуемые от него классы обязаны реализовать эти методы.
    Но что бы точно застраховаться от того, что класс не унаследован от абстрактного класса, можно сделать проверку:
        if not isinstance(vehicle, Vehicle)
        *Эта функция проверит родство. Наследуется ли объект от класса.
        *Если нет, то явно выпадет ошибка при попытке подсунуть не унаследованный класс
    """

    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def start_trip(self):
        print('Водитель готов к поездке')
        self.vehicle.start_engine()
        self.vehicle.drive()
        print('Поездка завершена')


driver_1 = Driver(Car())
driver_2 = Driver(Buss())
driver_3 = Driver(Motorcycle())

driver_1.start_trip()
print('|....|')
driver_2.start_trip()
print('|....|')
driver_3.start_trip()