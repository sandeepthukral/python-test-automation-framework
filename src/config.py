import os
from enum import Enum


class ReporterType(Enum):
    console_reporter = 'console'


class ConfigUi:

    @staticmethod
    def reporter_type() -> ReporterType:
        reporter_type = os.environ.get('REPORTER', 'console')
        return ReporterType.from_string(reporter_type)

    @staticmethod
    def report_dir() -> str:
        return os.environ.get('REPORT_DIR', 'test_report')
