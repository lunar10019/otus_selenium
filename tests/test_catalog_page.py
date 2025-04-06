from page_objects.catalog_page import CatalogPage


def test_check_title(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    CatalogPage(browser).check_title()


def test_check_content(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    CatalogPage(browser).check_content()


def test_check_display_control(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    CatalogPage(browser).check_display_control()


def test_check_input_sort(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    CatalogPage(browser).check_input_sort()


def test_check_sidebar(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    CatalogPage(browser).check_sidebar()


def test_change_currency(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")
    item_first_prices_text = CatalogPage(browser).get_first_price()
    CatalogPage(browser).click_on_dropdown()
    CatalogPage(browser).click_on_form_currency()
    CatalogPage(browser).dropdown_is_not_visible()
    item_second_prices_text = CatalogPage(browser).get_second_price()
    assert item_first_prices_text != item_second_prices_text
