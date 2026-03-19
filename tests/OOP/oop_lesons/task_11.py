class ShoppingCart:
    def __init__(self):
        self.dict_product = {}

    def add_item(self, name: str, price: float):
        self.dict_product[name] = price

    def total(self):
        sm = 0
        for v in self.dict_product.values():
            sm += v
        return sm

cart = ShoppingCart()
cart.add_item("Apple", 3.0)
cart.add_item("Milk", 2.5)
print(cart.total()) # 5.5