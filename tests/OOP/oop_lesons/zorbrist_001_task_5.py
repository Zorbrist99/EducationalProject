from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @property
    @abstractmethod
    def max_speed(self):
        pass


class Car(Transport):
    def __init__(self):
        self.__max_speed = 300

    def start(self):
        print('Машина едет')

    def stop(self):
        print('Машина остановлена')

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        if value > self.__max_speed:
            raise ValueError('Максимальная скорость 300')
        self.__max_speed = value


c = Car()
# c.max_speed = 320  # ValueError
c.max_speed = 250

print(c.max_speed)  # 250
c.start()  # Машина едет