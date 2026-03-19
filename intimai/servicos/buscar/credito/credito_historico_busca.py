from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class CreditoHistoricoBusca(ServicoBusca, EndpointMixin):
    def get_endpoint(self) -> str:
        return f'{self.CREDITO_ENDPOINT}{self.HISTORICO_ENDPOINT}{self.BUSCAR_ENDPOINT}'
