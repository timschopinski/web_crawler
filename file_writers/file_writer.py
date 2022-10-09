from abc import ABC, abstractmethod


class FileWriter(ABC):

    @classmethod
    @abstractmethod
    def save(cls, output: str, data):
        pass
