from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class TipoDocumentoEprocBusca(ServicoBusca, EndpointMixin):
    def __init__(self, id_protocolo: int | str, id_evento: int | str = None):
        self._id_protocolo = id_protocolo
        self._id_evento = id_evento

    def get_endpoint(self) -> str:
        if self._id_evento is None:
            return f'{self.EPROC_ENDPOINT}{self.PROTOCOLO_ENDPOINT}/{self._id_protocolo}{self.TIPOS_DOCUMENTO_ENDPOINT}'
        return f'{self.EPROC_ENDPOINT}{self.PROTOCOLO_ENDPOINT}/{self._id_protocolo}{self.TIPOS_DOCUMENTO_ENDPOINT}/{self._id_evento}'
