from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        
    modal_window_xpath = "//div[@class='modal-dialog']"
    button_modal_window_xpath = "//*[@id='modal-security']/div/div/div[1]/button"
    logout_option_xpath = "//header/div/ul/li[3]/a/span"

    def cakanie_na_modalne_okno(self):
        wait = WebDriverWait(self.driver, 35)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.modal_window_xpath)))

    def klik_na_tlacidlo_modalneho_okna(self):
        self.driver.find_element(By.XPATH, self.button_modal_window_xpath).click()
        
    def zatvorenie_modalneho_okna(self):
        self.cakanie_na_modalne_okno()
        return self.klik_na_tlacidlo_modalneho_okna()
    
    def vratenie_textu_logout(self):
        return self.driver.find_element(By.XPATH, self.logout_option_xpath).text
