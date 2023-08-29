import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#
# @pytest.fixture
# def driver():
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
#     time.sleep(3)
#     yield driver
#     driver.quit()


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser", default="firefox")
    if browser_name == "chrome":
        options = Options()
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    yield browser
    browser.quit()
