import pytest
from selenium import webdriver
@pytest.fixture()
def setup_and_teardown():
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://demo.opencart.com/admin/")
    yield
    driver.quit()