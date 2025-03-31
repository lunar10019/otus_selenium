from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import random
import string


class ProductGenerator:
    @staticmethod
    def generate_product_name(length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def generate_meta_tag(length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def generate_product_model(length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def generate_keyword(length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class AdminPage(BasePage):
    LOGIN_INPUT = By.ID, "input-username"
    PASSWORD_INPUT = By.ID, "input-password"
    FORM_LOGIN = By.ID, "form-login"
    NAME_INPUT = By.ID, "input-name-1"
    META_TAG_INPUT = By.ID, "input-meta-title-1"
    KEYWORD_INPUT = By.ID, "input-keyword-0-1"
    MODEL_INPUT = By.ID, "input-model"
    ALERT = By.ID, "alert"
    SEO_TAB = By.LINK_TEXT, "SEO"
    DATA_TAB = By.LINK_TEXT, "Data"
    LOGOUT_LINK = By.LINK_TEXT, "Logout"
    PRODUCTS_LINK = By.LINK_TEXT, "Products"
    CATALOG = By.XPATH, '//*[@id="menu-catalog"]/a'
    ADD_PRODUCT_BUTTON = By.XPATH, '// *[ @ id = "content"] / div[1] / div / div / a'
    SAVE_BUTTON = By.XPATH, '// *[ @ id = "content"] / div[1] / div / div / button'
    SUBMIT_LOGIN_BUTTON = By.CSS_SELECTOR, "#form-login button"


    product_name = ProductGenerator.generate_product_name()
    product_meta_tag = ProductGenerator.generate_meta_tag()
    product_product_model = ProductGenerator.generate_product_model()
    product_keyword = ProductGenerator.generate_product_model()

    def login_admin(self, username, password):
        self.input_value(self.LOGIN_INPUT, username)
        self.input_value(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_LOGIN_BUTTON)
        return self

    def wait_logout_button(self):
        self.get_element(self.LOGOUT_LINK)
        return self

    def click_logout_button(self):
        self.get_element(self.LOGOUT_LINK)
        self.click(self.LOGOUT_LINK)
        return self

    def wait_form_login(self):
        self.get_element(self.FORM_LOGIN)
        return self

    def open_products(self):
        self.click(self.CATALOG)
        self.get_element(self.PRODUCTS_LINK)
        self.click(self.PRODUCTS_LINK)
        return self

    def click_on_add_product(self):
        self.click(self.ADD_PRODUCT_BUTTON)
        return self

    def fill_form_new_product(self):
        self.input_value(self.NAME_INPUT, self.product_name)
        self.input_value(self.META_TAG_INPUT, self.product_meta_tag)
        self.click(self.DATA_TAB)
        self.get_element(self.MODEL_INPUT)
        self.input_value(self.MODEL_INPUT, self.product_product_model)
        self.click(self.SEO_TAB)
        self.get_element(self.KEYWORD_INPUT)
        self.input_value(self.KEYWORD_INPUT, self.product_keyword)
        return self

    def save_form(self):
        self.click(self.SAVE_BUTTON)
        return self

    def check_added_success(self):
        el = self.get_element(self.ALERT)
        self.check_text(el, "Success: You have modified products!")
        return self