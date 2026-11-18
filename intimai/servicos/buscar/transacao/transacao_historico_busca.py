from intimai.servicos.buscar.servico_busca import ServicoBusca
from intimai.servicos.endpoint import EndpointMixin


class TransacaoHistoricoBusca(ServicoBusca, EndpointMixin):
    def get_endpoint(self) -> str:
        return f'{self.TRANSACAO_ENDPOINT}{self.HISTORICO_ENDPOINT}'
