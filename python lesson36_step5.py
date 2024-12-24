from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from selenium import webdriver
import time
import math
import pytest

uncorrected_results = []

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(55)
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(''.join(uncorrected_results))

@pytest.mark.parametrize('link_task', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_find_ufo(browser, link_task):
    link = f"https://stepik.org/lesson/{link_task}/step/1"
    browser.get(link)
    answer_place = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')))
    answer_place.send_keys(str(math.log(int(time.time()))))

    submit_button = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[class="submit-submission"]')))
    submit_button.click()

    option_text = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[class="smart-hints__hint"]'))).text

    if option_text != "Correct!":
        uncorrected_results.append(option_text)

    assert "Correct!" == option_text, f'Error: {option_text}'