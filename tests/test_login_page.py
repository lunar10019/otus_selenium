from page_objects.login_page import LoginPage


def test_check_title(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    LoginPage(browser).check_title()


def test_check_content(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    LoginPage(browser).check_content()


def test_check_email_input(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    LoginPage(browser).check_email_input()


def test_check_password_input(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    LoginPage(browser).check_password_input()


def test_check_account_login(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    LoginPage(browser).check_account_login()
