from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CLASS_NAME, "btn")
    btn.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    q = browser.find_element(By.ID, "input_value")
    y = browser.find_element(By.ID, "answer")
    x = q.text
    y.send_keys(calc(x))
    btn1 = browser.find_element(By.CLASS_NAME, "btn")
    btn1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()