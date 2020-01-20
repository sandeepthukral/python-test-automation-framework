import logging
import os
from abc import abstractmethod


class BaseReporter(object):

    def __init__(self, output_dir: str):
        self.output_dir = output_dir

    @abstractmethod
    def is_case_failed(self) -> bool:
        pass

    @abstractmethod
    def start_step(self, message: str) -> None:
        pass

    @abstractmethod
    def finish_step(self, error_type, error_message, error_traceback):  # type: ignore
        pass

    @abstractmethod
    def start_suite(self, suite_name: str) -> None:
        pass

    @abstractmethod
    def finish_suite(self) -> None:
        pass

    @abstractmethod
    def start_case(self, case_name: str, suite_name: str) -> None:
        pass

    @abstractmethod
    def finish_case(self) -> None:
        pass

    @abstractmethod
    def set_description(self, description: str) -> None:
        pass

    def _get_output_dir(self, make_if_not_exists: bool = True) -> str:
        """
        Get directory for reporter output.
        Returns (str): output directory
        """
        directory = os.path.join(self.output_dir, self.__class__.__name__)
        if make_if_not_exists:
            if os.path.isdir(directory):
                return directory
            try:
                os.makedirs(directory)
                logging.info(f'Output directory created: {directory}.')
            except OSError as msg:
                logging.info(f'Failed to make dir: {msg}')
                if not os.path.isdir(directory):
                    raise
        return directory

    def _clear_output_dir(self) -> None:
        directory = os.path.normpath(os.path.abspath(os.path.expanduser(os.path.expandvars(self._get_output_dir()))))
        if not os.path.isdir(directory):
            return
        # Delete all files in report directory
        for directory_file in os.listdir(directory):
            directory_file = os.path.join(directory, directory_file)
            if not os.path.isfile(directory_file):
                continue
            try:
                os.unlink(directory_file)
            except OSError as error:
                logging.error(f'Failed to unlink: {directory_file}. {error}')