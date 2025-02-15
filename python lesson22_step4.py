from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("window.scrollBy(0, 150);")

    x = browser.find_element(By.ID, "input_value")
    x = x.text
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(calc(x))

    chb = browser.find_element(By.ID, "robotCheckbox")
    chb.click()

    rb = x = browser.find_element(By.ID, "robotsRule")
    rb.click()

    but = x = browser.find_element(By.CLASS_NAME, "btn")
    but.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()