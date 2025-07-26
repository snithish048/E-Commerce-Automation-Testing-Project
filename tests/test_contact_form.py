from pages.contact_page import ContactPage

def test_contact_form(browser):
    contact = ContactPage(browser)
    contact.submit_form("Alagu Nithis", "alagunit@example.com", "Hello", "This is a test.")
    assert contact.is_submission_successful()
