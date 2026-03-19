from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class ConsultaPreAnaliseBusca(ServicoBusca, EndpointMixin):
    def __init__(self, id: int | str = None):
        self._id = id

    def get_endpoint(self) -> str:
        if self._id is None:
            return f'{self.CONSULTA_PRE_ANALISE_ENDPOINT}{self.BUSCAR_ENDPOINT}'
        return f'{self.CONSULTA_PRE_ANALISE_ENDPOINT}/{self._id}{self.BUSCAR_ENDPOINT}'
