from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_logo(browser):
    browser.get(f"{browser.base_url}")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "logo")), message="")


def test_check_navbar(browser):
    browser.get(f"{browser.base_url}")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "narbar-menu")), message="")


def test_check_search(browser):
    browser.get(f"{browser.base_url}")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "search")), message="")


def test_check_content(browser):
    browser.get(f"{browser.base_url}")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > h3"))
    )
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content > h3"), "Featured")
    )
    assert el.text == "Featured"


def test_check_button_cart(browser):
    browser.get(f"{browser.base_url}")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "header-cart")), message="")


def test_change_currency(browser):
    browser.get(f"{browser.base_url}")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    item_first_prices_text = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > div > div > span.price-new",
            )
        ),
        message="",
    ).text
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "dropdown")), message=""
    ).click()
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2) > a")
        ),
        message="",
    ).click()
    item_second_prices_text = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > div > div > span.price-new",
            )
        ),
        message="",
    ).text
    assert item_first_prices_text != item_second_prices_text
