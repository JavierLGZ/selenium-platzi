import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class DynamicControls(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('./chromedriver')
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, 'Typos').click()
        driver.maximize_window()

    def test_find_typos(self):
        driver = self.driver
        paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
        text_to_check = paragraph_to_check.text
        tries = 1
        correct_text = "Sometimes you'll see a typo, other times you won't."
        while correct_text != text_to_check:
            driver.refresh()
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            tries += 1

        print(f"it need {tries} tries")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
