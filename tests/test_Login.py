import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.opencart.com/admin/")

time.sleep(3)
driver.quit()