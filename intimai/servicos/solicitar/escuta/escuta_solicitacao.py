from intimai.servicos.solicitar.servico_solicitacao import ServicoSolicitacao
from intimai.servicos.endpoint import EndpointMixin


class EscutaSolicitacao(ServicoSolicitacao, EndpointMixin):
    def __init__(self, id: int | str):
        self._id = id

    def get_endpoint(self) -> str:
        return f'{self.ESCUTA_ENDPOINT}/{self._id}{self.SOLICITAR_ENDPOINT}'

    def get_request(self) -> dict:
        return {}
