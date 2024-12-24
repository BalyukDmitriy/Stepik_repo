from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    btn1 = browser.find_element(By.ID, "book").click()

    zn1 = browser.find_element(By.ID, "input_value")
    zn1 = zn1.text
    zn2 = browser.find_element(By.ID, "answer")
    zn2.send_keys(calc(zn1))
    btn2 = browser.find_element(By.ID, "solve")
    btn2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()