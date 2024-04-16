from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def vpisanie_textu_do_elementu(self, text, locator_name, locator_value):
        # všeobecná funkcia pre vpísanie textu do elementu
        element = self.vezmi_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def klik_na_element(self, locator_name, locator_value):
        # všeobecná funkcia pre kliknutie na element
        element = self.vezmi_element(locator_name, locator_value)
        element.click()

    def ziskanie_textu_elementu(self, locator_name, locator_value):
        # všeobecná funkcia, ktorá získa text z elementu
        element = self.vezmi_element(locator_name, locator_value)
        return element.text

    def kontrola_zobrazovania_elementu(self, locator_name, locator_value):
        # všeobecná funkcia, ktorá zistí, či je element zobrazený
        element = self.vezmi_element(locator_name, locator_value)
        return element.is_displayed()

    def vezmi_element(self, locator_name, locator_value):
        """ všeobecná funkcia, ktorá zistí z názvu premennej aký typ lokátoru obsahuje a vráti element podľa daného
        lokátoru """
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

