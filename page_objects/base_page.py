import logging
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser, wait=3):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)
        self.actions = ActionChains(browser)
        self.__config_logger()

    def __config_logger(self, to_file=False):
        self.logger = logging.getLogger(type(self).__name__)
        os.makedirs("logs", exist_ok=True)
        if to_file:
            self.logger.addHandler(
                logging.FileHandler(f"logs/{self.browser.test_name}.log")
            )
        log_level = getattr(self.browser, "log_level", logging.INFO)
        self.logger.setLevel(level=log_level)

    def _text_xpath(self, text):
        return f"//*[text()='{text}']"

    def get_element(self, locator: tuple[str, str], timeout=3):
        self.logger.info(f"Search element on {locator}")
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_elements(self, locator: tuple[str, str], timeout=3):
        self.logger.info(f"Search elements on {locator}")
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def click(self, locator: tuple[str, str]):
        self.logger.info(f"Click {locator}")
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(
            0.3
        ).click().perform()

    def input_value(self, locator: tuple[str, str], text: str):
        self.logger.info(f"Input '{text}' into {locator}")
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)

    def wait_until_element_is_not_visible(self, locator: tuple[str, str], timeout=10):
        self.logger.info(f"Search element on {locator}")
        return WebDriverWait(self.browser, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def check_text(self, element, expected_title=""):
        self.logger.info(f"Compare text {element.text} with text {expected_title}")
        if element is None:
            raise ValueError("Element is None. Unable to check text.")

        assert element.text == expected_title, (
            f"Expected '{expected_title}', but got '{element.text}'"
        )
