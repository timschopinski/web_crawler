from utils.file_format import FileFormat
from file_writers.csv_file_writer import CsvFileWriter
from file_writers.json_file_writer import JsonFileWriter
from typing import Type, List


class FileManager:

    @staticmethod
    def _get_file_writer(file_format: FileFormat) -> Type[CsvFileWriter | JsonFileWriter]:
        writers = {
            FileFormat.CSV.value: CsvFileWriter,
            FileFormat.JSON.value: JsonFileWriter
        }
        return writers[file_format]

    def save(self, file_format: FileFormat, output: str, data: List[dict]):
        writer = self._get_file_writer(file_format)
        writer.save(output, data)
