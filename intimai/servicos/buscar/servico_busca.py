from abc import ABC, abstractmethod


class ServicoBusca(ABC):
    @abstractmethod
    def get_endpoint(self) -> str: ...
