import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class UI_TEST(unittest.TestCase):
    def test_something(self):
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://www.google.com')
        browser.find_element(By.NAME, 'q').send_keys('Hello')
        browser.find_element(By.NAME, 'q').submit()
        link = browser.find_element(By.CSS_SELECTOR, 'a>h3').text
        self.assertIN('hello', link)



if __name__ == '__main__':
    unittest.main()
