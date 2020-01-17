from typing import Any
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
# Only to get contextual help from the IDEs
from selenium.webdriver.firefox.webdriver import WebDriver


class WebDriverWrapper:
    """Higher abstraction wrapper for selenium.webdriver"""

    def __init__(self, webdriver: WebDriver):
        self.driver = webdriver

    def get(self, page_path: str) -> None:
        self.driver.get(page_path)

    def finish(self) -> None:
        self.driver.quit()

    def send_keys_as_action(self, *keys_to_send: Any) -> None:
        # Replace CMD button with CONTROL for non-mac os.
        if keys_to_send[0] is Keys.COMMAND and not _is_darwin_os():
            keys_to_send = (Keys.CONTROL, *keys_to_send[1:])
        ActionChains(self.driver).send_keys(*keys_to_send).perform()

    def wait_for_element_visible(self, element: WebElement, wait_time: int = 5) -> None:
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(expected_conditions.visibility_of(element))


def _is_darwin_os() -> bool:
    # Is OsX ?
    from sys import platform
    return True if platform == 'darwin' else False
