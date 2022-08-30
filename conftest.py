import pytest

@python.fixture(scope='sessions', autouse=True)
def browser_config():
    """Настройка разрешения окна браузера"""
    browser.config.window_width = 1920
    browser.config.window_height = 1080
# browser.driver.maximize_window()
    yeild
