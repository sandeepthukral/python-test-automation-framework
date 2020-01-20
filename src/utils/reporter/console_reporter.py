import logging
import os
from enum import Enum

from src.utils.reporter.base_reporter import BaseReporter


class Colors(Enum):
    header = '\033[95m'
    info = '\033[94m'
    success = '\033[32m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'


class ConsoleReporter(BaseReporter):
    current_suite: str
    current_test_case: str
    current_step_message: str

    def __init__(self, output_dir: str):
        super(ConsoleReporter, self).__init__(output_dir)
        self._clear_output_dir()
        self.case_failed = False
        # Set custom logging formatter.
        formatter = ConsoleFormatter()
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        # Clear existing handlers.
        logging.root.handlers = []
        logging.root.addHandler(handler)
        logging.root.setLevel(logging.DEBUG)

    def is_case_failed(self) -> bool:
        # TODO: Need to implement this method.
        return self.case_failed

    def start_suite(self, suite_name: str) -> None:
        self.current_suite = suite_name
        self.console_print(f'Start Test Suite: {suite_name}.', Colors.warning)

    def finish_suite(self) -> None:
        self.console_print(f'Finish Test Suite: {self.current_suite}.')

    def start_case(self, case_name: str, suite_name: str) -> None:
        self.case_failed = False
        self.current_test_case = case_name
        self.start_suite(suite_name)
        self.console_print(f'Start Test Case: {case_name}.', Colors.header)

    def finish_case(self) -> None:
        self.console_print(f'Finish Test Case: {self.current_test_case}', Colors.header)

    def start_step(self, message: str) -> None:
        self.current_step_message = message
        self.console_print(f'Step Begin: {self.current_step_message}.', Colors.success)

    def finish_step(self, error_type, _error_message, _error_traceback):  # type: ignore
        color = Colors.success
        result = 'success'
        if error_type is not None:
            self.case_failed = True
            color = Colors.fail
            result = 'fail'
        self.console_print(f'Step Finish ({result}): {self.current_step_message}.', color)

    def console_print(self, message: str, color: Colors = Colors.info) -> None:
        logging.info(message, extra={'color': color})

    def set_description(self, description: str) -> None:
        self.console_print(f'Case description: {description}', Colors.info)


class ConsoleFormatter(logging.Formatter):

    def __init__(self) -> None:
        super().__init__(fmt='%(asctime)s: %(message)s', datefmt='%H:%M:%S')
        self.is_tty = 'IDE_RUN' in os.environ

    def format(self, record: logging.LogRecord) -> str:  # noqa: A003
        result = logging.Formatter.format(self, record)
        if not self.is_tty:
            return result
        color = getattr(record, 'color', Colors.info)
        return f'{color.value}{result}{Colors.end.value}'