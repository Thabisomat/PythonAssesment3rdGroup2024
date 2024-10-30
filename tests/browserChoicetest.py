import pytest
from selenium import webdriver

@pytest.fixture
def browserSetup(browser):
    if browser.lower=="chrome":
        driver=webdriver.Chrome()
    elif browser.lower() == "safari":
        driver = webdriver.Safari
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge
        return driver

def pytest_adoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


