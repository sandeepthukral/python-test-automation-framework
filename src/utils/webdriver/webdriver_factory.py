from enum import Enum
from typing import Optional, Tuple, Dict, Any, Union
from .webdriver_wrapper import WebDriverWrapper
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

PAGE_LOAD_TIMEOUT = 30
SELENOID_SCREEN_SIZE = (1200, 900)


class BrowserName(Enum):
    chrome = 'chrome'
    firefox = 'firefox'
    edge = 'edge'
    safari = 'safari'
    opera = 'opera'


class WebdriverFactory:

    @staticmethod
    def get(browser: BrowserName, screen_size: Optional[Tuple[int, int]]) -> WebDriverWrapper:
        driver = LocalDriver.get(browser)
        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        if screen_size:
            driver.set_window_size(screen_size[0], screen_size[1])
        return WebDriverWrapper(driver)


class LocalDriver:

    @staticmethod
    def get(browser: BrowserName) -> Union[webdriver.Chrome, webdriver.Firefox]:
        if browser == BrowserName.firefox:
            return webdriver.Firefox()
        elif browser == BrowserName.chrome:
            chrome_options = webdriver.ChromeOptions()
            return webdriver.Chrome(options=chrome_options)
        raise ValueError(f'Browser {browser} is not implemented.')
