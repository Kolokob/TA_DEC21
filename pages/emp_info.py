from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.log_in import LoginPage


class EmployeeInfo(LoginPage):

    TABLE_HEADERS = ['Id', 'First (& Middle) Name', 'Last Name',
                     'Job Title', 'Employment Status', 'Sub Unit', 'Supervisor']

    btn_search = (By.XPATH, "//input[@id='searchBtn']")
    btn_reset = (By.XPATH, "//input[@id='resetBtn']")
    btn_add = (By.XPATH, "//input[@id='btnAdd']")
    select_job_title = (By.XPATH, "//select[@id='empsearch_job_title']")
    fld_employee_name = (By.ID, 'empsearch_employee_name_empName')


    def get_table_data(self, row, col):
        locator = f'//tr[{row}]td[{col}]'
        return self.browser.find_element(By.XPATH, locator)

    def click_table_header(self, table_header):
        if table_header not in self.TABLE_HEADERS:
            raise ValueError(f"Unknown {table_header} table header")

        locator = f'//tr/a[text() = "{table_header}"]'
        self.browser.find_element(By.ID, locator).click()

    def reset_search_form(self):
        self.browser.find_element(*self.btn_reset).click()

    def search_by_job_title(self, job_title):

        select_elem = self.browser.find_element(*self.select_job_title)
        Select(select_elem).select_by_visible_text(job_title)

        self.browser.find_element(*self.btn_search).click()

    def search_by_employee_name(self, emp_name):
        self.browser.find_element(*self.fld_employee_name).send_keys(emp_name)
        self.browser.find_element(*self.btn_search).click()


