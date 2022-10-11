from management.argument_manager import ArgumentManager
from crawler.data_collector import DataCollector
from file_writers.file_manager import FileManager


class Crawler:

    def __init__(self, argument_manager: ArgumentManager):
        self.argument_manager = argument_manager

    async def crawl(self):
        data_collector = DataCollector()
        file_manager = FileManager()
        page_data = await data_collector.get_page_data(self.argument_manager)
        page_data = [page.to_representation() for page in page_data]
        file_manager.save(self.argument_manager.format, self.argument_manager.output, page_data)



