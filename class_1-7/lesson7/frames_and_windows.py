import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

    def tearDown(self):
        self.browser.quit()

    def test_within_frame(self):
        self.browser.get('https://demoqa.com/frames')
        check_correct_site = self.browser.find_element(By.CLASS_NAME, 'main-header').text
        self.assertEqual('Frames', check_correct_site)

        iframe = self.browser.find_element(By.ID, "frame1")
        self.browser.switch_to.frame(iframe)