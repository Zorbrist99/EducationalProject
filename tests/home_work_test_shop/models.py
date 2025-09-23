from dataclasses import dataclass


class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

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

    def __hash__(self):
        return hash(self.name + self.description)

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, description='{self.description}')"

    def __str__(self):
        return f"{self.name} - {self.price} руб."


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}
        # По-умолчанию на складе вот такие позиции
        self.products_save = {
            "Яблоки": 100,
            "Бананы": 23
        }
        self.sm = 0

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        try:

            if buy_count <= 0:
                raise ValueError(f"Вы не можете добавить продукт в корзину с таким значением: {buy_count}")
            if product in self.products:
                self.products[product] += buy_count
            else:
                self.products[product] = buy_count

            return f'В корзине продукт: {product.name} количество: {self.products[product]}'

        except ValueError as e:
            return f'Ошибка {e.args[0]}'

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        try:
            ls = [product_key.name for product_key in self.products.keys()]

            if product.name not in ls:
                raise KeyError(f"Продукт который вы хотите удалить {product.name}, нет в корзине")

            if remove_count is None or self.products[product] < remove_count:
                del self.products[product]
                return f'Позиция {product.name} удалена из корзины'
            if remove_count < 0:
                raise ValueError(f'Передано отрицательное значение {remove_count}')
            else:
                self.products[product] -= remove_count
                return f'Из корзины удалено {remove_count} {product.name}'

        except KeyError as e:
            return f"Ошибка: {e.args[0]}"
        except ValueError as e:
            return f"Ошибка: {e.args[0]}"

    def clear(self):
        """
        Мы должны наполненную корзину вернуть пустой.
        Если корзина уже пуста вернуть предупреждение
        """
        if self.products != {}:
            self.products.clear()
            return 'Корзина очищена'
        else:
            return 'Корзина пуста'

    def get_total_price(self) -> float:
        """
        У меня есть несколько объектов продуктов, добавленных в корзину.
        Мне нужно взять цены продуктов добавленных в корзину, сложить, получить сумму и вернуть эту сумму
        Поправка: мне нужно вытащить цены на каждый продукт добавленный в корзину, умножить его на количество этих продуктов в корзине
        Сложить значения и таким образом получить сумму заказа
        """

        if self.products != {}:
            for product, count in self.products.items():
                self.sm += (product.price * count)
            return self.sm
        else:
            return 0.0

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """

        if self.products == {}:
            raise ValueError('У вас пустая корзина!')

        for fructs, counts in self.products.items():
            # Берем количество фрукта в корзине и количество на складе. Если количество в корзине больше чем на складе, мы должны упасть с ошибкой
            if fructs.name not in self.products_save.keys():
                raise KeyError(f'Продукта: {fructs.name} нет на складе. Выберите что-то другое')

            if self.products_save[fructs.name] < counts:
                raise ValueError(
                    f'Количество товаров на складе: {self.products_save[fructs.name]}, количество товаров в корзине: {counts}. '
                    f'Уменьшите количество товаров в корзине!'
                )

        for fructis, counts in self.products.items():
            self.products_save[fructis.name] -= counts

        self.products = {}
        return 'Спасибо за заказ. Приходите снова'
