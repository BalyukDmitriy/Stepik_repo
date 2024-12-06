from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    t = browser.find_element(By.ID, "treasure")
    peremen = t.get_attribute("valuex")
    y = calc(peremen)

    print(y)

    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(y)
    chb = browser.find_element(By.ID, "robotCheckbox")
    chb.click()
    rb = browser.find_element(By.ID, "robotsRule")
    rb.click()
    sb = browser.find_element(By.CLASS_NAME, "btn")
    sb.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()