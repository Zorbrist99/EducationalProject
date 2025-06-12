import pytest
from selene import browser, have
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
Варианты: 'normal', 'eager', 'none'
'normal' — дождаться полной загрузки (по умолчанию)

'eager' — дождаться DOMContentLoaded

'none' — вообще не ждать полной загрузки (полный контроль, может быть быстрее, но нужно следить вручную)
"""

input_line = '[name="q"]'
fail_text = '234jkl32jknkflrnk23'


def create_driver_with_page_load_strategy():
    options = Options()
    options.page_load_strategy = 'eager'
    return webdriver.Chrome(options=options)


"""
Можно прописать команду autouse=True и в таком случае можно не передавать фикстуру отдельно в метод. 
Она будет запускаться по-умолчанию
"""
@pytest.fixture(scope="session", autouse=True)
def open_browser():
    # browser.config.hold_driver_at_exit = True
    browser.config.driver = create_driver_with_page_load_strategy()
    browser.open('https://www.ecosia.org/')
    browser.element('[data-test-id="cookie-notice-accept"]').click()
    # browser.driver.set_window_size(560, 300)
    yield


@pytest.fixture(scope="function")
def clear_search_input():
    browser.element(input_line).click()
    browser.element('[data-test-id="button-icon"]').click()
    yield


def test_ecosia(open_browser, clear_search_input):
    browser.element(input_line).type('yashaka/selene').press_enter()
    browser.element('[id="main"]').should(
        have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_negative_ecosia(open_browser, clear_search_input):
    browser.element(input_line).type(fail_text).press_enter()
    browser.element('[data-test-id="message-tips-message"]').should(
        have.text('Unfortunately we didn’t find any results for “' + fail_text + '”'))
