import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests import BASE_URL, DEFAULT_WAIT


class BasePage:
    PAGE_URL = f"{BASE_URL}"
    PAGE_HEADER = ''

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)

    def go_to_page(self):
        self.browser.get(self.PAGE_URL)
