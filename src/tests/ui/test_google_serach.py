from src.page_objects.google_com.page_google_home import PageGoogleHome
from src.tests.ui.base_ui_test import BaseUiTest


class TestGoogleSearch(BaseUiTest):

    def prepare_preconditions(self) -> None:
        pass

    def test(self) -> None:
        # simple test searching on Google
        page = PageGoogleHome(self.webdriver)
        page.visit()
        page.search('python')
        assert 'Welcome to Python.org' in page.get_link_texts()