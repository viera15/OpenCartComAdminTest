import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://demo.opencart.com/admin/")

driver.find_element(By.ID, "input-username").send_keys("demo")
driver.find_element(By.ID,"input-password").send_keys("demo")
driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

wait = WebDriverWait(driver, 35)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='modal-dialog']")))
driver.find_element(By.XPATH, "//*[@id='modal-security']/div/div/div[1]/button").click()

ocakavany_text = "Logout"
assert driver.find_element(By.XPATH, "//header/div/ul/li[3]/a/span").text.__contains__(ocakavany_text)


time.sleep(5)
driver.quit()