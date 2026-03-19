class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError('Метод не реализован')


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f'Оплата по кредитной карте: {amount} руб.')


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f'Оплата через PayPal: {amount} руб.')


def make_payment(method: PaymentMethod, amount: float):
    method.pay(amount)


credit = CreditCardPayment()
paypal = PayPalPayment()

make_payment(credit, 1000)  # Оплата по кредитной карте: 1000 руб.
make_payment(paypal, 500.50)  # Оплата через PayPal: 500.5 руб.
