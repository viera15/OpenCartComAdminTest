import pytest
from selenium import webdriver
@pytest.fixture()
def setup_and_teardown(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://demo.opencart.com/admin/")
    request.cls.driver = driver
    yield
    driver.quit()