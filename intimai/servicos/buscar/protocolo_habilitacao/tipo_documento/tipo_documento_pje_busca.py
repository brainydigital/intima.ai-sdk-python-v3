from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class TipoDocumentoHabilitacaoPjeBusca(ServicoBusca, EndpointMixin):
    def __init__(self, id_autenticador: int | str):
        self._id_autenticador = id_autenticador

    def get_endpoint(self) -> str:
        return f'{self.PJE_ENDPOINT}{self.PROTOCOLO_HABILITACAO_ENDPOINT}/{self._id_autenticador}{self.TIPOS_DOCUMENTO_ENDPOINT}'
