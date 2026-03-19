from intimai.servicos.resultado.servico_resultado import ServicoResultado
from intimai.servicos.endpoint import EndpointMixin


class EscutaResultado(ServicoResultado, EndpointMixin):
    def __init__(self, id: int | str):
        self._id = id

    def get_endpoint(self) -> str:
        return f'{self.ESCUTA_ENDPOINT}/{self._id}{self.RESULTADO_ENDPOINT}'
