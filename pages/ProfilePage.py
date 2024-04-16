from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    edit_your_profile_card_header_xpath = "//div[@class= 'card-header']"

    def vratenie_textu_card_header(self):
        return self.ziskanie_textu_elementu("edit_your_profile_card_header_xpath", self.edit_your_profile_card_header_xpath)