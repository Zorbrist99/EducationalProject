from abc import ABC, abstractmethod


class Robot(ABC):

    @abstractmethod
    def speak(self):
        pass

    @property
    @abstractmethod
    def model(self):
        pass


class CleanerRobot(Robot):
    def __init__(self, model):
        self.model = model

    def speak(self):
        print('Я пылесошу')

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value: str):
        if value.startswith('CR-'):
            self.__model = value
            return
        raise ValueError('Название модели должно начинаться с "CR-"')


cleanerRobot = CleanerRobot('CR-2034')
cleanerRobot.speak()
print(cleanerRobot.model)
