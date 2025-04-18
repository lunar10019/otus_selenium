import pytest
import os
import logging
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("tests.log"), logging.StreamHandler()],
    )
    return logging.getLogger(__name__)


logger = setup_logging()


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption(
        "--base_url",
        action="store",
        default="http://192.168.0.3:8081",
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        for fixture_name in item.fixturenames:
            if "browser" in fixture_name:
                browser = item.funcargs[fixture_name]
                try:
                    allure.attach(
                        browser.get_screenshot_as_png(),
                        name="screenshot_on_failure",
                        attachment_type=AttachmentType.PNG,
                    )
                    logger.error(
                        f"Тест упал, скриншот сохранён в отчёт. Ошибка: {rep.longrepr}"
                    )
                except Exception as e:
                    logger.error(f"Не удалось сделать скриншот: {str(e)}")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser").lower()
    base_url = request.config.getoption("--base_url")

    logger.info(f"Инициализация браузера {browser_name}")
    logger.info(f"Базовый URL: {base_url}")

    driver = None
    try:
        with allure.step(f"Запуск браузера {browser_name}"):
            if browser_name == "chrome":
                driver = webdriver.Chrome()
            elif browser_name == "firefox":
                driver = webdriver.Firefox()
            else:
                error_msg = f"Неизвестный браузер: {browser_name}"
                logger.error(error_msg)
                raise ValueError(error_msg)

            driver.maximize_window()
            driver.base_url = base_url
            logger.info(f"Браузер {browser_name} успешно инициализирован")

            driver.get(base_url)
            allure.attach(
                driver.get_screenshot_as_png(),
                name="start_screen",
                attachment_type=AttachmentType.PNG,
            )

            yield driver
    except Exception as e:
        logger.error(f"Ошибка при инициализации браузера: {str(e)}")
        allure.attach(
            f"Ошибка: {str(e)}",
            name="browser_init_error",
            attachment_type=AttachmentType.TEXT,
        )
        raise
    finally:
        if driver:
            logger.info(f"Завершение работы браузера {browser_name}")
            with allure.step(f"Закрытие браузера {browser_name}"):
                driver.quit()
