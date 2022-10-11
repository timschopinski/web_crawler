from utils.file_format import FileFormat
from file_writers.csv_file_writer import CsvFileWriter
from file_writers.json_file_writer import JsonFileWriter
from file_writers.file_writer import FileWriter
from typing import Type, List, Union


class FileManager:

    @staticmethod
    def _get_file_writer(file_format: FileFormat) -> FileWriter:
        writers = {
            FileFormat.CSV.value: CsvFileWriter,
            FileFormat.JSON.value: JsonFileWriter
        }
        return writers[file_format]

    def save(self, file_format: FileFormat, output: str, data: List[dict]) -> None:
        writer = self._get_file_writer(file_format)
        writer.save(output, data)
