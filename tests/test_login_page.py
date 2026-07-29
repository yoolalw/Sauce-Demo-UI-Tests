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
        self.login_page.clicking_in_login_button()
        assert self.login_page.verifying_if_url_has_been_changed()

    def test_inserting_locked_user_in_fields(self):
        self.login_page.inserting_values_in_input_fields(self.data.locked_user, self.data.password)
        self.login_page.clicking_in_login_button()
        assert self.login_page.see_message() == 'Epic sadface: Sorry, this user has been locked out.'

    def test_inserting_incorrect_password(self):
        self.login_page.inserting_values_in_input_fields(self.data.standard, 'wrongPassword')
        self.login_page.clicking_in_login_button()
        assert self.login_page.see_message() == 'Epic sadface: Username and password do not match any user in this service'

    def test_inserting_null_fields(self):
        self.login_page.inserting_values_in_input_fields('', '')
        self.login_page.clicking_in_login_button()
        assert self.login_page.see_message() == 'Epic sadface: Username is required'

    def test_inserting_password_without_data(self):
        self.login_page.inserting_values_in_input_fields('standard', '')
        self.login_page.clicking_in_login_button()
        assert self.login_page.see_message() == 'Epic sadface: Password is required'



