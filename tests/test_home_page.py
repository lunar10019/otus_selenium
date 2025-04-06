from page_objects.home_page import HomePage


def test_check_logo(browser):
    browser.get(f"{browser.base_url}")
    HomePage(browser).check_logo()


def test_check_navbar(browser):
    browser.get(f"{browser.base_url}")
    HomePage(browser).check_navbar()


def test_check_search(browser):
    browser.get(f"{browser.base_url}")
    HomePage(browser).check_search()


def test_check_content(browser):
    browser.get(f"{browser.base_url}")
    HomePage(browser).check_content()


def test_check_button_cart(browser):
    browser.get(f"{browser.base_url}")
    HomePage(browser).check_button_cart()


def test_change_currency(browser):
    browser.get(f"{browser.base_url}")
    item_first_prices_text = HomePage(browser).get_first_price()
    HomePage(browser).click_on_dropdown()
    HomePage(browser).click_on_form_currency()
    HomePage(browser).dropdown_is_not_visible()
    item_second_prices_text = HomePage(browser).get_second_price()
    assert item_first_prices_text != item_second_prices_text
