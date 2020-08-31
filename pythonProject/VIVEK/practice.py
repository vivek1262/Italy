from selenium import webdriver
import time

root = webdriver.Chrome()
root.get("http://www.gmail.com")
time.sleep(5)
root.close()