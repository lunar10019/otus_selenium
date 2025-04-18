import allure

from page_objects.registration_page import RegistrationPage


@allure.title("Проверка заголовка")
def test_check_title(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")
    RegistrationPage(browser).check_title()


@allure.title("Проверка отображения контента")
def test_check_content(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")
    RegistrationPage(browser).check_content()


@allure.title("Проверка отображения свитчера подписки")
def test_check_subscribe_toggle(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")
    RegistrationPage(browser).check_subscribe_toggle()


@allure.title("Проверка отображения кнопки регистрации")
def test_check_account_register(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")
    RegistrationPage(browser).check_account_register()


@allure.title("Проверка отображения сайдбара")
def test_check_sidebar(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")
    RegistrationPage(browser).check_sidebar()


@allure.title("Проверка регистрации")
def test_registration(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")
    RegistrationPage(browser).wait_form_registration()
    RegistrationPage(browser).fill_form_registration()
    RegistrationPage(browser).privacy_policy_agree()
    RegistrationPage(browser).register_button()
