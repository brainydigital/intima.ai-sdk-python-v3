from intimai.servicos.solicitar.servico_solicitacao import ServicoSolicitacao
from intimai.servicos.endpoint import EndpointMixin


class AcaoConfirmarConsultaSolicitacao(ServicoSolicitacao, EndpointMixin):
    def __init__(self, id: int | str):
        self._id = id

    def get_endpoint(self) -> str:
        return f'{self.ACAO_ENDPOINT}/{self._id}{self.CONFIRMAR_CONSULTA_ENDPOINT}'

    def get_request(self) -> dict:
        return {}
