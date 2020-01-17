from abc import abstractmethod
from typing import Union, List

from selenium.webdriver.common.keys import Keys

from src.utils.webdriver.webdriver_wrapper import WebDriverWrapper


class BasePageObject(object):

    def __init__(self, webdriver: WebDriverWrapper):
        self._webdriver = webdriver

    @property
    @abstractmethod
    def url(self) -> str:
        pass

    @property
    @abstractmethod
    def host(self) -> str:
        return ''

    @property
    def path(self) -> str:
        return f'{self.host}{self.url}'

    # some standard methods

    def visit(self) -> None:
        print(f'Visiting {self.path}')
        self._webdriver.get(self.path)

    def click(self, selector: str) -> None:
        element = self._webdriver.driver.find_elements_by_css_selector(selector)[0]
        self._webdriver.wait_for_element_visible(element)
        element.click()

    def input(self, selector: str, text: str) -> None:
        element = self._webdriver.driver.find_elements_by_css_selector(selector)[0]
        self._webdriver.wait_for_element_visible(element)
        element.send_keys(text)

    def send_keys(self, *keys: Union[Keys, str]) -> None:
        self._webdriver.send_keys_as_action(keys)

    def get_elements_text(self, selector: str) -> List[str]:
        elements = self._webdriver.driver.find_elements_by_css_selector(selector)
        return [element.text for element in elements]
