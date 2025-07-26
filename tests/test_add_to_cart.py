import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_add_to_cart(browser):
    browser.execute_script("window.scrollBy(0, 600);")
    time.sleep(2)

    add_to_cart = browser.find_element(By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")
    ActionChains(browser).move_to_element(add_to_cart).click().perform()
    time.sleep(2)

    assert "Your product has been added to cart" in browser.page_source
