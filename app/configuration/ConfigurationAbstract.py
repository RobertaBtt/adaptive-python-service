from abc import ABC, abstractmethod


class ConfigurationAbstract(ABC):
    @abstractmethod
    def get(self, section: str, key: str):
        raise NotImplementedError

    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError
