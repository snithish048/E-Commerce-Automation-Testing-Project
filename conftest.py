import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()  # or use Firefox()
    driver.maximize_window()
    driver.get("https://automationexercise.com")
    yield driver
    driver.quit()
