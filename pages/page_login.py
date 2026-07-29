import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from conftest import  driver

class LoginPage:
    def __init__(self, driver):
        self.driver = WebDriver
        self.wait = WebDriverWait(driver, 10)
        self.username_input = (By.XPATH, '//*[@id="user-name"]')
        self.password_input = (By.XPATH, '//*[@id="password"]')
        self.login_btn = (By.XPATH, '//*[@id="login-button"]')


    def inserting_values_in_input_fields(self, username, password):
        self.wait.until(ec.visibility_of_element_located(self.username_input)).send_keys(username)
        self.wait.until(ec.visibility_of_element_located(self.password_input)).send_keys(password)

    def clicking_in_login_button(self):
        self.wait.until(ec.visibility_of_element_located(self.login_btn)).click()

    def verifying_if_url_has_been_changed(self):
        return self.driver.current_url