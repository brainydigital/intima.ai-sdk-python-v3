from abc import ABC, abstractmethod


class ServicoResultado(ABC):
    @abstractmethod
    def get_endpoint(self) -> str: ...
