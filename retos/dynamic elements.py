import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class DisapearElements(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('./chromedriver')
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()
        driver.maximize_window()

    def test_name_elements(self):
        driver = self.driver
        elements = []
        tries = 0

        while 'Gallery' not in elements:
            elements.clear()
            elements_list = self.driver.find_elements(By.XPATH, '//*[@id="content"]/div/ul/li')

            for element in elements_list:
                elements.append(element.text)
            print(elements)
            tries += 1
            driver.refresh()

        print(f'finished in {tries} tries')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
