import asyncio

from argument_manager import ArgumentManager
from crawler import Crawler
import sys


async def main(argv):
    argument_manager = ArgumentManager(argv)
    crawler = Crawler(argument_manager)
    await crawler.crawl()


if __name__ == '__main__':
    asyncio.run(main(sys.argv[1:]))
