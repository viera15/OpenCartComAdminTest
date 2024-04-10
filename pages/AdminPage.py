from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage


class AdminPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    admin_name_id = "input-username"
    admin_email_id = "input-password"
    button_login_xpath = "//button[contains(text(), 'Login')]"

    def vpisat_admin_meno(self, admin_name):
        self.vpisanie_textu_do_elementu(admin_name, "admin_name_id",self.admin_name_id)

    def vpisat_admin_heslo(self, admin_passw):
        self.vpisanie_textu_do_elementu(admin_passw, "admin_email_id",self.admin_email_id)


    def klik_na_login_tlacidlo(self):
        self.klik_na_element("button_login_xpath", self.button_login_xpath)
        return DashboardPage(self.driver)

    def prihlasenie_admina(self, admin_name, admin_passw):
        self.vpisat_admin_meno(admin_name)
        self.vpisat_admin_heslo(admin_passw)
        return self.klik_na_login_tlacidlo()