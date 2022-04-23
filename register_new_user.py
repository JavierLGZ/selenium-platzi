import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class RegisterNewUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('./chromedriver')
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_new_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, '/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element(By.LINK_TEXT, 'Log In').click()

        create_account_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element(By.ID, 'firstname')
        middle_name = driver.find_element(By.ID, 'middlename')
        last_name = driver.find_element(By.ID, 'lastname')
        email_address = driver.find_element(By.ID, 'email_address')
        news_letter = driver.find_element(By.ID, 'is_subscribed')
        password = driver.find_element(By.ID, 'password')
        confirm_password = driver.find_element(By.ID, 'confirmation')
        summit_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(
            first_name.is_enabled()
            and middle_name.is_enabled()
            and last_name.is_enabled()
            and email_address.is_enabled()
            and news_letter.is_enabled()
            and password.is_enabled()
            and confirm_password.is_enabled()
            and summit_button.is_enabled())

        first_name.send_keys('test')
        middle_name.send_keys('test')
        last_name.send_keys('test')
        email_address.send_keys('test')
        password.send_keys('test')
        confirm_password.send_keys('test')
        summit_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='search-test-report'))
