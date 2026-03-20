# # 1 вариант
# class Client:
#     def __init__(self, name, balance):
#         self.__name = name
#         self.__balance = balance
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def balance(self):
#         return self.__balance
#
#
# class Bank:
#     def __init__(self):
#         self.client = {}
#
#     def add_client(self, cls: Client):
#         self.client[cls.name] = cls.balance
#
#     def transfer(self, out_name: str, in_name: str, value: int):
#         self.client[out_name] -= value
#         self.client[in_name] += value
#
#     def get_balance(self, name: str):
#         return self.client[name]
#
#
# bank = Bank()
# bank.add_client(Client("Ivan", 1000))
# bank.add_client(Client("Anna", 500))
# bank.transfer("Ivan", "Anna", 300)
# print(bank.get_balance("Anna"))  # 800
#
#
# # 2 вариант
# class Client:
#     def __init__(self, name: str, balance: int):
#         self.name = name
#         self.balance = balance
#
#
# class Bank:
#     def __init__(self):
#         self.client = {}
#
#     def add_client(self, name: str, value: int):
#         self.client[name] = value
#
#     def transfer(self, out_name: str, in_name: str, value: int):
#         self.client[out_name] -= value
#         self.client[in_name] += value
#
#     def get_balance(self, name: str):
#         return self.client[name]
#
#
# bank = Bank()
# bank.add_client("Ivan", 1000)
# bank.add_client("Anna", 500)
# bank.transfer("Ivan", "Anna", 300)
# print(bank.get_balance("Anna"))  # 800


"""
Создай класс Client, у которого имя и баланс. Класс Bank, который хранит клиентов, может переводить деньги от одного к другому.
(подсказка, используйте словарь для хранения пар значений имени и баланса)
Ожидаемое поведение:
bank = Bank()
bank.add_client("Ivan", 1000)
bank.add_client("Anna", 500)
bank.transfer("Ivan", "Anna", 300)
print(bank.get_balance("Anna")) # 800
"""


class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.__class__.__name__}["{self.name}", "{self.balance}"]'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Значение баланса не может быть отрицательным")
        self.__balance = value

    def deposit(self, value: int):
        if value < 0:
            raise ValueError("К балансу нельзя прибавить отрицательное значение")
        self.balance += value

    def withdraw(self, value: int):
        if value > self.balance or value < 0:
            raise ValueError(f"Значение {value}, должно быть больше 0 и не превышать сумму баланса {self.balance}")
        self.balance -= value


class Bank:
    def __init__(self):
        self.clients = {}

    def add_client(self, name: str, balance: int):
        client = Client(name, balance)
        self.clients.setdefault(name, client)

    def transfer(self, out_name: str, in_name: str, value: int):
        out_name: Client = self.clients[out_name]
        in_name: Client = self.clients[in_name]
        out_name.withdraw(value)
        in_name.deposit(value)

    def get_balance(self, name_client: str):
        client: Client = self.clients[name_client]
        return client.balance


bank = Bank()
bank.add_client("Ivan", 1000)
bank.add_client("Anna", 500)
bank.transfer("Ivan", "Anna", 0)
print(bank.get_balance("Anna"))  # 800
