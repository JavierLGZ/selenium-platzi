import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from time import sleep


class TestingMercadoLibre(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('../chromedriver')
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.get("http://www.mercadolibre.com/")
        driver.maximize_window()

    def test_serch_ps4(self):
        items = {}
        driver = self.driver
        country = driver.find_element(By.ID, 'CO')
        country.click()
        search_field = driver.find_element(By.NAME, 'as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()

        location = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div/aside/section/div[6]/ul/li[1]/a/span[1]')
        driver.execute_script("arguments[0].click()", location)
        sleep(3)

        codition = driver.find_element(By.PARTIAL_LINK_TEXT, 'Nuevo')
        codition.click()
        sleep(3)

        order_menu = driver.find_element(By.CSS_SELECTOR, '#root-app > div > div > section > div.ui-search-view-options__container > div > div > div > div.ui-search-sort-filter > div > div > button > span')
        order_menu.click()
        higher_price = driver.find_element(By.CSS_SELECTOR, '#root-app > div > div > section > div.ui-search-view-options__container > div > div > div > div.ui-search-sort-filter > div > div > div > ul > a:nth-child(3)')
        higher_price.click()
        sleep(3)

        for i in range(5):
            article_name = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            article_price = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
            items[article_name] = article_price
        print(items)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
