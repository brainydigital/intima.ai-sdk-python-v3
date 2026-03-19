from abc import ABC, abstractmethod


class ServicoAtualizacao(ABC):
    @abstractmethod
    def get_endpoint(self) -> str: ...

    @abstractmethod
    def get_request(self) -> dict: ...
