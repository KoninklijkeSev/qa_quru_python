from selene.support.shared import browser
from selene import be, have

def test_google_should_find_selene():
    """Положительный тест на поиск selene в поисковой строке"""
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    browser.c

def test_google_no_should_find_selene():
    """Отрицательный тест на поиск selene в поисковой строке"""
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selenide - User-oriented Web UI browser tests in Python'))