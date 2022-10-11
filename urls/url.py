from abc import ABC, abstractmethod


class Url(ABC):

    @abstractmethod
    def to_string(self) -> str:
        pass



