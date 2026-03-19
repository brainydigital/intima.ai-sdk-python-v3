from intimai.servicos.solicitar.servico_solicitacao import ServicoSolicitacao
from intimai.servicos.endpoint import EndpointMixin


class AndamentoSolicitacao(ServicoSolicitacao, EndpointMixin):
    def __init__(self, id: int | str):
        self._id = id

    def get_endpoint(self) -> str:
        return f'{self.ANDAMENTO_ENDPOINT}/{self._id}{self.SOLICITAR_ENDPOINT}'

    def get_request(self) -> dict:
        return {}
