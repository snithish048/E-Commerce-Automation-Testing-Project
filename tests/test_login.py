from pages.login_page import LoginPage

def test_login(browser):
    login_page = LoginPage(browser)
    login_page.login("nithish@email.com", "testpassword")
    assert login_page.is_login_successful()
