import json
from typing import List, Callable, Type, Union
from argument_manager import ArgumentManager
import pandas as pd
from data_collector import DataCollector
from utils.file_format import FileFormat
from file_writers.json_file_writer import JsonFileWriter
from file_writers.csv_file_writer import CsvFileWriter
from file_writers.file_writer import FileWriter


class Crawler:

    def __init__(self, argument_manager: ArgumentManager):
        self.argument_manager = argument_manager

    @staticmethod
    def get_file_writer(file_format: FileFormat) -> Type[CsvFileWriter | JsonFileWriter]:
        writers = {
            FileFormat.CSV: CsvFileWriter,
            FileFormat.JSON: JsonFileWriter
        }
        return writers[file_format]

    def _save_to_csv(self, data):
        df = pd.DataFrame(data)
        df.to_csv(self.argument_manager.output, index=False)

    def _save_to_json(self, data):
        with open(self.argument_manager.output, "w", encoding='utf8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)

    def save(self, data: List[dict]):
        writer = self.get_file_writer(self.argument_manager.format)
        writer.save(self.argument_manager.output, data)

    def crawl(self):
        data_collector = DataCollector()
        data_collector.get_page_data(self.argument_manager.page)
        self.save(link_tree.data)


