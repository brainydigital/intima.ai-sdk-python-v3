from intimai.servicos.resultado.servico_resultado import ServicoResultado
from intimai.servicos.endpoint import EndpointMixin


class AcaoResultado(ServicoResultado, EndpointMixin):
    def __init__(self, id: int | str):
        self._id = id

    def get_endpoint(self) -> str:
        return f'{self.ACAO_ENDPOINT}/{self._id}{self.RESULTADO_ENDPOINT}'
