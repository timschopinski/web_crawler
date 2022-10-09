import sys
import getopt
from typing import List

from logger import Logger
from pathlib import Path
from utils.file_format import FileFormat
from urls.base_url import BaseUrl

class ArgumentManager:

    def __init__(self, argv):
        self.format = None
        self.output = None
        self._save_arguments(argv)

    @staticmethod
    def validate_format(value: str):
        valid_formats: List[FileFormat] = [FileFormat.CSV.value, FileFormat.JSON.value]
        return value in valid_formats

    def set_format(self, value: str):
        if self.validate_format(value):
            self.format = value
        else:
            Logger.log_wrong_format_message()
            sys.exit(2)

    def validate_output(self, value: str):
        path = Path(value)
        return self.format == path.suffix[1::]

    def set_output(self, value: str):
        if self.validate_output(value):
            self.output = value
        else:
            Logger.log_help_message()
            sys.exit(2)

    def _save_arguments(self, argv) -> None:
        try:
            opts, args = getopt.getopt(argv, 'hp:f:o:', ['help', 'page=', 'format=', 'output='])
        except getopt.GetoptError:
            sys.exit(2)
        for opt, arg in opts:
            if opt in ('--h', '--help'):
                Logger.log_help_message()
                sys.exit()
            elif opt in ('--p', '--page'):
                self.page = BaseUrl(arg)
            elif opt in ('--f', '--format'):
                self.set_format(arg)
            elif opt in ('--o', '--output'):
                self.set_output(arg)
