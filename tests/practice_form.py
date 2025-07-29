from selene import browser, have, by, be
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def create_driver_with_page_load_strategy():
    options = Options()
    options.page_load_strategy = 'eager'
    return webdriver.Chrome(options=options)


def test_successful_completion_of_form():
    # Добавить конфигурацию браузера не ждать рендеринга
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
    browser.element('#userNumber').set('8934999000')
    # Выбрать дату рождения
    # Нажимаем на строчку с календарем
    """
    Попытки ввести дату, а не выбирать ее в выпадающем окне
    """
    # browser.element('#dateOfBirthInput').click().press(Keys.CONTROL, 'a' ).set_value('10June1999').press_enter()
    # browser.element('#dateOfBirthInput').click().press(Keys.CONTROL, 'a', Keys.BACKSPACE)
    # browser.element('#dateOfBirthInput').set_value('10June1999').press_enter()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('option[value="6"]').click()
    browser.element('.react-datepicker__year-select').element('option[value="1999"]').click()
    browser.element('.react-datepicker__month').element(by.text('10')).click()
    # Ввести предметы
    browser.element('#subjectsContainer').click()
    browser.element('#subjectsInput').set('History').press_enter()
    # Выбрать хобби
    browser.element('#hobbiesWrapper').element(by.text('Reading')).click()
    # Загрузить файл
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/pin.png'))
    # Заполнить поле адресс
    browser.element('#currentAddress').set('Rus')
    # Выбрать страну
    browser.element('#react-select-3-input').set('NCR').press_enter()
    # Выбрать город
    browser.element('#react-select-4-input').set('Noida').press_enter()
    # Нажать кнопку подтверждения
    browser.element('#submit').click()
    # Проверить заполненные поля в поп апе
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-dark').should(have.text('Sergey Ermolaev')).should(be.visible)
    browser.element('.table-dark').should(have.text('Ermolaev@mail.ru')).should(be.visible)
    browser.element('.table-dark').should(have.text('Male')).should(be.visible)
    browser.element('.table-dark').should(have.text('8934999000')).should(be.visible)
    browser.element('.table-dark').should(have.text('10 July,1999')).should(be.visible)
    browser.element('.table-dark').should(have.text('History')).should(be.visible)
    browser.element('.table-dark').should(have.text('Reading')).should(be.visible)
    browser.element('.table-dark').should(have.text('pin.png')).should(be.visible)
    browser.element('.table-dark').should(have.text('Rus')).should(be.visible)
    browser.element('.table-dark').should(have.text('NCR Noida')).should(be.visible)
