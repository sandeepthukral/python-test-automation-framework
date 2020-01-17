from abc import ABC
from typing import List

from selenium.webdriver.common.keys import Keys

from src.page_objects.base_page_object import BasePageObject


class PageGoogleHome(BasePageObject, ABC):

    url = 'https://www.google.com'

    def search(self, query: str) -> None:
        selector_query = 'input[name="q"]'
        self.click(selector_query)
        self.input(selector_query, query)
        self.send_keys(Keys.ENTER)

    def get_link_texts(self) -> List[str]:
        selector = '#search h3'
        return self.get_elements_text(selector)
