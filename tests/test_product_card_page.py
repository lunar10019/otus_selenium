from page_objects.product_card import ProductCardPage


def test_check_tabs(browser):
    browser.get(
        f"{browser.base_url}/index.php?route=product/product&path=57&product_id=49"
    )
    ProductCardPage(browser).check_tabs()


def test_check_content(browser):
    browser.get(
        f"{browser.base_url}/index.php?route=product/product&path=57&product_id=49"
    )
    ProductCardPage(browser).check_content()


def test_check_product_info(browser):
    browser.get(
        f"{browser.base_url}/index.php?route=product/product&path=57&product_id=49"
    )
    ProductCardPage(browser).check_product_info()


def test_check_button_cart(browser):
    browser.get(
        f"{browser.base_url}/index.php?route=product/product&path=57&product_id=49"
    )
    ProductCardPage(browser).check_button_cart()


def test_check_account_form_product(browser):
    browser.get(
        f"{browser.base_url}/index.php?route=product/product&path=57&product_id=49"
    )
    ProductCardPage(browser).check_account_form_product()
