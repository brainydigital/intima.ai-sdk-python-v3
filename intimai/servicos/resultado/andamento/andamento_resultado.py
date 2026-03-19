from intimai.servicos.resultado.servico_resultado import ServicoResultado
from intimai.servicos.endpoint import EndpointMixin


class AndamentoResultado(ServicoResultado, EndpointMixin):
    def __init__(self, id: int | str, id_processo: int | str = None):
        self._id = id
        self._id_processo = id_processo

    def get_endpoint(self) -> str:
        if self._id_processo is None:
            return f'{self.ANDAMENTO_ENDPOINT}/{self._id}{self.RESULTADO_ENDPOINT}'
        return f'{self.ANDAMENTO_ENDPOINT}/{self._id}{self.RESULTADO_ENDPOINT}/{self._id_processo}'
