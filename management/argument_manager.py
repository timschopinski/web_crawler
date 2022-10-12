import sys
import getopt
from typing import List

from logger.logger import Logger
from pathlib import Path
from utils.file_format import FileFormat
from urls.base_url import BaseUrl


class ArgumentManager:

    def __init__(self, argv):
        self.format = None
        self.output = None
        self.allow_redirects = False
        self.max_depth = 2
        self.timeout = 3
        self._save_arguments(argv)

    @staticmethod
    def _validate_format(value: str) -> bool:
        valid_formats: List[FileFormat] = [FileFormat.CSV.value, FileFormat.JSON.value]
        return value in valid_formats

    def _set_format(self, value: str) -> None:
        if self._validate_format(value):
            self.format = value
        else:
            Logger.log_wrong_format_message()
            sys.exit(2)

    def _validate_output(self, value: str) -> bool:
        path = Path(value)
        return self.format == path.suffix[1::]

    def _set_output(self, value: str) -> None:
        if self._validate_output(value):
            self.output = value
        else:
            Logger.log_help_message()
            sys.exit(2)

    def _set_max_depth(self, value: str):
        if value.isnumeric() and int(value) > 0:
            self.max_depth = int(value)

    def _set_timeout(self, value: str):
        if value.isnumeric() and int(value) > 0:
            self.timeout = int(value)

    def _save_arguments(self, argv) -> None:
        try:
            long_opts = ['help', 'allow_redirects', 'max_depth=', 'page=', 'format=', 'output=', "timeout="]
            opts, args = getopt.getopt(argv, 'hp:f:o:', long_opts)
        except getopt.GetoptError:
            sys.exit(2)
        for opt, arg in opts:
            if opt in ('--h', '--help'):
                Logger.log_help_message()
                sys.exit()
            elif opt in ('--p', '--page'):
                self.page = BaseUrl(arg)
            elif opt in ('--f', '--format'):
                self._set_format(arg)
            elif opt in ('--o', '--output'):
                self._set_output(arg)
            elif opt == '--allow_redirects':
                self.allow_redirects = True
            elif opt == '--max_depth':
                self._set_max_depth(arg)
            elif opt == '--timeout':
                self._set_timeout(arg)
