import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


class AddRemoveElements(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('./chromedriver')
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        driver.maximize_window()

    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input('how many elements will you add?: '))
        elements_removed = int(input('how many elements will you remove?: '))
        tot_elements = elements_added - elements_removed

        sleep(3)
        for i in range(elements_added):
            self.driver.execute_script('addElement()')
        sleep(3)
        for i in range(elements_removed):
            self.driver.execute_script('deleteElement()')
        sleep(3)

        if tot_elements > 0:
            print(f'there are {tot_elements} elements on screen')
        else:
            print('there are 0 elements on screen')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
