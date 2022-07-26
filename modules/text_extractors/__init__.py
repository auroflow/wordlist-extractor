from abc import ABC, abstractmethod


class TextExtractor(ABC):
    @abstractmethod
    def get_text(self, filename: str) -> str:
        pass
