import time

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from pages.page_login import LoginPage
from utils.test_data import DataLogin

@pytest.mark.usefixtures("driver")
class TestLoginPage:
    driver = WebDriver
    wait = WebDriverWait

    def setup_method(self, driver):
        self.driver.get('https://www.saucedemo.com/')
        self.login_page = LoginPage(self.driver)
        self.data = DataLogin()

    def test_inserting_standard_login_in_fields(self):
        self.login_page.inserting_values_in_input_fields(self.data.standard, self.data.password)
        self.login_page.login_btn()
