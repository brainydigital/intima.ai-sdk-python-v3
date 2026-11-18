from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class TipoDocumentoMensagemGeralProjudiBusca(ServicoBusca, EndpointMixin):
    def __init__(self, id_autenticador: int | str):
        self._id_autenticador = id_autenticador

    def get_endpoint(self) -> str:
        return f'{self.PROJUDI_ENDPOINT}{self.PROTOCOLO_ENDPOINT}/{self._id_autenticador}{self.TIPOS_DOCUMENTO_MENSAGEM_GERAL_ENDPOINT}'
