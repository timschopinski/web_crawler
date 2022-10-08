from argument_manager import ArgumentManager
from crawler import Crawler
import sys


def main(argv):
    argument_manager = ArgumentManager()
    argument_manager.save_arguments(argv)
    crawler = Crawler(argument_manager)
    crawler.crawl()

if __name__ == '__main__':
    main(sys.argv[1:])
