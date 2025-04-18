import allure

from page_objects.login_page import LoginPage


@allure.title("Проверка заголовка")
def test_check_title(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    LoginPage(browser).check_title()


@allure.title("Проверка отображения контента")
def test_check_content(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    LoginPage(browser).check_content()


@allure.title("Проверка отображения поля Email")
def test_check_email_input(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    LoginPage(browser).check_email_input()


@allure.title("Проверка отображения поля Input")
def test_check_password_input(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    LoginPage(browser).check_password_input()


@allure.title("Проверка отображения кнопки логина")
def test_check_account_login(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/login")
    LoginPage(browser).check_account_login()
