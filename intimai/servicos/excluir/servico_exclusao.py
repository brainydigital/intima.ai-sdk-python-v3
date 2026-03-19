from abc import ABC, abstractmethod


class ServicoExclusao(ABC):
    @abstractmethod
    def get_endpoint(self) -> str: ...
