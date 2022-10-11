

class Logger:

    @staticmethod
    def log_help_message() -> None:
        print('crawl.py --page <URL> --format <csv/json> --output <path_to_file> \nprint_tree.py --page <URL>')

    @staticmethod
    def log_wrong_format_message() -> None:
        print('Invalid Format.')
        Logger.log_help_message()

    @staticmethod
    def log_timout_error() -> None:
        print('Timeout error.')