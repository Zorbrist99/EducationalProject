import time
import pytest
from selene import browser, have, be


@pytest.fixture(scope="session")
def open_browser():
    # browser.config.hold_driver_at_exit = True
    browser.open('https://www.ecosia.org/')
    browser.element('[data-test-id="cookie-notice-accept"]').click()
    # browser.driver.set_window_size(560, 300)
    yield


# TODO: фикстура фактически не работает. Необходимс подумать, как очищать после выполнения теста. По отдельности тесты работают
# TODO: Добавить удаление через кнопку крестика
# TODO: Посмотреть конфиг, который не будет ждать рендеринга страницы, а достаточно будет только дома
@pytest.fixture(scope="function")
def clear_search_input():
    browser.element('[name="q"]').should(be.visible).clear()
    yield
    # browser.element('[data-test-id="search-form-input"]').clear()


def test_ecosia(open_browser):
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('[id="main"]').should(
        have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
    time.sleep(1)
    browser.element('[name="q"]').clear()


def test_negative_ecosia(open_browser, clear_search_input):
    browser.element('[name="q"]').type('234jkl32jknkflrnk23').press_enter()
    browser.element('[data-test-id="message-tips-message"]').should(
        have.text('Unfortunately we didn’t find any results for “' + '234jkl32jknkflrnk23' + '”'))
