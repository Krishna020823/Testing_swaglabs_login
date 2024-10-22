from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators for login elements
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def enter_username(self, username: str):
        self.send_keys(*self.USERNAME_FIELD, username)

    def enter_password(self, password: str):
        self.send_keys(*self.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
