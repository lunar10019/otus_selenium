from page_objects.registration_page import RegistrationPage


def test_check_title(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")
    RegistrationPage(browser).check_title()

def test_check_content(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")
    RegistrationPage(browser).check_content()

def test_check_subscribe_toggle(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")
    RegistrationPage(browser).check_subscribe_toggle()

def test_check_account_register(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")
    RegistrationPage(browser).check_account_register()

def test_check_sidebar(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")
    RegistrationPage(browser).check_sidebar()

def test_registration(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")
    RegistrationPage(browser).wait_form_registration()
    RegistrationPage(browser).fill_form_registration()
    RegistrationPage(browser).privacy_policy_agree()
    RegistrationPage(browser).register_button()





