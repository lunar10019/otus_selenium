import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    TITLE = By.CSS_SELECTOR, "#form-login > h2"
    CONTENT = By.ID, "content"
    EMAIL_INPUT = By.ID, "input-email"
    PASSWORD_INPUT = By.ID, "input-password"
    ACCOUNT_LOGIN = By.ID, "account-login"

    @allure.step("Проверяю заголовок")
    def check_title(self):
        el = self.get_element(self.TITLE)
        self.check_text(el, "Returning Customer")
        return self

    @allure.step("Проверяю отображение контента")
    def check_content(self):
        self.get_element(self.CONTENT)
        return self

    @allure.step("Проверяю отображение поля Email")
    def check_email_input(self):
        self.get_element(self.EMAIL_INPUT)
        return self

    @allure.step("Проверяю отображение поля Password")
    def check_password_input(self):
        self.get_element(self.PASSWORD_INPUT)
        return self

    @allure.step("Проверяю отображение кнопки логина")
    def check_account_login(self):
        self.get_element(self.ACCOUNT_LOGIN)
        return self
