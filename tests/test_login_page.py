from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_title(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-login > h2"))
    )
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#form-login > h2"), "Returning Customer"
        )
    )
    assert el.text == "Returning Customer"


def test_check_content(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "content")))


def test_check_email_input(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "input-email")))


def test_check_password_input(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")))


def test_check_account_login_page(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "account-login")))
