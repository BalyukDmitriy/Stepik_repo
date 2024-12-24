from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element(By.CLASS_NAME, "btn")
    btn1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)
    zn1 = browser.find_element(By.ID, "input_value")
    zn2 = browser.find_element(By.ID, "answer")
    x = calc(zn1.text)
    zn2.send_keys(x)
    btn2 = browser.find_element(By.CLASS_NAME, "btn")
    btn2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()