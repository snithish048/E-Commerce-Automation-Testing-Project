from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    PRODUCT_LINK = (By.XPATH, "//a[text()=' Products']")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCH_TITLE = (By.CLASS_NAME, "title")

    def search_product(self, keyword):
        self.click(self.PRODUCT_LINK)
        self.enter_text(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)

    def is_result_displayed(self):
        return self.is_visible(self.SEARCH_TITLE)
