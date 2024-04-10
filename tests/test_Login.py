import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_spravne_udaje(self):
        self.driver.find_element(By.ID, "input-username").send_keys("demo")
        self.driver.find_element(By.ID, "input-password").send_keys("demo")
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()


        wait = WebDriverWait(self.driver, 35)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='modal-dialog']")))
        self.driver.find_element(By.XPATH, "//*[@id='modal-security']/div/div/div[1]/button").click()

        ocakavany_text = "Logout"
        assert self.driver.find_element(By.XPATH, "//header/div/ul/li[3]/a/span").text.__contains__(ocakavany_text)






