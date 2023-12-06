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

        frame_text = self.browser.find_element(By.ID, 'sampleHeading').text
        self.assertEqual('This is a sample page', frame_text)

        self.browser.switch_to.default_content()

        self.browser.switch_to.frame(self.browser.find_element(By.ID, "frame2"))

    def test_nested_frame(self):

        expected_text = 'Child Iframe'

        self.browser.get('https://demoqa.com/nestedframes')

        check_correct_site = self.browser.find_element(By.CLASS_NAME, 'main-header').text
        self.assertEqual('Nested Frames', check_correct_site)

        parent_frame = self.browser.find_element(By.ID, 'frame1')
        self.browser.switch_to.frame(parent_frame)

        child_frame = self.browser.find_element(By.TAG_NAME, 'iframe')
        self.browser.switch_to.frame(child_frame)

        self.assertEqual(expected_text, self.browser.find_element(By.XPATH, "//body/p").text)

        self.browser.switch_to.default_content()

    def test_other_page(self):
        self.browser.get('https://demoqa.com/browser-windows')

        self.browser.find_element(By.ID, "windowButton").click()

        open_windows = self.browser.window_handles
        self.browser.switch_to.window(open_windows[-1])

        window_url = self.browser.current_url
        self.assertIn('/sample', window_url)

        self.browser.switch_to.window(open_windows[0])

        self.assertEqual('This is sample page', self.browser.find_element(By.ID, 'sampleHeading').text)
