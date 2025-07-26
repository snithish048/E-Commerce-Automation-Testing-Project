from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_LINK = (By.LINK_TEXT, "Signup / Login")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(), 'Logged in as')]")

    def login(self, email, password):
        self.click(self.LOGIN_LINK)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        return self.is_visible(self.LOGGED_IN_TEXT)
