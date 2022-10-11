from typing import List

from file_writers.file_writer import FileWriter
import pandas as pd


class CsvFileWriter(FileWriter):

    @classmethod
    def save(cls, output: str, data: List[dict]) -> None:
        try:
            df = pd.DataFrame(data)
            df.to_csv(output, index=False)
        except Exception as e:
            print(e)





