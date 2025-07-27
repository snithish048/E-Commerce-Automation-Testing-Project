# 🛒 E-Commerce Automation Testing Project

This is a QA automation project built using **Selenium WebDriver with Python** to test core features of an e-commerce website:  
🔗 [https://automationexercise.com](https://automationexercise.com)

The project follows a **modular test structure** and demonstrates both **functional** and **UI automation testing** using **PyTest** and the **Page Object Model (POM)** design pattern.

---

## 🧪 Features Tested

| Test Case            | Description                                 |
|----------------------|---------------------------------------------|
| Login Test           | Verifies user login with valid credentials |
| Product Search Test  | Tests the product search functionality      |
| Add to Cart Test     | Adds a product to the shopping cart         |
| Contact Form Test    | Submits the contact form with test data     |

---

## 📂 Project Structure

```text
selenium-python-ecommerce-automation/
│
├── conftest.py                 # PyTest setup and teardown
├── requirements.txt            # Dependencies
├── README.md                   # Project documentation
│
├── tests/                      # All test cases
│   ├── test_login.py
│   ├── test_product_search.py
│   ├── test_add_to_cart.py
│   └── test_contact_form.py
│
└── pages/                      # Page Object Model (POM) classes
    ├── base_page.py
    ├── login_page.py
    ├── product_page.py
    └── contact_page.py
