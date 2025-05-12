import pytest
from selene import browser, have


@pytest.fixture(scope="session")
def open_browser():
    browser.config.hold_driver_at_exit = True
    browser.open('https://www.ecosia.org/')
    browser.element('[data-test-id="cookie-notice-accept"]').click()
    browser.driver.set_window_size(560, 300)
    yield

@pytest.fixture()
def clear_search_input():
    browser.element('[name="q"]').clear()
    yield

def test_ecosia(open_browser):
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('[data-test-id="result-title"]').should(
        have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_negative_ecosia(open_browser,clear_search_input):
    browser.element('[name="q"]').type('234jkl32jknkflrnk23').press_enter()
    browser.element('[data-test-id="message-tips-message"]').should(
        have.text('Unfortunately we didn’t find any results for “' + '234jkl32jknkflrnk23' + '”'))
    pass
