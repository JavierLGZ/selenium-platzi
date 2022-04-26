import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class Tables(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('./chromedriver')
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()
        driver.maximize_window()

    def test_sort_tables(self):
        driver = self.driver
        table_data = [[] for _ in range(5)]

        for i in range(5):
            header = driver.find_element(By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)
            for j in range(4):
                row_data = driver.find_element(By.XPATH, f'//*[@id="table1"]/tbody/tr[{j +1}]/td[{i+1}]')
                table_data[i].append(row_data.text)

        print(table_data)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
