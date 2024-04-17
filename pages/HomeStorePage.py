from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
from pages.ProfilePage import ProfilePage


class HomeStorePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def vratenie_url_stranky_your_store(self):
        return self.driver.current_url