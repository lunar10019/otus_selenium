import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class HomePage(BasePage):
    LOGO = By.ID, "logo"
    NAVBAR_MENU = By.ID, "narbar-menu"
    SEARCH = By.ID, "search"
    CONTENT = By.CSS_SELECTOR, "#content > h3"
    BUTTON_CART = By.ID, "header-cart"
    PRICE_NEW = (
        By.CSS_SELECTOR,
        "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > div > div > span.price-new",
    )
    CHANGED_PRICE_NEW = (
        By.CSS_SELECTOR,
        "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > div > div > span.price-new",
    )
    DROPDOWN = By.CLASS_NAME, "dropdown"
    FORM_CURRENCY = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2) > a"

    @allure.step("Проверяю контент")
    def check_content(self):
        el = self.get_element(self.CONTENT)
        self.check_text(el, "Featured")
        return self

    @allure.step("Проверяю отображение логотипа")
    def check_logo(self):
        self.get_element(self.LOGO)
        return self

    @allure.step("Проверяю отображение контента")
    def check_navbar(self):
        self.get_element(self.NAVBAR_MENU)
        return self

    @allure.step("Проверяю отображение поле 'Поиск'")
    def check_search(self):
        self.get_element(self.SEARCH)
        return self

    @allure.step("Проверяю отображение кнопки корзины")
    def check_button_cart(self):
        self.get_element(self.BUTTON_CART)
        return self

    @allure.step("Получаю первоночальную цену продукта")
    def get_first_price(self):
        return self.get_element(self.PRICE_NEW).text

    @allure.step("Получаю цену продукта после изменения валюты")
    def get_second_price(self):
        return self.get_element(self.CHANGED_PRICE_NEW).text

    @allure.step("Открываю выпадающий список")
    def click_on_dropdown(self):
        self.click(self.DROPDOWN)

    @allure.step("Меняю валюту")
    def click_on_form_currency(self):
        self.click(self.FORM_CURRENCY)

    @allure.step("Проверяю, что выпадающий список закрылся")
    def dropdown_is_not_visible(self):
        self.wait_until_element_is_not_visible(self.DROPDOWN)
