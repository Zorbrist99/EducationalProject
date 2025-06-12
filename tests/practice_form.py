from selene import browser, have, by
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver_with_page_load_strategy():
    options = Options()
    options.page_load_strategy = 'eager'
    return webdriver.Chrome(options=options)

def test_successful_completion_of_form():
    #Добавить конфигурацию браузера не ждать рендеринга
    browser.config.driver = create_driver_with_page_load_strategy()
    # Открыть страницу
    browser.open('https://demoqa.com/automation-practice-form')

    # Заполнить поле Имя
    browser.element('#firstName').set('Sergey')
    # Заполнить поле Фамилия
    browser.element('#lastName').set('Ermolaev')
    # Заполнить поле Имейл
    browser.element('#userEmail').set('Ermolaev@mail.ru')
    # Выбрать гендер
    """
    Команда by.text('Male') ищет элемент с тектом Male. То есть мы более точно нажимаем на локатор
    """
    browser.element('#genterWrapper').element(by.text('Male')).click()
    # Заполнить поле Телефона
    browser.element('#userNumber').set('89349990000')
    # Выбрать дату рождения
    #Нажимаем на строчку с календарем
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('option[value="6"]').click()
    browser.element('.react-datepicker__year-select').element('option[value="1999"]').click()
    browser.element('.react-datepicker__month').element(by.text('10')).click()
    # Ввести предметы
    browser.element('#subjectsContainer').click()
    browser.element('#subjectsInput').set('History').press_enter()
    # Выбрать хобби

    # Загрузить файл
    # Заполнить поле адресс
    # Выбрать страну
    # Выбрать город
    # Нажать кнопку подтверждения
    # Проверить заполненные поля в поп апе
    pass
