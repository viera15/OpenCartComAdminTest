import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.opencart.com/admin/")

driver.find_element(By.ID, "input-username").send_keys("demo")
driver.find_element(By.ID,"input-password").send_keys("demo")
driver.find_element(By.XPATH, "//button[contains(text(), ' Login')]").click()