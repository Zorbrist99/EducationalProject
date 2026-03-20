from abc import ABC, abstractmethod


class UIComponent(ABC):

    @abstractmethod
    def render(self):
        print()

    @property
    @abstractmethod
    def visible(self):
        pass


class Button(UIComponent):
    def __init__(self, text):
        self.text = text
        self.visible = True

    def __repr__(self):
        return f'Значение: {self.text}, Видимость: {self.visible}'

    def render(self):
        print(f'Кнопка: {self.text}')

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, value):
        if type(value) is not bool:
            raise ValueError("Значение value должно быть True или False")

        self.__visible = value


class TextField(UIComponent):
    def __init__(self, placeholder):
        self.placeholder = placeholder
        self.visible = True

    def __repr__(self):
        return f'Значение: {self.placeholder}, Видимость: {self.visible}'

    def render(self):
        print(f'Поле ввода: {self.placeholder}')

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, value):
        # Можно проверить принадлежит ли объект классу или его наследником
        if not isinstance(value, bool):
            raise ValueError("Значение value должно быть True или False")

        self.__visible = value


class Checkbox(UIComponent):
    def __init__(self, checked: bool):
        self.checked = checked
        self.visible = True

    def __repr__(self):
        return f'Значение: {self.checked}, Видимость: {self.visible}'

    def render(self):
        print(f'Чекбокс: {self.checked}')

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, value):
        if type(value) is not bool:
            raise ValueError("Значение value должно быть True или False")

        self.__visible = value


class UIContainer:
    def __init__(self):
        #Что бы отображались подсказки методов
        self.components :list[UIComponent] = []

    def add(self, components: UIComponent):
        self.components.append(components)

    def render_all(self):
        for value in self.components:
            if value.visible:
                value.render()


ui = UIContainer()
ui.add(Button("OK"))
ui.add(Checkbox(True))
ui.add(TextField("Введите имя"))
ui.components[2].visible = 'False'

ui.render_all()
