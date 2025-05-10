import time

from selene import browser, be, have, by


def test_ecosia():
    browser.open('https://www.ecosia.org/')
    browser.element('[data-test-id="search-form-input"]').type('yashaka/selene').press_enter()
    browser.element('[data-test-id="result-title"]').should(
    have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_DuckDuckgo():
    browser.open('https://duckduckgo.com/')
    browser.element('#searchbox_input').type('yashaka/selene').press_enter()
    time.sleep(0.02)
    browser.element('[data-area="mainline"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python - GitHub'))
