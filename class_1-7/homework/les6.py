import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class LoginTest(unittest.TestCase):
    LINK = 'http://hrm-online.portnov.com/'

    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.browser.get('http://www.google.com')

    def tearDown(self):
        self.browser.quit()

    def login_method(self):
        self.browser.get(self.LINK)
        self.browser.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys('admin')
        self.browser.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys('password')
        self.browser.find_element(By.XPATH, "//input[@id='btnLogin']").click()
        self.browser.implicitly_wait(2)

    def test_search_by_name(self):

        self.login_method()

        dropdown = self.browser.find_element(By.XPATH, "//select[@id='empsearch_job_title']")
        select = Select(dropdown)
        select.select_by_visible_text("QA Manager")
        self.browser.find_element(By.XPATH, "//input[@id='searchBtn']").click()

        rows = self.browser.find_elements(By.XPATH,
                                          "//tr[contains(@class, 'odd') or contains(@class, 'even')][.//td[contains(text(), 'QA Manager')]]")

        temp = [' '.join(i.text.split()[3:5]) for i in rows]
        check_res = all([i == temp[0] for i in temp])
        return check_res

    def test_alphabetical_order(self):

        self.login_method()

        self.browser.find_element(By.XPATH, "//a[contains(text(),'First (& Middle) Name')]").click()

        rows = self.browser.find_elements(By.XPATH, "//tr[contains(@class, 'odd') or contains(@class, 'even')]")

        temp = [i.text.split()[1].lower() for i in rows]

        for i in range(len(temp) - 1):
            if temp[i] > temp[i + 1]:
                return False

        return True



