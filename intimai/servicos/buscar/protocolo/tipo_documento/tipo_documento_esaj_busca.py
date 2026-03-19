from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class TipoDocumentoEsajBusca(ServicoBusca, EndpointMixin):
    def __init__(self, id_protocolo: int | str, id_classe: int | str = None):
        self._id_protocolo = id_protocolo
        self._id_classe = id_classe

    def get_endpoint(self) -> str:
        if self._id_classe is None:
            return f'{self.ESAJ_ENDPOINT}{self.PROTOCOLO_ENDPOINT}/{self._id_protocolo}{self.TIPOS_DOCUMENTO_ENDPOINT}'
        return f'{self.ESAJ_ENDPOINT}{self.PROTOCOLO_ENDPOINT}/{self._id_protocolo}{self.TIPOS_DOCUMENTO_ENDPOINT}/{self._id_classe}'
