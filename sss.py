from selenium import webdriver
import time

driver =webdriver.Chrome()

driver.get("http://www.fb.com")
driver.find_element_by_name("email").send_keys("9492716980")
time.sleep(5)
driver.find_element_by_name("pass").send_keys("Svivek123#")
time.sleep(5)
driver.find_element_by_name("login").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/span/div/div[1]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[5]/div/div[1]/div[2]/div/div/div/div/span").click()
driver.delete_all_cookies()
time.sleep(5)
driver.close()