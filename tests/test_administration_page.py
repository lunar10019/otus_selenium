import allure

from page_objects.admin_page import AdminPage


@allure.title("Логин в админку")
def test_login(browser):
    browser.get(f"{browser.base_url}/administration")
    AdminPage(browser).wait_form_login()
    AdminPage(browser).login_admin("user", "bitnami")
    AdminPage(browser).wait_logout_button()
    AdminPage(browser).click_logout_button()
    AdminPage(browser).wait_form_login()


@allure.title("Добавление нового продукта")
def test_add_new_product(browser):
    browser.get(f"{browser.base_url}/administration")
    AdminPage(browser).wait_form_login()
    AdminPage(browser).login_admin("user", "bitnami")
    AdminPage(browser).open_products()
    AdminPage(browser).click_on_add_product()
    AdminPage(browser).fill_form_new_product()
    AdminPage(browser).save_form()
