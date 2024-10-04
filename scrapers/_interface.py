from abc import ABC, abstractmethod

class IScraper(ABC):
    @abstractmethod
    def get_state(self):
        pass