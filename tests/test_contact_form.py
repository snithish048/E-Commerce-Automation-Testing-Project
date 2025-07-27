from pages.contact_page import ContactPage
from selenium.webdriver.common.alert import Alert

def test_contact_form(browser):
    alert = Alert(browser)
    contact = ContactPage(browser)
    contact.submit_form("Nithish", "nithish@example.com", "Hello", "This is a test.")

    # Handle alert if it appears
    try:
        alert = Alert(browser)
        print("Alert text:", alert.text)
        alert.accept()
        print("Alert accepted")
    except:
        print("No alert appeared")

    assert contact.is_submission_successful()
