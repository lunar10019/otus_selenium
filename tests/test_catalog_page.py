from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_title(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2")))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content > h2"), "Desktops"))
    assert el.text == "Desktops"


def test_check_content(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "content")))


def test_check_display_control(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "display-control")))


def test_check_input_sort(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "input-sort")))


def test_check_sidebar(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "column-left")))


def test_change_currency(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    item_first_prices_text = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "#product-list > div:nth-child(1) > div > div.content > div > div > span.price-new",
            )
        ),
    ).text
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "dropdown"))).click()
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2) > a")
        ),
    ).click()
    item_second_prices_text = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "#product-list > div:nth-child(1) > div > div.content > div > div > span.price-new",
            )
        ),
    ).text
    assert item_first_prices_text != item_second_prices_text
