from pages.product_page import ProductPage

def test_search_product(browser):
    product_page = ProductPage(browser)
    product_page.search_product("Tshirt")
    assert product_page.is_result_displayed()
