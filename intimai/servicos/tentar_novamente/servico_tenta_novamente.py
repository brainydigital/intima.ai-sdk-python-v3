from abc import ABC, abstractmethod


class ServicoTentaNovamente(ABC):
    @abstractmethod
    def get_endpoint(self) -> str: ...
