


class Book:
    def __init__(self, title, pages):
        self.__title = title
        self.pages = pages

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value: int):
        if 0 < value <= 10000:
            self.__pages = value
        else:
            raise ValueError(f'Page:{value} должно быть больше 0 и не больше 10k')


book = Book("Война и мир", 9000)
print(book.pages)
book.pages = 0
print(book.pages)
