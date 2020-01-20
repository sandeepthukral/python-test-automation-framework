import logging
import warnings

from selenium.webdriver.remote.remote_connection import LOGGER as SELENIUM_LOGGER


def start_logging() -> None:
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.getLogger('urllib3').setLevel(logging.ERROR)  # Reduce urllib logs.
    SELENIUM_LOGGER.setLevel(logging.WARNING)  # No info and debug logs.
    warnings.filterwarnings('ignore')  # Hide warnings logs
