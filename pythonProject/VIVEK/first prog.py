from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.facebook.com")
username = '//*[@id="email"]'
password = '//*[@id="pass"]'
log_in = '//*[@id="u_0_b"]'

time.sleep(5)
driver.find_element_by_xpath(username).send_keys("9492716980")
driver.find_element_by_xpath(password).send_keys("Svivek123#")

time.sleep(5)
driver.find_element_by_xpath(log_in).click()
time.sleep(10)

driver.close()
print("fb login successfully")