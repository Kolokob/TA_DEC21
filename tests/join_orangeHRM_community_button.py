import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select
from fixtures.admin_login_fixture import AdminLoginFixture


class Test_Join_OrangeHRM_Community(AdminLoginFixture):

    def test_employee_and_login(self):
        self.browser.find_element(By.XPATH, "//a[contains(text(),'Join OrangeHRM Community')]").click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        check_text = self.browser.find_element(By.XPATH, "//input[@id='Form_submitForm_action_request']").is_displayed()
        return check_text

    def test_search_by_name(self):
        # Test_2_0_employee_sort
        dropdown = self.browser.find_element(By.XPATH, "//select[@id='empsearch_job_title']")
        select = Select(dropdown)
        select.select_by_visible_text("QA Manager")
        self.browser.find_element(By.XPATH, "//input[@id='searchBtn']").click()

        rows = self.browser.find_elements(By.XPATH,
                                          "//tr[contains(@class, 'odd') or contains(@class, 'even')][.//td[contains(text(), 'QA Manager')]]")

        temp = [' '.join(i.text.split()[3:5]) for i in rows]
        check_res = all([i == temp[0] for i in temp])
        return check_res

    def test_alphabetical_order_for_multiple_pages(self):

        counter = 1
        self.browser.find_element(By.XPATH, "//a[contains(text(),'First (& Middle) Name')]").click()
        try:
            while True:
                rows = self.browser.find_elements(By.XPATH, "//tr[contains(@class, 'odd') or contains(@class, 'even')]")

                temp = [i.text.split()[1].lower() for i in rows]



                for i in range(len(temp) - 1):
                    if temp[i] == temp[i + 1]:
                        continue
                    self.assertLess(temp[i], temp[i + 1])

                counter += 1

                self.browser.find_element(By.XPATH, f"//ul[@class='paging bottom']//*[normalize-space(text()) = '{counter}']").click()

        except NoSuchElementException:
            if len(temp) < 50:
                print('The list of employees that less then 51 is in ASC order')
            else:
                print('The list of employees is in ASC order')
            return

