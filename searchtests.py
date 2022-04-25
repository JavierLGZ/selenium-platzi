import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class SearchTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('./chromedriver')
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_tee(self):
        driver = self.driver
        serch_field = driver.find_element(by=By.NAME, value='q')
        serch_field.clear()
        serch_field.send_keys("tee")
        serch_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        serch_field = driver.find_element(By.NAME, 'q')
        serch_field.send_keys('salt shaker')
        serch_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/a')
        self.assertEqual(1, len(products))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
