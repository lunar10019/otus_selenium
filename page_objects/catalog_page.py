import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    TITLE = By.CSS_SELECTOR, "#content > h2"
    CONTENT = By.ID, "content"
    DISPLAY_CONTROL = By.ID, "display-control"
    INPUT_SORT = By.ID, "input-sort"
    SIDEBAR = By.ID, "column-left"
    PRICE_NEW = (
        By.CSS_SELECTOR,
        "#product-list > div:nth-child(1) > div > div.content > div > div > span.price-new",
    )
    CHANGED_PRICE_NEW = (
        By.CSS_SELECTOR,
        "#product-list > div:nth-child(1) > div > div.content > div > div > span.price-new",
    )
    DROPDOWN = By.CLASS_NAME, "dropdown"
    FORM_CURRENCY = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2) > a"

    @allure.step("Проверяю заголовок")
    def check_title(self):
        el = self.get_element(self.TITLE)
        self.check_text(el, "Desktops")
        return self

    @allure.step("Проверяю отображение контента")
    def check_content(self):
        self.get_element(self.CONTENT)
        return self

    @allure.step("Проверяю отображение панели фильтров")
    def check_display_control(self):
        self.get_element(self.DISPLAY_CONTROL)
        return self

    @allure.step("Проверяю отображение элементов сортировки")
    def check_input_sort(self):
        self.get_element(self.INPUT_SORT)
        return self

    @allure.step("Проверяю отображение сайдбара")
    def check_sidebar(self):
        self.get_element(self.SIDEBAR)
        return self

    @allure.step("Получаю первоначальную цену продукта")
    def get_first_price(self):
        return self.get_element(self.PRICE_NEW).text

    @allure.step("Получаю цену продукта после смены валюты")
    def get_second_price(self):
        return self.get_element(self.CHANGED_PRICE_NEW).text

    @allure.step("Нажимаю на выпадающий список")
    def click_on_dropdown(self):
        self.click(self.DROPDOWN)

    @allure.step("Нажимаю на список валют")
    def click_on_form_currency(self):
        self.click(self.FORM_CURRENCY)

    @allure.step("Проверяю, что выпадающий список закрылся")
    def dropdown_is_not_visible(self):
        self.wait_until_element_is_not_visible(self.DROPDOWN)
