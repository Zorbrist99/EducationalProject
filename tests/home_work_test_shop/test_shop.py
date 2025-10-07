"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from .models import Product, Cart

#Если нужно распространить skip на все тесты в файле
#pytestmark = pytest.mark.skip(reason="Пробный пропуск. Тут должна быть задача")

@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    @pytest.mark.product
    @pytest.mark.check
    #Позволяет пропустить тест и в отчет вывести комментарий
    @pytest.mark.skip(reason="Пробный пропуск. Тут должна быть задача")
    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert not product.check_quantity(1005)
        assert product.check_quantity(905)
        assert product.check_quantity(1000)

    @pytest.mark.product
    @pytest.mark.buy
    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(950) is True
        assert product.buy(1000) is True
        assert product.buy(0) == 'Ошибка: Вы не можете оплатить количество товара: 0'
        assert product.buy(-100) == 'Ошибка: Вы не можете оплатить количество товара: -100'

    @pytest.mark.product
    @pytest.mark.buy
    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        cn = 1005

        assert product.buy(cn) == f'Ошибка: У тебя не хватает {cn - product.quantity} продуктов'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_added_product_cart(self, product, cart):
        cn = 3

        assert cart.products == {}
        assert cart.add_product(product, cn) == f"В корзине продукт: {product.name} количество: {cn}"
        assert cart.products == {product: cn}

    def test_two_added_product_cart(self, cart, product):
        cn = 3
        ck = 150

        cart.add_product(product, cn)
        assert cart.add_product(product, ck) == f"В корзине продукт: {product.name} количество: {ck + cn}"
        assert cart.products == {product: (cn + ck)}

    def test_delete_product_without_count(self, product, cart):
        """
        Проверка удаления продукта без количества
        """
        cart.products = {
            product: 3
        }

        assert cart.remove_product(product) == f'Позиция {product.name} удалена из корзины'
        assert cart.products == {}

    def test_delete_product_count_more_in_cart(self, cart, product):
        """
        Проверка полного удаления продукта, если передано количество больше чем в корзине
        """
        cart.products = {
            product: 3
        }

        assert cart.remove_product(product, 5) == f'Позиция {product.name} удалена из корзины'
        assert cart.products == {}

    def test_delete_product_count_less_is_cart(self, cart, product):
        """
        Проверка частичного удаления продукта, если передано количество меньше чем в корзине
        """
        cart.products = {
            product: 3
        }

        cn = 1

        assert cart.remove_product(product, cn) == f"Из корзины удалено {cn} {product.name}"
        assert cart.products[product] == 3 - cn

    def test_delete_product_not_in_cart(self, cart, product):
        """
        Проверка вывода ошибки если продукта нет в корзине
        """
        apple = Product('Яблоко', 100, "Вкусное яблоко", 1000)
        cart.products = {
            product: 3
        }

        assert cart.remove_product(apple, 3) == f'Ошибка: Продукт который вы хотите удалить {apple.name}, нет в корзине'
        assert cart.products[product] == 3

    def test_delete_product_negative_count(self, product, cart):
        """
        Проверка удаления продукта с отрицательным значением
        """
        cart.products = {
            product: 3
        }

        cn = -2

        assert cart.remove_product(product, cn) == f'Ошибка: Передано отрицательное значение {cn}'
        assert cart.products[product] == cart.products[product]

    def test_clear_product_cart(self, product, cart):
        cart.add_product(product, 5)

        assert cart.products != {}

        assert cart.clear() == 'Корзина очищена'
        assert cart.products == {}

        assert cart.clear() == 'Корзина пуста'
        assert cart.products == {}

    def test_get_total_price(self):
        cart_full = Cart()
        apple = Product("Яблоки", 50.0, "Свежие яблоки", 100)
        banana = Product("Бананы", 30.0, "Спелые бананы", 50)

        cart_full.products = {
            apple: 1,
            banana: 5
        }

        assert cart_full.get_total_price() == 200.0

        apple.price = 150
        assert cart_full.get_total_price() == 300

        cart_full.products[apple] = 3
        assert cart_full.get_total_price() == 600

        cart_empty = Cart()
        assert cart_empty.get_total_price() == 0

    def test_buy_product_cart(self, cart):
        """
        Успешная покупка двух товаров
        """

        apple = Product("Яблоки", 50.0, "Свежие яблоки", 100)
        banana = Product("Бананы", 30.0, "Спелые бананы", 50)

        cart.products = {
            apple: 4,
            banana: 5
        }

        assert cart.buy() == 'Спасибо за заказ. Приходите снова'

    def test_buy_product_cart_full(self, cart):
        """
        Проверка покупки товара, которого в корзине больше, чем на складе
        """

        apple = Product("Яблоки", 50.0, "Свежие яблоки", 100)
        banana = Product("Бананы", 30.0, "Спелые бананы", 50)

        cart.products = {
            apple: 4,
            banana: 56
        }

        with pytest.raises(ValueError) as inf:
            cart.buy()

        assert f'Количество товаров на складе: {cart.products_save[banana.name]}, количество товаров в корзине: {cart.products[banana]}. Уменьшите количество товаров в корзине!' in str(
            inf.value)

    def test_buy_product_is_not_products_save(self, cart):
        """
        Проверка покупки товара, которого нет на складе
        """

        apple = Product("Яблоки", 50.0, "Свежие яблоки", 100)
        orange = Product("Апельсины", 30.0, "Сочные апельсины", 50)

        cart.products = {
            apple: 3,
            orange: 3
        }

        with pytest.raises(KeyError) as inf:
            cart.buy()

        assert f"Продукта: {orange.name} нет на складе. Выберите что-то другое" in str(inf.value)

    def test_buy_products_decreasing_in_save(self, cart):
        """
        Проверка изменения товаров на складе
        """

        apple = Product("Яблоки", 50.0, "Свежие яблоки", 100)
        banana = Product("Бананы", 30.0, "Спелые бананы", 50)

        cart.products = {
            apple: 4,
            banana: 5
        }

        cart.buy()
        assert cart.products_save['Яблоки'] == 96
        assert cart.products_save['Бананы'] == 18

    def test_buy_multiple_purchases_in_row(self, cart):
        """
        Проверка нескольких покупок подряд
        """

        apple = Product("Яблоки", 50.0, "Свежие яблоки", 100)
        banana = Product("Бананы", 30.0, "Спелые бананы", 50)

        cart.products = {
            apple: 10,
            banana: 7
        }

        assert cart.buy() == 'Спасибо за заказ. Приходите снова'
        assert cart.products_save['Яблоки'] == 90
        assert cart.products_save['Бананы'] == 16

        cart.products = {
            apple: 22,
            banana: 12
        }

        assert cart.buy() == 'Спасибо за заказ. Приходите снова'
        assert cart.products_save['Яблоки'] == 68
        assert cart.products_save['Бананы'] == 4

    def test_buy_empty_shopping_cart(self, cart):
        """
        Проверка оплаты пустой корзины
        """

        with pytest.raises(ValueError) as inf:
            cart.buy()

        assert "У вас пустая корзина!" in str(inf.value)
