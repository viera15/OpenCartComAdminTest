from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage


class AdminPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    admin_name_id = "input-username"
    admin_email_id = "input-password"
    button_login_xpath = "//button[contains(text(), 'Login')]"

    def vpisat_admin_meno(self, admin_name):
        self.driver.find_element(By.ID, self.admin_name_id).click()
        self.driver.find_element(By.ID, self.admin_name_id).clear()
        self.driver.find_element(By.ID, self.admin_name_id).send_keys(admin_name)

    def vpisat_admin_heslo(self, admin_passw):
        self.driver.find_element(By.ID, self.admin_email_id).click()
        self.driver.find_element(By.ID, self.admin_email_id).clear()
        self.driver.find_element(By.ID, self.admin_email_id).send_keys(admin_passw)

    def klik_na_login_tlacidlo(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        return DashboardPage(self.driver)

    def prihlasenie_admina(self, admin_name, admin_passw):
        self.vpisat_admin_meno(admin_name)
        self.vpisat_admin_heslo(admin_passw)
        return self.klik_na_login_tlacidlo()