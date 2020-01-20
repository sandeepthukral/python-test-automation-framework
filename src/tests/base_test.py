import unittest
from src.utils.cached_property import cached_property
from src.utils.webdriver.logging import start_logging
from src.utils.webdriver.webdriver_factory import WebdriverFactory
from src.utils.webdriver.webdriver_factory import BrowserName


class BaseTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        start_logging()

    def tearDown(self) -> None:
        super().tearDown()
        # More will come here later

    @cached_property
    def webdriver(self):
        """Use Webdriver if the test needs a real browser."""
        webdriver = WebdriverFactory.get(
            browser=BrowserName('chrome'),
            screen_size=self.screen_size.value
        )
        self.addCleanup(self.finish_webdriver)  # The order of cleanups is very important here.
        return webdriver

    def finish_webdriver(self) -> None:
        self.webdriver.finish()  # Close webdriver instance.
