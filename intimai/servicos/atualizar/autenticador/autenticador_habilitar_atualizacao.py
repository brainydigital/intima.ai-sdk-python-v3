from intimai.servicos.atualizar.servico_atualizacao import ServicoAtualizacao
from intimai.servicos.endpoint import EndpointMixin


class AutenticadorHabilitarAtualizacao(ServicoAtualizacao, EndpointMixin):
    def __init__(self, id: int | str):
        self._id = id

    def get_endpoint(self) -> str:
        return f'{self.AUTENTICADOR_ENDPOINT}/{self._id}{self.HABILITAR_ENDPOINT}'

    def get_request(self) -> dict:
        return {}
