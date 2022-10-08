import sys
import getopt
from logger import Logger
from pathlib import Path


class ArgumentManager:

    def __init__(self):
        self._page = None
        self._format = 'csv'
        self._output = 'crawl-results.csv'

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value: str):
        self._page = value

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value: str):
        if not value in ('csv', 'json'):
            Logger.log_wrong_format_message()
            sys.exit(2)
        self._format = value

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value: str):
        path = Path(value)
        if self.format != path.suffix[1::]:
            Logger.log_help_message()
            sys.exit(2)
        self._output = value

    def save_arguments(self, argv) -> None:
        try:
            opts, args = getopt.getopt(argv, 'hp:f:o:', ['help', 'page=', 'format=', 'output='])
        except getopt.GetoptError:
            sys.exit(2)
        for opt, arg in opts:
            if opt in ('--h', '--help'):
                Logger.log_help_message()
                sys.exit()
            elif opt in ('--p', '--page'):
                self.page = arg
            elif opt in ('--f', '--format'):
                self.format = arg
            elif opt in ('--o', '--output'):
                self.output = arg
