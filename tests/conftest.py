import pytest
import os

from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--base_url", action="store", default="http://192.168.0.2:8081", help="Укажите базовый URL Opencart")


@pytest.fixture(scope="module")
def browser(request):
    browser = request.config.getoption("--browser").lower()
    base_url = request.config.getoption("--base_url")

    driver = None
    if browser == "chrome":
        print(f"Запуск Chrome с базовым URL: {base_url}")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print(f"Запуск Firefox с базовым URL: {base_url}")
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Неизвестный браузер: {browser}")

    driver.base_url = base_url
    yield driver
    print("Закрытие браузера...")
    if driver:
        driver.quit()

