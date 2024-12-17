from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    inp1 = browser.find_element(By.CSS_SELECTOR, ('input[placeholder="Enter first name"]'))
    inp1.send_keys("Ivan")
    inp2 = browser.find_element(By.CSS_SELECTOR, ('input[placeholder="Enter last name"]'))
    inp2.send_keys("Petrov")
    inp3 = browser.find_element(By.CSS_SELECTOR, ('input[placeholder="Enter email"]'))
    inp3.send_keys("Ivan.Petrov@yandex.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    element = browser.find_element(By.ID, "file.txt")
    element.send_keys(file_path)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()