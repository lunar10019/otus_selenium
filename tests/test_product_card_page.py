from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_tabs(browser):
    browser.get(f"{browser.base_url}/index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#content > ul")),
    )


def test_check_content(browser):
    browser.get(f"{browser.base_url}/index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "content")))


def test_check_product_info(browser):
    browser.get(f"{browser.base_url}/index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "product-info")))


def test_check_button_cart(browser):
    browser.get(f"{browser.base_url}/index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))


def test_check_account_form_product(browser):
    browser.get(f"{browser.base_url}/index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "form-product")))
