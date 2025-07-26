from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactPage(BasePage):
    CONTACT_LINK = (By.LINK_TEXT, "Contact us")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    SUBJECT_INPUT = (By.NAME, "subject")
    MESSAGE_INPUT = (By.NAME, "message")
    SUBMIT_BUTTON = (By.NAME, "submit")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(),'Success!')]")

    def submit_form(self, name, email, subject, message):
        self.click(self.CONTACT_LINK)
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.SUBJECT_INPUT, subject)
        self.enter_text(self.MESSAGE_INPUT, message)
        self.click(self.SUBMIT_BUTTON)

    def is_submission_successful(self):
        return self.is_visible(self.SUCCESS_MESSAGE)
