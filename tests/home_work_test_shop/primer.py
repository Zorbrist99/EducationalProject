from dataclasses import dataclass

"""
Пример использования dataclass декоратора, с помощью которого можно не переопределять методы
"""


@dataclass()
class Primer:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    # def __init__(self, name, price, description, quantity):
    #     self.name = name
    #     self.price = price
    #     self.description = description
    #     self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        try:
            if quantity <= 0:
                raise ValueError(f"Вы не можете оплатить количество товара: {quantity}")

            if not self.check_quantity(quantity):
                raise ValueError(f"У тебя не хватает {quantity - self.quantity} продуктов")

            return True

        except ValueError as e:
            return f'Ошибка: {e}'

    # def __hash__(self):
    #     return hash(self.name + self.description)
    #
    # def __repr__(self):
    #     return f"Product(name='{self.name}', price={self.price}, description='{self.description}')"
    #
    # def __str__(self):
    #     return f"{self.name} - {self.price} руб."
