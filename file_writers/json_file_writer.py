import json

from file_writers.file_writer import FileWriter


class JsonFileWriter(FileWriter):

    @classmethod
    def save(cls, output, data):
        try:
            with open(output, "w", encoding='utf8') as outfile:
                json.dump(data, outfile, indent=4, ensure_ascii=False)
        except:
            pass
        #  TODO: handle exceptions
