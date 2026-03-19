class Counter:
    def __init__(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def get_count(self):
        return self.__count

c = Counter()
c.increment()
c.increment()
print(c.get_count()) # выведет 2
