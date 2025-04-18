import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import random
import string


class UserGenerator:
    @staticmethod
    def generate_first_name(length=10):
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def generate_last_name(length=10):
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def generate_email(domain="example.com"):
        username_length = random.randint(5, 10)
        username = "".join(
            random.choices(string.ascii_lowercase + string.digits, k=username_length)
        )
        return f"{username}@{domain}"

    @staticmethod
    def generate_password(length=10):
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))


class RegistrationPage(BasePage):
    TITLE = By.CSS_SELECTOR, "#content > h1"
    CONTENT = By.ID, "content"
    INPUT_NEWSLETTER = By.ID, "input-newsletter"
    ACCOUNT_REGISTER = By.ID, "account-register"
    SIDEBAR = By.ID, "column-right"
    FIRST_NAME_INPUT = By.ID, "input-firstname"
    LAST_NAME_INPUT = By.ID, "input-lastname"
    EMAIL_INPUT = By.ID, "input-email"
    PASSWORD_INPUT = By.ID, "input-password"
    FORM_REGISTRATION = By.ID, "form-register"
    CONTINUE = By.XPATH, '//*[@id="form-register"]/div/button'
    TOGGLE = By.XPATH, '//*[@id="form-register"]/div/div/input'

    user_first_name = UserGenerator.generate_first_name()
    user_last_name = UserGenerator.generate_last_name()
    user_email = UserGenerator.generate_email()
    user_password = UserGenerator.generate_password()

    @allure.step("Проверяю заголовок")
    def check_title(self):
        el = self.get_element(self.TITLE)
        self.check_text(el, "Register Account")
        return self

    @allure.step("Проверяю отображение контента")
    def check_content(self):
        self.get_element(self.CONTENT)
        return self

    @allure.step("Проверяю отображение свитчера подписки")
    def check_subscribe_toggle(self):
        self.get_element(self.INPUT_NEWSLETTER)
        return self

    @allure.step("Проверяю отобржение кнопки регистрации")
    def check_account_register(self):
        self.get_element(self.ACCOUNT_REGISTER)
        return self

    @allure.step("Проверяю отображение сайдбара")
    def check_sidebar(self):
        self.get_element(self.SIDEBAR)
        return self

    @allure.step("Жду отображения формы регистрации")
    def wait_form_registration(self):
        self.get_element(self.FORM_REGISTRATION)
        return self

    @allure.step("Заполняю форму регистрации")
    def fill_form_registration(self):
        self.input_value(self.FIRST_NAME_INPUT, self.user_first_name)
        self.input_value(self.LAST_NAME_INPUT, self.user_last_name)
        self.input_value(self.EMAIL_INPUT, self.user_email)
        self.input_value(self.PASSWORD_INPUT, self.user_password)
        return self

    @allure.step("Соглашаюсь с политикой конфиденциальности")
    def privacy_policy_agree(self):
        self.click(self.TOGGLE)
        return self

    @allure.step("Нажимаю на кнопку регистрации")
    def register_button(self):
        self.click(self.CONTINUE)
        return self
