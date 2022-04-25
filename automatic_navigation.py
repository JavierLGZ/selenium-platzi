import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

class NavigationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('./chromedriver')
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.get("http://google.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_browser_navigation(self):
        driver = self.driver
        serch_field = driver.find_element(By.NAME, 'q')
        serch_field.send_keys('platzi')
        serch_field.submit()

        driver.back()
        driver.forward()
        driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
