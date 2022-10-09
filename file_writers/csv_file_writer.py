from file_writers.file_writer import FileWriter
import pandas as pd

class CsvFileWriter(FileWriter):

    @classmethod
    def save(cls, output: str, data):
        try:
            df = pd.DataFrame(data)
            df.to_csv(output, index=False)
        except Exception as e:
            pass
        #  TODO: handle exception




