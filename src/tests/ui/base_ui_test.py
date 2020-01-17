from enum import Enum
from src.tests.base_test import BaseTest
import src.tests.ui as tests_dir
import os, inspect


class BrowserSize(Enum):
    mobile = (400, 900)
    desktop = (1200, 900)

class BaseUiTest(BaseTest):
    def setUp(self) -> None:
        super().setUp()
        self.prepare_preconditions()
        # More will come here later

    def tearDown(self) -> None:
        super().tearDown()
        # More will come here later

    def prepare_preconditions(self) -> None:
        pass

    @property
    def test_case_name(self) -> str:
        return self.__class__.__name__

    @property
    def screen_size(self) -> BrowserSize:
        return BrowserSize.desktop

    @property
    def test_suite_name(self) -> str:
        current_class_file_directory = os.path.dirname(inspect.getfile(self.__class__))
        relative_directory = os.path.dirname(tests_dir.__file__)
        return os.path.relpath(current_class_file_directory, relative_directory)
