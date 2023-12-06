import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

from fixtures.admin_login_fixture import AdminLoginFixture
from fixtures.login import LogIn

fake = Faker()

login = LogIn()


class Test_Add_Employee_And_Login_Validation(AdminLoginFixture):

    def test_employee_and_login(self):
        self.browser.find_element(By.XPATH, "//input[@id='btnAdd']").click()
        first_name = fake.first_name()
        self.browser.find_element(By.XPATH, "//input[@id='firstName']").send_keys(first_name)

        last_name = fake.last_name()
        self.browser.find_element(By.XPATH, "//input[@id='lastName']").send_keys(last_name)

        check = self.browser.find_element(By.XPATH, "//input[@id='chkLogin']").click()
        user_name = fake.user_name()
        self.browser.find_element(By.XPATH, "//input[@id='user_name']").send_keys(user_name)

        passw = fake.password()
        self.browser.find_element(By.XPATH, "//input[@id='user_password']").send_keys(passw)
        self.browser.find_element(By.XPATH, "//input[@id='re_password']").send_keys(passw)

        save = self.browser.find_element(By.XPATH, "//input[@id='btnSave']").click()

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='welcome']"))
        ).click()

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Logout')]"))
        ).click()

        login.log_in(self.browser, user_name, passw, first_name)
