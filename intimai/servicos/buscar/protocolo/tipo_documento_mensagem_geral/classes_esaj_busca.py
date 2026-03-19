from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class ClassesEsajBusca(ServicoBusca, EndpointMixin):
    def __init__(self, id_protocolo: int | str):
        self._id_protocolo = id_protocolo

    def get_endpoint(self) -> str:
        return f'{self.ESAJ_ENDPOINT}{self.PROTOCOLO_ENDPOINT}/{self._id_protocolo}{self.CLASSES_ENDPOINT}'
