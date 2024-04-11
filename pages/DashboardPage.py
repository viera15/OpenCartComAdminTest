from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        
    modal_window_xpath = "//div[@class='modal-dialog']"
    button_modal_window_xpath = "//*[@id='modal-security']/div/div/div[1]/button"
    logout_option_xpath = "//header/div/ul/li[3]/a/span"
    logo_cesta_xpath = "//img[@title= 'OpenCart']"
    profil_dropdown_xpath = "//span[@class= 'd-none d-md-inline d-lg-inline']"

    def cakanie_na_modalne_okno(self):
        wait = WebDriverWait(self.driver, 35)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.modal_window_xpath)))

    def klik_na_tlacidlo_modalneho_okna(self):
        self.klik_na_element("button_modal_window_xpath", self.button_modal_window_xpath)
        
    def zatvorenie_modalneho_okna(self):
        self.cakanie_na_modalne_okno()
        return self.klik_na_tlacidlo_modalneho_okna()

    #TODO zjednodušiť a použiť metódu z BasePage
    def vratenie_textu_logout(self):
        return self.driver.find_element(By.XPATH, self.logout_option_xpath).text

    def klik_na_logout(self):
        self.klik_na_element("logout_option_xpath", self.logout_option_xpath)

    def zobrazovanie_loga(self):
        return self.kontrola_zobrazovania_elementu("logo_cesta_xpath", self.logo_cesta_xpath)
    
    def vratenie_textu_dropdown_profilu(self):
        return self.ziskanie_textu_elementu("profil_dropdown_xpath", self.profil_dropdown_xpath)



