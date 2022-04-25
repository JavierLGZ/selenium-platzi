import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('./chromedriver')
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        serch_field = self.driver.find_element(by=By.ID, value="search")

    def test_search_text_field_by_name(self):
        serch_field = self.driver.find_element(By.NAME, "q")

    def test_search_text_field_by_class_name(self):
        serch_field = self.driver.find_element(By.CLASS_NAME, "input-text")

    def test_search_button_enable(self):
        button = self.driver.find_element(By.CLASS_NAME, "button")

    def test_count_promo_banner_images(self):
        banner_list = self.driver.find_element(By.CLASS_NAME, "promos")
        banners = banner_list.find_elements(by=By.TAG_NAME, value='img')
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        xpath = '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[1]'
        vip_promo = self.driver.find_element(By.XPATH, xpath)

    def test_shoppin_cart(self):
        css_selector = "div.header-minicart span.icon"
        serch_field = self.driver.find_element(By.CSS_SELECTOR, css_selector)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
 

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='search-test-report'))
