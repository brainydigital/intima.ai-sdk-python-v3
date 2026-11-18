from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class CreditoConsumoMensalBusca(ServicoBusca, EndpointMixin):
    def get_endpoint(self) -> str:
        return f'{self.CREDITO_ENDPOINT}{self.CONSUMO_MENSAL_ENDPOINT}'
