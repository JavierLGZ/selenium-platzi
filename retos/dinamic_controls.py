import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicControls(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('./chromedriver')
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()
        driver.maximize_window()

    def test_dynamic_controls(self):
        driver = self.driver
        checkbox = driver.find_element(By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')
        checkbox.click()
        remove_add_button = driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button')
        remove_add_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))

        enable_disable_button = driver.find_element(By.CSS_SELECTOR, '#input-example > button')
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))
        text_area = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
        text_area.send_keys('platzi')
        enable_disable_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
