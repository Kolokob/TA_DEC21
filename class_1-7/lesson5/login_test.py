import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest(unittest.TestCase):



    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.browser.get('http://www.google.com')

    def tearDown(self):
        self.browser.quit()

    def test_valid_login(self):
        self.browser.get('http://hrm-online.portnov.com/symfony/web/index.php/auth/login')
        login_field = self.browser.find_element(By.ID, 'txtUsername')
        login_field.send_keys('admin')
        password_field = self.browser.find_element(By.ID, 'txtPassword')
        password_field.send_keys('password')
        login_button = self.browser.find_element(By.ID, 'btnLogin')
        login_button.click()
        employee_taylor = self.browser.find_element(By.XPATH, "//a[contains(text(),'Taylor')]").text
        assert employee_taylor == 'Taylor'


if __name__ == '__main__':
    unittest.main()
