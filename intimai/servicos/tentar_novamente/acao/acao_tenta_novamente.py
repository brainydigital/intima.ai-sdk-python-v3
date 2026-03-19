from intimai.servicos.tentar_novamente.servico_tenta_novamente import ServicoTentaNovamente
from intimai.servicos.endpoint import EndpointMixin


class AcaoTentaNovamente(ServicoTentaNovamente, EndpointMixin):
    def __init__(self, id: int | str):
        self._id = id

    def get_endpoint(self) -> str:
        return f'{self.ACAO_ENDPOINT}/{self._id}{self.TENTAR_NOVAMENTE_ENDPOINT}'
