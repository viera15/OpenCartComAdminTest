from selenium.webdriver.common.by import By

class AdminPage:

    def __init__(self, driver):
        self.driver = driver

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