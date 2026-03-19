from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class EventosEprocBusca(ServicoBusca, EndpointMixin):
    def __init__(self, id_protocolo: int | str):
        self._id_protocolo = id_protocolo

    def get_endpoint(self) -> str:
        return f'{self.EPROC_ENDPOINT}{self.PROTOCOLO_ENDPOINT}/{self._id_protocolo}{self.EVENTOS_ENDPOINT}'
