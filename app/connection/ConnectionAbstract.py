import abc


class ConnectionAbstract(abc.ABC):
    def connect(self) -> bool:
        raise NotImplementedError

    def disconnect(self) -> bool:
        raise NotImplementedError
