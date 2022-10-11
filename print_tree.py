from management.argument_manager import ArgumentManager
from crawler.data_collector import DataCollector
from urls.link_tree import LinkTree
import sys
import asyncio


async def main(argv):
    argument_manager = ArgumentManager(argv)
    data_collector = DataCollector()
    link_tree = LinkTree()
    page_data = await data_collector.get_page_data(argument_manager)
    page_data = [page.to_representation() for page in page_data]
    link_tree.print_tree(page_data)


if __name__ == '__main__':
    asyncio.run(main(sys.argv[1:]))
