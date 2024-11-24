import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(5)

driver.get("https://yandex.ru")
time.sleep(5)

driver.close()