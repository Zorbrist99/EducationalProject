import time

from selene import have, be, by
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tests.word_with_file.script_os import TMP_DIR

"""
Все команды с webDriver это настройка браузера под себя. 
Это как будто ты говоришь:
"Открой браузер, настрой его вот так, и отдай мне управление."
"""
"""
options = webdriver.ChromeOptions()
Создаёшь объект настроек браузера. Это как список параметров, который ты дашь браузеру при запуске.
"""
options = webdriver.ChromeOptions()

"""
Набор пользовательских настроек, которые мы можем выставить в браузере по-умолчанию
"""
prefs = {
    "download.default_directory": TMP_DIR,
    "download.prompt_for_download": False
}

"""
Метод add_experimental_option(), фактичеки задает "неофициальные"  настройки браузера. 
"""
options.add_experimental_option("prefs", prefs)
options.page_load_strategy = 'eager'
"""
34 и 35 строки. Мы скачиваем браузер и запускаем Chrome с нужными опциями. 
После этого передаем Selen готовый браузер, которым он может управлять 
"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver


def test_downloud_file():
    browser.open('https://github.com/pytest-dev/pytest/blob/main/README.rst')
    browser.element('[data-testid="download-raw-button"]').click()
    time.sleep(10)


def test_search_proba1():
    browser.open("https://www.ecosia.org/")
    browser.element('[data-test-id="search-form-input"]').set('Selenide').press_enter()
    time.sleep(5)
    browser.element('[data-test-id="result-link"]').click()
    browser.element('[id="lang_rus"]').click()
    browser.element('.main-menu-pages').element(by.text('Отзывы')).click()
    browser.element('.wrapper-color-content').should(have.text('Что говорят о Selenide')).should(be.visible)


def test_search_proba2():
    pass