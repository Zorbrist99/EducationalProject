# 1 вариант
class Client:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance


class Bank:
    def __init__(self):
        self.client = {}

    def add_client(self, cls: Client):
        self.client[cls.name] = cls.balance

    def transfer(self, out_name: str, in_name: str, value: int):
        self.client[out_name] -= value
        self.client[in_name] += value

    def get_balance(self, name: str):
        return self.client[name]


bank = Bank()
bank.add_client(Client("Ivan", 1000))
bank.add_client(Client("Anna", 500))
bank.transfer("Ivan", "Anna", 300)
print(bank.get_balance("Anna"))  # 800


# 2 вариант
class Client:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance


class Bank:
    def __init__(self):
        self.client = {}

    def add_client(self, name: str, value: int):
        self.client[name] = value

    def transfer(self, out_name: str, in_name: str, value: int):
        self.client[out_name] -= value
        self.client[in_name] += value

    def get_balance(self, name: str):
        return self.client[name]


bank = Bank()
bank.add_client("Ivan", 1000)
bank.add_client("Anna", 500)
bank.transfer("Ivan", "Anna", 300)
print(bank.get_balance("Anna"))  # 800
