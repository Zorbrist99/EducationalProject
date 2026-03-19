class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def area(self):
        return self.__width * self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError
        else:
            self.__width = value


r = Rectangle(5, 10)
print(r.area) # 50
r.width = -1# ValueError

