from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
from pages.HomeStorePage import HomeStorePage
from pages.ProfilePage import ProfilePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    products_content_header_xpath = "//li[@class='breadcrumb-item']//a[contains(text(),'Products')]"


    def vratenie_textu_z_hlavicky_obsahovej_casti_products(self):
        return self.ziskanie_textu_elementu("products_content_header_xpath",
                                            self.products_content_header_xpath)