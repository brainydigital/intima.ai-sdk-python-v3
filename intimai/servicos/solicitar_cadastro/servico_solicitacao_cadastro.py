from abc import ABC, abstractmethod


class ServicoSolicitacaoCadastro(ABC):
    @abstractmethod
    def get_endpoint(self) -> str: ...

    @abstractmethod
    def get_request(self) -> dict: ...
