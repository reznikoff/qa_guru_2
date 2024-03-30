import pytest
from selene import browser

@pytest.fixture
def browser_conf():
    browser.config.window_height = 1920
    browser.config.window_width = 800
    yield
    browser.quit()
