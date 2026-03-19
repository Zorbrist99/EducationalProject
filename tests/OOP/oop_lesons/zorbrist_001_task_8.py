from abc import ABC, abstractmethod





class Form(ABC):

    @abstractmethod
    def validate(self):
        pass


class EmailForm(Form):
    def __init__(self):
        self.__email = None

    @property
    def email(self):
        return self.__email

    def validate(self, value: str):
        if ("@" in value) and ('.' in value):
            self.__email = value
        else:
            raise ValueError("Не выполнено обязательное условие")


class PhoneForm(Form):
    def __init__(self):
        self.__phone = 0

    @property
    def phone(self):
        return self.__phone

    def validate(self, value: int):
        if str(value).isdigit() and len(str(value)) > 11:
            self.__phone = value
        else:
            raise ValueError("Не выполнено обязательное условие")


emailForm = EmailForm()
print(emailForm.email)
emailForm.validate('avc@mail.ru')
# emailForm.validate('avc@mailru')
# emailForm.validate('avc.mail.ru')
print(emailForm.email)


phoneNumber = PhoneForm()

print(phoneNumber.phone)
phoneNumber.validate(1234567891011)
print(phoneNumber.phone)
# phoneNumber.validate("1234567891011sadsad")
# phoneNumber.validate("abc")
