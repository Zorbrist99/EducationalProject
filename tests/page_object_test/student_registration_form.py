import os

from selene import browser, by

class StudentRegistrationPage:

    def __init__(self):
        self.first_name = '#firstName'
        self.last_name = '#lastName'
        self.user_email = '#userEmail'
        self.user_gender = "#genterWrapper"
        self.user_phone = "#userNumber"
        self.calendar = "#dateOfBirthInput"
        self.set_month_birth = ".react-datepicker__month-select"
        self.set_year_birth = ".react-datepicker__year-select"
        self.set_day_birth = ".react-datepicker__month"
        self.line_subject = "#subjectsContainer"
        self.set_subject = "#subjectsInput"
        self.hobbies = "#hobbiesWrapper"
        self.upload = '#uploadPicture'
        self.input_address = '#currentAddress'
        self.country = '#react-select-3-input'
        self.city = '#react-select-4-input'
        self.submit_button = '#submit'

    def open_form(self, name_page):
        browser.open(name_page)
        return self

    def set_first_name(self, name):
        browser.element(self.first_name).set(name)
        return self

    def set_last_name(self, last_name):
        browser.element(self.last_name).set(last_name)
        return self

    def set_email(self, user_email):
        browser.element(self.user_email).set(user_email)
        return self

    def choose_gender(self, gender_user):
        browser.element(self.user_gender).element(by.text(gender_user)).click()
        return self

    def set_phone_number(self, user_phone):
        browser.element(self.user_phone).set(user_phone)
        return self

    def set_date_of_birth(self, month, year, day):
        browser.element(self.calendar).click()
        browser.element(self.set_month_birth).element(f'option[value="{month}"]').click()
        browser.element(self.set_year_birth).element(f'option[value="{year}"]').click()
        browser.element(self.set_day_birth).element(by.text(f'{day}')).click()
        return self

    def set_subjects(self, subject):
        browser.element(self.line_subject).click()
        browser.element(self.set_subject).set(subject).press_enter()
        return self

    def choose_hobbies(self, hobby):
        browser.element(self.hobbies).element(by.text(hobby)).click()
        return self

    def upload_file(self, file_name):
        browser.element(self.upload).send_keys(os.path.abspath(file_name))
        return self

    def set_address(self, address):
        browser.element(self.input_address).set(address)
        return self

    def select_country(self, country):
        browser.element(self.country).set(country).press_enter()
        return self

    def select_city(self, city):
        browser.element(self.city).set(city).press_enter()
        return self

    def click_submit(self):
        browser.element(self.submit_button).click()
        return self
