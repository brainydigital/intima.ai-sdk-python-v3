from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class TipoDocumentoMensagemGeralHabilitacaoPjeBusca(ServicoBusca, EndpointMixin):
    def __init__(self, id_protocolo_habilitacao: int | str):
        self._id_protocolo_habilitacao = id_protocolo_habilitacao

    def get_endpoint(self) -> str:
        return f'{self.PJE_ENDPOINT}{self.PROTOCOLO_HABILITACAO_ENDPOINT}/{self._id_protocolo_habilitacao}{self.TIPOS_DOCUMENTO_MENSAGEM_GERAL_ENDPOINT}'
