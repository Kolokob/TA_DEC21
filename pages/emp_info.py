from selenium.webdriver.common.by import By

from pages.log_in import LoginPage


class EmployeeInfo(LoginPage):
    TABLE_HEADERS = ['Id', 'First (& Middle) Name', 'Last Name',
                     'Job Title', 'Employment Status', 'Sub Unit', 'Supervisor']

    def get_table_data(self, row, col):
        locator = f'//tr[{row}]td[{col}]'
        return self.browser.find_element(By.XPATH, locator)

    def click_table_header(self, table_header):
        if table_header not in self.TABLE_HEADERS:
            raise ValueError(f"Unknown {table_header} table header")

        locator = f'//tr/a[text() = "{table_header}"]'
        self.browser.find_element(By.ID, locator).click()
