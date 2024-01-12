import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 10.0
    browser.config.window_width = 1920
    browser.config.window_height = 1020

    yield
    browser.quit()