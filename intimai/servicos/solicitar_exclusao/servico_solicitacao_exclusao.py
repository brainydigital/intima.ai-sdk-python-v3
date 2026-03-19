from abc import ABC, abstractmethod


class ServicoSolicitacaoExclusao(ABC):
    @abstractmethod
    def get_endpoint(self) -> str: ...
