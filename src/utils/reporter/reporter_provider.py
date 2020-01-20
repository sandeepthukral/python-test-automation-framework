from enum import Enum
from .console_reporter import ConsoleReporter


class ReporterType(Enum):
    allure = 'allure'
    console = 'console'

    @staticmethod
    def from_string(string: str) -> 'ReporterType':
        return ReporterType(string)


def get_reporter(reporter_type: ReporterType, reporter_dir: str) -> ConsoleReporter:
    if reporter_type == ReporterType.console:
        return ConsoleReporter(reporter_dir)
    raise ValueError(f'Reporter {reporter_type} is not available.')