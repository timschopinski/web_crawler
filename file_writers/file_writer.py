from abc import ABC, abstractmethod
from typing import List


class FileWriter(ABC):

    @classmethod
    @abstractmethod
    def save(cls, output: str, data: List[dict]) -> None:
        pass
