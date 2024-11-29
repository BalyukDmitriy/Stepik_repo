import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.driver.get(link)

        input1 = self.driver.find_element(By.CSS_SELECTOR, "div > input")
        input1.send_keys("Ivan")
        input2 = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input")
        input2.send_keys("Petrov")
        input3 = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > input")
        input3.send_keys("Smolensk")
        button = self.driver.find_element(By.CSS_SELECTOR, "button")
        button.click()

        welcome_text_elt = self.driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        self.driver.quit()

class TestRegistration2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.driver.get(link)

        input1 = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > input")
        input1.send_keys("Ivan")
        input2 = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input")
        input2.send_keys("Petrov")
        input3 = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > input")
        input3.send_keys("Smolensk")
        button = self.driver.find_element(By.CSS_SELECTOR, "button")
        button.click()

        time.sleep(1)
        welcome_text_elt = self.driver.find_element(By.TAG_NAME, "h1")  # Finding the welcome message
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()