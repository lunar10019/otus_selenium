from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductCardPage(BasePage):
    TABS = By.CSS_SELECTOR, "#content > ul"
    CONTENT = By.CSS_SELECTOR, "#content > h3"
    PRODUCT_INFO = By.ID, "product-info"
    BUTTON_CART = By.ID, "button-cart"
    FORM_PRODUCT = By.ID, "form-product"

    def check_tabs(self):
        self.get_element(self.TABS)
        return self

    def check_content(self):
        self.get_element(self.CONTENT)
        return self

    def check_product_info(self):
        self.get_element(self.PRODUCT_INFO)
        return self

    def check_button_cart(self):
        self.get_element(self.BUTTON_CART)
        return self

    def check_account_form_product(self):
        self.get_element(self.FORM_PRODUCT)
        return self
