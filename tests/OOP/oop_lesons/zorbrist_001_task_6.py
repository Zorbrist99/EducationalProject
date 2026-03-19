class Ticket:
    def __init__(self):
        self.__nomer_ticket = 0

    @property
    def nomer_ticket(self):
        return self.__nomer_ticket

    @nomer_ticket.setter
    def nomer_ticket(self, nomer):
        if nomer < 0:
            raise ValueError('Номер билета не может быть отрицательным')
        if nomer == 0:
            raise ValueError('Не может быть нулевого билета')
        self.__nomer_ticket = nomer


ticket = Ticket()
print(ticket.nomer_ticket)
ticket.nomer_ticket = 245
print(ticket.nomer_ticket)

ticket.nomer_ticket = 0
ticket.nomer_ticket = -245
